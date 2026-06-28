# DLC 1 — Echoes of Amundsen

## Confirmed Design Elements

**Title:** Echoes of Amundsen
**Setting:** Amundsen Station ruins / Amundsen Tower scrap mountain — South Pole
**Central companion:** Kendra Heinrich (see her README for full character design)
**Arcanet subnet:** Inter-subnet relay (neutral — not assigned to any single subnet; the only pre-Split-Brain reconciliation point for all six subnet records)
**DLC position:** No hard gate — any order. Earns capstone position through design, not locks. See `DLC_PSB_Framework.md`.

---

## Design Commitments

- **Brutally, maximally, mercilessly hard by design and by lore.** Kendra Heinrich (M10, A10, N10, E10) was defeated and stranded here. Whatever did that is still present. The player's stats will almost certainly be substantially lower than hers. The DLC is designed as the natural endpoint of a fully developed build — something only a character who has been preparing for it can survive.
- **The reward justifies the difficulty.** Kendra is among the most powerful recruitable companions in the game. She also effectively wins a portion of the Final Climax by default through Presence-Based Deterrence (Upper Earth operatives flee rather than call reinforcements). The difficulty of earning her must be proportional to what she provides.
- **Enemies are unique to the South Pole.** No enemy type in this DLC appears in the main game or other DLCs. They must be credibly capable of defeating Kendra — anything less would be lore-incoherent.
- **The environment is a co-antagonist.** The South Pole itself fights the player. This is not flavor — it is a mechanical reality designed into every area.
- **Equipment carry restriction (Honest Hearts analogue).** The player cannot bring everything. A carry limit is imposed at DLC entry. Exact weight number TBD, but the principle is confirmed: preparation decisions matter before entry. Minimum five ways to raise the limit must exist (per series design law).
- **Point of no return is the geography.** Concordia is 1,660 km from the South Pole. Once in, the player is in. No supply runs, no reinforcements, no retreat.

---

## Environmental Hazards — Standard Mode

All of these function without Hardcore mode. They are base-layer consequences of the environment, not survival meter mechanics.

### Thermal Exposure
Open and uninsulated areas deal continuous cold damage to the player. The damage rate varies by exposure level — a wide Antarctic plain is more lethal than a sheltered scrap tunnel. Heat sources (functioning geothermal vents, enclosed ruin sections, improvised shelter) stop the damage. Navigation *is* thermal management — the player must plan movement around shelter chains.

Enemies that force the player out of cover and into open cold are doubly dangerous: they're a combat threat and a thermal threat simultaneously.

### Coldshock Condition
As thermal exposure accumulates, the player develops Coldshock — Inner Tepenia's equivalent of hypothermia. Coldshock does not kill directly; it degrades.

**Critical mechanic:** As Coldshock worsens, Siligel (robot food) provides diminishing returns. The cold impairs the protagonist's ability to process nutrition efficiently. At severe Coldshock, eating the same amount of Siligel provides a fraction of the benefit it would at full health. This creates a resource pressure spiral in the South Pole: being cold makes food less useful, which means you need more food to stay functional, which is scarce.

**Siligel is robot food — not lubricant, not blood, not a structural fluid.** Cold does not deplete Siligel. It reduces how much benefit the player gets from eating it. The distinction matters.

**Coldshock stages:**

| Stage | Condition | Siligel Efficiency | Additional Effects |
|---|---|---|---|
| 0 | Normal | 100% | None |
| 1 | Chilled | 80% | Minor Agility penalty |
| 2 | Cold | 60% | Agility penalty increases; Investigation begins degrading |
| 3 | Coldshock | 40% | Significant stat penalties across multiple MACHINE stats |
| 4 | Deep Coldshock | 20% | Severe penalties; movement impaired |
| 5 | Critical | 5% | Approaching emergency shutdown; Siligel nearly useless |

**Recovery:** Finding a heat source or shelter reduces Coldshock stages. In standard mode, reaching shelter and resting fully reverses the condition. Speed of recovery depends on the quality of the heat source and time spent there.

### Structural Collapse
The Amundsen Tower scrap mountain is millions of tons of debris from a near-orbit impact settling over years. It is not stable.

- Specific areas are actively unstable. Gunfire, explosions, and heavy movement in marked zones can trigger localized collapses.
- This creates stealth pressure independent of enemy detection — noise management matters because the environment punishes it.
- Collapse events are telegraphed by audio and visual cues (groaning metal, visible structural sway) so the player who pays attention survives. The player who rushes does not.

