### Signature Abilities – Inner Tepenia Implementation

These are the turn-based isometric equivalents of Cyberpunk 2077’s Berserk, Sandevistan, and Overclock. They are designed to feel powerful, thematic, and consistent with the real-time versions planned for the *Outer Tepenia* series.

#### Tepenian Names

| Cyberpunk 2077 | Tepenian Name          | Relevant MACHINE Stat | Core Theme                  |
|----------------|------------------------|-----------------------|-----------------------------|
| **Berserk**    | **Rage**      | Might                 | Aggressive combat surge     |
| **Sandevistan**| **Framejacking**       | Agility               | Hacking your own movement systems |
| **Overclock**  | **Overclock**   | Calculation           | Computational / efficiency surge |

---

#### Implementation in Inner Tepenia (Turn-Based Isometric)

These abilities function as **temporary multi-turn power states** rather than real-time bursts. They last a number of turns and come with clear costs and after-effects.

##### 1. Framejacking (Agility-based)

**Concept**: You temporarily hack your own movement and action systems for extreme speed.

**Effect** (lasts 3–5 turns, duration and strength scale with Agility):
* Significantly increased movement range per turn (typically double or more); Massive increase to movement range per turn (e.g., double or triple normal movement)
* Reduced AP cost for attacks and movement (-1 or -2 AP per action)
* Gain 1–3 free movement tiles per turn (0 AP cost)

**After-Effect**:
* Movement speed penalty for 1–2 turns after the effect ends (systems cooling down)

**Flavor**: Your Bridge Unit runs its locomotion systems at unsafe speeds by temporarily overriding safety protocols. "Framejacking" its own locomotion systems.

**Cost / Risk**:
* After it ends, you suffer a movement penalty for 1–2 turns (systems need to cool down)
* Higher Agility = longer duration and stronger effect
* Can be combined with movement-focused perks for insane kiting potential

##### 2. Rage (Might-based)

**Concept**: You enter a temporary aggressive combat state (similar to BG3 Berserk or classic rage).

###### Possible Effects:

**Option A**: Action Economy Focus
* For 3–4 turns: All non-attack actions cost significantly fewer AP (especially hacking, item use, complex abilities)
* Gain 1–2 "free" complex actions per turn
* Attacks are slightly more expensive (you're prioritizing precision over raw output)

**Option B**: Precision & Damage Focus
* +40–60% damage on aimed/special attacks
* Greatly increased critical hit chance
* Reduced AP cost specifically for aimed attacks

**Option C**: Hybrid
* Temporary boost to one MACHINE stat (Calculation or another)
* Reduced AP costs across the board
* Small chance of "system strain" (random minor debuff)

**Effect** (lasts 3–4 turns):
* +30–50% damage on all attacks (scales with Might)
* Reduced AP cost for attacks
* Minor damage resistance or ability to ignore certain debuffs
* May limit access to non-aggressive/support abilities

**After-Effect**:
* Increased damage taken for 1–2 turns after the effect ends, or a temporary stat penalty

**Flavor**: You force your combat systems into an over-aggressive mode, trading control for raw power.

**Cost / Risk**:
* After it ends, you take increased damage for 1–2 turns or suffer a temporary stat penalty
* In Hardcore Mode: Low Humanity versions could add "loss of control" mechanics (random targeting or forced aggressive actions)


##### 3. Overclock (Calculation-based)

**Concept**: You push your computational systems far beyond normal limits for massive efficiency and precision.

**Recommended Primary Effect** (lasts 3–4 turns):
* All non-attack actions (hacking, item use, complex abilities) cost significantly fewer AP
* Gain 1–2 “free” complex actions per turn
* Attacks may cost slightly more AP (you’re prioritizing precision and efficiency over volume of fire)

**Alternative / Hybrid Effects** (can be mixed):
* Greatly increased critical hit chance on aimed attacks
* Temporary boost to one MACHINE stat
* Reduced AP costs across most actions

**After-Effect**:
* Temporary increase in AP costs or reduced maximum AP for 1–2 turns (system strain)

**Flavor**: You are running your Bridge Unit’s processors at dangerous speeds to achieve near-perfect tactical efficiency.

**Cost / Risk**:
* After it ends: Temporary penalty to AP or increased costs for 1–2 turns
* In Hardcore Mode: Low Humanity versions could add "glitch" effects (random AP loss, misfires, or temporary loss of control)


---

#### Quick Summary of Recommendations

| Ability            | Stat          | Duration     | Main Benefits                              | After-Effect                     | Best Playstyle                  |
|--------------------|---------------|--------------|--------------------------------------------|----------------------------------|---------------------------------|
| **Framejacking**   | Agility       | 3–5 turns    | Massive movement + cheaper/faster actions | Movement penalty                 | Mobile, kiting, hit-and-run     |
| **Rage**  | Might         | 3–4 turns    | High damage + cheaper attacks              | Increased damage taken           | Aggressive melee / burst damage |
| **Overclock** | Calculation | 3–4 turns    | Much cheaper complex actions + precision   | Increased AP costs / strain      | Tactical, support, ability spam |

---

#### Hardcore Mode – Humanity Scaling

In Hardcore Mode, the player’s **Humanity** stat acts as a sliding scale that modifies these abilities:

* **Higher Humanity**:
  * Slightly lower damage / power bonus
  * Reduced or eliminated negative after-effects
  * More stable and controlled version of the ability

* **Lower Humanity**:
  * Higher damage / power bonus
  * Stronger negative after-effects
  * Risk of additional negative effects (temporary loss of control, random glitches, hallucinations, or forced aggressive actions)

This creates meaningful roleplaying and build choices. A high-Humanity character can use these abilities more safely and frequently, while a low-Humanity character treats them as high-risk, high-reward trump cards that can backfire.

---

#### Perks & Traits That Interact with These Abilities

**Perks**
* **Enhanced Protocols** (3 ranks)  
  Increases duration of all signature abilities by 1 turn per rank.  
  *Prerequisite*: Relevant stat 7+

* **Stable Systems**  
  Reduces the severity of after-effects from signature abilities.  
  *Prerequisite*: Engine 7+ or Nerve 7+

* **Unstable Overdrive**  
  Increases the power of signature abilities but also increases after-effect duration.  
  *Prerequisite*: Low Humanity builds encouraged

* **Precision Overclock**  
  When using **Overclock**, gain additional bonuses to critical hits and complex actions.  
  *Prerequisite*: Calculation 8+

* **Fury Amplifier**  
  When using **Rage**, gain bonus damage and lifesteal on attacks.  
  *Prerequisite*: Might 8+

* **Framejacking Mastery**  
  When using **Framejacking**, gain even greater movement bonuses and the ability to ignore some terrain penalties.  
  *Prerequisite*: Agility 8+

**Traits (Character Creation)**
* **Prototype Overclocker**  
  **+** Signature abilities are significantly more powerful.  
  **–** After-effects are more severe and last longer.

* **Stable Frame**  
  **+** After-effects of signature abilities are reduced or removed.  
  **–** Base power of the abilities is slightly lower.

* **Unstable Mind**  
  **+** Signature abilities gain extra effects when Humanity is low.  
  **–** Risk of random negative effects even outside of Hardcore Mode.

* **Combat Savant**  
  **+** Bonus to one signature ability of your choice (chosen at creation).  
  **–** -1 to the other two relevant MACHINE stats.

---

**Design Notes**
* These abilities are intended to be rare, high-impact moments rather than spammable tools.
* They pair extremely well with the existing AP system and the fast Minmax secret endings.
* In *Outer Tepenia*, these will transition into real-time burst abilities with the same stat requirements and scaling logic.
