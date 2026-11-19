# Deathproof (Trait) — placeholder name

**What this is:** a design note, not a locked decision. Written 2026-11-19 from the developer's own description. Like every trait in
`Traits.md`, it is provisional. **"Deathproof" is a temporary placeholder;** the official name is not chosen yet.

---

## The idea, as the developer gave it (2026-11-19)

**The bonus: every death makes the character stronger, with no upper limit.**
- Each time the character dies, they come back **1% stronger**: 1% more HP, 1% more damage, 1% more DT, *"and so on and so forth."*
- **It stacks on every death, without any upper limit.** The developer's example: *"if you've died a thousand times, then you are 1,000%
  stronger than you otherwise normally would be *without* the trait."*

**The trade-off: a permanent penalty to XP gained.**
- **It starts at half.** At the very beginning of the game, with zero deaths, the character gains **half** the XP they otherwise would.
- **Each death adds 0.5% to the penalty**, up to a **maximum penalty of −95%** of XP gained.
- **Floor: at least 1 XP per award.** *"This is so that, for any particular instance that rewards XP, the amount of XP rewarded is never
  0. It's always at least 1."*

**The numbers, worked out from the description** (an orchestrator's reading, for checking; not the developer's words):

| Deaths | Stat bonus | XP penalty | XP actually gained |
|--:|--:|--:|--:|
| 0 | +0% | −50% | 50% |
| 10 | +10% | −55% | 45% |
| 50 | +50% | −75% | 25% |
| **90** | +90% | **−95% (the cap)** | **5%** |
| 100 | +100% | −95% | 5% |
| 1,000 | +1,000% | −95% | 5% |

- Penalty after *d* deaths: 50% + 0.5% × *d*, capped at 95%. **The cap is reached at the 90th death.**
- XP for one award: the base award × (1 − penalty), and never less than 1.
- The stacks **add** (decided, question 3): 1,000 deaths gives +1,000%, eleven times the base value.

**Its shape:** the reverse of the usual death penalty. The character levels slowly all game, but every failure leaves them tougher, so a
player who dies a lot ends up a low-level character with very high stats.

---

## Open questions (flagged, not decided)

1. ✅ **What counts as dying, answered 2026-11-19.** Developer: *"Simply reloading a save doesn't count as dying. The player should've
   chosen something like "return to last save" from a menu or something."* So a death is the character actually dying in play; a reload
   the player chooses for any other reason is not one. **The orchestrator's reading, to confirm:** the death is counted when it happens,
   and the count survives the "return to last save" that follows it, so it is kept outside the save the player returns to. The
   original options were (a) inside the save, lost on reload, or (b) outside the save, kept across reloads.
2. ⏸️ **Deferred to future design and development (developer, 2026-11-19):** *"that is a good point, actually. We'll need to
   address that in future design & development"*. The original question: **Deliberate dying.** After the 90th death the XP penalty stops growing, but the stat bonus keeps climbing without limit. Under
   question 1(b), a player could die on purpose, many times, cheaply. Is farming deaths an intended way to play the trait, or should
   something limit it (deaths only count in combat, or a short cooldown, or only deaths the game was not reloaded straight past)?
3. ✅ **Adding, decided 2026-11-19.** Developer: *"Adding. If it were "compounding", then it would be ridiculous and break the game"*.
   Each death adds +1% of the base value, so 1,000 deaths gives +1,000% (eleven times the base). Compounding (×1.01 per death, about
   21,000 times the base at 1,000 deaths) is ruled out.
4. ⏸️ **TBD (developer, 2026-11-19).** **Which stats does "and so on" cover?** Named: HP, damage, DT. Open: skills and stats, AP, carry weight, critical chance and damage,
   resistances, healing received, speed. Skill and dialogue checks are flat thresholds (`Skills.md`); does the bonus raise the stats that
   feed them, or only combat numbers?
5. ⏸️ **TBD (developer, 2026-11-19).** **Rounding.** Is the reduced XP rounded down, rounded to nearest, or rounded up before the 1 XP floor is applied?
6. **Hardcore Mode** (`Core-Mechanics/Hardcore_Mode.md`): does Deathproof work the same way there, and does a Hardcore death interact
   with its other systems (degradation, permanent companion death)?
7. **Other traits.** With Opposite Day (`Opposite_Day_Trait.md`), XP is exempt from inversion, so the XP penalty stays a penalty; would
   Deathproof's stat bonuses become penalties? That falls under Opposite Day's deferred question 4 (other traits and perks).
8. **The name.** "Deathproof" is a placeholder until the official name is chosen.

---

## Cross-references

- `Traits.md`, Whole-Game Modifier Traits: Deathproof sits beside Opposite Day as a trait that changes a game-wide rule rather than
  trading one stat for another.
- **No Level-Scaling** (cross-project law): unaffected. Deathproof scales the player's own character by deaths; the world, enemies and loot
  never scale with it.
- **Realism vs fun, fun wins** (cross-project law): a death that makes a robot stronger is not realistic, and it is a game rule, so fun
  decides it.
