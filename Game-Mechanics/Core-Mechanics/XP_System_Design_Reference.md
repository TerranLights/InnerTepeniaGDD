# XP System Design Reference
## Full working record: Fallout: New Vegas baseline research, the pacing problem, and the settled base-game model

**What this is:** a complete capture of the design conversation that produced Inner Tepenia's XP-per-content-type
numbers and the base-game leveling pacing target. `Experience_and_Leveling_System.md` holds the clean,
authoritative rules (two XP channels, level cap, deferred spending); this file holds the *working* material
behind it — the real Fallout: New Vegas numbers used as a baseline, the specific pacing problem that came up,
every idea considered, and the reasoning for what got kept vs. rejected. Referred back to here rather than
re-derived from scratch.

---

## Part 1 — Fallout: New Vegas Baseline (verified real numbers)

### Level-up XP formula

**Cumulative XP required to reach level n = (n − 1) × (75n + 50)**

Reverse-engineered from a saved level-XP chart (`to-be-integrated/Fallout New Vegas - Level-XP Chart.png`,
levels 1-30) and cross-verified against an independently-cited total (186,200 XP to reach level 50 — the
formula produces exactly that value). Confirmed accurate.

Clean statement of the same rule: **the first level-up costs 200 XP; each subsequent level-up costs 150 XP
more than the previous one.**

| Level | Cumulative XP | Level | Cumulative XP |
|---|---|---|---|
| 1 | 0 | 20 | 29,450 |
| 2 | 200 | 25 | 46,200 |
| 3 | 550 | 30 | 66,700 |
| 4 | 1,050 | 35 | 90,950 |
| 5 | 1,700 | 40 | 118,950 |
| 6 | 2,500 | 45 | 150,700 |
| 7 | 3,450 | 50 | 186,200 |
| 8 | 4,550 | 64 | **305,550** |
| 9 | 5,800 | 100 | 747,450 |
| 10 | 7,200 | | |

Level 64 (Inner Tepenia's own base-game cap) and level 100 (full-DLC cap) computed by extending the same
verified formula unchanged, per the operating principle of using real FNV numbers wherever a new value is
needed rather than inventing a separate curve.

The saved chart also included FNV's separate Karma-title system (Samaritan→Messiah / Drifter→True Mortal /
Grifter→Devil per level) — a single-axis good/neutral/evil system, distinct from the Fame/Infamy reputation
system already noted elsewhere in the project. Not used for anything here; flagged in case it's relevant
later.

### Level cap structure

FNV: 30 base, +5 per DLC × 4 DLCs (Dead Money, Honest Hearts, Old World Blues, Lonesome Road) = 50 total.
Inner Tepenia's own structure already mirrors this shape (64 base, +5 per subnet DLC × 6, +6 for DLC 1,
totaling 100) — established prior to this conversation in `Experience_and_Leveling_System.md`.

### Real quest XP examples (confirmed)

