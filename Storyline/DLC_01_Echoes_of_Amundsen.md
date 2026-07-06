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

**Mechanism specified 2026-07-05** (see `Theoretical-Calculations/Amundsen_Tower_Space_Fountain_Design.md`'s "Primary Purpose" section and `Energy_Grid_Failure_Rationale.md` #11): Amundsen Tower wasn't just a tall structure that fell — it was a continuously circulating electromagnetic mass driver carrying ~324 GW net, with a network of superconducting bearing stations spread across its full height, and the whole system doubled as the continent's energy-regulating flywheel. When it collapsed, that wasn't a clean shutdown — it was a catastrophic failure of a system built to run continuously, at civilization-scale power, indefinitely. **Some severed sections of the accelerator track and damaged bearing stations plausibly still hold trapped, dangerous residual charge, over a decade later** — not just ambient "weirdness," but genuine live-electrical hazards buried in specific wreckage zones. This directly parallels the newly-established emergency-power-feedback mechanic (drawing down the intact pellet stream too far risks structural collapse) — here, the danger is the inverse: wreckage that's already structurally failed but electromagnetically hasn't fully discharged.

- Navigation systems unreliable in anomaly zones.
- Targeting assistance degrades or fails.
- HUD elements glitch.
- Extended exposure (Hardcore: also corrupts memory integrity — see Hardcore Mode document).
- Some enemy units are specifically adapted to operate inside anomaly fields — they function normally where the player's systems don't. This is an intentional design asymmetry.
- **New, 2026-07-05:** specific wreckage zones (identifiable superconducting bearing-station remnants, severed accelerator-track segments) can carry a genuine live-discharge hazard — sudden, damaging electromagnetic pulses triggered by proximity, movement, or metal contact, distinct from the passive "interference" effects above. Telegraphed the same way as Structural Collapse and Debris Falls (audio/visual cues — humming, arcing light, hair-raising static) so an attentive player can route around them, consistent with this DLC's existing "pays attention survives, rushes doesn't" design language.

### Crevasse Terrain
The Antarctic ice beneath and around the scrap mountain has fractured from the tower's original impact.

- Hidden crevasses in areas that look stable. Instant-death falls.
- Taught through clear sensory cues: cracking sounds underfoot, ice discoloration, subtle visual texture differences, visual flexing of the surface.
- The player who pays attention survives. The player who sprints across terrain they haven't read doesn't.

---

## What Defeated Kendra Heinrich — Confirmed Design

**Primary framework: Option D (environment + attrition + enemies that prevent recovery).**

Kendra was not defeated by something stronger than her. She was defeated by the compounding of the environment degrading her systems over time and enemies she could have beaten at full capacity — but couldn't at 60%, after weeks of exposure with no resupply, no shelter, and no way out. She didn't lose a fight. She lost a war of attrition she was fighting alone.

Options A (networked autonomous defense systems) and B (station security systems gone rogue) exist as minor/lesser enemy types within this framework — they are part of what kept her from recovering and kept her pinned, not the primary explanation for her defeat. They are not the answer. The system is the answer.

The player's advantage over Kendra is not being stronger than her. It is having support, preparation, and knowledge she went in without. See `DLC_01_Enemy_Design_Options.md` for the full design discussion.

**Enemy specific types and designs:** TBD during Phase 7.

---

## Kendra's Situation — What the Player Arrives To Find

The game is set approximately 10–15 years after the Long Night War. Kendra has been stranded at the South Pole for that entire time.

During and immediately after the battle, she killed as many Upper Earth forces as she could. When she was too badly damaged to continue fighting in the open, she did two things: she set up automated weapons systems in the surrounding ruins to continue killing any subsequent Upper Earth forces that came, and she retreated inside the actual Amundsen-Scott South Pole Station — the pre-war scientific facility, the real-world building that exists at the South Pole today — and locked it from inside.

The automated defenses she set up are still running. They have been killing anything that approaches for a decade or more. This is why her own defense systems are what the player has to fight through to reach her — she built them herself, and they don't know to stop.

Inside the station, she has been waiting. Low on power reserves. Low on energy. No way to call for help (and too proud to do so even if she could). After 10–15 years of this, by the time the player arrives, she is extremely weak and frail. The war goddess who wiped out an Upper Earth assault force is barely functional. The station is locked tight. She does not know anyone is coming.

The player must find a way in. See the section below.

---

## Getting Into the Station — Confirmed Entry Methods

The Amundsen-Scott Station is locked from inside by Kendra. The automated defense systems cover the exterior approaches. There are multiple ways to reach her — confirmed minimum of nine, spanning environmental discoveries, brought items and companions, perks, and traits.

**Environmental (found in the DLC — minimum 3):**

1. **Underground utility tunnel network** — The Amundsen-Scott station has an extensive underground tunnel system carved into the ice, built during the pre-war era. One entrance is buried under accumulated debris near the outer ruins. Requires Investigation 7 to locate. Then Lockpick 45 or Repair 35 to open the frozen-shut hatch. (On replays after first completion, Naizelle's Physical Gap Reading can substitute for the Investigation 7 threshold.)

   *Design note for future development:* The tunnel interior should be populated with lore content revealing what happened here during the Long Night War — terminal entries, personal journals, audio logs, environmental storytelling (abandoned equipment, signs of hasty evacuation or last stands, physical evidence of what the station was doing when the war hit). This is one of the few locations where pre-war primary sources are physically present rather than archived. The content of what the player finds should be developed during Phase 7 storyline work, in coordination with whatever is confirmed about Upper Earth's use of the tower and the events of the Long Night War at this site.

2. **Breach point in the damaged section** — During Kendra's final battle, part of the station exterior took impact damage. She sealed it from inside with improvised materials. From outside, a player with Might 8+ or a demolition item can force an opening. Getting there requires surviving the exterior kill zone — this approach pairs naturally with any defense suppression method.

3. **Emergency geothermal access hatch** — On the far side of the station, opposite the main entrance, a pre-war maintenance hatch for the station's geothermal power infrastructure. Kendra was too badly damaged to seal it during lockdown. Reaching it requires crossing a stretch of completely open ice with no cover — lethal without defense suppression, stealth capability, or cold resistance. Once reached: Lockpick 30 or Repair 25.

4. **Ventilation shaft** — External ventilation intakes are buried in the snow at several points around the building. One is accessible if cleared and navigated. Agility 8 required to move through without getting stuck. Finding the right intake requires Investigation 5 or thorough perimeter exploration.

**Brought items and companions:**

5. **Ji-Eun Kim's anti-sensor cloaking device** — A portable device provided by Ji-Eun before DLC entry (she does not accompany the player). Suppresses the player's sensor signature long enough to approach the main entrance without triggering the automated defenses. At the door: Lockpick 55 or Hacking 60 to bypass Kendra's lock. Without the cloaking, the defenses fire before the player can work the lock. This is the most direct approach to the main entrance.

6. **Military-grade breach charge** — A shaped demolition charge capable of opening a reinforced door without structural collapse. Acquired through specific main game faction contacts or found in the outer ruins. No skill threshold — the tool does the work. Uses a carry slot.

7. **Advanced electronic lockpick kit** — A specialist tool purchased from a specific vendor in the main game (Gemini or Aquarius supplier). Bypasses electronic locks that standard lockpicks cannot handle. Lockpick 40 still required — the kit handles the electronic layer; skill handles the mechanical. Lighter than the breach charge.

**Perks:**

8. **Structural Exploitation** (Repair/Engineering 75+ or named perk in the engineering tree) — The player has studied building design thoroughly enough to identify fault lines and leverage points invisible to others. A weakened section of the exterior that no one else could breach becomes a viable entry point. No additional tools needed — knowledge is the tool.

9. **Dead Air** (high-level Stealth perk, Agility 7+) — Advanced stealth capability allows movement through the automated defense kill zone without triggering fire. Combined with reaching any of the environmental entry points, this makes otherwise-suicidal exterior approaches survivable for a stealth build.

**Traits:**

10. **Cold-Tempered** (character creation trait) — Exceptional thermal resistance. One entry route — the exposed crossing to the emergency geothermal hatch — is simply lethal to a standard build regardless of HP. A Cold-Tempered character can make the crossing without additional assistance. The one entry only cold-resistant builds can take alone.

**MACHINE stat threshold:**

11. **Call Out to Her** (Humanity 8+) — If the player reaches the station's external intercom point (requiring cloaking, Dead Air, or one of the environmental approaches to the near side of the building), they can attempt to speak to Kendra directly through the speaker system. Humanity 8 is enough to reach her — to make her understand the war is over, that someone came specifically for her, that she doesn't have to be alone anymore. She opens the door herself. The most thematically significant entry method. The only one that changes the emotional register of everything that follows.

---

## South Pole DLC — Multiple Approaches to the Central Challenge

At minimum five distinct approaches must exist for defeating the DLC's central threat (per series design law). Confirmed approach so far:

1. **Ji-Eun Kim's anti-sensor cloaking technology** — provides a significant edge in surviving and navigating content that would otherwise be immediately lethal. The single most valuable pre-DLC preparation item.
2–5+. TBD during Phase 7 design.

---

## PSB Framework Connection

See `DLC_PSB_Framework.md` for how DLC 1 connects to the Planetary Split Brain questline. The South Pole is the only location containing the pre-Split-Brain unified Arcanet archive — the only reconciliation point for all six subnet records. This makes it both the hardest DLC content and the one with the deepest lore stakes.

### A Dedicated Guardian System Protecting the Archive (established 2026-07-05)

Per the now-confirmed mechanism in `DLC_PSB_Framework.md`, Upper Earth's strike on Amundsen Tower didn't just destroy Tepenia's space access — it very likely caused the Planetary Split Brain itself, severing every inter-subnet Arcanet link at once. If Upper Earth's forces understood what they were doing when they hit this specific site — not just "destroy the space elevator" but "sever Tepenia's entire information network in one strike" — it's plausible they left something behind specifically meant to make sure that severing stays permanent: a **dedicated denial system guarding the pre-Split-Brain archive itself**, separate from Kendra's own defenses and separate from the general environmental hazards above.

This raises the stakes of the archive specifically, rather than treating it as incidental loot found at the end of a hard dungeon. Structurally, this should be the DLC's own distinct challenge layered on top of (not folded into) "get past Kendra's automated defenses" and "survive the environment" — a third, separate obstacle whose entire purpose is protecting exactly the thing the DLC's deepest lore payoff depends on. Whether this is an automated Upper Earth system still running after 10-15 years, a booby-trap/failsafe triggered by archive access attempts, or something else is TBD — the design commitment here is only that the archive should not be trivially accessible once the player gets past Kendra's own perimeter; reaching it should be its own achievement.

## Cross-DLC Bypass Gifts — Master Tracking List (established 2026-07-05)

Per the project's Cross-DLC Bypass Design Law (`Storyline/DLC_Overview.md`, `project_cross_dlc_survival_gifts` memory), every part of the game — the base game and each of the 6 subnet DLCs — contributes exactly one guaranteed, fully optional piece of "help" toward Echoes of Amundsen. Tracked here in one place for this DLC specifically:

| Source | Gift | Status |
|---|---|---|
| **Base game** | Ji-Eun Kim's anti-sensor cloaking technology — lets the player approach past Amundsen Station's automated defenses instead of fighting through them | ✅ Confirmed |
| **DLC 2 (Byrd)** | TBD | ⬜ Not yet designed |
| **DLC 3 (Palmer/Peninsula)** | TBD — not the Archivist's Trail below, which counts toward DLC 5 instead | ⬜ Not yet designed |
| **DLC 4 (Mawson)** | The Ice Cold Buddhism thread's extreme-cold survival perk (exact name TBD) — reduces or removes the Coldshock/extreme-cold penalty | ✅ Confirmed, perk name pending |
| **DLC 5 (Halley)** | "The Archivist's Trail" — the physical decryption codekey that skips the archive's extreme decryption skill check entirely | ✅ Confirmed |
| **DLC 6 (Janbogo/Ross)** | TBD | ⬜ Not yet designed |
| **DLC 7 (Mirny)** | TBD | ⬜ Not yet designed |

### The Archivist's Trail — A Cross-DLC Bypass for Decrypting the Archive (established 2026-07-05)

Decrypting the Amundsen Station archive by force is meant to be an extreme skill check — placeholder figures for discussion: 10 Calculation, 10 Nerve, 10 Engine, and 100 Hacking, high enough that almost no build reaches it without deliberate specialization. **A discoverable, fully optional breadcrumb trail — starting in an entirely different DLC — lets the player bypass that check with a physical decryption codekey instead**, following the established Cross-DLC Bypass Design Law (see `DLC_Overview.md` and `project_cross_dlc_survival_gifts` memory) — optional side content only, never delivered by an NPC or main-quest beat.

**The trail:**

1. **Juan Carlos's own original archive (Palmer subnet, DLC 3):** exploring Juan Carlos's badly-destroyed archive — ground floor, or possibly a basement office, personal effects still present (art on the walls, non-functional terminals) — the player finds a personal record: a handwritten note or audio log from the archivist himself, documenting (not personally performing) the fact that Tepenian truckers had just hauled out the last batch of encrypted datadrives, being consolidated into what would become Amundsen Station's unified archive (see `Specs/Juan_Carlos.md` and `project_juan_carlos_archive_origin` memory for the established lore this pays off). He notes the drives were "encrypted pretty well," that a colleague has a codekey, but that he keeps a backup one himself "just by the nightstand" at his wife's family home — and signs off mentioning a friend has a surprise gift waiting for him at a specific bar, back in Esperanza, "where all the other families are."

2. **Esperanza (Palmer subnet, DLC 3):** the player can find the ruins of that bar. A terminal note there references the friend's gift to the archivist (a small, personal detail — charming but not narratively significant on its own) and mentions his home being better for having received it.

3. **The archivist's home (Esperanza):** identifiable by his name on personal effects, plus references to his wife's own things — photos, letters, parcel shipments — that let the player logically deduce she was originally from **Sanay** (Halley subnet, DLC 5) — her hometown, not a childhood home, since she's a robot — including an extremely specific description of her house there, and a physical door key the player can take.

4. **Sanay (Halley subnet, DLC 5):** the player locates the described house. Multiple ways in, consistent with the series' multiple-approaches design law:
   - **The key**, if carried from Esperanza — opens the door directly, no check.
   - **Lockpick 50** (placeholder figure) — picks the lock without the key.
   - **Investigation 7 + Agility 6** (placeholder figures) — the player notices a slightly offset section of the back wall, then jiggles it open, bypassing the front door entirely.

   Inside, in a drawer, the player finds the decryption codekey the archivist's note referenced.

5. **Back at Amundsen Station (DLC 1):** using the codekey decrypts the archive directly — no skill check required at all, regardless of build.

**Cross-DLC geography note, resolved 2026-07-05:** the trail begins and runs mostly through DLC 3 (Juan Carlos, then Esperanza — both Palmer subnet), only crossing into DLC 5 (Sanay, Halley subnet) for the final key location, before paying off in DLC 1. Confirmed by the developer: this counts as **DLC 5 (Halley)'s** guaranteed gift toward Kendra's DLC specifically, since that's where the actual bypass item is physically located — DLC 3 (Palmer)'s own geography here is the discovery-trail setup for DLC 5's gift, not a separate contribution toward its own quota. DLC 3 still needs its own, separate gift designed later.

---

### Upper Earth's Own Presence at the Site — Flagged, Not Yet Added (2026-07-05)

A related idea was raised and discussed but not yet written in as confirmed design: whether Upper Earth left actual personnel or active military assets at the site (as opposed to just automated denial systems, covered above). The developer's own objection is a real logistical one — by the time the player arrives, any such personnel would have been there 10-15 years, which requires one of: (A) rotating shifts (~6 months each), (B) continuous presence with a nearby resupplied base camp, or (C) longer rotations (~1-2 years) with resupply. Any of these is *possible*, but needs background investigation — how Upper Earth would logistically sustain a South Pole presence for over a decade, what that implies about their broader post-war relationship with/awareness of Tepenia, and why they'd consider this specific site worth that ongoing cost — before it's added as confirmed design. Not contradicted, just deferred. See `TODO.md`.

---

## Open Questions

- [x] What defeated Kendra — **confirmed: Option D (environment + attrition) as primary; A and B as minor elements**
- [x] How Kendra's defenses are still running — **confirmed: she set them up herself during the battle and retreated inside**
- [x] Where Kendra is — **confirmed: inside the actual Amundsen-Scott South Pole Station, locked from inside, 10–15 years stranded**
- [x] Minimum ways into the building — **confirmed: 11 methods across environmental, brought, perk, and trait categories**
- [ ] Specific enemy types and their designs — two new hazard/threat directions established 2026-07-05 (residual electromagnetic wreckage hazards, a dedicated archive-guardian system), a third (Upper Earth's own on-site personnel/assets) flagged but deferred pending logistics investigation — see above
- [x] Archive decryption bypass — **confirmed 2026-07-05: "The Archivist's Trail," a cross-DLC breadcrumb chain (Juan Carlos → Esperanza → Sanay) yielding a physical codekey that skips the extreme decryption skill check entirely — see above**
- [ ] Exact carry weight restriction number for DLC entry
- [ ] Five minimum approaches to the central challenge — only Ji-Eun cloaking confirmed; 4+ TBD
- [ ] Main storyline structure and beats
- [ ] South Pole side content
- [ ] Kendra romance mini-quest beats (Phase 7)
- [ ] Connection between DLC events and The Vigil [NAME TBD] faction in Concordia
