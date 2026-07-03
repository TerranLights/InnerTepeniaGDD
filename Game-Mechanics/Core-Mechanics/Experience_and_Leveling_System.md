### Experience (XP) System — Inner Tepenia

**Core Design Goal:** Follow the **Fallout: New Vegas model** of quest experience,
not the **Baldur's Gate 3 model**. Established 2026-07-03, non-negotiable design
law for this project.

---

#### The Two Models (why we're rejecting one of them)

**Baldur's Gate 3 model (rejected):** every individual quest step grants its own
small XP award, independently. Skip a step, and that XP is gone forever — there is
no path to recover it. A player who solves a quest efficiently is *penalized*
relative to a player who did every optional sub-step, even if the efficient
player's solution was smarter or more skillful.

> Example: read a book (+15 XP), find an oil lantern (+15 XP), open a chest
> (+15 XP), talk to the quest NPC (+15 XP) = 60 XP total *if you did everything*.
> Skip straight to the NPC and you get 15 XP. "And that's it. Goodbye. Have a nice
> day. Go away now."

**Fallout: New Vegas model (adopted):** the quest itself pays out a single lump
sum of XP on completion. How the player gets there — which optional steps they
found, which they skipped, which order they did things in — is entirely up to
them. A player who skips straight to the end and completes the quest gets the
**full** quest-completion XP, not a fraction of it.

> Same example, our model: skip straight to talking to the quest NPC, complete the
> quest → **full 60 XP**, same as the player who read the book, found the lantern,
> and opened the chest first. The optional steps exist for their own narrative/
> gameplay value (lore, loot, alternate solutions), not as XP checkboxes the player
> is punished for missing.

---

#### Two XP Channels

Inner Tepenia has two distinct sources of XP, matching real Fallout: New Vegas
behavior — they don't get conflated into one system:

**1. Quest-completion lump sum** (the main system, described above). Calculated
once, at the moment of completion, from:

1. **Base quest value** — a fixed amount set per quest based on scope/difficulty
   (main quest > major side quest > minor side quest), same for everyone.
2. **Gate-checks passed** — skill-level thresholds, perk-gated dialogue/action
   options, and similar checks the player passed *anywhere during the quest*
   contribute to the total. A player who had the stats/perks to unlock an
   alternate path is rewarded for having built that character, not for having
   clicked through extra dialogue.
3. **MACHINE stat / perk / trait modifiers** — the player's build adjusts the
   final number (exact formula TBD — likely a percentage modifier off the base,
   similar in spirit to the AP formula's Nerve modifier in
   `Action_Points_Base-Level_System.md`).

All of the above is calculated together and paid out as one lump sum when the
quest completes — not doled out in real time as each individual action happens.
The player sees quest-tracker updates as they go (informational, not a reward),
but the quest XP itself lands once, at the end, as a single number.

**2. Skill-use XP** *(confirmed 2026-07-03)*: mini-activities — lockpicking,
hacking terminals, and comparable skill-driven actions — grant their **own
immediate XP** the moment they succeed, separate from and in addition to any
quest-completion lump sum. This applies whether the action happens inside a quest
or out in the world with no quest attached at all. Unlike quest XP, this is not
held back or bundled — it's a small, direct reward for successfully using a skill,
the moment the skill is used.

---

#### Design Rationale

- **No permanently missable XP.** Since the full amount is available via
  completion alone, a player who finds a faster or smarter solution is never
  penalized relative to a completionist player. Optional content is rewarded
  through its own intrinsic value (loot, lore, character reactions, alternate
  outcomes) — not gated behind a separate, disappearing XP tax.
- **Character build matters, exploration doesn't have to.** A high-Investigation
  or high-Calculation build that breezes past gate-checks earns more XP for
  *being that build*, not for having done more clicking. This keeps MACHINE
  stats, perks, and traits meaningfully tied to progression.
- **Respects player agency.** "How it is that the player reaches the quest is up
  to him/her" — the destination pays out fully; the path there is the player's
  choice, not a scored checklist.

---

#### Level Cap & DLC Progression *(established 2026-07-03)*

Base game level cap is **64**, with a perk slot every 2 levels (32 slots total —
see `Perks/Regular_Perks_-_Level-Up.md`). Each of Inner Tepenia's 7 planned DLCs
raises the cap, mirroring Fallout: New Vegas's own pattern:

| DLC | Cap increase |
|---|---|
| Each of the 6 subnet DLCs | +5 |
| DLC 1 — South Pole (Kendra Heinrich) | +6 |
| **Base + all 7 DLCs** | **64 + 30 + 6 = 100** |

Landing on exactly 100 (50 perk slots at the every-2-levels cadence) rather than
99 was a deliberate choice — a player who owns the complete game shouldn't be one
level short of a perk they'd otherwise have earned.

---

#### Open Questions

- **Exact formula** for how gate-checks scale into the quest-completion lump sum,
  and how skill level/stats scale skill-use XP amounts — needs concrete numbers,
  likely modeled after the AP system's formula style (base value + stat-derived
  modifier).
- **Base quest-value tiers** — what the actual XP numbers look like for main
  quest vs. major side quest vs. minor side quest vs. companion quest.
- **Skill-use XP amounts and diminishing returns** — flat per-success amount vs.
  scaling by difficulty; whether repeat successes on trivial locks/terminals keep
  paying out or taper off (real New Vegas caps this per-lock/per-terminal on first
  success).
- **Level cap and pacing** — how many quests/hours per level, cross-reference
  against `Character_Creation_Overview.md` and the perk cadence in
  `Perks/Regular_Perks_-_Level-Up.md`.
