# MACHINE Stat Influence Map

A single reference document mapping each MACHINE stat to every system it touches — skills, formulas, passive effects, dialogue unlocks, and non-skill mechanics. Use this as the authoritative source when designing content that involves a specific stat.

---

## M — Might
**Definition**: Raw physical strength, power, structural force.  
**Fallout equivalent**: Strength

### Skills governed (5)
| Skill | Role |
|---|---|
| Jury-Rigging & Repurposing | Secondary (brute-force repair) |
| Frontier Survival & Cold Adaptation | Secondary (physical frame robustness) |
| Non-Lethal Restraint & Subdual | Primary (overpowering without killing) |
| Improvised Weaponry & Combat Jury-Rig | Primary (weaponizing heavy objects) |
| Defensive Posturing & Endurance Fighting | Primary (sustained brawl endurance) |

### Non-skill effects
- **Carry weight cap** — high Might allows carrying heavier equipment, salvage, and weapons
- **Melee damage bonus** — directly scales unarmed and heavy-weapon damage
- **Forced entry** — breaking locked doors, collapsing barriers, clearing rubble; high Might opens physical shortcuts
- **Physical intimidation checks** — certain dialogue branches require Might above a threshold
- **Structural installation** — moving and mounting heavy grid components in engineering quests

### Formulas
- No direct formula contribution currently (TBD: may feed melee damage formula)

### Design note
Currently underrepresented vs its Fallout Strength equivalent. See pending work: raise Might relevancy pass.

---

## A — Agility
**Definition**: Speed, reflexes, coordination, fine motor control.  
**Fallout equivalent**: Agility

### Skills governed (15)
| Skill | Role |
|---|---|
| Precision Maintenance & Repair | Primary (fine motor precision) |
| Jury-Rigging & Repurposing | Primary (dexterous improvisation) |
| Undergrid Navigation & Salvaging | Primary (navigating tight spaces) |
| Hydroponic Systems | Primary (delicate system tending) |
| Highway Maintenance & Transit Systems | Primary (precision installation) |
| Environmental Exploitation & Ripple Reading | Secondary (physical positioning) |
| Stealth & Infiltration | Primary (silent movement, timing) |
| Scavenging & Resource Foraging | Primary (quick searching) |
| Hazard Navigation | Primary (rapid movement through danger) |
| Non-Lethal Restraint & Subdual | Primary (speed and control) |
| Improvised Weaponry & Combat Jury-Rig | Secondary (fast weapon grab) |
| Tactical Grid Combat | Primary (positioning, initiative) |
| Sonic Attunement | Secondary (precise physical resonance) |
| Golden Eye Calibration | Primary (fine optical calibration) |
| Cultural Performance & Resonance | Secondary (physical expressiveness) |

### Non-skill effects
- **Base AP per turn** — `Base AP = 6 + floor(Agility ÷ 2)` (primary AP driver)
- **Movement cost** — base movement 1 AP/tile; higher Agility does not reduce tile cost directly but gives more AP to spend
- **Stealth detection** — passive avoidance of enemy awareness checks
- **Initiative order** — high Agility characters act earlier in turn order (TBD on implementation)
- **Evasion** — potential dodge chance modifier (TBD)

### Formulas
- `Base AP = 6 + floor(Agility ÷ 2)`

---

## C — Calculation
**Definition**: Logical processing, computation, optimization, problem-solving.  
**Fallout equivalent**: Intelligence + Luck (partial)

### Skills governed (15)
| Skill | Role |
|---|---|
| Thermal Engineering | Secondary (engineering math) |
| Siligel Chemistry | Primary (chemical computation) |
| Decentralized Systems Design | Primary (systems architecture) |
| Power Grid Management | Primary (grid optimization math) |
| Data Archaeology | Secondary (interpreting recovered data) |
| Arcanet Navigation & Hacking | Primary (writing exploits, routing) |
| Information Verification & Analysis | Secondary (cross-referencing logic) |
| Cryptography & Decryption | Primary (computational code-breaking) |
| Pre-War Lore & History | Secondary (logical inference from evidence) |
| Subnet Optimization | Primary (network efficiency algorithms) |
| Data Leakage & Information Warfare | Primary (programming attacks) |
| Tactical Grid Combat | Secondary (tactical computation) |
| Electronic Warfare | Primary (jamming and signal manipulation) |
| Holographic Projection & AI Interaction | Primary (interfacing with AI systems) |
| Memory & Consciousness Manipulation | Primary (computing consciousness patterns) |

### Non-skill effects
- **Skill points per level** — strongest contributor: `floor(Calculation ÷ 2)` added to formula
- **NODE / targeting system** — Calculation is the **primary accuracy stat**: `Hit % = (Calculation × 4) + ...`; also scales the Processing Cycles resource pool and drives predictive targeting overlays
- **Critical chance** — `Base Crit Chance = floor(Calculation ÷ 2) %`; primary source of crit probability across all attacks
- **Crafting quality** — high Calculation improves output quality for technical crafting recipes
- **Dialogue unlocks** — technical/scientific dialogue branches (hacking terminals, engineering analysis)
- **Hacking** — Calculation determines base success rate and options available on hack attempts

