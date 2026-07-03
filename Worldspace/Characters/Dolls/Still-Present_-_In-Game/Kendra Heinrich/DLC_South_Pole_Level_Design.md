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

## 7. Intro/End Slide Structure *(established 2026-07-03)*

Per `Storyline/DLC_Overview.md`'s Fallout: New Vegas-modeled design standard, all
7 DLCs get both a framed intro sequence and end slides — DLC 1 is not an
exception on the intro side. The developer already has a clear picture of what
Kendra's opening sequence should be (not yet transcribed here — pick up in a
future session); it just won't follow the "establish a cast of multiple
factions/characters" shape the other six DLCs' intros will, since this is a solo
story about one character rather than a multi-faction conflict.

**End slides — the actual problem, and the Lonesome Road model:** DLC 1 has no
faction ecosystem to generate per-faction outcome slides the way the other six
DLCs will (multiple characters, competing factions, regional politics). It's
just Kendra, alone, fading in the underbelly of Amundsen Station. **Lonesome
Road solves the identical end-slide problem** in NV (minimal cast — just the
Courier and Ulysses, no local factions) by making its endings about the *largest
strategic picture* — which missiles get launched, what that means for the whole
NCR-Legion war — rather than local faction consequences. That's the intended
model for Kendra's end slides specifically. (Lonesome Road separately has no
intro sequence at all, which is an unrelated fact about it — the parallel being
drawn here is about the ending structure only.)

**Five candidate end-slide angles (2026-07-03, explicitly subject to revision
once actual plot-outlining begins):**

1. **Kendra's own personal fate** — the most direct analog to a companion-fate
   slide: what actually happens to her based on what the player does in the
   underbelly. Does she finally get to stop, get recovered or preserved somehow,
   remain exactly as she is, or something else?
2. **The site's epilogue** — the Tower ruins/scrap mountain itself as the
   "character" with a fate, the way Lonesome Road treats the Divide and its
   missiles as the real subject rather than any person. Sealed, memorialized,
   stripped for salvage, left disturbed? A faction-less but still
   player-reactive consequence system.
3. **The evacuation dead** — ties directly to the already-logged "frozen bodies
   along the evacuation routes" idea (see `TODO.md`). If the DLC lets the player
   recover, document, or identify any of the people who didn't make it to the
   Tower in time, an end slide could cover whether their stories made it home to
   their subnets — a way to gesture at *all six other DLCs* from inside the one
   DLC that otherwise has no factions of its own.
4. **The Arcanet archive / Planetary Split Brain** — Amundsen Station holds the
   last synchronized pre-Split-Brain archive. If the DLC involves accessing or
   restoring it, that's a legitimate, faction-independent stake with real
   downstream consequences for whether the Split Brain gets resolved.
5. **A capstone reflection across all six other DLCs** — since DLC 1 releases
   *last* (see `project_level_cap_dlc_progression` memory / `DLC_Overview.md`
   Release Order section), its final slide(s) could reflect back across
   everything the player has already done across the whole Federation — the way
   Lonesome Road's ending functions as commentary on the entire NCR-Legion
   conflict rather than its own isolated story.

---

## 8. Dual-Outcome Companion Perk — Working Example *(established 2026-07-03)*

Per `Game-Mechanics/Perks/Perk_Framework.md`'s universal dual-outcome companion
perk system (the Cass/Hand-of-Vengeance-vs-Calm-Heart model, extended so the
companion's branch also determines a paired player perk), Kendra's Arcanet
archive/hardware decision (angle 4 above) is the current working example of a
**three-way branch** — evaluated and judged competent, per the "try for three,
don't force it" guidance in `Perk_Framework.md`:

**A. Restore & Broadcast** — fully restore the archive and transmit the true
pre-split history to all six subnets, resolving the Planetary Split Brain.
- *Kendra's psychology:* closure and vindication. Her sacrifice at the Tower
  becomes verifiably known everywhere, not just felt as loss — for an 8w7
  who's spent the whole DLC stripped of control, this is the one path where
  she gets something back.
- *Candidate companion perk:* **"Vindicated"**
- *Candidate player perk:* reputation/recognition-flavored, paying off across
  every other DLC region (unique dialogue, faster standing gains) — the
  player is now known Federation-wide as the one who told the truth.

**B. Recover but Control the Release** — hold the archive, release it
selectively (Concordia's government, a specific faction, or kept as leverage)
rather than broadcasting it openly.
- *Kendra's psychology:* arguably the more natural fit for an 8 than option A —
  8s trust control and calculated strength, not naive openness. She could
  approve of this specifically because it doesn't hand something this
  dangerous to everyone indiscriminately.
- *Candidate companion perk:* **"The Long Game"**
- *Candidate player perk:* leverage/information-advantage flavored — discounts,
  unique access to gated dialogue or quest paths tied to holding a genuine
  secret.

**C. Let It Go** — don't restore it, or actively let it be lost; the past
stays buried.
- *Kendra's psychology:* the most complicated of the three — part relief (the
  burden of memory ends, including whatever the archive holds about her own
  failure) and part grief (nothing gets redeemed, nothing gets fixed). Ties
  well to the game's own robot-consciousness north star question.
- *Candidate companion perk:* **"The Weight Set Down"**
- *Candidate player perk:* more philosophical/mechanical than the other two —
  something about moving forward unburdened rather than gaining leverage or
  reputation.

**Status:** all three read as genuinely distinct, coherent choices rather than
a padded third option — this branch is a plausible template for how other
companions' three-way splits might be evaluated, though exact perk
names/mechanics are placeholders pending real design work.

---

## 9. Open Questions

- Exact nature of the corrupted/automated underground threat (if used) — needs its
  own design pass, not just a label
- Whether the military strike weapon type (still flagged open in
  `World_History_Reference.md`) should inform the specific hazard types on site
  (e.g., a kinetic strike vs. an energy weapon would leave different residue)
- How explicitly the game reveals "the collapse defeated her" vs. leaving it
  something the player pieces together environmentally
- Precise placement of Kendra's location within the underground layer
