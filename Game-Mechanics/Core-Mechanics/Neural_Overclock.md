# Neural Overclock System

A top-down, turn-based adaptation of Cyberpunk 2077's Berserk / Sandevistan / Overclock ability framework. Three distinct modes, one unified cyberware system. Designed to enhance — not conflict with — the Minmax build questlines and unique interactions.

The system is stat-dependent and drawback-required by design. Base version is accessible to any build; true power comes from minmax investment while the built-in costs and narrative consequences keep high-power use balanced and meaningful.

---

## Acquisition and Core Rules

**Acquisition:** Cyberware implant. Obtainable via crafting, quest reward, or early-game choice. Upgradable through perks, district vendors, or specific Minmax build paths.

**Activation:** Costs AP (or a dedicated "Overclock Action"). Enters the chosen Mode for 1–3 turns. Duration scales with upgrades and Engine stat.

**Cooldown:** 3–5 turns after deactivation. Prevents spam; creates vulnerability windows that enemy AI exploits.

**Resource — Neural Strain:** A meter that builds with use. High Strain causes escalating drawbacks or forced shutdown. Strain does not reset between encounters automatically — resource management extends beyond individual fights.

**Exploration use:** Bonus movement tiles or reduced exploration AP costs while in an active mode. Not purely a combat tool.

**Mutual exclusivity at high tiers:** The three modes become mutually exclusive at advanced tiers (very expensive to switch). Lower tiers allow limited mixing. This encourages build commitment and rewards Minmax specialization.

---

## MACHINE Stat Scaling

| Stat | Overclock Effect |
|------|-----------------|
| Engine | Efficiency — lower activation cost, longer duration, less Strain buildup |
| Agility | Framejack potency — speed and action efficiency |
| Might | Berserk damage output and damage resistance |
| Calculation | Overclock optimization — bonus actions, reduced ability costs |
| Nerve | Resilience — less health/Strain drain, better control during mode |
| Humanity | Narrative effects — low Humanity triggers "cyberpsychosis" events or unique quest hooks on heavy use |
| Investigation | Secondary effects — synergizes with hacking-style builds in Overclock mode |

---

## The Three Modes

### Mode 1 — Framejack (Sandevistan Equivalent)

**Stat focus:** Agility / Engine

**Effects:**
- Bonus AP or heavily reduced action costs for movement and attacks
- One "free" basic action or extra movement phase per turn
- Feels like getting more turns within the same time window

**Flavor:** Neural acceleration — you move and react at framejacked speed while the world feels slowed around you.

**Drawbacks:**
- High Strain buildup per turn
- Post-mode "lag": reduced AP or slowed reactions on the following turn

**Best for:** High Agility + Engine Minmax builds. Speedrun-friendly burst movement and combat.

**Minmax hook:** High Agility builds unlock unique Framejack quest interactions or secret ending paths.

---

### Mode 2 — Berserk (Rage/Tank)

**Stat focus:** Might

**Effects:**
- Bonus damage (especially melee and signature abilities)
- Bonus damage resistance/armor rating
- Possible cleave or multi-hit effects
- "Can't die below X% HP" during active mode — health drain instead of death

**Flavor:** Adrenaline plus neural override — you become an unstoppable close-quarters force.

**Drawbacks:**
- Heavy health drain per turn
- Restricted precision options during mode (fine hacking, certain perks unavailable)
- Overuse triggers narrative consequences — companion reactions, ending flags

**Best for:** High Might + Nerve Minmax builds. Melee or aggressive combat styles.

**Minmax hook:** Strong synergy with existing combat perks; unique "Berserk" endings or companion reactions if used excessively.

---

### Mode 3 — Overclock (Ability/Hack Spam)

**Stat focus:** Calculation

**Effects:**
- Reduced AP costs for complex abilities, hacking, item use, and signature abilities
- Extra uses or chaining of abilities that normally have cooldowns
- Bonus to targeting or system optimization

**Flavor:** Pushing your OS and cyberdeck beyond design limits for raw computational throughput.

**Drawbacks:**
- Rapid Strain buildup
- Risk of random debuffs, misfires, or forced cooldown at high Strain
- Health cost on overuse

**Best for:** High Calculation + Investigation Minmax builds. Ability/tech-focused play styles.

**Minmax hook:** Ties directly into existing hacking/complex action cost systems; Calethina may comment on or react to heavy Overclock use.

---

## Drawbacks — Non-Negotiable Design Constraint

Drawbacks are required on all three modes. The system's power level is only acceptable because the costs are real. No version of Neural Overclock should exist without escalating consequences for sustained use.

The drawback structure creates vulnerability windows that smart enemy AI can exploit (focus fire during cooldown, cyberware-disrupting attacks, area control). This means the system adds challenge alongside power, not just raw advantage.

Narrative consequences of heavy use are tracked and feed into:
- Existing Minmax questline folders (unique interactions for overclock-heavy builds)
- Companion reactions (especially Calethina)
- Endings (overclock addiction / cyberpsychosis pathways)
- Post-idolization perks and secret ending triggers

---

## Balance Principles

**Enemy counterplay:** AI prioritizes punishing the cooldown/vulnerability window. Enemy units with cyberware-disrupting attacks specifically target Overclock users.

**Tuning levers:** All scaling formulas connect to the existing AP base system and MACHINE stat modifiers. Minmax master charts provide a testing baseline.

**No flat power for everyone:** The system is stat-dependent, not a flat upgrade available to all builds equally. A mid-stat generalist gets limited value. A committed Minmax build gets the full power — with the full consequences.

**Accessibility vs. depth:** The base implant is usable by any build without specialization. The true ceiling of each mode requires heavy investment and forces accepting the associated risks.

---

## Integration Notes

- Cross-reference: `Game-Mechanics/Character-Creation/Perks.md` (perk unlocks per mode)
- Cross-reference: `Game-Mechanics/Core-Mechanics/Action_Points_Base-Level_System.md` (AP integration)
- Cross-reference: `Game-Mechanics/Character-Creation/Minmax_Build_Master_Chart_-_All_35_Combinations.md` (which builds synergize with which modes)
- New perks for each mode belong in the existing Perks folder structure
- District-specific cyberware upgrades: Aquarius (experimental tiers), Capricorn (industrial-grade), Pisces (black market variants)