### Debris Falls
- Triggered by noise or player weight in specific unstable overhead zones.
- Lethal if caught directly. Near-miss deals heavy damage.
- Audio/visual telegraph before trigger (creaking, shifting, dust falling).
- A mechanic that rewards spatial awareness and punishes charging through spaces without looking up.

### Blizzard Events
- Periodic. Timed. Predictable after the first encounter — the player learns the rhythm.
- Near-zero visibility during the event. Range-based combat becomes unreliable; close-quarters threats dominate.
- Enemy encounters during a blizzard are significantly more dangerous than the same encounter in clear conditions.
- A prepared player retreats to a defensible position before the blizzard hits. An unprepared player is caught in the open.
- Can be used strategically — blizzard conditions disadvantage enemies that rely on sight as much as they disadvantage the player.

### Magnetic Anomalies
The tower's destruction left zones of disrupted magnetic and electronic interference throughout certain ruins sections.

- Navigation systems unreliable in anomaly zones.
- Targeting assistance degrades or fails.
- HUD elements glitch.
- Extended exposure (Hardcore: also corrupts memory integrity — see Hardcore Mode document).
- Some enemy units are specifically adapted to operate inside anomaly fields — they function normally where the player's systems don't. This is an intentional design asymmetry.

### Crevasse Terrain
The Antarctic ice beneath and around the scrap mountain has fractured from the tower's original impact.

- Hidden crevasses in areas that look stable. Instant-death falls.
- Taught through clear sensory cues: cracking sounds underfoot, ice discoloration, subtle visual texture differences, visual flexing of the surface.
- The player who pays attention survives. The player who sprints across terrain they haven't read doesn't.

---

## Enemy Design — Open Design Question

**The central unanswered question: what defeated Kendra Heinrich?**

Whatever it is must be:
- Unique to the South Pole / Amundsen Station ruins — no equivalent anywhere else in the game
- Credibly capable of defeating a character with M10, A10, N10, E10
- Thematically connected to the site (Long Night War, tower destruction, inter-subnet relay going dark)
- A legitimate final challenge for a maxed-out player at the end of their build arc

**Three candidate directions — decision pending:**

**Option A — Upper Earth Autonomous Defense Network (UADN)**
Left behind after the deliberate destruction of Amundsen Tower. A distributed system of cold-adapted, self-repairing, coordinated units designed to deny recovery of the site. They know the terrain. They use the environment as a weapon (pushing targets into open cold, triggering structural instability). They didn't beat Kendra in a single fight — they contained her, wore her down through attrition, and let the cold finish the work. The Long Night War is still being fought here by hardware that doesn't know the war ended.

**Option B — Amundsen Station Security Systems Gone Rogue**
The station's own defense infrastructure triggered total lockdown when the tower was destroyed. Years of cold and isolation have corrupted their protocols — they are no longer fully rational, which makes them harder to counter than a competent enemy. They do almost-logical things in ways that don't follow predictable tactical patterns.

**Option C — Something That Survived the Fall**
The tower was carrying things when destroyed. Some survived the crash. The cold preserved it. The isolation let it establish itself. What it is connects to what Upper Earth was doing with the tower — a design question that reaches into the broader lore.

*Note: Option A is the current leading candidate — a network architecture gives the DLC multiple stages of revelation and the ability to change enemy behavior when sub-components are destroyed. Decision to be confirmed during Phase 7 DLC design.*

---

## South Pole DLC — Multiple Approaches to the Central Challenge

At minimum five distinct approaches must exist for defeating the central threat (per series design law). Confirmed approaches so far:

1. **Ji-Eun Kim's anti-sensor cloaking technology** — not a guaranteed win; provides a significant edge in surviving and navigating content that would otherwise be immediately lethal. One of the most valuable pre-DLC preparation items.
2–5. TBD during Phase 7 design.

---

## PSB Framework Connection

See `DLC_PSB_Framework.md` for how DLC 1 connects to the Planetary Split Brain questline. The South Pole is the only location containing the pre-Split-Brain unified Arcanet archive — the only reconciliation point for all six subnet records. This makes it both the hardest DLC content and the one with the deepest lore stakes.

---

## Open Questions

- [ ] What defeated Kendra — confirm Option A, B, or C (or hybrid)
- [ ] Specific enemy types and their designs
- [ ] Exact carry weight restriction number for DLC entry
- [ ] Five minimum approaches to the central challenge (only Ji-Eun cloaking confirmed so far)
- [ ] Main storyline structure and beats
- [ ] South Pole side content
- [ ] Kendra romance mini-quest beats (Phase 7)
- [ ] Connection between DLC events and The Vigil [NAME TBD] faction in Concordia
