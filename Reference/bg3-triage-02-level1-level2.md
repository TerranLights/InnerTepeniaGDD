# BG3 Conversion Triage — Level 1 & Level 2 Spells

First-pass triage/survey per `Game-Mechanics/Perks/BG3_Conversion_Basis_of_Translation.md`. Source:
`Reference/bg3-spells-mechanical-detail.txt` lines 176-510 (Level 1, 52 entries) and 511-788 (Level 2, 42
entries). Applies Section 1's 6-outcome decision tree and Section 2's diegetic-source lens. **No final AP
costs, exact numbers, or final names are proposed here** — this is triage only, per direct developer
instruction. Damage types cite `Game-Mechanics/Combat/Damage_Types.md` directly, not re-derived.

**Outcome key:** 1 = Quickhack · 2 = Level-up perk · 3 = Earned perk · 4 = Trait · 5 = Item/equipment/weapon
category · 6 = Doesn't translate — drop.

---

## Level 1

| BG3 Name | Outcome (1-6) | Hard Sci-Fi Translation Concept |
|---|---|---|
| Animal Friendship | 1 | Quickhack: pheromone/chemical pacifier dose or short-range calming signal that suppresses a non-sapient animal's aggression toward the user. Low-Int-target framing restricts this to feral Antarctic wildlife, not humans or robots. |
| Armour of Agathys | 2 | Level-up perk: cryo-retaliation plating that grants a temporary damage buffer and burns (Cold) any melee attacker who strikes you, until the buffer depletes or you rest. |
| Arms of Hadar | 5 | Item: a self-centered nanite-burst emitter/grenade dealing Nanotech/Molecular Disassembly damage (per Damage_Types.md's Necrotic mapping) in a radius, with a chance to disrupt nearby enemies' next action. |
| Bane | 1 | Quickhack: short-range signal-jamming pulse that degrades up to 3 targets' weapon accuracy and resolve (flat hit-chance/threshold penalty) for its duration. |
| Bless | 1 | Quickhack: squad-link encouragement/stim broadcast over the Bridge Unit tether, giving up to 3 allies a flat accuracy/resolve boost for its duration. |
| Charm Person | 1 | Quickhack: short jack-in compliance hack (or pheromone dose) on a human target per Enchantment's neural-interface/chemical mapping — suppresses hostile action against the user unless the user harms them first. |
| Chromatic Orb | 5 | Item: a selectable-payload energy sidearm — the player picks the active damage type (Acid/Cold/Fire/Lightning/Poison/Thunder, all already defined in Damage_Types.md) per shot; routes through the existing ranged hit-chance system since it uses an attack roll. |
| Colour Spray | 1 | Quickhack: cone-area dazzler/flashbang pulse (holographic overload per the Illusion mapping) blinding everyone under a combined toughness threshold for a short duration. |
| Command | 1 | Quickhack: short jack-in command-injection forcing a simple compliance behavior (approach/drop weapon/flee/halt/kneel) on a human or robot target through the Bridge Unit interface. |
| Compelled Duel | 1 | Quickhack: aggro-lock/taunt signal fixing a target's combat focus on the user, giving it accuracy disadvantage against anyone else for its duration. |
| Create or Destroy Water | 5 | Item: a portable atmospheric condenser/drainage charge that conjures or clears a water surface in an area, interacting with the existing Wet/ice-terrain hazard mechanics. |
| Disguise Self | 5 | Item: a holographic full-body disguise rig/chameleon-coating suit that changes visual appearance until deactivated — no mechanical benefit beyond visual, matching the BG3 original. |
| Dissonant Whispers | 1 | Quickhack: targeted sonic/neural assault burst (Psychic/Neural damage) causing pain-signal damage plus a brief seize/freeze debuff on a failed threshold. |
| Divine Favour | 5 | Item: a combat stim/ammo-overcharge chem boosting weapon damage output for a few turns. |
| Enhance Leap | 5 | Item: a leg-servo/exosuit calibration stim that triples jump distance for its duration. |
| Ensnaring Strike | 5 | Item: specialized tangle-net/monofilament ammo that, on a weapon hit, restrains the target and inflicts ongoing Piercing damage until freed. |
| Entangle | 5 | Item: a deployable adhesive-foam/net-mine grenade that creates difficult terrain and restrains anyone caught in it. |
| Expeditious Retreat | 5 | Item: an adrenal/servo-boost stim granting an extra dash/sprint each turn while active. |
| Faerie Fire | 1 | Quickhack: IR-paint/sensor-tag marker pulse that strips a target's stealth and makes it easier to hit for its duration. |
| False Life | 5 | Item: an adrenaline/stim-pack chem granting a temporary damage buffer. |
| Feather Fall | 5 | Item: impact-dampening exosuit boots/grav-stabilizer field generator preventing fall damage in an area. |
| Find Familiar | 2 | Level-up perk: a deployable micro-recon drone (the Cat/Crab/Frog/Rat/Raven/Spider roster reskinned as drone chassis classes), summoned once per rest cycle — check `Core-Mechanics/Companion_System.md` before finalizing so it doesn't duplicate existing companion mechanics. |
| Fog Cloud | 5 | Item: a smoke/aerosol-fog grenade creating a vision-blocking area. |
| Goodberry | 5 | Item: a siligel ration/nutrient-paste pack doubling as minor field healing and camp supply. |
| Magic Missile | 5 | Item: a smart-targeting micro-munition launcher (Force/Kinetic damage) firing auto-tracking submunitions that can split across multiple targets, no attack roll needed since they auto-hit. |
| Cure Wounds | 5 | Item: a nanite med-injector/stim-gel pack for direct field healing on humans; per canon has no effect on robots (need repair kits instead), matching the original's "no effect on undead/constructs" clause. |
| Shield (spell) | 1 | Quickhack: reflexive kinetic-dampening field/reactive plating micro-burst triggered defensively, granting a brief armor spike for one turn. |
| Burning Hands | 5 | Item: a cone-spread flamethrower/incendiary nozzle weapon (Fire/Thermal damage). |
| Grease | 5 | Item: a slick-foam/lubricant grenade creating flammable difficult terrain that can knock targets prone. |
| Guiding Bolt | 5 | Item: a laser-designator round (Radiant damage, attack-roll-based) that marks the target, granting the next attack against it bonus accuracy. |
| Hail of Thorns | 5 | Item: explosive-tipped arrows/rounds detonating a shrapnel burst (Piercing) around the impact point on hit or miss. |
| Healing Word | 5 | Item: a remote-deployed med-injector dart/mini-drone providing instant ranged field healing. |
| Hellish Rebuke | 2 | Level-up perk: a passive retaliatory countermeasure (thermal discharge/plating spike) that automatically damages an attacker the instant you take a hit. |
| Heroism | 1 | Quickhack: courage-stim broadcast pulse granting fear-debuff immunity and a rolling damage buffer to the target for its duration. |
| Hex | 2 | Level-up perk: a nanite target-tagging mark (Nanotech damage per the Necrotic mapping) dealing bonus damage on every hit landed and degrading one of the target's skill checks — Scorpio/Aquarius-flavored per the framework's Necromancy note. |
| Hunter's Mark | 2 | Level-up perk: a sensor-lock/target-designation HUD system granting bonus weapon damage against a marked target for the engagement, free to reapply if the target dies mid-fight. |
| Ice Knife | 5 | Item: a thrown cryo-knife/hybrid freeze-charge (Piercing initial + Cold burst, attack-roll-based) that can also generate a short-lived ice surface. |
| Inflict Wounds | 5 | Item: a close-range nanite-disruptor blade/gauntlet dealing heavy Nanotech (Necrotic-mapped) damage on a melee hit. |
| Longstrider | 5 | Item: a leg-servo calibration stim/exosuit boost adding sustained movement speed. |
| Mage Armour | 5 | Item: a nanoweave underlay/light bodysuit providing a baseline armor rating for otherwise-unarmored characters; removed if heavier armor is equipped. |
| Protection from Evil and Good | 6 | Drop: the entire mechanic is keyed to a Forgotten Realms creature-type taxonomy (Aberration/Celestial/Elemental/Fey/Fiend/Undead) with no equivalent categorization in Inner Tepenia's robots-and-humans setting; no narrow subset survives without fabricating a parallel taxonomy. |
| Ray of Sickness | 5 | Item: a toxin dart-gun/chemical injector weapon (Poison damage, attack-roll-based) that also inflicts a lingering debuff on hit. |
| Sanctuary | 1 | Quickhack: a targeting-jam/ECM field that drops the user off hostile weapons-lock until they act against an enemy. |
| Searing Smite | 5 | Item: incendiary ammo/blade coating that ignites on a melee hit for ongoing Fire/Thermal damage. |
| Shield of Faith | 2 | Level-up perk: a toggleable personal deflector-field emitter granting a flat armor bonus while active. |
| Sleep | 5 | Item: a sleeper-gas/nerve-suppressant grenade incapacitating everyone in the area under a combined toughness threshold, until they take damage. |
| Speak with Animals | 5 | Item: a bio-acoustic signal decoder/translator gadget for interpreting Antarctic wildlife vocalizations and body language — niche utility with no combat application. |
| Tasha's Hideous Laughter | 1 | Quickhack: a neural-overload pulse inducing involuntary spasming/collapse (can't act, prone) on a failed threshold, breakable by damage. |
| Thunderous Smite | 5 | Item: a piston-fist/shock-knuckle melee weapon mod dealing bonus Thunder damage plus a knockback-and-prone effect on hit. |
| Thunderwave | 5 | Item: a directional shockwave/sonic-charge emitter (Thunder damage) that knocks back everyone in its cone. |
| Witch Bolt | 5 | Item: a sustained-beam arc weapon (Lightning damage, Arc Weapons category, attack-roll-based) that keeps dealing damage each turn the user spends an action maintaining the lock. |
| Wrathful Smite | 5 | Item: a stun-blade/neural-disruption melee coating dealing bonus Psychic damage and inducing a brief freeze/fear response on hit. |

