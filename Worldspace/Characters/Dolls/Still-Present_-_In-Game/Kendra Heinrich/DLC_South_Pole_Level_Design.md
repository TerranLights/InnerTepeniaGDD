# Kendra Heinrich — DLC: South Pole Level Design

**Status: proposed working direction, not locked canon.** This document answers the
"critical open design question" flagged in `README.md` ("what defeated her?") and
builds out the physical site the DLC takes place in, using the engineering derived in
`Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`. Developer should
treat this as a strong, physics-grounded recommendation to accept, adjust, or replace
— not a finished decision.

---

## 1. Site Overview — Physical Condition of the Base

Amundsen Tower was a **space fountain** (not a classic elevator — impossible at the
South Pole; see the companion Theoretical-Calculations file), destroyed by a
deliberate military strike on its base accelerator/power complex during the Long
Night War. Losing power meant losing the pellet stream that held the entire 150 km
structure up — the whole tower came down, essentially in place, over the following
minutes.

**What this means physically for the site:**

- **The original surface facility is gone, not ruined-but-standing.** The debris
  field is centered exactly where the base facility was — the central mass of
  wreckage doesn't sit near the original station, it sits *on top of* where the
  original station was. There is no clean "abandoned base" to walk into; there is a
  mountain where the base used to be.
- **The underground foundation shaft (~2.7 km deep, bored into bedrock) very
  plausibly survived**, structurally separate from the collapsing surface tube. This
  housed the linear accelerator, power generation, pellet return-loop machinery, and
  maintenance tunnels — i.e., exactly the "underground tunnels" this whole design
  question started from. Likely state: mostly intact structurally, but **catastrophic
  damage concentrated at whatever point took the military strike** (the power plant
  vault is the leading candidate, being the "single point of failure" that explains
  why a strike there was sufficient to bring the whole tower down), with surface
  access points crushed or buried by the debris above.
- **Result: two very different environments stacked on each other** — a devastated,
  chaotic, unstable surface, and a largely intact but sealed-off, partially damaged
  tunnel network underneath. This is a strong dungeon/surface split for level design.

## 2. What Defeated Her (Proposed Answer)

Kendra's stat block (Might 10, Agility 10, Nerve 10, Engine 10) is written to be
absurd on purpose — no conventional enemy is a credible threat to her in a fair
fight, and her own file says the answer needs to be "credibly capable of defeating a
war goddess."

**Proposed answer: she wasn't defeated by an enemy. She was defeated by the collapse
itself.**

She was holding the line against Upper Earth forces at the base while evacuees caught
the last rides up the Tower. The military strike took out the accelerator/power
complex — and then roughly 246,000 tonnes of tower came down, the bulk of it landing
within a ~50–100 m radius of exactly where she was standing, over the course of a few
minutes (the longest-falling material, from 150 km up, takes about 6.6 minutes to
reach the ground). That isn't a fight to win or lose — it's a force-of-nature event
that "defeats" anyone regardless of stats. This satisfies every requirement in her
file:

- **Unique to the site** — this specific event only happens here, once
- **Credibly capable of defeating her** — nothing about her combat stats helps
  against a collapsing megastructure
- **Thematically connected** — it's literally the site's own defining catastrophe,
  the same event that ended the Long Night War evacuation and severed Tepenia from
  space
- **A legitimate final-tier challenge** — surviving it at all (which she did) is
  itself the proof of how tough she is; the DLC's job is to earn her stats, not
  contradict them

This also directly explains "stranded" without requiring an ongoing enemy to be
holding her captive: she survived — consistent with her stats — most plausibly by
being caught near or inside the surviving underground shaft rather than on the open
surface, but injured, and with her way out now buried under a mountain.

## 3. Ongoing DLC Hazards (Why Rescue Is Still the Hardest Content in the Game)

The initial "defeat" is backstory, not a fight the player experiences. The DLC's
actual difficulty — already established as brutally hard by design — comes from what
the site has become in the years since:

- **The debris mountain as traversal hazard.** Not a clean ruin — unstable, twisted,
  advanced-metamaterial wreckage (built on Hana Jinn's metamaterials research
  lineage), climbing/navigation challenges, sharp and unstable footing, possible
  buried unexploded ordnance from the original strike.
- **Residual energy/radiation hazards** from the struck power plant. Ties directly
  into the already-established Amundsen Resonance Effect
  (`Energy_Grid_Failure_Rationale.md` #11 — the Tower "drew massive planetary-scale
  energy") and thematically parallels reason #10 (contaminated geothermal wells from
  wartime weapons) — a plausible second, site-specific contamination source, distinct
  from Concordia's own.
