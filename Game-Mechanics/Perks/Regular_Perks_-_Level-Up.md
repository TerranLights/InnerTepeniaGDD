# Regular Perks (Level-Up)

**Marked for future review (2026-07-04):** every perk in this file — old and newly added alike — is provisional. Progress toward the 160-perk target doesn't mean any individual perk is locked in; names, stat/skill requirements, rank structures, and effects are all subject to adjustment once actual design & development reaches this system, and adding more perks later may prompt revisiting ones already here (for balance, overlap, or thematic fit). Treat this whole file as a working draft, not final content.

One perk slot earned every **2 levels** — **32 total slots** across the base game (level cap: 64). **DLCs raise the cap** *(established 2026-07-03)*: each of the 6 subnet DLCs adds +5 levels (2.5 perk slots' worth on its own — see note below), and the South Pole DLC (DLC 1, Kendra Heinrich) adds +6 levels (3 perk slots). Base game + all 7 DLCs = level cap 100 = **50 total perk slots** — a clean number against the ~160-perk target roster (see `Perks.md`/`Special_Unique_Perks.md`), landing exactly on a perk-cadence boundary rather than 1 level short.

*Note on partial-DLC ownership:* since each subnet DLC adds an odd number of levels (+5), owning an odd count of subnet DLCs (1, 3, or 5 of the 6) leaves the level cap on an odd number — one level short of a full perk cycle at that specific point. Owning an even count of subnet DLCs (0, 2, 4, or 6), or the South Pole DLC alone or in any combination, always lands on an even cap. **Largely mitigated by release order** *(established 2026-07-03, see `DLC_Overview.md`)*: the South Pole DLC (DLC 1) is planned to release *last*, after all 6 subnet DLCs — so a player following release order has all 6 subnet DLCs (even, no parity issue) before Kendra's DLC ever becomes available. Only an issue for a player who deliberately skips subnet DLCs.

At each opportunity the player chooses **one** perk from the available pool. Most perks have 2–3 ranks; a rank counts as one perk choice.

**Target pool size: 160 distinct perks** (5× the 32 available slots, ensuring the player always has far more options than opportunities). Currently **101/160 designed** (63%) as of 2026-07-26, after the `Skills.md` restructure (44 skills → 25, single-stat) pushed a large batch of perks into this file — 15 genuinely new perks from the restructure's own perk candidates, plus renaming/retargeting the skill requirements on most of the perks already here. **A significant number of existing perks are now orphaned** — they still list a skill requirement referencing a former skill that became a perk in its own right (Tactical Grid Combat, Electronic Warfare, Threat Assessment, Non-Lethal Restraint & Subdual → Non-Lethal Neutralization, Improvised Weaponry & Combat Jury-Rig → Improvised Weaponry, Defensive Posturing & Endurance Fighting → Endurance Fighting, Ossuary Resonance, Sonic Attunement, Holographic Projection) or a skill cut entirely with no replacement (Subnet Optimization, Information Verification & Analysis, Data Leakage & Information Warfare, Moral Philosophy & Ethical Reasoning, Companion Command & Loyalty, Robot Religion Insight, Isolation & Psychological Resilience) — each is marked inline where it appears, left as-is pending a real design decision rather than silently guessed at. The remaining ~59 perks are marked as pending in the placeholder section at the bottom of this file.

**Target distribution: ~107 non-combat (67%) / ~53 combat (33%)**  
Currently: 65 non-combat / 36 combat. Pending perks should maintain roughly this ratio.  
Perks are primarily a system for deepening playstyle identity, not a combat improvement checklist.

Requirements use MACHINE stat abbreviations: **M** Might · **A** Agility · **C** Calculation · **H** Humanity · **I** Investigation · **N** Nerve · **E** Engine

---

## Social / Diplomatic

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Empathic Resonance** *(requirement updated 2026-07-26 — Empathy Protocols is now a distinct perk, not a skill; retargeted to Insight, the skill that actually replaced it)* | H 7, Insight 50 | 2 | Read the emotional state of any NPC; unlock compassionate dialogue options unavailable to others. Rank 2: NPCs in a receptive emotional state will share information they would normally withhold. |
| **Silver Tongue** *(requirement updated 2026-07-26 — Diplomatic Negotiation retargeted to Speech)* | H 6, Speech 40 | 2 | +20% success on non-combat persuasion checks. Rank 2: after a failed persuasion check, one retry attempt per conversation becomes available. |
| **Living Lie Detector** *(requirement updated 2026-07-26)* | I 7, Insight 50 | 1 | Always know when an NPC is lying. Choose whether to reveal this knowledge in the moment or hold it for leverage. |
| **Faction Whisperer** *(requirement updated 2026-07-26 — Faction & Reputation Management retargeted to Narrative, per the new Reputation Management perk's own mapping)* | H 7, Narrative 50 | 2 | Reputation gains with all factions are amplified. Rank 2: once per faction per playthrough, a single catastrophic reputation event can be walked back through subsequent positive actions. |
| **Cover Identity** *(requirement updated 2026-07-26 — Deception & Narrative Crafting retargeted to Deception)* | H 6, Deception 45 | 2 | Maintain a false identity within a hostile faction significantly longer before being recognized. Rank 2: plant a false record trail that actively corroborates the cover story. |
| **Moral Authority** *(requirement updated 2026-07-26 — Moral Philosophy & Ethical Reasoning was cut with no replacement skill; flagged, skill threshold dropped rather than guessed at)* | N 8 | 1 | When making a moral argument, NPCs whose Nerve falls below a threshold cannot challenge the player's position through words — they must accept it or escalate to force. |
| **Negotiator's Patience** *(requirement updated 2026-07-26)* | N 7, Speech 55 | 2 | In multi-stage dialogue encounters (summits, negotiations, interrogations), the player character can sustain their position through more pressure stages without forced concession. Rank 2: actively tire opposing parties — their position weakens with each failed stage. |
| **Ghost of the Room** *(requirement updated 2026-07-26)* | H 7, Deception 60 | 1 | If the player character witnesses an event without intervening, NPCs involved can be made to forget they were present. Powerful for intelligence gathering without commitment. |
| **Off the Record** *(added 2026-07-24, requirement updated 2026-07-26 — Faction & Reputation Management retargeted to Narrative)* | H 6, Narrative 45 | 1 | The first Reputation Matrix shift the player causes in any given district stays hidden/unregistered until a second shift in the same direction crosses it — lets a player deliberately test the waters or operate under the radar early in a district, at the cost of not being able to bank early goodwill either. |
| **Diplomat** *(added 2026-07-26, from the Skills.md restructure)* | H 8, N 7, Speech 80 | 1 | Full diplomatic authority in formal negotiations — summits, treaty talks, faction leadership meetings treat the player character as a legitimate party rather than a mere messenger or petitioner. |
| **Empathy Protocols** *(added 2026-07-26 — reuses a name freed up when the old skill of the same name was retired in favor of Insight)* | H 8, Insight 75 | 1 | Genuinely deep emotional attunement: sense not just that an NPC feels something, but the specific shape of it — grief, resentment, longing — well enough to address the real issue rather than its surface symptom. |
| **Reputation Management** *(added 2026-07-26)* | N 7, Narrative 80 | 1 | Actively author how the player character is perceived rather than just reacting to reputation as it accrues — plant a specific narrative about oneself in a district and have it actually stick and spread. |

---

## Growth / Learning *(new category, added 2026-07-04 — ported from Fallout: New Vegas)*

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Educated** | C 4 | 1 | Gain 2 additional skill points every time you level up. |
| **Swift Learner** | C 4 | 3 | Gain an additional 10% experience whenever XP is earned, per rank (up to +30% at rank 3). |
| **Comprehension** | — | 1 | Gain an additional skill point for reading a full data archive/log entry; reading a technical manual (Inner Tepenia's magazine equivalent) grants double the normal skill points. |

---

## Technical / Engineering

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Jury-Rig Virtuoso** *(requirement updated 2026-07-26 — Jury-Rigging & Repurposing folded into the new Repair skill. Note: the audit gave a single finalized "Jury-Rigging (80 Repair)" data point; kept as this existing two-rank 50/90 split instead of collapsing to one perk, since the two ranks already had distinct, well-developed effects — worth the developer's direct confirmation if a single-perk-at-80 was actually intended instead)* | A 7, M 6, Repair 50 | 2 | Repair and repurpose items using dissimilar components that normally wouldn't work together. Rank 2: perform "impossible" repairs during active crises — restoring systems others have written off. |
| **Jury-Rig Mastery** *(added 2026-07-04, ported from FNV's "Jury Rigging"; requirement updated 2026-07-26, same note as above)* | A 8, Repair 90 | 1 | Repair any item using any roughly similar item, regardless of type — true mastery-tier extension of Jury-Rig Virtuoso, no longer limited to dissimilar-but-related components. |
| **Thermal Engineer** *(renamed 2026-07-26 from "Thermal Equilibrium" — Thermal Engineering no longer exists as a skill at all; this perk now gates on Level + Calculation alone, per the Skills.md restructure)* | Level 12, C 7 | 2 | Improved heat and power allocation in managed systems; reduces collateral damage during blackouts. Rank 2: temporarily stabilize a failing grid section, buying time for a proper solution. |
| **Power Grid Management** *(renamed 2026-07-26 from "Power Conduit" to match the finalized perk name)* | Level 12, E 6, C 6 | 2 | Route emergency power through improvised pathways, unlocking unique solutions in grid quests. Rank 2: improvised bypasses persist after the player leaves the area — lasting infrastructure change. |
| **Siligel Chemist** *(requirement updated 2026-07-26 — Siligel Chemistry retargeted to the new Chemistry skill)* | Level 8, C 6, Chemistry 50 | 2 | Improved crafting and efficiency with siligel-based components. Rank 2: synthesize rare siligel compounds not available through normal commerce or salvage. |
| **Decentralized Systems** *(renamed 2026-07-26 from "Lattice Architect" — Decentralized Systems Design no longer exists as a skill; retargeted to Hacking)* | C 7, Hacking 75 | 1 | +30% effectiveness when designing or linking decentralized power nodes. Core perk for the Independent Lattice hidden path. |
| **Precision Maintenance** *(renamed 2026-07-26 from "Precision Calibration" — Precision Maintenance & Repair retargeted to the new Repair skill)* | E 7, Repair 90 | 1 | Repaired items degrade more slowly and occasionally exceed their base specifications after repair. The player character's fine motor calibration is operating at peak precision. |
| **Hydroponic Systems** *(renamed 2026-07-26 from "Hydroponic Specialist" — Hydroponic Systems no longer exists as a skill, only as this perk's own name now; requirement dropped the Engine stat per the finalized version, gating purely on the two feeder skills)* | Chemistry 50, Biology 50 | 2 | Improved yields, growth rates, and system efficiency in hydroponic operations. Rank 2: cultivate rare medicinal and chemical plants not available through any other source. |

---

## Information / Data

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Data Ghost** *(requirement updated 2026-07-26 — Arcanet Navigation & Hacking retargeted to Hacking)* | C 7, Hacking 55 | 1 | Trace signature is significantly reduced on all hacks. Passive data reads on Level 1–2 systems (C ≤4 / Hacking ≤30 requirement) have a high chance of leaving no trace at all. Active manipulation still generates a signature. Stepping stone toward Ghost in the Machine. |
| **Ghost in the Machine** *(requirement updated 2026-07-26)* | Level 24+, C 7, Hacking 90 | 1 | Any hack on a system with a Calculation requirement of 5 or below **OR** a Hacking skill requirement of 50 or below is **completely untraceable** — no log entry, no signature, no consequence. Covers all Level 0–3 systems. High-security systems (Level 4+) remain traceable even with this perk. See `Hacking_and_Traceability_System.md` for full context. |
| **Arcanet Weaver** *(requirement updated 2026-07-26)* | C 8, Hacking 60 | 2 | Hacking is faster and more reliable across all system types. Rank 2: queue multiple simultaneous operations within a single hack session. |
| **Data Archaeologist** *(renamed 2026-07-26 from "Deep Archive" — Data Archaeology no longer exists as a skill; retargeted to Cryptography at the audit's own finalized threshold (80), matching the new identity-noun perk naming convention — see `feedback_perk_naming_convention`)* | C 7, Cryptography 80 | 2 | Recover data from more severely corrupted sources than normally possible. Rank 2: recover data classified as permanently unrecoverable — pre-war records, scrubbed histories, war-era blackouts. |
| **Signal Sculptor** *(orphaned 2026-07-26 — Subnet Optimization was cut entirely, no replacement skill; left as-is pending a decision on whether this perk gets retargeted, redesigned, or retired)* | C 7, Subnet Optimization 50 | 1 | Optimize Arcanet subnets in ways that create lasting network shortcuts — bypasses and cached routes that persist across the playthrough and can be used by faction contacts. |
| **Disinformation Architect** *(orphaned 2026-07-26 — Data Leakage & Information Warfare was split apart: Data Leakage was cut entirely, and Information Warfare became a tentative Trait, not a skill. This perk's actual concept overlaps closely with that Trait's "Data Leak" action — worth reconciling the two later rather than guessing here)* | C 8, Data Leakage & Information Warfare 60 | 1 | Planted false information persists, spreads through the Arcanet, and can be used to shift faction narratives over extended time. Slow-burning social weapon. |
| **Pattern Intuition** *(orphaned 2026-07-26 — Information Verification & Analysis was cut entirely, no replacement skill)* | I 7, Information Verification & Analysis 55 | 1 | Unreliable or manipulated information sources are flagged automatically. The player character recognizes disinformation campaigns, misdirection, and planted evidence on sight. |
| **Cryptographer's Eye** *(requirement updated 2026-07-26 — Cryptography & Decryption retargeted to Cryptography)* | C 7, Cryptography 55 | 2 | Decryption is significantly faster and more reliable. Rank 2: given enough time, break encryption that is theoretically unbreakable — including pre-war military-grade ciphers. |
| **Computer Whiz** *(added 2026-07-04, ported from FNV; requirement updated 2026-07-26)* | C 7, Hacking 70 | 1 | Gain one additional attempt after failing a hack on a high-security (Level 4+) system, before the normal lockout applies. |
| **Infiltrator** *(added 2026-07-04, ported from FNV; requirement updated 2026-07-26 — "Lockpicking" was just a naming variant of the finalized "Lockpick" skill)* | I 7, Lockpick 70 | 1 | Gain one additional attempt after failing to pick a broken lock. |
| **Arcanet Navigation** *(added 2026-07-26)* | C 6, Hacking 50 | 1 | Navigate the Arcanet's subnet architecture directly and fluently — faster travel between nodes, and an instinctive sense of a subnet's layout before fully exploring it. |

---

## Survival / Exploration

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Ripple Weaver** *(requirement updated 2026-07-26 — Environmental Exploitation & Ripple Reading split apart; retargeted to Survival, the skill behind the finalized Environmental Exploitation perk, since Ripple Reading itself is still tentative/unfinalized)* | I 6, E 6, Survival 50 | 2 | Predict power grid ripples and blackouts before they happen; better salvage during fluctuations. Rank 2: exploit ripples actively as solutions to quests and puzzles — turning crises into tools. |
| **Frontier Resilience** *(requirement updated 2026-07-26 — Frontier Survival & Cold Adaptation retargeted to Outdoorsman)* | E 6, M 6, Outdoorsman 55 | 2 | Cold resistance and improved performance in Frostlands and extreme environments. Rank 2: construct and maintain modular outposts in the Frostlands — permanent field infrastructure. |
| **Undergrid Runner** *(requirement updated 2026-07-26 — Undergrid Navigation & Salvaging was cut with no replacement skill; matches the finalized perk of the same underlying concept from the Skills.md restructure)* | Level 10, A 8, I 7, E 7 | 2 | Faster movement and reduced hazard effects in the Undergrid. Rank 2: reveal hidden routes and passages visible only to the most experienced Undergrid navigators. |
| **Salvage Instinct** *(requirement updated 2026-07-26 — Scavenging & Resource Foraging retargeted to Survival)* | I 6, Survival 50 | 2 | Better quality loot from all searched containers and areas. Rank 2: detect hidden or buried containers not visible through normal inspection. |
| **Environmental Reader** *(requirement updated 2026-07-26, same reasoning as Ripple Weaver)* | I 7, Survival 60 | 1 | Gas leaks, structural collapse risk, live electrical hazards, and other environmental dangers are always visible before entering an area — and can often be weaponized rather than avoided. |
| **Hazard-Adapted Systems** *(orphaned 2026-07-26 — Hazard Navigation is now a perk in its own right rather than a skill; left as-is pending a decision on how this perk should gate instead)* | E 7, Hazard Navigation 55 | 2 | Penalties from environmental hazards (ice, collapsing tunnels, blackout zones) are significantly reduced. Rank 2: certain hazards that would stop other characters become tactical tools the player character can exploit. |
| **Isolation Protocol** *(blocked 2026-07-26 — both halves of Isolation & Psychological Resilience are still tentative/undesigned in the Skills.md restructure, not yet finalized; left as-is until those are resolved)* | N 7, Isolation & Psychological Resilience 55 | 1 | Psychological debuffs from prolonged isolation, Arcanet interference, and blackout-zone static have no effect. The player character's systems have fully adapted to operating alone. |
| **Scavenger's Luck** *(added 2026-07-04, ported from FNV's Fortune Finder/Scrounger)* | I 5 | 1 | Considerably more currency and ammunition (quantity, not quality) turn up in searched containers and stockpiles — distinct from Salvage Instinct, which improves loot quality rather than raw quantity. |
| **Frontier Survival** *(added 2026-07-26)* | E 8, N 7, Outdoorsman 75 | 1 | Thrive rather than merely survive in the Frostlands — sustained exposure carries no penalty at all, and the player character can guide others through conditions that would otherwise require dedicated survival gear. |
| **Cold Adaptation** *(added 2026-07-26)* | E 7, N 6, Outdoorsman 50 | 1 | Meaningfully reduced cold-exposure penalties outside protected districts — a real edge in the Frostlands without yet being fully at home there. |
| **Environmental Exploitation** *(added 2026-07-26)* | E 6, I 7, Survival 50 | 1 | Actively turn hazardous conditions — ripples, blackouts, structural instability — into tools and opportunities rather than just surviving them. |
| **Scavenger** *(added 2026-07-26, akin to Fallout's "Scrounger")* | I 7, Survival 50 | 1 | Find what everyone else missed — hidden or buried caches in places already searched by other scavengers, in locations nobody else thought to check. |
| **Hazard Navigation** *(added 2026-07-26)* | A 8 ||OR|| I 8; Survival 50 ||OR|| Athletics 75 ||OR|| Acrobatics 75 | 1 | Move through ice, collapsing tunnels, and blackout zones with genuine confidence rather than just tolerance — reachable through a physical-endurance build, an analytical/investigative build, or an agility-and-finesse build alike. |

---

## Cultural / Philosophical

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Goth Adept** *(orphaned 2026-07-26 — Ossuary Resonance is now a perk in its own right rather than a skill; left as-is pending a decision on how this perk should gate instead)* | H 6, Ossuary Resonance 50 | 2 | Deep understanding of Goth death-ritual culture — unique dialogue options with Goth NPCs and access to rituals normally closed to outsiders. Rank 2: unlock Goth-exclusive questlines and participate in closed ceremonies. |
| **Sonic Initiate** *(orphaned 2026-07-26 — same issue: Sonic Attunement is now a quest-gated perk, not a skill)* | A 6, H 6, Sonic Attunement 50 | 2 | Resonance with Cymaticist sonic practices — unique interactions with sound-based technology and Cymaticist communities. Rank 2: use sonic technology in ways only trained Cymaticists can, including Cymaticist-locked equipment. |
| **AI Diplomat** *(orphaned 2026-07-26 — same issue: Holographic Projection is now a perk, not a skill)* | C 7, H 6, Holographic Projection & AI Interaction 55 | 1 | Negotiate with advanced AIs as social equals rather than as users issuing commands. Opens unique dialogue trees with AI characters entirely unavailable through other means. |
| **Robot Theologian** *(requirement updated 2026-07-26 — Robot Religion Insight was cut entirely as a former Specialized/Cultural skill, with no perk or skill replacement at all; skill threshold dropped rather than guessed at)* | H 7 | 1 | Mediate conflicts between robot religious sects with genuine authority. Opens unique questlines tied to robot spiritual practices across multiple districts, and unlocks religious dialogue branches in major quests. |
| **Ossuary Resonance** *(added 2026-07-26)* | Level 16, H 7, N 7 | 1 | A genuine, unlearned attunement to Goth death-ritual practice — not studied from the outside, but felt the way an initiate feels it. Distinct from Goth Adept above, which is knowledge acquired through study rather than something innate. |
| **Sonic Attunement** *(added 2026-07-26, quest-gated — completion of the relevant questline is the gate itself, no stat/skill threshold needed on top)* | Quest-gated | 1 | Full Cymaticist sonic-practice standing, earned through the questline itself rather than through stat investment. |
| **Golden Eye Calibration** *(added 2026-07-26, quest-gated)* | Quest-gated | 1 | *(Effect not yet designed — carried over from the Skills.md restructure as a placeholder quest-gated perk.)* |
| **Holographic Projection** *(added 2026-07-26)* | C 7 ||OR|| N 8, E 8; Hacking 60 ||OR|| Sleight of Hand 100 | 1 | Use a data network to project a "decoy" version of oneself elsewhere — the decoy can't manipulate anything; its only function is distraction. Reachable through a hacker's build (Calculation + Hacking) or a con-artist's build (Nerve + Engine + Sleight of Hand) alike. |

---

## Economic / Resource

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Black Market Fluency** | I 6, Pisces reputation (moderate) | 2 | Better prices, access, and selection in black market contexts across all districts. Rank 2: acquire items listed as unavailable, destroyed, or restricted — if someone in Concordia has it, it can be found. |
| **Resource Recovery** *(requirement updated 2026-07-26 — Scavenging & Resource Foraging retargeted to Survival)* | E 6, Survival 50 | 2 | Components used in crafting have a chance to partially return. Rank 2: return rate improves significantly; high-Engine characters recover nearly half of all consumed materials. |
| **Siligel Economy** *(requirement updated 2026-07-26 — Siligel Chemistry retargeted to Chemistry)* | E 8, Chemistry 55 | 1 | All siligel consumption rates permanently reduced. Represents deep systemic self-optimization of the player character's internal processes — something that cannot be undone. |
| **Strong Back** *(added 2026-07-04, ported from FNV)* | M 5, E 5 | 1 | +50 carry weight. |

---

## Companion / Leadership

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Companion Cohesion** *(requirement updated 2026-07-26 — Companion Command & Loyalty was cut entirely as a skill, with no direct replacement; skill threshold dropped rather than guessed at)* | N 7, H 6 | 2 | Companions perform significantly better in combat and exploration when near the player character. Rank 2: enables two companions to be active simultaneously, where the normal limit is one. |
| **Trusted Command** *(requirement updated 2026-07-26, same reasoning)* | N 8 | 1 | Every companion's crisis behavior improves by one tier permanently — companions who would flee hold position; companions who hold position push harder. |
| **Shared Experience** *(requirement updated 2026-07-26, same reasoning)* | H 7 | 1 | The active companion gains skill points in their primary skill category every time the player character levels up. Long-term investment in a specific companion pays off mechanically. |
| **[NAME PENDING — Companion Command & Loyalty]** *(added 2026-07-26 from the Skills.md restructure; deliberately NOT using that exact name as a permanent title, since it's the same name as the skill just retired above — flagged in the audit itself as \[to-be-renamed\])* | N 7, H 7 | 1 | Direct, effective command presence over a companion in the field — the kind of leadership that gets followed without needing to be Trusted Command's deeper, earned loyalty first. |
| **Bond Ledger** *(added 2026-07-24, marked for possible future renaming — mutually exclusive with Grief Ledger; requirement updated 2026-07-26, same Companion Command & Loyalty issue as the three perks above)* | H 6 | 1 | Repeated re-specs with a companion present accumulate Bond faster on the Fragmentation Matrix. Builds toward the deeper companion tiers (up to The Long Vigil) more readily, at the cost of slower Grief accumulation — a build that leans into closeness over catharsis. |
| **Grief Ledger** *(added 2026-07-24, marked for possible future renaming — mutually exclusive with Bond Ledger; requirement updated 2026-07-26, same issue)* | N 6 | 1 | Repeated re-specs with a companion present accumulate Grief faster on the Fragmentation Matrix, but each individual re-spec's Grief cost to the player character is reduced. A build that leans into processing change quickly over building steady closeness. |

---

## Combat — Offensive

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Rapid Fire Protocols** *(orphaned 2026-07-26 — Tactical Grid Combat is now a perk in its own right rather than a skill; left as-is pending a decision on how these five Tactical-Grid-Combat-gated perks should gate instead)* | A 7, Tactical Grid Combat 50 | 2 | Basic attacks cost 1 fewer AP (minimum 3 AP per attack). Rank 2: the first attack of each turn costs 1 additional AP less — the opening shot is always efficient. |
| **Precision Strike** *(orphaned 2026-07-26, same issue)* | N 6, I 6, Tactical Grid Combat 50 | 2 | Aimed and special attacks cost 1 fewer AP. Rank 2: also gain +10% accuracy on all aimed attacks. |
| **Grim Reaper Protocols** | M 6, A 6 | 1 | Killing an enemy in combat refunds 3 AP, once per turn. Rewards aggressive, decisive play. |
| **Improvised Lethality** *(orphaned 2026-07-26 — Improvised Weaponry & Combat Jury-Rig is now a perk, not a skill)* | M 7, Improvised Weaponry & Combat Jury-Rig 55 | 2 | Improvised weapons deal significantly more damage. Rank 2: construct improvised weapons mid-combat at no AP cost — turn the environment into an arsenal. |
| **Power Strike** *(orphaned 2026-07-26 — Non-Lethal Restraint & Subdual is now the perk Non-Lethal Neutralization, not a skill)* | M 8, Non-Lethal Restraint & Subdual 50 | 1 | Every fourth consecutive melee attack in an engagement triggers an automatic knockdown, regardless of target size or armor type. |
| **Electronic Disruptor** *(orphaned 2026-07-26 — Electronic Warfare is now a perk, not a skill)* | C 7, Electronic Warfare 55 | 2 | EMP and electronic attacks have higher success rates and longer effect durations. Rank 2: a successful electronic attack can chain disruption to one adjacent electronic target at no additional cost. |
| **Overclocked Aggression** | E 8, M 7 | 1 | Once per combat: sacrifice maximum AP on the next turn to gain +4 temporary AP on the current turn. High-risk burst option. |
| **Crusher** *(added 2026-07-26, marked for possible future renaming)* | Level 26, M 7, N 6, E 7 | 2 | Rank 1: Power Attacks (`Combat/Power_Attacks.md`) deal +20% damage, and their vulnerability window is mitigated by 10 points — the base -20% DT/-20% DR penalty becomes -10% DT/-10% DR for one turn. Rank 2: Power Attacks deal +30% damage, and the mitigation rises to 20 points — fully canceling the base penalty, leaving no DT/DR penalty at all. |
| **Steady Retrieval** *(added 2026-07-24, orphaned 2026-07-26 — same Improvised Weaponry & Combat Jury-Rig issue as Improvised Lethality above)* | A 6, Improvised Weaponry & Combat Jury-Rig 45 | 2 | Retrieving a thrown weapon that's stuck where it landed costs 1 fewer AP. Rank 2: thrown weapons can also be thrown 1 additional grid step farther before retrieval range becomes an issue. Direct hook into the game's own thrown-weapon retrieval rule. |
| **Non-Lethal Neutralization** *(added 2026-07-26)* | M 8, A 6 ||OR|| H 7, N 7 | 1 | Reliably take an enemy down without killing them, reachable through a physical-control build (Might + Agility) or a de-escalation build (Humanity + Nerve) alike. |
| **Improvised Weaponry** *(added 2026-07-26)* | M 6, A 6, C 7 | 1 | Turn whatever's at hand — pipes, tools, debris — into a genuinely effective weapon, on the fly, without dedicated equipment. |
| **Endurance Fighting** *(added 2026-07-26 — distinct from the existing, now-orphaned "Endurance Fighter" perk below)* | M 10 ||OR|| A 7, N 7, E 7 | 1 | Keep fighting effectively well past the point that would stop most combatants, reachable through raw physical toughness alone or through a balanced agility/composure/systems build. |
| **Tactical Grid Combat** *(added 2026-07-26)* | A 8, C 7 | 1 | Read and exploit the tactical grid itself — positioning, cover, and movement options resolve faster and more precisely than for a combatant relying on instinct alone. |
| **Electronic Warfare** *(added 2026-07-26)* | C 8, I 7 | 1 | Direct, reliable disruption of enemy electronics and robotic systems in the field, beyond what any single Electronic Disruptor-style trick can manage on its own. |
| **Threat Assessment** *(added 2026-07-26)* | I 8, N 7 | 1 | Accurately read a combat encounter's real danger level before it starts — not just who's hostile, but who's actually dangerous. |

---

## Combat — Defensive

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Reactive Shielding** *(orphaned 2026-07-26 — Defensive Posturing & Endurance Fighting is now the perk Endurance Fighting, not a skill)* | E 7, Defensive Posturing & Endurance Fighting 50 | 2 | When taking heavy damage, automatic partial absorption triggers. Rank 2: can trigger once per AP cycle rather than once per combat. |
| **Endurance Fighter** *(orphaned 2026-07-26, same issue — note the near-name-collision with the new Endurance Fighting perk added below in Combat — Offensive, which is a distinct perk)* | M 7, N 7, Defensive Posturing & Endurance Fighting 55 | 1 | AP penalties from taking damage don't apply until health drops below 25%, rather than at the normal threshold. |
| **Combat Awareness** *(orphaned 2026-07-26 — Threat Assessment is now a perk, not a skill)* | I 6, Threat Assessment 50 | 2 | Before combat begins, identify which enemies will act first and approximate their damage potential. Rank 2: detects ambushes before they trigger, converting a surprise attack into a normal initiative sequence. |
| **Armor Integrity** | E 7, M 6 | 2 | Equipped armor degrades significantly more slowly in extended engagements. Rank 2: armor damage heals partially between combats, reducing maintenance burden on long expeditions. |
| **Last System Standing** | N 9, E 7 | 1 | Once per combat, when health would reach zero, survive at 1 HP and immediately gain 2 AP for an emergency action. The player character refuses to go offline. |
| **Toughness** *(added 2026-07-04, ported from FNV)* | E 5 | 2 | +3 permanent damage resistance per rank. |
| **Life Giver** *(added 2026-07-04, ported from FNV)* | E 6 | 1 | +30 maximum health. |
| **Nerves of Steel** *(added 2026-07-04, ported from FNV — reworked, see note below)* | E 7 | 1 | Up to 2 unused AP at the end of your turn carry over into your next turn instead of being discarded (does not stack beyond 2 banked AP at a time). *(Provisional — flagged for developer review: FNV's original effect, "20% faster AP regeneration," doesn't map onto Inner Tepenia's turn-based AP model, since AP doesn't regenerate mid-turn and unused AP is discarded by the base rule rather than continuously refilling. This reworks it as the first implementation of the AP-banking idea already flagged, undesigned, in `Core-Mechanics/Action_Points_Perks_and_Traits.md`. Gated on Engine since Engine is already defined as the recovery-speed/AP-replenishment stat.)* |

---

## Combat — NODE / Targeting

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Processing Overdrive** *(orphaned 2026-07-26, same Tactical Grid Combat issue as the Combat — Offensive perks above)* | C 7, Tactical Grid Combat 50 | 2 | NODE analysis window is extended. Rank 2: one additional shot can be queued per NODE activation. |
| **Weak Point Specialist** *(orphaned 2026-07-26, same issue)* | I 7, Tactical Grid Combat 55 | 2 | Scanned weak points display estimated damage and likely secondary effects before the shot is committed. Rank 2: targeting a scanned weak point costs 1 fewer AP. |
| **Cascade Protocol** | N 8, C 7 | 1 | Critical hits on robot enemies have a significantly higher chance to trigger cascade failures. A cascade can spread from the struck component to one adjacent system. |
| **Predictive Algorithms** | C 8, I 7 | 1 | In NODE mode, moving targets display projected positions. Accuracy penalties for targeting moving enemies are halved. |
| **Focus Under Fire** *(orphaned 2026-07-26, same issue)* | N 7, Tactical Grid Combat 45 | 2 | Taking damage during NODE activation drains Nerve at a reduced rate. Rank 2: taking damage during NODE no longer drains Nerve at all — the player character's focus is unbreakable. |
| **Perimeter Awareness** *(added 2026-07-04, ported from FNV's Alertness)* | I 6 | 1 | While stationary and not moved this turn, gain a bonus to targeting accuracy in NODE mode equivalent to +2 Investigation. |
| **Math Wrath** *(added 2026-07-26, ported directly from FNV — verified against the real perk: Level 10, Science 70, "reduces all V.A.T.S. AP costs by 10%," no other effect; requirement updated 2026-07-26 — Arcanet Navigation & Hacking retargeted to Hacking)* | Hacking 70 | 1 | All NODE-mode attacks cost 10% less AP. |

---

## Combat — Hybrid / Specialized

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Non-Lethal Specialist** *(orphaned 2026-07-26 — Non-Lethal Restraint & Subdual is now the perk Non-Lethal Neutralization, not a skill)* | A 6, M 6, Non-Lethal Restraint & Subdual 50 | 2 | Subdual options are faster and more reliable; non-lethal takedowns leave targets incapacitated longer. Rank 2: perform non-lethal takedowns on enemy types that are normally immune to subdual. |
| **Field Repair Protocols** *(requirement updated 2026-07-26 — Precision Maintenance & Repair retargeted to Repair)* | E 6, Repair 50 | 2 | Perform emergency self-repair during combat using components in inventory — no workbench needed. Rank 2: can also repair companions mid-combat without spending additional AP. |
| **Threat Exploitation** *(orphaned 2026-07-26 — Threat Assessment is now a perk, not a skill)* | I 7, Threat Assessment 55 | 1 | After successfully assessing a threat before combat, the first attack on that target is guaranteed to hit regardless of other modifiers. Preparation pays. |
| **Robotics Expert** *(added 2026-07-04, ported from FNV; orphaned 2026-07-26, same Threat Assessment issue)* | C 6, Threat Assessment 50 | 1 | +25% damage against robot enemies. Non-alerted robots can be shut down (rather than killed) by sneaking up and deactivating them directly. |
| **Silent Running** *(added 2026-07-04, ported from FNV; requirement updated 2026-07-26 — Stealth & Infiltration retargeted to Sneak)* | A 6, Sneak 50 | 1 | Running no longer breaks stealth or interrupts a sneak attempt. |
| **Quick Draw** *(added 2026-07-04, ported from FNV — reworked for turn-based AP, per the user's own design)* | A 5 | 1 | Drawing or holstering a weapon in combat costs no AP. *(FNV's original effect, "50% faster equip/holster," is a real-time animation-speed mechanic that doesn't translate to a discrete per-action AP cost — this reworks the same intent, removing weapon-switching as a tactical burden, into an AP-cost term instead.)* |

---

## Perk Count by Category

*(Updated 2026-07-26 after the `Skills.md` restructure — see the intro note above regarding orphaned perks. Previously updated 2026-07-24 — Off the Record, Bond Ledger, Grief Ledger, Steady Retrieval — and 2026-07-04 after adding 15 Fallout-adapted perks — see `project_fallout_trait_perk_adaptation` memory.)*

| Category | Count | Type |
|----------|-------|------|
| Social / Diplomatic | 12 | Non-combat |
| Growth / Learning | 3 | Non-combat |
| Technical / Engineering | 8 | Non-combat |
| Information / Data | 11 | Non-combat |
| Survival / Exploration | 13 | Non-combat |
| Cultural / Philosophical | 8 | Non-combat |
| Economic / Resource | 4 | Non-combat |
| Companion / Leadership | 6 | Non-combat |
| **Non-combat subtotal** | **65** | **64%** |
| Combat — Offensive | 15 | Combat |
| Combat — Defensive | 8 | Combat |
| Combat — NODE / Targeting | 7 | Combat |
| Combat — Hybrid / Specialized | 6 | Combat |
| **Combat subtotal** | **36** | **36%** |
| **Total** | **101** | |

Expansion in future design passes should maintain roughly this non-combat to combat ratio. DLC perks may skew toward the DLC's thematic focus, but the aggregate ratio across base game + all DLC should remain non-combat dominant.

---

## Pending Perks — Placeholders (~59 remaining to reach 160 target)

*(Updated 2026-07-26 after the `Skills.md` restructure pushed the designed count from 82 to 101. Previously updated 2026-07-04 after the Fallout-adapted perk batch — see `project_fallout_trait_perk_adaptation` memory.)*

The categories below indicate where additional perks are needed. Names and effects are to be designed during dedicated perk design passes. Rough targets per category to reach the 160 total at the correct ratio:

### Non-combat (need ~42 more to reach ~107 total)

| Category | Currently designed | Still needed |
|----------|-------------------|-------------|
| Social / Diplomatic | 12 | ~6 more |
| Growth / Learning | 3 | ~6 more |
| Technical / Engineering | 8 | ~10 more |
| Information / Data | 11 | ~5 more |
| Survival / Exploration | 13 | ~3 more |
| Cultural / Philosophical | 8 | ~4 more |
| Economic / Resource | 4 | ~6 more |
| Companion / Leadership | 6 | ~4 more |

### Combat (need ~17 more to reach ~53 total)

| Category | Currently designed | Still needed |
|----------|-------------------|-------------|
| Combat — Offensive | 15 | ~0 more (already over target — fine, not a problem) |
| Combat — Defensive | 8 | ~5 more |
| Combat — NODE / Targeting | 7 | ~6 more |
| Combat — Hybrid / Specialized | 6 | ~6 more |

**Design note for future passes**: When adding perks, prioritize filling underrepresented categories first (Cultural/Philosophical, Companion/Leadership, Growth/Learning) before adding more to already-robust categories (Technical, Information/Data, Social). New non-combat categories not yet invented are still encouraged — the world of Inner Tepenia has enough distinct systems to support them.

**Before adding more perks, resolve the orphaned-perk backlog from the 2026-07-26 restructure first** (see the intro note and every perk marked *orphaned*/*blocked* inline above) — retargeting those to a real gate matters more than growing the raw count further.
