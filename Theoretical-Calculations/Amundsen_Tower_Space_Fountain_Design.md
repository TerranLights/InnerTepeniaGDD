# Amundsen Tower — Space Fountain Design

## TL;DR (2026-07-03)

1. **Scaling for a wartime evacuation surge is possible but not necessary.** The
   existing single track's theoretical max throughput (~90,000 people/hour) is ~180x
   the normal design capacity (~502/hour), and even fully maxed out only adds ~1% to
   the guide tube's structural weight. Any "some portion of the population escaped"
   figure — a scenario table in the file runs from ~360K to over 20 million depending
   on surge rate and evacuation window — works without changing the tower's physical
   size. This is a creative choice, not a physics constraint.
2. **The ~19.4 million tonnes of ice excavated** boring the foundation shaft down to
   bedrock (~21.2 billion liters if melted) is proposed as split between a one-time
   water-supply windfall during construction and engineered ice ridges piled around
   the base that double as windbreaks — giving the site a distinctive landscape
   feature.
3. **Essentially none of the Tower's material reaches orbit when destroyed.** It was
   a stationary, Earth-anchored structure held up by momentum transfer, not orbital
   motion — once support is lost it falls, it doesn't fly off. Even the pellet
   stream's own velocity (~51% of orbital velocity, and vertical rather than
   horizontal) means it comes back down near the base rather than becoming new
   orbital debris. Reinforces the localized "scrap mountain" conclusion.
4. **DLC idea (logged in `TODO.md`, not yet designed):** since the Tower's own
   throughput was never the evacuation bottleneck, the real tragedy is the journey
   *to* it — frozen bodies (human and robot) found along the routes various subnets'
   populations took while trying to reach Amundsen Tower during the Long Night War,
   many not making it in time. Relevant to DLC 1 (Kendra Heinrich) and potentially
   every regional subnet DLC.
5. **~93% of the ~246,250 t of debris reaches the ground; only ~7% burns up in the
   atmosphere.** The passive structure never exceeds ~1.7 km/s falling from rest
   (well below the ~4-7 km/s threshold where unshielded material starts ablating), so
   it survives largely intact. The pellet stream is the exception — it always impacts
   at exactly its 4.0 km/s launch speed (energy conservation), right at that
   threshold, so it's the one population with meaningful burnup (~50% estimated
   loss). Net: the scrap mountain is built from ~228,875 t, which piles into a
   ~27–109 m mound depending on how concentrated it lands (radius 100m vs 50m).
6. **Debris spreads roughly 2–10 km from the base (representative case ~3–4 km)**,
   driven entirely by wind — Coriolis deflection is exactly zero at the South Pole
   (same reason a classic space elevator doesn't work there). The site is likely a
   tall central mountain of bulk wreckage ringed by a thinner debris apron reaching a
   few km out, not one uniform pile — still nowhere close to Concordia (~1,660 km).
7. **Shipping the ~3.225 million tonnes of construction material in was never the
   bottleneck.** Across a multi-port network (Janbogo year-round; Halley subnet and
   Byrd/Ft McMurdo seasonal, ~90-100 days/year), even a modest fleet delivers
   everything in ~4 years — the seasonal Weddell Sea route takes ~3.6x longer than
   the year-round Janbogo route for the same tonnage, but both are trivial next to
   the ~65-75 year total build. Confirms (again) that tech development and on-site
   assembly, not material logistics, consumed most of the construction timeline.

---

Working design for the physical mechanism of Amundsen Tower (the Space Elevator),
established 2026-07-02. Covers *what kind of structure it is and how it works*, plus
worked dimensions, mass, and power figures (see "At a Glance" below). Remaining
sub-details are flagged under "Still Open" at the bottom.

---

## At a Glance

| Quantity | Value |
|---|---|
| Tower height | 150 km (past the Kármán line, short of full LEO ~400km+) |
| Guide tube mass | 225,000 tonnes |
| Pellet stream | ~270 tonnes/s circulating, launched at 4 km/s |
| Net power draw | ~324 GW (gross ~2.16 TW before regenerative recovery) |
| Base accelerator track | ~1.63 km |
| Foundation load | ~3.2 million tonnes-force over a ~63m-diameter core footprint |
| Foundation depth | ~2,700m — the real-world thickness of the Antarctic ice sheet at the South Pole before hitting bedrock |
| Bearing stations | 300, at 500m spacing (~100t each, ~30,000t total) |
| Waystations | 5 (Base, ~15km, ~50km, ~100km/Kármán line, 150km terminus) |
| Throughput needed for 9.5M pop. over ~65yr window | ~17 people/hour bare average — comfortably achievable, not a design constraint |

**Points worth flagging:**

- **The foundation depth question resolves itself from real geography** —
  Amundsen-Scott South Pole Station genuinely sits on ~2.7 km of ice. Any stable
  foundation has to bore through that to bedrock regardless of what the accelerator
  itself needs, which lines up almost exactly with the ~1.63 km accelerator track
  length anyway. That's "extremely thick, penetrates deep into the earth," with a
  concrete number attached.
- **Power draw is civilization-scale on purpose** (~324 GW net, comparable to a
  meaningful fraction of current global electricity generation) — that's what
  justifies the Amundsen Resonance Effect already in the Energy Grid lore.
- **Construction rate checks out easily** — ~8.8 tonnes/day average over 70 years is
  nowhere near a bottleneck, suggesting most of the 65–75 year build window went into
  developing the tech and building the power/accelerator infrastructure, not
  assembling the tube itself.
- **Collapse dynamics support the localized scrap mountain** — because the tube is a
  chain of independently-supported segments rather than one rigid rod, a power-loss
  failure drops the whole thing roughly vertically rather than toppling like a felled
  tree, keeping wreckage near the base instead of scattering across the 1,660 km to
  Concordia.
- **The tower doesn't reach full orbital velocity on its own** (delivers ~3.62 km/s
  vertically vs. ~7.82 km/s orbital velocity needed at that altitude) — confirming
  it's a launch-assist structure, with a final rocket stage finishing the job,
  consistent with Hana Jinn's original "mass drivers to launch reusable rockets"
  framing.
