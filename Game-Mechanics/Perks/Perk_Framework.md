# Perk Framework — Inner Tepenia

## Design Foundation

Inner Tepenia's perk system is modeled on **Fallout: New Vegas** and inherits its most important structural insight: the perks a player *chooses* at level-up are their build decisions, while the perks they *earn* through play are rewards for how they actually lived in the world. These two pools never compete for the same slot.

The result is a system where two playthroughs of the same character build can feel radically different, because the earned perks collected along the way reflect which quests were done, which companions were romanced or lost, which factions were helped or burned, which enemies were hunted obsessively, and what corners of the world were found.

**Target perk count (base game):**
- Level-up perks available to choose from: **160 distinct perks** (target; 5× the 32 available perk slots, so the player always has far more options than opportunities). Currently at **61/160** (38%) — see `Regular_Perks_-_Level-Up.md`. Remaining ~100 perks are pending design.
- Total earned perks across all categories: **200–300+**
- Grand total: **250–360+ perks** before any DLC

Earned perks should substantially outnumber level-up perks. This is intentional and desirable.

---

## Tier 1: Level-Up Perks

**File:** `Regular_Perks_-_Level-Up.md`

### Rules
- The player earns **one perk slot every 2 levels** — 32 total slots across the base game's 64-level cap.
- At each perk opportunity, the player chooses **one** perk from the available pool.
- Level-up perks require MACHINE stat minimums and/or skill thresholds to unlock.
- Most have **2–3 ranks**; a player may take a rank at each perk opportunity.
- The available pool should be wide enough that no two playthroughs naturally choose the same 32 perks. Target ~50–60 distinct perks in the base game pool.
- DLCs may add additional level-up perks to the pool and raise the perk slot count.

### Design rules
- Every level-up perk must create or reinforce a **specific playstyle**. Generic +5% damage perks are not acceptable.
- Perks should **interact** with the skill, stat, and faction systems — not float above them.
- No level-up perk should be universally optimal. There should always be a tradeoff or a context where it underperforms.
- Ranked perks must show **meaningful progression** between ranks — not just a number increase. Rank 2 should open a new use case or change behavior, not merely improve the Rank 1 effect.
- Prerequisites gate perks to appropriate build stages. Early-available perks (low stat requirements) should be broadly useful but modest. Late-stage perks (high stat + skill requirements) can be powerful and niche.

### Fallout Precedence
FNV perks taken every 2 levels. Inner Tepenia matches this rate exactly.

---

## Tier 2: Earned Perks

Earned perks **do not use level-up perk slots**. They are additive rewards — pure upside — awarded automatically when the player meets specific conditions. The player cannot "spend" an earned perk or choose between them; they simply accumulate.

Earned perks should be numerous, varied, and deeply embedded in the world. A player who completes every district questline, every companion arc, every challenge tier, and finds every hidden location will have meaningfully more earned perks than one who rushes the main story. Neither path is wrong — but the thorough player's character will feel like a different, richer entity.

---

### Category A: Challenge Perks

**File:** `Challenge_Perks_-_Task-Based.md`  
**FNV equivalent:** Challenge perks (Bug Stomper, Camel of the Mojave, etc.)

**Definition:** Awarded automatically when a cumulative, measurable action reaches a threshold. The player may not even be aware they are working toward these — they are discovered rather than pursued.

**Design rules:**
- Always **ranked** (2–3 ranks). The first rank should arrive naturally in a normal playthrough for that type of activity. Later ranks require genuine dedication.
- The unlock condition must be something the game can track reliably: kill counts by enemy type, skill use counts, item counts, distance traveled, failed attempts, days survived, etc.
- The perk effect must be **thematically connected** to the unlock condition. Killing 50 robots should not give a social bonus.
- Do not gate challenge perks on rare or missable events. They should feel like recognition of play patterns, not obscure secrets.
- Many challenge perks will be invisible to the player until earned — they appear in the perk screen with a brief "you have earned this for..." description.

