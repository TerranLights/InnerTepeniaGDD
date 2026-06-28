# Phase 4 — Perks

**Prerequisite:** Phase 1 complete (stat system settled — can't design Might/Nerve-specific perks until the stats are final). Phase 2 underway (companion quest perks require companion questlines, which require factions to be designed).

**Parallel with:** Phase 3 (Characters). These phases can run simultaneously.

**What this phase does:** Completes all six perk categories that currently have no files, and adds the remaining 99 level-up perks (61 designed, 160 target).

**Current state:** 
- Level-up perks: 61/160 designed
- Challenge perks: ~7 designed, categories defined
- District capstone perks: ✅ complete (24)
- Companion perks: ❌ no file created
- Quest/choice perks: ❌ no file created
- Skill milestone perks: ❌ no file created
- World/discovery perks: ❌ no file created
- Doll/Idolization perks: 🟡 partially covered in capstone file

---

## Design Principles for This Phase

### Perks must express build identity

Each perk should change how the player plays the game, not just increase a number. The standard from Fallout 1/2: perks are rare enough to feel like identity statements. Inner Tepenia's level-up schedule (160 perks over 64 levels = ~2.5 per level) is denser than F1/2 but equivalent to FNV. The FNV lesson: when perks are this frequent, each one must still be specific enough to change behavior. Flat stat bonuses are the floor, not the ceiling. A perk that increases Agility by 1 point is filler. A perk that converts 10% of Agility into bonus critical hit detection probability is a build decision.

### Perks should have identifiable voices

Looking at the existing 61 level-up perks: the best ones feel like they were written for a specific kind of player making a specific kind of choice. The worst ones feel like they were written to fill a slot. When designing new perks: before writing the mechanical effect, ask "who is this perk for, and what does it say about how they're playing the game?" If the answer is "anyone who happens to have this stat level," the perk isn't specific enough.

### Companion perks: presence as design constraint

Companion perks should be thematically tied to the companion. Favi della Torre's presence should produce something different from Villena Hiresvett's presence. The perk shouldn't just be a bonus — it should tell the player something about who this companion is and what they bring to shared work. Design the thematic logic before designing the mechanical effect.

### Quest/choice perks: consequences that follow you

These are one of the GDD's most distinctive earned perk categories. They function as the game remembering what you did. The design constraint: a choice perk should not be available after the choice has passed — you either made the choice or you didn't, and the perk reflects that. The mechanical effect should be appropriate to the magnitude of the choice. A minor choice produces a minor perk. A major irreversible choice produces a perk significant enough to feel like what it is.

### Skill milestone perks: escalating rewards for deep investment

The model: investing 50 points in a skill unlocks one behavior, 75 unlocks another, 100 unlocks something else. The milestone perks are progression rewards that change what the skill can do, not just how well it does it. Science 75 might unlock a new category of Engineering interaction rather than just adding a flat Science bonus. The design question for each skill: what would change if a practitioner went from expert to master? What becomes possible that wasn't before?

### World/discovery perks: the game remembering what you found

These perks reward exploration and engagement with specific world-content. The model: visiting a location, reading a terminal, witnessing an event, or speaking to a specific NPC triggers the perk. The mechanical effect should be thematically consistent with what was discovered. Finding the Deep Level Keeper's hidden archive might produce a perk about historical knowledge — a bonus to Investigation checks about pre-war history. Finding the Memorial Tower in Janbogo might produce a perk about understanding grief — a bonus to Humanity checks involving loss.

---

## 4.1 — Create the Five Missing Perk Files

**Priority: Highest (structural work).**

Before any content can be written, the files need to exist with their framework intact. Each file should be structured consistently with the existing perk files.

**Files to create:**
- `Companion_Perks.md` — one section per companion
- `Quest_and_Choice_Perks.md` — organized by quest/arc, with sub-sections for specific choices
- `Skill_Milestone_Perks.md` — organized by skill, with each skill's 50/75/100 milestone effects
- `World_and_Discovery_Perks.md` — organized by world region, cross-referencing specific locations
- `Doll_Idolization_Perks_Extension.md` (or extend the existing capstone file) — if the capstone file partially covers this, audit what's missing and add it

---

## 4.2 — Level-Up Perks: Design the Remaining 99

**Priority: High, but can proceed incrementally.**

61 perks designed. 99 more needed. This is substantial but workable as a sustained project rather than a single session.

### Approach

Design in thematic batches rather than numerically. The existing 61 perks already establish the tone and mechanical register. Work through the remaining MACHINE stat categories that are underserved:

1. **Might perks** — blocked until Might stat is finalized (Phase 1 task). Complete last within this batch.
2. **Nerve perks** — blocked until Nerve stat is finalized (Phase 1 task). Complete last within this batch.
3. **Agility perks** — map existing Agility perks, identify the build archetypes they don't yet support, fill the gaps.
4. **Calculation perks** — same audit approach.
5. **Humanity perks** — same audit approach. Humanity is the stat most directly connected to the guiding principles; its perks should include some that specifically engage with the robot experience and the human-robot relationship.
6. **Investigation perks** — same audit approach.
7. **Engine perks** — same audit approach.

For each stat: list the existing perks, identify the build archetypes that are missing, design perks to fill those gaps. Don't design 99 perks from scratch — design the ones the existing 61 haven't covered.

### Quality bar

Every level-up perk should pass the following:
- Does it change how the player plays, not just how well?
- Is it specific enough that two different builds would make different use of it?
- Is it thematically coherent with the MACHINE stat it derives from?
- Does it have a name that's interesting enough to make the player want to take it?

---

## 4.3 — Challenge Perks: Complete the Category

**Priority: Medium.**

~7 challenge perks designed, categories defined. Challenge perks are earned by performing specific in-game feats (killing 50 enemies of a specific type, completing a specific difficult combat without taking damage, etc.). They're mechanical rewards for specific forms of engagement.

The design principle: challenge perks should reward behavior the game wants to encourage without making that behavior mandatory. A player who never seeks challenges can complete the game — but a player who does gets visible mechanical rewards that reflect their investment.

Targets: approximately 100-150 challenge perks. This is the largest single category by target count.

Design in thematic batches:
- **Combat excellence challenges** — kill counts, accuracy challenges, combat style restrictions
- **Dialogue/skill challenges** — pass a certain number of skill checks, negotiate X successful peaceful resolutions
- **Exploration challenges** — discover a certain percentage of each district's spaces, visit all locations in a region
- **Relationship challenges** — reach Idolized with multiple districts simultaneously, complete X companion quests
- **Survival challenges** — complete combat encounters under specific restrictive conditions
- **Moral weight challenges** — make a certain number of choices in the "morally difficult" category without using any resolution mechanic that would make them easier

---

## 4.4 — Companion Perks: One Per Companion

**Priority: Medium. Blocked until companion questlines are finalized (Phase 3 + Phase 5).**

Eight companions. One passive perk per companion (active while companion is present). One "questline complete" perk per companion (earned by finishing their personal arc).

The companion passive perk should express who the companion is — not a generic combat bonus, but something that could only come from being around this specific person. Favi della Torre's perk should feel like Favi della Torre.

The questline perk should reflect what changed — what the companion resolved about themselves, and how that resolution changes what the player can do or be in the world.

Design these once the companion personalities and questlines are both settled (Phase 3 for personality, Phase 5 for questline specifics).

---

## Phase 4 Output Checklist

**File creation:**
- [ ] `Companion_Perks.md` file created with framework
- [ ] `Quest_and_Choice_Perks.md` file created with framework
- [ ] `Skill_Milestone_Perks.md` file created with framework
- [ ] `World_and_Discovery_Perks.md` file created with framework
- [ ] Doll/Idolization perks: audited and completed

**Level-up perks:**
- [ ] Might perks (after Phase 1 Might finalization)
- [ ] Nerve perks (after Phase 1 Nerve finalization)
- [ ] Agility perks: gaps filled
- [ ] Calculation perks: gaps filled
- [ ] Humanity perks: gaps filled
- [ ] Investigation perks: gaps filled
- [ ] Engine perks: gaps filled
- [ ] Total level-up perks: 160/160

**Earned perk categories:**
- [ ] Challenge perks: target count reached (~100-150)
- [ ] Companion perks: all 8 companions have passive + questline perk (after Phase 5)
- [ ] Quest/choice perks: all major choices covered
- [ ] Skill milestone perks: all 44 skills have milestone effects
- [ ] World/discovery perks: all major exploration rewards designed

**When all items are checked: perk system is complete.**
