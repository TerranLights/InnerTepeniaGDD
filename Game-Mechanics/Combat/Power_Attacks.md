# Power Attacks

**What this is:** a design draft, not a locked decision — written 2026-07-25. Addresses a mechanic that's
self-evident for the real-time Outer Tepenia trilogy (hold the attack button to charge a power attack,
release to execute) but needs its own genuine translation for Inner Tepenia's turn-based system, played
entirely via mouse and keyboard. Melee and unarmed only — ranged weapons already have their own equivalent
trade-off (see Fast Shot / Trigger Discipline in `Character-Creation/Traits.md`, and the existing Basic vs.
Aimed/Special AP-cost split below).

---

## Why a Direct Real-Time Port Doesn't Work

Outer Tepenia's version trades a **time** resource (how long you hold the button) for power. Inner Tepenia's
turn-based combat has no time dimension inside a turn — the only resource that exists to trade is **Action
Points**. So the honest, faithful translation isn't "simulate a charge-up delay inside a turn" (which would
just be an arbitrary animation, not a real mechanical trade-off) — it's recognizing that AP cost is already
functioning as this game's version of "commitment," and building Power Attack as a melee-specific extension
of a pattern the game already uses.

**The existing pattern this extends:** `Action_Points_Base-Level_System.md` already splits Basic Attacks
(4-6 AP) from Aimed/Special Attacks (6-8 AP, "higher damage or effects") — a generic, weapon-agnostic version
of exactly this trade-off. Power Attack is that same shape, made melee-specific and given a second cost
beyond AP so it isn't just a strictly-better option whenever AP allows it.

---

## The Mechanic — Option C, confirmed 2026-07-25

Of the three candidate shapes weighed, **Option C is the confirmed foundational mechanic**: the risk of a
Power Attack sits *after* the swing lands, not in whether it lands at all. This is the more faithful
translation of real-time "hold to charge, release to strike" games specifically — the actual downside of a
real-time heavy attack is normally the recovery/endlag afterward, not a higher whiff chance. Turn-based
Power Attack ports that same shape: guaranteed accuracy, real damage, and a cost paid on the *following*
enemy turn(s) rather than baked into the attack roll itself.

**Power Attack — melee/unarmed only:**
- **AP cost:** higher than a standard melee attack (mirroring the existing Aimed/Special premium). Exact
  number not set here.
- **Accuracy:** unchanged — a Power Attack is exactly as likely to land as a standard melee attack of the
  same kind. No whiff-more-often penalty of any sort.
- **Damage:** meaningfully higher than a standard attack — enough to matter, not a marginal bump. Exact
  number not set here.
- **The actual cost — vulnerability after the swing, not during it, confirmed 2026-07-25:** landing a Power
  Attack applies **-20% DT and -20% DR** to the attacker, lasting for exactly **one subsequent turn** —
  a clean, self-expiring window that maps directly onto turn-based structure the same way real-time recovery
  frames map onto a real-time clock. This plugs straight into the existing damage formula
  (`Damage_Threshold_and_Damage_Resistance.md`: `Final Damage = max((Base Damage × (100−min(DR,85))/100) − DT,
  Base Damage × 0.15)`) with no new mechanic required — incoming attacks during that one turn simply resolve
  against the attacker's temporarily-reduced DT/DR, hitting harder across the board rather than more often.

**Relationship to existing systems, not a replacement for any of them:**
- **Heavy Handed trait** (`Character-Creation/Traits.md`: +20% melee/unarmed damage, -60% crit damage) is a
  permanent *build-level* choice. Power Attack is a *per-turn tactical* choice. A character with Heavy Handed
  who also throws a Power Attack stacks both — the trait shapes what kind of melee character you are; the
  attack choice is what you do on any given turn. No conflict: Heavy Handed's own cost (weaker crits) and
  Power Attack's own cost (post-swing vulnerability) sit on entirely different axes.
- **Might's melee/unarmed damage bonus** (`Might_Expanded_Systems_Tentative.md`, still a draft file) applies
  underneath Power Attack's own bonus the same way it applies to any other melee attack — no special
  interaction needed.
