# Cross-Subnet City Relationships

**Started 2026-07-20**, resolving the `TODO.md` "Cross-nation/cross-subnet city relationship check" item
(flagged 2026-07-17, explicitly deferred until now). **Goal, per the developer's own framing:** find real
ways cities relate to each other *across* subnets, not just within one, so that as the player discovers
lore, Tepenia reads as a genuinely interconnected country that happened to fracture into six mutually
isolated information environments (the Planetary Split Brain) — not six subnets that only ever shared a
landmass. Distinct from the City History Enhancement Opportunities pass (works within a city's own
history) and from existing subnet-internal relationship work already scattered across individual
Megasheets — this file is specifically hunting for connections that cross a subnet boundary, the same way
`City_Refugee_District_Affinities.md` mapped city-to-Concordia-district relationships.

**Working status: in progress, multi-session scope.** This file is the resumable source of truth — check
what's filled in vs. flagged before starting a new session on this thread.

**Method, in order of how concrete the evidence is:**
1. **Physical infrastructure** (highway/aviation network) — the most concrete, least invented basis;
   traced directly from `Locations/Infrastructure/Highways.md` and existing aviation-route lore.
2. **Already-established connections** — relationships already present in existing lore, cataloged here
   for the first time as a *cross-subnet* set rather than scattered across individual city files.
3. **Shared founding/Primary/Significant-tier nations across subnet boundaries** — pending data-gathering,
   see the checklist below.
4. **Real-world historical/expedition parallels** not yet dramatized in-world, surfaced by checking
   whether two cities' real-world namesakes had an actual historical relationship.

---

## Part 1 — Physical Infrastructure: The Highway Network as a Connectivity Map

Tracing every highway route in `Highways.md` for subnet-boundary crossings reveals a genuine national
topology, not a random scatter. Reproduced here specifically as a cross-subnet reference (the source file
itself is organized by highway number, not by what it connects).

### The country's actual shape, subnet to subnet

- **Palmer ↔ Byrd ↔ Mirny, one continuous corridor.** Hwy 1 (Esperanza → Marambio → Byrd) connects
  directly to Hwy 22 at Byrd, and Hwy 22 runs on through the South Pole to the Zhongshan/Sinheung/
  Shirayuki tri-junction in Mirny subnet. **Byrd's only overland link to the rest of the country runs
  through this single corridor in both directions** — it's simultaneously Palmer's only overland exit
  and Mirny's western approach to the Peninsula. This is the single most structurally important corridor
  in the whole network: three subnets (Palmer, Byrd, Mirny) share exactly one overland thread.
- **Mirny ↔ Janbogo, direct.** Hwy 2 runs Casey (Mirny) → Dumont d'Urville (Janbogo) with no
  intermediate subnet. A short, direct coastal link between two subnets that otherwise read as fairly
  distant from each other.
- **Halley ↔ Mawson ↔ Mirny ↔ Concordia, via the Sayowa Junction.** Hwy 7/7-ext (all of Halley subnet's
  own spine) terminates at the Sayowa Junction, which is also where Hwy 4 (→ Mawson → Sinheung, Mirny)
  and Hwy 37 (→ Dome Fuji, Mawson → Kunlun/Vostok, Mirny → Concordia) converge. **Every one of Halley
  subnet's 8 cities is, by road, one single junction away from Mawson, Mirny, and Concordia.** Mawson
  subnet — only 3 cities, the smallest subnet — sits structurally as the connective tissue joining
  Halley, Mirny, and Concordia together, matching Sayowa's own established "Point Where Three Roads
  Meet" civic identity almost exactly. Worth treating deliberately: Mawson's national importance is
  disproportionate to its population, purely as connective infrastructure.
- **Mirny ↔ Concordia, direct.** Hwy 110 runs the length of Mirny subnet (Zhongshan → Davis → Mirny →
  Casey) straight to Concordia.
- **Janbogo ↔ Concordia, direct.** Hwy 183 runs Concordia to Dumont d'Urville, passing the Janbogo
  region (via connecting roads to Janbogo, Zukelli, Cape Adare) and Denison directly.
- **Janbogo ↔ Byrd/South Pole corridor.** Hwy 175 (a connector, not a city-to-city road) links the
  Janbogo region directly to the same Hwy 22 corridor Byrd and Palmer depend on — a second, independent
  thread tying Janbogo into the Byrd/Palmer/Mirny corridor beyond just its Mirny link via Hwy 2.