- "They Went That-a-Way" (Doc Mitchell) — 1,000 XP
- "Ring-a-Ding-Ding!" (Jessup) — 1,000-1,200 XP
- "The House Always Wins I" — 600 XP
- "I Forgot to Remember to Forget" (Boone's companion quest) — 500 XP

Aggregate pattern: main-quest XP totals roughly **3,000 XP across the early main quests (levels 1-4) up to
~22,000 XP for the late main quests (levels 45-50)**. Side-quest XP runs **75-550 XP per quest**. Quest XP in
real FNV also scales somewhat with the player's current level at completion — the exact scaling formula
wasn't recoverable, but it's a real mechanic, not adopted here (Inner Tepenia's own model already commits to
a flat lump sum per quest, before MACHINE-stat/perk/trait modifiers).

Real design precedent worth noting: FNV mostly **removed per-kill combat XP** (a deliberate Sawyer-era
departure from Fallout 3) — quest completion is almost the entire XP source in real FNV. Consistent with the
direction Inner Tepenia's own model already leans.

### Real Challenges data (verified via saved wiki page)

Source: `to-be-integrated/Fallout_ New Vegas challenges _ Fallout Wiki _ Fandom.html`, extracted directly.

**Base game (no DLC) challenges, across all three categories:**

| Category | Count | Total XP |
|---|---|---|
| Damage challenges | 31 | 1,900 |
| Kill challenges | 21 (5 are 3-rank) | 1,864 (all ranks) |
| Other challenges (crafting, gambling, exploration, chems, hacking, etc.) | 49 | 2,525 |
| **Total** | **101** | **6,289** |

This single number was the load-bearing discovery of the whole conversation: **all 101 base-game FNV
challenges combined, every rank included, total only 6,289 XP.** Real FNV's own version of "Activities"
(the user's category: minigames, crafting, exploration milestones, location discovery, Challenges) is
already present in this same "Other" table — Caravan/Blackjack/Roulette/Slots, "Crafty"/"Crafty Veteran"
(crafting), "Walker of the Mojave"/"Master of the Mojave" (location discovery), "Low Tech Hacking," etc. This
confirmed that Activities/Challenges were never meant to be a leveling pathway in FNV — they're a small bonus
layer on top of quest XP, not a load-bearing content pillar.

---

## Part 2 — The Design Problem (chronological)

### The starting anchors (fixed, not revisited)

- District Main Questline: **3,000 XP** flat, one per district (`District_Main_Questlines.md`)
- District Under-Questline: **700 XP** flat, ~9 average per district (`District_Under_Questline_Design_Method.md`)
- Everything else: use real FNV numbers as the baseline

### Problem 1 — First pacing check

12 districts' (excluding Hub) worth of main+under content alone = 111,600 XP → Level 38, ~75% to 39.
13 districts (including Hub) = 120,900 XP → Level 40, ~32% to 41. Both land around 59-63% of the base-game
cap of 64, using *only* district quest content, before the base-game main questline, companions, or activities.

### Problem 2 — The real design goal

Stated goal: a player who completes **all base-game content — every district's main quest, under-questline,
and side-quest content, all companion quests, all activities, everything** — should reach **Level 64** by
the time they've finished roughly **8-9 districts**, not needing all 13. Not a request to change the fixed
3,000/700 anchors — a statement about how much total *content* should exist.

This required identifying every other XP source the model was missing:
- A genuine **third district-level tier**, "side-quest," smaller than Under-Questline (confirmed by the
  developer as real, not a synonym) — plus a separate, later-flagged possibility of true non-district-bound
  side-content (not yet designed for, may or may not be added).
- **Companion quests** — confirmed target: at least 30 companions in the base game (no DLC), "so there's a
  companion no matter what playstyle." Cross-checked against the actual roster:
  `Worldspace/Characters/Dolls/Still-Present_-_In-Game/recruitable/` has 44 folders total, some already
  DLC-reserved (e.g., Kendra Heinrich is DLC 1) — 44 minus DLC reservations comfortably clears 30.
- **Activities** — defined by the developer as minigames, crafting, exploration milestones, location
  discovery, and Challenges (explicitly citing real FNV examples: "A Fistful of Hollars," "I am not
  Left-Handed," "Day Tripper," "Stimpaddict," "Up to the Challenge" — all confirmed present in the extracted
  data above).
- **The base game's own single, overarching main questline** — distinct from any district's own main
  questline, not counted anywhere until this point in the conversation. Developer had no target number in
  mind; used the real FNV main-quest total (~25,000 XP) as a placeholder, later revised upward (see below).

### Problem 3 — The volume problem

With companions at a first-pass 500 XP average (real FNV Boone precedent) and Activities at the real,
verified 6,289 XP total, the remaining gap for the new "side-quest" tier came out to **~175,000-185,000 XP**
(depending on 8 vs. 9 districts). At FNV's real side-quest range (~75-550, call it ~300 average), that's
roughly **580-620 individual minor side-quests** — far beyond FNV's own total side-quest count, and not
realistic to hand-author solo.

**Radiant (procedurally reskinned) quests were proposed as one fix and explicitly rejected** — "it just
feels lazy from a development perspective, and the player will catch on." **Repeatable quests (fixed,
hand-authored, but completable multiple times) were accepted instead** as the right way to close a large XP
gap without either an unrealistic bespoke-quest count or a procedural-feeling shortcut.

### Problem 4 — Closing the gap: three levers, applied together

Per explicit instruction, all three adjustment levers were applied simultaneously:

| Lever | Original | Final |
|---|---|---|
| District target | 8-9 | **10** |
| Companion quest average | 500 (FNV precedent) | **1,500** |
| Base-game main questline | 25,000 (FNV placeholder) | **65,000** |

---

## Part 3 — The Settled Model

| XP Source | Value | Notes |
|---|---|---|
| District Main Questline | 3,000 XP flat | 1 per district; narrowed from multiple generated candidates per `District_Main_Questlines.md`'s own production workflow |
| District Under-Questline | 700 XP flat | ~9 average per district (floor 5, target 15-20); every valid candidate kept, no narrowing |
| Companion Quest | ~1,500 XP average (draft) | ≥30 companions targeted, base game only (no DLC) |
| Activities (minigames/crafting/exploration/location discovery/Challenges) | ~6,289 XP total (FNV-precedented scale) | Modeled on real FNV's 101 base-game challenges; deliberately NOT a major leveling pathway |
| Base-game Main Questline (Concordia-wide) | 65,000 XP (draft) | Distinct from any district's own main questline; well above FNV's real ~25,000 total, weighted up on purpose |
| Repeatable Quest Types | 40+ distinct types, ~75-150 XP/completion, ~16-32 repeats average | Fills the remaining gap; see brainstormed list below |
| **Design/pacing goal** | **Level 64 reached via ~10 of 13 districts' worth of full content** | Player need not touch all 13 districts to hit the base-game cap |

### The final math (10-district scenario)

| Source | XP |
|---|---|
| District main+under (10 × 9,300) | 93,000 |
| Companions (30 × 1,500) | 45,000 |
| Activities (real FNV-precedented total) | 6,289 |
| Base-game main questline | 65,000 |
| **Subtotal** | **209,289** |
| **Remaining for repeatable quests** | **~96,261** |
| **Level 64 target** | **305,550** |

96,261 XP ÷ (~75-150 XP per completion) ≈ 640-1,280 total completions needed — covered by **40+ distinct
repeatable quest types**, each completed roughly 16-32 times on average, rather than hundreds of unique
bespoke quests or procedurally-varied radiant content.

---

## Part 4 — Repeatable Quest Type Brainstorm (40 starting concepts)

Organized by mechanic/hook rather than by district, since these are meant to mostly cut across the whole
city. Starting menu to pick from, cut, and remix — not finalized.

**Courier / delivery**
1. Fixed merchant needs specific goods run between two named locations, same route each time
2. Diplomatic courier — sealed messages between two fixed Government District offices
3. Salvage runs — a fixed contact needs specific components retrieved from a named ruin/wreck
4. Black-market fence runs (Pisces) — move specific goods through the same contact repeatedly

**Crafting / commission**
5. A named artisan repeatedly commissions a specific crafted item (same recipe each time)
6. Doll cosmetic/functional upgrade commissions from a fixed customizer
7. Repair contracts — Virgo maintenance workers need the same category of infrastructure repair
8. Energy grid calibration tasks from a fixed Aries engineer

**Combat / training**
9. Sparring circuit — a fixed training hall, scripted opponents, repeatable for XP
10. Underground fight club bouts (Pisces) — fixed recurring matches
11. Companion sparring/training sessions (distinct from their personal questline)
12. Supply-shipment security/escort runs, same route, recurring threat profile

**Information / verification**
13. Gemini Truth Markets — buy a low-reliability rumor, verify it, resell at a markup
14. Broadcast-accuracy verification jobs for the Verification Faction
15. Archive retrieval/organizing tasks (Scorpio's Archive, Libra's Treaty Vaults)

**Maintenance / upkeep**
16. Robot diagnostic/maintenance checkups from a fixed mechanic
17. Terminal hacking / lock bypass commissions for legitimate retrieval jobs
18. Structural inspection jobs tied to a fixed Undergrid inspector
19. Merit-board audits from a fixed Capricorn inspector

**Social / diplomatic**
20. Mediate minor citizen disputes for a fixed Government District petitioner clerk
21. Petition-filing assistance (paperwork errands) in the Government District
22. Speech/negotiation practice trials with a recurring NPC

**Care / community**
23. Resource donation drives — Cancer's Sanctuary, recurring supply needs
24. Mother's Circuit intake-data processing (fixed task, recurring)
25. Bond registry backlog assistance (Taurus)
26. Coolant/medical supply donation runs

**Exploration / frontier**
27. Explorer Guild survey jobs — collect data from marked Frostlands points
28. Explorer Guild rank trials — fixed trial repeated to build standing
29. Memory Keeper story-collection rounds (fixed roster of elders)

**Faction / reputation**
30. Small recurring errands from any faction rep to build standing over time
31. Bounty-board contracts against a fixed roster of recurring threat types
32. Debt collection/enforcement jobs for Pisces' Operators

**Culture / performance**
33. Performance understudy gigs — Leo's director needs a recurring stand-in
34. Cymaticist resonance-tuning tasks (small, recurring)
35. Research-assistant sample/data fetches for a minor Aquarius lab (not the Living Network)

**Misc systemic**
36. Vermin/hazard clearing at fixed recurring incursion points
37. Companion small-errand requests (distinct from personal questlines)
38. Fixed gambling matches against named NPC opponents, if a Tepenia equivalent minigame exists
39. Pest/security sweep contracts for a fixed district administrator
40. Recurring supply-run contracts between two fixed districts' own institutions

---

## Part 5 — DLC Main Questline XP (established 2026-07-22)

- Each of the 6 subnet DLCs' own main questline: **70,000 XP** flat.
- DLC 1, "Echoes of Amundsen" (Kendra Heinrich, South Pole): **200,000 XP** flat —
  deliberately far above the standard DLC rate, since this DLC is designed to be
  brutally unforgiving; completing it earns an outsized reward.

**A pacing consequence, confirmed intentional (developer, 2026-07-22):** base game
complete (Level 64, 305,550 XP) + all 7 DLC main questlines (6 × 70,000 + 200,000
= 620,000 XP) = **925,550 XP** — already **178,100 XP more** than the 747,450
required for Level 100. A player who fully completes the base game and then does
*only* the seven DLC main questlines (no DLC side content, no DLC-native
companions, no DLC activities) already overshoots the absolute level cap.

**This is a deliberate, standing design law, not a bug to fix:** the developer
explicitly confirmed this slack is wanted — "I want players to be able to reach
max level without grinding through absolutely every single thing in the entire
game. I want Inner Tepenia to be fun and not a grindy homework assignment."
Mirrors the base game's own design goal exactly (Level 64 reachable via ~10 of 13
districts, not full completion). Any surplus at Level 100 with all DLCs owned
simply has nowhere to bank to (per the XP Banking rule above), same as reaching
max level in real FNV — that's expected, not a shortfall to correct. **Future XP
numbers for anything in this system should preserve this slack, not tighten it
away.**

---

## Open Questions / Still TBD

- Exact per-companion XP values (currently a flat 1,500 average target, not itemized per companion)
- Final selection and full write-up of repeatable quest types (40 draft concepts above, not yet finalized
  or distributed to specific NPCs/locations)
- Whether true non-district-bound side-content (not tied to any district, closer to Witcher 3's "Frying
  Pan" tier per the earlier Novac-calibration conversation) will actually be added — flagged as a
  possibility by the developer, not decided
- MACHINE stat / perk / trait modifiers on top of these lump sums (still TBD per `Experience_and_Leveling_System.md`'s own original open questions)
- Exact skill-use XP amounts (Channel 2 — lockpicking, hacking, etc.) — not addressed in this conversation
- Whether the repeatable-quest repeat cap (16-32 per type) should vary by type, or be roughly uniform
- DLC-level side content XP (DLC-native companions, DLC under-questlines/side-quests, DLC activities) —
  only each DLC's own main questline has been valued so far (Part 5); everything else within a DLC is
  still unpriced
