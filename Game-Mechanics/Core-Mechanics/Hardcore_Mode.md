# Hardcore Mode — Inner Tepenia

*This document is partially complete. Core mechanic structure and South Pole DLC interactions are confirmed. Full Hardcore mode design requires further development — flagged for a dedicated design session.*

---

## Design Philosophy

**Standard mode makes Inner Tepenia dangerous. Hardcore mode makes it consuming.**

In standard mode, consequences are immediate and direct: damage, resource cost, death. The world fights the player.

In Hardcore mode, consequences compound over time through degradation systems. The world doesn't just fight the player — it wears them down. Systems that are fine in isolation become lethal in combination. The South Pole is where this distinction is sharpest: what Kendra could not survive alone is survivable with preparation and support — but Hardcore mode narrows that margin significantly.

---

## Standard vs. Hardcore — The Core Distinction

| System | Standard Mode | Hardcore Mode |
|---|---|---|
| Thermal exposure | Direct HP damage in cold areas | HP damage + component degradation over time |
| Coldshock | Reduces Siligel efficiency; reversed by shelter | Same, plus additional system failures at stages 3–5 |
| Structural collapse | Damage on direct hit | Near-misses also risk component damage |
| Magnetic anomalies | Navigation/targeting/HUD disruption | + Prolonged exposure corrupts memory integrity |
| Blizzard events | Visibility reduction | + Environmental seal stress; extended exposure causes system errors without shelter |
| Ammo | Weightless | Has weight (affects carry capacity decisions) |
| Companions | Can be downed and revived | Can permanently die |
| Siligel | Instant benefit | Gradual processing (benefit delivered over time, not instantly) |

---

## Robot-Specific Survival Mechanics (Hardcore)

Standard Fallout Hardcore mechanics (hunger, thirst, sleep) apply to biological characters. The protagonist of Inner Tepenia is a robot. The equivalents are:

### Siligel — Robot Food
**Siligel is robot food.** Not lubricant, not blood, not a structural fluid — nutritional input. In standard mode it restores HP and energy immediately. In Hardcore mode, Siligel processes gradually — the benefit is delivered over time rather than instantly, making combat healing less reliable.

### Coldshock and Siligel Efficiency
The Coldshock condition (see `DLC_01_Echoes_of_Amundsen.md` for full stage table) reduces how much benefit the player gets from consuming Siligel. The cold impairs the protagonist's ability to process nutrition efficiently.

This creates a compounding spiral specific to the South Pole DLC:
1. Cold exposure → Coldshock accumulates
2. Coldshock → Siligel provides diminishing returns
3. Diminishing Siligel returns → need more food to maintain function
4. Resources are scarce → getting more food is difficult
5. Difficulty → more combat and exposure → more cold

In Hardcore mode, this spiral is tighter and faster than in standard mode. Getting out of cold and into shelter is not just good practice — it is mandatory resource management.

### Power Consumption
- Equivalent to hunger/thirst
- High-intensity operation (sustained combat, running, heavy system use) depletes energy reserves faster than low-intensity movement
- Running dry does not kill instantly — it degrades performance in escalating steps before shutdown: Might penalties → Agility penalties → system failures → shutdown
- Energy restores through Siligel consumption, rest in safe areas, or power source items
- *Full design for power consumption tiers: TBD*

### Thermal Regulation
- The protagonist's thermal management systems are stressed by extreme cold
- In standard mode: thermal exposure causes HP damage
- In Hardcore mode: sustained cold also degrades the thermal regulation component itself — meaning the protagonist becomes *less able to handle cold* the longer they're exposed without recovery time
- Recovery requires not just reaching shelter but spending time there

### Memory Integrity
- Extended high-stress operation without a consolidation cycle (rest) degrades processing
- Low integrity effects: slower Calculation-dependent checks, Investigation thresholds harder to meet, occasional dialogue option mis-fires
- Not catastrophic immediately, but accumulating — and in the South Pole, rest opportunities are scarce
- Recovery: consolidation cycle in a safe location (the South Pole has very few of these)
- Magnetic anomaly zones (see DLC_01) accelerate memory integrity loss during prolonged exposure

### Component Wear
- In standard mode, equipment degrades but the protagonist's body systems are stable
- In Hardcore mode, specific body systems wear with use:
  - Agility-related components from sustained combat
  - Engine-related from extended exertion without rest
  - Thermal regulation from cold exposure
- Component wear creates maintenance requirements that don't exist in standard mode
- Unaddressed component wear eventually causes the associated stat to drop until repaired

---

## Companion Permanent Death (Hardcore)

Same as Fallout: New Vegas Hardcore mode. Companions who are downed and not revived in time are permanently dead.

**South Pole DLC implication:** Kendra Heinrich can be killed during the DLC before she joins the player as a companion. This is a permanent loss — she does not become available after the DLC if she died during it. This represents one of the highest stakes in any Hardcore playthrough.

---

## Further Development Required

The following aspects of Hardcore mode are undesigned and require a dedicated session:

- [ ] Full power consumption tier system (depletion rates, penalty thresholds, recovery rates)
- [ ] Component wear repair mechanics (where, how, cost)
- [ ] Memory integrity consolidation mechanics (time required, location requirements)
- [ ] Interaction between all Hardcore systems simultaneously (compound failure states)
- [ ] Hardcore-specific items, perks, and traits
- [ ] Whether Hardcore mode is toggled at game start or can be changed mid-game
- [ ] Hardcore mode achievements / recognition
- [ ] Difficulty scaling adjustments specific to Hardcore (if any)
- [ ] How Hardcore interacts with the re-spec system (Identity Fragmentation under compound stress)