- **Halley ↔ Byrd/South Pole corridor — and specifically the Arcanet.** Hwy 59, explicitly named "the
  Atlantic Throughway ('Arcanet Line')" in its own header, connects a ramp on Hwy 7 (between Halley and
  Abowasa) to a ramp on Hwy 22 near the South Pole, and **carries the Arcanet cable along its full
  length.** This is worth real attention: a physical, named trunk cable connecting Halley subnet directly
  to the Byrd/South Pole corridor is exactly the kind of infrastructure whose severance the Planetary
  Split Brain would plausibly have involved, or whose survival/partial-survival could be a genuine
  present-day plot thread (does Hwy 59's Arcanet Line still carry anything? Is it the reason certain
  cross-subnet contact never fully died even after the Split Brain?). Currently unexplored — flagged
  below as a high-value open thread, not yet written into any Split Brain material.

### The aviation layer (`Locations/Infrastructure/Airports.md`) — reinforces and extends the highway map

Tepenia's confirmed airports are few and deliberately curated, but tracing them reveals a genuine
cross-subnet aviation network layered on top of the highway one:

- **Dome Fuji (Mawson) is the country's real aviation convergence point, despite having no airport of
  its own.** It's supplied by air from **three separate directions**: Troll Airport (Halley subnet), the
  Tri-Cities Airport (Zhongshan/Sinheung/Shirayuki, Mirny subnet), and Mountain Pass Airport (between
  Kunlun and Vostok, Mirny subnet, also "reasonably accessible" to Dome Fuji per its own entry) — with
  cargo forwarded the final stretch via Hwy 37/Hwy 4. **A real, worth-dramatizing tension**: Tepenia's
  most remote, most nearly-Arcanet-less city is simultaneously the logistics focal point three separate
  regional aviation routes converge on. Isolation and centrality coexisting in the same city is a genuine
  story, not just a supply-chain footnote.
- **Marambio Airport (Palmer) is explicitly domestic**, "links Marambio to other Tepenian cities via the
  highway/aviation network" — plausibly a secondary/backup link into the Byrd corridor alongside Hwy 1,
  not yet confirmed either way.
- The **Machu Picchu Airport** (Sejong/Juan Carlos) is international (Upper Earth-facing via Ushuaia),
  not a domestic cross-subnet link — noted for completeness, not part of this file's actual scope.

### Direct city-to-city highway links across a subnet boundary (no intermediate stop)

| City A | Subnet | City B | Subnet | Via |
|---|---|---|---|---|
| Marambio (and the Peninsula cities behind it) | Palmer | Byrd | Byrd | Hwy 1 → Hwy 22 |
| Casey | Mirny | Dumont d'Urville | Janbogo | Hwy 2 |
| Sayowa (via the Spur/Junction) | Mawson | Lazar / Princess Elisabeth | Halley | Hwy 7-ext |
| Sayowa (via the Spur/Junction) | Mawson | Sinheung / Shirayuki | Mirny | Hwy 4 |
| Dome Fuji | Mawson | Kunlun / Vostok | Mirny | Hwy 37 |
| Vostok | Mirny | Concordia | — | Hwy 37 |
| Casey | Mirny | Concordia | — | Hwy 110 |
| Denison / (Janbogo region) | Janbogo | Concordia | — | Hwy 183 |

---

## Part 2 — Already-Established Cross-Subnet Connections (cataloged here for the first time as a set)

These already exist in scattered form across individual city files; this is the first place they're
collected together specifically as the country's cross-subnet fabric.

- **Belgrano (Halley) ↔ Byrd (Byrd).** Belgrano built Tepenia's first overland vehicles (the
  "Arrastradoras"/"Rastra" tracked vehicles) and mounted the expedition that found Byrd on the strength
  of old maps alone — Tepenia's founding overland-exploration story, connecting the country's most
  remote subnet to the Halley subnet directly. See `project_belgrano_byrd_expedition` memory.
- **Kunlun (Mirny) ↔ Dome Fuji (Mawson).** The only two 100%-robot cities in Tepenia; also the two poles
  of Ice-Cold Buddhism (Kunlun the holiest site, Dome Fuji its major pilgrimage destination), and directly
  linked by Hwy 37 (see Part 1). Already dramatized as a Course of Events cross-subnet chain during the
  nationwide Enhancement pass.
