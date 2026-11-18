# Opposite Day (Trait)

**What this is:** a design note, not a locked decision. Written 2026-11-17 from the developer's own description.
Like every trait in `Traits.md`, it is provisional. Unlike Wild Wasteland (`Wild_Wasteland_Trait.md`), which
changes content and no numbers, Opposite Day changes **every number**: it is a global inversion of effects.

---

## The idea, as the developer gave it (2026-11-17)

> *"Essentially, this would make it so that absolutely everything in the entire game has the opposite effect of
> what it normally does without the trait."*

**Bonuses become penalties, for the same length of time:**
- Something that normally gives **+20 Lockpick for 60 seconds** now inflicts **−20 Lockpick for 60 seconds**.
- Something that normally gives **+3 Humanity for two minutes** now inflicts **−3 Humanity for two minutes**.

**Penalties become bonuses** (each lasting and capped exactly as the penalty would be without the trait; see open question 2, decided):
- Something that normally inflicts **−1 Nerve** now **permanently gives +1 Nerve**.
- Something that normally inflicts **−3 Agility** now **permanently gives +3 Agility**.

**Why anyone would take it**, in the developer's words: *"This sounds like a terrible idea, until you consider
that things in the game that normally inflict penalties now give bonuses."*

**The trade-off the developer named:**
- **It costs:** the in-game equivalents of Fallout's skill magazines and skill books become *"essentially
  worthless"*, since their boosts turn into penalties.
- **It rewards:** a character could become *"brutally overpowered"* by doing things that normally carry a cost,
  such as *"wearing heavy armor and consuming the equivalent of alcohol."*

**Its shape:** a high-risk, high-knowledge build trait. A player who learns which things normally hurt can turn
the whole game's cost structure into a power source. A player who doesn't will be crippled by every helpful
item they touch.

---

## Open questions (flagged, not decided)

Each of these decides how far "absolutely everything" reaches.