- **The 9.5M orbital population target doesn't require a bigger tower.** Moving the
  entire established orbital population through the Tower alone over the ~65-year
  window between completion and the Long Night War only requires ~17 people/hour on
  average — the 150 km design already comfortably supports this with room to spare
  for a realistic non-uniform migration curve and a dramatic wartime evacuation surge.

---

## The Physics Problem: Why Not a Classic Space Elevator

The textbook "space elevator" design — a cable extending from an equatorial anchor
point out past geostationary orbit, held taut because the counterweight moves faster
than orbital velocity at that radius — **only works on the equator**. It relies
entirely on Earth's rotation to generate tension via the counterweight.

Amundsen Tower is anchored at the South Pole (Amundsen Station), which sits *on*
Earth's rotation axis — essentially zero rotational velocity. The classic
tension-cable mechanism cannot exist there. A polar space elevator in the traditional
sense is a physical non-starter, ruled out on this basis.

## The Solution: A Space Fountain

A **space fountain** is a real, previously-proposed (if never built) megastructure
concept — not invented for this setting. It solves the polar-location problem because
it doesn't depend on planetary rotation or a counterweight at all.

**Core mechanism:**
- A continuous stream of small, dense pellets is electromagnetically accelerated
  upward at extremely high velocity from a linear accelerator at the base — literally
  a scaled-up mass driver, the same underlying technology as Hana Jinn's metamaterials
  research (see below).
- At the top, the pellets are magnetically decelerated and redirected into a return
  channel, traveling back down to the base, where they're re-accelerated — a closed,
  continuously circulating loop. The pellets are never cargo; they never leave the
  system.
- The physical tower — the **guide tube** — does not hold itself up by compressive
  strength the way a normal rigid tower does. Instead it's fitted with magnetic
  bearing stations along its length, each of which nudges the passing pellet stream
  slightly and, by Newton's third law, is nudged back. Spread across the tube's full
  height, this is what supports the structure's weight — the same principle as a jet
  of water holding up a floating ball, which is where the name comes from.
- Because the tube isn't fighting its own compressive weight, it can be comparatively
  light for its height. Its main engineering demand is precision: if the pellet stream
  ever clips the tube wall instead of running clean through center, that's a
  catastrophic failure. This is a natural place for Hana Jinn's metamaterials legacy
  to pay off again, generations later — lightweight, strong, precisely-manufacturable
  guide tube segments and magnets.
- **Works at any latitude, including the poles** — the one property a classic elevator
  cannot offer.

## Passenger & Cargo Transport

The pellet stream and the passenger/cargo system are **two separate structures riding
together, not one**:

- The pellet stream is the load-bearing "engine." It must run continuously — it
  cannot stop without the structure losing support.
- Passengers and cargo ride in separate magnetically-levitated cars, running alongside
  the guide tube on their own linear-motor track, using the same underlying magnetic
  technology but mechanically and operationally independent of the pellet loop.
  Functionally, a vertical maglev train running parallel to (not inside) the fountain
  mechanism that holds its own track up.
- These cars **can** slow down, stop, and dock at the base, the top, or any
  intermediate stations along the way — exactly like a normal elevator or funicular.
  This opens the door to waystations partway up the Tower (docking platforms,
  maintenance posts, possibly small habitats) as level-design/lore material beyond
  just "the base" and "the top."

## Why This Fits Established Canon

- **Hana Jinn** (`Worldspace/Characters/Dolls/Past_History_-_Known_to_Tepenians/Hana
  Jinn/`) — her metamaterials-for-mass-drivers research (early-to-mid 2300s) is the
  direct conceptual and technological ancestor of the space fountain's linear
  accelerator. Amundsen Tower is that same principle, rediscovered/rebuilt by exiled,
  cut-off Tepenia at monumental scale, ~250 years later.
