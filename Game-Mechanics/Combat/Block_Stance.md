# Block Stance

**What this is:** a design draft, not a locked decision — written 2026-07-27. Answers a question left open in
`Perks/FNV_Perk_Cross_Reference_Audit.md`'s "Needs a Developer Decision" bucket: whether Inner Tepenia has any
"block" defensive mechanic for enemies at all, since the FNV perk **Unstoppable Force** (x4 damage through
enemy blocks) depends on one existing. Confirmed at the time of that audit: nothing in the combat docs
(`Damage_Threshold_and_Damage_Resistance.md`, `Targeting_System.md`, `Power_Attacks.md`) establishes any kind
of blocking, guarding, or parrying mechanic — this is a genuine blank slate, not a duplicate of an existing
system.

---

## Why a Real-Time-Style Reflex Block Doesn't Work

The obvious real-time translation of "blocking" — a timed reflex input that reduces or negates an incoming
hit — has no home in Inner Tepenia's turn-based structure the same way a real-time charge-and-release power
attack didn't (`Power_Attacks.md`'s own reasoning applies here too). There's no moment inside a turn where a
reflex input could occur. The honest translation has to work through the resource that already governs every
tactical choice in this game: **Action Points**.

**Also ruled out, and why:** a flat percentage chance to block an incoming hit (a dice-roll defense check)
would work mechanically, but conflicts with the game's own binding design law
(`Skills.md`'s "Flat Thresholds, No Dice Rolls" section) — RNG in Inner Tepenia is explicitly reserved for
ranged combat hit chance and aimed-shot probability only, not layered on top as a second combat roll. A
stance-based mechanic keeps blocking fully deterministic, consistent with how DT/DR, Power Attacks, and every
other combat system in this game already resolves.

---

## Real-Game Precedent — Confirmed 2026-07-27

Researched against several existing turn-based games with a "block"/"guard" mechanic, since none of this
needed to be invented from nothing:

- **Persona series (P4/P5/P5R) "Guard" command — the confirmed model for Block Stance.** Spending your turn
  to Guard reduces incoming damage substantially (~50% in P5 Royal), negates weakness-exploitation and
  critical hits, and prevents status conditions that turn — a genuine "give up your action, gain a defensive
  bonus until your next turn" trade, the same shape already drafted below.
- **Slay the Spire / Marvel's Midnight Suns "Block"** — a different shape, considered and set aside: a
  numeric shield/absorption pool gained from specific cards rather than a universal defensive action, decaying
  over time rather than expiring on a fixed turn count. Not the direction chosen.
- **Darkest Dungeon "Guard"** — a genuinely different mechanic (redirecting an *ally's* incoming damage onto
  the guarding character), not self-defense at all. Noted only so it doesn't get conflated with this system.

## The Mechanic — Draft, 2026-07-27

**Block Stance** is an AP-costed defensive action, available to both the player character and enemies (it's
an action, not a perk — anyone with AP to spend can attempt it).

- **AP cost:** higher than a standard action, reflecting genuine commitment to defense over offense — exact
  number not set here.
- **Effect:** entering Block Stance grants a temporary DT/DR bonus that lasts **until the start of the
  character's next turn** — the same "commits now, resolves later" shape as Power Attacks' own vulnerability
  window, just pointed in the defensive direction instead of the offensive one.
- **The cost:** entering Block Stance forecloses attacking that turn — the same opportunity-cost logic that
  already governs every AP decision in the game (spend AP on this, and it's not available for an attack this
  turn). No new resource or mechanic is introduced; this is the existing AP economy applied to a new choice.
- **Duration:** exactly one enemy turn's worth of protection, then the bonus expires — mirrors Power Attacks'
  own "one subsequent turn" window for symmetry between the two opposed mechanics.

**Tentative addition, flagged 2026-07-27 for later review — not yet decided:** Persona's own Guard command
does more than reduce damage; it also negates weakness-exploitation and critical hits entirely for that turn.
Inner Tepenia already has a close analog to build this onto: the NODE targeting system
(`Targeting_System.md` — Investigation governs the weak-point bonus, Nerve governs crit severity tiers).
Block Stance could plausibly negate or reduce those specific bonuses against the blocking character while
active, not just apply a flat DT/DR bump — giving it the same "can't be cheesed this turn" character Persona's
version has. Held as a tentative possibility, not folded into the core mechanic above yet — revisit later.

**Why this needs to exist for both sides, not just the player:** an enemy that can enter Block Stance gives
combat AI a genuine defensive behavior to fall back on (rather than always attacking), and gives
**Unstoppable Force** something concrete to punish — bypassing or specifically countering an enemy currently
in Block Stance — rather than a vague "ignores blocking" clause with no real mechanic underneath it.

---

## Relationship to Existing Systems

- **DT/DR formula** (`Damage_Threshold_and_Damage_Resistance.md`): Block Stance's bonus plugs directly into
  the existing `Final Damage = max((Base Damage × (100−min(DR,85))/100) − DT, Base Damage × 0.15)` formula —
  no new damage-resolution math needed, just a temporary modifier to the existing DT/DR inputs.
- **Power Attacks** (`Power_Attacks.md`): a clean mechanical mirror-image. Power Attacks trade guaranteed
  offense now for vulnerability later; Block Stance trades no offense now for protection later. A player
  could plausibly alternate between the two — Power Attack this turn, Block Stance the next to ride out the
  vulnerability window — a synergy worth keeping in mind once both systems are further along.
- **Unstoppable Force** (`Perks/FNV_Perk_Cross_Reference_Audit.md`, still in "Needs a Developer Decision"):
  this mechanic is what that perk needs to exist before it can move to a real perk-pool entry. Effect
  direction: bypasses or substantially reduces the DT/DR bonus Block Stance grants an enemy, rewarding a
  Might-heavy melee build for pushing through a braced opponent rather than waiting them out.

---

## Open Questions

- Exact AP cost and exact DT/DR bonus numbers — not set here, needs the same balance pass as the rest of the
  AP economy and Power Attacks' own still-open numbers.
- Whether Block Stance should have its own skill/perk synergies the way Power Attacks does (All-In Brawler,
  Crusher) — not yet explored.
- Whether the bonus should be a flat point value (like Crusher's Mitigation) or a percentage, and whether it
  should affect DT, DR, or both — not yet decided.
- How enemy AI decides when to enter Block Stance versus attack — a real behavioral design question once this
  moves past the mechanic-definition stage.
- Exact resolution for Unstoppable Force once Block Stance itself is finalized — currently only a direction
  ("bypasses or reduces the bonus"), not a locked effect.
