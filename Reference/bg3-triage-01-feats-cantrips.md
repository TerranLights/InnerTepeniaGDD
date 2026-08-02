# BG3 Conversion — Triage Pass 01: Feats & Cantrips

First-pass triage/survey applying `Game-Mechanics/Perks/BG3_Conversion_Basis_of_Translation.md`'s Section 1
decision tree (6-outcome triage) and Section 2 diegetic-source lens to every entry in
`Reference/bg3-feats-full-list.txt` (53 feats) and the CANTRIPS section of
`Reference/bg3-spells-mechanical-detail.txt` (25 cantrips). **Triage only — no final AP costs, exact numbers,
or final names are set here**, per direct developer instruction. Damage types are referenced from the already-
solved `Game-Mechanics/Combat/Damage_Types.md`, not re-derived.

**Outcome key:** 1 = Quickhack · 2 = Level-up perk · 3 = Earned perk · 4 = Trait · 5 = Item/equipment/weapon
category · 6 = Doesn't translate / drop.

---

## Feats

| BG3 Name | Outcome (1-6) | Hard Sci-Fi Translation Concept |
|---|---|---|
| Ability Improvement | 2 | Already covered — this is exactly what Intense Training (`Permanent_MACHINE_Stat_Increases.md`) already provides (up to 10 ranks, +1 to any one MACHINE stat per rank, hard cap 10). No new perk needed; this feat's entire scope is already implemented. |
| Actor | 2 | Level-up perk: the Charisma+1 half is already covered by Intense Training (Humanity); the real content is a bonus skill-point injection into Speech and Performance, read as a trained "read the room, play the part" social-engineering specialization. |
| Alert | 2 | Level-up perk translating "initiative" into Inner Tepenia's turn economy: the character always acts first entering a new encounter and can't be caught in an ambush-triggered surprise round — framed as reflex-conditioning/threat-response training, Nerve-gated. |
| Athlete: Standing Up | 2 | Level-up perk (Might/Athletics-gated): cheaper movement cost recovering from prone/downed, plus a flat jump-distance increase — physical-conditioning payoff, not a stat trick. |
| Charger: Weapon Attack | 2 | Level-up perk (Might, Blunt/Bladed Melee-gated): a closing-charge melee strike dealing bonus damage that doesn't provoke enemy reactive attacks — covering ground and striking in one committed motion. |
| Charger: Shove | 2 | Level-up perk, same charge mechanic as above resolving as a forced-displacement shove instead of damage — distance scaled by Might vs. target mass, matching existing physical-contest logic. |
| Crossbow Expert: Point-Blank | 2 | Level-up perk (Mechanical Weapons skill-gated): removes the point-blank accuracy penalty for spring/mechanical ranged weapons — trained close-quarters handling of a weapon class built for distance. |
| Crossbow Expert: Wounding | 2 | Level-up perk extending the duration of a Piercing-inflicted bleed/wound DoT (`Damage_Types.md`) when using Mechanical Weapons — a called-shot/ammo-tuning specialization, not a new damage type. |
| Defensive Duellist | 2 | Level-up perk (Agility-gated, Bladed Melee skill): a successful parry/reactive deflection against melee adds a flat defense bonus vs. the next incoming hit — trained fencing reflex, not a dice-based reaction. |
| Dual Wielder | 2 | Level-up perk unlocking full two-weapon fighting with non-light Blunt/Bladed Melee weapons (normally restricted to light weapons), Might/Agility-gated. |
| Dual Wielder: Bonus Armour Class | 2 | Companion perk to the above: a small flat defense bonus for fighting with a melee weapon in each hand — the extra parry surface two live weapons provide. |
| Dungeon Delver: Perception | 2 | Level-up perk (Investigation-gated): automatically reveals hidden objects/caches and structural hazards within inspection range — a trained-attention perk layered on Investigation's existing flat-threshold detection law, not a new roll. |
| Dungeon Delver: Resist Traps | 2 | Level-up perk pairing with the above: reduced damage from environmental/structural hazards (rigged doors, industrial traps, pressure plates) — hazard-conditioning, Engine-adjacent. |
| Durable | 2 | Level-up perk (Engine-gated): full HP restored on any downtime/rest-equivalent — a self-repair-nanite/metabolic recovery specialization; the Constitution+1 half is already covered by Intense Training. |
| Elemental Adept | 2 | Level-up perk: choose one type from `Damage_Types.md` (e.g., Fire/Thermal, Acid, Lightning) — weapons/ammo of that type bypass the target's resistance and never roll their damage floor. Ammunition/energy-cell calibration expertise with one damage type. |
| Great Weapon Master: Bonus Attack | 2 | Level-up perk (Might, heavy Blunt/Bladed Melee builds): a kill or critical hit with a heavy melee weapon grants a free follow-up attack that turn — momentum-driven combat chaining. |
| Great Weapon Master: All In | 2 | Level-up perk: a toggleable power-attack stance for two-handed melee weapons, trading accuracy for a flat damage bonus — a deliberate overcommit switched on per swing. |
| Heavily Armoured | 2 | Level-up perk (Might-gated, requires the medium-armor perk below): unlocks proficient heavy plating/exosuit-class armor use without its normal mobility/AP penalty. |
| Heavy Armour Master | 2 | Level-up perk (Might-gated, requires Heavily Armoured): flat reduction to incoming Bludgeoning/Piercing/Slashing damage while wearing heavy armor, layering on the existing DT/DR system (`Damage_Types.md`). |
| Lightly Armoured | 2 | Level-up perk: unlocks proficient light-armor use without its stealth/mobility penalty; the Might/Dexterity+1 half is already covered by Intense Training. |
| Lucky | 2 | One of the cleanest conversions in the set: `Skills.md` already carves out ranged-combat hit chance and aimed-shot probability as Inner Tepenia's sole RNG contexts, so this becomes a small charge pool (recharging on rest-equivalent downtime) that forces a re-roll of a missed shot or guarantees a landed one — a direct hit on the one place the game tolerates randomness. |
| Mage Slayer: Saving Throw Advantage | 2 | Level-up perk: while in melee range of an enemy running a Signal Weapon/quickhack-style effect, gain a flat resistance bonus against that effect landing — anti-hacker melee training. |
| Mage Slayer: Attack Caster | 2 | Level-up perk: a free reactive melee strike against an enemy actively triggering a jack-in/Signal Weapon effect within melee range — punishes exposed hackers mid-activation. |
| Mage Slayer: Break Concentration | 2 | Level-up perk: melee hits against an enemy currently running a sustained "active effect" (Section 3's Concentration-equivalent) reduce that effect's odds of surviving the hit — battlefield disruption specialization. |
| Magic Initiate: Bard | 2 | Level-up perk: cross-training into the social-engineering kit — two Speech/Deception-flavored quickhacks plus one limited-use (rest-gated) Narrative/Performance-tier ability, Humanity-governed instead of a new "class." |
| Magic Initiate: Cleric | 2 | Level-up perk: cross-training into field medicine — two Medicine-flavored quickhacks plus one limited-use biotech stabilization ability, Investigation-governed. |
| Magic Initiate: Druid | 2 | Level-up perk: cross-training into survival/field biology — two Survival/Biology-flavored quickhacks plus one limited-use environmental-hazard ability, Engine-governed. |
| Magic Initiate: Sorcerer | 2 | Level-up perk: cross-training into innate neural-interface use — two jack-in-delivered quickhacks plus one limited-use Signal Weapon-tier ability, reflecting unusually strong natural Bridge Unit affinity rather than trained hacking. |
| Magic Initiate: Warlock | 2 | Level-up perk: cross-training into the nanotech/Scorpio-Aquarius dark-tech kit — two Necromancy-lens quickhacks (nanite/bio-agent debuffs) plus one limited-use higher-risk ability, kept morally loaded per the framework's Necromancy note. |
| Magic Initiate: Wizard | 2 | Level-up perk: cross-training into studied hacking — two Hacking/Cryptography-flavored quickhacks plus one limited-use Calculation-governed ability, the "book-learned" counterpart to Sorcerer's innate version above. |
| Martial Adept | 2 | Level-up perk: unlocks two chosen melee/ranged combat maneuvers (trip, disarm, called shot) usable via a small AP-surge charge pool recharging on rest-equivalent downtime — trained technique, not raw damage. |
| Medium Armour Master | 2 | Level-up perk (requires the light-armor chain): removes medium armor's Sneak penalty and improves its Agility-derived defense bonus — better-fitted plating, not heavier plating. |
| Mobile | 2 | Level-up perk (Agility/Acrobatics-gated): flat movement-speed increase, no penalty from rough terrain, no reactive attacks triggered disengaging after a melee strike — exosuit servo/leg-cyberware conditioning (Transmutation's stim/augmentation lens). |
| Moderately Armoured | 2 | Level-up perk (requires Lightly Armoured): unlocks proficient medium-armor and shield use. |
| Performer | 2 | Level-up perk tying directly into the Performance skill (Humanity-governed, added 2026-07-28): a starting/bonus instrument plus a Performance skill-point injection; the Charisma+1 half already covered by Intense Training. |
| Polearm Master: Bonus Attack | 2 | Level-up perk (reach-weapon Blunt/Bladed Melee builds): a bonus reach-weapon strike using the weapon's rear end, at a small extra AP cost rather than BG3's Bonus Action. |
| Polearm Master: Opportunity Attack | 2 | Level-up perk pairing with the above: reach weapons get a reactive strike against any enemy entering their extended range, not just ones leaving melee. |
| Resilient | 2 | Level-up perk: the stat+1 half is already covered by Intense Training; the "save proficiency" half becomes a flat resistance bonus against one chosen status-effect category (per the open condition-taxonomy gap flagged in the framework's Section 5) — genuinely new content, not a duplicate of Ability Improvement. |
| Ritual Caster: Free Spells | 2 | Level-up perk mapped through Section 3's ritual-casting rule (non-combat-only, zero AP/resource cost): access to two out-of-combat utility quickhacks from a small menu — e.g., a forensic data-recovery scan on a corpse/black-box, a temporary mobility stim, or a holographic disguise overlay. |
| Savage Attacker | 2 | Level-up perk preserving the "more consistent high melee damage" feel without dice: raises the effective damage floor on melee hits to a flat percentage of the roll's max, rather than roll-twice-keep-highest — a deterministic translation per `Skills.md`'s no-dice-rolls law. |
| Sentinel: Vengeance | 2 | Level-up perk (bodyguard/tank build): a free reactive melee strike against any enemy that attacks an ally within the player's melee range. |
| Sentinel: Snare | 2 | Level-up perk pairing with the above: a landed reactive strike also locks the target's movement for the remainder of that turn. |
| Sentinel: Opportunity Advantage | 2 | Level-up perk: reactive/opportunity strikes get a flat hit-chance bonus, extending Section 3's ranged-hit-chance substitution to reactive melee. |
| Sharpshooter: Low Ground | 2 | Level-up perk (Guns/Energy Weapons-gated): removes the elevation-disadvantage penalty on ranged attacks made from lower ground. |
| Sharpshooter: All In | 2 | Level-up perk: the ranged mirror of Great Weapon Master's All In — a toggleable power-shot stance trading accuracy for flat bonus damage with proficient ranged weapons. |
| Shield Master | 2 | Level-up perk gated on wielding a physical riot/ballistic shield item (equipment-dependent, not an item category of its own): improves the shield's passive defense and unlocks using it to block AoE explosive/thermal attacks for reduced or negated damage. |
| Skilled | 2 | Level-up perk, the cleanest of the set: a flat skill-point injection across three skills of the player's choice — "proficiency" swaps directly for Inner Tepenia's point-investment model, no reinterpretation needed. |
| Spell Sniper | 2 | Level-up perk: access to one bonus quickhack from any category, plus a stacking crit-threshold reduction specifically for Signal Weapon/quickhack-delivered attacks (as distinct from conventional gunplay). |
| Tavern Brawler | 2 | Level-up perk (Unarmed skill/Might-gated): unarmed strikes, improvised weapons, and thrown objects scale off Might twice over instead of once — a trained brawler/improvised-weapon specialization; the stat+1 half already covered by Intense Training. |
| Tough | 2 | Level-up perk: flat HP-per-level increase — direct, no reinterpretation needed since HP already works the same way mechanically. |
| War Caster: Concentration | 2 | Level-up perk: the player's active-effect slot (Section 3's Concentration-equivalent) resists being knocked out by incoming damage more reliably — hardened focus/interface-stability training. |
| War Caster: Opportunity Spell | 2 | Level-up perk: unlocks a reactive quickhack use (a melee-range Arc Weapon-style shock discharge) against an enemy disengaging from melee range, spent as a reaction rather than on the player's own turn. |
| Weapon Master | 2 | Level-up perk: removes the unfamiliar-weapon handling penalty for four chosen weapon categories (`Damage_Types.md`'s Weapon Category Cross-Reference table) — broad cross-training; the stat+1 half already covered by Intense Training. |

**Distribution note:** all 53 feats landed on Outcome 2 (level-up perk), none on 1/3/4/5/6. This is a direct
confirmation of the framework's own Section 1 prediction ("BG3 feats are closer in shape to Inner Tepenia's
traits or level-up perks than to quickhacks — feats are permanent, chosen investments, never at-will
abilities") rather than a triage shortcut — every entry was checked against the Outcome 5 (item), Outcome 4
(double-edged trait), and Outcome 3 (automatic reward) tests individually and none fit better than a chosen,
repeatable, stat/skill-gated build investment. Roughly a third of entries (Ability Improvement, Actor, Durable,
Heavily/Lightly/Moderately Armoured, Performer, Resilient, Tavern Brawler, Weapon Master) explicitly note where
their raw stat-bump component overlaps with the already-existing Intense Training mechanism in
`Permanent_MACHINE_Stat_Increases.md`, per the framework's direct instruction to check there first.

---

## Cantrips

| BG3 Name | Outcome (1-6) | Hard Sci-Fi Translation Concept |
|---|---|---|
| Fire Bolt | 5 | Basic attack of a Thermal/Cell-Fed energy weapon dealing Fire/Thermal damage (`Damage_Types.md`); high-ground range extension and object-ignition carry over as that weapon category's existing thermal-ignition flavor. |
| Eldritch Blast | 5 | Basic attack of a kinetic/coilgun sidearm (Force damage per `Damage_Types.md`); beam-count scaling at higher levels becomes a burst-fire/multi-round upgrade mod rather than a new spell rank, and Repelling Blast becomes a knockback-focused ammo variant. |
| Sacred Flame | 5 | Precision laser/particle-beam weapon attack (Radiant damage per `Damage_Types.md`); the binary "negates entirely on success" resolves as a flat evasion threshold (Agility/Acrobatics) rather than a to-hit roll, per Section 3's saving-throw-to-flat-gate substitution. |
| Acid Splash | 5 | Thrown corrosive-chem grenade or handheld sprayer (Acid damage per `Damage_Types.md`, Thrown/Explosives category); the Dexterity-save negation becomes a flat Agility/Acrobatics evasion threshold. |
| Blade Ward | 1 | Quickhack: a short-burst reactive-plating/nanoweave pulse (Abjuration's diegetic default) reducing incoming Bludgeoning/Piercing/Slashing damage for a couple of turns — one of the framework's own named quickhack examples. |
| Bone Chill | 5 | Ranged nanite/bio-agent round (Necrotic → nanite molecular disassembly per `Damage_Types.md`) whose payload also suppresses the target's regen/med-nanite response for a turn; kept dark and Scorpio/Aquarius black-market-flavored per the framework's Necromancy note. |
| Booming Blade | 5 | Melee weapon coating/mod (sonic-resonant edge, Thunder damage per `Damage_Types.md`) that punishes a struck target for moving away within the same turn — a weapon property, not a trained technique. |
| Bursting Sinew | 5 | A grim consumable: a nanite/breaching charge deployed onto a fresh corpse, detonating it into Piercing shrapnel (`Damage_Types.md`) and consuming the body — Scorpio/Aquarius/Pisces black-market item, kept dark per the framework's explicit instruction not to sanitize Necromancy-lens material. |
| Dancing Lights | 5 | A deployable, remotely-repositionable light marker/flare (thrown or clip-on) — pure illumination utility with no combat footprint, so it reads as carried equipment rather than a trained perk or jack-in effect (notably absent from the framework's own quickhack example list, unlike Guidance/Resistance/Friends/Minor Illusion). |
| Friends | 1 | Quickhack: a short-range pheromone-compound or neural-flattery pulse (jack-in/dispenser-delivered) improving an NPC's disposition for its duration, with a real downside if the target later realizes they were manipulated (approval hit, possible hostility) — matches Enchantment's diegetic default directly. |
| Guidance | 1 | Quickhack: a short-range Bridge Unit coaching/analysis pulse that temporarily lowers a specific skill check's effective threshold for the target — extending the same "temporarily extends the floor" logic `Skills.md` already uses for companion presence. |
| Light | 5 | A flashlight/glow-patch attachment item — object-targeted, resistible-by-others illumination with no combat function, same reasoning as Dancing Lights above. |
| Mage Hand | 1 | Quickhack: a jack-in-deployed micro-manipulator drone (cooldown-gated, matching the "1/Short Rest" recharge pace) that grabs, shoves, or relocates small objects at range without the player closing distance — Conjuration's "drone deployment" default landing directly. |
| Minor Illusion | 1 | Quickhack: a holographic decoy/noise-maker projector drawing nearby attention toward a false point of interest — one of the framework's own named quickhack examples (Illusion → holographic projection tech). |
| Poison Spray | 5 | Short-range chemical sprayer/contact-toxin dispenser (Poison damage per `Damage_Types.md`), craftable chem-weapon; largely ineffective against sealed robots per that file's own anti-human specialization note. |
| Produce Flame | 5 | Incendiary chem-flare/firestarter item — throwable for Fire/Thermal damage (`Damage_Types.md`) or held as a light source, doubling as illumination gear the same way the BG3 cantrip does. |
| Ray of Frost | 5 | Basic attack of a Thermal Weapons-category cryo-injector (Cold damage per `Damage_Types.md`, which explicitly lists "cryo weapons"/"freeze-injectors" as that type's in-world source); movement-slow, fire-extinguishing, and surface-freezing carry over as existing environmental interactions of that weapon. |
| Resistance (cantrip) | 1 | Quickhack: an armor-plating/stim pulse temporarily raising a target's resistance threshold against one damage or status category — one of the framework's own named quickhack examples, Abjuration's diegetic default. |
| Shillelagh | 5 | A servo-assisted "smart-grip" attachment for a blunt melee weapon, letting Calculation or Agility substitute for Might on that weapon's attacks for its duration — a physical weapon mod, not a trained capability (Transmutation's cyberware/stim lens applied to the item rather than the character). |
| Shocking Grasp | 5 | Melee stun-baton/arc-contact weapon (Arc Weapons category, Lightning damage per `Damage_Types.md`) that also disables the target's next reactive action; bonus effectiveness against metal-armored (conductive) targets carries over directly. |
| Thaumaturgy | 1 | Quickhack: a short-duration vocal/bio-modulation stim (subvocal resonance booster) improving Speech/Deception-flavored intimidation and Performance checks for its duration — Transmutation's chem-stim default landing. |
| Thorn Whip | 5 | A grapple-line or monofilament whip weapon (Bladed Melee/Piercing per `Damage_Types.md`) dealing damage and reeling the target several meters closer on a hit — matches Piercing's existing "monofilament" in-world flavor. |
| Toll the Dead | 5 | A targeted nanite/sonic "finisher" weapon (Necrotic → nanite disassembly per `Damage_Types.md`) whose damage output scales up against targets already showing structural/HP damage; the save-based resolution becomes a flat Nerve/Humanity threshold gate per Section 3. |
| True Strike | 1 | Quickhack: a targeting-assist pulse (smart-scope calibration / Bridge Unit target-lock) boosting the player's next ranged hit-chance or aimed-shot precision — a direct hit on Inner Tepenia's one legitimate combat-RNG context (`Skills.md`). |
| Vicious Mockery | 1 | Quickhack: a targeted infrasound/psy-audio harassment pulse (or jack-in insult-injection) dealing minor Psychic/Neural damage (`Damage_Types.md`) and degrading the target's next attack accuracy on a failed resistance threshold — Enchantment/Psychic's diegetic default, narrow debuff footprint matching the quickhack shape exactly. |

**Distribution note:** 16 of 25 cantrips landed on Outcome 5 (item/weapon — direct-damage, attack-roll-shaped
cantrips reading as a weapon's basic attack), 9 landed on Outcome 1 (quickhack — utility/debuff/buff cantrips
with a narrow, short-duration footprint), and none required Outcome 6 (drop) or Outcome 4 (trait) — matching
the framework's Section 2 prediction that cantrips split cleanly into "basic weapon attacks" and
"quickhacks with a cooldown, not a resource cost," with no cantrip requiring the more exotic Outcome 3
(earned perk) or Outcome 6 (drop) treatment reserved for spells/feats with deeper systemic or lore
entanglement.

---

**Status:** Triage pass 01 complete, 2026-08-02 — all 53 feats and all 25 cantrips covered. No final
AP/cooldown numbers, resource costs, or names assigned; that is the next phase of work per the framework's
Section 7 process (name, file into destination doc, assign numbers).
