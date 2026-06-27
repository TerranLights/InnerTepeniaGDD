### Action Points (AP) System – Inner Tepenia

**Inner Tepenia** is a top-down isometric turn-based game. Therefore, Action Points work as a **fresh pool every turn**, similar to classic Fallout 1 & 2, while staying consistent with the real-time AP system planned for the future *Outer Tepenia* games.

#### Core Design Goal
Make **Agility**, **Nerve**, and **Engine** all feel meaningful and synergistic in combat and exploration, while keeping the system tactical, readable, and satisfying for both casual players and speedrunners.

---

#### Base Action Points per Turn

Every character receives a new pool of Action Points at the start of their turn.

**Formula:**
> **Base AP = 6 + floor(Agility / 2)**

**Examples:**
- Agility 4 → 8 AP
- Agility 6 → 9 AP
- Agility 8 → 10 AP
- Agility 10 → 11 AP

---

#### Nerve Modifier (Reliability & Bonus AP)

**Nerve** modifies your total AP pool each turn.

**Formula:**
> **Nerve Modifier = floor((Nerve - 5) / 2)**

**Examples:**
- Nerve 3 → -1 AP
- Nerve 5 → 0 (neutral)
- Nerve 7 → +1 AP
- Nerve 9 → +2 AP
- Nerve 10 → +2 or +3 AP

**Final AP at start of turn = Base AP + Nerve Modifier**

---

#### Engine – Efficiency & Cost Reduction

Since there is no regeneration during a turn, **Engine** governs how *efficiently* you spend your AP.

**Primary Role:**
- Reduces the cost of **movement** and certain repeated actions.

**Recommended Mechanics:**
- Base movement cost = **1 AP per tile**
- Every 2 points of Engine above 5 grants **1 free movement point** per turn (or reduces movement cost).
- High Engine also slightly reduces the AP cost of reloading, using items, and some abilities.

**Example:**
- Engine 8 → You may get 2–3 “free” movement tiles per turn, or movement costs 1 AP for every 1.5 tiles (rounded appropriately).

---

#### Standard AP Costs

| Action                        | Typical Cost       | Notes |
|-------------------------------|--------------------|-------|
| Move 1 tile                   | 1 AP               | Can be reduced by high Engine |
| Basic Attack                  | 4–6 AP             | Depends on weapon type |
| Aimed / Special Attack        | 6–8 AP             | Higher damage or effects |
| Reload Weapon                 | 2–4 AP             | Can be reduced by Engine/perks |
| Use Item from Inventory       | 2–4 AP             | Varies by item |
| Hacking / Complex Interaction | 6–10 AP            | High-investment actions |
| Powerful Ability / Overclock  | 8–15 AP            | Big payoff, expensive |
| Stand Up / Minor Action       | 2–3 AP             | Recovery actions |

Unused AP at the end of your turn are **discarded**. Use them or lose them.

---

#### Design Benefits

- **Agility** = Raw quantity of actions (more AP)
- **Nerve** = Consistency and slight bonus AP (feels reliable)
- **Engine** = Efficiency and fluidity (cheaper actions, better movement)
- Creates strong, distinct builds (high Agility glass cannon vs high Engine efficient survivor vs high Nerve well-rounded character)
- Supports speedrunning and optimization (different stat distributions create very different playstyles)
- Maintains strong continuity with the future *Outer Tepenia* real-time games

---

#### Future-Proofing for Outer Tepenia

This system is intentionally designed so that:
- **Agility** will determine base AP pool in real-time games.
- **Nerve** will affect AP bonuses/penalties.
- **Engine** will control regeneration speed.

Players who understand the system in *Inner Tepenia* will already intuitively understand how their stats affect action economy in the 3D open-world games.

---

**Implementation Notes**
- Clearly display current AP and costs in the UI during combat/exploration.
- Perks can further modify the system (e.g. +1 permanent AP, reduced movement cost, bonus actions, etc.).
- Some powerful perks or items may grant temporary extra AP or free actions.
