# FNV Perk Cross-Reference Audit

**What this is:** a working review document, not a design decision — created 2026-07-26 after the developer
pointed out that only 7 perks had been pulled from `to-be-integrated/Fallout_New_Vegas_-_perks_full-list.txt`
despite it being a genuinely complete list (~109 named perks across all levels). This is the real full pass:
every perk in that source file, sorted by what it needs before (or whether it can) become an Inner Tepenia
perk. Nothing below is written into `Regular_Perks_-_Level-Up.md` yet — this is the sorting stage.

**22 perks already ported/adapted, for reference** (not repeated below): Educated, Swift Learner,
Comprehension, Tag!, Computer Whiz, Infiltrator, Scavenger (merges Fortune Finder + Scrounger), Strong Back,
Pack Rat, Stonewall, Toughness, Life Giver, Nerves of Steel (reworked), Perimeter Awareness (from Alertness),
Math Wrath, Sniper, Concentrated Fire, Better Criticals, Robotics Expert, Silent Running, Quick Draw
(reworked), Ninja. Also conceptually covered without a direct port: **Grim Reaper's Sprint** (VATS-kill AP
refund) already exists as the independently-designed **Grim Reaper Protocols**; **Burden to Bear** (+50 carry
weight) is redundant with the already-ported **Strong Back**, same effect.

---

## Clean Candidates — All Resolved 2026-07-26

Every perk that was in this bucket has now been sorted: 29 written into `Regular_Perks_-_Level-Up.md`'s base
160 (Heave Ho!, Friend of the Night, Light Touch, Old World Gourmet, Travel Light, Bloody Mess, Ferocious
Loyalty, Mad Bomber, Living Anatomy, Super Slam!, Terrifying Presence, Here and Now, Finesse, Mister Sandman,
Nerd Rage!, Fast Metabolism, Heavyweight, Hobbler, Hit the Deck, Piercing Strike, Splash Damage, Center of
Mass, Light Step, Action Girl, Meltdown, Weapon Handling, Paralyzing Palm, Them's Good Eatin', Broad
Daylight), 5 moved to "DLC-Scoped Candidates" below (Demolition Expert, Gunslinger, Hand Loader, Commando,
Tunnel Runner), and 2 moved to "Flagged for Further Exploration" below (Walker Instinct, Certified Tech) —
plus the sexuality quartet, Rapid Reload, Plasma Spaz, and Laser Commander, all already written in during the
prior pass. See `Regular_Perks_-_Level-Up.md` for the actual written entries; nothing further needed here.

---

## Resolved and Written In (formerly "Still Pending a Sub-Decision")

