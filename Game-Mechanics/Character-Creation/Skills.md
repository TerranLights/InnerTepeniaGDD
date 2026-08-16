# Skills & Leveling System

Skills range from **1 to 100**, though each skill's actual reachable maximum is capped by its single governing MACHINE stat — see `Skill_Caps_and_Stat_Synergy.md`. Skills are improved through use, trainers, skill books, quests, and level-up points.

There are **26 skills** total. **Finalized 2026-07-26**, after a full restructure: every skill is governed by exactly **one** MACHINE stat, never a blend (the multi-stat blending in the Skill Point Gain formula below is a separate system that sizes the total point pool, not any individual skill's own scaling). Most of what used to inflate the count to 44 turned out, on inspection, to be perks — a specific technique or unlock — rather than skills, a broad domain worth investing points in. Those moved to `Perks/Regular_Perks_-_Level-Up.md`, gated by Level + stat + skill thresholds instead. 25 is deliberately closer to Fallout: New Vegas's own 13-skill count than the old 44 ever was — a natural consequence of skills and perks finally being separated correctly. Full restructuring history lives in `Skills_Review_-_Verb_vs_Noun_Audit.md`. **Reopened to 26, 2026-07-28:** **Performance** (instrument-playing, BG3-inspired) was added under Humanity — the one exception to the otherwise-locked 25, see its own entry in the Full Skill List and the Tag Skills section below for its unique start-item behavior.

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

**Terminology, confirmed 2026-08-16 — binding for all writing about this system, not just formal spec: these are
"checks," never "rolls."** The word "roll" itself implies randomness that doesn't exist here, even used
casually or descriptively — there is no dice, no chance, no probability distribution behind a skill or stat
check anywhere in Inner Tepenia or the wider Outer Tepenia series. Say "a Repair check," "a Humanity check," "an
Investigation check" — never "a Repair roll." (Ranged combat hit chance and aimed-shot body-part probability
remain the sole named exception where actual randomness applies, per above — "roll" is accurate language there,
and only there.)

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

**Performance's unique Tag behavior, added 2026-07-28 — the first of its kind in Inner Tepenia:** Tagging
**Performance** additionally grants a starting instrument item, the same way FNV grants a starting laser
pistol to a character who Tags Energy Weapons. The player doesn't otherwise start the game with an
instrument — Tagging Performance is the sole way to begin with one. This is a genuinely new category of Tag
effect (a start-item grant, not just a flat point bonus); whether any other skill gets a similar treatment is
open, not decided here.

---

## Full Skill List

Organized by governing MACHINE stat rather than by theme — every skill listed under a stat is governed by
that stat alone. Where a skill's scope could be ambiguous, a short note clarifies it.

### Might (3)
- Athletics — raw physical capability: forcing open jammed doors/hatches, hauling yourself somewhere under load, feats of strength. The "can you overpower this" skill.
- Blunt Melee
- Mechanical Weapons

### Agility (4)
- Sneak
- Sleight of Hand
- Acrobatics — precision movement: balance, vaulting, tumbling/dodging, reduced fall damage. The "can you finesse your way past/through this" skill — distinct from Athletics' raw-power approach to the same kinds of obstacles.
- Bladed Melee

### Calculation (4)
- Chemistry — one of several skills descended from a single broad "Science" concept
- Hacking
- Cryptography — a distinct discipline from Hacking: securing/breaking codes and encryption, not breaking into systems
- Energy Weapons

### Humanity (4)
- Narrative
- Speech
- Insight
- Performance — instrument-playing, added 2026-07-28, BG3-inspired; see "Tag Skills" above for its unique starting-instrument behavior when Tagged

### Investigation (4)
- Repair
- Lockpick
- Medicine — treats both human injury/illness and robot vital-system instability under one clinical skill
- Biology — one of several skills descended from a single broad "Science" concept; covers biological/life-sciences knowledge, distinct from Chemistry, Hacking, and Cryptography's own slices of that same territory; **moved here from Humanity, 2026-07-28** — pattern-recognition/analysis of biological systems fits Investigation's governing definition more directly than Humanity's empathy/social-awareness focus

### Nerve (4)
- Deception
- Barter
- Guns
- Explosives

### Engine (3)
- Survival
- Outdoorsman
- Unarmed

**Specialized/Cultural is no longer a skill category.** Its former skills ([NAME TBD], Robot Religion Insight,
Cultural Performance & Resonance, Memory & Consciousness Manipulation) were cut entirely — general player
actions rather than an investable domain or a worthwhile perk. The category itself survives only as a
perks-only bucket (Ossuary Resonance, Sonic Attunement, Golden Eye Calibration, Holographic Projection) in
`Perks/Regular_Perks_-_Level-Up.md`, mixing true quest-gated perks (no stat/skill threshold — completion of
the questline is the gate itself) with Ossuary Resonance's own genuine stat/level gate, which simply never had
a better-fitting home.

---

**Design Note**:
A focused skill pool + limited points per level + strong Tag bonus creates clear build identity and high replayability. Hidden paths rely heavily on specific skill synergies. Investigation meaningfully influences how many points you receive, rewarding analytical builds while punishing extremely low Investigation. Skill *breadth* now comes primarily from the much larger perk pool (`Perks/Regular_Perks_-_Level-Up.md`) built on top of these 25 skills, rather than from the skill list itself trying to cover every specific technique.
