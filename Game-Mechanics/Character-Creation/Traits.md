# Traits

**Marked for future review (2026-07-04):** every trait in this file — old and newly added alike — is provisional. Reaching the 25-trait target doesn't mean any individual trait is locked in; names, bonuses, penalties, and stat/skill gates are all subject to adjustment once actual design & development work reaches character creation, and adding more traits later may prompt revisiting ones already here (for balance, overlap, or thematic fit). Treat this whole file as a working draft, not final content.

Traits are major, permanent choices made during **Character Creation**. You may select **up to 4** traits. Taking more traits progressively increases overall difficulty.

**Target trait count, established 2026-07-04 (modeled on Fallout: New Vegas's 10 base + 6 Old World Blues, max 2 selectable — scaled up considerably):**
- **Base game: 25 traits** (target; **27 currently designed** as of 2026-07-04 — see consolidation note below and the Fallout-Adapted Traits section — target already cleared, with room for a few more if good ideas come up).
- **Each of the 7 DLCs adds +5 traits** to the pool (6 subnet DLCs + the South Pole DLC, Kendra Heinrich's "Echoes of Amundsen").
- **Grand total with base game + all 7 DLCs: 60 traits** (25 + 7×5).
- **Max selectable at character creation: 4** (up from FNV's 2) — a player who owns every DLC chooses from the full 60-trait pool but still only picks up to 4, same as a base-game-only player choosing from 25.

**Consolidation note (2026-07-04):** this file previously listed only 10 traits; 7 more (the "AP-Economy" group below) existed separately in `Core-Mechanics/Action_Points_Perks_and_Traits.md` and weren't being counted toward the trait total anywhere. Merged here so this file is the single authoritative trait list — 17 total, not 10.

**Redesigned in full, 2026-07-28** — all 10 originally referenced skill names that don't exist anywhere in
the real, finalized 25/26-skill list (`Skills.md`, locked 2026-07-26), a holdover from an older, pre-lock
skill taxonomy. Every trait below has been rebuilt against real skills, with more varied mechanic shapes
(conditional bonuses, access-gate discounts, resource-cost reductions, stat trades) instead of the old
uniform "+15%/+15% skill, -1 stat" pattern.

| Trait Name | Bonuses | Penalties | Thematic Fit |
|---|---|---|---|
| **Lattice Mind** | +20% Repair success on jury-rigged/patched-together equipment<br>Hacking targets that are themselves improvised/non-standard systems require 1 tier lower access threshold | -1 Humanity | Hidden paths, tech innovators — sees hidden order in patched-together systems, not people |
| **Cold-Blooded Optimizer** | +20% Chemistry when synthesizing siligel or industrial compounds<br>-20% material cost when repairing/crafting via efficiency-optimized methods<br>+2 Calculation | -2 Humanity | Industrial efficiency, cold optimization over warmth |
| **Empathic Bridge** | +20% Speech effectiveness specifically in de-escalation/conflict-avoidance dialogue<br>+2 Humanity | -1 Might | Social, non-lethal diplomats |
| **Ripple Intuitive** | +20% Insight when reading a volatile/escalating situation<br>+25% effect from environmental hazards triggered in combat (fire, explosives, hazardous terrain) | -1 Calculation while under high stress | Crisis exploitation — reads and exploits chaotic, cascading situations |
| **Frontier Hardened** | +20% Survival and Outdoorsman effectiveness while outside the domed/interior districts<br>+15% Repair specifically on field repairs made away from proper facilities<br>+1 Engine while outside domed/interior districts | -1 Humanity while inside civilized/interior districts | Sagittarius/frontier explorers |
| **Narrative Ghost** | +20% Deception<br>+15% Narrative<br>Unlocks an extra dialogue option to probe any NPC for rumors/information<br>+1 Nerve | -1 Humanity ("harder to build genuine trust") | Information brokers, manipulators |
| **Engine Overclocker** | +1 Engine<br>Once per combat, when at 0 AP, immediately gain a burst of +3 temporary AP | After using the burst: -2 Engine and -2 Agility until the end of combat (burnout) | High-risk players, emergency-overclock builds |
| **Humanity Anchor** | +1 Humanity<br>+20% Insight specifically when interacting with the active companion<br>Bond-building progress with the active companion accelerates (`Core-Mechanics/Fragmentation_Matrix.md`) | -10% skill gain specifically in Calculation-governed skills (Chemistry, Hacking, Cryptography, Energy Weapons) | Roleplay / companion-focused builds |
| **Undergrid Phantom** | +20% Repair<br>+15% Sneak specifically in low-light or underground environments | -1 Might | Virgo infiltrators |
| **Sonic Resonance** | +20% Narrative and Speech when performing publicly<br>Reputation gains specifically in Leo progress faster (ties to the district's own "recognition levels" system, `District_Canon_Reference.md`) | -1 Might | Leo artistic/performer builds |

### AP-Economy Traits *(merged 2026-07-04 from `Core-Mechanics/Action_Points_Perks_and_Traits.md`, where they originally lived)*

| Trait Name | Bonuses | Penalties | Thematic Fit |
|---|---|---|---|
| **High-Output Frame** | +2 base AP per turn | -1 to all MACHINE stats when below 50% health (systems running hot) | Aggressive, high-health tank builds |
| **Efficient Design** | Movement costs 1 fewer AP per turn (minimum 1) | -1 Agility | Mobility/exploration builds |
| **Overclocked Prototype** | +3 AP on the first turn of every combat | -2 AP on all subsequent turns of that combat (systems need time to stabilize) | Alpha-strike, opening-heavy playstyles |
| **Fragile but Fast** | +2 Agility | Taking damage costs 1 AP on the next turn (stackable up to -3) | Glass-cannon Agility builds |
| **Steady Nerves** | Nerve counts as 2 higher for the AP modifier calculation | -1 Agility | NODE/tactical combat builds |
| **Minimalist Frame** | +15% movement speed when carrying less than 30% of carry weight | -2 AP per turn when encumbered | Light/stealth scout builds |
| **Echo Chamber** | Occasionally gain +2 temporary AP near Arcanet nodes or during blackouts (unpredictable) | Occasionally lose 1-2 AP at the start of your turn due to system interference | Arcanet-adjacent, unpredictable playstyles |

### Fallout-Adapted Traits *(added 2026-07-04, ported from Fallout: New Vegas's 16-trait roster after a comparison pass — see `project_fallout_trait_perk_adaptation` memory)*

| Trait Name | Bonuses | Penalties | Thematic Fit |
|---|---|---|---|
| **Built to Destroy** | +5% critical hit chance | Equipment (weapons, armor, robot components) degrades 15% faster | High-risk-reward aggressive builds |
| **Good Natured** | +5% effectiveness with all non-combat skills | -5% effectiveness with all combat skills | Diplomats, non-lethal builds |
| **Fast Shot** | Ranged weapon attacks cost 20% less AP | -20% ranged weapon accuracy | Volume-of-fire, aggressive gunplay |
| **Trigger Discipline** | +20% ranged weapon accuracy | Ranged weapon attacks cost 20% more AP | Precision, patient gunplay — direct opposite of Fast Shot |
| **Heavy Handed** | +20% melee/unarmed damage | -60% critical damage with melee/unarmed | Might-focused brawlers |
| **Kamikaze** | +10 AP | -15% armor effectiveness (damage resistance) | High-AP glass-cannon builds |
| **Hoarder** | +25 carry weight *(exact lbs/kg baseline TBD pending Inner Tepenia's own carry-weight economy numbers)* | -1 to all MACHINE stats while carrying less than the carry-weight threshold *(TBD, same dependency)* | Scavenger/salvage-culture builds (Undergrid, Rothera/Troll/Belgrano mechanic culture) |
| **Skilled** | +5% effectiveness to every skill | -10% XP gained | Generalist builds |
| **Claustrophobia** | +1 to all MACHINE stats while outdoors (Frostlands, exposed terrain) | -1 to all MACHINE stats while indoors (enclosed districts, Undergrid) | Frostlands/Sagittarius explorers |
| **Agoraphobia** *(added 2026-07-04, the user's own requested counterpart to Claustrophobia — exact opposite effect)* | +1 to all MACHINE stats while indoors | -1 to all MACHINE stats while outdoors | Undergrid/enclosed-district specialists |
| **Wild Wasteland** *(added 2026-07-28 — see its own dedicated file, `Wild_Wasteland_Trait.md`, for full design)* | **None — zero stat effect**, matching the real FNV trait exactly | **None** | Purely a content-flag: swaps in/adds special encounters and references throughout the game, mixing in-universe absurdism with real-world meta references; quantity and placement decided organically over time, not fixed upfront |
| **Hot Tempered** *(added 2026-07-28, renamed from FNV's "Hot Blooded" — robots run on synovial-fluid-equivalent lubricant rather than blood in the literal sense, so the developer renamed it to fit; verified against the real perk)* | +15% damage while below 50% health | -2 Humanity, -2 Agility, and -2 Investigation while below 50% health *(Perception → Humanity, per `MACHINE_Stats.md`'s own stated FNV-equivalent mapping — Humanity = "Perception + Charisma"; Investigation added on top per developer request, since Investigation is this system's own pattern-recognition/analysis stat — another facet of what a real loss of Perception would degrade)* | Aggressive, low-health-threshold glass-cannon builds — pairs naturally with All-In Brawler/Kamikaze |
| **Loose Cannon** *(added 2026-07-28, verified against the real perk — AP-cost translation follows the same pattern already used for Fast Shot)* | Thrown weapon attacks cost 30% less AP | Thrown weapons have 25% less range | Volume-of-throws builds (`Combat/Throwing_Weapons.md`) |
| **Small Frame** *(added 2026-07-28, verified against the real perk — currently decorative, see note below)* | +1 Agility | Fragile limbs (25% extra limb damage) *(decorative until a limb-specific damage system exists — see `Perks/FNV_Perk_Cross_Reference_Audit.md`'s "Blocked on a Missing System" table and the matching `TODO.md` entry)* | Agility-focused builds willing to trade limb durability for speed |

**Limb-specific damage system — developer-confirmed wanted, 2026-07-28.** Small Frame's own penalty depends
on it existing, and the developer explicitly confirmed (independent of this trait) that "limb-crippling
should absolutely be a functionality in Inner Tepenia, just like in Fallout." This elevates the existing
`FNV_Perk_Cross_Reference_Audit.md`/`TODO.md` blocker (previously flagged only for Adamantium Skeleton/Eye
for Eye) from a neutral "blocked" note to a confirmed future system — see those files' updated entries.

**Cross-series note on Claustrophobia/Agoraphobia, flagged 2026-07-28 — for future reference, not an Inner
Tepenia change:** both traits will be **absent from Outer Tepenia 1 and 2**. In both games the player is
either piloting a ship in space or inside orbital infrastructure interacting directly with other characters —
there's no meaningful indoor/outdoor distinction left for either trait to key off, rendering the whole
concept pointless in those two settings. **Both traits return for Outer Tepenia 3 ("New Centauri")** — that
installment is set in the Centauri star system, where inhabited, landable planets restore a genuine
outdoor/indoor distinction for the traits to apply to. See `project_outer_tepenia_series` memory for the
fuller cross-series context this fits into.

**Status check, 2026-07-28 — reconciling against the full FNV 16-trait roster the developer dropped in
`to-be-integrated/Fallout_New_Vegas_-_traits_-_full-list.txt`:** 13 of 16 now addressed (the 9 original plus
Wild Wasteland, Hot Tempered, Loose Cannon, Small Frame). **3 remain, each blocked on a prerequisite system
that doesn't exist yet, confirmed 2026-07-28:**
- **Early Bird** (day/night-dependent SPECIAL bonus/penalty) — needs a day/night cycle, which doesn't exist
  anywhere in the current docs (same blocker already flagged for the FNV perks Night Person/Solar Powered in
  `FNV_Perk_Cross_Reference_Audit.md`).
- **Four Eyes** (+Perception while wearing glasses, permanent −1 otherwise) — needs a robot equivalent of
  "wearing glasses": some kind of equippable/removable optical or sensory augmentation slot. **Genuinely new
  gap, not previously flagged anywhere.**
- **Logan's Loophole** (chems last longer, addiction set to zero, locks level cap at 30) — needs a robot
  equivalent of substance addiction, distinct from Glitch-Coolant (which is confirmed social/flavor, not a
  combat-chem or addiction mechanic) — same blocker already flagged for the FNV perks Chemist/Chem Resistant/
  Implant GRX in `FNV_Perk_Cross_Reference_Audit.md`.

### Stat-Gap Traits *(added 2026-07-24, marked for possible future renaming — see the gap note below)*

| Trait Name | Bonuses | Penalties | Thematic Fit |
|---|---|---|---|
| **Load-Bearing** | +2 Might | -1 Agility | A frame built for raw output at the cost of nimbleness — Aries/Power Core culture |
| **Cold Calculation** | +2 Calculation | -1 Humanity | Thought optimized past the point of patience for messy human/robot feeling — Capricorn/Gemini technocrat builds |
| **Bridge Feedback** | +2 Investigation while jacked in | -1 Humanity while jacked in | Other minds' patterns bleed through the Bridge Unit connection, sharpening pattern-recognition at a real emotional cost |

### Combat-Specialization Traits *(added 2026-07-26, marked for possible future renaming)*

| Trait Name | Bonuses | Penalties | Thematic Fit |
|---|---|---|---|
| **All-In Brawler** | Power Attacks (see `Combat/Power_Attacks.md`) add +10× Might to damage, applying to both normal and critical hits | The Power Attack vulnerability window worsens from the base -20% DT/-20% DR to **-40% DT/-40% DR, lasting two turns instead of one** | The purest possible glass-cannon melee build — enormous burst damage from a single swing, at the cost of a much longer, much deeper vulnerability window afterward |

**Design note:** built directly on top of the newly-confirmed Power Attack mechanic (`Combat/Power_Attacks.md`)
— rather than a generic damage trait, this one specifically doubles down on Power Attack's own existing
risk/reward shape (guaranteed damage now, vulnerability later) by making both sides of that trade more
extreme. Pairs directly with the **Crusher** perk below, which pushes the same trade-off in the opposite
direction — see that perk's own design note for how the two interact when taken together.

### Founding-Lineage Traits *(added 2026-07-25, marked for possible future renaming)*

| Trait Name | Bonuses | Penalties | Thematic Fit |
|---|---|---|---|
| **Reclaimer's Hands** | +15% Precision Maintenance & Repair specifically when working on pre-exile (real Upper-Earth-era) infrastructure — recognizing and restoring centuries-dormant stations, runways, and equipment across the many cities founded this way (see `Founding_Nation_Bug_Investigation_Methodology.md`'s "ex-program exiles among the founding population" mechanic) | -10% effectiveness with purely Tepenian-developed systems the character's founding lineage never touched | Descended from a 2564 founding-era ex-program exile (aviator, researcher, engineer) — a genuinely different lineage than the Upper Earth Defectors (who arrived ~250 years later, during the Long Night War); inherited real expertise without inherited context |

**Design note on this trait's origin:** grew directly out of the 2026-07-25 GPS-purposes-only sweep across
city-history files, which established as binding law that a city's real-world station hands its 2564 exiles
only a physical shell — never personnel or institutional continuity — and that any inherited operational
skill in a founding story has to trace to *ex-program exiles among the founding population itself*. This
trait is the player-facing expression of being descended from exactly one of those figures.

### Information/Cyber Warfare Traits *(added 2026-07-26, tentative — flagged for future review, not locked in)*

| Trait Name | Bonuses | Penalties | Thematic Fit |
|---|---|---|---|
| **Information Warfare** | +20% Hacking *(corrected 2026-07-28 — the original "+15% Electronic Warfare" referenced a skill that never existed in the real 25/26-skill list; Hacking, Calculation-governed, is the real skill closest to this trait's cyber-offense theme)*; unlocks a new offensive action, **Data Leak** — a NODE-adjacent debuff (Calculation + Investigation) that exposes a target's weakness rather than dealing direct damage (proposed: temporary DT/DR reduction, or disabling one of the target's tactical options for a turn) | -1 Humanity; using Data Leak costs standing with whoever gets exposed — a Faction & Reputation Management hit regardless of justification or outcome | Gemini-adjacent cyber-offense specialists — the hacker/information-warrior archetype, distinct from a straight Hacking skill investment |

**Design note:** grew out of the 2026-07-26 Information/Data skill restructure — "Data Leakage" was cut as its
own standalone skill (it read more like a tactic than an investable skill), on the understanding that whatever
trait or perk absorbed "Information Warfare" should be the thing that actually *enables* that tactic in play.
**Explicitly tentative — the developer confirmed the general idea but not this exact shape.** Numbers, the
debuff's precise effect, and even the trait-vs-perk placement itself are all open for revision before this is
considered final.

**Real production dependency, flagged 2026-07-25 — this trait's bonus is currently decorative, not
functional.** The founding-era reclamations that motivated it (Marambio, Abowasa, Casey, etc.) are all
historical backstory, already resolved centuries before the game's present day — there's no *current*
pre-exile derelict infrastructure in the game yet for this trait's Precision Maintenance & Repair bonus to
actually apply to. See the matching flag in `Perks/World_and_Discovery_Perks.md`'s "Derelict's Eye" entry —
both need the same thing: at least one genuinely still-derelict, present-day-discoverable pre-exile site
built into real quest content, on the Byrd model (a site nobody claimed at founding, only found much later).
**Not designed yet — flagged, not solved.**

**Design Note**: Traits are flavorful and double-edged, directly supporting different district playstyles and hidden path accessibility.

**Design note on the remaining gap, resolved 2026-07-24:** Might, Calculation, and Investigation previously didn't appear as any trait's *primary* bonus stat (only as penalties or conditional penalties) — the three Stat-Gap Traits above close this. Might and Nerve are still marked TENTATIVE pending their own MACHINE-stat design pass (see `TODO.md`).

**Current base-game trait count, corrected 2026-07-28:** **37 traits** (10 Base + 7 AP-Economy + 14 Fallout-Adapted + 3 Stat-Gap + 1 Combat-Specialization + 1 Founding-Lineage + 1 Information/Cyber Warfare), well past the original 25 target — the previous "33" figure here was stale, predating the 4 FNV traits added 2026-07-28 (Wild Wasteland, Hot Tempered, Loose Cannon, Small Frame).
