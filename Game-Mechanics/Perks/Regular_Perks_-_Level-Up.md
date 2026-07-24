# Regular Perks (Level-Up)

**Marked for future review (2026-07-04):** every perk in this file — old and newly added alike — is provisional. Progress toward the 160-perk target doesn't mean any individual perk is locked in; names, stat/skill requirements, rank structures, and effects are all subject to adjustment once actual design & development reaches this system, and adding more perks later may prompt revisiting ones already here (for balance, overlap, or thematic fit). Treat this whole file as a working draft, not final content.

One perk slot earned every **2 levels** — **32 total slots** across the base game (level cap: 64). **DLCs raise the cap** *(established 2026-07-03)*: each of the 6 subnet DLCs adds +5 levels (2.5 perk slots' worth on its own — see note below), and the South Pole DLC (DLC 1, Kendra Heinrich) adds +6 levels (3 perk slots). Base game + all 7 DLCs = level cap 100 = **50 total perk slots** — a clean number against the ~160-perk target roster (see `Perks.md`/`Special_Unique_Perks.md`), landing exactly on a perk-cadence boundary rather than 1 level short.

*Note on partial-DLC ownership:* since each subnet DLC adds an odd number of levels (+5), owning an odd count of subnet DLCs (1, 3, or 5 of the 6) leaves the level cap on an odd number — one level short of a full perk cycle at that specific point. Owning an even count of subnet DLCs (0, 2, 4, or 6), or the South Pole DLC alone or in any combination, always lands on an even cap. **Largely mitigated by release order** *(established 2026-07-03, see `DLC_Overview.md`)*: the South Pole DLC (DLC 1) is planned to release *last*, after all 6 subnet DLCs — so a player following release order has all 6 subnet DLCs (even, no parity issue) before Kendra's DLC ever becomes available. Only an issue for a player who deliberately skips subnet DLCs.

At each opportunity the player chooses **one** perk from the available pool. Most perks have 2–3 ranks; a rank counts as one perk choice.

**Target pool size: 160 distinct perks** (5× the 32 available slots, ensuring the player always has far more options than opportunities). Currently **80/160 designed** (50%) as of 2026-07-24, after adding 15 perks ported/adapted from Fallout: New Vegas following a comparison pass (see `project_fallout_trait_perk_adaptation` memory), plus 4 more (Off the Record, Bond Ledger, Grief Ledger, Steady Retrieval — all marked for possible future renaming) tied to systems designed after that pass (the Reputation Matrix, the Fragmentation Matrix, and the thrown-weapon retrieval rule). The remaining ~80 perks are marked as pending in the placeholder section at the bottom of this file.

**Target distribution: ~107 non-combat (67%) / ~53 combat (33%)**  
Currently: 52 non-combat / 28 combat. Pending perks should maintain roughly this ratio.  
Perks are primarily a system for deepening playstyle identity, not a combat improvement checklist.

Requirements use MACHINE stat abbreviations: **M** Might · **A** Agility · **C** Calculation · **H** Humanity · **I** Investigation · **N** Nerve · **E** Engine

---

## Social / Diplomatic

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Empathic Resonance** | H 7, Empathy Protocols 50 | 2 | Read the emotional state of any NPC; unlock compassionate dialogue options unavailable to others. Rank 2: NPCs in a receptive emotional state will share information they would normally withhold. |
| **Silver Tongue** | H 6, Diplomatic Negotiation 40 | 2 | +20% success on non-combat persuasion checks. Rank 2: after a failed persuasion check, one retry attempt per conversation becomes available. |
| **Living Lie Detector** | I 7, Empathy Protocols 50 | 1 | Always know when an NPC is lying. Choose whether to reveal this knowledge in the moment or hold it for leverage. |
| **Faction Whisperer** | H 7, Faction & Reputation Management 50 | 2 | Reputation gains with all factions are amplified. Rank 2: once per faction per playthrough, a single catastrophic reputation event can be walked back through subsequent positive actions. |
| **Cover Identity** | H 6, Deception & Narrative Crafting 45 | 2 | Maintain a false identity within a hostile faction significantly longer before being recognized. Rank 2: plant a false record trail that actively corroborates the cover story. |
| **Moral Authority** | N 8, Moral Philosophy & Ethical Reasoning 60 | 1 | When making a moral argument, NPCs whose Nerve falls below a threshold cannot challenge the player's position through words — they must accept it or escalate to force. |
| **Negotiator's Patience** | N 7, Diplomatic Negotiation 55 | 2 | In multi-stage dialogue encounters (summits, negotiations, interrogations), the player character can sustain their position through more pressure stages without forced concession. Rank 2: actively tire opposing parties — their position weakens with each failed stage. |
| **Ghost of the Room** | H 7, Deception & Narrative Crafting 60 | 1 | If the player character witnesses an event without intervening, NPCs involved can be made to forget they were present. Powerful for intelligence gathering without commitment. |
| **Off the Record** *(added 2026-07-24, marked for possible future renaming)* | H 6, Faction & Reputation Management 45 | 1 | The first Reputation Matrix shift the player causes in any given district stays hidden/unregistered until a second shift in the same direction crosses it — lets a player deliberately test the waters or operate under the radar early in a district, at the cost of not being able to bank early goodwill either. |

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
| **Jury-Rig Virtuoso** | A 7, M 6, Jury-Rigging & Repurposing 50 | 2 | Repair and repurpose items using dissimilar components that normally wouldn't work together. Rank 2: perform "impossible" repairs during active crises — restoring systems others have written off. |
| **Jury-Rig Mastery** *(added 2026-07-04, ported from FNV's "Jury Rigging")* | A 8, Jury-Rigging & Repurposing 90 | 1 | Repair any item using any roughly similar item, regardless of type — true mastery-tier extension of Jury-Rig Virtuoso, no longer limited to dissimilar-but-related components. |
| **Thermal Equilibrium** | E 7, Thermal Engineering 40 | 2 | Improved heat and power allocation in managed systems; reduces collateral damage during blackouts. Rank 2: temporarily stabilize a failing grid section, buying time for a proper solution. |
| **Power Conduit** | E 7, Power Grid Management 55 | 2 | Route emergency power through improvised pathways, unlocking unique solutions in grid quests. Rank 2: improvised bypasses persist after the player leaves the area — lasting infrastructure change. |
| **Siligel Chemist** | C 7, Siligel Chemistry 50 | 2 | Improved crafting and efficiency with siligel-based components. Rank 2: synthesize rare siligel compounds not available through normal commerce or salvage. |
| **Lattice Architect** | C 7, E 6, Decentralized Systems Design 60 | 1 | +30% effectiveness when designing or linking decentralized power nodes. Core perk for the Independent Lattice hidden path. |
| **Precision Calibration** | A 8, Precision Maintenance & Repair 60 | 1 | Repaired items degrade more slowly and occasionally exceed their base specifications after repair. The player character's fine motor calibration is operating at peak precision. |
| **Hydroponic Specialist** | E 6, Hydroponic Systems 50 | 2 | Improved yields, growth rates, and system efficiency in hydroponic operations. Rank 2: cultivate rare medicinal and chemical plants not available through any other source. |
| **Transit Authority** | A 6, E 6, Highway Maintenance & Transit Systems 50 | 2 | Faster inter-district travel; discover hidden and unmaintained transit routes. Rank 2: restore critical transit systems in ways that open new permanent fast-travel options. |

---

## Information / Data

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Data Ghost** | C 7, Arcanet Navigation & Hacking 55 | 1 | Trace signature is significantly reduced on all hacks. Passive data reads on Level 1–2 systems (C ≤4 / Hacking ≤30 requirement) have a high chance of leaving no trace at all. Active manipulation still generates a signature. Stepping stone toward Ghost in the Machine. |
| **Ghost in the Machine** | Level 24+, C 7, Arcanet Navigation & Hacking 90 | 1 | Any hack on a system with a Calculation requirement of 5 or below **OR** a Hacking skill requirement of 50 or below is **completely untraceable** — no log entry, no signature, no consequence. Covers all Level 0–3 systems. High-security systems (Level 4+) remain traceable even with this perk. See `Hacking_and_Traceability_System.md` for full context. |
| **Arcanet Weaver** | C 8, Arcanet Navigation & Hacking 60 | 2 | Hacking is faster and more reliable across all system types. Rank 2: queue multiple simultaneous operations within a single hack session. |
| **Deep Archive** | C 7, Data Archaeology 55 | 2 | Recover data from more severely corrupted sources than normally possible. Rank 2: recover data classified as permanently unrecoverable — pre-war records, scrubbed histories, war-era blackouts. |
| **Signal Sculptor** | C 7, Subnet Optimization 50 | 1 | Optimize Arcanet subnets in ways that create lasting network shortcuts — bypasses and cached routes that persist across the playthrough and can be used by faction contacts. |
| **Disinformation Architect** | C 8, Data Leakage & Information Warfare 60 | 1 | Planted false information persists, spreads through the Arcanet, and can be used to shift faction narratives over extended time. Slow-burning social weapon. |
| **Pattern Intuition** | I 7, Information Verification & Analysis 55 | 1 | Unreliable or manipulated information sources are flagged automatically. The player character recognizes disinformation campaigns, misdirection, and planted evidence on sight. |
| **Cryptographer's Eye** | C 7, Cryptography & Decryption 55 | 2 | Decryption is significantly faster and more reliable. Rank 2: given enough time, break encryption that is theoretically unbreakable — including pre-war military-grade ciphers. |
| **Computer Whiz** *(added 2026-07-04, ported from FNV)* | C 7, Arcanet Navigation & Hacking 70 | 1 | Gain one additional attempt after failing a hack on a high-security (Level 4+) system, before the normal lockout applies. |
| **Infiltrator** *(added 2026-07-04, ported from FNV)* | I 7, Lockpicking 70 | 1 | Gain one additional attempt after failing to pick a broken lock. |

---

## Survival / Exploration

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Ripple Weaver** | I 6, E 6, Environmental Exploitation & Ripple Reading 50 | 2 | Predict power grid ripples and blackouts before they happen; better salvage during fluctuations. Rank 2: exploit ripples actively as solutions to quests and puzzles — turning crises into tools. |
| **Frontier Resilience** | E 6, M 6, Frontier Survival & Cold Adaptation 55 | 2 | Cold resistance and improved performance in Frostlands and extreme environments. Rank 2: construct and maintain modular outposts in the Frostlands — permanent field infrastructure. |
| **Undergrid Runner** | A 6, E 5, Undergrid Navigation & Salvaging 45 | 2 | Faster movement and reduced hazard effects in the Undergrid. Rank 2: reveal hidden routes and passages visible only to the most experienced Undergrid navigators. |
| **Salvage Instinct** | I 6, Scavenging & Resource Foraging 50 | 2 | Better quality loot from all searched containers and areas. Rank 2: detect hidden or buried containers not visible through normal inspection. |
| **Environmental Reader** | I 7, Environmental Exploitation & Ripple Reading 60 | 1 | Gas leaks, structural collapse risk, live electrical hazards, and other environmental dangers are always visible before entering an area — and can often be weaponized rather than avoided. |
| **Hazard-Adapted Systems** | E 7, Hazard Navigation 55 | 2 | Penalties from environmental hazards (ice, collapsing tunnels, blackout zones) are significantly reduced. Rank 2: certain hazards that would stop other characters become tactical tools the player character can exploit. |
| **Isolation Protocol** | N 7, Isolation & Psychological Resilience 55 | 1 | Psychological debuffs from prolonged isolation, Arcanet interference, and blackout-zone static have no effect. The player character's systems have fully adapted to operating alone. |
| **Scavenger's Luck** *(added 2026-07-04, ported from FNV's Fortune Finder/Scrounger)* | I 5 | 1 | Considerably more currency and ammunition (quantity, not quality) turn up in searched containers and stockpiles — distinct from Salvage Instinct, which improves loot quality rather than raw quantity. |

---

## Cultural / Philosophical

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Goth Adept** | H 6, Ossuary Resonance 50 | 2 | Deep understanding of Goth death-ritual culture — unique dialogue options with Goth NPCs and access to rituals normally closed to outsiders. Rank 2: unlock Goth-exclusive questlines and participate in closed ceremonies. |
| **Sonic Initiate** | A 6, H 6, Sonic Attunement 50 | 2 | Resonance with Cymaticist sonic practices — unique interactions with sound-based technology and Cymaticist communities. Rank 2: use sonic technology in ways only trained Cymaticists can, including Cymaticist-locked equipment. |
| **AI Diplomat** | C 7, H 6, Holographic Projection & AI Interaction 55 | 1 | Negotiate with advanced AIs as social equals rather than as users issuing commands. Opens unique dialogue trees with AI characters entirely unavailable through other means. |
| **Robot Theologian** | H 7, Robot Religion Insight 60 | 1 | Mediate conflicts between robot religious sects with genuine authority. Opens unique questlines tied to robot spiritual practices across multiple districts, and unlocks religious dialogue branches in major quests. |

---

## Economic / Resource

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Black Market Fluency** | I 6, Pisces reputation (moderate) | 2 | Better prices, access, and selection in black market contexts across all districts. Rank 2: acquire items listed as unavailable, destroyed, or restricted — if someone in Concordia has it, it can be found. |
| **Resource Recovery** | E 6, Scavenging & Resource Foraging 50 | 2 | Components used in crafting have a chance to partially return. Rank 2: return rate improves significantly; high-Engine characters recover nearly half of all consumed materials. |
| **Siligel Economy** | E 8, Siligel Chemistry 55 | 1 | All siligel consumption rates permanently reduced. Represents deep systemic self-optimization of the player character's internal processes — something that cannot be undone. |
| **Strong Back** *(added 2026-07-04, ported from FNV)* | M 5, E 5 | 1 | +50 carry weight. |

---

## Companion / Leadership

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Companion Cohesion** | N 7, H 6, Companion Command & Loyalty 50 | 2 | Companions perform significantly better in combat and exploration when near the player character. Rank 2: enables two companions to be active simultaneously, where the normal limit is one. |
| **Trusted Command** | N 8, Companion Command & Loyalty 60 | 1 | Every companion's crisis behavior improves by one tier permanently — companions who would flee hold position; companions who hold position push harder. |
| **Shared Experience** | H 7, Companion Command & Loyalty 55 | 1 | The active companion gains skill points in their primary skill category every time the player character levels up. Long-term investment in a specific companion pays off mechanically. |
| **Bond Ledger** *(added 2026-07-24, marked for possible future renaming — mutually exclusive with Grief Ledger)* | H 6, Companion Command & Loyalty 40 | 1 | Repeated re-specs with a companion present accumulate Bond faster on the Fragmentation Matrix. Builds toward the deeper companion tiers (up to The Long Vigil) more readily, at the cost of slower Grief accumulation — a build that leans into closeness over catharsis. |
| **Grief Ledger** *(added 2026-07-24, marked for possible future renaming — mutually exclusive with Bond Ledger)* | N 6, Companion Command & Loyalty 40 | 1 | Repeated re-specs with a companion present accumulate Grief faster on the Fragmentation Matrix, but each individual re-spec's Grief cost to the player character is reduced. A build that leans into processing change quickly over building steady closeness. |

---

## Combat — Offensive

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Rapid Fire Protocols** | A 7, Tactical Grid Combat 50 | 2 | Basic attacks cost 1 fewer AP (minimum 3 AP per attack). Rank 2: the first attack of each turn costs 1 additional AP less — the opening shot is always efficient. |
| **Precision Strike** | N 6, I 6, Tactical Grid Combat 50 | 2 | Aimed and special attacks cost 1 fewer AP. Rank 2: also gain +10% accuracy on all aimed attacks. |
| **Grim Reaper Protocols** | M 6, A 6 | 1 | Killing an enemy in combat refunds 3 AP, once per turn. Rewards aggressive, decisive play. |
| **Improvised Lethality** | M 7, Improvised Weaponry & Combat Jury-Rig 55 | 2 | Improvised weapons deal significantly more damage. Rank 2: construct improvised weapons mid-combat at no AP cost — turn the environment into an arsenal. |
| **Power Strike** | M 8, Non-Lethal Restraint & Subdual 50 | 1 | Every fourth consecutive melee attack in an engagement triggers an automatic knockdown, regardless of target size or armor type. |
| **Electronic Disruptor** | C 7, Electronic Warfare 55 | 2 | EMP and electronic attacks have higher success rates and longer effect durations. Rank 2: a successful electronic attack can chain disruption to one adjacent electronic target at no additional cost. |
| **Overclocked Aggression** | E 8, M 7 | 1 | Once per combat: sacrifice maximum AP on the next turn to gain +4 temporary AP on the current turn. High-risk burst option. |
| **Steady Retrieval** *(added 2026-07-24, marked for possible future renaming)* | A 6, Improvised Weaponry & Combat Jury-Rig 45 | 2 | Retrieving a thrown weapon that's stuck where it landed costs 1 fewer AP. Rank 2: thrown weapons can also be thrown 1 additional grid step farther before retrieval range becomes an issue. Direct hook into the game's own thrown-weapon retrieval rule. |

---

## Combat — Defensive

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Reactive Shielding** | E 7, Defensive Posturing & Endurance Fighting 50 | 2 | When taking heavy damage, automatic partial absorption triggers. Rank 2: can trigger once per AP cycle rather than once per combat. |
| **Endurance Fighter** | M 7, N 7, Defensive Posturing & Endurance Fighting 55 | 1 | AP penalties from taking damage don't apply until health drops below 25%, rather than at the normal threshold. |
| **Combat Awareness** | I 6, Threat Assessment 50 | 2 | Before combat begins, identify which enemies will act first and approximate their damage potential. Rank 2: detects ambushes before they trigger, converting a surprise attack into a normal initiative sequence. |
| **Armor Integrity** | E 7, M 6 | 2 | Equipped armor degrades significantly more slowly in extended engagements. Rank 2: armor damage heals partially between combats, reducing maintenance burden on long expeditions. |
| **Last System Standing** | N 9, E 7 | 1 | Once per combat, when health would reach zero, survive at 1 HP and immediately gain 2 AP for an emergency action. The player character refuses to go offline. |
| **Toughness** *(added 2026-07-04, ported from FNV)* | E 5 | 2 | +3 permanent damage resistance per rank. |
| **Life Giver** *(added 2026-07-04, ported from FNV)* | E 6 | 1 | +30 maximum health. |
| **Nerves of Steel** *(added 2026-07-04, ported from FNV — reworked, see note below)* | E 7 | 1 | Up to 2 unused AP at the end of your turn carry over into your next turn instead of being discarded (does not stack beyond 2 banked AP at a time). *(Provisional — flagged for developer review: FNV's original effect, "20% faster AP regeneration," doesn't map onto Inner Tepenia's turn-based AP model, since AP doesn't regenerate mid-turn and unused AP is discarded by the base rule rather than continuously refilling. This reworks it as the first implementation of the AP-banking idea already flagged, undesigned, in `Core-Mechanics/Action_Points_Perks_and_Traits.md`. Gated on Engine since Engine is already defined as the recovery-speed/AP-replenishment stat.)* |

---

## Combat — NODE / Targeting

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Processing Overdrive** | C 7, Tactical Grid Combat 50 | 2 | NODE analysis window is extended. Rank 2: one additional shot can be queued per NODE activation. |
| **Weak Point Specialist** | I 7, Tactical Grid Combat 55 | 2 | Scanned weak points display estimated damage and likely secondary effects before the shot is committed. Rank 2: targeting a scanned weak point costs 1 fewer AP. |
| **Cascade Protocol** | N 8, C 7 | 1 | Critical hits on robot enemies have a significantly higher chance to trigger cascade failures. A cascade can spread from the struck component to one adjacent system. |
| **Predictive Algorithms** | C 8, I 7 | 1 | In NODE mode, moving targets display projected positions. Accuracy penalties for targeting moving enemies are halved. |
| **Focus Under Fire** | N 7, Tactical Grid Combat 45 | 2 | Taking damage during NODE activation drains Nerve at a reduced rate. Rank 2: taking damage during NODE no longer drains Nerve at all — the player character's focus is unbreakable. |
| **Perimeter Awareness** *(added 2026-07-04, ported from FNV's Alertness)* | I 6 | 1 | While stationary and not moved this turn, gain a bonus to targeting accuracy in NODE mode equivalent to +2 Investigation. |

---

## Combat — Hybrid / Specialized

| Perk | Requirements | Ranks | Effect |
|------|-------------|-------|--------|
| **Non-Lethal Specialist** | A 6, M 6, Non-Lethal Restraint & Subdual 50 | 2 | Subdual options are faster and more reliable; non-lethal takedowns leave targets incapacitated longer. Rank 2: perform non-lethal takedowns on enemy types that are normally immune to subdual. |
| **Field Repair Protocols** | E 6, Precision Maintenance & Repair 50 | 2 | Perform emergency self-repair during combat using components in inventory — no workbench needed. Rank 2: can also repair companions mid-combat without spending additional AP. |
| **Threat Exploitation** | I 7, Threat Assessment 55 | 1 | After successfully assessing a threat before combat, the first attack on that target is guaranteed to hit regardless of other modifiers. Preparation pays. |
| **Robotics Expert** *(added 2026-07-04, ported from FNV)* | C 6, Threat Assessment 50 | 1 | +25% damage against robot enemies. Non-alerted robots can be shut down (rather than killed) by sneaking up and deactivating them directly. |
| **Silent Running** *(added 2026-07-04, ported from FNV)* | A 6, Stealth & Infiltration 50 | 1 | Running no longer breaks stealth or interrupts a sneak attempt. |
| **Quick Draw** *(added 2026-07-04, ported from FNV — reworked for turn-based AP, per the user's own design)* | A 5 | 1 | Drawing or holstering a weapon in combat costs no AP. *(FNV's original effect, "50% faster equip/holster," is a real-time animation-speed mechanic that doesn't translate to a discrete per-action AP cost — this reworks the same intent, removing weapon-switching as a tactical burden, into an AP-cost term instead.)* |

---

## Perk Count by Category

*(Updated 2026-07-24 — added 4 perks tied to newer systems: Off the Record, Bond Ledger, Grief Ledger, Steady Retrieval. Previously updated 2026-07-04 after adding 15 Fallout-adapted perks — see `project_fallout_trait_perk_adaptation` memory.)*

| Category | Count | Type |
|----------|-------|------|
| Social / Diplomatic | 9 | Non-combat |
| Growth / Learning | 3 | Non-combat |
| Technical / Engineering | 9 | Non-combat |
| Information / Data | 10 | Non-combat |
| Survival / Exploration | 8 | Non-combat |
| Cultural / Philosophical | 4 | Non-combat |
| Economic / Resource | 4 | Non-combat |
| Companion / Leadership | 5 | Non-combat |
| **Non-combat subtotal** | **52** | **65%** |
| Combat — Offensive | 8 | Combat |
| Combat — Defensive | 8 | Combat |
| Combat — NODE / Targeting | 6 | Combat |
| Combat — Hybrid / Specialized | 6 | Combat |
| **Combat subtotal** | **28** | **35%** |
| **Total** | **80** | |

Expansion in future design passes should maintain roughly this non-combat to combat ratio. DLC perks may skew toward the DLC's thematic focus, but the aggregate ratio across base game + all DLC should remain non-combat dominant.

---

## Pending Perks — Placeholders (~84 remaining to reach 160 target)

*(Updated 2026-07-04 after the Fallout-adapted perk batch — see `project_fallout_trait_perk_adaptation` memory.)*

The categories below indicate where additional perks are needed. Names and effects are to be designed during dedicated perk design passes. Rough targets per category to reach the 160 total at the correct ratio:

### Non-combat (need ~55 more to reach ~107 total)

| Category | Currently designed | Still needed |
|----------|-------------------|-------------|
| Social / Diplomatic | 9 | ~9 more |
| Growth / Learning | 3 | ~6 more |
| Technical / Engineering | 9 | ~9 more |
| Information / Data | 10 | ~6 more |
| Survival / Exploration | 8 | ~8 more |
| Cultural / Philosophical | 4 | ~8 more |
| Economic / Resource | 4 | ~6 more |
| Companion / Leadership | 5 | ~5 more |

### Combat (need ~25 more to reach ~53 total)

| Category | Currently designed | Still needed |
|----------|-------------------|-------------|
| Combat — Offensive | 8 | ~7 more |
| Combat — Defensive | 8 | ~5 more |
| Combat — NODE / Targeting | 6 | ~7 more |
| Combat — Hybrid / Specialized | 6 | ~6 more |

**Design note for future passes**: When adding perks, prioritize filling underrepresented categories first (Cultural/Philosophical, Companion/Leadership, Growth/Learning) before adding more to already-robust categories (Technical, Information/Data, Social). New non-combat categories not yet invented are still encouraged — the world of Inner Tepenia has enough distinct systems to support them.
