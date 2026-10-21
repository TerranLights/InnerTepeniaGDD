# The Fallout Precedence Law — the single governing statement

**Binding design law.** This file gathers every statement of the law, with its one exception, in one place so it is easy to find. The shorter statements elsewhere in the repo stay where they are (listed at the end); where any of them differs from this file, this file is the full version.

---

## The law

When the old-school Fallout games (Fallout 1, Fallout 2, Fallout: New Vegas) conflict with each other on a design decision, **Fallout: New Vegas takes precedence over Fallout 1 and 2. No exceptions** (apart from the one format exception below).

| Situation | What Inner Tepenia does |
|---|---|
| Fallout 1/2 do **A**, and New Vegas does **not** do A | A is a **valid option** for Inner Tepenia |
| Fallout 1/2 do **A**, and New Vegas does **B** | Inner Tepenia does **B**, no exceptions |
| New Vegas has no equivalent system | Fall back to Fallout 1/2 |

**Why.** New Vegas is the most refined expression of the classic Fallout design philosophy, and it takes unconditional precedence over Fallout 1/2 when they diverge.

**Scope.** Mechanics, tone, quest design, companion design, and any area where the two games make different choices. Fallout 1/2 remain relevant as spiritual predecessors; New Vegas is the binding reference.

**How to apply.** Any time a design question touches old-school Fallout precedent (perks, skills, stats, combat, inventory, and so on), check New Vegas first. If New Vegas has an answer, that answer is law.

---

## The one exception: format incompatibility (extremely rare)

If a New Vegas mechanic is fundamentally dependent on **real-time 3D gameplay** and **cannot be translated 1:1** into a top-down, turn-based, isometric game, adapt it using **Fallout 1/2's equivalent as the baseline**, since Fallout 1/2 share Inner Tepenia's format.

**The canonical example:** VATS in New Vegas is a real-time-pause targeting overlay. In Inner Tepenia it becomes **NODE**, adapted from Fallout 1/2's AP-based aimed-shot system, which is the format-native equivalent.

**The test for whether the exception applies:** *"Is New Vegas doing this differently because it's a better design, or because it's a 3D real-time game?"* Only the latter triggers the exception. New Vegas's design philosophy almost always applies even when a specific mechanic needs format adaptation.

---

## Deliberate departures (recorded so they are not mistaken for violations)

The law is binding, but the developer can rule otherwise on a specific point. Known departures:
- **Level-up spending is deferred, not forced.** New Vegas drops the player into a mandatory perk choice at level-up; Inner Tepenia banks skill points and perks until the player chooses to spend them (`Game-Mechanics/Core-Mechanics/Experience_and_Leveling_System.md`, "What Happens on Level-Up," 2026-07-10, described there as one of the very few deliberate departures).
- **Quest tracking by dialogue choice.** New Vegas gives no choice about whether the opening quest is tracked; Inner Tepenia lets the player's dialogue answer decide it, and new quests never take the tracker on their own (`Game-Mechanics/Core-Mechanics/Quest_Tracking_and_Active_Quest_State.md`, 2026-10-18).

## A direct consequence: no level-scaling

New Vegas does not scale enemies or loot to the player's level, so Inner Tepenia does not either. The developer's separate immutable law (**No level-scaling, none, no exceptions**, 2026-08-02) is also in the global instructions and in `Game-Mechanics/Universal_Rules.md`.

## Movement points, a worked case (2026-10-18)

The AP file says movement costs 1 AP per tile "as in Fallout 1 and 2." Under the law this falls on the **first row of the table**: New Vegas, being real-time outside VATS, has no turn-based AP-for-movement system, so Fallout 1/2's approach is a valid option for Inner Tepenia (and is also what the format-incompatibility exception would point to). Engine's free tiles and the Nerve-based movement perk are additions on top of that baseline.

---

## Where the shorter statements live (kept where they are)

- `General-Overview-Notes/Game_Design_Principles.md`, "Fallout Precedence Law" subsection.
- `Game-Mechanics/Universal_Rules.md`, "Design Law" section (bottom of the file).
- `Dev-Road-Map/10-Fallout-Design-Reference.md`, introduction ("in effect throughout").
- Mentions: `Code-Architecture/README.md` (line 50, applied loosely to Godot technical decisions), `Code-Architecture/12_Text_Based_Testing_Harness.md`, `to-be-integrated/Dialogue_Tree_Spreadsheet_Setup_Guide.md`, `TODO.md` (quest marker options), and the Experience and Leveling file above.
- The memory copy: `memory/feedback_fallout_precedence_law.md` (in the Claude auto-memory folder for this project, not in the repo).