**Target quantity:** ~100–150 challenge perks (across 50–75 distinct challenges, most with 2–3 ranks)

**Challenge perk sub-categories to cover:**
- Combat kills by enemy type (robots, humans, hybrids, Frostlands fauna, etc.)
- Combat style (non-lethal takedowns, NODE kills, melee kills, EMP kills, etc.)
- Skill usage (hacks, repairs, dialogue successes, deceptions, crafting, etc.)
- Exploration (districts visited, Undergrid zones mapped, hidden locations found, etc.)
- Survival (blackouts survived, time spent in extreme cold, total damage taken, etc.)
- Faction interaction (quests completed per faction, betrayals, reputation swings, etc.)
- Economic (total caps spent, items crafted, items sold, etc.)
- Companion-related (hours in combat alongside each companion, times they were downed, etc.)

---

### Category B: Companion Perks

**File:** `Companion_Perks.md` *(to be created)*  
**FNV equivalent:** Companion perks (Scribe Counter, Regular Maintenance, etc.)

**Definition:** Perks earned through time spent with companions, completing their personal quests, or reaching specific relationship milestones.

**Design rules:**
- Two sub-types:
  - **Passive (presence-dependent):** Active only while the companion is in the party. Lost if the companion is dismissed or dies.
  - **Permanent (quest-earned):** Awarded after completing a companion's personal questline or reaching a key relationship milestone. These are kept regardless of companion status.
- Every companion should have a minimum of **3–5 perks total** — a mix of passive and permanent.
- Passive companion perks should reflect the companion's *expertise and personality*, not just be generic buffs. Calethina's passive perks should feel nothing like a Frontier scout companion's passive perks.
- Permanent companion perks should feel like the companion has genuinely *taught the player something* or *changed the player character* — not just unlocked a stat bonus.
- Companions with especially deep questlines (e.g., Calethina) should have more perks and more nuanced unlock conditions.
- Some companion perks may be mutually exclusive with perks from a rival or opposing companion.

**Target quantity:** ~25–40 companion perks across all base game companions

**Per-companion perk structure (minimum):**
| Perk Type | Count | Notes |
|-----------|-------|-------|
| Passive (early) | 1 | Available from first joining |
| Passive (deep) | 1 | Unlocked after a specific milestone or questline stage |
| Permanent (questline) | 1–2 | Earned by completing their personal arc |
| Permanent (choice) | 0–1 | Earned by making a specific choice during their arc |

---

### Category C: Quest and Choice Perks

**File:** `Quest_and_Choice_Perks.md` *(to be created)*  
**FNV equivalent:** Brainless/Heartless/Spineless (Old World Blues), Eureka!/All or Nothing (endgame), etc.

**Definition:** Perks earned by completing quests or making specific significant choices during them. Some are straightforward completion rewards; others are mutually exclusive branches awarded based on which option the player chose.

**Design rules:**
- **Completion perks** are awarded simply for finishing a quest. These are the most common type — treat them as a tangible reward for engagement.
- **Choice perks** are mutually exclusive. The player earns one based on which path they took. These perks should make the choice feel permanently meaningful — something about the player character changed based on what they did.
- Choice perks in the same quest should be **equally valuable but differently useful**. One choice should not be objectively better than the other.
- Some perks may require not just completing a quest but doing so in a specific *way* (under a time limit, without killing anyone, using a specific skill, etc.).
- Main story quest perks should be major and memorable — they represent turning points in the player character's experience of the crisis.
- Side content quest perks can be more niche and flavor-driven.

**Target quantity:** ~50–70 quest and choice perks (main story + side content + faction quests)

**Quest perk sub-categories:**
- Main story branch completions (Acts 1, 2, 3 each contribute)
- District side quest completions
- Faction alliance or betrayal choices
- Major moral decision branch rewards
- Hidden quest completions (secret content rewards)
- "How you did it" awards (pacifist run of a quest, full combat resolution, etc.)

