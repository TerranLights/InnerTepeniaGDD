# Perk Framework — Inner Tepenia

**Marked for future review (2026-07-04):** every specific perk designed so far, in every category and every file this document points to, is provisional — see the same note at the top of `Regular_Perks_-_Level-Up.md`. Filling out the target counts below is not the same as locking in the perks already written; expect adjustment as more get added and as actual design & development work begins.

## Design Foundation

Inner Tepenia's perk system is modeled on **Fallout: New Vegas** and inherits its most important structural insight: the perks a player *chooses* at level-up are their build decisions, while the perks they *earn* through play are rewards for how they actually lived in the world. These two pools never compete for the same slot.

The result is a system where two playthroughs of the same character build can feel radically different, because the earned perks collected along the way reflect which quests were done, which companions were romanced or lost, which factions were helped or burned, which enemies were hunted obsessively, and what corners of the world were found.

**Target perk count (base game):**
- Level-up perks available to choose from: **160 distinct perks** (target; 5× the 32 available perk slots, so the player always has far more options than opportunities). Currently at **76/160** (48%) as of 2026-07-04 — see `Regular_Perks_-_Level-Up.md`. Remaining ~84 perks are pending design.
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
| Permanent (choice) | 0–1 | See "Dual-Outcome Companion Perks" below — this is not optional, it's the standard resolution mechanic for every companion's personal questline |

---

### Dual-Outcome Companion Perks — Universal Structure *(established 2026-07-03)*

**Binding design law, applies to every recruitable companion in the base game
and every DLC, with no exceptions.** Modeled directly on Fallout: New Vegas's
companion quest resolutions — most concretely, Cass's personal quest ending in
either the **Hand of Vengeance** or **Calm Heart** perk depending on how the
player handles the situation behind her caravans disappearing.

**The structure, two tiers:**

1. **The companion's own perk branches.** Every companion's personal questline
   resolves into one of (at minimum) **two mutually exclusive companion
   perks** — not a single fixed outcome. Which one they receive depends on how
   the player approached the resolution: the choices made, the influence
   exerted, the path taken. This replaces the "Permanent (choice), 0–1" line
   above — it is not an optional bonus perk, it's the standard shape every
   companion's questline resolution should take.
2. **The player's perk is derived from the companion's outcome.** This is the
   layer beyond the FNV precedent: whichever of the mutually exclusive
   companion perks a companion ends up with **determines which of a
   corresponding pair of player perks the player themselves receives.** The
   player perk is not chosen independently — it's downstream of which
   companion-perk branch got triggered. Player Perk A pairs with Companion
   Perk A; Player Perk B pairs with Companion Perk B. The player cannot get
   Companion Perk A's outcome and Player Perk B — the two tiers are locked
   together per branch.

**Why this matters design-wise:** it means every companion's resolution
produces a *coherent pair* — a psychological/narrative outcome for the
companion, and a mechanical outcome for the player that reflects and reinforces
that same choice, rather than the player perk being an arbitrary, disconnected
reward bolted onto the story beat.

**Scope:** this applies to all base-game companions and all DLC companions,
including Kendra Heinrich (DLC 1) — see
`Kendra Heinrich/DLC_South_Pole_Level_Design.md` for how this maps onto her
specific end-of-DLC decision points (the Arcanet/hardware handling, the
evacuation dead, and possibly others), each of which is a candidate branching
point for her dual-outcome companion perk.

### No Good Endings — Every Branch Carries a Real Trade-Off *(established 2026-07-03)*

**Binding design law, applies to every branch of every companion questline,
with no exceptions.** No branch of any companion's dual-outcome (or
three/four/five-way) resolution is allowed to be a clean "good ending." Every
single branch — regardless of which perk it produces — must carry a genuine
negative trade-off alongside whatever it gains. The player should never be able
to identify one branch as simply "the right choice with no downside."

