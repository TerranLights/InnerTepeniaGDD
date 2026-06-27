# Might — Expanded Systems (TENTATIVE)

**Status**: Draft for design review. Everything here is a proposal. Keep, modify, or discard any element during a dedicated design pass.

**Goal**: Raise Might from 5/44 skills (11%) to a stat that feels as consequential as Agility or Engine outside of direct combat, without forcing it to be mandatory or overshadowing other stats.

**Core principle**: Might is the *brute-force path*. Other stats offer elegant solutions — Calculation hacks the lock, Investigation finds the hidden route, Nerve talks the guard down. Might walks through the door.

---

## System 1: Carry Weight

The player's carrying capacity is gated by Might. This affects which equipment loadouts are viable and how much salvage can be hauled per expedition.

**Proposed formula:**
> `Carry Capacity = 40 + (Might × 12)` *(units TBD — could be kg, mass units, equipment slots)*

| Might | Carry Capacity |
|-------|---------------|
| 1     | 52            |
| 3     | 76            |
| 5     | 100           |
| 7     | 124           |
| 10    | 160           |

**Encumbrance tiers (tentative):**
| Load | Effect |
|------|--------|
| 0–49% | No penalty |
| 50–74% | –1 AP per turn |
| 75–89% | –2 AP per turn, movement costs +1 AP/tile |
| 90–99% | –3 AP, crawling speed only |
| Over cap | Cannot move |

**Design notes:**
- High Engine reduces encumbrance *penalties* (efficiency), but Might sets the *cap*. A high Engine / low Might character is efficient but limited on what they can carry.
- Heavy weapons (sledgehammers, mounted salvage gear, large energy weapons) have Might minimums. Using them below minimum incurs an AP cost penalty per attack.
- Relevant to salvage-focused builds — players who dump Might sacrifice haul efficiency and must make more trips or rely on companions.

---

## System 2: Melee and Unarmed Damage Bonus

Might directly scales the damage output of all unarmed strikes and melee weapons. This makes a dedicated Might build viable in combat without requiring separate skills to carry the load.

**Proposed formula:**
> `Melee Damage Bonus = floor(Might ÷ 2)`

| Might | Melee Bonus |
|-------|-------------|
| 1     | +0          |
| 3     | +1          |
| 5     | +2          |
| 7     | +3          |
| 9     | +4          |
| 10    | +5          |

**Design notes:**
- This is a *flat damage bonus* added on top of weapon base damage and skill modifiers, similar to Fallout's Strength damage bonus.
- For a robot, "unarmed" could be chassis strike, hydraulic slam, or pneumatic impact — flavor should feel mechanical, not biological.
- Improvised Weaponry & Combat Jury-Rig skill synergizes strongly: a high Might + high Improvised Weaponry character can turn any salvage object into a lethal weapon.
- Non-Lethal Restraint & Subdual: Might determines whether a grapple succeeds outright, or requires an opposed Agility check.

---

## System 3: Forced Entry and Physical Shortcuts

High Might opens physical routes and shortcuts that bypass skill checks, locks, and blocked paths. This gives Might a consistent utility function in exploration and quest design — not just in combat.

**Proposed threshold system:**

| Might | What can be forced |
|-------|--------------------|
| 3     | Standard interior doors, lightweight barricades, rusted gates |
| 5     | Reinforced residential doors, light blast doors, collapsed light debris |
| 7     | Heavy industrial doors, thick rubble, structural panels |
| 9     | Military-grade barriers, blast-sealed hatches |
| 10    | Even some "impassable" structural walls (with significant noise / debris) |

**Design notes:**
- Forcing entry is always *louder and messier* than picking a lock or hacking a panel. High Investigation/Agility solutions are quieter. Might is valid but not stealthy.
- Each forced entry should produce environmental consequences: noise alerts nearby enemies, structural debris may block the path afterward, power conduits may rupture.
- In engineering quests, Might checks can allow the player to physically move heavy grid components that others cannot shift — a concrete shortcut that bypasses a puzzle solution.
- Forced entry should never be the *only* solution, always an *additional* solution. This preserves player freedom.