- **Mallory Dufay** (`Worldspace/Characters/Dolls/Past_History_-_Known_to_Tepenians/
  Mallory Dufay/`) — oversaw the first launches/construction of the original orbital
  infrastructure built on this same tech lineage; her role (structural/safety
  inspection of exactly this kind of hazard) is thematically continuous with whatever
  safety discipline Amundsen Tower's construction and operation would have required.
- **The Amundsen Resonance Effect** (`Energy_Grid_Failure_Rationale.md`, reason #11)
  — already-established canon states the destroyed Tower "once drew massive
  planetary-scale energy," and that the current Antarctic grid's instabilities trace
  back to that loss. A space fountain's pellet stream requires enormous *continuous*
  power to keep circulating — this is exactly the profile of power draw that reason
  #11 already describes. No retcon needed; the design was implied before it was named.
- **Deliberate military destruction** (`World_History_Reference.md`) — cutting power
  to the base accelerator is a far more plausible single point of failure for a
  targeted military strike than physically demolishing a megastructure. This matches
  the established framing that the Tower's destruction was deliberate, not incidental
  battle damage.
- **The scrap mountain stays local** (doesn't reach Concordia, ~1,660 km away) — a
  space fountain doesn't need to physically extend to full LEO altitude; like Hana
  Jinn's original mass-driver concept, it only needs to impart sufficient
  altitude/velocity before handing off to a final rocket-propulsion stage. Keeping the
  tower's actual height in the tens-to-low-hundreds-of-km range (rather than full
  orbital altitude) makes a near-vertical collapse near the base far more plausible
  than debris scattering across a swath of the continent the way a felled structure
  the height of low orbit would.
- **Kendra Heinrich DLC underground tunnels** — the base would need to house the full
  linear accelerator, the pellet return loop, and massive power generation, all
  anchored against continuous downward reaction force. Tunnels running *through* the
  base (accelerator maintenance access, return-loop channels, power conduits) is a
  natural fit, rather than tunnels running around an inert foundation.

## The Numbers (worked 2026-07-02)

All figures below are order-of-magnitude engineering estimates built from explicitly
stated assumptions — adjust any assumption and the downstream numbers rescale
accordingly. Full derivation in scratch calculations; reproduced here as the working
reference.

**Stated assumptions:**
- Tower height: **150 km** — chosen to clear the Kármán line (100 km, the conventional
  edge of space) by a comfortable margin while staying well short of full LEO orbital
  altitude (~400 km+, ISS altitude). This keeps the structure's own collapse-debris
  footprint plausible (see below) and preserves the "final rocket stage does the rest"
  handoff concept inherited from Hana Jinn's original mass-driver design.
- Guide tube: **1,500 kg/m** average mass (structural sheath + magnetic bearings +
  parallel maglev passenger/cargo track + pellet return channel combined) — a rough
  analog to heavy dual-use industrial/rail infrastructure, deliberately light relative
  to what a self-supporting rigid tower of the same height would need, per the "not
  fighting its own compressive weight" design principle above.
- Pellet launch velocity: **4 km/s** at the base.
- Sustained accelerator load: **500 g** — aggressive but continuous/non-destructive
  for a purpose-built, presumably metamaterial-lined accelerator track.
- Bedrock bearing capacity: **10 MPa** (a strong-bedrock engineering design value).
- Base facility mass (power generation + accelerator hardware + support complex):
  **3 million tonnes**.

**Results:**

| Quantity | Value |
|---|---|
| Guide tube total mass | 225,000 tonnes |
| Pellet velocity at top (before turnaround) | ~3.62 km/s |
| Required pellet mass flow rate | ~270 tonnes/s (closed loop — not consumed) |
| Gross accelerator power (no recovery) | ~2.16 TW |
| Net power draw (85% regenerative recovery assumed) | ~324 GW |
| Base accelerator track length (to reach 4 km/s at 500g) | ~1.63 km |
| Total downward force on foundation | ~3.16×10¹⁰ N (~3.2 million tonnes-force) |
| Minimum structural core footprint (at 10 MPa bedrock) | ~3,160 m² (~63 m diameter) |
| Tube assembly rate needed over a 70-year build | ~8.8 tonnes/day |

**The foundation depth question resolves itself geographically:** Amundsen-Scott
South Pole Station sits atop roughly **2,700 m of Antarctic ice** before reaching
bedrock (real-world figure). Any stable foundation — regardless of the accelerator's
own ~1.6 km length requirement — must bore down through that full ice depth to anchor
in solid rock. This alone accounts for "extremely thick, penetrates deep into the
earth": a ~2.7 km shaft/plinth complex is comfortably deeper than the deepest real
mine shafts today (~4 km) but not absurdly so, and gives Kendra Heinrich's underground
tunnels a concrete depth range to be consistent with.

**Power draw sanity check:** ~324 GW net (or up to 2.16 TW gross, pre-recovery) is
civilization-scale — comparable to or exceeding present-day total global electricity
generation. This is intentionally huge: it's what "drew massive planetary-scale
energy" (the Amundsen Resonance Effect, `Energy_Grid_Failure_Rationale.md` #11) is
describing, and explains why its sudden loss during the Long Night War left a
permanent scar on Tepenia's power grid rather than a routine outage.

**Construction timeline sanity check:** ~8.8 tonnes/day average assembly rate over 70
years is comfortably achievable — likely means most of the 65–75 year build window
was spent developing the technology, building the power/accelerator infrastructure,
and testing, rather than being bottlenecked on raw material assembly of the guide
tube itself.

**Collapse/debris-locality sanity check:** unlike a single rigid rod toppling from a
hinge at the base (which would fling wreckage roughly as far as its own height), a
space fountain's guide tube is a chain of discrete, independently-supported segments.
A power-loss failure would cause the whole chain to lose support roughly
simultaneously rather than pivot as one unit — each segment free-falls close to
vertically, slowed by atmospheric drag on the way down, with only wind drift (not
orbital horizontal velocity) affecting lateral spread. This is consistent with wreckage
staying confined to the South Pole vicinity rather than reaching Concordia
(~1,660 km away) — a taller, faster-moving, or orbital-altitude structure would be a
much harder fit for that constraint.

**Orbital handoff:** true orbital velocity at 150 km altitude is ~7.82 km/s
(horizontal). The tower only delivers ~3.62 km/s of (vertical) velocity at the top —
it gets payloads up and moving fast, but a final rocket stage still has to do
real work to complete orbital insertion. This is consistent with Amundsen Tower being
a launch-assist megastructure, not a complete point-to-point orbital shuttle on its
own — the same division of labor implied by Hana Jinn's original "mass drivers to
launch reusable rockets" framing.

## Bearing Station Design (worked 2026-07-02)

- **Spacing: 500 m** → **300 bearing stations** across the 150 km tube. At the
  pellet stream's speed (3.6–4 km/s), that's a correction every 125–138 milliseconds
  — frequent enough for tight magnetic confinement given the stream is moving at
  km/s speeds, not anywhere near relativistic, so this spacing carries real margin,
  not a razor's-edge tolerance.
- **Per-station mass: ~100 tonnes** (superconducting magnets, cooling, control
  systems) → **30,000 tonnes total** across all 300 stations.
- The remaining **195,000 tonnes** of the guide tube's total mass is continuous
  structure between stations (sheath, parallel maglev track, pellet return channel)
  — averaging **~1,300 kg/m**, close to but distinct from the earlier lumped 1,500
  kg/m figure (which included the stations).

## Waystations (worked 2026-07-02)

Since the passenger/cargo maglev cars are mechanically independent of the pellet
stream (see "Passenger & Cargo Transport" above), stopping at intermediate stations
is purely a placement decision, not a physics constraint. Proposed layout — five
stations total, chosen at meaningful altitude thresholds:

| Station | Altitude | Purpose |
|---|---|---|
| Base Terminal | 0 km | Main terminal; surface transport connections; accelerator/power complex |
| Cloudline Station | ~15 km | Above the dense troposphere and most weather/wind — first major environmental threshold |
| Relay Station | ~50 km | Mid-altitude maintenance and redundancy waypoint |
| Kármán Station | ~100 km | The traditional "edge of space" boundary — symbolically and operationally significant; plausible site for a named, culturally important location |
| Orbital Terminus | 150 km | Top of the tower; docking point for the final rocket-propulsion stage to complete orbital insertion |

Names are working placeholders — open to whatever fits Tepenian naming conventions.

## Throughput & the 9.5M Population Question (worked 2026-07-02)

**The question:** how large would Amundsen Tower need to be to move the established
orbital population (**9,543,076** — `Official_Population_Census.md`) up from Tepenia
between the Tower's completion (~2629–2639) and the Long Night War (~2694–2704)?

**Operating window:** central estimate **65 years** (range 55–75 years depending on
which end of each date range is paired with which).

**The headline finding: the bare statistical average is very modest.**
Assuming, as a conservative upper bound, that the *entire* 9.5M population figure
was transported via the Tower (no in-orbit robot manufacturing or human births
counted — both of which almost certainly did contribute, given ~200+ years of
already-established off-world industrial capacity via the Hana Jinn/Mallory Dufay
lineage predating the Treaty):

| Window | Required average rate |
|---|---|
| 55 years (fastest tower, earliest war) | ~19.8 people/hour |
| 65 years (central estimate) | ~16.75 people/hour |
| 75 years (slowest tower, latest war) | ~14.5 people/hour |

**That means the Tower's 150 km height and existing design are not actually
throughput-constrained by the population target at all.** The height was set by
physics (space fountain mechanics, orbital handoff, debris-locality on collapse) —
and it turns out to already be more than large enough to hit 9.5M without needing to
scale up further. This is a real finding, not a dodge: the answer to "how large would
it need to be" is "no larger than already designed — the numbers already work."

**Proposed passenger system (with realistic margin, not bare minimum):**
- 30-person maglev cars, traveling at ~1,500 km/h (417 m/s) — a fast but
  passenger-survivable speed, well below the pellet stream's 4 km/s.
- One-way travel time: **~6 minutes**.
- Design capacity at **30x the bare average** (margin for a realistic non-uniform
  migration curve — slow ramp-up in the early decades, busier later — plus everyday
  operational headroom): **~502 people/hour**, or about one car departure every
  **3.6 minutes**, needing only **2 cars simultaneously in transit** per direction at
  any given moment. Even this generously-margined design is a small, unglamorous
  system relative to the megastructure carrying it.
- **Wartime evacuation surge:** the established "large-scale population movement" of
  evacuees fleeing via the Tower during the Long Night War itself was almost
  certainly a short, desperate spike far above this steady-state design capacity —
  packed cars, continuous max-cadence departures, likely rationing/triage of who
  gets a seat. The system as sized has enormous headroom to flex into that scenario
  dramatically without needing retroactive resizing.

## Scaling for a Wartime Evacuation Surge (worked 2026-07-03)

**Question:** can the tower be scaled up — thicker, higher passenger capacity — to
account for an additional wave of the national population escaping via the Tower
during the Long Night War (on top of the 9.5M already established as living/working
in orbit before the war began)? Is scaling even necessary?

**Is it possible?** Yes — a thicker guide tube with more parallel maglev tracks is a
straightforward (if power-hungry) upgrade: more/heavier structure means more weight
for the pellet stream to support, which scales via the same relation used throughout
this document (`dm/dt = W / (2×v0)`) — more mass flow rate and/or higher pellet
velocity, and proportionally more power.

**Is it necessary? No — the existing single-track design already has enormous
untapped headroom, without changing the tower's physical size at all:**

- Theoretical maximum throughput of the *existing* single track (300 cars
  simultaneously in transit at 500m spacing, ~6 minute one-way trip): **~90,000
  people/hour** — roughly **180x** the steady-state design capacity proposed above.
- Critically, **packing the tube with the maximum 300 cars only adds ~2,400 tonnes**
  of transient weight (at ~8 tonnes/car) — **about 1% of the guide tube's 225,000
  tonne structural mass.** The pellet stream and power system sized earlier already
  handle this without modification. Emergency surge capacity is a matter of building
  and running more cars, not re-engineering the tower.

**Suggested scale for "some portion of the national population" escaping during the
war** (your creative call — these are just illustrative combinations of surge
throughput × evacuation window):

| Surge rate | 30 days | 60 days | 90 days |
|---|---|---|---|
| 502/hr (normal design capacity, no surge) | ~361,000 | ~723,000 | ~1,084,000 |
| 2,000/hr (modest surge — more cars added) | ~1,440,000 | ~2,880,000 | ~4,320,000 |
| 10,000/hr (major surge — most of theoretical max) | ~7,200,000 | ~14,400,000 | ~21,600,000 |

For reference, the established census implies a pre-war surface (non-orbital)
population of roughly **~21.5 million** (9.2M orbital ≈ 30% of the pre-war total, per
the existing census finding in `TODO.md`). A figure in the **few hundred thousand to
low millions** range (top-left of the table) reads as "a meaningful portion escaped,"
without implying most of the surface population made it out — consistent with
Tepenia still having a substantial post-war population in Concordia and elsewhere.
**This is a narrative choice, not a physics-constrained one — the tower can support
any of these figures without modification.**

## Excavated Ice — Where Does It Go? (worked 2026-07-03)

Boring the ~2.7 km foundation shaft down to bedrock excavates a large volume of ice.
Assuming a ~100m diameter shaft (generous vs. the ~63m core structural footprint, to
allow construction clearance):

- **Volume excavated: ~21.2 million m³**
- **Mass: ~19.4 million tonnes** of ice
- **If fully melted: ~21.2 billion liters of water** — for scale, enough to supply a
  500,000-person city at 150 L/person/day for **~283 days (~0.8 years)**

**Proposed disposition — a combination, not a single answer:**
- **Partially melted for water supply** during construction and ongoing operations —
  a huge, one-time captive resource windfall. Plausible detail: this incidentally
  solved regional water supply concerns for a significant stretch of the Tower's
  construction era.
- **The remainder piled into engineered ice ridges/mounds around the base facility**
  — practical spoil disposal that doubles as windbreaks against Antarctic katabatic
  winds (a genuine engineering use, not just a place to dump material). This gives a
  distinctive, dramatic landscape feature for the base site: artificial ice ridges
  ringing the facility, visible evidence of the excavation at a glance.

## Destruction Debris — Does Any of It Reach Space? (worked 2026-07-03)

**Short answer: essentially none of it.** Amundsen Tower's material was never in
orbit to begin with, and nothing about its destruction changes that.

- **The guide tube itself is a stationary, Earth-anchored structure**, held up by
  continuous momentum transfer from the pellet stream — not by orbital motion. It was
  never moving fast enough, or in the right direction, to be "in orbit." Once the
  pellet stream stops (power cut), the tube simply loses its support and falls, the
  same as any structure that loses its foundation — it doesn't fly off anywhere.
- **The pellet stream's own material also falls back.** Its maximum speed (4 km/s) is
  only about **51% of orbital velocity** at 150 km altitude (7.82 km/s) — and
  critically, that 4 km/s is *vertical*, while orbital velocity is *horizontal*.
  Pellets in transit at the moment of failure become simple ballistic
  projectiles — moving straight up or down, not sideways — so they come back down
  near where they were, subject only to wind drift and a minor Coriolis deflection
  over their fall time, not scattered across any real distance.
- This reinforces (rather than revises) the earlier "scrap mountain stays local"
  conclusion used to justify the tower's 150 km height in the first place: there's no
  plausible mechanism, structural or pellet-stream, for Amundsen Tower's own material
  to become new orbital debris. Everything comes down, and comes down close to home.

## Atmospheric Burnup — How Much Reaches the Ground? (worked 2026-07-03)

Total material that becomes wreckage: the guide tube (225,000 t) plus whatever
pellets were in flight at the moment of failure (~21,250 t, given a ~39-second
one-way transit time at the ~270 t/s pellet throughput) — **~246,250 t total.** Not
all of it necessarily reaches the ground, but the answer splits sharply into two very
different populations, because they fall under very different physics.

**The guide tube (structure, bearings, sheathing) falls from rest.** It was never
moving — it was a stationary structure held up by the pellet stream, not something
with its own velocity. Once support is lost, it simply free-falls from whatever
altitude it was at:

| Starting altitude | Impact velocity (vacuum freefall, upper bound) |
|---|---|
| 150 km (top) | ~1.70 km/s |
| 100 km | ~1.39 km/s |
| 50 km | ~0.98 km/s |
| 20 km | ~0.62 km/s |
| 5 km | ~0.31 km/s |

**The pellet stream falls carrying its full operational velocity — and by energy
conservation, it always impacts at exactly 4.0 km/s**, regardless of where in its
up/down journey the power failure occurred (whatever goes up at v0 in a vacuum comes
back down at v0; the altitude at which the failure happens doesn't change the total
mechanical energy of the flight).

**Comparing to real-world reference velocities:**
- ICBM reentry vehicles — need ablative heat shielding: **~4–7 km/s**
- Orbital (LEO) reentry, e.g. deorbiting satellites: **~7.82 km/s**
- Meteors: **~11–72 km/s** (most mass vaporizes)

**This splits the debris cleanly:**
- The **guide tube** never exceeds ~1.7 km/s — well below even the ICBM-reentry
  threshold. This material would experience only modest heating from supersonic (not
  hypersonic) air friction — surface scorching at most. The large majority of it
  (estimated **~97%**) plausibly reaches the ground intact.
- The **pellet stream** impacts at exactly **4.0 km/s — right at the low end of the
  ICBM-reentry threshold**, and unlike a warhead, pellets have no ablative heat
  shielding. This is the one population where meaningful atmospheric burnup is
  physically justified — estimated **~50%** loss, with the rest surviving as
  melted/pitted fragments.

(Both survival percentages are reasoned estimates from the velocity comparison
above, not a precise ablation simulation — real losses would depend on pellet
material, size, and fragment shape, which aren't specified yet.)

**Net result:**

| | Mass | Survival estimate | Reaches ground |
|---|---|---|---|
| Guide tube / structure | 225,000 t | ~97% | ~218,250 t |
| Pellet stream | 21,250 t | ~50% | ~10,625 t |
| **Total** | **246,250 t** | **~93%** | **~228,875 t** |

**~93% of the tower's material reaches the ground; ~7% (~17,000 t) burns up —
and nearly all of that loss comes specifically from the actively-moving pellet
stream, not the passive structure.** The structure was simply never moving fast
enough to burn up in any meaningful way.

## Scrap Mountain — Physical Size (worked 2026-07-03)

Using the ~228,875 t that actually reaches the ground (not the full pre-atmosphere
total), at a bulk density of 800 kg/m³ (loose, jumbled collapsed wreckage — much less
dense than the intact material):

- **Debris volume: ~286,000 m³**

How tall this reads depends on how concentrated the pile is — the established lore
already calls it a "giant mountain of scrap" (`TODO.md`), which favors the tighter end:

| Pile radius | Resulting height |
|---|---|
| 50 m | **~109 m — a genuine mountain** |
| 100 m | ~27 m — a substantial hill |
| 250 m | ~4 m — a wide, low debris field |

## How Far Does the Debris Actually Spread? (worked 2026-07-03)

The pile-radius question above was left open-ended; actual physics resolves it.
Since the structure falls essentially straight down (no horizontal velocity of its
own), the only thing that can spread it out sideways is wind — and one thing that
*doesn't* contribute is worth naming explicitly:

**Coriolis deflection is exactly zero at the South Pole.** The classical formula for
an object's sideways deflection while falling scales with cos(latitude); at the pole
(latitude 90°), that term is zero. This is the same underlying fact that ruled out a
classic tension-cable space elevator here in the first place (zero rotational
velocity at the pole) — it also means falling debris gets no rotational "push"
sideways at all. Wind is the only real driver of lateral spread.

**Fall time** (two-phase: near-vacuum above ~50km, drag-limited descent through the
denser lower atmosphere below that) works out to:

| Origin altitude | Fall time |
|---|---|
| 150 km (top) | ~6.6 min |
| 100 km | ~5.9 min |
| 50 km | ~1.7 min |
| 20 km | ~1.1 min |
| 5 km | ~0.5 min |

**Drift = wind speed × fall time.** Real-world South Pole wind is comparatively
mild for Antarctica (it's on the high inland plateau, not a coastal katabatic wind
funnel) — averaging **~5–6 m/s**, with storm conditions reaching **~20–25 m/s**. For
the longest-falling material (from the top, ~6.6 min):

| Wind condition | Drift (worst case, top-of-tower origin) |
|---|---|
| Calm (~5 m/s) | ~2.0 km |
| Average (~10 m/s) | ~3.9 km |
| Storm (~25 m/s) | ~9.9 km |

**Answer: roughly a 2–10 km radius**, with ~3–4 km as the representative case under
typical South Pole wind conditions — comfortably short of Concordia (~1,660 km away),
so the "stays local" constraint holds by two orders of magnitude either way.

**This means the debris field isn't a single uniform pile — it's layered by
origin altitude:** material from low on the tower (short fall, minimal drift) lands
close to the base; material from higher up (longer fall, more time for wind to act)
lands progressively farther out, mostly in whatever direction the wind was blowing
during the collapse. The likely resulting shape: a genuinely tall, concentrated
**mountain of the bulk structural wreckage right at the base** (from the tower's
lower reaches and the sheer volume of material collapsing in place), surrounded by a
**thinner debris apron extending 2–4 km outward** (from higher-origin material and
the faster-falling pellet stream) — both "mountain" and "field" are accurate,
describing different rings of the same site.

## Base Facility Layout (worked 2026-07-02)

**The foundation shaft (~2.7 km deep, matching real South Pole ice thickness) is a
single unified structure, not separate systems stacked together:**
- The bottom of the shaft (deepest, anchored in bedrock) houses the **1.63 km linear
  accelerator track**, oriented vertically, launching pellets straight up through the
  remaining ice/shaft distance and directly into the visible guide tube at the
  surface — no direction change needed between accelerator and tower.
- Above/alongside the accelerator: **power generation**. Given the ~324 GW net draw,
  primary generation is plausibly an advanced nuclear/fusion reactor array (already
  implied by the existing Power Core lore's "geothermal/nuclear systems" framing in
  `Energy_Grid_Failure_Rationale.md` #1), supplemented by geothermal taps into
  Antarctic subglacial volcanic activity — real, if localized, geothermal sources do
  exist under the Antarctic ice sheet.
- **Pellet storage and return-loop machinery** — the closed-loop circulation system
  that catches, redirects, and re-launches the ~270 tonnes/s pellet stream.
- **Maintenance and access tunnels** threading through all of the above — this is the
  direct link to the Kendra Heinrich DLC's underground tunnels, which per the
  original prompt for this whole design pass, plausibly run *through* this shaft
  complex rather than around an inert foundation.

**Surface complex:** the structurally load-bearing core footprint is only ~63 m in
diameter (per the foundation math above), but the operational facility around it —
worker/robot support facilities, cargo processing terminals, administrative
buildings, surface transport connections toward the rest of Tepenia — would sprawl
across a much larger area, plausibly on the order of **1–2 km²**, consistent with how
real large infrastructure projects have footprints far bigger than their
structural core.

## Construction Material Logistics — How Long to Ship It In? (worked 2026-07-03)

**Total material to deliver:** guide tube (225,000 t) + base facility (~3,000,000 t
— power generation, accelerator hardware, support complex) = **~3,225,000 tonnes**.
None of this can come from Upper Earth (Tepenia is politically isolated pre-Tower) —
it has to move by intra-Tepenian coastal freighter from wherever it's sourced or
manufactured, to a port, then overland to the South Pole construction site.

**Multi-port network, per the user's steer:** material arrives via several coastal
regions in parallel, not one single route:

| Route | Share (assumed) | Shipping season |
|---|---|---|
| Janbogo (Terra Nova Bay polynya) | 40% | Year-round — genuinely ice-free regardless of season, per Janbogo's own Specs file |
| Halley subnet (Weddell Sea / Queen Maud Land / King Haakon Sea) | 40% | ~100 days/year (seasonal) |
| Byrd subnet (Ross Ice Shelf) + Fort McMurdo (Ross Sea) | 20% | ~90 days/year (seasonal) |

**Fleet assumption (era-appropriate, not modern-industrial scale):** modest cargo
vessels at ~15,000 t capacity each, a small fleet per route (3/3/2 ships), ~14-day
round-trip turnaround for intra-Tepenian coastal distances.

**Result — the seasonal constraint matters a lot, exactly as the question implied:**

| Route | Voyages needed | Years to deliver its share |
|---|---|---|
| Janbogo (year-round) | 86 | **~1.1 years** |
| Halley subnet (seasonal) | 86 | **~4.0 years** |
| Byrd/Ft McMurdo (seasonal) | 43 | **~3.3 years** |

Same tonnage, but the seasonal Halley route takes **~3.6x longer** than the
year-round Janbogo route to deliver an identical share — a direct, quantified
illustration of why the "not all year round" constraint matters. Since the three
routes run in parallel, the overall shipping campaign is bounded by the slowest one:
**~4 years** with this modest fleet.

**The overland leg (port → South Pole) runs concurrently, not serially:**

| Port | Approx. distance | One-way transit (early, ungroomed route, ~1.5 km/h effective) |
|---|---|---|
| Janbogo | ~1,750 km | ~49 days |
| Halley subnet | ~1,650 km | ~46 days |
| Byrd/Ross Ice Shelf | ~1,400 km | ~39 days |
| Fort McMurdo | ~1,600 km | ~44 days |

Heavy tracked convoys can run through at least the summer continuously, hauling
from stockpiled port material rather than waiting on individual ships — so this
doesn't add serially to the ~4-year shipping campaign, though early trips (before
any route is "groomed" into an established highway, the way Hwy 183 etc. are
elsewhere in Tepenia) would run on the slow end of that range.

**Bottom line: full material delivery is plausibly achievable within single-digit
years (~5-10, allowing for ramp-up and real-world inefficiency) — a small fraction
of the established ~65-75 year total construction window.** This reinforces the
earlier construction-rate finding (~8.8 tonnes/day average assembly rate, nowhere
near a bottleneck): **material logistics was never the limiting factor.** Most of
the 65-75 years went into developing the underlying technology and the on-site
assembly/construction itself, not waiting on shipments.

**Canon resolution (2026-07-03) — why the 65-75 year window still holds despite
this:** the Falkland-Treaty-to-Tower-completion window was never *all* Tower
construction time. Per `World_History_Reference.md` ("The Space Elevator (Amundsen
Tower)"), it's a phased national infrastructure sequence: cities founded and built
out → subnet-internal highways → the Arcanet gradually connected subnet by subnet →
**Hwy 22 (the Transcontinental Highway) built, running directly through the South
Pole/Amundsen Station itself** (confirmed against the highway map — corrected from
an earlier, wrong assumption that a separate Hwy 175 segment was needed to reach the
Pole) → **only then does Tower construction proper begin**, plausibly in the final
~12-17 years of the 65-75 year window. That final phase is exactly what this
document's shipping/assembly numbers describe. Hwy 22 reaching the South Pole is the
literal precondition for this section's overland-leg assumptions (a groomed,
established highway rather than an ad-hoc early traverse).

## Still Open

- Precise construction start date (must predate ~2629–2639 completion by 65–75
  years, i.e., starting shortly after the Falkland Treaty in 2564 per existing
  canon) and the specific weapon(s)/method used in its destruction — both flagged in
  `World_History_Reference.md`
- Detailed cargo/freight throughput (as distinct from passengers) — likely modest,
  since bulk construction material for orbital infrastructure comes from debris
  in-situ, not Tower-launched cargo (see `Orbital_Infrastructure_Mass_Budget.md`)
- Naming conventions for the five waystations
- Wartime evacuation surge — actual peak throughput achieved during the Long Night
  War evacuation itself, if a specific figure becomes useful for narrative/level design

## Cross-References

- `World_History_Reference.md` — "The Space Elevator (Amundsen Tower)" section
- `TODO.md` — "Amundsen Tower — determine actual dimensions"
- `Worldspace/Characters/Dolls/Past_History_-_Known_to_Tepenians/Hana Jinn/`
- `Worldspace/Characters/Dolls/Past_History_-_Known_to_Tepenians/Mallory Dufay/`
- `Worldspace/Energy_Grid_Failure_Rationale.md` (reason #11)
- `Orbital_Infrastructure_Mass_Budget.md`, `Von_Braun_Wheel_Mass_Budget.md`,
  `Design_Efficiency_Comparison.md` (companion Theoretical-Calculations files)
- `Worldspace/Characters/Dolls/Still-Present_-_In-Game/Kendra Heinrich/
  DLC_South_Pole_Level_Design.md` — applies the math in this file to DLC 1's site
  condition, level design zones, and a proposed answer to "what defeated her"
