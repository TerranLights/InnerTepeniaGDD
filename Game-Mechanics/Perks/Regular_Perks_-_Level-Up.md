# Regular Perks (Level-Up)

**Marked for future review (2026-07-04):** every perk in this file — old and newly added alike — is provisional. Progress toward the 260-perk target *(raised 2026-07-26 from 160)* doesn't mean any individual perk is locked in; names, stat/skill requirements, rank structures, and effects are all subject to adjustment once actual design & development reaches this system, and adding more perks later may prompt revisiting ones already here (for balance, overlap, or thematic fit). Treat this whole file as a working draft, not final content.

One perk slot earned every **2 levels** — **32 total slots** across the base game (level cap: 64). **DLCs raise the cap** *(established 2026-07-03)*: each of the 6 subnet DLCs adds +5 levels (2.5 perk slots' worth on its own — see note below), and the South Pole DLC (DLC 1, Kendra Heinrich) adds +6 levels (3 perk slots). Base game + all 7 DLCs = level cap 100 = **50 total perk slots** — a clean number against the ~160-perk target roster (see `Perks.md`/`Special_Unique_Perks.md`), landing exactly on a perk-cadence boundary rather than 1 level short.

*Note on partial-DLC ownership:* since each subnet DLC adds an odd number of levels (+5), owning an odd count of subnet DLCs (1, 3, or 5 of the 6) leaves the level cap on an odd number — one level short of a full perk cycle at that specific point. Owning an even count of subnet DLCs (0, 2, 4, or 6), or the South Pole DLC alone or in any combination, always lands on an even cap. **Largely mitigated by release order** *(established 2026-07-03, see `DLC_Overview.md`)*: the South Pole DLC (DLC 1) is planned to release *last*, after all 6 subnet DLCs — so a player following release order has all 6 subnet DLCs (even, no parity issue) before Kendra's DLC ever becomes available. Only an issue for a player who deliberately skips subnet DLCs.

At each opportunity the player chooses **one** perk from the available pool. Most perks have 2–3 ranks; a rank counts as one perk choice.

**Target pool size: 260 distinct perks** *(raised 2026-07-26 by developer request — +100 beyond the original 160, keeping the same 67%/33% non-combat/combat ratio. The original 160 was a clean 5× the 32 available slots; 260 is a deliberate stretch beyond that derivation, not a recalculated slot multiple.)* Currently **143/260 designed** (55%) as of 2026-07-27, after adding Intense Training (Growth/Learning) — see `Character-Creation/Permanent_MACHINE_Stat_Increases.md`. Previously, after the developer's own full pass over the `Skills.md`-restructure batch (merges, cuts, reworked formulas) plus a full cross-check against a complete real Fallout: New Vegas perk list — this caught a real bug (Computer Whiz and Infiltrator had lost their genuine Level 18 gate in an earlier pass, now restored) and supplied 45 new ports across two rounds. Round 1 (16 ports): Tag!, Pack Rat, Stonewall, Sniper, Concentrated Fire, Better Criticals, Ninja, Ladykiller, Confirmed Bachelor, Black Widow, Cherchez la Femme, Rapid Reload, Plasma Spaz, Laser Commander, Junk Rounds, Vigilant Recycler. Round 2 (29 ports, developer-triaged): Here and Now, Terrifying Presence, Mad Bomber, Friend of the Night, Old World Gourmet, Travel Light, Light Step, Them's Good Eatin', Ferocious Loyalty, Heavyweight, Heave Ho!, Bloody Mess, Super Slam!, Piercing Strike, Splash Damage, Action Girl, Meltdown, Weapon Handling, Light Touch, Fast Metabolism, Hit the Deck, Nerd Rage!, Living Anatomy, Finesse, Hobbler, Center of Mass, Paralyzing Palm, Mister Sandman, Broad Daylight. Ladykiller/Confirmed Bachelor/Black Widow/Cherchez la Femme resolve against the established sexuality rule (`project_sexuality_rules`): Ladykiller and Black Widow/Cherchez la Femme are available to any character of the matching gender presentation (human or robot); Confirmed Bachelor is robot-male-presenting only, since human men are canonically heterosexual-only. A further batch was deferred to specific DLCs (Hunter/Entomologist/Animal Friend/Tribal Wisdom → Mirny DLC; Shotgun Surgeon/The Professional/And Stay Back → Halley DLC, after a lore check ruled out Palmer; Demolition Expert/Gunslinger/Hand Loader/Commando → DLC-scoped, unspecified; Tunnel Runner → Byrd DLC), flagged for further exploration before writing in (Walker Instinct, Certified Tech), or blocked on missing systems (Long Haul, Adamantium Skeleton, Explorer — fast travel or limb-specific damage) — see `FNV_Perk_Cross_Reference_Audit.md` and `TODO.md`. **A number of perks remain orphaned or still gate on a skill deliberately cut** — marked inline where it applies — pending a real design decision rather than being guessed at. The remaining ~118 perks are marked as pending in the placeholder section at the bottom of this file.

**Target distribution: ~174 non-combat (67%) / ~86 combat (33%)**  
Currently: 79 non-combat / 63 combat — combat is already well past the *old* 53-perk target and even accounts for most of the *new* 86-perk target's headroom; future design passes should be almost entirely non-combat to make any real progress toward the expanded 174 non-combat goal.  
Perks are primarily a system for deepening playstyle identity, not a combat improvement checklist.

Requirements use MACHINE stat abbreviations: **M** Might · **A** Agility · **C** Calculation · **H** Humanity · **I** Investigation · **N** Nerve · **E** Engine

---

## Social / Diplomatic

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Empathic Resonance** *(requirement updated 2026-07-26 — Empathy Protocols is now a distinct perk, not a skill; retargeted to Insight, the skill that actually replaced it)* | H 7, Insight 50 | 2 | Read the emotional state of any NPC; unlock compassionate dialogue options unavailable to others. Rank 2: NPCs in a receptive emotional state will share information they would normally withhold. |
| **Silver Tongue** | H 9 OR N 8, Speech 40 | 2 | +20% bonus to non-combat persuasion checks. Rank 2: after a failed persuasion check, one retry attempt per interaction becomes available. |
| **Lie Detector** | I 9 OR H 9, Insight 50 | 1 | Always know when an NPC is lying. Choose whether to reveal this knowledge in the moment or hold it for leverage. |
| **Faction Whisperer** | H 7, Narrative 50 | 2 | Reputation gains with all factions are amplified. Rank 2: once per faction per playthrough, a single catastrophic reputation event can be walked back through subsequent positive actions. |
| **Cover Identity** | H 9 OR N 8, Deception 75 | 2 | Maintain a false identity within a hostile faction significantly longer before being recognized. Rank 2: plant a false record trail that actively corroborates the cover story. |
| **Moral Authority** | N 8 | 1 | When making a moral argument, NPCs whose Nerve falls below a threshold cannot challenge the player's position through words; they must accept it or escalate to force. |
| **Professional Negotiator** | N 7, Speech 55 | 2 | In multi-stage dialogue encounters (summits, negotiations, interrogations), the player character can sustain their position through more pressure stages without forced concession. Rank 2 *(req: N 9, Speech 75)*: actively tire opposing parties; their position weakens with each failed stage. |
| **Fly on the Wall** | H 7 OR N 9, Deception 80 OR Sneak 100 | 1 | If the player character witnesses an event without intervening, NPCs involved can be made to forget they were present. Powerful for intelligence gathering without commitment. |
| **Off the Record** | Level 18, H 7 OR N 7, Narrative 65 | 1 | The first Reputation Matrix shift the player causes in any given district stays hidden/unregistered until a second shift in the same direction crosses it; lets a player deliberately test the waters or operate under the radar early in a district, at the cost of not being able to bank early goodwill either. |
| **Diplomat** | H 8, N 8, Speech 90 | 1 | Full diplomatic authority in formal negotiations; summits, treaty talks, faction leadership meetings treat the player character as a legitimate party rather than a mere messenger or petitioner. |
| **Empathy Protocols** | H 8, Insight 75 | 1 | Genuinely deep emotional attunement: sense not just that an NPC feels something, but the specific shape of it (e.g., grief, resentment, longing, etc.) well enough to address the real issue rather than its surface symptom. |
| **Reputation Management** | N 7, Narrative 80 | 2 | Actively author how the player character is perceived rather than just reacting to reputation as it accrues. Rank 1: plant a specific narrative about oneself in a district and have it actually stick and spread; Rank 2: Mitigation against Negative faction reputiation *(Formula: base level Faction Reputation Modifier + [Hum x 10]%)* |
| **Ladykiller** *(added 2026-07-26, ported from FNV — male, straight; available to any male character, human or robot, since heterosexuality is universal under the established sexuality rule)* | — | 1 | +10% damage against female-presenting targets; unique dialogue options with female NPCs. |
| **Confirmed Bachelor** *(added 2026-07-26, ported from FNV — male, gay; available only to male-presenting robot characters, never human males, since human men are canonically heterosexual-only — see `project_sexuality_rules`. A robot character with both this and Ladykiller roleplays as bisexual.)* | — *(robot, male-presenting, only)* | 1 | +10% damage against male-presenting targets; unique recognition dialogue with other male characters who share this orientation — including non-recruitable NPCs, mirroring FNV's Manny Vargas/Major Knight precedent. |
| **Black Widow** *(added 2026-07-26, ported from FNV — female, straight; available to any female character, human or robot, both established bisexual under the sexuality rule)* | — | 1 | +10% damage against male-presenting targets; unique dialogue options with male NPCs. |
| **Cherchez la Femme** *(added 2026-07-26, ported from FNV — female, lesbian; available to any female character, human or robot. A character with both this and Black Widow roleplays as bisexual.)* | — | 1 | +10% damage against female-presenting targets; unique recognition dialogue with other female characters who share this orientation. |
| **Terrifying Presence** *(added 2026-07-26, ported from FNV)* | Speech 70 | 1 | Intimidate a foe through dialogue; closing out the interaction causes them to flee combat briefly. |

---

## Growth / Learning *(new category, added 2026-07-04 — ported from Fallout: New Vegas)*

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Educated** | C 4 | 1 | Gain 2 additional skill points every time you level up. |
| **Swift Learner** | C 4 | 3 | Gain an additional 10% experience whenever XP is earned, per rank (up to +30% at rank 3). |
| **Comprehension** | — | 1 | Gain an additional skill point for reading a full data archive/log entry; reading a technical manual (Inner Tepenia's magazine equivalent) grants double the normal skill points. |
| **Intense Training** *(added 2026-07-27, ported directly from FNV — verified against the real perk: Level 2, up to 10 ranks total, no other requirement; reverses an earlier "Not Portable As-Is" call in `FNV_Perk_Cross_Reference_Audit.md`, per developer confirmation; see `Character-Creation/Permanent_MACHINE_Stat_Increases.md` for the full permanent-stat-growth system this belongs to)* | Level 2 | 10 | Permanently gain +1 to any single MACHINE stat of your choice, up to the normal cap of 10. Can be taken up to 10 times total across a playthrough. |
| **Tag!** *(added 2026-07-26, ported directly from FNV — no stat gate on the real perk either)* | Level 16 | 1 | Choose a 4th skill to Tag, receiving the same one-time +15 point bonus the original three Tag Skills grant at character creation. |
| **Here and Now** *(added 2026-07-26, ported directly from FNV — no stat gate on the real perk either)* | — | 1 | Instantly gain a full level. |

---

## Technical / Engineering

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Jury Rigging** | Level 14, Repair 80 | 3 | Rank 1: Repair and repurpose items using dissimilar components that normally wouldn't work together ; Rank 2: Increased effectiveness upon degradated items *(Formula: base level Repair effectiveness + [Calc x 10]%)*; Rank 3: Repair any item using any roughly similar item, regardless of type, Increased effectiveness upon degradated items *(Formula: base level Repair effectiveness + [Calc x 15]%)* |
| **Thermal Engineer** | Level 12, C 7 | 2 | Improved heat and power allocation in managed systems; reduces collateral damage during blackouts. Rank 2: temporarily stabilize a failing grid section, buying time for a proper solution. *(flagged for future review)*|
| **Power Grid Manager** | Level 12, E 6, C 6 | 2 | Route emergency power through improvised pathways, unlocking unique solutions in grid quests. Rank 2: improvised bypasses persist after the player leaves the area — lasting infrastructure change. |
| **Siligel Chemist** | Level 8, C 7, Chemistry 50 | 2 | Improved crafting and efficiency with siligel-based components. Rank 2: synthesize rare siligel compounds not available through normal commerce or salvage. *(requirement updated 2026-07-26 — Siligel Chemistry retargeted to the new Chemistry skill)* |
| **Decentralized Systems** | C 7, Hacking 75 | 1 | +30% effectiveness when designing or linking decentralized power nodes. Core perk for the Independent Lattice hidden path. *(flagged for future review)*|
| **Precision Maintenance** | C 9 OR Repair 100 | 3 | Repaired items degrade more slowly and occasionally exceed their base specifications after repair. The player character's fine motor calibration is operating at peak precision.: Rank 1: items degrade 10% slower, Rank 2: items degrade 20% slower, Rank 3: items degrade 30% slower |
| **Hydroponic Specialist** | Chemistry 50, Biology 50 | 2 | Rank 1: Improved yields, growth rates, and system efficiency in hydroponic operations. Rank 2: cultivate rare medicinal and chemical plants not available through any other source. |
| **Junk Rounds** *(added 2026-07-26, ported from FNV — Luck retargeted to Investigation, since Engine is already the recovery-speed/AP-replenishment stat, not a resourcefulness stat)* | I 6, Repair 45 | 1 | Craft ammunition using scrap metal and salvaged components. |
| **Vigilant Recycler** *(added 2026-07-26, ported from FNV — Science retargeted away from any of its three descendant skills entirely, per developer's own call: field-survivalist skills fit better than a lab-science one)* | Repair 50 OR Outdoorsman 70 | 1 | When using Energy Weapons, twice as likely to recover drained ammunition components; more efficient recycling recipes available at workbenches. |
| **Mad Bomber** *(added 2026-07-26, ported from FNV)* | Repair 45, Explosives 45 | 1 | Unlocks special explosive crafting recipes at any workbench. |



---

## Information / Data

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Ghost in the Machine** | Level 18, C 6, Hacking 55 | 2 | Rank 1: Trace signature is significantly reduced on all hacks. Passive data reads on Level 1–2 systems (C ≤4 / Hacking ≤30 requirement) have a high chance of leaving no trace at all. Active manipulation still generates a signature. ; Rank 2 *(req: Level 24, C 7, Hacking 90)*: Any hack on a system with a Calculation requirement of 5 or below **OR** a Hacking skill requirement of 50 or below is **completely untraceable**: no log entry, no signature, no consequence. Covers all Level 0–3 systems. High-security systems (Level 4+) remain traceable even with this perk. See `Hacking_and_Traceability_System.md` for full context. |
| **Arcanet Weaver** *(requirement updated 2026-07-26)* | C 8, Hacking 60 | 2 | Hacking is faster and more reliable across all system types. Rank 2: queue multiple simultaneous operations within a single hack session. |
| **Data Archaeologist** *(renamed 2026-07-26 from "Deep Archive" — Data Archaeology no longer exists as a skill; retargeted to Cryptography at the audit's own finalized threshold (80), matching the new identity-noun perk naming convention — see `feedback_perk_naming_convention`)* | C 7, Cryptography 80 | 2 | Recover data from more severely corrupted sources than normally possible. Rank 2: recover data classified as permanently unrecoverable (e.g., pre-war records, scrubbed histories, war-era blackouts, etc.) |
| **Signal Sculptor** | C N 10 OR E 10 OR Hacking 90 | 1 | Optimize Arcanet subnets in ways that create lasting network shortcuts; bypasses and cached routes that persist across the playthrough and can be used by faction contacts. |
| **Disinformation Architect** *(flagged for future renaming)* | C 8, N 8, Hacking 90 | 1 | Planted false information persists, spreads through the Arcanet, and can be used to shift faction narratives over extended time. Slow-burning social weapon. |
| **Pattern Intuition** | I 7, Insight 75 OR Deception 75 | 1 | Unreliable or manipulated information sources are flagged automatically. The player character recognizes disinformation campaigns, misdirection, and planted evidence on sight. |
| **Cryptographer's Eye** *(flagged for renaming; something related to the Rosetta Stone)* | C 7, Cryptography 55 | 2 | Decryption is significantly faster and more reliable. Rank 2: given enough time, break encryption that is theoretically unbreakable, including pre-war military-grade ciphers. |
| **Computer Whiz** | Level 18, C 7, Hacking 70 | 1 | Gain one additional attempt after failing a hack on a high-security (Level 4+) system, before the normal lockout applies. *(ported from FNV; requirement updated 2026-07-26 — restored the Level 18 gate present on the real perk, dropped in an earlier pass)* |
| **Infiltrator** | Level 18, I 7, Lockpick 70 | 1 | Gain one additional attempt after failing to pick a broken lock. *(ported from FNV; requirement updated 2026-07-26 — restored the Level 18 gate present on the real perk, dropped in an earlier pass)* |
| **Arcanet Navigation** *(added 2026-07-26)* | C 6, Hacking 50 | 1 | Navigate the Arcanet's subnet architecture directly and fluently; faster travel *(flagged for future review)* between nodes, and an instinctive sense of a subnet's layout before fully exploring it. |

---

## Survival / Exploration

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Ripple Weaver** *(flagged for future review, tentatively possible removal)* | I 6, E 6, Survival 50 | 2 | Predict power grid ripples and blackouts before they happen; better salvage during fluctuations. Rank 2: exploit ripples actively as solutions to quests and puzzles — turning crises into tools. |
| **Frontier Resilience** *(requirement updated 2026-07-26 — Frontier Survival & Cold Adaptation retargeted to Outdoorsman)* | E 6, M 6, Outdoorsman 55 | 2 | Cold resistance and improved performance in Frostlands and extreme environments. Rank 2: construct and maintain modular outposts in the Frostlands, permanent field infrastructure. |
| **Undergrid Runner** *(requirement updated 2026-07-26)* | Level 10, A 8, I 7, E 7 | 2 | Faster movement and reduced hazard effects in the Undergrid. Rank 2: reveal hidden routes and passages visible only to the most experienced Undergrid navigators. |
| **Salvage Instinct** *(requirement updated 2026-07-26)* | I 6, Survival 50 | 2 | Better quality loot from all searched containers and areas. Rank 2: detect hidden or buried containers not visible through normal inspection. |
| **Environmental Reader** *(requirement updated 2026-07-26, flagged for renaming)* | I 7, Survival 60 | 1 | Gas leaks, structural collapse risk, live electrical hazards, and other environmental dangers are always visible before entering an area; and can often be weaponized rather than avoided. |
| **Hazard-Adapted Systems** *(orphaned 2026-07-26, flagged for future renaming)* | I 7, E 7, Survival 55 | 2 | Penalties from environmental hazards (ice, collapsing tunnels, blackout zones) are significantly reduced. Rank 2: certain hazards that would stop other characters become tactical tools the player character can exploit. |
| **Isolation Protocol** *(blocked 2026-07-26 — flagged for future review)* | N 7, E 6, Survival 65 | 1 | Psychological debuffs from prolonged isolation, Arcanet interference, and blackout-zone static have no effect. The player character's systems have fully adapted to operating alone. |
| **Scavenger** *(added 2026-07-04, ported from FNV's Fortune Finder/Scrounger)* | I 7 OR Survival 75 | 2 | Find what everyone else missed: hidden or buried caches in places already searched by other scavengers, in locations nobody else thought to check. distinct from Salvage Instinct, which improves loot quality rather than raw quantity. Rank 1: Considerably more currency and ammunition (quantity, not quality) turn up in searched containers and stockpiles; Rank 2: Additional bonus to all items found via Rank 1 *(Formula: base level Scavenger effectiveness + [MOD x 10]%, where MOD is either Nerve or Engine, whichever is higher)* |
| **Frontier Survival** *(added 2026-07-26)* | E 8, N 7, Outdoorsman 75 | 1 | Thrive rather than merely survive in the Frostlands; sustained exposure carries no penalty at all, and the player character can guide others through conditions that would otherwise require dedicated survival gear. |
| **Cold Adaptation** *(added 2026-07-26)* | E 7, N 6, Outdoorsman 50 | 1 | Meaningfully reduced cold-exposure penalties outside protected districts, a real edge in the Frostlands without yet being fully at home there. |
| **Environmental Exploitation** *(added 2026-07-26)* | E 6, I 7, Survival 50 | 1 | Actively turn hazardous conditions (e.g., ripples, blackouts, structural instability, etc.) into tools and opportunities rather than just surviving them. |
| **Hazard Navigation** *(added 2026-07-26)* | A 8 ||OR|| I 8; Survival 50 ||OR|| Athletics 75 ||OR|| Acrobatics 75 | 1 | Move through ice, collapsing tunnels, and blackout zones with genuine confidence rather than just tolerance — reachable through a physical-endurance build, an analytical/investigative build, or an agility-and-finesse build alike. |
| **Friend of the Night** *(added 2026-07-26, ported from FNV — Perception retargeted to Investigation)* | I 6, Sneak 30 | 1 | Eyes adapt quickly to low-light conditions. |
| **Old World Gourmet** *(added 2026-07-26, ported from FNV)* | E 6, Survival 45 | 1 | +25% addiction resistance; +50% health bonus from snack-food items; Glitch-Coolant grants health in addition to its normal effects. |
| **Travel Light** *(added 2026-07-26, ported from FNV)* | Survival 45 | 1 | +10% movement speed while wearing light armor or no armor. |
| **Light Step** *(added 2026-07-26, ported from FNV — Perception retargeted to Investigation)* | I 6, A 6 | 1 | Floor traps and mines never trigger. |
| **Them's Good Eatin'** *(added 2026-07-26, ported from FNV)* | Survival 55 | 1 | Creatures killed have a chance to yield a potent healing item when looted. |

---

## Cultural / Philosophical

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Goth Adept** *(flagged for renaming, as well as becoming a quest-based perk)* | *(none)* previously: *(H 8 OR Insight 90)* | 1 | Deep understanding of Goth death-ritual culture; unique dialogue options with Goth NPCs and access to rituals normally closed to outsiders. unlock Goth-exclusive questlines and participate in closed ceremonies. |
| **Sonic Initiate** *(flagged for renaming)* | Level 24, A 6, H 6, Insight 50 | 2 | Resonance with Cymaticist sonic practices; unique interactions with sound-based technology and Cymaticist communities. Rank 2: use sonic technology in ways only trained Cymaticists can, including Cymaticist-locked equipment. |
| **Theologian** *(requirement updated 2026-07-26 — Robot Religion Insight was cut entirely as a former Specialized/Cultural skill, with no perk or skill replacement at all; skill threshold dropped rather than guessed at)* | H 8 OR N 9, Speech 90 OR Insight 90 | 1 | Mediate conflicts between robot religious sects with genuine authority. Opens unique questlines tied to robot spiritual practices across multiple districts, and unlocks religious dialogue branches in major quests. |
| **Ossuary Resonance** *(added 2026-07-26)* | Level 26, H 8, N 7, Insight 90 | 1 | A genuine, unlearned attunement to Goth death-ritual practice; not studied from the outside, but rather, felt the way an initiate feels it. Distinct from Goth Adept above, which is knowledge acquired through study rather than something innate.; Rank 2 *(req: Level 36)*: unlock Goth-exclusive questlines and participate in closed ceremonies normally only available to players having completed the *Goth Adept* questline. |
| **Sonic Attunement** *(added 2026-07-26, quest-gated — completion of the relevant questline is the gate itself, no stat/skill threshold needed on top)* | Quest-gated | 1 | Full Cymaticist sonic-practice standing, earned through the questline itself rather than through stat investment. |
| **Golden Eye Calibration** *(added 2026-07-26, quest-gated)* | Quest-gated | 1 | *(Effect not yet designed — carried over from the Skills.md restructure as a placeholder quest-gated perk.)* |
| **Holographic Projection** *(added 2026-07-26)* | C 7 ||OR|| N 8, E 8; Hacking 60 ||OR|| Sleight of Hand 100 | 1 | Use a data network to project a "decoy" version of oneself elsewhere — the decoy can't manipulate anything; its only function is distraction. Reachable through a hacker's build (Calculation + Hacking) or a con-artist's build (Nerve + Engine + Sleight of Hand) alike. |
| **Golden Ring Devotee** *(added 2026-08-11, surfaced while designing TBN [TCY-42 ravishing extravagant Lillian]'s Romance Beat 2 check — see `Core-Mechanics/Companion_System.md`)* | H 7, Insight 70 OR Narrative 70 | 1 | Deep understanding of Leo's grand/intimate performance tradition (the "Golden Ring") — recognized by practitioners of either house as someone who genuinely gets it, not a tourist. Unique dialogue options with Leo performers across both houses; surfaces the district's own internal politics normally closed to outsiders. |

---

## Economic / Resource

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Black Marketeer** | I 6, Pisces reputation (positive) *(flagged for repartitioning into a quest-based perk)* | 2 | Better prices, access, and selection in black market contexts across all districts. Rank 2: *(req: Black Marketeer questline completion)* acquire items listed as unavailable, destroyed, or restricted — if someone in Concordia has it, it can be found. |
| **Resource Recovery** *(requirement updated 2026-07-26 — Scavenging & Resource Foraging retargeted to Survival)* | C 6, Survival 75 | 2 | Components used in crafting have a chance to partially return. Rank 2: return rate improves significantly; high-Engine characters recover nearly half of all consumed materials. |
| **Siligel Metabolism** *(requirement updated 2026-07-26 — Siligel Chemistry retargeted to Chemistry)* | E 8, Chemistry 55 | 1 | All siligel consumption rates permanently reduced. Represents deep systemic self-optimization of the player character's internal processes — something that cannot be undone. |
| **Strong Back** *(added 2026-07-04, ported from FNV)* | M 5, E 5 | 1 | +50 carry weight. |
| **Pack Rat** *(added 2026-07-26, ported from FNV; carry-weight unit baseline still TBD, same dependency already flagged on the Hoarder trait)* | I 5, Barter 70 | 1 | Items weighing two pounds or less now weigh half as much — complements Strong Back's flat carry-weight bonus rather than duplicating it. |
| **Heavyweight** *(added 2026-07-26, ported from FNV — Might-scaling)* | M 6 | 1 | Weapons above a set weight threshold weigh half as much. |

---

## Companion / Leadership

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Companion Cohesion** *(flagged for future renaming)* | N 8, H 7 | 2 | Companions perform significantly better in combat and exploration when physically near the player character. Rank 2: enables two companions to be active simultaneously, where the normal limit is one. |
| **Trusted Command** *(requirement updated 2026-07-26, same reasoning)* | N 8 | 1 | Every companion's crisis behavior improves by one tier permanently — companions who would flee hold position; companions who hold position push harder. |
| **Shared Experience** *(requirement updated 2026-07-26, same reasoning)* | H 7 | 1 | The active companion gains skill points in their primary skill category every time the player character levels up if currently in active party. Long-term investment in a specific companion pays off mechanically. |
| **[NAME PENDING — Companion Command & Loyalty]** *(added 2026-07-26 from the Skills.md restructure; deliberately NOT using that exact name as a permanent title, since it's the same name as the skill just retired above — flagged in the audit itself as \[to-be-renamed\])* | N 7, H 7 | 1 | Direct, effective command presence over a companion in the field — the kind of leadership that gets followed without needing to be Trusted Command's deeper, earned loyalty first. |
| **Bond Ledger** *(added 2026-07-24, marked for possible future renaming — mutually exclusive with Grief Ledger, EXCEPT for Calethina, who has both — see her own README)* | H 6 | 1 | Repeated re-specs with a companion present accumulate Bond faster on the Fragmentation Matrix. Builds toward the deeper companion tiers (up to The Long Vigil) more readily, at the cost of slower Grief accumulation — a build that leans into closeness over catharsis. |
| **Grief Ledger** *(added 2026-07-24, marked for possible future renaming — mutually exclusive with Bond Ledger, EXCEPT for Calethina, who has both — see her own README)* | N 6 | 1 | Repeated re-specs with a companion present accumulate Grief faster on the Fragmentation Matrix, but each individual re-spec's Grief cost to the player character is reduced. A build that leans into processing change quickly over building steady closeness. |
| **Ferocious Loyalty** *(added 2026-07-26, ported from FNV — Cha retargeted to Humanity)* | H 6 | 1 | When the player character drops below 50% health, the active companion gains +50 DR. |

---

## Combat — Offensive

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Rapid Fire Protocols** | A 7, Tactical Grid Combat 50 | 2 | Basic attacks cost -5% AP (minimum 3 AP per attack). Rank 2: the first attack of each turn costs an additional -5% AP less (the opening shot is always efficient.) |
| **Precision Strike** *(orphaned 2026-07-26, same issue)* | N 7, I 7, Acrobatics 50 | 2 | Aimed and special attacks cost -5% AP. Rank 2: also gain +10% accuracy on all aimed attacks. |
| **Grim Reaper Protocols** | M 6, A 6 | 1 | Killing an enemy in combat refunds 3 AP, once per turn. Rewards aggressive, decisive play. |
| **Improvised Lethality** *(orphaned 2026-07-26 — Improvised Weaponry & Combat Jury-Rig is now a perk, not a skill)* | M 7, Improvised Weaponry & Combat Jury-Rig 55 | 2 | Improvised weapons deal significantly more damage. Rank 2: construct improvised weapons mid-combat at no AP cost — turn the environment into an arsenal. |
| **Power Strike** *(orphaned 2026-07-26 — Non-Lethal Restraint & Subdual is now the perk Non-Lethal Neutralization, not a skill)* | M 8, Bladed Melee 50 OR Blunt Melee 50 | 1 | Every melee attack in an engagement has a chance to trigger an automatic knockdown, regardless of target size or armor type. *(flagged for formula)* |
| **Electronic Disruptor** *(orphaned 2026-07-26 — Electronic Warfare is now a perk, not a skill)* | C 7, Hacking 60 | 2 | EMP and electronic attacks have higher success rates and longer effect durations. Rank 2: a successful electronic attack can chain disruption to one adjacent electronic target at no additional cost. |
| **Overclocked Aggression** | E 8, M 7 | 1 | Once per combat: sacrifice half maximum-total AP on the next turn to gain +[4 + *(Calc)* + *(Nerve)*] temporary AP on the current turn. High-risk burst option. |
| **Crusher** *(added 2026-07-26, marked for possible future renaming)* | Level 26, M 7, N 6, E 7 | 2 | Rank 1: Power Attacks (`Combat/Power_Attacks.md`) deal +20% damage, and their vulnerability window is mitigated by 10 points — the base -20% DT/-20% DR penalty becomes -10% DT/-10% DR for one turn. Rank 2: Power Attacks deal +30% damage, and the mitigation rises to 20 points — fully canceling the base penalty, leaving no DT/DR penalty at all. |
| **Steady Retrieval** *(added 2026-07-24, orphaned 2026-07-26 — same Improvised Weaponry & Combat Jury-Rig issue as Improvised Lethality above)* | A 6, Improvised Weaponry & Combat Jury-Rig 45 | 2 | Retrieving a thrown weapon that's stuck where it landed costs 1 fewer AP. Rank 2: thrown weapons can also be thrown 1 additional grid step farther before retrieval range becomes an issue. Direct hook into the game's own thrown-weapon retrieval rule. |
| **Non-Lethal Neutralization** *(added 2026-07-26)* | M 8, A 6 ||OR|| H 7, N 7 | 1 | Reliably take an enemy down without killing them, reachable through a physical-control build (Might + Agility) or a de-escalation build (Humanity + Nerve) alike. |
| **Improvised Weaponry** *(added 2026-07-26, flagged for addition upon Launch full release)* | M 6, A 6, C 7 | 1 | Turn whatever's at hand — pipes, tools, debris — into a genuinely effective weapon, on the fly, without dedicated equipment. |
| **Endurance Fighting** *(added 2026-07-26 — distinct from the existing, now-orphaned "Endurance Fighter" perk below)* | M 10 ||OR|| A 7, N 7, E 7 | 1 | Keep fighting effectively well past the point that would stop most combatants, reachable through raw physical toughness alone or through a balanced agility/composure/systems build. |
| **Tactical Grid Combat** *(added 2026-07-26, flagged for reconfiguration, as this mostly cannot apply to a turn-based environment)* | A 8, C 7 | 1 | Read and exploit the tactical grid itself — positioning, cover, and movement options resolve faster and more precisely than for a combatant relying on instinct alone. |
| **Electronic Warfare** *(added 2026-07-26)* | C 8, I 7 | 1 | Direct, reliable disruption of enemy electronics and robotic systems in the field, beyond what any single Electronic Disruptor-style trick can manage on its own. |
| **Threat Assessment** *(added 2026-07-26, flagged for further elaboration)* | I 8, N 7 | 1 | Accurately read a combat encounter's real danger level before it starts — not just who's hostile, but who's actually dangerous. |
| **Rapid Reload** *(added 2026-07-26, ported from FNV — confirmed reloading is modeled as an explicit AP-costed action)* | A 5, Guns 30 | 1 | Reloading costs 25% less AP than normal. |
| **Plasma Spaz** *(added 2026-07-26, ported from FNV — confirmed Energy Weapons has named subtypes)* | Energy Weapons 70 | 1 | AP cost for all plasma weapons is reduced by 20%. |
| **Laser Commander** *(added 2026-07-26, ported from FNV — confirmed Energy Weapons has named subtypes)* | Energy Weapons 90 | 1 | +15% damage and +10% critical chance with any laser weapon. |
| **Heave, Ho!** *(added 2026-07-26, ported from FNV — directly relevant to the Throwing Weapons system, Might already governs throw distance)* | M 5, Explosives 30 | 1 | +50% thrown weapon velocity and range. |
| **Bloody Mess** *(added 2026-07-26, ported from FNV — no stat gate on the real perk either)* | — | 1 | +5% overall damage; more violent death animations. |
| **Super Slam!** *(added 2026-07-26, ported from FNV)* | M 6, Bladed Melee 45 OR Blunt Melee 45 | 1 | Melee attacks have a chance to knock the target down. |
| **Piercing Strike** *(added 2026-07-26, ported from FNV)* | Unarmed 70 | 1 | Unarmed and melee attacks negate 15 points of the target's DT. |
| **Splash Damage** *(added 2026-07-26, ported from FNV)* | Explosives 70 | 1 | +25% explosive area of effect. |
| **Action Girl** *(added 2026-07-26, ported from FNV)* | A 6 | 2 | +15 AP per rank. |
| **Meltdown** *(added 2026-07-26, ported from FNV)* | Energy Weapons 90 | 1 | Foes killed by energy weapons emit a corona of harmful energy, damaging anyone standing nearby. |
| **Weapon Handling** *(added 2026-07-26, ported from FNV — Might-scaling)* | M < 10 | 1 | Weapon Might requirements are 2 points lower than normal. |

---

## Combat — Defensive

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Reactive Shielding** *(orphaned 2026-07-26 — Defensive Posturing & Endurance Fighting is now the perk Endurance Fighting, not a skill)* | E 7, Athletics 60 OR Acrobatics 60 OR Survival 60 | 2 | When taking heavy damage, automatic partial absorption triggers for two turns, once per combat-encounter; Rank 2: can trigger once per AP cycle rather than once per combat. |
| **Endurance Fighter** *(orphaned 2026-07-26, same issue — note the near-name-collision with the new Endurance Fighting perk added below in Combat — Offensive, which is a distinct perk)* | M 7, N 7, Athletics 60 OR Acrobatics 60 OR Survival 60 | 1 | AP penalties from taking damage don't apply until health drops below 25%, rather than at the normal threshold. |
| **Combat Awareness** *(flagged for mechanics expansion)* | I 6, Insight 50 | 2 | Before combat begins, identify which enemies will act first and approximate their damage potential. Rank 2: detects ambushes before they trigger, converting a surprise attack into a normal initiative sequence. |
| **Armor Integrity** | E 7, M 6, Repair 50 | 2 | Equipped armor degrades significantly more slowly in extended engagements. Rank 2: armor damage heals partially between combats, reducing maintenance burden on long expeditions. |
| **Last Stand** | N 9, E 7 | 1 | Once per combat, when health would reach zero, survive at 1 HP and immediately gain double AP for an emergency action upon the player's turn, immune to all attacks until it's the player's turn *(i.e., "The player character refuses to go offline.")* |
| **Stonewall** *(added 2026-07-26, ported from FNV)* | M 6, E 6 | 1 | +5 DT against melee and unarmed attacks; cannot be knocked down during combat. |
| **Toughness** *(added 2026-07-04, ported from FNV)* | E 5 | 2 | +3 permanent DT per rank. |
| **Life Giver** *(added 2026-07-04, ported from FNV)* | E 6 | 1 | +30 maximum health. |
| **Nerves of Steel** *(added 2026-07-04, ported from FNV — reworked, see note below)* | E 7 | 1 | Up to 2 unused AP at the end of your turn carry over into your next turn instead of being discarded (does not stack beyond 2 banked AP at a time). *(Provisional — flagged for developer review: FNV's original effect, "20% faster AP regeneration," doesn't map onto Inner Tepenia's turn-based AP model, since AP doesn't regenerate mid-turn and unused AP is discarded by the base rule rather than continuously refilling. This reworks it as the first implementation of the AP-banking idea already flagged, undesigned, in `Core-Mechanics/Action_Points_Perks_and_Traits.md`. Gated on Engine since Engine is already defined as the recovery-speed/AP-replenishment stat.)* |
| **Light Touch** *(added 2026-07-26, ported from FNV)* | A 6, Repair 45 | 1 | While wearing light armor, +5% critical hit chance; enemies suffer -25% critical hit chance against the player character. |
| **Fast Metabolism** *(added 2026-07-26, ported from FNV — no stat gate on the real perk either)* | — | 1 | +20% HP restored from healing items. |
| **Hit the Deck** *(added 2026-07-26, ported from FNV)* | Explosives 70 | 1 | +25 DT against explosive damage. |
| **Nerd Rage!** *(added 2026-07-26, ported from FNV — Science retargeted to Hacking, matching Computer Whiz/Math Wrath's own precedent)* | C 5, Hacking 50 | 1 | Whenever health drops to 20% or below, gain +15 DT and Might is treated as maxed for the duration. |

---

## Combat — NODE / Targeting

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Processing Overdrive** *(orphaned 2026-07-26, same Tactical Grid Combat issue as the Combat — Offensive perks above)* | Level 20, C 7, Hacking 50 OR Insight 50 | 2 | NODE analysis window is extended *(flagged for elaboration)*. Rank 2: one additional shot can be queued per NODE activation. |
| **Salt in the Wound** *(orphaned 2026-07-26, same issue)* | I 7, Acrobatics 55 OR Insight 55 | 2 | Scanned weak points display estimated damage and likely secondary effects before the shot is committed. Rank 2: targeting a scanned weak point costs -5% AP. |
| **Chain Protocol** | N 8, C 7 | 1 | Critical hits on robot enemies have a significantly higher chance to trigger cascade failures. A cascade can spread from the struck component to one adjacent system. |
| **Predictive Algorithms** *(flagged for reconfiguration, possible deferrment until Outer Tepenia trilogy)* | C 8, I 7 | 1 | In NODE mode, moving targets display projected positions. Accuracy penalties for targeting moving enemies are halved. |
| **Focus Under Fire** *(flagged for reconfiguration, possible deferrment until Outer Tepenia trilogy)* | N 7, Tactical Grid Combat 45 | 2 | Taking damage during NODE activation drains Nerve at a reduced rate. Rank 2: taking damage during NODE no longer drains Nerve at all — the player character's focus is unbreakable. |
| **Perimeter Awareness** *(added 2026-07-04, ported from FNV's Alertness)* | I 6 | 1 | While stationary and not moved this turn, gain a bonus to targeting accuracy in NODE mode equivalent to +2 Investigation. |
| **Math Wrath** *(added 2026-07-26, ported directly from FNV — verified against the real perk: Level 10, Science 70, "reduces all V.A.T.S. AP costs by 10%," no other effect; requirement updated 2026-07-26 — Arcanet Navigation & Hacking retargeted to Hacking)* | Hacking 70 | 1 | All NODE-mode attacks cost 10% less AP. |
| **Sniper** *(added 2026-07-26, ported from FNV — mapped onto Investigation since Inner Tepenia has no Perception stat and Investigation already governs the weak-point bonus in `Targeting_System.md`; exact percentage/formula not yet designed, flagged for a future balance pass)* | I 6 | 1 | Increased chance to land a scanned weak-point hit in NODE mode. |
| **Concentrated Fire** *(added 2026-07-26, ported from FNV — mapped onto Calculation (crit-chance governance) plus the two ranged skill lines it originally gated on; exact percentage/formula not yet designed, flagged for a future balance pass)* | C 6, Guns 60, Energy Weapons 60 | 1 | Accuracy increases with each subsequent NODE-mode attack queued against the same target or body part. |
| **Better Criticals** *(added 2026-07-26, ported from FNV — real perk gates on Perception + Luck, neither of which exist as Inner Tepenia MACHINE stats; developer's call: Nerve alone)* | N 6 | 1 | +50% damage with critical hits. |
| **Living Anatomy** *(added 2026-07-26, ported from FNV)* | Medicine 70 | 1 | Reveals a target's health and DT in NODE mode; +5% damage against humans and non-feral robots. |
| **Finesse** *(added 2026-07-26, ported from FNV — no stat gate on the real perk either)* | — | 1 | +5% critical hit chance. |
| **Hobbler** *(added 2026-07-26, ported from FNV — Perception retargeted to Investigation)* | I 7 | 1 | +25% chance to hit a target's legs in NODE mode. |
| **Center of Mass** *(added 2026-07-26, ported from FNV)* | Guns 70 | 1 | +15% NODE-mode damage when targeting the torso. |
| **Paralyzing Palm** *(added 2026-07-26, ported from FNV)* | Unarmed 70 | 1 | A NODE-mode unarmed attack can paralyze the target for a short duration. |

---

## Combat — Hybrid / Specialized

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Non-Lethal Specialist** *(orphaned 2026-07-26 — Non-Lethal Restraint & Subdual is now the perk Non-Lethal Neutralization, not a skill)* | A 6, M 6, Non-Lethal Restraint & Subdual 50 | 2 | Subdual options are more reliable and cost -5% AP; non-lethal takedowns leave targets incapacitated longer. Rank 2: perform non-lethal takedowns on enemy types that are normally immune to subdual. |
| **Field Repair Protocols** *(requirement updated 2026-07-26 — Precision Maintenance & Repair retargeted to Repair)* | E 6, Repair 50 | 2 | Perform emergency self-repair during combat using components in inventory — no workbench needed. Rank 2: can also repair companions mid-combat without spending additional AP. |
| **Threat Exploitation** *(orphaned 2026-07-26 — Threat Assessment is now a perk, not a skill)* | I 7, Acrobatics 55 OR Insight 55 | 1 | After successfully assessing a threat before combat, the first attack on that target is guaranteed to hit regardless of other modifiers. Preparation pays. |
| **Robotics Expert** *(added 2026-07-04, ported from FNV; orphaned 2026-07-26, same Threat Assessment issue)* | N 6, Hacking 50 | 1 | +25% damage against automated defenses. Non-alerted automated defenses can be shut down (rather than destroyed) by sneaking up and deactivating them directly. |
| **Silent Running** *(added 2026-07-04, ported from FNV; flagged for repurposing to the Outer Tepenia trilogy)* | A 6, Sneak 50 | 1 | Running no longer breaks stealth or interrupts a sneak attempt. |
| **Quick Draw** *(added 2026-07-04, ported from FNV — reworked for turn-based AP, per the user's own design)* | A 5 | 1 | Drawing or holstering a weapon in combat costs no AP. *(FNV's original effect, "50% faster equip/holster," is a real-time animation-speed mechanic that doesn't translate to a discrete per-action AP cost — this reworks the same intent, removing weapon-switching as a tactical burden, into an AP-cost term instead.)* |
| **Ninja** *(added 2026-07-26, ported from FNV — Melee Weapons/Sneak retargeted to Bladed Melee OR Blunt Melee, plus Sneak; explicitly includes thrown blades, per the game's own Throwing Weapons system)* | Bladed Melee 80 OR Blunt Melee 80, Sneak 80 | 1 | Multiplies critical hit chance with melee, unarmed, and thrown-blade weapons; +25% damage with melee/unarmed/thrown-blade sneak-attack criticals. |
| **Mister Sandman** *(added 2026-07-26, ported from FNV)* | Sneak 60 | 1 | Instantly kill a sleeping NPC undetected; grants bonus XP. |
| **Broad Daylight** *(added 2026-07-26, ported from FNV — no stat gate on the real perk either)* | — | 1 | No Sneak penalty from using a light source. |

---

## Perk Count by Category

*(Recounted 2026-07-26 — 29 more FNV ports added across all non-combat categories plus Combat — Offensive/Defensive/NODE/Hybrid, after the developer triaged the full Clean Candidates list (write in / flag for exploration / assign to a DLC). Previously recounted 2026-07-26 after 3 FNV ports added to Combat — Offensive (Rapid Reload, Plasma Spaz, Laser Commander), after resolving the Black Widow/Cherchez la Femme/Ladykiller/Confirmed Bachelor question, after cross-checking against a complete real FNV perk list, and after the developer's own full pass over the perk list, the `Skills.md` restructure, 2026-07-24 — Off the Record, Bond Ledger, Grief Ledger, Steady Retrieval — and 2026-07-04 after adding 15 Fallout-adapted perks — see `project_fallout_trait_perk_adaptation` memory.)*

| Category | Count | Type |
|----------|-------|------|
| Social / Diplomatic | 17 | Non-combat |
| Growth / Learning | 6 | Non-combat |
| Technical / Engineering | 10 | Non-combat |
| Information / Data | 10 | Non-combat |
| Survival / Exploration | 17 | Non-combat |
| Cultural / Philosophical | 7 | Non-combat |
| Economic / Resource | 6 | Non-combat |
| Companion / Leadership | 7 | Non-combat |
| **Non-combat subtotal** | **80** | **56%** |
| Combat — Offensive | 26 | Combat |
| Combat — Defensive | 13 | Combat |
| Combat — NODE / Targeting | 15 | Combat |
| Combat — Hybrid / Specialized | 9 | Combat |
| **Combat subtotal** | **63** | **44%** |
| **Total** | **143** | |

Expansion in future design passes should maintain roughly this non-combat to combat ratio. DLC perks may skew toward the DLC's thematic focus, but the aggregate ratio across base game + all DLC should remain non-combat dominant.

---

## Pending Perks — Placeholders (~118 remaining to reach 260 target)

*(Updated 2026-07-26 — target pool size raised from 160 to 260 by developer request, same 67%/33% ratio, adding roughly 60% more headroom to every category's own rough target below. Previously updated after 29 more FNV ports pushed the designed count from 113 to 142, after 3 more FNV ports pushed the count from 108 to 111, after 4 more FNV ports pushed the count from 104 to 108, after cross-checking against a complete real FNV perk list pushed the count from 97 to 104, after the `Skills.md` restructure pushed the count from 82 to 101, and 2026-07-04 after the Fallout-adapted perk batch — see `project_fallout_trait_perk_adaptation` memory.)*

The categories below indicate where additional perks are needed. Names and effects are to be designed during dedicated perk design passes. Rough targets per category to reach the 260 total at the correct ratio:

### Non-combat (need ~95 more to reach ~174 total)

| Category | Currently designed | Rough target | Still needed |
|----------|-------------------|--------------|-------------|
| Social / Diplomatic | 17 | ~29 | ~12 more |
| Growth / Learning | 6 | ~15 | ~9 more |
| Technical / Engineering | 10 | ~29 | ~19 more |
| Information / Data | 10 | ~26 | ~16 more |
| Survival / Exploration | 17 | ~26 | ~9 more |
| Cultural / Philosophical | 7 | ~20 | ~13 more |
| Economic / Resource | 6 | ~16 | ~10 more |
| Companion / Leadership | 7 | ~16 | ~9 more |

### Combat (need ~23 more to reach ~86 total, unevenly distributed)

| Category | Currently designed | Rough target | Still needed |
|----------|-------------------|--------------|-------------|
| Combat — Offensive | 26 | ~20 | ~0 more (already over target — fine, not a problem) |
| Combat — Defensive | 13 | ~22 | ~9 more |
| Combat — NODE / Targeting | 15 | ~22 | ~7 more |
| Combat — Hybrid / Specialized | 9 | ~22 | ~13 more |

**Design note for future passes**: even with the expanded 260 goal, Combat — Offensive alone already exceeds its own rough share, while the other three combat categories and nearly every non-combat category still have real room to grow. Prioritize the most underrepresented categories first (Growth/Learning, Companion/Leadership, Combat — Hybrid/Specialized, Cultural/Philosophical) before adding more to already-robust ones (Combat — Offensive above all). New non-combat categories not yet invented are still encouraged — the world of Inner Tepenia has enough distinct systems to support them.

**Before adding more perks, resolve the orphaned-perk backlog from the 2026-07-26 restructure first** (see the intro note and every perk marked *orphaned*/*blocked* inline above) — retargeting those to a real gate matters more than growing the raw count further.