**Model: Fallout: New Vegas's "For Auld Lang Syne" (Arcade Gannon).** Convince
him to fight at Hoover Dam, and he can't tend to the sick and injured at the
Mormon Fort — he's left wondering if he abandoned the people who needed him.
Convince him to stay at Freeside, and the Enclave Remnants go into the Second
Battle of Hoover Dam one person short. Neither path is a win. Both cost
something real. This is the template for every companion resolution in Inner
Tepenia.

**What this means in practice:** when designing (or, during worldbuilding
sessions, drafting placeholder ideas for) any companion's branch structure,
each branch needs its trade-off made explicit alongside its gain — not left
implicit or glossed over because the branch "sounds positive." A branch that
currently reads as pure triumph, pure closure, or pure moral clarity is
incomplete and needs a real cost added before it's considered done, even at the
placeholder/brainstorming stage.

**Retroactive correction (completed 2026-07-03):** Kendra's "Restore &
Broadcast" and Vosora's "Publication" branches (both drafted before this
principle was established) were framed too cleanly positive — vindication/
closure with no attached cost. Both have since been corrected; see
`Kendra Heinrich/DLC_South_Pole_Level_Design.md` section 8 and
`Vosora Lashár Tanslock/README.md` Design Notes for the corrected text.

### Companion-Mediated Access — Each Branch Unlocks Exclusive Content Through the Companion *(established 2026-07-03)*

**Binding design law, applies to every companion questline branch, stacking on
top of the perk pair and the No Good Endings trade-off — this is a third,
additive layer, not a replacement for either.** Each branch of a companion's
questline resolution grants **the companion** (not the player directly) access
to something new — a location, a building, a faction, a group of people. That
access is what actually opens the door for the player: new things to do, and
new in-world lore to learn, mediated entirely through that companion having
that specific relationship or standing. **This content is exclusive to that
specific branch** — a different branch resolution unlocks different exclusive
content, not the same content through a different door. There is no equivalent
mechanic in Fallout: New Vegas; this is an Inner Tepenia-original addition.

**Illustrative example, using Cass's real companion quest "Heartache by the
Number":** the choice itself — destroy the Crimson Caravan Company and the
Van Graffs, or submit evidence against them to the NCR — is the actual quest
resolution in Fallout: New Vegas. **What's invented here is only the
subsequent companion-mediated-access consequences below**, illustrating what
this Inner Tepenia mechanic would look like layered on top of that real
choice:
- **Destroy CCC/Van Graffs:** Cass gains control of both businesses — the
  player gets access, through her, to high-quality Van Graffs energy weapons
  at a steep discount and new Crimson Caravan supply routes to nearby
  factions (Freeside, the Kings). Trade-off: NCR retailers refuse to deal
  with the player, now seen as dangerous.
- **Submit evidence to the NCR:** the NCR strengthens its position with
  leverage over both companies. Trade-off: the player is marked *persona non
  grata* by the CCC, the Van Graffs, and everyone commercially connected to
  them — refused sales, possible hostility.

Neither branch is a clean win (per No Good Endings), and each opens a
**different, mutually exclusive door** to activities and lore that the other
branch's path never provides at all.

**Why this matters:** it means a companion's questline resolution reshapes the
player's actual reach into the world — not just their stat sheet — and it
gives real, permanent weight to which branch was chosen beyond the perk itself.
It also reinforces replayability: seeing the content locked behind a different
companion branch is a genuine reason to play through a questline again
differently.

**Status:** not yet applied to Kendra's or Vosora's drafted branches in detail
— this principle was established after their perk pairs were drafted. Sketching
what each branch's companion-mediated access might look like is future work,
explicitly marked for the same review-at-design-time treatment as everything
else in this document.

**Branch count policy — 2 floor, 3 goal, 4 permitted, 5 hard cap *(established
2026-07-03, refined same day):*** the FNV baseline is always exactly 2 outcomes
(Hand of Vengeance / Calm Heart). Inner Tepenia's policy:

- **Two is the floor**, not the target — every companion questline resolves
  into *at least* two mutually exclusive outcomes.