---

### Category D: District Capstone Perks

**File:** `post-Idolization_Questline_Perks.md` *(already exists and is populated)*  
**FNV equivalent:** No direct equivalent — unique to Inner Tepenia's district structure

**Definition:** The highest-tier earned perks in the game, awarded at the conclusion of each district's major capstone questline. Require Idolized reputation with the district and completion of the full questline arc. Always come in mutually exclusive pairs based on the player's final choice in the questline.

**Status:** All 12 districts documented with 2 perks each = **24 capstone perks** already designed.

**Design rules:**
- These are the most powerful earned perks in the game. They should feel like major permanent abilities, not just stat bumps.
- Always mutually exclusive within a district (you made a choice; the district reflects it permanently).
- Cross-district synergies are encouraged — certain capstone perk combinations from different districts should interact in interesting ways.
- Can only be earned once per playthrough; directly linked to major story consequences.

**Target quantity:** 24 (complete — 2 per district × 12 districts). DLCs may add new districts with their own pairs.

---

### Category E: Skill Milestone Perks

**File:** `Skill_Milestone_Perks.md` *(to be created)*  
**FNV equivalent:** Partial equivalent in skill bonuses; most direct equivalent is the "Master Trader" / "Hand Loader" style perks

**Definition:** Awarded automatically when a skill reaches a specific threshold (25, 50, 75, 100). These represent the player character's systems having self-optimized through repeated use — the skill has been used enough that something new has crystallized.

**Design rules:**
- Each major skill should have **2–3 milestone perks** across the 25/50/75/100 range. Not every skill needs all four tiers — some might only have 2.
- Milestone perks should feel like a **qualitative change**, not just a +% bonus. At 75 Arcanet Navigation, something new becomes possible — a new approach, a new reading of the world — not just "hacking is slightly better."
- The 100 milestone perk (true mastery) should be genuinely powerful and rare. Reaching 100 in any skill without significant investment is impossible by design (see Skill_Caps_and_Stat_Synergy.md), so the perk should reflect that rarity.
- Skill milestone perks are invisible until earned — they don't appear as goals in any menu. They are discovered.

**Target quantity:** ~60–80 milestone perks across the 44-skill list (~1.5 average per skill across 2–3 thresholds)

---

### Category F: World and Discovery Perks

**File:** `World_and_Discovery_Perks.md` *(to be created)*  
**FNV equivalent:** Perks from Vault locations, from specific NPCs, from reading certain books/terminals

**Definition:** Perks earned by finding hidden locations, completing non-obvious action sequences, reading full sets of data logs, meeting specific obscure NPCs, or stumbling onto content that isn't signposted.

**Design rules:**
- These are the most hidden perks in the game. No quest marker, no journal entry, no tooltip. The player either finds them through exploration and curiosity, or never knows they existed.
- World perks should feel like the world *rewarded* the player for paying attention. Reading a full archive of pre-war engineering documents should teach the player character something real.
- Some world perks are region-specific (Undergrid-exclusive, Frostlands-exclusive, specific building or ruin).
- Some world perks are NPC-specific — given by a hidden or hard-to-reach character who teaches the player something.
- These perks can be unusual, experimental, or flavorful in ways that more formal perks cannot be. The world perk earned by finding the secret Ossuary archive can be genuinely strange.

**Target quantity:** ~30–50 world and discovery perks

---

### Category G: Idolization and Companion-Arc Perks (Dolls)

**File:** `post-Idolization_Questline_Perks.md` also covers this; may split into dedicated file  
**FNV equivalent:** Companion perks from personal questlines

**Definition:** Perks earned through deep personal relationships with the Doll characters — the in-universe robots based on real-world doll figures. Distinct from general Companion Perks (Category B) in that Doll perks are specifically tied to the Idolization system and the emotional arc of each Doll's questline.