- **The NODE/crit system** (`Targeting_System.md`: Calculation = crit chance, Investigation = weak-point
  bonus, Nerve = crit severity) applies to Power Attack exactly as it would to any other attack — **this is
  now a fully resolved non-issue under Option C**, since Power Attack no longer touches accuracy or crit math
  at all. The open question this used to raise no longer applies.
- **Rage** (`Signature_Abilities.md`, multi-turn Might-based buff state: cheaper high-damage attacks,
  increased damage taken as an after-effect) turns out to share Power Attack's *exact* underlying shape —
  both are "hit harder now, pay for it in vulnerability after." This is a genuinely nice synergy worth
  building toward deliberately rather than treating as incidental: a Rage-stance character throwing Power
  Attacks is explicitly a high-risk/high-reward burst archetype, with both systems' vulnerability windows
  stacking rather than working against each other.

---

## Trait and Perk Built Directly On This Mechanic — added 2026-07-26

Confirms the "skill/perk synergies" open question below in the direction of "yes, and here are the first two,"
pushing the same risk/reward trade-off in opposite directions:

- **All-In Brawler** (Trait, `Character-Creation/Traits.md`) — the glass-cannon direction. Adds +10× Might to
  Power Attack damage (both normal and crit), but worsens the vulnerability window to **-40% DT/-40% DR for
  two turns** instead of the base -20%/-20% for one. The purest expression of the mechanic's own risk/reward
  shape, pushed to its extreme in both directions at once.
- **Crusher** (Perk, `Perks/Regular_Perks_-_Level-Up.md`, Combat — Offensive, Level 26/M7/N6/E7, 2 ranks) —
  the mitigation direction. Rank 1: +20% Power Attack damage, and the vulnerability window's -20%/-20% base
  penalty is reduced by 10 points to -10%/-10% (one turn). Rank 2: +30% Power Attack damage, and the
  mitigation rises to 20 points — fully canceling the base penalty to zero.
- **How they stack, if a character has both:** Mitigation is a flat point value, not a percentage, so it
  applies uniformly regardless of the base penalty's own size. A character with both All-In Brawler (which
  raises the penalty to -40%/-40%) and Crusher Rank 2 (-20 points of mitigation) nets a **-20%/-20% penalty
  for two turns** (All-In Brawler's own doubled duration is untouched by Crusher, which only mitigates the
  DT/DR percentage) — still a real cost, but meaningfully softened, alongside a very large stacked damage
  bonus from both sources at once. A legitimate, coherent late-game glass-cannon-with-training-wheels build.

---

## The Input Question — Mouse and Keyboard, No Real-Time Charging

Since there's no real-time charge window inside a turn-based turn, "hold to charge, release to strike" can
still exist as a **pure input gesture** rather than an actual timer:

- **Hold the attack button/click** on a valid melee target queues the Power Attack variant of the action.
- **Release** confirms and resolves it — instantly, using the AP cost/damage/accuracy numbers above, not a
  simulated charge delay.
- A quick tap (no hold) resolves a standard attack as normal.

This preserves the *feel* of the input gesture across the trilogy's different control schemes (real-time
hold-and-release in Outer Tepenia; the same hold-and-release gesture as a selection mechanism, not a timer,
here) without pretending Inner Tepenia's combat has a time dimension it doesn't have. An on-screen UI
alternative (a right-click context option, or a dedicated hotkey) should exist alongside the hold gesture for
players who prefer explicit menu selection over a held click.

---

## Open Questions

- Exact AP premium and damage bonus numbers — not set here, needs to go through the same balance pass as the
  rest of the AP economy. **The vulnerability-window penalty itself is now confirmed (-20% DT / -20% DR, one
  subsequent turn)** — only the AP cost and damage bonus remain unset.
- Whether the -20%/-20% DT/DR penalty stacks with itself if the character throws consecutive Power Attacks
  across multiple turns in a row (does a second Power Attack refresh the one-turn window, stack an
  additional -20%/-20% on top, or simply not stack at all beyond the existing debuff) — not decided.
- ~~Whether Power Attack should have its own skill/perk synergies~~ — **resolved 2026-07-26:** yes — see
  the All-In Brawler trait and Crusher perk above, the first two of presumably more to come.
- Whether ranged weapons deserve their own distinct "commit harder" mechanic beyond the existing Fast
  Shot/Trigger Discipline trait pair, for symmetry — not raised by the developer, noted only as a possible
  future parallel question.