1. **What counts as "everything"?**
   - ✅ **Healing and damage: inverted, decided 2026-11-17.** Developer: *"yes, include that, because it would be
     fucking hilarious."* Repair items and every other healing source damage the character.
   - ✅ **Enemy attacks, ADJUSTED the same day (developer, 2026-11-17)**, replacing the first version (in which all
     incoming damage healed):
     - **An enemy's ordinary hit does its normal damage.** Nothing changes there.
     - **An enemy's critical hit heals the character** by the amount it would have dealt.
     - **Any healing past the character's maximum spills over** and heals the **active companion**.
   - **What this does to play,** written down so it is designed for, not discovered:
     - **Enemies that crit often become the safest to fight.** A crit-heavy enemy is a medic with a grudge, so
       their crit rate turns from a threat into a resource.
     - **Fights stay dangerous.** Ordinary hits still hurt, so the character can still die in combat. Unlike the
       first version, a firefight is not a refill.
     - **Help hurts.** A repair kit is a weapon pointed at yourself, and a companion who patches you up mid-fight
       is a hazard, while the enemy's crits patch up both of you.
   - **Follow-ups, answered by the developer 2026-11-17:**
     - ✅ **(1a) The character's own crits heal the enemy**, the mirror of the rule above. *"Yes, because it would
       be funny."* The player's best shots become their worst, so an Opposite Day build wants a low crit rate.
     - ✅ **(1b) Overflow with nowhere to go:**
       - **Normal Mode:** it is lost. *"there's nothing much else that could reasonably happen."*
       - **Hardcore Mode** (`Core-Mechanics/Hardcore_Mode.md`): **the spillover goes back and heals the enemy.**
     - ✅ **(1c) Environmental hazards do normal damage, but of the opposite *type*** (*"fire inflicts cold
       damage, etc etc"*). The pairs come from `Combat/Damage_Types.md`:

       | Type | Becomes | Status |
       |---|---|---|
       | Fire / Thermal | Cold | ✅ the developer's example |
       | Cold | Fire / Thermal | ✅ the same pair, reversed |
       | Radiant | Necrotic, and back | PROPOSED (the damage list derives from BG3, where the two are opposites) |
       | Bludgeoning (falls), Piercing, Slashing, Acid, Force, Lightning, Poison, Thunder, Radiation, EMP, Plasma, and the rest | ? | **OPEN.** No natural opposite. Options: (a) unchanged; (b) each given a designed counterpart; (c) every type with no pair becomes one fixed type |

       What follows: a geothermal vent freezes the character, and Antarctic exposure burns them. Cold resistance
       and heat resistance swap value for an Opposite Day build. Whether armor resistances are read before or
       after the swap is open.
     - ✅ **(1d) Crit-built enemies are intended to feed the character.** *"yes."* **Correction to how the question
       was asked:** the player is **always a robot** (a human player exists only through modding), so No Mercy's
       anti-human half never applies to the player in the base game. Its anti-robot half (+20% crit chance, +50%
       crit damage against robots) does: a No Mercy enemy is a walking repair bay for an Opposite Day robot,
       while its own crits are sent back by (1a).
     - ✅ **(1e) Companion and NPC reactions are a source of jokes.** *"that could be an amazing source of in-game
       jokes."* Placed organically during content design, like Wild Wasteland's moments, with no fixed count.
       Starting ideas: a companion thanking the enemy for the spillover; a companion learning not to "help";
       a medic NPC refusing to treat the player; an enemy confused that its best shot made things worse.
   - ✅ **Exempt, decided 2026-11-17 (developer):** these do **not** invert.
     - **XP:** *"because then, the player would never level up, and that would just be punishing the player
       needlessly."*
     - **Carry weight, AP costs and prices:** *"because there wouldn't be an "opposite" to be had."*
     - **Reputation:** *"because then, the game would be utterly broken."*
2. ✅ **Duration: identical to the effect without the trait, decided 2026-11-17.** Developer: *"the time-period
   and/or cap/limit is identical to whatever it is without the trait. It's just the effect that's reversed."*
   Heavy armor's −3 Agility, which lasts while the armor is worn, becomes +3 Agility while it is worn. Only a
   penalty that is permanent without the trait becomes a permanent bonus. The "permanently" in the opening
   examples applies to that case.
3. ✅ **Stacking and caps: identical to the effect without the trait, same ruling.** A source that stacks
   without the trait stacks the same way with it; one that is capped is capped at the same limit, now as a
   bonus. The "brutally overpowered" ceiling is therefore the game's own penalty ceilings, reversed: as high as
   the worst the game can do to a character without the trait.
4. ⏸️ **Deferred until the perks are determined (developer, 2026-11-17):** *"that's something that we'll need to
   investigate once the Perks are actually determined, but I imagine it would be very funny."* The original
   question: **Other traits and perks.** Are other traits' own bonuses and penalties "things in the game"? If so, taking
   Opposite Day alongside, for example, Hot Tempered would invert that trait's numbers too. Perks: the same
   question. And Opposite Day has no numbers of its own to invert.
5. ⏸️ **Deferred, to be addressed when the time comes (developer, 2026-11-17).** The original question: **The
   alcohol equivalent.** `Traits.md` records that Glitch-Coolant is *social and flavor, not a combat-chem
   or addiction mechanic*. So the "consume the equivalent of alcohol" route depends on a consumable with a
   real stat penalty existing. That is the same missing system Logan's Loophole is blocked on.
6. ⏸️ **Deferred, to be investigated later (developer, 2026-11-17).** The original question: **Hard-coded
   effects.** Several traits carry a *hard override* rather than a number: Demagogue's universal
   first-impression skepticism, Fists First's loss of de-escalation options, Broad Strokes' blindness to
   detail. Do those invert (into, for example, universal first-impression warmth)? Or does Opposite Day touch
   numbers only?
7. ✅ **Story and dialogue checks are NOT inverted, decided 2026-11-17.** Developer: *"if they did, the game would
   be beyond-broken."* The checks are flat thresholds (`Skills.md`). Opposite Day changes only the stats feeding
   them; the thresholds and the pass/fail logic are untouched.
8. ✅ **The tell: required, decided 2026-11-17.** Developer: *"it should be clearly noted so that there's no
   confusion about what's happening."* Every inverted effect is clearly marked to the player, since the item
   and effect descriptions would otherwise be wrong for them. The marking's exact form (a distinct color or
   icon on inverted buffs and debuffs, inverted wording in descriptions, a combat-log line on a reversed crit)
   is settled during UI design.

---

## Cross-references

- `Traits.md`, Fallout-Adapted Traits: Wild Wasteland is the nearest structural cousin (a whole-game modifier
  rather than a stat trade), and Logan's Loophole has the same consumable-system blocker as question 5.
- **No Level-Scaling** (cross-project law): unaffected. Opposite Day changes the player's own effects, never
  the world's difficulty.