### Formulas
- `Skill points = max(3, 2 + floor(C÷2) + floor(N÷2) + INV modifier)`
- NODE cost formula: `Cost = Base + Distance + Body Part Difficulty – INV bonus` (Calculation also scales Processing Cycles pool)

---

## H — Humanity
**Definition**: Emotional intelligence, empathy, social awareness, connection.  
**Fallout equivalent**: Perception + Charisma (partial)

### Skills governed (13)
| Skill | Role |
|---|---|
| Rumor & Network Intelligence | Secondary (social information networks) |
| Diplomatic Negotiation | Primary (reading and leading negotiations) |
| Empathy Protocols | Primary (emotional recognition and response) |
| Faction & Reputation Management | Primary (understanding group dynamics) |
| Deception & Narrative Crafting | Primary (social manipulation) |
| Faction Rhetoric | Primary (tailored persuasion) |
| Moral Philosophy & Ethical Reasoning | Primary (ethical conviction and argument) |
| Companion Command & Loyalty | Secondary (emotional connection to companions) |
| Ossuary Resonance | Primary (connection to Goth death-ritual culture) |
| Sonic Attunement | Primary (empathic resonance with Cymaticist practice) |
| Holographic Projection & AI Interaction | Secondary (making AI interaction meaningful) |
| Robot Religion Insight | Primary (cultural empathy for robot spiritual practice) |
| Cultural Performance & Resonance | Primary (authentic emotional expression) |

### Non-skill effects
- **NPC reaction modifier** — baseline disposition toward the player; high Humanity improves initial NPC attitudes
- **Faction reputation gain rate** — positive actions grant slightly more reputation points
- **Merchant discounts** — high Humanity unlocks better barter rates
- **Companion morale** — affects companion satisfaction and loyalty thresholds
- **Dialogue branches** — emotional/empathic dialogue options gated on Humanity thresholds

### Formulas
- No direct formula contribution currently

---

## I — Investigation
**Definition**: Pattern recognition, information gathering, analysis, deduction.  
**Fallout equivalent**: — (new stat)

### Skills governed (21)
| Skill | Role |
|---|---|
| Jury-Rigging & Repurposing | Secondary (reading what parts can be repurposed) |
| Decentralized Systems Design | Secondary (spotting systemic patterns) |
| Undergrid Navigation & Salvaging | Secondary (reading underground environments) |
| Data Archaeology | Primary (recognizing patterns in old data) |
| Arcanet Navigation & Hacking | Secondary (reading network topology) |
| Information Verification & Analysis | Primary (distinguishing true from false) |
| Rumor & Network Intelligence | Primary (identifying reliable information) |
| Cryptography & Decryption | Secondary (recognizing cipher patterns) |
| Pre-War Lore & History | Primary (connecting historical patterns) |
| Subnet Optimization | Secondary (identifying inefficiencies) |
| Data Leakage & Information Warfare | Secondary (spotting exploitable gaps) |
| Empathy Protocols | Primary (reading emotional patterns) |
| Deception & Narrative Crafting | Secondary (reading the target to craft the lie) |
| Environmental Exploitation & Ripple Reading | Primary (reading terrain and environmental cues) |
| Stealth & Infiltration | Secondary (reading guard patterns) |
| Scavenging & Resource Foraging | Secondary (recognizing salvageable material) |
| Hazard Navigation | Secondary (pattern-reading danger) |
| Electronic Warfare | Secondary (recognizing signal patterns) |
| Golden Eye Calibration | Secondary (precise optical pattern recognition) |
| Memory & Consciousness Manipulation | Secondary (recognizing consciousness structure) |
| Robot Religion Insight | Secondary (recognizing spiritual/cultural patterns) |

### Non-skill effects
- **Skill points per level** — modifier contributor (see table in Skills.md); ranges from -3 to +3
- **NODE / targeting** — secondary accuracy contributor: `Hit % = (CAL × 4) + (INV × 2) + ...`; also reduces NODE targeting cost by identifying exploitable weak points (`Cost = Base + Distance + Body Part Difficulty – INV Bonus`)
- **Critical chance (conditional)** — `+floor(Investigation ÷ 3) %` crit bonus, but **only when targeting a scanned/identified weak point**; rewards pre-combat reconnaissance
- **Passive detection** — awareness radius for hidden enemies, traps, and interactable objects
- **Map discovery** — reveals more of the map on exploration
- **Loot quality** — higher Investigation increases chance of finding better items in searched containers
- **Deduction dialogue** — branches that require noticing inconsistencies or connections in conversation

### Formulas
- `Skill points = max(3, 2 + floor(C÷2) + floor(N÷2) + INV modifier)`
- NODE hit chance formula (secondary contributor); NODE cost formula (primary cost reducer via INV Bonus term)

---

## N — Nerve
**Definition**: Mental resilience, willpower, influence over companions.  
**Fallout equivalent**: — (new stat)