- **Sinheung (Mirny) ↔ Byrd (Byrd).** Tepenia's only two active Cradle/fabrication-synthesis-chamber
  manufacturers — already dramatized as a Course of Events cross-subnet chain, deliberately written as
  pure industrial fact without touching Cradle/player-origin implications.
- **Troll (Halley) ↔ Sinheung (Mirny) ↔ Dome Fuji (Mawson), a genuine three-subnet logistics triangle.**
  Troll Airfield and a smaller Sinheung-area airstrip are the two direct aviation routes that kept
  Dome Fuji supplied through a substantial stretch of its history — two separate routes converging on one
  city, not a relay chain. Already written into `Specs/Troll.md`, `Specs/Dome_Fuji.md`, `Specs/
  Sinheung.md`, `Local_Cultures/Halley_Subnet/Troll.md`.
- **Davis (Mirny) ↔ Mawson (Mawson).** Shared Australian Antarctic naming heritage; confirmed
  administratively separate, symbolic-only connection (occasional ceremonial/national-holiday
  acknowledgment, not genuine operational ties) — established in `Davis_Full_Extrapolation.md` Section
  IV, low-cost severance under the Planetary Split Brain since there was never a deep working
  relationship to lose.
- **Mirny subnet's internal Australian-heritage network (Davis, Casey, Mirny) survives the Split Brain**,
  per the same Full_Extrapolation finding — genuinely relevant here because it's the explicit contrast
  case proving intra-subnet links survive while inter-subnet links (like the Davis-Mawson one above) were
  actually severed.

---

## Part 3 — A Real-World Historical Connection, Not Yet Dramatized (high-value open thread)

