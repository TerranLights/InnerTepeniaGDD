# Tutorial Section Specification

**What this is:** a standalone spec for the opening/tutorial sequence itself — split out into its own file so
it can be referenced independently of the Demo and Early Access planning it overlaps with. The tutorial
sequence (Calethina's lab → Beat 1/Capricorn, per `Storyline/Main-Story/Main_Quest_Revised_Beat_Structure_TENTATIVE.md`)
*is* the Demo's actual content (see `Demo_Content_Specification.md`), but this file exists because the
tutorial has its own design mandate independent of Demo/wishlist concerns — it's the one piece of content
every single player of the finished game will experience, regardless of whether they ever touched a Demo.
Written 2026-07-23.

**Governing principle:** per `Demo_Content_Specification.md` Section 6 (the "New Vegas Lesson," drawn from how
Obsidian built Goodsprings), the tutorial's job is to function as a **compressed, representative summary of
every significantly major thing the player will definitely experience across the full game** — which is why
it should be finalized late in development even though it's chronologically the first thing a player sees.
This file is the content brief that principle produces.

---

## 1. Systems every CRPG tutorial has to cover, in Inner Tepenia's own specific form

- **MACHINE stats mattering immediately.** At least one moment in Beat 1 where a Calculation, Humanity,
  Nerve, or Investigation check visibly changes an outcome — not just a flavor line — so character-creation
  choices land right away. See `Game-Mechanics/Character-Creation/Character_Creation_Overview.md` for the
  full 7-stat system.
- **Tag skill payoff.** Something in the Capricorn diagnostic that's meaningfully easier, or newly possible,
  because of a Tagged skill (the flat +15 bonus), so it reads as a real build decision rather than a number
  on a sheet.
- **One real combat encounter** — enough to establish the turn-based isometric loop, without needing the full
  perk/leveling arc behind it yet.
- **A first level-up**, timed to land during or right after Beat 1 — the lump-sum XP model
  (`feedback_xp_lump_sum_model`) should be *felt* early, not just explained in a menu.

## 2. What makes this specifically an Inner Tepenia tutorial, not a generic one

- **The Reputation Matrix's first registration.** The game's own Fame/Infamy two-axis system
  (`reference_fnv_reputation_chart` is its own design touchstone) needs its first real move to happen here —
  Capricorn's industrial-pressure content is a natural place for a player's early choice to visibly shift a
  rep number, previewing that the whole game tracks this.
- **The throwing-weapons retrieval rule.** Distinctive enough (`Game-Mechanics/Combat/Throwing_Weapons.md` —
  thrown blades stay where they land until retrieved) to deserve a deliberate small moment, not left to be
  discovered by accident.
- **The Bridge Unit / jack-in identity itself.** Calethina literally creates the player as a Bridge Unit at
  game start — this is the actual opening scene, not backstory, so it needs to be established clearly and
  mechanically here. See `project_bridge_unit_and_jackin`.
- **At least one unmarked discovery.** Per `Design_Principles.md` Section IV, something in Beat 1 should be
  findable without a quest marker — teaching the player from minute one that this game rewards actually
  looking, not just following waypoints.
- **The "you can say no" moment.** Declining Calethina's opening request and wandering off is a confirmed,
  real option (per the beat-structure file's own starting-location note) — the tutorial should make this
  legible as genuine agency, not hide it as a secret, since it previews the game's entire non-linear
  philosophy.

## 3. Tone-setting, not mechanical

- **The robot-human relations baseline** ("egalitarian, skewed toward robots," per
  `project_human_robot_relations_baseline`) should be legible through at least one ambient interaction in
  Beat 1 — Capricorn's industrial workforce is a natural place for this to show up without exposition.
- **A planted-not-resolved hook**, exactly as Beat 1 already does with Capricorn's rigged historical judgment
  — the tutorial should teach players that not everything pays off immediately, since that's the game's
  long-arc storytelling shape throughout.

## 4. Deliberately out of scope for the tutorial

Core systems elsewhere in the game that should NOT be introduced here, because they're either too much
apparatus for an opening or illegible until much later content has accumulated:

- The Fragmentation Matrix / re-spec system.
- Full companion recruitment and romance (see `Demo_Content_Specification.md` Section 2 for the reasoning —
  no recruitable companion in this sequence, a non-recruitable NPC stands in).
- The Conflict-Accumulation System (only becomes legible once many beats' worth of choices exist).
- Any DLC content.

---

## Still Open

- The exact opening-task choice among the 8 candidates in
  `starting_task_possibilities_-_Act_1_-_leaving_Calethina's_lab.md` — "The Heating Grid Failure" is only a
  lean in the source beat-structure file, not confirmed. See
  `Storyline/Main-Story/Opening_Scenario_Synthesis_-_The_Capricorn_Data_Log.md` for a proposed synthesis of
  the Capricorn data-log retrieval (already committed to by Beat 1) into a three-path scenario that actually
  hits this file's own checklist — flagged 2026-07-23 as something to come back to, not yet locked in.
- Which specific skill/stat check carries the "MACHINE stats matter immediately" moment, and which Tag skill
  gets the payoff moment — not chosen yet.
- Whether the unmarked discovery and the "say no" branch are the same moment or two separate ones.
- Exact scheduling of the "rough draft early, finalize late" production plan described in
  `Demo_Content_Specification.md` Section 6 — no milestones chosen yet.
