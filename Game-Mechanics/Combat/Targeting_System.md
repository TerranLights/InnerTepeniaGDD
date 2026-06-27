# Targeting System (VATS / C.O.R.E. / N.O.D.E.)

**File:** `Targeting_System.md`
**Location:** `Game-Mechanics/Combat/`
**Date:** June 23, 2026 
**Working Title:** VATS (placeholder)
**Final Name Candidates:** C.O.R.E. (Chassis Operational Response Enhancement) or N.O.D.E. (Neural Operating Directive Enhancement)

---

## Core Philosophy

The targeting system in *Inner Tepenia* is based on the classic **Fallout 1 & 2** called-shot VATS system (turn-based, Action-Point-driven, body-part targeting). It has been modernized and expanded to feel native to a world where the player is a **robot** and over half the population consists of robots and hybrids.

**Design Goals:**
- Reward tactical thinking, preparation, and skill investment over pure reflex.
- Emphasize the robotic / analytical nature of the player character.
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

Higher **Calculation** increases accuracy. Higher **Investigation** reduces cost (scanning weak points lowers the processing overhead of targeting them).

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
`Hit % = (Calculation × 4) + (Investigation × 2) + (Agility bonus) + (Weapon Skill) – (Distance) – (Body Part Penalty) + (Nerve Focus Bonus)`

**Calculation** is the primary stat for this system — it represents computing the exact trajectory, strike probability, and damage potential for each targeted component. **Investigation** is secondary — it reduces targeting costs and contributes accuracy by identifying weak points worth targeting in the first place.

### 4. Critical Hits

Critical hits in Inner Tepenia are governed by three MACHINE stats, each covering a distinct dimension of what a "perfect strike" actually means.

**Critical Chance**

`Crit Chance = floor(Calculation ÷ 2) % + Investigation Weak Point Bonus + NODE Bonus + weapon/perk modifiers`

| Component | Source | Notes |
|-----------|--------|-------|
| Base crit chance | `floor(Calculation ÷ 2) %` | CAL 6 → 3%; CAL 10 → 5% |
| Weak point bonus | `floor(Investigation ÷ 3) %` | Only applies when targeting a **scanned/identified** weak point |
| NODE bonus | Flat +% (TBD, ~3–5%) | Applies to all shots fired from within NODE activation |

**Investigation's weak point bonus does not apply to unscanned targets.** It rewards players who spend the AP to scan enemies first — the crit is the payoff for having done the reconnaissance.

**Critical Severity — governed by Nerve**

Nerve does not add to crit *chance*. It determines what the critical hit *does* beyond a raw damage multiplier.

| Nerve | Crit Outcome |
|-------|-------------|
| 1–4 | Extra damage only (standard multiplier, TBD) |
| 5–6 | Crit may cause a light status: Stagger or minor Sensor Scramble |
| 7–8 | Crit reliably causes a meaningful status: Joint Lock, Overheat, or EMP burst |
| 9–10 | Crit can trigger a cascade failure on robot enemies — a critical to the power core destabilizes adjacent systems |

**The three-stat model:**
- **Calculation** — determines how often crits happen ("I computed the perfect strike vector")
- **Investigation** — unlocks crit bonuses by identifying where the weaknesses are ("I already knew where the armor plating gaps were")
- **Nerve** — determines what the crit accomplishes beyond numbers ("I didn't flinch when the window opened")

These three dimensions are independent. A high-Calculation / low-Nerve character crits often but deals only bonus damage. A high-Nerve / moderate-Calculation character crits rarely but causes cascading system failures when it happens. A player who invests in all three gets the full picture: frequent crits, preferentially against scanned weak points, that reliably cause status effects.

### 5. Special Robotic Features

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
- Calculation and Investigation are both highly desirable for combat-focused players, for different reasons: Calculation for raw accuracy and crit frequency, Investigation for cost efficiency and weak point exploitation.
- The system should feel like a natural extension of the player's robotic nature rather than an external game mechanic.
- Nerve's crit severity role means a high-Nerve combat build can be effective without stacking raw damage — cascade failures and status effects create a distinct tactical identity.
- Visuals: Glowing targeting reticles, wireframe overlays, data readouts, subtle digital "scanning" effects.
- Audio: Low mechanical hums, data processing sounds, synthetic voice confirmations ("Target acquired. Weak point locked.").

Let me know when you're ready to expand any section (formulas, body parts list, perks, visual design, etc.) or if you'd like adjustments!