---

## System 4: Physical Intimidation in Dialogue

Separate from Nerve-based psychological intimidation (see Nerve Expanded Systems). Might-based intimidation is demonstrating *physical capacity* — a show of force, a controlled demonstration of what you could do to someone.

**Proposed threshold dialogue unlocks:**

| Might | Unlocks |
|-------|---------|
| 4     | "You could crush that" — basic threat displays, stopping an attack with one hand |
| 6     | Can physically restrain an NPC mid-conversation as a warning |
| 8     | Bending weapons, shattering objects, structural demonstrations of power |
| 10    | Even hardened combat veterans register a real threat assessment |

**Design notes:**
- Might intimidation works best against physically-aware NPCs (combat veterans, security robots, gang enforcers). It is *less effective* against purely intellectual or political NPCs, who may not register physical threat as relevant to their position.
- Nerve-based intimidation (psychological authority) and Might-based intimidation (physical dominance) can *stack* or *conflict* depending on the NPC type and context.
- Low Might + attempting physical intimidation = the NPC calls the bluff. Possible hostile outcome.
- High Might physical intimidation should feel like a quiet, controlled moment — not a tantrum. The robot that calmly bends a metal pipe in half is more frightening than the one that shouts.

---

## System 5: Heavy Equipment Operation

Certain weapons, tools, and industrial machines have a Might minimum. Operating them below minimum is possible but costly.

**Proposed categories:**

| Category | Might Min | Penalty if Below |
|----------|-----------|-----------------|
| Standard sidearms / light tools | 1 | None |
| Two-handed weapons / medium salvage gear | 4 | +2 AP cost per use |
| Heavy weapons / industrial cutters | 6 | +4 AP cost, –15% accuracy |
| Mounted or crew-served weapons | 8 | Cannot fire solo (requires companion assist) |
| Prototype or ancient heavy ordnance | 10 | Cannot use at all |

**Design notes:**
- High Engine *reduces* AP cost of operating equipment (efficiency), but Might *enables* operating it at base cost. A high Engine / low Might character can use light tools very efficiently but hits the heavy weapon wall.
- Mounted weapons that require Might 8 but can be used with a companion assist at lower Might — ties into companion mechanics and Nerve (loyalty) systems.

---

## Tentative New Skills (Optional — for design consideration)

These are not committed additions to the 44-skill list. They are options to consider if Might still feels thin after the above systems are implemented.

**Option A: Structural Breach & Forced Entry** (Might)  
A dedicated skill for physical shortcuts — forced doors, structural demolition, debris clearing. Currently this is handled as a flat Might threshold check. A skill version would allow lower-Might characters to invest in this capability, at the cost of skill points.

**Option B: Physical Threat & Displays of Force** (Might + Nerve)  
A combined skill for physical intimidation that bridges Might (the capacity) and Nerve (the controlled menace). Would replace the threshold-based approach above with a skill-check approach, allowing diverse builds to attempt physical intimidation at a skill cost.

**Option C: Heavy Arms Operation** (Might + Engine)  
A skill for operating heavy weapons and industrial machinery. Could subsume the Might minimum system into a skill check, letting characters invest in this specifically rather than needing a raw Might threshold.

---

## Summary: What Might Would Now Govern

| Domain | System |
|--------|--------|
| Physical combat power | Melee / unarmed damage bonus |
| Equipment viability | Carry weight cap, heavy weapon minimums |
| Exploration shortcuts | Forced entry threshold checks |
| Social leverage | Physical intimidation dialogue |
| Quest utility | Structural installation, heavy component movement |
| Skill coverage | 5 existing skills (Jury-Rigging, Frontier Survival, Non-Lethal Restraint, Improvised Weaponry, Defensive Posturing) |
