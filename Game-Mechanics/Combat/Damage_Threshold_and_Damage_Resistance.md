# Combat Mechanics - Damage Threshold, Damage Resistance & Layered Protection

**File:** `Combat_Mechanics_DT_DR.md`
**Location:** `Game-Mechanics/Combat/`
**Date:** June 23, 2026
**System Basis:** Adapted and expanded from Fallout: New Vegas DT + DR mechanics, integrated with the MACHINE stat system and a layered chassis + rare armor model for *Inner Tepenia*.

---

## 1. Overview

*Inner Tepenia* uses a layered damage mitigation system that combines **Damage Threshold (DT)** and **Damage Resistance (DR)** with a sci-fi Bridge Unit chassis.

- Most baseline protection comes from the player’s robotic **chassis** and installed **augmentations**.
- **MACHINE stats** modify how effective that protection is.
- **Rare wearable armor** pieces act as valuable, high-impact additions layered on top (inspired by Cyberpunk 2077’s emphasis on equipped gear while keeping FNV-style tactical depth).
- Wearable armor is **not common** — finding or earning good pieces should feel like meaningful upgrades.

---

## 2. Core Damage Formula

**Final Damage** = `max( (Base Damage × (100 − min(DR, 85)) / 100) − DT , Base Damage × 0.15 )`

**Order of Application:**
1. Apply **DR** (multiplicative percentage reduction, capped at 85%).
2. Apply **DT** (flat subtraction).
3. Apply the **minimum damage floor** (15% of base damage).

**Notes:**
- This creates strong differentiation: DT excels against low-damage attacks, while DR scales better against heavy hits.
- The 15% floor prevents complete immunity while still allowing powerful mitigation builds.
- Critical hits are calculated on **base damage** before DT/DR.

---

## 3. Damage Types

| Damage Type       | DT Effectiveness          | DR Effectiveness          | Typical Sources                          | Notes |
|-------------------|---------------------------|---------------------------|------------------------------------------|-------|
| **Ballistic**     | Very High                 | Moderate                  | Conventional firearms, projectiles       | Classic small-arms combat |
| **Energy**        | Moderate / Lower          | Very High                 | Lasers, plasma, directed energy          | Common in advanced/experimental tech |
| **Explosive**     | Moderate                  | High                      | Grenades, rockets, bombs                 | Area damage |
| **Melee**         | High                      | Lower                     | Blades, blunt weapons, fists             | Close-quarters |
| **Disrupt/EMP**   | Special resistance needed | Special DR or Nerve bonus | Electronic warfare, certain enemies      | Affects robotic systems |
| **Radiation**     | Low                       | Special resistance        | Environmental hazards, certain weapons   | Long-term / lingering threat |

Armor and augmentations can have **per-damage-type** DT and DR values.

---

## 4. Base Chassis Protection (from MACHINE Stats)

Every Bridge Unit has a robotic chassis that provides the foundation of their survivability.

**Base Formulas:**

- **Base DT** = `floor( (Engine × 2.5) + (Might × 1.5) )`
- **Base DR** = `floor(Calculation × 2)` (as a percentage)

**Design Notes on Formulas:**
- **Engine** is the primary driver of overall durability (fits the “operational endurance” theme).
- **Might** adds meaningful physical toughness without dominating.
- **Calculation** provides the main source of percentage-based protection (system optimization and energy handling).
- These values scale naturally with stat investment and feel rewarding without being overwhelming at low levels.

**Example at Level 1 (typical spread):**
- Engine 7 + Might 6 → Base DT ≈ `floor(17.5 + 9) = 26`
- Calculation 6 → Base DR ≈ 12%

Augmentations can add flat DT, % DR, or multipliers to these base values.

---

## 5. MACHINE Stat Modifiers on Armor Effectiveness

MACHINE stats improve how effective your current chassis and armor perform.

| Stat                  | Influence on Armor Effectiveness                          | Example Mechanical Effect |
|-----------------------|-----------------------------------------------------------|---------------------------|
| **Might (M)**         | Improves physical armor plating effectiveness             | +1 DT per 2 points of Might (Ballistic & Melee) |
| **Engine (E)**        | Increases overall chassis durability and sustained resistance | +1 DT per point of Engine above 5; reduces DT loss from damage over time |
| **Calculation (C)**   | Improves energy dispersion and system optimization        | +1% DR per point of Calculation (Energy & Disrupt damage) |
| **Agility (A)**       | Allows better positioning or partial evasion              | Small chance (1% per point) to reduce incoming effective DT by 10–20% |
| **Nerve (N)**         | Maintains armor performance under stress or electronic attack | Reduces DT/DR penalties from Disrupt/EMP damage |
| **Investigation (I)** | Helps identify weak points in enemy armor                 | Bonus to armor penetration when attacking (see Section 7) |
| **Humanity (H)**      | Minor support/leadership bonuses                          | Small DT/DR aura for nearby companions (1–2 points per 4 Humanity) |