**Design rules:**
- Doll perks should reflect the *specific identity* of that Doll — their skills, their history, their personality.
- The most powerful Doll perks should be earned at the conclusion of their full personal arc, not mid-way through.
- Some Doll perks may only be accessible if certain choices were made earlier in the relationship — they represent trust earned or a shared experience that shaped both characters.
- Calethina, as the central companion, should have the deepest and most extensive perk structure of any Doll.

**Target quantity:** ~20–30 Doll/Idolization perks across all base game Dolls

---

## Perk Design Principles (All Categories)

### The effect must be specific
Vague effects ("combat improved," "dialogue better") are not acceptable. Every perk must describe exactly what changes, under what circumstances, and by how much (even if the "how much" is a described behavior change rather than a number).

### The effect must be thematically coherent
A perk earned by killing 50 robots should make the player character better at something related to fighting robots, not at cooking or diplomacy. The thematic link between unlock condition and effect must be visible and logical.

### No perk should be mandatory
Any playstyle should be viable without any single perk. Perks enhance and specialize; they should never be the sole reason a build works.

### Ranked perks must evolve
Between ranks, the perk should open new behavior, not just improve numbers. Rank 2 of a hacking perk might not just increase hack success rate — it might unlock a new type of hack that wasn't available at Rank 1.

### Some perks should be combinatorial
Design some perks specifically to become exceptional when combined with other specific perks. These reward players who are paying attention to synergies. Do not design perks that are independently strong AND combinatorially broken.

### Mutually exclusive perks must be equally desirable
Any time two perks are mutually exclusive (choice perks, capstone perks), both options must feel genuinely appealing. The loss of the unchosen perk should sting. If one option is obviously better, it was designed wrong.

### Fallout Precedence applies
When designing a perk that covers territory Fallout 1/2 and FNV both cover, the FNV implementation is canonical reference. If FNV doesn't cover it (robot-specific mechanics, Arcanet systems, MACHINE stats), design freely.

---

## File Structure

| File | Category | Status |
|------|----------|--------|
| `Regular_Perks_-_Level-Up.md` | Tier 1: Level-Up | Partial (~10 perks; needs ~40–50 more) |
| `Challenge_Perks_-_Task-Based.md` | Category A: Challenge | Partial (~7 perks; needs ~100+ more) |
| `Companion_Perks.md` | Category B: Companion | Not yet created |
| `Quest_and_Choice_Perks.md` | Category C: Quest/Choice | Not yet created |
| `post-Idolization_Questline_Perks.md` | Category D: District Capstone | Complete (24 perks) |
| `Skill_Milestone_Perks.md` | Category E: Skill Milestone | Not yet created |
| `World_and_Discovery_Perks.md` | Category F: World/Discovery | Not yet created |
| `Special_Unique_Perks.md` | Categories D/G overlap | Partial — review for consolidation |
| `Perks.md` | Overview/summary | Partial — review for consolidation |

---

## Perk Count Targets (Base Game)

| Category | File | Target Count |
|----------|------|-------------|
| Level-Up | `Regular_Perks_-_Level-Up.md` | ~50–60 distinct perks |
| Challenge | `Challenge_Perks_-_Task-Based.md` | ~100–150 (across ~60–75 challenges) |
| Companion | `Companion_Perks.md` | ~25–40 |
| Quest / Choice | `Quest_and_Choice_Perks.md` | ~50–70 |
| District Capstone | `post-Idolization_Questline_Perks.md` | 24 (complete) |
| Skill Milestone | `Skill_Milestone_Perks.md` | ~60–80 |
| World / Discovery | `World_and_Discovery_Perks.md` | ~30–50 |
| Doll / Idolization | *(see companion + capstone files)* | ~20–30 |
| **Total** | | **~360–500+ perks** |

DLCs add to every category. Each DLC should substantially expand earned perk counts, particularly challenge and quest perks tied to the new content.
