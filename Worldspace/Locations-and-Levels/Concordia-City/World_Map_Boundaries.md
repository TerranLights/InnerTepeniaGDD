# World Map Boundaries — Marking the Edge of the Playable World

**What this is:** a design draft, not a locked decision — written 2026-07-25. Addresses a concrete level-design
need: Concordia's outermost districts border open, hostile Antarctic terrain rather than another district or
a neutral wall, so there needs to be a real, in-world way to signal "this is the edge of the playable map"
without it reading as an arbitrary invisible barrier.

**Corrected 2026-07-25, against the actual reference map:** the developer confirmed they never established
Concordia as a citywide domed city — that was an over-generalization on my part, extrapolating too far from
Sagittarius's own "outside the domes is lethal" line (plural "domes," a detail worth taking more literally
than I initially did). The actual map (`Reference/Images/Maps/Concordia_City_-_Extended_map_-_with_labels_-_Color-Coded_by_District.jpeg`)
is a **radial city**: a central hub (the Axis Mundi/Neutral Hub), with ten districts packed into compact
inner rings close to that hub, and only **Sagittarius** and **Capricorn** actually reaching the true outer
perimeter — each in a visibly different way, confirmed directly by the developer:

- **Sagittarius** — the map shows it as a huge arc spanning nearly the entire outer ring. Confirmed: this is
  genuinely **outside** whatever protection the interior districts have, dotted with small, scattered
  clusters of homes and Rastras rather than dense urban development — a true open frontier.
- **Capricorn** — the map shows a second, smaller arc reaching the perimeter on the lower-left, at a
  noticeably denser scale than Sagittarius (contiguous industrial development, not scattered homesteads).
  Confirmed: Capricorn is **partially** exterior — a much more plentiful presence of buildings of varying
  sizes spread across a stretch of fabrication yards, some portion of which sits past whatever protects the
  interior, unlike Sagittarius's fully-open exposure.
- **The remaining ten districts** occupy the compact interior rings and are protected from the brutal climate
  by two complementary mechanisms, **confirmed by the developer 2026-07-27**: genuinely **multiple domes**
  (plural, matching Sagittarius's own canon line literally — a patchwork of district-level or zone-level
  environmental seals, not one continuous citywide dome), *plus* ordinary buildings within those domes that
  are themselves simply designed to withstand the cold, the way any real cold-climate architecture would be.
  The domes aren't doing all the work alone — they're the primary environmental seal, and the buildings
  underneath them are a second, more mundane layer of cold-hardened construction on top of that.

---

## The Governing Fact This Design Should Build On

Whatever the exact mechanism (patchwork domes, environmental seals, something else), the working picture is:
**most of Concordia is interior and protected; Sagittarius is fully exterior; Capricorn straddles the
boundary, industrial and partially exposed.** This means the "edge of the playable world" isn't one uniform
line around the whole city — it's specifically the outer boundary of the Sagittarius and Capricorn arcs, and
those two need different treatment from each other, not a single shared design.

**A useful precedent already sketched, even in a superseded file:** the old, stale-naming draft
`city-and-district_layout_-_preliminary_suggestions.md` (not current canon, but worth reusing the idea) already
described a Frostlands district "on the very edge of Concordia, overlooking the endless Antarctic ice," with
an "Outer Highway Terminus & Watchtowers" marking where maintained road stops. That specific image — a
watchtower and a dead-ending highway — is worth keeping regardless of that file's own outdated status, and
it now maps directly onto the confirmed map geometry: the three highway ramps labeled at the map's outer
edge (Hwy 37 Mountain Cut Throughway, Hwy 110 Coastal Cut Highway, Hwy 183 Janbogo Highway) all terminate
precisely in Sagittarius/Capricorn territory, since those are the only two districts that actually touch the
city's true perimeter.

---

## The Two-Layer Boundary Model, Applied Differently Per District