These modifiers make stat investment feel impactful on survivability even before finding rare armor.

---

## 6. Rare Wearable Armor Additions

True wearable armor pieces are **rare and valuable**. They are layered **on top** of the player’s chassis and augmentations rather than replacing them.

**How They Work:**
- Rare armor adds **extra DT and/or DR** (often with damage-type specificity).
- They can include powerful bonuses but usually come with drawbacks (energy drain, reduced Agility, visibility to scanners, reputation effects, etc.).
- Some pieces may require minimum MACHINE stat thresholds to equip effectively.
- Availability is tied to exploration, quests, district reputation (especially Idolized status), or the black market.

**Example Rare Armor Pieces:**

| Armor Piece                    | Added DT/DR                          | Bonuses / Drawbacks                              | Source Flavor |
|--------------------------------|--------------------------------------|--------------------------------------------------|---------------|
| **Industrial Carapace Plating** | +18 Ballistic DT, +8% Ballistic DR  | +Endurance in industrial zones; -10% Agility, higher energy drain | Aries / Capricorn districts |
| **Experimental Dispersion Vest** | +10% Energy DR, +6% Disrupt DR     | Small chance to reflect minor energy damage; fragile | Aquarius labs |
| **Shadow Weave Cloak**         | +8 DT (all types), +12% vs Disrupt  | Strong stealth bonuses; visible to advanced scanners, minor Humanity penalty | Pisces black market |
| **Frontier Reinforced Duster** | +12 Ballistic DT, +5% Explosive DR  | Good cold resistance; bulky, reduces Agility    | Sagittarius frontier |

These pieces should feel like exciting, meaningful upgrades rather than standard loot.

---

## 7. Armor-Piercing / Penetration Mechanics

Weapons and ammunition can reduce a target’s **effective DT**.

### Two Types of Penetration:

**A. Flat DT Reduction** (most common)
- Reduces the target’s DT by a fixed amount **before** final damage calculation.
- Examples:
  - Standard ammo: 0 reduction
  - Armor-Piercing (AP) rounds: **−10 to −25 DT**
  - High-penetration experimental rounds: **−30 or more**
  - Some energy weapons: innate **−5 to −15 DT**

**Formula:**
`Effective DT = max(0, Target DT − Penetration)`

**B. Percentage DT Bypass** (advanced weapons)
- Ignores a percentage of the target’s DT.
- Example: Certain plasma or Gauss weapons bypass **30–50%** of DT.

**Combined Example:**
- Target has 40 DT
- Weapon has 15 flat penetration + 25% bypass
- Effective DT = `(40 − 15) × 0.75 = 18.75`

### Ammo Trade-offs
- **Armor-Piercing**: Higher penetration, slightly lower base damage, rarer/more expensive.
- **Hollow Point / Explosive**: Higher damage vs soft targets, but reduced effectiveness against high-DT armor.
- **Standard**: Balanced.

Investigation can provide bonuses to spotting weak points, further improving penetration.

---

## 8. Examples

**Example 1: Mid-game fight (no rare armor)**
- Base Damage: 80 (Ballistic)
- Player: Base DT 28, Base DR 18%
- Calculation: After DR `80 × 0.82 = 65.6` → After DT `65.6 − 28 = 37.6`
- **Final Damage: ~38**

**Example 2: With rare armor**
- Same attack, player now has +15 Ballistic DT and +10% Ballistic DR from rare plating
- Effective DT = 43, Effective DR = 28%
- After DR `80 × 0.72 = 57.6` → After DT `57.6 − 43 = 14.6`
- **Final Damage: ~15** (much better survivability)

**Example 3: Armor-piercing ammo vs high-DT target**
- Target has 45 DT
- Weapon uses AP ammo (−20 DT)
- Effective DT = 25
- Significantly higher damage output against heavily armored enemies.

---

## 9. Additional Notes & Design Goals

- **Chassis as Foundation**: Players should feel capable even without rare armor, thanks to stat investment and augmentations.
- **Rare Armor as Power Spikes**: These pieces should feel exciting and district-flavored.
- **Tactical Depth**: DT rewards smart positioning and fighting weaker enemies; DR rewards preparing for big threats.
- **Balance Goal**: The 15% minimum floor + stat scaling keeps the system fair while still allowing powerful tank or specialized builds.
- **Future Expansion**: Environmental effects (blackouts, extreme cold), critical hit interactions, and district-specific armor perks can be added later.

---

This document provides a complete, cohesive combat protection system that merges FNV’s tactical DT/DR depth with Cyberpunk 2077-inspired emphasis on equipped gear, while staying true to *Inner Tepenia*’s setting and MACHINE stats.
