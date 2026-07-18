# Game Design Fundamentals — Development Status in Inner Tepenia

**What this is:** a short-form companion to `Game_Design_Fundamentals_and_Fun_Architecture.md` (the full
deep-dive on all 14 components). This file skips the theory and just tracks, per item, how developed or
addressed it already is in this project's own existing systems — ordered least-developed to
most-developed, the same "what needs attention first" logic `TODO.md`'s own tier system uses (its
"Decision Required" tier leads, "Completed" trails). Use this as a quick reference for what to keep
developing, and where.

---

## Not Yet Addressed

- [ ] **Legible feedback ("juice")** — no dedicated design pass exists yet for skill-check/combat feedback
  signatures. Largely a late-stage polish concern, reasonable to still be greenfield at this project stage.
- [ ] **Variable-ratio reinforcement** — no loot table or reward-schedule design work found yet. Worth
  addressing whenever itemization/loot design starts.

## Flagged / Minimal Development

- [ ] **Fail-forward design** — no named system yet, but the standing "no good endings" law (see
  `General-Overview-Notes/Game_Design_Principles.md`) and dual-outcome perk structure are philosophically
  adjacent. Needs an explicit pass wherever skill checks gate companion/quest content.
- [ ] **Rhythm/pacing variety** — `Storyline/Main-Story/Main_Quest_Revised_Beat_Structure_TENTATIVE.md`
  exists but is explicitly flagged "sparse/not finalized" in
  `Dev-Road-Map/Early_Access_vs_Launch_Content_Split.md`. Macro-rhythm across beats not yet audited.
- [ ] **Flow (challenge/skill curve)** — no explicit difficulty-curve design pass. The deferred level-up
  spending system (HP immediate, skill points/perks banked) gestures at player-controlled pacing but isn't
  a deliberate flow-curve tool yet.

## Partially Developed

- [ ] **Systemic interaction** — `Game-Mechanics/Combat/Damage_Types.md` and
  `District_Armor_Augmentations_and_Protection.md` exist with real cross-referencing (13-category weapon
  taxonomy), but cross-system emergent combos haven't been explicitly audited district-by-district.
- [ ] **Resource scarcity** — reasonably developed: `Action_Points_Base-Level_System.md`,
  `Action_Points_Perks_and_Traits.md`, `Neural_Overclock.md`, and the full Player Re-Spec cost/trade-off
  suite. Mostly needs a balance-pass discipline check once content is fuller, not new design.
- [ ] **Self-Determination Theory (autonomy/competence/relatedness)** — well-served *implicitly* by the
  MACHINE stat system, dual-outcome perks, and companion approval work, but never audited explicitly
  against the three-need framework. Worth a deliberate check once more companion content lands.
- [ ] **Roleplay affordances over binary morality** — the MACHINE stats + Enneagram companion-personality
  framework already give a genuine multi-axis foundation (no karma meter exists in this project). Not yet
  codified as an explicit dialogue-writing guideline for quest writers to follow.

## Well-Developed

- [x] **Meaningful choice + consequence** — the strongest-developed item on this list. Dual-outcome
  companion perks, the standing no-good-endings law, all 13 districts' full Victory
  Condition/Main-Negative/Minor-Negatives writeups in `Climax_Structure_and_District_Ending_Consequences.md`,
  and the new holographic end-screen concept for delivering it efficiently.
- [x] **Character build as its own puzzle** — extensively developed:
  `Game-Mechanics/Character-Creation/` holds the full Minmax Build system (35 combinations, multiple chart
  formats), Skill_Caps_and_Synergy, MACHINE_Stat_Influence_Map, and Speedrun_Builds.
- [x] **Companion systems with legible state** — `Core-Mechanics/Companion_System.md`, the dual-outcome
  perk structure, and the detailed Early Access/Launch companion-roster staging work
  (`Early_Access_vs_Launch_Content_Split.md`) all point at this being a mature, actively-maintained system.
- [x] **A legible threat that clarifies stakes** — the Great Blackout climax is fully designed and
  explicitly built to give every earlier player choice a throughline back to a stake established since the
  opening hours.
- [x] **Exploration/curiosity loop** — not originally built as a "fun architecture" system, but functions
  as one: the just-completed City History and District History Enhancement Opportunities passes (35 cities
  + 13 districts, 240 flagged ideas total) are, structurally, a large bank of ready-to-place
  curiosity-rewards, once woven into explorable space.

---

## Reading this table

Items in the top two tiers are genuine gaps — no existing system addresses them yet, or only a
philosophically-adjacent one does. Items in the bottom two tiers already have real infrastructure to build
on; the work remaining there is refinement and explicit auditing, not invention from scratch. See
`Game_Design_Fundamentals_and_Fun_Architecture.md` for the full mechanism/example/failure-mode writeup
behind any item here.
