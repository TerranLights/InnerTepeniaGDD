# Targeting System (VATS / C.O.R.E. / N.O.D.E.)

**File:** `Targeting_System.md`  
**Location:** `Game-Mechanics/Combat/`  
**Date:** June 23, 2026  
**Working Title:** VATS (placeholder)  
**Final Name Candidates:** C.O.R.E. (Chassis Operational Response Enhancement) or N.O.D.E. (Neural Operating Directive Enhancement)

---

## Core Philosophy

The targeting system in *Inner Tepenia* is based on the classic **Fallout 1 & 2** called-shot VATS system (turn-based, Action-Point-driven, body-part targeting). It has been modernized and expanded to feel native to a world where the player is a **Bridge Unit** and over half the population consists of robots and hybrids.

**Design Goals:**
- Reward tactical thinking, preparation, and skill investment over pure reflex.
- Emphasize the robotic / analytical nature of Bridge Units.
- Integrate deeply with MACHINE stats (especially Investigation, Calculation, and Nerve).
- Create meaningful interaction with the DT/DR armor system.
- Feel advanced and "in-universe" rather than purely game-mechanical.

---

## System Flavor (Placeholder)

Until we choose between **C.O.R.E.** and **N.O.D.E.**, the system is internally referred to as **VATS**.

- **C.O.R.E.** flavor: Industrial, foundational — "Accessing core combat protocols."
- **N.O.D.E.** flavor: Analytical, neural — "Running predictive targeting subroutine."

---

## Core Mechanics

### 1. Activation
- Activated in combat via hotkey or dedicated input.
- Enters **Focused Analysis Mode** — time slows significantly (but does not fully pause).
- The player has a limited **Analysis Window** (typically 4–8 real-time seconds, or a number of internal "ticks").
- During this window, multiple targeted shots can be queued.

### 2. Cost System
Uses a hybrid resource cost instead of pure Action Points:

- **Primary Cost**: **Processing Cycles** (tied to Calculation + Engine).
- **Secondary Cost**: Minor **Energy** or **Neural Load** drain.

**Basic Cost Formula (starting point):**
`Cost = Base Cost + (Distance Modifier) + (Body Part Difficulty) – (Investigation Bonus)`

Higher **Calculation** and **Investigation** reduce costs and/or increase accuracy.

### 3. Targeting & Hit Chance

**Key Body Parts / Targets** (adaptable for humans, robots, and hybrids):
- **Head / Sensor Array** — High critical chance, strong Investigation synergy.
- **Torso / Main Chassis** — Balanced.
- **Power Core / Reactor** — High damage + risk of explosion/overheat. Partially bypasses DT.
- **Joints / Actuators** — Crippling (slows or disables movement).
- **Limbs / Weapon Mounts** — Disarm or reduce outgoing damage.
- **Neural Core / Bridge Interface** — Strong Disrupt / psychological effects (especially vs robots).
- **Scanned Weak Points** — Special highlighted targets that appear after successful analysis.

**Hit Chance Formula (starting point):**
`Hit % = (Investigation × 4) + (Calculation × 2) + (Agility bonus) + (Weapon Skill) – (Distance) – (Body Part Penalty) + (Nerve Focus Bonus)`

**Investigation** is the primary stat for this system — it represents your ability to scan and exploit weaknesses.

### 4. Special Robotic Features

These features differentiate the system from classic Fallout VATS:

- **Predictive Targeting** — High Calculation shows ghost trajectories or predicted movement.
- **DT Reduction / Bypass** — Targeting specific components (joints, power cores, sensor arrays) can ignore or reduce a portion of the target's DT.
- **Status Effects** — Joint Lock, Overheat, Sensor Scramble, EMP Pulse, etc.
- **Energy Feedback** — Successfully hitting power-related weak points can sometimes refund small amounts of energy.
- **Multi-Target Queuing** — Chain shots across multiple enemies in one activation (with increasing cost).

### 5. Risks & Balance

- **Focus Drain** — Taking damage while in Analysis Mode drains Nerve and may reduce accuracy.
- **Over-analysis Penalty** — Extended or repeated use causes diminishing returns or a short cooldown (processor heat buildup).
- **Enemy Counter** — Advanced robots or high-Calculation enemies can resist or partially counter your targeting scan.

---

## Example Combat Flow

1. Combat begins. You activate the targeting system.
2. Time slows dramatically. Your sensors highlight potential weak points on enemies.
3. You spend Processing Cycles to queue targeted shots (e.g., "Power Core — 42% chance, high damage + Overheat risk").
4. You can queue 2–4 shots depending on your stats and remaining resources.
5. Time resumes and the queued shots resolve with precise, robotic flair.

---

## Design Notes & Future Expansion

- Strong synergy with the DT/DR layered protection system.
- Investigation becomes a highly desirable stat for combat-focused players.
- The system should feel like a natural extension of being a Bridge Unit rather than an external game mechanic.
- Visuals: Glowing targeting reticles, wireframe overlays, data readouts, subtle digital "scanning" effects.
- Audio: Low mechanical hums, data processing sounds, synthetic voice confirmations ("Target acquired. Weak point locked.").

This document serves as the foundation. We can iterate on specific formulas, body-part effects, perk integrations, and visual/audio design as needed.

---

**Ready for your repo.**  
You can paste this directly into `Game-Mechanics/Combat/Targeting_System.md`.

Let me know when you're ready to expand any section (formulas, body parts list, perks, visual design, etc.) or if you'd like adjustments!