**Layer 1 — the felt boundary (soft, arrives first, different texture per district).**
- **Sagittarius:** worsening storm and cold effects intensify with proximity to the true edge — reduced
  visibility, stronger wind, harsher cold-exposure mechanics. Reinforces the district's own established
  thematic core (the district that had to answer "why go further" as a survival question, not an abstract
  one).
- **Capricorn:** the felt boundary is architectural/industrial first, environmental second — building
  density thins out, the fabrication yards read as progressively more exposed and less maintained, machinery
  more weather-worn, before the same worsening cold/storm effects Sagittarius has kick in closer to the true
  edge. The player should notice "this part of the industrial district feels more exposed" before the
  weather itself confirms it.

**Layer 2 — the hard boundary (physical, final, per district).** With the interior districts' own protection
now confirmed (multiple domes plus cold-hardened building construction underneath them), Sagittarius and
Capricorn's own outer edges are where the *true* city limit sits, since the map confirms they're the only two
districts that reach it — neither is domed at all, which is exactly why they're the ones exposed to open
Antarctic terrain in the first place. The actual play-space limit should be something built and visible — a
wall, a terminus checkpoint, a watchtower — not an invisible collision plane, and it doesn't need to look the
same in both districts (frontier/military-adjacent in Sagittarius; industrial/perimeter-fence in Capricorn).

**The actual stop mechanism, confirmed 2026-07-27 — two parts working together, since they solve different
holes in the same problem:**

1. **NPC checkpoint on the road itself.** A guard or checkpoint officer stationed at each highway terminus
   (Hwy 110, Hwy 37, Hwy 183) is the in-world reason travel toward Casey, Vostok/Mountain Pass Test
   Site/Kunlun, or Janbogo/the Hwy 175 junction toward the South Pole is currently closed. This is the
   quest-gate: the same checkpoint can simply wave the player through once the relevant DLC or story beat
   unlocks that route, with no separate mechanic needed for "the road is open now."
2. **Glitch-and-reposition everywhere else**, adapted from a real, confirmed precedent —
   **Cyberpunk 2077's map-edge handling**: pushing past the true boundary anywhere off the checkpointed
   roads (open Sagittarius terrain, Capricorn's fabrication-yard sprawl) triggers a warning, and persisting
   past it causes a glitch effect that repositions the player back inside the playable zone. This is the
   systemic backstop that catches every route a player might try around a checkpoint, so no invisible wall or
   awkward terrain-blocking is needed anywhere along the boundary.

**Framing note:** rather than a generic meta/fourth-wall system message, the glitch should read as *diegetic*
— a frame or sensor malfunction from extreme cold, or a loss of Arcanet signal coverage at the edge of the
network, consistent with the player character's own robotic "frame" (the same framing already used for the
implant system's "your frame can't handle this" refusal) and with the Engine-gated cold-exposure effect
covering the same stretch of terrain. The exact warning text isn't written yet — just the mechanism and its
framing.

**Production note, 2026-07-27:** the developer expects to use the glitch-and-reposition mechanism
**universally** at first — i.e., before any DLC ships, every one of the three highway termini would *also*
glitch-and-reposition the player rather than route through an actual staffed checkpoint, since there's no
open destination for any of them yet at base-game launch. The NPC-checkpoint mechanism only becomes the
active, distinct layer once a given DLC actually opens its corresponding route — until then, all three
termini behave exactly like the rest of the boundary (glitch-and-reposition only, no checkpoint dialogue).

**Why both layers, not just one:** a hard wall with no warning reads as arbitrary; a soft warning with no
firm edge either goes on forever (confusing) or needs an invisible wall anyway (same problem, just delayed).
Layering them means the player always has legible information about where they stand relative to the edge.

---

## Concrete Implementation Candidates

- **Watchtowers and an "Outer Highway Terminus"** — reusing the legacy draft's own image, and now directly
  confirmed by the actual map: the three highway ramps (Hwy 37, Hwy 110, Hwy 183) all terminate at the true
  perimeter, in Sagittarius/Capricorn territory specifically. A maintained road that visibly, deliberately
  stops, marked by a real structure (a watchtower, a checkpoint gate) rather than just trailing off, gives
  the player a concrete, findable landmark for "this is the edge" rather than a fuzzy zone. **Real
  destinations confirmed 2026-07-27** — none of these three are dead-end ramps; each actually goes somewhere,
  which reframes the terminus/watchtower structures as *checkpoints on a through-road* rather than the end of
  the road itself:
  - **Hwy 110** leads toward the city of **Casey**.
  - **Hwy 37** leads through **Vostok**, the **Mountain Pass Test Site**, and on to **Kunlun**.
  - **Hwy 183** leads toward the city of **Janbogo**, and — before reaching it — links via a junction to
    **Hwy 175**, heading in the direction of the South Pole.
- **Sagittarius: scattered homesteads thinning into true open ice** — the map shows small clusters of homes
  and Rastras, not dense development; the felt boundary here is really about *density* thinning out entirely,
  not a wall suddenly appearing.
- **Capricorn: fabrication yards thinning into exposed, unmaintained industrial sprawl** — denser than
  Sagittarius throughout, per the map, so its own version of "thinning out" reads as increasingly derelict or
  minimally-staffed yard space rather than homes disappearing.
- **Environmental storm intensity as a gradient, not a toggle** — Layer 1's cold/visibility effects (in both
  districts, once close enough to the true edge) should scale with proximity rather than snapping on at a
  fixed line.