- **Possible corrupted automated systems** still live in the surviving tunnel
  network — a direct parallel to the "corrupted control AIs" already established for
  Concordia's own power grid (`Energy_Grid_Failure_Rationale.md` #6). Malfunctioning
  accelerator control systems, defense systems, or salvaged/repurposed automation
  gone wrong are all plausible without inventing anything new.
- **The environment as co-antagonist** (already established in her `README.md`):
  extreme cold, total isolation, no supply lines, no shelter infrastructure.

## 4. Level Design Zones

The physics-derived structure of the debris field (see
`Amundsen_Tower_Space_Fountain_Design.md`, "How Far Does the Debris Actually
Spread?") maps directly onto a natural zone layout:

| Zone | Distance from center | Character | Content ideas |
|---|---|---|---|
| **The Mountain** | ~50–100 m radius, ~27–109 m tall | Central hazard; the dominant visual landmark | Traversal/climbing challenge; likely where Kendra is trapped, near a buried underground access point; densest wreckage and highest-value salvage |
| **Debris Apron** | 2–4 km out (up to ~10 km in storm-scatter scenarios) | Thinning scattered wreckage, including melted/pitted pellet-stream fragments (the ~50% of pellets that survived atmospheric passage — distinct material from the bulk structural debris) | Scavenging content; environmental storytelling; strong fit for the already-logged "frozen dead along the routes to Amundsen Tower" DLC idea — evacuees who didn't make it in time would plausibly be found here |
| **Clear Ground** | beyond ~4–10 km | Undamaged, open terrain | Plausible site for a present-day outpost/camp — a hub area for the DLC; see Vigil connection below |
| **Underground** | beneath the Mountain | Largely intact shaft/tunnel network, damaged near the power plant vault | The likely dungeon-crawl heart of the DLC; where Kendra is actually found; corrupted systems and residual energy hazards concentrate here |

## 5. Supporting Math (Full Derivation in Theoretical-Calculations)

Key figures pulled from `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`,
relevant to this site:

- Tower height: 150 km; total structure ~225,000 t; foundation shaft ~2.7 km deep
  (real South Pole ice thickness to bedrock)
- Total debris created at destruction: ~246,250 t (guide tube + pellets in flight)
- ~93% of that mass reaches the ground (~228,875 t); ~7% burns up in atmosphere —
  and that loss is concentrated almost entirely in the pellet stream (which impacts
  at exactly its 4.0 km/s launch speed, near the ablation threshold), not the passive
  structure (which never exceeds ~1.7 km/s falling from rest)
- Resulting debris pile: ~286,000 m³ bulk volume; ~27–109 m tall depending on
  concentration (100m vs 50m radius) — the tighter end fits the established "giant
  mountain of scrap" language
- Debris spread radius: ~2–10 km, driven by wind alone — **Coriolis deflection is
  exactly zero at the South Pole** (same geometric fact that ruled out a classic
  tension-cable elevator here), so there's no rotational scattering, only wind drift
- All of this stays two orders of magnitude short of Concordia (~1,660 km away),
  consistent with the established "wreckage does not reach Concordia" canon

## 6. Connections to Other Established Lore

- **The Vigil** — their reverence for the site (and the existing "repurposing Tower
  scrap is an Infamy trigger" rule) fits naturally with a present-day camp in the
  Clear Ground zone: close enough to maintain their signal towers and vigil, far
  enough to not be living directly in/on the wreckage. Their Infamy reaction to
  scavenging reads as protecting a mass-grave/war-memorial site, not just guarding
  resources.
- **Vosora Lashár Tanslock** — she organized the Tower's original *construction*
  logistics and is now stranded in Concordia, transmitting data to space-dwelling
  Tepenians. She's a strong candidate for a questline hook: unique knowledge of the
  base facility's original layout (accelerator geometry, tunnel network, power plant
  location) could help the player — or Kendra herself — navigate the underground
  layer, giving a builder/destroyer thematic pairing with Kendra's defender role.
- **Frozen dead along the routes to Amundsen Tower** (logged in `TODO.md`) — fits
  the Debris Apron zone specifically, since that's the terrain evacuees would have
  been crossing in the final approach to the Tower.

## 7. Open Questions

- Exact nature of the corrupted/automated underground threat (if used) — needs its
  own design pass, not just a label
- Whether the military strike weapon type (still flagged open in
  `World_History_Reference.md`) should inform the specific hazard types on site
  (e.g., a kinetic strike vs. an energy weapon would leave different residue)
- How explicitly the game reveals "the collapse defeated her" vs. leaving it
  something the player pieces together environmentally
- Precise placement of Kendra's location within the underground layer
