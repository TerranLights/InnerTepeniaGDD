### Action Points – Perks, Traits & Advanced Rules

This section expands on the core AP system with character customization options and optional depth.

#### Perks That Interact with Action Points

**Status (2026-10-18):** the authoritative perk list is `Perks/Regular_Perks_-_Level-Up.md`. This file's earlier perk list had drifted from it, so the four perks that exist in both now point there, and the rest are marked as proposals. Several perks, traits and skills (including the skill named "Tactical Grid Combat") are expected to be renamed or replaced later.

**In the authoritative perk list (see there for requirements and effects)**
- **Grim Reaper Protocols**: Might 6 and Agility 6; killing an enemy in combat refunds 3 AP, once per turn. *(The earlier "Machine 7+" here was not a valid stat, and the earlier 3–5 AP was superseded.)*
- **Rapid Fire Protocols**: reduces the AP cost of basic attacks (minimum 3 AP).
- **Precision Strike**: reduces the AP cost of aimed and special attacks.
- **Undergrid Runner**: faster movement and reduced hazard effects in the Undergrid.

**Proposed, not yet in the perk list.** Each needs proper requirements (stat plus skill) in the perk list's format before it can be added. Requirements below are the original drafts.

**Movement perk (new, Nerve-based)** *(decided 2026-10-18; name to be set, and this replaces the old "Efficient Exosuit")*
- Several ranks inside one perk, as in Fallout: one minimum requirement, no higher stat needed for later ranks, and the player may take multiple ranks.
- Each rank adds **movement-only** tiles per turn: **+1 tile, or +10% of the character's total movement tiles, whichever is higher.** For typical pools of 8 to 13 tiles this is +1 per rank; the percentage matters for larger pools, such as during Framejacking. These tiles cannot be spent on attacks or other actions.
- Based on **Nerve**, so movement builds are not tied entirely to Agility and Engine. *Suggested:* 3 ranks, Nerve 6+ (to be set when the perk is written).

**Direct AP Increases**
- **Action Protocols** (3 ranks)  
  +1 AP per turn.  
  *Prerequisite*: Agility 6+

- **High-Output Protocols** (2 ranks)  
  +2 AP per turn.  
  *Prerequisite*: Agility 8+ and Nerve 7+

**Resource & Ability Efficiency**
- **Siligel Optimization**  
  Reloading and using energy/siligel-based items costs 1 fewer AP.  
  *Prerequisite*: Engine 6+

- **Overclock Surge** (Combat Perk)  
  Once per combat, gain +4 temporary AP for one turn at the cost of reduced max AP next turn (or minor system strain).  
  *Prerequisite*: to be set (the original draft read "Machine 8+", which is not a stat).  
  *Note: unrelated to the Neural Overclock cyberware system; the name is expected to change.*

- **Field Expedient Reload**  
  Reloading no longer ends your turn’s momentum — you can still move after reloading.  
  *Prerequisite*: Engine 5+

**Utility / Quality of Life**
- **Quick Pockets**  
  Using items from inventory costs 1 fewer AP.  
  *Prerequisite*: Agility 6+

- **Emergency Systems**  
  When below 25% health, gain +3 temporary AP for one turn.  
  *Prerequisite*: Nerve 7+

---

#### Traits (Character Creation Only)

*(Moved 2026-07-04 to `Character-Creation/Traits.md`'s "AP-Economy Traits" section, so all traits live in one authoritative file — see there for High-Output Frame, Efficient Design, Overclocked Prototype, Fragile but Fast, Steady Nerves, Minimalist Frame, and Echo Chamber. These 7 have clear pros and cons and directly affect your action economy.)*

---

#### Optional Advanced Rules

These can be added for more depth (recommended for higher difficulty or veteran players).

**Base Rule**: Unused AP are **discarded** at the end of every turn. This is the canonical default.

**Future Perk / Trait Options (math TBD — design pass pending):**

**1. AP-to-Movement Conversion (Perk or Trait)**
- Unused AP at end of turn convert into bonus movement tiles for a last-chance repositioning burst.
- Could be a perk reward for completing relevant questlines (e.g., Agility- or Engine-focused district capstones).
- Exact conversion ratio and tile cap to be determined during perk design pass.

**2. Carry-Over AP (Banking) — Perk Option**
- A perk or trait could allow banking a small number of unused AP into the next turn.
- Would require careful tuning to avoid snowball effects.
- Exact cap and Engine interaction to be determined during perk design pass.

**3. Fatigue / Overheat**
- If you spend 80%+ of your AP on attacks/abilities in one turn, you suffer a small debuff next turn (-1 AP or reduced accuracy).
- High Engine reduces or removes this penalty.

**4. Free Actions**
- Certain low-impact actions cost **0 AP**:
  - Switching weapons
  - Minor environmental interaction (opening doors, flipping switches)
  - Dropping an item
- Can be expanded with perks.

**5. Overclock / Emergency Mode** *(unrelated to the Neural Overclock cyberware)*
- Once per combat, you can spend **Health or Energy** to gain temporary AP (e.g., 1 AP per 10% health lost).
- High-risk, high-reward option for desperate situations. Ties beautifully into the “Overclock Surge” perk.

**6. Movement as a Separate Resource (Advanced Variant)** *(open: conflicts with the single Agility-based AP pool; to be decided later, per the developer, 2026-10-18)*
- Give every character a small pool of **Movement Points** (separate from main AP).
- Base Movement Points = 4 + floor(Agility / 2)
- Main AP is then used only for attacks, items, abilities, etc.
- This hybrid approach feels more modern while still being very tactical.

**7. Momentum System (Optional Flavor)**
- Consecutive attacks or movement without using items/abilities grant small bonuses (e.g., +1 accuracy or slight AP refund).
- Encourages aggressive, flowing playstyles.

---

**Design Notes**
- These perks and traits strongly reinforce the three core stats:
  - **Agility** → More actions
  - **Nerve** → Reliability and bonuses
  - **Engine** → Efficiency and fluidity
- The system remains accessible for new players while offering deep optimization for veterans and speedrunners.
- Many of these perks work especially well with the fast Minmax secret endings (particularly the high-mobility ones).
