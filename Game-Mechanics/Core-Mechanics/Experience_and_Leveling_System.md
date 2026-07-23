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

#### DLC Main Questline XP *(established 2026-07-22)*

Completing a DLC's own central main questline grants a flat lump sum, same lump-sum
principle as district main questlines:

- **Each of the 6 subnet DLCs: 70,000 XP.**
- **DLC 1 — "Echoes of Amundsen" (Kendra Heinrich, South Pole): 200,000 XP** — a
  deliberate outlier, reflecting that this DLC is designed to be brutally,
  mercilessly unforgiving. A player who actually completes it has earned a reward
  well beyond the standard DLC rate.

---

#### XP Banking at the Level Cap *(established 2026-07-22)*

**The rule:** unless the player already owns all 7 DLCs and has reached the absolute
level cap (100), any XP earned that would push the player's level past their
*current* cap doesn't get discarded or floor-capped — it's **banked**. The moment
the player's cap rises (buying and installing any DLC), banked XP is immediately
applied toward the new cap, leveling the player up as far as it allows. If banked
XP still exceeds what the new cap requires, the remainder stays banked, waiting
for the next cap increase — and so on, until either the bank is exhausted or the
player reaches Level 100 with all 7 DLCs owned, at which point there's no further
cap to raise and banking no longer applies (there's nowhere left for surplus XP to
go).

**Worked example:** a player with no DLCs reaches Level 64 (the base-game cap) and
keeps playing, accumulating 10,000 XP beyond the Level 64 requirement. That 10,000
XP is banked, not lost. The player later buys any one DLC, raising their cap by 5
(or by 6, if it's DLC 1). The banked 10,000 XP is immediately applied — the player
levels up as far as the new cap allows, and if any XP is left over after hitting
that new cap, it keeps banking, ready for the next DLC purchase.

**Why:** a direct extension of this system's existing "no permanently missable XP"
principle (see Design Rationale, above) to the level-cap boundary specifically. A
player shouldn't feel their time and effort were wasted just because they hit a
*temporary* ceiling — the cap is a pacing gate tied to available DLC content, not
a statement that further-earned XP has no value. Only the true, final ceiling
(Level 100, every DLC owned) has no "next cap" for banked XP to roll into, so it's
the one case where the banking behavior doesn't apply.

---

#### What Happens on Level-Up *(established 2026-07-10 — deliberate divergence from Fallout: New Vegas)*

**Fallout: New Vegas model (rejected here):** the moment the player levels up, they are dropped straight into the level-up screen and required to immediately choose a perk (and, in some Fallout titles, immediately allocate skill points) before returning to play. The choice can't be deferred.

**Inner Tepenia's model:** leveling up splits into two categories that behave differently:

- **Automatic, immediate effects** — anything that isn't a meaningful choice happens the instant the level-up triggers, no player input required: HP increase, and any other flat level-based character effects (e.g. Environmental Resistance +n%). These aren't decisions, so there's no reason to gate them behind a menu visit.
- **Skill points and perks — banked, not forced.** The player accumulates skill points (per the formula in `Character-Creation/Skills.md`) and earns a perk slot every 2 levels (per `Perks/Regular_Perks_-_Level-Up.md`), but nothing requires spending them the moment they're earned. They simply sit there, available, until the player chooses to open the relevant menu and spend them — mid-quest, back at a home base, or twenty levels later, entirely at the player's own pace.

**Why:** this is one of the very few deliberate departures from the binding Fallout Precedence Law ([[feedback_fallout_precedence_law]]). Forcing an immediate perk choice interrupts whatever the player is doing (combat aftermath, a tense dialogue, mid-exploration) for a decision that often benefits from more information — what the player is about to face, what companion or questline is coming up, what build direction actually makes sense once they've seen more of the game. Letting points and perks bank removes that interruption entirely without changing the underlying progression math.

**How to apply:** any future UI/flow design for leveling up should never force the player into a mandatory allocation screen. The level-up moment itself should be near-invisible except for the automatic effects; perks and skill points remain visible/available in their respective menus (however those end up designed) whenever the player wants to engage with them.

---

#### Open Questions

- **Exact formula** for how gate-checks scale into the quest-completion lump sum,
  and how skill level/stats scale skill-use XP amounts — needs concrete numbers,
  likely modeled after the AP system's formula style (base value + stat-derived
  modifier).
- **Base quest-value tiers — RESOLVED (draft), 2026-07-22.** District Main
  Questline = 3,000 XP; District Under-Questline = 700 XP (~9 avg/district);
  Companion Quest = ~1,500 XP average (≥30 companions, base game); base-game
  Main Questline (Concordia-wide) = 65,000 XP (draft); Activities
  (minigames/crafting/exploration/location discovery/Challenges) modeled on
  real FNV's ~6,289 XP total across 101 base-game challenges — deliberately a
  minor, not major, XP pathway. Full derivation, the FNV baseline numbers used,
  and the pacing goal (Level 64 reachable via ~10 of 13 districts) are in
  `XP_System_Design_Reference.md`.
- **Skill-use XP amounts and diminishing returns** — flat per-success amount vs.
  scaling by difficulty; whether repeat successes on trivial locks/terminals keep
  paying out or taper off (real New Vegas caps this per-lock/per-terminal on first
  success). Still open.
- **Level cap and pacing — partially resolved.** Level-up XP formula verified
  against real FNV data: cumulative XP(n) = (n − 1) × (75n + 50) (first level-up
  costs 200, each one after costs 150 more than the last). Level 64 requires
  305,550 cumulative XP. Full pacing math — how district/companion/main-quest/
  activity/repeatable-quest content adds up against this — is in
  `XP_System_Design_Reference.md`. Still open: exact hours-per-level pacing,
  and cross-reference against `Character_Creation_Overview.md` and the perk
  cadence in `Perks/Regular_Perks_-_Level-Up.md`.