---

## Level 2

| BG3 Name | Outcome (1-6) | Hard Sci-Fi Translation Concept |
|---|---|---|
| Aid | 5 | Item: a pre-mission squad-wide nanite reinforcement injection raising max HP buffer until the next rest. |
| Arcane Lock | 1 | Quickhack: a countermeasure hack that electronically hardens a door/container/terminal lock against tampering for its duration — an inverted, defensive use of the hacking interface. |
| Barkskin | 2 | Level-up perk: subdermal nanoweave plating toggle setting a minimum armor floor while active. |
| Blindness | 1 | Quickhack: an optical-disruptor dart/EM flash pulse blinding a target (accuracy disadvantage, attackers get advantage) for its duration, re-checked each turn. |
| Blur | 2 | Level-up perk: a toggleable optical-distortion/holographic jamming field making the user harder to hit at range while active. |
| Branding Smite | 5 | Item: a laser-tagging blade coating dealing bonus Radiant damage and marking the target, stripping any active stealth/cloak tech for its duration. |
| Calm Emotions | 1 | Quickhack: an area pheromone/EM pacification pulse suppressing hostile intent in the area and de-escalating already-triggered aggression. |
| Cloud of Daggers | 5 | Item: a deployable rotor-blade/shrapnel-cloud mine dealing repeat Slashing damage to anyone in or moving through the area. |
| Crown of Madness | 1 | Quickhack: a control-override hack forcing a hostile human or robot to attack whatever's nearest instead of the user, re-checked each turn. |
| Darkness | 5 | Item: a combined smoke/EM-jamming obscurant grenade blocking vision and ranged attacks both in and out of the area. |
| Darkvision (spell) | 5 | Item: a low-light/thermal optics implant or cybernetic eye augment. |
| Detect Thoughts | 2 | Level-up perk: an Investigation/Calculation-gated neural-read capability letting the user passively pick up a conversation partner's surface thoughts via short-range interface bleed, matching Divination's "skill-milestone perk" default. |
| Enhance Ability | 5 | Item: a stat-specific combat stim (six flavors, one per relevant check) granting an edge on checks using one chosen stat. |
| Enlarge/Reduce | 5 | Item: an exosuit-overdrive/growth-hormone stim (Enlarge: +size, +carry capacity, +Might-check edge, +damage) or a servo-compacting chem (Reduce: the opposite); Reduce is the weaker half of the pair and may not earn its own slot on further review. |
| Enthrall | 2 | Level-up perk: a Speech/Deception-skill-gated capability that fixes an NPC's attention on the user, narrowing their peripheral awareness — a diversion tool, not a combat effect, matching Enchantment's social-manipulation landing. |
| Flame Blade | 5 | Item: a plasma/thermal-edge melee weapon (Cell-Fed Weapons category) that sheds light and can't be thrown or handed off. |
| Flaming Sphere | 2 | Level-up perk: a deployable incendiary combat drone with its own toughness/armor that the user can reposition each turn while it burns nearby enemies — matches Conjuration's drone-deployment default. |
| Gust of Wind | 5 | Item: a compressed-gas/pneumatic knockback tool pushing everyone in a line and knocking them off balance. |
| Heat Metal | 1 | Quickhack: an induction/EM heating hack that superheats a target's held metal weapon or worn plating, forcing a drop or inflicting ongoing Fire/Thermal damage, reapplicable each turn. |
| Hold Person | 1 | Quickhack: a Signal Weapon-style paralysis/neural lock-up disabling a humanoid target's movement and actions for its duration, re-checked each turn — the framework's own worked example for exactly this spell shape. |
| Invisibility (spell) | 2 | Level-up perk: an active camouflage/optical cloak toggle, broken by attacking, using items, or taking damage, matching the original's break conditions. |
| Knock | 1 | Quickhack: a remote lock-bypass hack instantly defeating a mundane electronic/mechanical lock regardless of difficulty; bypassing owned property still flags as a crime per existing systems. |
| Lesser Restoration | 5 | Item: a broad-spectrum antidote/nanite medkit curing disease, poisoning, paralysis, and blindness in one application. |
| Magic Weapon | 5 | Item: a weapon calibration chem/temporary mod coating granting a flat accuracy and damage bonus until the next rest. |
| Melf's Acid Arrow | 5 | Item: a corrosive dart/acid-round launcher (Acid damage, immediate + delayed tick, attack-roll-based) that also leaves a corrosive surface degrading armor. |
| Mirror Image | 2 | Level-up perk: a deployable holographic decoy field generating illusory duplicates that absorb incoming hits before the real target is struck. |
| Misty Step | 2 | Level-up perk: a thruster-assisted micro-blink — a short-range instant reposition via leg-servo/jet-assist burst to any visible unoccupied spot, gated by Engine/Might thresholds; the one clean grounded substitute for teleport-shaped effects without inventing new physics. |
| Moonbeam | 2 | Level-up perk: a deployable mobile beam-emitter drone (Radiant damage) the user can reposition each turn while it burns anyone standing in its beam. |
| Pass Without Trace | 1 | Quickhack: a squad-wide stealth-dampening broadcast (sound/thermal signature suppression) delivered via Bridge Unit tether. |
| Phantasmal Force | 1 | Quickhack: a neural pain-loop injection (Psychic/Neural damage) delivered directly through jack-in each turn, re-checked against a threshold to end early. |
| Prayer of Healing | 5 | Item: an out-of-combat squad medkit/nanite treatment session, usable only during downtime. |
| Protection from Poison | 5 | Item: an antitoxin injector/respirator filter upgrade neutralizing active poisons and resisting further Poison damage. |
| Ray of Enfeeblement | 5 | Item: a servo-disruptor dart weapon (attack-roll-based, per the framework's routing rule) that halves a target's Might-based weapon damage for its duration. |
| Scorching Ray | 5 | Item: a burst-fire thermal/plasma weapon firing three independently-aimed shots (Fire/Thermal damage). |
| See Invisibility (spell) | 2 | Level-up perk: a sensor-suite upgrade (Investigation/Divination-flavored) letting the user detect cloaked/hidden targets in an area, forcing active camouflage to fail. |
| Shadow Blade | 5 | Item: a monowire/vibro-blade with a neural-disruption edge (Psychic/Neural damage), stronger against targets in low visibility or obscuring cover. |
| Shatter | 5 | Item: a sonic-charge grenade (Thunder damage), especially effective against robots and structures per the anti-robot Thunder note in Damage_Types.md. |
| Silence | 1 | Quickhack: a comms/signal-jamming field disabling voice comms and anything requiring an unobstructed jack-in connection within its radius — the framework's own worked example for this spell. |
| Spike Growth | 5 | Item: a deployable spike-mine/caltrop field generator dealing Piercing damage per interval of movement through the area. |
| Spiritual Weapon | 2 | Level-up perk: a deployable autonomous attack drone acting on its own initiative each turn, one active at a time, immune to opportunity attacks. |
| Warding Bond | 2 | Level-up perk: a Bridge Unit damage-redistribution tether linking the user to an ally, granting the ally resistance/armor while redirecting a share of their damage back to the user; persists if the user is downed, ends if they die. |
| Web | 5 | Item: an adhesive-foam/webbing grenade creating flammable difficult terrain that restrains anyone caught in it, while also cushioning falls. |

---

## Outcome Distribution Summary

| Outcome | Level 1 | Level 2 | Total |
|---|---|---|---|
| 1 — Quickhack | 13 | 10 | 23 |
| 2 — Level-up perk | 6 | 12 | 18 |
| 3 — Earned perk | 0 | 0 | 0 |
| 4 — Trait | 0 | 0 | 0 |
| 5 — Item/equipment/weapon | 32 | 20 | 52 |
| 6 — Drop | 1 | 0 | 1 |
| **Total** | **52** | **42** | **94** |