**Davis and Mawson share more than naming heritage — their real-world namesakes had a direct historical
relationship.** John King Davis (Davis's namesake) captained the *SY Aurora* on Douglas Mawson's own
historical expeditions, and personally completed the relief voyage that rescued Mawson's stranded party
after Mawson lost his own companions. This is a real, deep, already-latent connection between these two
specific cities that the existing "shared naming heritage, administratively separate" treatment (Part 2,
above) doesn't actually use — it currently only credits the two cities with sharing a *category*
(Australian Antarctic heritage), not the far more specific fact that Davis's own namesake personally saved
Mawson's namesake's life. Worth developing deliberately: a founding-era story, memorial tradition, or
Course of Events chain built on this specific historical fact would give Davis↔Mawson real narrative
weight beyond the currently-thin "occasional ceremonial gesture" framing — while still respecting the
existing "administratively separate, low operational stakes" ruling, since a *symbolic* story (a shared
memorial day, a piece of ceremonial rhetoric, a named landmark) doesn't require inventing genuine
operational ties that Full_Extrapolation Section IV already ruled out.

---

## Part 4 — Shared Founding-Nation Cross-Reference

**Data gathered 2026-07-20** from `Official_Population_Census.md`'s Primary/Significant tiers, all 35
cities. Most cross-subnet nation overlap simply reflects the country's own known regional shipping
geography (already established: South Africa→Halley, New Zealand→Ross region/Byrd+Janbogo,
Australia→Dumont d'Urville Sea/Mirny+Mawson coast) — Halley/Palmer read USA-Primary/Euro-Significant
throughout, while Mirny/Mawson/Janbogo read China-Primary/Pacific-Significant (Japan, South Korea,
Indonesia, Australia) throughout. That expected pattern isn't itself a "finding" worth dramatizing. Three
genuine anomalies stood out against that baseline — cities whose composition doesn't match their own
subnet's regional pattern, each a real, non-obvious thread:

- **Byrd's population doesn't match its own physical lifeline.** Byrd's Primary/Significant profile
  (Japan + USA Primary; South Korea, Canada, Indonesia, Australia Significant) is the Pacific-facing
  Janbogo/Mirny/Mawson demographic shape almost exactly — but Byrd's *only* overland connection to the
  rest of the country runs through Palmer subnet (Hwy 1 → Hwy 22, Part 1 above), which is USA-Primary/
  Euro-Significant throughout. **Byrd's people and Byrd's road point in two different directions.** The
  likely real explanation: Byrd's population arrived predominantly via the established New Zealand supply
  route into the Ross region (which the Janbogo subnet's Ross Sea-facing cities also draw on), not
  overland via Palmer at all — meaning Byrd's genuine population kinship is with **Janbogo**, while its
  physical, structural dependency is on **Palmer**. A real, dramatizable tension: two entirely different
  kinds of connection pointing at two different subnets.
- **Vostok and Byrd share a Primary-nation pairing (USA + Japan) that no other city in Tepenia has.**
  Every other city is either single-Primary or has a different Primary combination. Worth investigating
  directly — whether this is coincidence or points at a real shared migration-era event or population
  movement between these two specific cities, neither of which has any other established connection to
  the other (Vostok's own established partnership is with Kunlun, not Byrd).
- **Fort McMurdo's Significant tier doesn't match its own Janbogo-subnet siblings.** Every other Janbogo
  city (Janbogo, Zukelli, Cape Adare, Dumont d'Urville, Scott, Denison) shares the same Pacific-facing
  Significant-tier shape (Japan, South Korea, Canada/Indonesia, Australia). Fort McMurdo's is instead
  Euro-heavy — Germany, France, UK, Italy — matching the Halley/Palmer pattern instead. **This is
  thematically apt, not just an anomaly to explain away**: Fort McMurdo is Tepenia's established
  historical/political capital (`TODO.md`, "National Capital — RESOLVED"). A capital plausibly drew
  migrants from across the *whole* country for political and administrative reasons, not just its own
  region — giving Fort McMurdo's demographic signature a real, in-character reason to break its own
  subnet's regional pattern, and a genuine basis for a Fort McMurdo↔Halley/Palmer population-migration
  connection distinct from anything else in this file.

---

## Part 5 — Still Isolated / Needs Work

Cross-checking every city named in Parts 1-4 against the full 35: **20 of 35 cities now have at least one
identified cross-subnet connection.** Mirny and Mawson subnets are fully covered (every one of their
cities appears above); Byrd (the only city in its subnet) is covered. The remaining **15 cities have no
cross-subnet connection identified yet** — the real priority list for continuing this thread:

- **Palmer (7 of 8 still isolated — only Marambio has a connection so far, via the Byrd corridor):**
  Esperanza, Juan Carlos, Palmer City, Port Lockroy, Rothera, Sejong, Signy.
- **Halley (4 of 8 still isolated — Belgrano, Lazar, Princess Elisabeth, and Troll are covered):**
  Halley (the city), Abowasa, Neumayer, Sanay.
- **Janbogo (4 of 7 still isolated — Dumont d'Urville, Denison, and Fort McMurdo are covered):**
  Cape Adare, Janbogo (the city), Scott, Zukelli.

**Palmer subnet is the clear gap** — it has by far the weakest cross-subnet connectivity of any subnet
(only its one highway gateway city, Marambio, connects outward at all), consistent with its own
established character as Tepenia's most peripheral, Peninsula-isolated region, but worth a dedicated look
specifically because a whole subnet reading as disconnected from the rest of the country undercuts the
"Tepenia was a real, unified country" goal this file exists to serve.

---

## Status and Next Steps

This is a **first-pass map**, not finished lore — it identifies *where* real cross-subnet connections
exist or plausibly exist, following the developer's own instruction to work through this "via whatever
means makes the most sense in-world, depending on each city's respective situations, circumstances,
traits, characteristics, etc." Turning any of the threads above into actual dramatized content (a Course
of Events-style chain, a piece of Megasheet cross-reference, an NPC storyline) is a separate, follow-up
step for whichever connections the developer wants to prioritize — this file's job is making sure that
next step has real material to work from, not guesswork.

**Still open:**
1. Byrd's population-vs-geography tension and the Vostok/Byrd shared Primary-nation pairing (Part 4) —
   both genuinely surprising, neither yet explained anywhere in existing lore.

**Resolved since this list was first written, 2026-08-06:**
- **Hwy 59's Arcanet Line** (Part 1) — developed into its own Course of Events chain
  (`Halley_09_One_Road_Two_Signals.md`) plus multiple Historical Vignettes entries.
- **The Davis/Mawson real-historical-rescue connection** (Part 3) — dramatized across three separate
  Historical Vignettes entries in Davis's and Mawson's own files.
- **Palmer subnet's overall weak connectivity** (Part 5) — superseded by `City_National_Connections.md`,
  which gives all 35 outer cities at least one identified connection (see that file's own "Coverage Note").
  This file's own Part 5 count (20/35) is accordingly historical, not a live gap.
- Fort McMurdo's Euro-heavy demographic anomaly (Part 4, not separately numbered above but discussed
  there) is still open — tracked as its own item in `City_National_Connections.md`'s "Open Threads Worth
  Flagging" list instead, alongside the still-open item above.
