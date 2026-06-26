# Neural Overclock System (Framejack / Berserk / Overclock)

**Status**: Proposed Design  
**Author**: Grok + TerranLights Collaboration  
**Version**: 1.1 (Updated with 8+ Stat Gate)  
**Location in GDD**: Game-Mechanics/Combat/ or Game-Mechanics/Core-Mechanics/

## Overview & Design Goals

This document defines a top-down, turn-based, isometric adaptation of Cyberpunk 2077’s **Berserk / Sandevistan (Framejacking) / Overclock** mechanics, unified under a single cyberware system called **Neural Overclock**.

The system is designed to:
- Reward extreme **MACHINE stat minmax builds** with powerful, flashy gameplay.
- Integrate seamlessly with existing **minmax questlines, unique interactions, secret endings**, and narrative reactivity.
- Maintain strong trade-offs so it does **not** make the game trivially easy.
- Enhance rather than conflict with the AP-driven tactical combat and character progression.

### Compatibility with Minmax Questlines
**No major conflicts** exist. The Overclock system is primarily a **combat/gameplay tool**, while minmax questlines are **narrative/reactivity tools**. They complement each other:

- Stat extremes naturally amplify specific Overclock modes.
- Heavy or repeated use feeds into side content, companion reactions (e.g. Calethina), district idolization, cyberpsychosis events, and alternate endings.
- Acquisition, upgrades, and special variants can be gated behind or rewarded by specific lifepaths and minmax combinations.

## Stat Gate Requirement

To access any Neural Overclock mode, the player **must have at least 8 points** in the associated primary MACHINE stat. This gate:

- Ensures the system feels earned and tied to deep investment.
- Creates meaningful opportunity cost (high specialization in one area weakens others).
- Significantly reduces the risk of the system becoming overpowered for non-minmax playstyles.
- Perfectly aligns with the existing minmax/speedrun philosophy and master chart system.

**Specific Requirements**:
- **Framejack Mode**: Agility 8+
- **Berserk Mode**: Might 8+
- **Overclock Mode**: Calculation 8+

At exactly 8 the mode is functional and strong. Bonuses scale further at 9–10, rewarding full minmax commitment.

## Core Rules (All Modes)

- **Acquisition**: Cyberware implant (craftable, quest reward, early-game choice, or tied to specific builds). The implant itself may have lower prerequisites, but **activation of a mode requires the 8+ stat gate**.
- **Activation**: Costs AP (or a dedicated “Overclock Action”). Enters chosen Mode for **1–3 turns** (duration scales with Engine and upgrades).
- **Cooldown**: 3–5 turns after deactivation.
- **Resource**: **Neural Strain** meter. Builds with use and causes escalating drawbacks.
- **Stat Scaling** (key for balance & minmax synergy):
  - **Engine**: Efficiency, duration, reduced Strain.
  - **Agility**: Framejacking potency, bonus movement/actions.
  - **Might**: Berserk damage and tanking.
  - **Calculation**: Ability/hack optimization and chaining.
  - **Nerve**: Resilience to backlash and control.
  - **Humanity / Investigation**: Narrative flavor and secondary effects (low Humanity increases cyberpsycho risk).
- **Universal Drawbacks**:
  - Health or Strain drain per turn/action.
  - Post-mode debuff window (reduced AP, vulnerability, etc.).
  - Limited total uses per combat / per day (or implant wear).
- **Exploration Use**: Bonus movement tiles or reduced AP costs while active.

## The Three Modes

### 1. Framejack Mode (Sandevistan-style)
**Primary Stat Gate**: Agility 8+  

- **Effects**:
  - Bonus AP or heavily reduced movement/attack costs.
  - One “free” basic action or extra movement phase per turn.
  - Feels like acting in accelerated time while the world slows.
- **Drawbacks**:
  - Rapid Strain buildup.
  - Post-mode “lag” (reduced AP or slowed reactions next turn).
- **Best For**: High Agility/Engine minmax builds, speedrun-style play.
- **Minmax Hook**: Unique Framejack questlines, secret paths, and special interactions.

### 2. Berserk Mode (Rage / Tank-Damage)
**Primary Stat Gate**: Might 8+  

- **Effects**:
  - Significant bonus to damage (especially melee/signature abilities).
  - Increased Damage Resistance / Armor.
  - Possible cleave/multi-hit or “cannot die below X% HP” (with health drain instead).
- **Drawbacks**:
  - Heavy health drain.
  - Restricted fine control (limited precision hacking or certain perks).
  - Loss of accuracy on ranged options.
- **Best For**: High Might melee/tank builds.
- **Minmax Hook**: Synergizes with existing combat perks; unique Berserk narrative branches and endings.

### 3. Overclock Mode (Ability / Hack Spam)
**Primary Stat Gate**: Calculation 8+  

- **Effects**:
  - Reduced AP costs for complex abilities, hacking, item use, and signature abilities.
  - Extra uses or chaining potential.
  - Improved targeting/optimization.
- **Drawbacks**:
  - Very rapid Strain buildup.
  - Risk of random misfires, debuffs, or forced shutdown at high Strain.
  - Health cost on overuse.
- **Best For**: High Calculation tech/ability-focused builds.
- **Minmax Hook**: Direct ties to hacking questlines and computational mastery endings.

## Optional High-Level Structure
At higher tiers, the three modes can be made **mutually exclusive** or very expensive to switch between (mirroring CP2077 OS choices). Lower tiers allow limited mixing. This encourages build commitment and diversity across minmax combinations.

## Balance & Counterplay

The 8+ stat gate, combined with the following, keeps the system from making the game too easy:

- Strong, visible drawbacks and cooldowns that feel heavier on builds with low Nerve or supporting stats.
- Diminishing returns or tiered bonuses (strong at 8, exceptional at 9–10).
- Smart enemy AI: focus-fire during vulnerability windows, cyberware-disrupting attacks, area denial.
- Narrative and mechanical consequences for heavy use (Strain overflow → cyberpsychosis events, reputation hits, unique bad endings).
- Everything scales with existing MACHINE formulas, AP economy, and damage thresholds.
- True power requires deep minmax investment + acceptance of risks.

Even optimized 8–10 builds will have clear weaknesses elsewhere, preserving challenge and replayability.

## Integration Points with Existing Systems

- **Perks**: New entries in Regular, Challenge, Special, and post-Idolization perk lists (some perks could lower effective thresholds slightly or amplify modes at 8+).
- **Minmax Builds**: Dedicated sections in all 35+ stat combo folders for Overclock variants and 8+ interactions.
- **Story & Endings**: Overuse or high-stat activation triggers content in Side-Content, Main-Story, and Endings/Secret-Endings.
- **Technical Notes**: Implement as a data-driven Resource with mode-specific modifiers and stat-gate checks. Fits Godot 4.x architecture and mod support.

## Future Expansion Ideas
- Implant tiers and district-specific mods.
- Visual/audio feedback (screen effects, slowed world during Framejack, etc.).
- Companion reactions and unique dialogue when the player overclocks.
- Speedrun / challenge mode support.

---

**Next Steps**
- Playtest 8+ builds against existing minmax master charts and combat encounters.
- Draft specific perk list and exact numerical formulas.
- Write enemy counter-design document.
- Expand narrative hooks for Calethina and major NPCs.

This system should feel powerful, thematic, and true to the “every choice has weight” and “no good endings” pillars of Inner Tepenia.