### Skills governed (10)
| Skill | Role |
|---|---|
| Diplomatic Negotiation | Secondary (holding firm in negotiations) |
| Faction & Reputation Management | Secondary (maintaining composure with hostile factions) |
| Faction Rhetoric | Secondary (willpower to hold a persuasive line) |
| Deception & Narrative Crafting | Secondary (willpower to sustain the deception) |
| Moral Philosophy & Ethical Reasoning | Primary (strength of moral conviction) |
| Companion Command & Loyalty | Primary (willpower-based leadership) |
| Isolation & Psychological Resilience | Primary (resisting psychological breakdown) |
| Defensive Posturing & Endurance Fighting | Primary (mental endurance in prolonged combat) |
| Threat Assessment | Secondary (staying calm enough to read threats accurately) |
| Ossuary Resonance | Secondary (psychological immersion in Goth ritual) |

### Non-skill effects
- **AP modifier per turn** — `Nerve Modifier = floor((Nerve - 5) ÷ 2)`, ranges from -2 to +2 at extremes
- **NODE focus bonus** — Nerve contributes a focus bonus to hit chance while in targeting mode
- **Critical severity** — Nerve governs what a critical hit *does* beyond a damage multiplier: Nerve 1–4 = extra damage only; Nerve 5–6 = light status (Stagger, minor Sensor Scramble); Nerve 7–8 = meaningful status (Joint Lock, Overheat, EMP burst); Nerve 9–10 = cascade failure on robot enemies (critical to one system destabilizes adjacent systems)
- **Psychological debuff resistance** — terror effects, morale breaks, intimidation, companion panic
- **Companion loyalty cap** — Nerve sets the ceiling on how fiercely companions will follow dangerous orders
- **Willpower dialogue** — resisting coercion, holding positions under pressure, intimidating NPCs
- **Focus Drain resistance** — taking damage during NODE activation drains Nerve; high Nerve resists this

### Formulas
- `AP per turn = Base AP + floor((Nerve - 5) ÷ 2)`
- NODE hit chance: `+ Nerve Focus Bonus` term

### Design note
Currently underrepresented in skills (10/44 = 23%). Its AP formula role and psychological resistance role are significant, but additional skill coverage is a pending design pass.

---

## E — Engine
**Definition**: Operational endurance, efficiency before burnout.  
**Fallout equivalent**: Endurance

### Skills governed (12)
| Skill | Role |
|---|---|
| Thermal Engineering | Primary (heat management and energy systems) |
| Precision Maintenance & Repair | Secondary (sustained maintenance operations) |
| Siligel Chemistry | Secondary (sustained chemical processing) |
| Decentralized Systems Design | Secondary (long-running system stability) |
| Undergrid Navigation & Salvaging | Secondary (endurance in harsh underground conditions) |
| Hydroponic Systems | Secondary (sustained tending cycles) |
| Highway Maintenance & Transit Systems | Secondary (sustained physical labor) |
| Power Grid Management | Secondary (sustained grid monitoring) |
| Frontier Survival & Cold Adaptation | Primary (heat generation against cold) |
| Environmental Exploitation & Ripple Reading | Secondary (sustained fieldwork) |
| Isolation & Psychological Resilience | Secondary (operational endurance in isolation) |
| Hazard Navigation | Secondary (sustained movement through hazardous zones) |

### Non-skill effects
- **AP efficiency — movement** — `Every 2 Engine above 5 grants 1 free movement point per turn`
- **AP efficiency — actions** — high Engine reduces AP cost of reloading, item use, and certain abilities
- **Siligel consumption rate** — high Engine reduces passive siligel drain
- **Heat / cold resistance** — Engine determines how long the player can operate in extreme temperature zones before debuffs apply
- **Sustained operation** — extended activities (long hauls, multi-hour underground trips) require Engine checks; failure causes debuffs
- **Fatigue resistance** — reduces penalty accumulation from high AP expenditure turns (see Optional Advanced Rules in Action_Points_Perks_and_Traits.md)

### Formulas
- Free movement points: `floor((Engine - 5) ÷ 2)` when Engine > 5
- Movement cost reduction for high Engine builds (exact ratio TBD per perk/trait design pass)

---

## Stat Coverage Summary

| Stat | Skills | % of 44 | Primary Formula Role |
|------|--------|---------|----------------------|
| Investigation | 21 | 48% | Skill points (modifier); NODE hit (primary) |
| Calculation | 15 | 34% | Skill points (strongest contributor) |
| Agility | 15 | 34% | Base AP |
| Humanity | 13 | 30% | — (NPC relations, faction rep) |
| Engine | 12 | 27% | AP movement efficiency |
| Nerve | 10 | 23% | AP modifier; NODE focus bonus |
| Might | 5 | 11% | — (melee damage TBD) |

**Pending design passes:**
- Might relevancy raise (melee damage formula, forced-entry system, carry weight)
- Nerve relevancy raise (more skill coverage, intimidation system, companion loyalty mechanics)
