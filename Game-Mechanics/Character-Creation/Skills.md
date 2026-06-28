# Skills & Leveling System

Skills range from **1 to 100** and are improved through use, trainers, skill books, quests, and level-up points.  
There are **44 skills** total, encouraging deep specialization.

---

## Core Design Law: Flat Thresholds, No Dice Rolls

**There are no dice rolls for skill or stat checks in Inner Tepenia.** Every non-combat gate is a flat threshold: the player either meets the requirement or they don't. This applies to the Outer Tepenia series as well — it is a series-wide design commitment.

The only context where random number generation applies is ranged combat hit chance (whether a bullet lands) and aimed-shot probability (VATS-equivalent hit chance per body part). Everything else is binary.

**What this means in practice:**
- A locked door requiring Lockpick 50 opens if you have 50. It does not open if you have 49, regardless of any roll.
- A trap requiring Investigation 7 to detect is automatically detected if you have 7. There is no "roll to notice."
- A repair check requiring Repair 45 succeeds or fails based solely on whether your skill meets 45.
- Dialogue options gated behind MACHINE stats or skills appear or do not appear. There is no chance of failure on a check you qualify for.

*Fallout: New Vegas precedent: Perception 7 automatically reveals hollow walls in RepCONN HQ; Repair 22 automatically disarms tripwires; Repair 45 automatically disarms rigged shotguns. No dice involved — the threshold is met or it isn't.*

**Companion effects follow the same logic.** A companion with Investigation 10 does not give the player a "+X bonus to Investigation rolls." They extend the player's effective detection floor — certain things are automatically noticed when that companion is present that would otherwise require an Investigation threshold the player hasn't met.

---

## Core Design Law: Minimum Five Solutions

**Every quest in Inner Tepenia must have at least five ways to complete it. Every non-story-gated skill check must have at least five ways to pass it.** This is a series-wide binding commitment applying to Inner Tepenia and all three future Outer Tepenia games.

*Fallout: New Vegas precedent (Chris Avellone's stated design goal):* The FNV team aimed for at least three solutions to every quest. They achieved this to a remarkable degree. Inner Tepenia commits to a higher floor: five.

**What counts as a separate solution:**
- A distinct skill at a specific threshold (e.g., Survival 50)
- A specific perk (e.g., Strong Back, Pack Rat)
- A stat threshold on a MACHINE stat
- A companion being present and providing an alternate path
- A prior quest decision or faction reputation that changes available options
- An item or resource that substitutes for a skill requirement

**The Honest Hearts weight limit example (six solutions):** Talking to Jed Masterson, the base weight limit is 75 lbs. Six separate ways exist to raise it to 100: Survival 50 ("I've humped this way before"); Strong Back perk; Pack Rat perk; Science 50 (spot Ricky's broken PipBoy); Medicine 50 (identify his Psycho addiction); Speech 50 (call his bluff). This is the target density for Inner Tepenia — at minimum, across the entire game.

**Story-gated access is exempt.** Some spaces, conversations, and options are intentionally locked behind specific companion standing or questline progress (e.g., Seica's Scorpio spiritual access, secret halls only she can open). These are design choices, not failed solutions — the gate is the point. The five-solution rule applies to situations where the player is trying to accomplish something and the question is *how*, not *whether they're allowed to*.

**Implementation note:** When writing any quest or skill-gated encounter, before finalizing it, explicitly list all five (or more) solution paths. If fewer than five exist, add more before the design is considered complete.

---

---

## Skill Point Gain per Level

**Final Formula:**  
`max(3, 2 + floor(Calculation ÷ 2) + floor(Nerve ÷ 2) + Investigation Modifier)`

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

| Build Description              | CAL | NRV | INV | Points per Level |
|--------------------------------|-----|-----|-----|------------------|
| Extreme Tank / Brute           | 1   | 1   | 1   | **3**            |
| Low Intelligence Build         | 3   | 4   | 4   | **4**            |
| Balanced Generalist            | 6   | 6   | 5   | **8**            |
| High Analyzer / Thinker        | 8   | 5   | 9   | **10**           |
| Ultra Focused Build            | 10  | 8   | 10  | **14**           |
| Optimized Genius Build         | 10  | 10  | 10  | **15**           |
| Social Tank                    | 1   | 1   | 1   | **3**            |

This ensures:
- No build is completely starved of progression (minimum 3 points per level).
- High **Calculation** remains the strongest contributor.
- **Nerve** and **Investigation** still provide meaningful bonuses/penalties.
- Extremely specialized characters (e.g. pure physical or pure social tanks) progress slowly and must rely heavily on Tag Skills, companions, items, and quest rewards.

Point gain ranges from **3–15 per level**, with most builds landing between **5–10**, forcing meaningful specialization across the **64-level base game progression**. DLCs may raise the level cap beyond 64.

---

## Tag Skills (Character Creation)

After allocating your MACHINE stats, you may **Tag 3 skills**.

Each Tagged skill immediately receives a one-time flat bonus of **+15 points**.

This front-loads your chosen playstyle while still requiring sustained investment to reach mastery.

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
- Empathy Protocols (Humanity + Investigation)
- Faction & Reputation Management (Humanity + Nerve)
- Deception & Narrative Crafting (Humanity + Investigation + Nerve)
- Faction Rhetoric (Humanity + Nerve)
- Moral Philosophy & Ethical Reasoning (Humanity + Nerve)
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
- Defensive Posturing & Endurance Fighting (Might + Nerve)
- Tactical Grid Combat (Agility + Calculation)
- Electronic Warfare (Calculation + Investigation)
- Threat Assessment (Investigation + Nerve)

### Specialized / Cultural (8)
- Ossuary Resonance (Humanity + Nerve)
- Sonic Attunement (Agility + Humanity)
- Golden Eye Calibration (Agility + Investigation)
- Holographic Projection & AI Interaction (Calculation + Humanity)
- [NAME TBD] (All stats — unique progression)
- Robot Religion Insight (Humanity + Investigation)
- Cultural Performance & Resonance (Humanity + Agility)
- Memory & Consciousness Manipulation (Calculation + Investigation)

---

**Design Note**:
The large skill pool + limited points per level + strong Tag bonus creates clear build identity and high replayability. Hidden paths rely heavily on specific skill synergies. Investigation meaningfully influences how many points you receive, rewarding analytical builds while punishing extremely low Investigation.
