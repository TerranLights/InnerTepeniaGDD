# Phase 1 — Foundations

**Prerequisite:** Blocking decisions resolved (see `02-Blocking-Decisions.md`).

**What this phase does:** Establishes the shared vocabulary and settled systems that every subsequent phase depends on. Everything in Phase 2 and beyond will reference the outputs of Phase 1. Work on later phases before Phase 1 is complete creates the same problem as designing quests for an undesigned faction — you're writing against a specification that doesn't exist yet.

**Estimated scope:** Medium. Most of these are decisions and targeted writing, not full document creation.

---

## 1.1 — Finalize Might and Nerve

**Priority: High. Blocks: Perk design (Phase 4); build documentation.**

Both stats are marked TENTATIVE. They have expanded-systems design documents (`Might_Expanded_Systems_Tentative.md`, `Nerve_Expanded_Systems_Tentative.md`) but are not finalized.

### What needs to happen

Read both documents. Make a pass at each with the following questions:
1. Is there mechanical overlap between these two stats and any of the five confirmed stats (Agility, Calculation, Humanity, Investigation, Engine)? If yes, resolve the overlap or differentiate more clearly.
2. Does each stat have a clearly defined role in combat, in dialogue, and in exploration? (The confirmed stats all do.)
3. Are the stat's downstream effects (skill bonuses, perk prerequisites, build archetypes) compatible with the 35 Minmax Build combinations already documented?

If both stats hold up under these questions, remove the TENTATIVE flag. If either needs redesign, do the redesign before removing the flag.

### Design reference
F1/2's SPECIAL stats all have clear roles in three registers: combat (Strength = melee damage, carry weight; Agility = AP), dialogue (Charisma = NPC reactions, companion count; Intelligence = dialogue complexity, quest availability), and exploration (Perception = random encounter detection, item find; Endurance = HP, environmental resistance). MACHINE stats should pass the same three-register test.

---

## 1.2 — Establish 7 District Proper Names

**Priority: High. Blocks: In-game text; any immersion document; district NPC dialogue references.**

Seven districts currently have placeholder zodiac names as their only designation — Cancer, Taurus, Leo, Scorpio, Aries, Capricorn, Libra. The other six districts have proper in-world names (Aquarius's actual name, the Hub, etc.). The zodiac codes are the GDD's shorthand; the in-world signage name is what residents and NPCs actually call the district.

### What needs to happen

For each of the seven unnamed districts, establish:
1. The formal district name (on official signage)
2. The informal name (what residents actually say)
3. Whether the zodiac code survives in-world in any form (as a historical designation, a slang term, a political marker)

The naming should be internally consistent with the world's history: post-Long Night War naming conventions, the political and cultural identity of each district, and the way district names have been used as shorthand elsewhere in the GDD.

### Approach

These names don't need to be designed all at once. Work district by district. Start with the districts most referenced in completed story documents (Cancer and Scorpio appear most frequently in Act 2; Taurus and Leo are major in companion backstories). That leaves Aries, Capricorn, and Libra as lower urgency.

---

## 1.3 — Resolve District Informal Name Conflicts

**Priority: High (blocking). Blocks: Story document editing; any NPC dialogue that uses place references.**

`Act2_Story_Progression.md` uses informal district names that conflict with names used in other documents. Until this is resolved, any editor writing new NPC dialogue that references a district runs the risk of using the wrong name.

### What needs to happen

Read `Act2_Story_Progression.md` against `District_Canon_Reference.md` (or equivalent canonical reference document). Make a list of every informal name in the story document. For any that conflict with the district canon reference, decide which version is canonical and update the non-canonical document.

Document the canonical informal names in a single reference file so future documents have one source of truth. Add a note to that file that it supersedes any conflicting usage elsewhere.

---

## 1.4 — Resolve the Robot Religion Naming Conflict

**Priority: High. Blocks: Phase 2 (robot religion design).**

There is an unresolved naming issue with the five robot religions. Specifically, the religion currently using the placeholder "Cymatics reverence" uses the same name as a faction that exists in a different document — the "Cymaticists" appear as both a religion and as a referenced faction (with overlap with the Chorus of the Deep faction concept). Before the religion can be designed, it needs a definitive in-world name that doesn't create a false identity with the faction.

### What needs to happen

1. Determine whether the Cymaticists are a religion, a faction, or both (a faction whose identity is built around a religion, like real-world religious orders).
2. If both: establish the religion's proper name first, then establish the faction as "the Cymaticist faction" as a secondary designation.
3. If separate: give the religion its proper in-world name (currently just "Cymatics reverence" as placeholder) and keep the faction as the Cymaticists.

The Chorus of the Deep (faction concept) explicitly overlaps with the Cymaticists — it describes "geothermal engineers with a spiritual bent (strong overlap with Cymaticists)." Whether the Chorus of the Deep is a subgroup of the Cymaticists, an independent faction, or a merged design is also a decision this task needs to resolve.

---

## 1.5 — Establish the Janbogo Subnet Nexus Canon

**Priority: Medium. Blocks: Any Janbogo quest content; faction story beats in Janbogo.**

Three narrative integration options for the Janbogo Subnet Nexus have been proposed, none canonized. This is a world-building decision with significant downstream effects on the Veilkeepers faction (which is based in Janbogo) and on any quests set in Janbogo.

### What needs to happen

Review the three proposed options. Make a decision. Document the canonical version in the Janbogo world-building file. Flag the Veilkeepers faction document (Phase 2) to be consistent with it.

---

## Phase 1 Output Checklist

By the end of Phase 1, the following should all be resolved:

- [ ] Might stat: TENTATIVE flag removed (or redesign completed)
- [ ] Nerve stat: TENTATIVE flag removed (or redesign completed)
- [ ] 7 district proper names established (formal + informal)
- [ ] District informal name conflict resolved; canonical reference document created
- [ ] Robot religion / Cymaticist naming conflict resolved
- [ ] Chorus of the Deep relationship to Cymaticists determined
- [ ] Janbogo Subnet Nexus narrative integration canonized

**When all items are checked: proceed to Phase 2.**
