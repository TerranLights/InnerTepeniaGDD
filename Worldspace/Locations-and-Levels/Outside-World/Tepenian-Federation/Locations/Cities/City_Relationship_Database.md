# Tepenian City Relationship Database

**Purpose:** Consistency reference for written lore — journal entries, audio logs, terminal entries, transit logs, shipping manifests, NPC dialogue, etc. Cross-check any city-to-city reference against this file to catch geographic, logistical, or network errors before they enter the game.

**Sources:** Three reference maps —
- Antarctica station/national possession map
- Antarctica/Tepenia Highway Map (with highway routes drawn over)
- Arcanet Regional Subnets map

---

## 1. Highway Quick Reference

All highways are pre-Long Night War infrastructure. Post-war, coastal sections are partially or fully non-operational. Inland sections (particularly those connecting Concordia, Byrd, Vostok, and the South Pole ruins) may still be functional or partially maintained.

**Corrected in full 2026-07-06** — the table below replaces an earlier version with multiple route errors (wrong termini, missing junctions, cities listed as main-line stops that are actually spur/connecting-road access, at least one highway — Hwy 37 — that was badly incomplete and out of order). See individual notes for what changed.

| Hwy # | Name | Nickname | Route Summary | Notes |
|---|---|---|---|---|
| **1** | Rothera Highway | "Palmer Highway" | Esperanza *(northern terminus)* → Marambio → *(ramp: road to Port Lockroy; boat to Palmer City)* → *(ramp: road to Rothera)* → Byrd *(western terminus)* | **Corrected 2026-07-06:** northern terminus is Esperanza, not Marambio; Port Lockroy, Palmer City, and Rothera are reached via connecting ramps rather than being main-line stops — Palmer City specifically requires a boat crossing from its ramp, not a road. Byrd end connects directly to Hwy 22's endpoint there. Western loop; only route connecting the Antarctic Peninsula to the rest of Tepenia. |
| **2** | Dumont Coast Highway | "DCH" | *(junction with Hwy 110)* → Casey → Dumont d'Urville | **Corrected 2026-07-06:** Cape Denison removed from this route — it belongs to Hwy 183 instead (see below). Western end is a junction with Hwy 110, not a bare starting point. Dumont d'Urville end connects directly to Hwy 183's endpoint there. Short coastal route along the Dumont d'Urville Sea. |
| **4** | Mawson-Sinheung Highway | — | The Sayowa Junction → Mawson → Sinheung → *(Shirayuki)* | **Corrected 2026-07-06:** substantially extended and reordered — previously just "Mawson → Shirayuki → Sinheung"; now runs the full Sayowa-to-Shirayuki stretch, with Sinheung and Shirayuki's order swapped. **Further corrected 2026-07-06, same day:** the western terminus is the Sayowa Junction, a three-way crossing (with Hwy 7-ext and Hwy 37) located near Sayowa rather than in the city itself, linked to Sayowa proper via the Sayowa Spur connecting road. The far end sits at a tri-junction connecting directly to both Hwy 110's and Hwy 22's endpoints. |
| **7** | Belgrano Highway | "Atlantic Highway" | Belgrano → Halley → Abowasa → *(ramp to Neumayer, between Abowasa and Sanay)* → Sanay → Troll → Lazar | Confirmed 2026-07-06, unchanged — does NOT pass through Neumayer directly; Neumayer's connector ramp sits between Abowasa and Sanay. |
| **7-ext** | Belgrano Highway Extension | — | Lazar → Princess Elisabeth → The Sayowa Junction | **Corrected 2026-07-06:** added the junction with Hwy 37 shortly before reaching Sayowa. **Further corrected 2026-07-06, same day:** the eastern terminus is the Sayowa Junction itself (where Hwy 4, Hwy 7-ext, and Hwy 37 genuinely converge), not Sayowa the city — the Sayowa Spur links the city to this junction. Built **2611–2614**; only highway with confirmed in-world construction dates. |
| **22** | Transcontinental Highway | — | Byrd *(Amundsen Sea end)* → South Pole (Amundsen Station) → *(junction with Hwy 175)* → *(dual-junction with Hwy 37, bidirectional)* → *(junction with Hwy 59)* → Zhongshan/Sinheung/Shirayuki tri-junction | **Corrected 2026-07-06:** added a dual-junction with Hwy 37 along the interior stretch; confirmed the eastern end is a genuine tri-junction connecting directly to both Hwy 4's and Hwy 110's endpoints. Byrd end connects directly to Hwy 1's endpoint. Cross-continent spine, West Antarctica to East Antarctic coast; still does not pass through Sayowa or Mawson directly. |
| **37** | Mountain Cut Throughway | — | The Sayowa Junction → Dome Fuji → *(dual-junction with Hwy 22, bidirectional)* → Kunlun → **Mountain Pass Airport** → Vostok → Concordia | **Corrected 2026-07-06 — this route was badly incomplete and out of order.** Dome Fuji is now a confirmed stop *(its own file's stale "no highway access" claim was fixed the same session — see `Specs/Dome_Fuji.md`)*. Kunlun and Vostok's order is reversed from the old listing. **Further corrected 2026-07-06, same day:** the northeastern terminus is the Sayowa Junction, not Sayowa the city — see Hwy 4/Hwy 7-ext notes above. **Also added, same day: Mountain Pass Airport**, a waypoint (not a city) between Kunlun and Vostok, confirmed via the developer's own airport-map reference as a genuine functional Tepenian airstrip — reasonably accessible to Kunlun, Dome Fuji, Amundsen Station (via the nearby Hwy 22 dual-junction), and Concordia to an extent. **Confirmed 2026-07-07: a joint Vostok-Kunlun venture that manufactured fabrication-synthesis chambers**, part of the nationwide Cradle infrastructure, shipped out via this same highway/airport network. **Historical, not current** — the outpost ran on residual overflow from Amundsen Tower's continent-wide regulated grid; the Tower's destruction ended that supply and the outpost's manufacturing capability permanently, though the facility is still standing, simply dark rather than destroyed. Concordia end connects directly to both Hwy 110's and Hwy 183's endpoints via the outer ring linking Concordia's Capricorn and Sagittarius districts. East Antarctic plateau traverse — not through the Transantarctic Mountains. |
| **59** | Atlantic Throughway | "Arcanet Line" | *(ramp with Hwy 7, between Halley and Abowasa)* → *(ramp with Hwy 22, farther from the South Pole than Hwy 175's ramp)* | **Corrected 2026-07-06:** Hwy 7 ramp specifically sits between Halley and Abowasa, not just "at Halley"; confirmed its Hwy 22 ramp is farther from the South Pole than Hwy 175's own ramp with Hwy 22. Connector highway, not a city-to-city road; also carries the Arcanet cable along its full length. |
| **110** | Coastal Cut Highway | — | Zhongshan → Davis → Mirny → Casey → Concordia | **Corrected 2026-07-06:** this is a genuine full route to Concordia as a real terminus, not an "inland spur from Casey" as previously described. Zhongshan end sits at a tri-junction with Hwy 4's and Hwy 22's endpoints; Concordia end connects directly to Hwy 37's and Hwy 183's endpoints via the outer ring linking Concordia's Capricorn and Sagittarius districts. Main East Antarctic coastal route. |
| **175** | Central Cut Throughway | — | *(ramp with Hwy 183, near Janbogo)* → *(ramp with Hwy 22, closer to the South Pole than Hwy 59's ramp)* | **Corrected 2026-07-06:** the Hwy 183 ramp is located near Janbogo, not near Concordia — Hwy 183 still junctions with Hwy 175, just much farther from Concordia than previously listed. Connects the Janbogo subnet region to the South Pole; its own Hwy 22 ramp sits closer to the Pole than Hwy 59's does. |
| **183** | Janbogo Highway | — | Concordia → *(junction with Hwy 175, near Janbogo)* → passes near Janbogo/Zukelli *(connecting road, not direct)* → passes near Cape Adare *(connecting road, not direct)* → Denison → Dumont d'Urville | **Corrected 2026-07-06 — this route was wrong.** Concordia end connects directly to Hwy 110's and Hwy 37's endpoints via the outer ring linking Concordia's Capricorn and Sagittarius districts. Janbogo, Zukelli, and Cape Adare are reached via connecting roads rather than being main-line stops — consistent with Fort McMurdo's and Scott's already-established spur-road access, which is unaffected by this correction. Denison is now confirmed on this route (moved from Hwy 2). Dumont d'Urville end connects directly to Hwy 2's endpoint there. |
| **Neumayer connector** | *(unnamed)* | — | Nearest safe point on Hwy 7 (between Abowasa and Sanay) → Neumayer | Small connector road; exact organization TBD |
| **Sayowa Spur** | The Sayowa Spur | — | The Sayowa Junction → Sayowa | **Added 2026-07-06.** A large, dedicated connecting road (not a minor ramp like the Neumayer connector) linking Sayowa proper to the Sayowa Junction — the genuine three-way crossing of Hwy 4, Hwy 7-ext, and Hwy 37. Added once Sayowa's own vision session established it as a real, physically developed industrial/residential city, not a place where the highway junction sits directly downtown. |

**Route to Byrd from Concordia:** Hwy 183 (via Janbogo/Zukelli, Cape Adare, Denison, or directly to the Hwy 175 junction near Janbogo) → Hwy 175 → junction with Hwy 22 → Hwy 22 (Amundsen Sea direction) → Byrd. Multiple transfers; a very long journey. *(Note re-confirmed 2026-07-06: the Hwy 175 junction sits near Janbogo, not right at Concordia's own end of Hwy 183, per the correction above.)*

**Hitchhiking, established 2026-07-05:** on a specific subset of highways, hitchhiking is a genuinely valid, established way to get around Tepenia — not a desperate last resort, but a normal travel option: **Hwy 7** (Belgrano Highway), **Hwy 4** (Mawson-Sinheung Highway), **Hwy 110** (Coastal Cut Highway), **Hwy 2** (Dumont Coast Highway), and a short segment of **Hwy 1** specifically between Marambio and Rothera. Exact in-world reasoning for why hitchhiking works on these particular routes (traffic density, cultural norms, freight-truck culture, something else) not yet developed — flagged for future design.

---

## 2. Arcanet Regional Subnets

Six subnets, each named after its hub city. **Official names** are the hub city names — used in Arcanet documentation, government records, and signage. **Colloquial nicknames** in quotes are informal regional terms, not official designations.

| Subnet | Hub | Colloquial Nickname | Member Cities |
|---|---|---|---|
| **Palmer** | Palmer City | "American" | Palmer City, Rothera, Esperanza, Marambio, Sejong, Juan Carlos, Port Lockroy, Signy* |
| **Halley** | Halley | "Atlantic" | Halley, Belgrano, Neumayer, Sanay, Troll, Abowasa, Lazar, Princess Elisabeth |
| **Mawson** | Mawson | *(none)* | Mawson, Sayowa, Dome Fuji *(Sinheung and Shirayuki moved to Mirny 2026-07-05 — see below)* |
| **Mirny** | Mirny | "Australian" | Mirny, Vostok, Kunlun, Casey, Zhongshan, Davis, Sinheung, Shirayuki *(latter two joined 2026-07-05 — real-world geography places the Larsemann Hills cluster far closer to Davis than to Mawson Station; see `TODO.md`)* |
| **Janbogo** | Janbogo | *(none)* | Janbogo, Fort McMurdo, Scott, Zukelli, Cape Adare, Dumont d'Urville, Cape Denison, Concordia |
| **Byrd** | Byrd | "Pacific" | Byrd *(Framheim and Little America removed from canon 2026-07-03 — see their Specs files; Byrd is now the subnet's only city)* |

**Signy\*:** Shown with a dashed border on the Arcanet map — peripheral/weaker connectivity, due to being on an island (South Orkney Islands) off the main peninsula. Treat as intermittent or lower-bandwidth in lore.

**Colloquial nickname note:** "American," "Atlantic," "Australian," and "Pacific" are informal terms — not official. Characters from non-matching cities within these subnets (e.g., Rothera in the "American" subnet, Mirny in the "Australian" subnet) may find their subnet's nickname inaccurate or mildly irritating. Mawson and Janbogo have no established colloquial nicknames.

**Amundsen Station (South Pole):** **Confirmed: inter-subnet relay — neutral ground; not a member of any subnet.** The South Pole was the routing node through which all six subnets communicated with each other. When the Long Night War destroyed Amundsen Station, it severed all inter-subnet Arcanet connections simultaneously, causing the **Planetary Split Brain** — each subnet became permanently isolated, developing its own version of historical records, sometimes in direct conflict with other subnets. The last synchronized pre-split Arcanet archive is cached at the South Pole ruins — the only place in Tepenia where the full unified record can be recovered. See Split Brain rules in Section 4.

---

## 3. City Profiles

Organized alphabetically. Each profile contains the data needed to verify lore consistency.

---

### Abowasa
- **Real stations:** Aboa Station (Finland) + Wasa Research Station (Sweden) — two genuinely separate facilities ~200m apart *(corrected 2026-07-05 — see `Specs/Abowasa.md`)*
- **Region:** Queen Maud Land / King Haakon VII Sea (Atlantic coast)
- **Status:** Damaged; partially operational *(corrected 2026-07-03 from "Destroyed" — resolved as a middle ground between conflicting sources; see `Specs/Abowasa.md`)*
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
- **Highways:** *(corrected 2026-07-14 — this entry previously hedged "Hwy 22 may also pass through — confirm against map" and omitted Hwy 59 entirely, despite both already being confirmed elsewhere in this same file's own highway table above and in `Specs/Amundsen_Station.md`)* a genuine three-highway node — Hwy 22 (Transcontinental Highway) passes directly through; Hwy 175 (Central Cut Throughway) terminates here; Hwy 59 (Atlantic Throughway/Arcanet Line) also terminates here, at a ramp farther from the Pole than Hwy 175's own ramp with Hwy 22
- **Direct highway neighbors:** Hwy 22 (Byrd, west / Zhongshan tri-junction, east), Hwy 175 (south toward the Hwy 183 junction / Ross Sea region), Hwy 59 (north toward Halley)
- **Notes:** Site of the Amundsen Tower (space elevator); destroyed by Upper Earth militaries; scrap confined to South Pole vicinity; last synchronized Arcanet archive is here; named after Roald Amundsen. **Proposed 2026-07-09** (Byrd's cross-reference pass): Hwy 22 passes directly through this site on Byrd's own eastern freight route to the rest of Tepenia — since that route is established as currently functioning, a maintained bypass through or around the debris field is proposed to exist and stay open, a fragile piece of infrastructure the whole eastern half of the country's supply chain depends on — see Byrd's entry above.

---

### Belgrano
- **Real station:** Belgrano Station II (Argentina) ✓
- **Region:** Weddell Sea coast (Atlantic)
- **Status:** Ruins (DLC 5) *(corrected 2026-07-03 from "Damaged; partially operational" — survived the Long Night War itself but became ruined in the subsequent period, per `Official_Population_Census.md`; distinct from cities destroyed outright during the war)*
- **Arcanet subnet:** Halley ("Atlantic")
- **Highways:** Hwy 7 (western terminus)
- **Direct highway neighbors:** Halley (east, Hwy 7)
- **Notes:** Western terminus of Hwy 7; Hwy 59 originates at Halley, not Belgrano — Belgrano reaches Hwy 59 via Hwy 7 to Halley; Hwy 7 bears the "Belgrano" name; the Extension (2611–2614) extends east from Lazar, not from Belgrano. **Coastal port receiving South African summer freighter shipments** (raw materials from Africa) as part of the seasonal Halley subnet supply window — see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`. **Proposed 2026-07-09** (Byrd's cross-reference pass): invented the Arrastradora/Rastra vehicle specifically to reach Byrd during the founding expedition; Byrd is proposed to still manufacture Rastra-descended freight haulers today, an unbroken lineage from Belgrano's own founding-era invention — see Byrd's entry above.

---

### Shirayuki
- **Real station:** Bharati Station (India) — infrastructure only; India's second Antarctic station, never occupied by an Indian exile population per established canon
- **Region:** Indian Ocean coast
- **Status:** Damaged; partially operational *(corrected 2026-07-03 from "Destroyed" — resolved consistently alongside Sinheung and Zhongshan as the three Larsemann Hills cluster cities; see `Specs/Shirayuki.md`)*
- **Arcanet subnet:** Mirny *(corrected 2026-07-05 — moved from Mawson; real-world geography places the Larsemann Hills cluster far closer to Davis (Mirny) than to Mawson Station. See `TODO.md`. Highway network unaffected — Hwy 4 remains a physical road independent of Arcanet subnet boundaries.)*
- **Highways:** Hwy 4 — eastern terminus *(corrected 2026-07-14 — this entry previously said "midpoint" with Sinheung to its east, contradicting the authoritative route in `Locations/Infrastructure/Highways.md` and `City_Relationship_Database.md`'s own top-of-file highway table, both of which place Shirayuki as Hwy 4's actual eastern endpoint, with Sinheung as the midpoint between Mawson and Shirayuki. This entry was apparently never updated during the 2026-07-06 Sayowa Junction correction, which the session's own notes list as having fixed only "Fort McMurdo's, Vostok's, and two summary notes" — not this entry.)*
- **Direct highway neighbors:** Sinheung (west, Hwy 4)
- **Notes:** Founding population resolved 2026-07-03 as Japanese, via a pre-exile diplomatic allocation by the International Court of Diplomacy at Jeju-do (an Upper Earth institution) — a deliberate balancing decision given Korea's existing footholds (Janbogo, Sejong) and China's ubiquitous presence, including immediately adjacent at Zhongshan. Named Shirayuki 2026-07-08. **Coastal port that received Australian freighter shipments** (raw materials, staged via Hobart/Fremantle), as part of the Hwy 4 coastal supply line (a physical logistics route, independent of the city's Mirny Arcanet subnet membership).

---

### Byrd
- **Real station:** Byrd Station (USA)
- **Region:** West Antarctica — inland
- **Status:** Survived — struggling (nature of struggle TBD)
- **Arcanet subnet:** Byrd ("Pacific") — **hub city**
- **Highways:** Hwy 1 (western/southern terminus, from the Antarctic Peninsula side only), Hwy 22 (western/Amundsen Sea terminus) *(corrected 2026-07-03 — Byrd is Hwy 1's terminus, not a pass-through point; the highway does not extend to the Ross Ice Shelf or Fort McMurdo at all, and never did — that claim, plus the supply-chain note below, predates this session's Hwy 1 route correction and referenced the now-removed Framheim/Little America besides)*
- **Direct highway neighbors:** Rothera (north, via Hwy 1, ultimately connecting to the whole Antarctic Peninsula chain), [Hwy 22 junction with Hwy 175 going east]
- **Notes:** Only surviving city besides Concordia; ~1,530m altitude — lower than Concordia (3,233m); West Antarctic location; DLC centerpiece (storyline TBD); hub of the Byrd ("Pacific") Arcanet subnet; NOT directly connected to Hwy 175 — reach via Hwy 22. Inland, not a port itself. Its only confirmed overland connection is Hwy 1 to the Antarctic Peninsula (via Rothera); it has no highway connection to the Ross Sea coastal ports at all. Its historical connection to Janbogo/Concordia was via the (now broken) aviation route, not any road — see `Specs/Byrd.md`.

**National supply-network connections, added 2026-07-09** — the project-wide cross-reference pass done for Byrd's Megasheet (`City_Megasheets/Byrd_Subnet/Byrd/Byrd_Cross_Reference_Synthesis.md`), included here since these connections cross subnet boundaries and belong in the consistency database, not just Byrd's own city folder:
- **The Cradle network:** Byrd is one of only two currently-active fabrication-synthesis chamber manufacturing sites nationwide (the other is Sinheung, Mirny subnet), building to a schematic designed at Neumayer (Halley subnet). Three subnets, one supply chain, no other established connection between them otherwise.
- **The Rastra lineage:** Belgrano (Halley subnet) invented the Arrastradora/Rastra vehicle specifically to reach Byrd during the founding expedition. Proposed: Byrd itself now manufactures Rastra-descended heavy freight haulers as part of its own fabrication output — the same vehicle lineage as the DLC 1 Rastra.
- **Hwy 1 corridor (north):** runs the full length of the Palmer subnet to Byrd's door (Esperanza → Marambio → Port Lockroy/Palmer City ramps → Rothera → Byrd). Rothera proposed as Byrd's natural manufacturing peer (both heavy-industry cities on the same route); Esperanza's Basque farming tradition proposed as Byrd's food supplier — a two-way trade corridor, not export-only.
- **Hwy 22 corridor (east):** runs the whole continent from Byrd through the Amundsen Station ruins to the Zhongshan/Sinheung/Shirayuki tri-junction (Mirny subnet), with further reach toward Mawson (Hwy 4), Concordia/Vostok/Kunlun/Dome Fuji (Hwy 37 dual-junction), and, more distantly, Janbogo (Hwy 175) and Halley subnet (Hwy 59). Proposed: since Byrd currently supplies "an enormous portion of the country," a maintained bypass through or around the Amundsen Station debris field must exist and stay open — a fragile, high-stakes piece of infrastructure in the same league as Troll Airfield or the Sayowa Junction.

See the full Byrd Megasheet for the complete reasoning behind each of these.

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
- **Highways:** Hwy 183 (Janbogo Highway) *(corrected 2026-07-13 — this entry still said "Hwy 2 (DCH) — eastern terminus," the pre-2026-07-06 assignment; the highway-network table above this per-city section (Hwy 2 and Hwy 183 rows) already had the correction, it just never propagated down to this entry)*
- **Direct highway neighbors:** Dumont d'Urville (north, via Hwy 183)
- **Notes:** Founded on Mawson's 1912 expedition base (Cape Denison); on Hwy 183 between the Cape Adare connecting road and Dumont d'Urville *(corrected 2026-07-13, matching the 2026-07-06 highway correction — previously said "eastern end of Dumont Coast Highway")*; destroyed Long Night War; Census I population: 522,975 humans / 543,168 robots / 1,066,143 combined *(corrected 2026-07-05 to match `Official_Population_Census.md`'s main City Populations table — this line had cited that same file's slightly different Section IV historical-note figures instead; that discrepancy between Section IV and the main table is itself still open, see `TODO.md`)*. **Dumont d'Urville Sea coastal port receiving Australian freighter shipments** (raw materials, staged via Hobart) — see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

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
- **Notes:** Three highway exits confirmed from city map; survived Long Night War due to inland position; French/Italian founding; Rastra tracked vehicles primary transport; full city logistics in `to-be-integrated/city-logistics/Concordia_City_Logistics.md`

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
- **Highways:** Hwy 37 ✓ *(corrected 2026-07-13 — Dome Fuji is a confirmed stop on Hwy 37 per `Locations/Infrastructure/Highways.md` and `Specs/Dome_Fuji.md`, both fixed 2026-07-06; this entry was never updated to match)*
- **Notes:** Japanese inland station; altitude too extreme for population growth; in Mawson subnet — connected via Arcanet cable, not road, but a real physical highway link exists via Hwy 37 (between the Sayowa Junction and Kunlun); an interior plateau highway crossing this distance doesn't make overland resupply practical, so the established aviation lifeline remains the real explanation for how Dome Fuji stayed supplied

---

### Dumont d'Urville
- **Real station:** Dumont d'Urville Station (France)
- **Region:** Dumont d'Urville Sea coast
- **Status:** Damaged; partially operational
- **Arcanet subnet:** Janbogo
- **Highways:** Hwy 2 (DCH) — eastern terminus; also the northern endpoint of Hwy 183, which connects directly to Hwy 2's own endpoint here *(corrected 2026-07-13 — previously listed only Hwy 2, with Denison attributed to that same highway; Denison was moved to Hwy 183 in the 2026-07-06 correction, making this city a genuine two-highway junction)*
- **Direct highway neighbors:** Casey (west, via Hwy 2), Cape Denison (south, via Hwy 183)
- **Notes:** Dumont d'Urville Sea named after this location/explorer; French station; major refugee source for Concordia (Dumont d'Urville Sea coast = primary refugee geography). **Primary Dumont d'Urville Sea port for Australian freighter shipments** (raw materials, staged via Hobart) — mirrors the real French IPEV logistics chain, which runs *L'Astrolabe* out of Hobart despite France being the founding/operating nation; see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

---

### Esperanza
- **Real station:** Esperanza Base (Argentina) ✓
- **Region:** Antarctic Peninsula — northern tip
- **Status:** Destroyed (Long Night War) *(corrected 2026-07-03 — was stale, contradicted 4 other sources including this city's own Specs file)*
- **Arcanet subnet:** Palmer ("American")
- **Highways:** Hwy 1 — northern peninsula section, added as a waypoint 2026-07-03 (Marambio → *(causeway)* → Trinity Peninsula mainland → Esperanza → Palmer City → Port Lockroy → Rothera → Byrd); real-world verification confirmed Esperanza (Hope Bay) sits only ~58km from Marambio's mainland causeway landing, genuinely on the way toward Palmer City, unlike Sejong/Juan Carlos's true island isolation
- **Direct highway neighbors:** Marambio (north, via causeway), Sejong (nearby, no highway — island-isolated), Palmer City (south via Hwy 1)
- **Notes:** Oldest continuously occupied Antarctic station in real life; historic families; northern peninsula cluster alongside Marambio, Sejong, Juan Carlos. **Proposed 2026-07-09** (Byrd's cross-reference pass): sits at Hwy 1's northern terminus and, given its established Basque agricultural tradition, is proposed as Byrd's food supplier along that same corridor — see Byrd's entry above.

---

### Fort McMurdo
- **Real station:** McMurdo Station (USA) ✓
- **Region:** Ross Sea — Ross Island
- **Status:** Damaged; partially operational
- **Arcanet subnet:** Janbogo
- **Highways:** Hwy 183, via spur/connecting road, not a main-line stop *(corrected 2026-07-03 — the "Hwy 1 eastern terminus" claim was wrong; Hwy 1's confirmed termini are Marambio and Byrd, both on the Antarctic Peninsula/West Antarctic side — it never reaches the Ross Sea side at all)*
- **Direct highway neighbors:** Scott (adjacent, shared spur access), Janbogo (north, via Hwy 183) — no highway connection to Byrd or West Antarctica; Byrd's only overland connection to the Ross Sea side runs the opposite way, via Hwy 22 → Hwy 175 → Hwy 183
- **Notes:** Largest Antarctic station in real life → largest pre-war Tepenian city; "Fort" = mining/resource-processing hub + deliberate reference to Fort MacMurray (Alberta, Canada); reached via a spur road across McMurdo Sound, not a direct Hwy 183 main-line stop — same spur-access pattern as Scott (see `Locations/Infrastructure/Highways.md`) *(corrected 2026-07-13 — this line's own leftover "two-highway junction" phrasing predated the 2026-07-03 Hwy 1 correction just above it and was never cleaned up)*; Scott directly adjacent; **does NOT connect to Hwy 37** — that route runs the Sayowa Junction → Dome Fuji → Kunlun → Vostok → Concordia on the East Antarctic plateau *(route corrected 2026-07-06)*. **Ross Sea coastal port receiving New Zealand freighter shipments** (raw materials) — see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

---

### Framheim — REMOVED FROM CANON (2026-07-03)
**No longer a Tepenian city.** Real-world verification found the Bay of Whales (the site Framheim and Little America were both reconstructed near) was entirely eliminated by the 1987 Iceberg B-9 calving event; with no surviving pre-exile infrastructure at either location to begin with, neither city had a physical basis left. Full reasoning and population disposition: `Official_Population_Census.md`'s removal note. **The Byrd↔Janbogo aviation refueling route (`Specs/Byrd.md`) still needs a fix, deliberately deferred pending a fuller options discussion (see `TODO.md`). The Hwy 1 land route does NOT need a fix — corrected 2026-07-03, it never actually passed through Framheim or Little America; that was a separate, unrelated error in this file (see the Hwy 1 highway-table entry, below).**

---

### Halley
- **Real station:** Halley Stations I–VI (UK) ✓
- **Region:** Weddell Sea coast — Brunt Ice Shelf (Atlantic)
- **Status:** Damaged; partially operational
- **Arcanet subnet:** Halley ("Atlantic") — subnet namesake, **not** the technical relay nexus *(corrected 2026-07-13 — this entry previously called Halley the "hub city," stale since the 2026-07-04 resolution that placed the subnet's actual Arcanet relay nexus at Sanay's stable bedrock instead, precisely because Halley's own floating ice shelf is too unstable for permanent critical infrastructure; see `Specs/Halley.md` and `Specs/Sanay.md`)*
- **Highways:** Hwy 7 (hub/midpoint), Hwy 59 (originates here — junction with Hwy 7) ✓
- **Direct highway neighbors:** Belgrano (west, Hwy 7), Abowasa (east, Hwy 7)
- **Notes:** Built on a **floating ice shelf** — the city literally moved over time; unique structural character no other Tepenian city shares; Hwy 59 (Arcanet cable line) originates at Halley and runs inland to Hwy 22's northern bend. *(Corrected 2026-07-13 — this line previously called Halley "hub port for South African summer freighter shipments" with "the most developed port infrastructure," directly contradicting established canon: Halley deliberately has no docks or airstrip of its own, precisely because the ice shelf's own motion would carry away any fixed maritime infrastructure. Belgrano and Sanay are the subnet's actual receiving ports; goods reach Halley overland via the Hwy 7 connector, whichever passage is open.)* See `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

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
- **Status:** Destroyed *(resolved 2026-07-05 — see `Specs/Juan_Carlos.md`)*
- **Arcanet subnet:** Palmer ("American")
- **Highways:** None — corrected 2026-07-03, resolving the flag from the same day's Marambio correction. Real-world verification confirmed Livingston Island sits 110km across the Bransfield Strait from the mainland Peninsula and 95.4km from Sejong on King George Island, both far too wide for any causeway/bridge (contrast Marambio's 0.93km Picnic Passage crossing). Juan Carlos has no highway connection at all — maritime/aviation access only.
- **Direct highway neighbors:** None (no highway access) — Esperanza, Marambio, and Sejong remain nearby Peninsula-cluster neighbors culturally and by shipping/aviation route, just not by road
- **Notes:** Spanish station, Livingston Island; northern peninsula cluster

---

### Kunlun
- **Real station:** Kunlun Station / Dome Argus (Sinian Federation — China)
- **Region:** East Antarctic plateau — inland (highest station)
- **Altitude:** 4,093m
- **Status:** Survived — too high altitude for viable large settlement
- **Arcanet subnet:** Mirny ("Australian")
- **Highways:** Hwy 37 ✓
- **Direct highway neighbors:** Dome Fuji (one direction, Hwy 37), Vostok (other direction, Hwy 37, via the Mountain Pass Airport waypoint) *(corrected 2026-07-13 — previously listed Vostok and Concordia; the same stale route order already fixed on `Highways.md`, `Specs/Vostok.md`, and this file's own Vostok entry back on 2026-07-06, but missed here)*
- **Notes:** Highest station in Antarctica; Sinian Federation origin; altitude too extreme for population growth; in Mirny subnet despite Sinian Federation ownership — subnets were organized geographically, not nationally; on Hwy 37 between Dome Fuji and Vostok

---

### Little America — REMOVED FROM CANON (2026-07-03)
**No longer a Tepenian city.** Same reasoning and consequences as Framheim, above.

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
- **Region:** Antarctic Peninsula — northern tip (Seymour Island)
- **Status:** Destroyed *(corrected 2026-07-03 from "Damaged" — Seymour Island is small and flat, built around one single concentrated strategic asset (the airfield), a single-point-of-failure target unlike Rothera's large, decentralizable Adelaide Island; see `Specs/Marambio.md`. **Updated 2026-07-13** — this predates the 2026-07-04 Vision Notes session establishing Marambio's equally-central shipyard/port identity alongside the airfield; the destruction eliminated both assets at once, not the airfield alone.)*
- **Arcanet subnet:** Palmer ("American")
- **Highways:** Hwy 1 — waypoint, not terminus *(corrected 2026-07-13 — this entry still said "northern terminus / origin," stale since 2026-07-06 when `Specs/Marambio.md` established Esperanza as Hwy 1's true northern terminus, with Marambio as a waypoint reached via the causeway/bridge chain described below)*
- **Direct highway neighbors:** Sejong, Juan Carlos (nearby, no highway — island-isolated); Esperanza (north via Hwy 1, across the causeway/bridge chain — Esperanza is the true northern terminus)
- **Notes:** Argentine Air Force station in real life; in-game a dual-mode logistics hub — one of only eight confirmed functional Tepenian airports, alongside an equally-important shipyard/port receiving from South America and shipping onward across the Weddell Sea *(corrected 2026-07-13 — previously described only the aviation role, predating the 2026-07-04 Vision Notes session that established the shipyard as equally central)*

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
- **Highways:** Hwy 4 (Mawson-Sinheung)
- **Direct highway neighbors:** the Sayowa Junction (west, via the Sayowa Spur), Sinheung (east, Hwy 4) *(corrected 2026-07-14 — this entry previously listed Shirayuki as the direct eastern neighbor, contradicting the authoritative route in `Locations/Infrastructure/Highways.md`, which places Sinheung immediately east of Mawson and Shirayuki as Hwy 4's actual eastern endpoint beyond it. Never updated during the 2026-07-06 Sayowa Junction correction — see Shirayuki's and Sinheung's own entries for the same gap.)*
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
- **Highways:** Unnamed connector road to nearest safe point on Hwy 7 (between Abowasa and Sanay) ✓
- **Direct highway neighbors:** None via Hwy 7 directly — connected only via connector road
- **Notes:** **NOT on Hwy 7** — Hwy 7 passes directly from Abowasa to Sanay; Neumayer is served by a small unnamed connector road branching off at the nearest geographically safe point; connector road organization TBD; this makes Neumayer slightly less accessible than other Hwy 7 cities. **Not a coastal receiving port** *(corrected 2026-07-14 — this line previously claimed Neumayer received South African summer freighter shipments; that was the same stale claim corrected out of `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md` during Halley's own bug-check pass on 2026-07-13, but this entry itself was missed at the time)*. Neumayer was never established as a receiving port; the Halley subnet's two actual coastal receiving ports for the seasonal South African freighter influx are Belgrano and Sanay — see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

---

### Palmer City
- **Real station:** Palmer Station (USA) ✓
- **Region:** Antarctic Peninsula — Anvers Island (64°46'S, 64°03'W)
- **Status:** Destroyed (Long Night War) — first settled, first destroyed
- **Arcanet subnet:** Palmer ("American") — **hub city**
- **Highways:** Hwy 1 — waypoint *(corrected 2026-07-03 — Palmer City is not Hwy 1's terminus; Marambio is the northern terminus, Byrd the western/southern terminus. Palmer City sits between Esperanza and Port Lockroy along the route, added the same day.)*
- **Direct highway neighbors:** Esperanza (north, Hwy 1), Port Lockroy (south, Hwy 1)
- **Notes:** First settled location in Tepenia (June 21, 2564); cultural and entertainment capital; 100 Miles Davis Blvd. is the first official address in Tepenia; most accessible from Upper Earth = first settled AND first heavily targeted; full lore in `Palmer_City.md`

---

### Port Lockroy
- **Real station:** Port Lockroy (UK) ✓
- **Region:** Antarctic Peninsula
- **Status:** Damaged; partially operational *(corrected 2026-07-03 from "Destroyed" — too strategically irrelevant (heritage/museum city, no military or industrial value) to be a priority target, and plausibly conflated with adjacent Palmer City's strike zone given direct highway proximity; see `Specs/Port_Lockroy.md`)*
- **Arcanet subnet:** Palmer ("American")
- **Highways:** Hwy 1 — passes through
- **Direct highway neighbors:** Palmer City (north), Rothera (south)
- **Notes:** Founded on UK historical expedition base; on Hwy 1 between Palmer City and Rothera; damaged, not destroyed, in the Long Night War *(corrected 2026-07-13 — this field still said "destroyed," directly contradicting the Status line above, corrected to "Damaged; partially operational" back on 2026-07-03 but never propagated to this Notes field in the same entry)*

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
- **Notes:** Highway named "Rothera Highway" first, "Palmer Highway" as nickname — suggests Rothera was the more significant city at the time of naming, or naming ran south to north. **Proposed 2026-07-09** (Byrd's cross-reference pass): Byrd's natural manufacturing peer via the Hwy 1 corridor, both heavy-industry cities on the same route — see Byrd's entry above.

---

### Sanay
- **Real station:** Sanae IV Station (South Africa)
- **Region:** Queen Maud Land / King Haakon VII Sea
- **Status:** Damaged; partially operational *(corrected 2026-07-03 from "Destroyed" — resolved as a middle ground; see `Specs/Sanay.md`)*
- **Arcanet subnet:** Halley ("Atlantic") — hosts the subnet's actual technical relay nexus *(added 2026-07-13 — this entry never carried the 2026-07-04 resolution: the nexus sits at Sanay's stable Vesleskarvet bedrock, built there by Halley's own residents' hands-on labor, while Halley keeps only the subnet's naming credit; see `Specs/Sanay.md` and `Specs/Halley.md`)*
- **Highways:** Hwy 7
- **Direct highway neighbors:** Abowasa (west, Hwy 7), Troll (east, Hwy 7)
- **Notes:** South African station; Queen Maud Land; Neumayer is nearby but on a connector road, not a direct Hwy 7 neighbor. One of the two Halley subnet coastal receiving ports (alongside Belgrano) for South African freighter shipments.

---

### Scott
- **Real station:** Scott Base (New Zealand)
- **Region:** Ross Sea — Ross Island (adjacent to McMurdo)
- **Status:** Damaged; partially operational
- **Arcanet subnet:** Janbogo
- **Highways:** Hwy 183, via spur/connecting road, not a main-line stop *(corrected 2026-07-13 — this entry still claimed "Hwy 1, eastern terminus," the exact same false claim already corrected in Fort McMurdo's own entry above on 2026-07-03; Hwy 1's confirmed termini are Marambio and Byrd, both on the Antarctic Peninsula/West Antarctic side — it never reaches the Ross Sea side at all)*
- **Direct highway neighbors:** Fort McMurdo (adjacent, shared spur access), Janbogo (north, via Hwy 183)
- **Notes:** Directly adjacent to Fort McMurdo on Ross Island; New Zealand station; reached via the same spur road as Fort McMurdo, not a Hwy 1 junction. **Ross Sea coastal port receiving New Zealand freighter shipments** (raw materials) — fittingly, given Scott's own real-world founding nation is New Zealand — see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

---

### Sejong
- **Real station:** King Sejong Station (Unified Korea)
- **Region:** Antarctic Peninsula — King George Island
- **Status:** Destroyed (Long Night War)
- **Arcanet subnet:** Palmer ("American")
- **Highways:** None — corrected 2026-07-03, same issue as Juan Carlos. Real-world verification confirmed King George Island sits 160-177km from the mainland Peninsula and from Marambio's causeway landing — far too wide for any bridge, same order of magnitude as Juan Carlos's isolation. `Specs/Sejong.md` already correctly said "TBD — maritime and aviation connections primary."
- **Direct highway neighbors:** None (no highway access) — Esperanza, Marambio, and Juan Carlos remain nearby Peninsula-cluster neighbors culturally and by shipping/aviation route, just not by road
- **Notes:** Named after King Sejong the Great (Hangul alphabet creator) — founded by South Korean exiles, but Sejong's own Korean population has since diluted to just 5.79%, its smallest Significant-tier nation, behind the USA's sole 21.65% Primary; a founding-era naming heritage shared with Janbogo, not a living Korean demographic tie (Tepenia's two genuine living Korean centers are Janbogo and Sinheung, Mirny subnet, 34.62% Primary) *(corrected 2026-07-13 — previously "Unified Korea's Antarctic presence alongside Janbogo," overstating present-day relevance and omitting Sinheung; see `Specs/Sejong.md`)*; King George Island = slightly off the peninsula proper

---

### Signy
- **Real station:** Signy Station (UK) ✓
- **Region:** South Orkney Islands (Atlantic Ocean — north of Antarctic Peninsula)
- **Status:** Survived; fully operational *(upgraded 2026-07-03 from "Damaged" — too remote and marginal for Upper Earth's forces to have struck directly; the war reached Signy indirectly instead, cutting supply lines and leaving its robot population facing a siligel shortage even though the human population can sustain itself on the Scotia Sea's marine resources; see `Specs/Signy.md`)*
- **Arcanet subnet:** Palmer ("American") — peripheral/dashed boundary
- **Highways:** None — maritime/air only ✓
- **Notes:** Northernmost Tepenian outpost; island location makes road connection impossible; Palmer subnet connection weak/intermittent (dashed border on Arcanet map); communications to/from Signy should reflect delays and dropouts in lore

---

### Sinheung
- **Real station:** Sinheung Station (Russia)
- **Region:** Indian Ocean coast
- **Status:** Damaged; partially operational *(corrected 2026-07-03 from "Destroyed" — Sinheung and Zhongshan sit at effectively identical real-world coordinates, only a few hundred meters apart; differing survival outcomes made no physical sense; resolved consistently alongside Zhongshan and the Larsemann Hills' Japanese city (now Shirayuki); see `Specs/Sinheung.md`)*
- **Arcanet subnet:** Mirny *(corrected 2026-07-05 — moved from Mawson, joining Zhongshan and Shirayuki in the Larsemann Hills cluster; real-world geography places it far closer to Davis (Mirny) than to Mawson Station. See `TODO.md`. Highway network unaffected — Hwy 4 remains a physical road independent of Arcanet subnet boundaries.)*
- **Highways:** Hwy 4 — midpoint *(corrected 2026-07-14 — this entry previously said "eastern terminus" with Shirayuki to its west, contradicting the authoritative route in `Locations/Infrastructure/Highways.md`, which places this city (Sinheung) as the midpoint between Mawson and Shirayuki, with Shirayuki as the actual eastern endpoint. Never updated during the 2026-07-06 Sayowa Junction correction — see Shirayuki's own entry above for the same gap.)*
- **Direct highway neighbors:** Mawson (west, Hwy 4), Shirayuki (east, Hwy 4)
- **Notes:** Between Mawson and Shirayuki on the Hwy 4 coastal link; Russian station. **Coastal port that received Australian freighter shipments** (raw materials, staged via Hobart/Fremantle) pre-destruction, as part of the Hwy 4 coastal supply line (a physical logistics route, independent of the city's Mirny Arcanet subnet membership). **Proposed 2026-07-09** (Byrd's cross-reference pass): the other currently-active Cradle chamber manufacturing site alongside Byrd, both building to Neumayer's schematic — see Byrd's entry above.

---

### Sayowa
- **Real station:** Syowa Station (Japan), East Ongul Island — genuinely offshore, ~4km from the mainland (confirmed via real-world research 2026-07-06)
- **Region:** Indian Ocean coast
- **Status:** Damaged; partially operational
- **Arcanet subnet:** Mawson
- **Highways:** **Corrected 2026-07-06** — Hwy 4 (western terminus of that highway) and Hwy 7-ext (eastern terminus) both meet Hwy 37's northeastern terminus at **the Sayowa Junction**, a genuine three-way crossing located near Sayowa rather than in the city itself; the Sayowa Spur (a large connecting road) links Sayowa proper to this junction. Sayowa itself is not directly on any of the three highways' main lines.
- **Direct highway neighbors:** via the Sayowa Junction and Spur — Mawson (Hwy 4), Princess Elisabeth (Hwy 7-ext), Dome Fuji (Hwy 37)
- **Notes:** **Major junction city, though the junction itself sits just outside town** — three highways converge at the Sayowa Junction from very different directions; Hwy 4 runs the Mawson-Sinheung industrial corridor, Hwy 7-ext connects westward to the full Atlantic coast highway system, Hwy 37 goes inland to Concordia via the plateau. Japanese station (JARE); **corrected 2026-07-06 — no longer Tepenia's primary Japanese demographic presence** (that's Shirayuki now, 36.27% Japan-Primary; Sayowa's own Japan share is diluted to 2.71%). **Vision session, 2026-07-06:** genuinely industrialized (fabrication, trucking & dispatch) as well as residential, not purely a junction waypoint. **Hwy 22 does not pass through Sayowa.** **Coastal port receiving Australian freighter shipments** (raw materials, staged via Hobart/Fremantle) as part of the Mawson subnet coastal supply line — see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`.

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
- **Direct highway neighbors:** Kunlun (one direction, Hwy 37), Concordia (other direction, Hwy 37) *(corrected 2026-07-06 — Sayowa itself is not directly on Hwy 37; the highway's northeastern terminus is the Sayowa Junction, near but not in Sayowa, reached via Dome Fuji first from that end)*
- **Notes:** Russian inland station; sits above subglacial Lake Vostok — one of the largest lakes on Earth, buried under the ice; on Hwy 37 between Kunlun and Concordia *(corrected 2026-07-13 — this previously said "between Sayowa and Kunlun," an even older, doubly-stale fragment that both omitted Dome Fuji and directly contradicted the correct neighbor line immediately above it)*; **NOT on Hwy 59**

---

### Zhongshan
- **Real station:** Zhongshan Station (Sinian Federation — China)
- **Region:** Indian Ocean coast / East Antarctica
- **Status:** Damaged; partially operational
- **Arcanet subnet:** Mirny ("Australian") — as of 2026-07-05, its Larsemann Hills neighbors Sinheung and Shirayuki have joined it here too (moved from Mawson subnet; see `TODO.md`)
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
- **Concordia is the only fully functioning major city.** Byrd survives but is struggling. Most coastal cities were destroyed or severely damaged during the Long Night War — fully destroyed cities include Palmer City, Marambio, Sejong, Casey, Denison, Cape Adare, Zukelli, Juan Carlos *(status resolved 2026-07-05 — see `Specs/Juan_Carlos.md`)*, and Amundsen Station. Princess Elisabeth is also destroyed (ruins with straggling survivors). Damaged but partially operational cities — retaining surviving sections and populations — include Port Lockroy, Sanay, Abowasa, Sinheung, Shirayuki, Zhongshan, and many others *(list corrected 2026-07-03 — several of these were previously miscategorized as destroyed in this same note)*. Signy is fully survived and untouched. Dome Fuji and Kunlun both received real population figures on 2026-07-04 (123,449 at Kunlun, entirely robot; 55,072 at Dome Fuji, entirely robot with nationality preserved) via a deliberate redistribution — *corrected from "never viable population centers," which was accurate before that date but is no longer true; see `Official_Population_Census.md`'s Kunlun/Dome Fuji redistribution note*. *(Kunlun's original single-nation-Chinese reclassification was superseded 2026-07-06 — its population is now a curated 19-nation space/astronomy/comms-heritage draw, same total.)*
- **Palmer City is on the Antarctic Peninsula** — as far from Concordia as any point in Antarctica. Palmer City refugees are rare in Concordia and traveled an exceptionally long way.
- **Janbogo is partially operational** — key link between Concordia and the outside world. Anything entering or leaving Concordia by ground passes through Janbogo.
- **Fort McMurdo and Scott are adjacent** on Ross Island — effectively twin cities, not distant settlements.
- **Amundsen Station (South Pole) is deep interior** — not coastal, not easily accessible, a major expedition destination.
- **Signy is an island** in the South Orkney Islands, north of the main continent. Travel to Signy is maritime only — no road connection exists.
- **Halley was on a floating ice shelf** — it moved. Characters from Halley would be aware their city literally drifted over time.
- **Sayowa is a major highway junction city** — the actual crossing point, **corrected 2026-07-06**, is the Sayowa Junction (a three-way convergence of Hwy 4, Hwy 7-ext, and Hwy 37), located near Sayowa rather than in it, linked to the city via the Sayowa Spur. In lore, it was a significant transfer point between the two sides of the continent.

### Network Rules
- **Arcanet subnet official names** are the hub city names (Palmer, Halley, Mawson, Mirny, Janbogo, Byrd). Colloquial nicknames ("American," "Atlantic," etc.) are informal — use official names in any formal in-world documentation.
- **Hwy 59 carries both road traffic and Arcanet cable** — physical damage to Hwy 59 disrupts Arcanet connectivity across the Halley subnet's inland connection. These consequences are simultaneous.
- **Signy's Arcanet connection was weak/intermittent** — communications to/from Signy should reflect delays, dropouts, and lower bandwidth.
- **Amundsen Station was the inter-subnet relay** — any cross-subnet Arcanet communication in lore set before the Long Night War would have been routed through the South Pole.

### Highway Rules
- **Hwy 1 is the only land route connecting the Antarctic Peninsula to the rest of Tepenia** — travel from Palmer City to Concordia by ground: Palmer → Hwy 1 → Byrd → Hwy 22 → Hwy 175 junction → Hwy 175 → Hwy 183 → Concordia. Extremely long journey.
- **Hwy 7 does NOT pass through Neumayer** — Neumayer is on a small unnamed connector road. Transit logs and travel accounts should reflect that Neumayer required a detour off the main highway.
- **The Belgrano Highway Extension was built 2611–2614** — lore set before 2611 cannot reference it; lore set 2611–2614 could reference construction; lore set after 2614 treats it as existing infrastructure.
- **Hwy 37 is an East Antarctic plateau route** — the Sayowa Junction → Dome Fuji → Kunlun → Vostok → Concordia *(corrected 2026-07-06 for both the Sayowa Junction distinction and the Kunlun/Vostok order)*. It does NOT cross the Transantarctic Mountains and does NOT connect to Fort McMurdo or the Ross Sea cities.
- **Hwy 183 has Concordia as its northern terminus** — travel from Concordia to the Ross Sea cities (Fort McMurdo, Janbogo, etc.) uses Hwy 183 south. Shipping logs between Concordia and the Ross Sea reference Hwy 183.
- **Hwy 59 does NOT reach the South Pole or Concordia** — it is a connector between Hwy 7 and the northern bend of Hwy 22, carrying Arcanet cable. It is not a city-to-city road.

---

## 5. Open Questions (for future resolution)

- ~~**Governmental capital of Tepenia**~~ **RESOLVED 2026-07-07: Fort McMurdo** (see `National_Capital_Candidates.md`) — Palmer City was cultural, not governmental.
- **Neumayer connector road** — exact organization, name, and which precise point on Hwy 7 it branches from (between Abowasa and Sanay, at nearest safe geographic point — details TBD)
- ~~**Hwy 22 at Amundsen Station** — does Hwy 22 pass through the South Pole, or does Hwy 175 connect to it at a point away from the South Pole? (confirm against map)~~ **RESOLVED 2026-07-03:** confirmed against `Reference-Images/Maps/Antarctica_highway_map_by_topology.jpeg` — Hwy 22 passes directly through the South Pole/Amundsen Station.
- ~~**Maitri rename** — city will be renamed in later documents; new name TBD~~ **RESOLVED 2026-07-03:** finalized as "Lazar" — see `Specs/Lazar.md` for the full two-settlement coalescence founding story.
- **Hwy 7 order between Belgrano and Abowasa** — confirmed: Belgrano → Halley → Abowasa; intermediate stops (if any) between Halley and Abowasa not yet verified
