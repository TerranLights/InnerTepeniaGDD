# Skills & Leveling System

**File:** `Skills.md`
**Location:** `Game-Mechanics/Character-Creation/`
**Date:** June 22, 2026

Skills range from **1 to 100** and are improved through use, trainers, skill books, quests, and level-up points.
There are **44 skills** total, encouraging deep specialization.

---

## Skill Point Gain per Level

**Base Formula:**
`floor( (Calculation ÷ 2) + (Nerve ÷ 2) + Investigation Modifier )`

### Investigation Modifier Table
| Investigation (INV) | Modifier |
|---------------------|----------|
| 10                  | +3       |
| 8 – 9               | +2       |
| 6 – 7               | +1       |
| **5**               | **+0**   |
| 4                   | -1       |
| 2 – 3               | -2       |
| 1                   | -3       |

### Examples
- **CAL 6 + NRV 6 + INV 5** → floor(3 + 3 + 0) = **6 points per level**
- **CAL 8 + NRV 4 + INV 9** → floor(4 + 2 + 2) = **8 points per level**
- **CAL 10 + NRV 8 + INV 1** → floor(5 + 4 - 3) = **6 points per level**
- **CAL 4 + NRV 4 + INV 10** → floor(2 + 2 + 3) = **7 points per level**

This keeps point gain intentionally low (typically **4–10 points per level**), forcing meaningful specialization over a long progression (target ~60–64 levels).

---

## Tag Skills (Character Creation)

After allocating your MACHINE stats (which determines your skill points per level), you may **Tag 3 skills**.

- Each Tagged skill immediately receives a one-time bonus of:
  **(Skill points per level) + 5**

**Example**:
If your stats give you **7 skill points per level**, each Tagged skill starts with **+12 points**.

This front-loads your chosen playstyle while still requiring investment to reach mastery.

---

## Full Skill List

### Technical / Engineering (9)
- Thermal Engineering (Engine + Calculation)
- Precision Maintenance & Repair (Agility + Engine)
- Jury-Rigging & Repurposing (Agility + Might + Investigation)
- Siligel Chemistry (Calculation + Engine)
- Decentralized Systems Design (Calculation + Engine + Investigation)
- Undergrid Navigation & Salvaging (Agility + Investigation + Engine)
- Hydroponic Systems (Agility + Engine)
- Highway Maintenance & Transit Systems (Agility + Engine)
- Power Grid Management (Engine + Calculation)

### Information / Data (8)
- Data Archaeology (Calculation + Investigation)
- Arcanet Navigation & Hacking (Calculation + Investigation)
- Information Verification & Analysis (Calculation + Investigation)
- Rumor & Network Intelligence (Investigation + Humanity)
- Cryptography & Decryption (Calculation + Investigation)
- Pre-War Lore & History (Calculation + Investigation)
- Subnet Optimization (Calculation + Investigation)
- Data Leakage & Information Warfare (Calculation + Investigation)

### Social / Diplomatic (7)
- Diplomatic Negotiation (Humanity + Nerve)
- Empathy Protocols (Humanity + Calculation)
- Faction & Reputation Management (Humanity + Nerve)
- Deception & Narrative Crafting (Humanity + Calculation + Investigation)
- Faction Rhetoric (Humanity + Nerve)
- Moral Philosophy & Ethical Reasoning (Humanity + Calculation)
- Companion Command & Loyalty (Nerve + Humanity)

### Survival / Exploration (6)
- Frontier Survival & Cold Adaptation (Engine + Might)
- Environmental Exploitation & Ripple Reading (Investigation + Engine + Agility)
- Stealth & Infiltration (Agility + Investigation)
- Isolation & Psychological Resilience (Nerve + Engine)
- Scavenging & Resource Foraging (Agility + Investigation)
- Hazard Navigation (Ice, Tunnels, Blackouts) (Agility + Investigation + Engine)

### Combat & Security (6)
- Non-Lethal Restraint & Subdual (Agility + Might)
- Improvised Weaponry & Combat Jury-Rig (Might + Agility)
- Defensive Posturing & Endurance Fighting (Engine + Nerve)
- Tactical Grid Combat (Agility + Calculation)
- Electronic Warfare (Calculation + Investigation)
- Threat Assessment (Investigation + Nerve)

### Specialized / Cultural (8)
- Ossuary Resonance (Humanity + Nerve)
- Sonic Attunement (Agility + Humanity)
- Golden Eye Calibration (Agility + Investigation)
- Holographic Projection & AI Interaction (Calculation + Humanity)
- Bridge Protocol Mastery (All stats — unique progression)
- Robot Religion Insight (Humanity + Calculation)
- Cultural Performance & Resonance (Humanity + Agility)
- Memory & Consciousness Manipulation (Calculation + Investigation)

---

**Design Note**:
The large skill pool + limited points per level + strong Tag bonus creates clear build identity and high replayability. Hidden paths rely heavily on specific skill synergies. Investigation now meaningfully influences how many points you receive, rewarding analytical builds while punishing extremely low Investigation.

---

This update is fully consistent with your existing `MACHINE_Stats.md` and the previous skill point design. You can copy-paste this directly over the current `Skills.md` file (or merge as needed).

Would you like me to also create an updated version of the main **Leveling & Progression** document that includes XP formulas, Integrity (HP), and this new skill point system all in one place?