- **Three is the goal.** When actual design & development work reaches each
  companion's questline, the default question should be "can this competently
  support three mutually exclusive outcomes instead of two?" (see the Kendra
  Arcanet/hardware branch: Restore & Broadcast / Recover & Control / Let It Go
  — three genuinely distinct choices, not a padded middle option).
- **Four is permitted** when the specific companion, questline, and situation
  genuinely support four distinct, coherent, mutually exclusive outcomes — not
  a default to reach for, but not off-limits either. See Vosora Lashár
  Tanslock's "What the Silence Says" as the working four-branch example
  (Publication / Leverage / The Shape of the Gap / The Wrong Answer — her own
  pre-existing questline design already supported all four cleanly).
- **Five is the hard cap.** No companion questline should ever resolve into
  more than five mutually exclusive outcomes, regardless of how much the
  material seems to support it. An upper limit exists on purpose — there is a
  practical ceiling on scope, playtesting, and how many genuinely distinct
  paths a single questline resolution can coherently support before the
  branches stop being meaningfully different from each other.
- Where a questline's situation doesn't naturally support a third (or fourth,
  or fifth) coherent branch, don't force one — a weak or redundant extra
  option is worse than a clean, smaller set. This is always a per-companion,
  per-questline judgment call made during actual design work, never a blanket
  mandate to hit the maximum.

**All specific perk names, exact branch counts, and outcome designs proposed
during worldbuilding sessions (including the Kendra and Vosora examples in this
document) are explicitly marked for review once actual design & development
work begins, and may be adjusted at that point.** Nothing here is locked in
ahead of that pass.

**Other open questions:**
- Exact naming/design of each companion's perk pair (or triad) — per-character
  design work
- Exact naming/design of each corresponding player perk pair (or triad) —
  per-character design work, likely done in the same pass as the companion
  perk branch

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

**File:** `World_and_Discovery_Perks.md` *(created 2026-07-25 — 1 entry, "Derelict's Eye")*  
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
| `Regular_Perks_-_Level-Up.md` | Tier 1: Level-Up | Partial (76 designed; ~84 more needed to reach 160 target) |
| `Challenge_Perks_-_Task-Based.md` | Category A: Challenge | Partial (~7 perks; needs ~100+ more) |
| `Companion_Perks.md` | Category B: Companion | Not yet created |
| `Quest_and_Choice_Perks.md` | Category C: Quest/Choice | 6/~50-70 designed (Faith & Belief sub-category) |
| `post-Idolization_Questline_Perks.md` | Category D: District Capstone | Complete (24 perks) |
| `Skill_Milestone_Perks.md` | Category E: Skill Milestone | Not yet created |
| `World_and_Discovery_Perks.md` | Category F: World/Discovery | 1/~30-50 designed |
| `Special_Unique_Perks.md` | Categories D/G overlap | Partial — review for consolidation |
| `Perks.md` | Overview/summary | Partial — review for consolidation |

---

## Perk Count Targets (Base Game)

| Category | File | Target Count |
|----------|------|-------------|
| Level-Up | `Regular_Perks_-_Level-Up.md` | 160 target; 76 currently designed |
| Challenge | `Challenge_Perks_-_Task-Based.md` | ~100–150 (across ~60–75 challenges) |
| Companion | `Companion_Perks.md` | ~25–40 |
| Quest / Choice | `Quest_and_Choice_Perks.md` | ~50–70 |
| District Capstone | `post-Idolization_Questline_Perks.md` | 24 (complete) |
| Skill Milestone | `Skill_Milestone_Perks.md` | ~60–80 |
| World / Discovery | `World_and_Discovery_Perks.md` | ~30–50 |
| Doll / Idolization | *(see companion + capstone files)* | ~20–30 |
| **Total** | | **~360–500+ perks** |

DLCs add to every category. Each DLC should substantially expand earned perk counts, particularly challenge and quest perks tied to the new content.
