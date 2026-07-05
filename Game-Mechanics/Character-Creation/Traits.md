# Traits

**Marked for future review (2026-07-04):** every trait in this file — old and newly added alike — is provisional. Reaching the 25-trait target doesn't mean any individual trait is locked in; names, bonuses, penalties, and stat/skill gates are all subject to adjustment once actual design & development work reaches character creation, and adding more traits later may prompt revisiting ones already here (for balance, overlap, or thematic fit). Treat this whole file as a working draft, not final content.

Traits are major, permanent choices made during **Character Creation**. You may select **up to 4** traits. Taking more traits progressively increases overall difficulty.

**Target trait count, established 2026-07-04 (modeled on Fallout: New Vegas's 10 base + 6 Old World Blues, max 2 selectable — scaled up considerably):**
- **Base game: 25 traits** (target; **27 currently designed** as of 2026-07-04 — see consolidation note below and the Fallout-Adapted Traits section — target already cleared, with room for a few more if good ideas come up).
- **Each of the 7 DLCs adds +5 traits** to the pool (6 subnet DLCs + the South Pole DLC, Kendra Heinrich's "Echoes of Amundsen").
- **Grand total with base game + all 7 DLCs: 60 traits** (25 + 7×5).
- **Max selectable at character creation: 4** (up from FNV's 2) — a player who owns every DLC chooses from the full 60-trait pool but still only picks up to 4, same as a base-game-only player choosing from 25.

**Consolidation note (2026-07-04):** this file previously listed only 10 traits; 7 more (the "AP-Economy" group below) existed separately in `Core-Mechanics/Action_Points_Perks_and_Traits.md` and weren't being counted toward the trait total anywhere. Merged here so this file is the single authoritative trait list — 17 total, not 10.

| Trait Name                    | Bonuses                                              | Penalties                                              | Thematic Fit |
|-------------------------------|------------------------------------------------------|--------------------------------------------------------|--------------|
| **Lattice Mind**             | +15% Decentralized Systems Design<br>+15% Jury-Rigging & Repurposing | -1 Humanity                                           | Hidden paths, tech innovators |
| **Cold-Blooded Optimizer**   | +15% Thermal Engineering<br>+15% Siligel Chemistry  | -1 Humanity                                           | Industrial efficiency |
| **Empathic Bridge**          | +15% Empathy Protocols<br>+15% Diplomatic Negotiation | -1 Might                                              | Social, non-lethal diplomats |
| **Ripple Intuitive**         | +15% Environmental Exploitation & Ripple Reading<br>+10% Data Archaeology | -1 Calculation (under high stress)                   | Crisis exploitation |
| **Frontier Hardened**        | +15% Frontier Survival & Cold Adaptation<br>+10% Precision Maintenance | -1 Humanity (in civilized districts)                 | Sagittarius explorers |
| **Narrative Ghost**          | +15% Deception & Narrative Crafting<br>+10% Rumor & Network Intelligence | -1 Humanity (harder to build genuine trust)          | Narrative Lattice |
| **Engine Overclocker**       | +1 Engine<br>+20% performance when pushing during crises | Risk of temporary burnout (Engine drain)             | High-risk players |
| **Humanity Anchor**          | +1 Humanity<br>+15% Empathy Protocols<br>+15% Companion Command | -10% skill gain in pure technical skills             | Roleplay / companion builds |
| **Undergrid Phantom**        | +15% Precision Maintenance & Repair<br>+15% Stealth & Infiltration | -1 Might                                              | Virgo infiltrators |
| **Sonic Resonance**          | +15% cultural/performative skills (Leo district)   | -1 Structural stability in high-vibration areas      | Leo artistic builds |

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

**Design Note**: Traits are flavorful and double-edged, directly supporting different district playstyles and hidden path accessibility.

**Design note on the remaining gap:** with the Fallout-Adapted Traits above, the base-game trait count is now **27 of the 25 target** (2 over target — not a problem, just noting the goalpost is already cleared). Might, Calculation, and Investigation still don't appear as any trait's *primary* bonus stat (only as penalties or conditional penalties) — worth keeping in mind for any further traits designed later, especially since Might and Nerve are also the two MACHINE stats still marked TENTATIVE pending their own design pass (see `TODO.md`).