- **Sagittarius's own failed dome-extension history as set dressing** — the Third Expansion Collapse
  (`District_Canon_Reference.md`) could be represented physically: a visibly incomplete or collapsed
  expansion attempt near the boundary, giving the edge itself narrative texture rather than being a purely
  functional wall.

---

## Open Questions

- ~~What exactly protects the ten interior districts, and is "domes" (plural, from Sagittarius's own canon
  line) the right mechanism, or something else entirely?~~ — **resolved 2026-07-27:** multiple domes (a
  patchwork, not one citywide dome) plus ordinary cold-hardened building construction underneath them as a
  second layer. See the corrected description near the top of this file.
- ~~Whether the highway network extending outward from Sagittarius... implies certain roads *do* continue
  past the boundary toward DLC subnet content~~ — **resolved 2026-07-27:** all three do, and each has a real,
  named destination rather than dead-ending — see the "Watchtowers and an Outer Highway Terminus" entry
  above (Hwy 110 → Casey; Hwy 37 → Vostok, Mountain Pass Test Site, Kunlun; Hwy 183 → Janbogo, with a Hwy 175
  junction toward the South Pole). This reframes the terminus structures as manned checkpoints on a working
  through-road, not barriers at the end of a dead-end street — worth keeping in mind for whether travel past
  them is free-roam, on-rails, or quest-gated, which is still an open question in its own right (see below).
- ~~Given the highways are confirmed through-roads rather than dead ends, is travel past Concordia's
  checkpoints toward Casey/Vostok/Kunlun/Janbogo/the South Pole meant to be free-roam, on-rails, or
  quest-gated?~~ — **resolved 2026-07-27:** quest-gated, via an NPC checkpoint stationed at each terminus that
  simply opens once the corresponding DLC/story beat unlocks that route. Until a route unlocks, that
  terminus behaves identically to the rest of the boundary (see the Layer 2 mechanism above).
- Exact mechanical representation of the cold/storm gradient (a stat/status effect? a pure visual-only cue?
  something that actually damages the player over time the further out they push?) — **developer has no
  design preference yet as of 2026-07-27; still fully open,** including whether it hooks into any existing
  MACHINE stat (e.g., Engine, since the player character has a "frame" rather than a human body) or is purely
  presentational. Worth a dedicated design pass rather than guessing at numbers here.
- ~~Whether Concordia's other ten districts have any of their own boundary-adjacent design needs~~ —
  **resolved by the actual map:** they're all fully interior, packed into the compact inner rings around the
  hub. This document's scope is correctly limited to Sagittarius and Capricorn only.