| Perk | Real FNV Requirement | Real FNV Effect | Resolution |
|---|---|---|---|
| **Junk Rounds** *(resolved and written into `Regular_Perks_-_Level-Up.md`, 2026-07-26; its former pair, Miss Fortune, was dropped entirely)* | Luck 6, Repair 45 | Craft ammunition from scrap metal and tin cans | Luck → Investigation (Engine was ruled out — it's the recovery-speed/AP-replenishment stat, not a resourcefulness stat). Final: I 6, Repair 45. |
| **Vigilant Recycler** *(resolved and written into `Regular_Perks_-_Level-Up.md`, 2026-07-26)* | Science 70 | 2x energy ammo recovery, better recycling recipes | Retargeted away from all three Science-descendant skills entirely — developer's call: field-survivalist skills (Repair, Outdoorsman) fit "recycling" better than a lab-science skill. Final: Repair 50 OR Outdoorsman 70. |

---

## DLC-Scoped Candidates (real perks, but belong to a specific DLC rather than the base 160)

| Perk(s) | DLC | Why |
|---|---|---|
| **Hunter**, **Entomologist**, **Animal Friend**, **Tribal Wisdom** *(assigned 2026-07-26)* | **Mirny DLC (DLC 7)** | Confirmed: wildlife/huntable-creature content belongs specifically here, tied to Davis's near-idyllic setting — as close to a breadbasket/agricultural identity as Antarctica allows, per Davis's already-established "breadbasket/research identity" (see `project_davis_course_of_events_regeneration` memory). |
| **Shotgun Surgeon**, **The Professional**, **And Stay Back** *(assigned 2026-07-26, locked to Halley DLC)* | **Halley DLC** | Confirmed: traditional firearms exist only in coastal cities, where there's real cause for concern over an Upper Earth invasion. Halley chosen over Palmer after a lore check: Palmer City is established as a tourism/diplomatic gateway to Upper Earth (casinos, jazz, the Machu Picchu Base visa system), not a militarized culture — it was the *target* of Upper Earth's wartime strikes, not a martial subnet, and Port Lockroy's garrison is explicitly decommissioned into a heritage museum. Halley's Belgrano has genuine, ongoing military civic character instead — founded when a ranking Air Force officer extended military command structure over the entire civilian population, producing a lasting "frontier-proud, almost martial civic bearing" — reinforced by Halley's broader working-class/industrial identity (Troll, Sanay). **Base-game equivalent still open** — the developer confirmed there can be "items-turned-weapons" counterparts; proposed direction is three new perks built on the existing **Improvised Weaponry** perk (a DT-penetration version, a sneak-attack-crit version, a knockback version) rather than reusing the gun-specific names. Not yet drafted. |
| **Demolition Expert**, **Gunslinger**, **Hand Loader**, **Commando** *(assigned 2026-07-26 — specific DLC not yet named)* | DLC-scoped, unspecified | Developer's call: these belong in a DLC rather than the base 160. Which specific DLC wasn't specified — flagged for a later decision. |
| **Tunnel Runner** *(assigned 2026-07-26)* | **Byrd DLC** | Developer's call: Tunnel Runner (sneak-speed bonus) belongs specifically to the Byrd DLC. |

---

## Flagged for Further Exploration (not written in, not DLC-assigned — held for later design work)

| Perk | Real FNV Requirement | Real FNV Effect | Why it's held |
|---|---|---|---|
| **Walker Instinct** *(flagged 2026-07-26)* | Survival 50 | +1 to two stats while outdoors | Developer's call: needs further exploration before writing in, despite no missing-system blocker. |
| **Certified Tech** *(flagged 2026-07-26)* | — | +25% crit vs. robots, high chance of bonus crafting component from destroyed robots | Developer's call: needs further exploration before writing in, despite being a strong thematic fit for a robot-heavy setting. |

---

## Needs a Developer Decision (mapping/subtype question, not a missing system)

| Perk | Real FNV Requirement | Real FNV Effect | The open question |
|---|---|---|---|
| **Unstoppable Force** | Str 7, Melee Weapons 90 | x4 damage through enemy blocks | Whether a "block" defensive mechanic exists for enemies at all — genuinely undecided, worth exploring rather than assumed either way. |
| **Chemist** / **Chem Resistant** *(flagged for future review, 2026-07-26)* | Medicine-gated | Chems/stims last longer; addiction resistance | Depends on whether combat-buff chems and an addiction system are modeled (distinct from Glitch-Coolant, which is more a social/flavor substance). Not resolved now — revisit later. |
| **Implant GRX** *(flagged for future review, 2026-07-26)* | End 8 | Non-addictive subdermal chem injector, 2 ranks | Strong candidate for the "Augmentation/Cybernetics" perk category floated earlier this session — needs that category to exist first, or a chem system to hook into. Not resolved now — revisit later. |

---

## Blocked on a Missing System (not a rejection — genuinely can't build yet)

| Perk(s) | Missing system |
|---|---|
| Rad Child, Lead Belly, Rad Resistance, Atomic!, Irradiated Beauty, Rad Absorption | No radiation mechanic confirmed anywhere in the docs. |
| Night Person, Solar Powered | No day/night cycle confirmed. |
| Home on the Range, Roughin' It | No camping/sleep-for-bonus system confirmed. |
| Long Haul *(already flagged in `TODO.md`)* | No fast-travel system. |
| Adamantium Skeleton, Eye for Eye *(Adamantium Skeleton already flagged in `TODO.md`)* | No limb-specific damage system. |
| **Explorer** *(reclassified 2026-07-26 — corrected: this perk reveals fast-travel locations on the map, not quests/quest-markers; the developer's own correction to my earlier mischaracterization)* | No fast-travel system — same blocker as Long Haul. |

---

## Not Portable As-Is (FNV-specific naming, Karma-based, or real-time-only mechanics)

| Perk(s) | Why |
|---|---|
| Cowboy, Grunt, Sneering Imperialist, Fight the Power!, Purifier, Mile in Their Shoes | All gated on specific FNV weapon lists, factions (NCR/Legion/Brotherhood/tribals/raiders), or named FNV creatures — no clean 1:1 translation, though the underlying *idea* (faction-specific or creature-specific combat bonuses) could seed original Tepenian perks later. |
| Cannibal, Ghastly Scavenger (chained to Cannibal) | Karma-gated; Inner Tepenia has no Karma system, and the `TODO.md` "Tepenian counterpart to Karma/Sanity" item is explicitly still unresolved. |
| Ain't Like That Now, Just Lucky I'm Alive, Thought You Died | The Level 50 Karma-tiered trio — same blocker, though conceptually similar to an IF-meter-tiered or Reputation-Matrix-tiered endgame perk once that system exists. |
| Run 'n Gun | Real-time movement-accuracy mechanic (reduced weapon spread while walking/running) — no clean turn-based translation. |
| Voracious Reader, Retention | Real-time magazine-duration/duplication mechanics that don't fit the no-dice-roll, instant-application skill-book model already established; overlaps with the already-ported Comprehension. |
| Slayer | +30% real-time attack speed — would need the same kind of AP-cost rework Quick Draw already got, not a direct port. |

---

## Flagged Suspect Source-Text Entries (verify before using, don't assume)

- **Mysterious Stranger**'s listed effect ("+50% damage with fire-based weapons") is almost certainly a
  transcription error in the source .txt — that's actually Pyromaniac's real effect. The real Mysterious
  Stranger perk summons an ally NPC who lands a devastating attack in V.A.T.S. **Don't build from the listed
  text without verifying against the actual wiki first**, same lesson as the earlier Math Wrath fabrication
  incident.
- **Robotics Expert** appears twice in the source file (once under "Level 10," once under "Level 12") —
  almost certainly a duplication artifact from however the list was compiled, not two distinct real perks.
  Already ported once; no action needed, just noting the source's own redundancy.

---

## Open Questions

- Which of the "Clean Candidates" should actually get written into `Regular_Perks_-_Level-Up.md` first —
  all of them, or a prioritized subset? The six marked **High priority** above are the ones with the clearest
  existing-system fit and the most obvious current gaps to fill.
- Every "Needs a Developer Decision" item requires an actual call before it can move to the clean-candidate
  bucket — none should be guessed at.
- Whether to eventually build a small Karma/Sanity-analog system (`TODO.md`'s existing open item) partly to
  unlock the perks currently blocked on it (Cannibal, the Level 50 trio).
