# BG3 Conversion Triage — Level 3 & Level 4 Spells

First-pass triage/survey of `Reference/bg3-spells-mechanical-detail.txt`'s Level 3 (34 entries) and Level 4 (21
entries) sections, applying `Game-Mechanics/Perks/BG3_Conversion_Basis_of_Translation.md`'s Section 1 decision
tree and Section 2 diegetic-source lens. No final AP costs, exact numbers, or final names are proposed here —
per direct developer instruction, this is survey/triage only. Damage types cite `Game-Mechanics/Combat/Damage_Types.md`
directly rather than re-deriving.

**Outcome key:** 1 = Quickhack · 2 = Level-up perk · 3 = Earned perk · 4 = Trait · 5 = Item/equipment/weapon
category · 6 = Doesn't translate/drop

---

## Level 3

| BG3 Name | Outcome (1-6) | Hard Sci-Fi Translation Concept |
|---|---|---|
| Animate Dead | 3 | Nanite-driven reanimation of a corpse's motor systems into a controlled servant-drone. Per the framework's dark-material flag, this stays quest-locked/Scorpio-Aquarius-flavored (Earned/Quest category) rather than a generic level-up option, echoing the "targeted nanites" reinterpretation `Damage_Types.md` already gives Necrotic. |
| Beacon of Hope | 2 | A broadcast "triage beacon" signal that boosts the efficacy of medical stims applied within its radius and improves squad survival odds at critical HP — a Medicine-adjacent support build capability. |
| Bestow Curse | 1 | Single-target jack-in payload (choose a dread/attack-disruption/vulnerability variant) that degrades a target's combat performance via neural-interface disruption or a slow-acting chemical agent — the Enchantment-default quickhack landing. |
| Blinding Smite | 5 | A flash-radiant coated blade or melee weapon attachment that discharges a blinding coherent-light pulse on a solid hit — Radiant damage (per `Damage_Types.md`) plus an optical-overload/Blinded-equivalent debuff. |
| Blink | 1 | A short-range emergency phase-dash: a personal EM-cloak/hard-light displacement burst that briefly pulls the user off targeting locks and repositions them, combat-only. |
| Call Lightning | 5 | Sustained-strike lightning ordnance (portable rail-arc caster or called-in strike beacon) dealing Lightning damage repeatedly over a duration — Arc Weapons category. |
| Conjure Barrage | 5 | A cone-pattern shrapnel/flechette dispersal weapon (grenade or shotgun-class blast) dealing Slashing damage across a frontal arc. |
| Counterspell | 2 | A reactive counter-intrusion capability through the Bridge Unit — detects and jams an incoming hostile quickhack/jack-in attack before it resolves, gated by a Calculation/Hacking-skill threshold check against the attacker's tier. |
| Crusader's Mantle | 2 | A short-range combat-stim/morale broadcast that boosts allies' weapon damage output for its duration — a squad-support build option. |
| Daylight | 5 | A high-intensity floodlight flare or worn illuminator that nullifies optical-camouflage/darkness-based Illusion-tech effects within its radius. |
| Elemental Weapon | 5 | Swappable elemental ammunition or a coating cartridge that adds a chosen secondary damage type (per `Damage_Types.md`) and an accuracy bonus to a conventional weapon. |
| Fear | 1 | A cone-area Signal Weapon effect — a terror-inducing neural/psychic overload pulse (Psychic damage type) forcing targets to disarm and flee line-of-sight. |
| Feign Death | 1 | An induced low-signature state — humans trigger a medical near-coma stim, robots drop to idle/dormant power mode — granting broad damage resistance and poison/disease-equivalent immunity while unable to act, ending if the target is healed. |
| Fireball | 5 | A standard high-yield thermal/incendiary grenade or plasma charge dealing Fire/Thermal damage in a blast radius. |
| Gaseous Form | 5 | A one-use vapor-phase nanite-dispersal aerosol rendering the user an untargetable gas-form swarm able to squeeze through gaps, at the cost of being unable to fight — matches Transmutation's "rarely a permanent perk" default. |
| Glyph of Warding | 5 | A placeable proximity-triggered charge (damage variants: Acid/Cold/Fire/Lightning/Thunder, or non-damage: knockout gas/detonation) that arms against anyone but the deployer. |
| Grant Flight | 5 | A single-use strap-on thruster canister granting an ally short hover-jump bursts across a turn, must touch down at movement's end — Transmutation's exosuit-servo default. |
| Haste | 5 | A high-potency combat stim granting a temporary extra action and reflex/speed boost, with a mandatory "crash" (Lethargic-equivalent) turn once it wears off — the standard Transmutation-default consumable landing. |
| Hunger of Hadar | 5 | A corrosive-cryo fog grenade that blankets an area in blinding vapor, dealing Cold then Acid damage per turn to anyone caught inside and slowing movement. |
| Hypnotic Pattern | 1 | An area holographic dazzle-pattern projection that locks anyone who sees it into passive stupor until they take damage or are shaken — the Illusion-default quickhack; robots/constructs are immune per lacking the relevant optical-cognitive vulnerability. |
| Lightning Arrow | 5 | An arc-charged projectile round (bow-equivalent or rifle ammo) dealing Lightning damage on impact plus a secondary burst radius. |
| Lightning Bolt | 5 | A chained rail-discharge weapon firing a penetrating line of Lightning damage through everything in its path. |
| Mass Healing Word | 2 | A Medicine-skill-gated "field triage broadcast" — a bonus-action-speed remote stim dispersal that heals multiple nearby allies at once; humans-only, no effect on robots. |
| Plant Growth | 5 | An expanding structural-foam/insulating-gel canister that floods an area with sticky, slowing terrain, burnable away with thermal weapons — drops the literal-vegetation flavor as a poor fit for the Antarctic setting while keeping the mechanical shape. |
| Protection from Energy | 2 | A toggleable shielding-tech capability — calibrated ablative/reactive plating or a personal EM dampener granting resistance to one chosen energy damage type while active — Abjuration's armor-tech default. |
| Remove Curse | 1 | A decontamination/system-purge routine that clears active hostile status debuffs (chemical antidote for humans, corrupted-firmware flush for robots) from the target. |
| Revivify | 5 | A nanite-loaded defibrillator/trauma injector that stabilizes a freshly downed companion at minimum HP. The framework explicitly green-lights this "1 HP, no extra cost" model as acceptable, unlike true resurrection (Section 6 drop list). |
| Sleet Storm | 5 | A freeze-grenade that extinguishes fire, coats an area in slick ice (slowing movement, chance to fall), and interferes with sustained device/ability operation nearby. |
| Slow | 1 | A multi-target EM "system throttle" pulse (Arc Weapons/Signal Weapons EMP-adjacent kit) that cuts movement, defense, and action economy on everyone caught in its field. |
| Speak with Dead | 2 | An Investigation-skill-gated "neural residue recovery" capability — scanning a fresh corpse's neural cache/black-box storage for a handful of last-known data points; unusable on bodies destroyed by high-damage-type kills. |
| Spirit Guardians | 2 | A ring of micro-combat-drones the player deploys and sustains around themselves, dealing periodic Radiant or Nanotech-equivalent damage to anyone in range — Conjuration's sustained-perk default. |
| Stinking Cloud | 5 | A nausea-gas canister (Poison damage type) that incapacitates anyone failing to hold their breath/resist each turn inside its cloud. |
| Vampiric Touch | 5 | A melee siphon tool dealing direct damage while transferring a portion back to the user as HP/coolant — the exact "transfer vs. denial" vampiric subtype the `Damage_Types.md` Siphon section already defines (Drain Weapons category). |
| Warden of Vitality | 2 | A Medicine-gated combat-medic capability unlocking a repeatable bonus-action self/ally heal action for the duration of an active field-med aura. |

---

## Level 4

| BG3 Name | Outcome (1-6) | Hard Sci-Fi Translation Concept |
|---|---|---|
| Banishment | 1 | A short-range stasis-field/containment burst that locks a target out of acting, moving, or being targeted for a couple of turns — the drop list's "cut the planar framing, keep the containment shape" reinterpretation. |
| Blight | 5 | A black-market or Aquarius-lab nanite-disassembly charge dealing heavy Necrotic damage, notably harsher against organic/plant-tissue targets and inert against robots. Dark-sourced given Necromancy's flagged material, but it's a straight single-target nuke rather than a summon, so it lands as a weapon item rather than a quest-locked perk. |
| Confusion | 1 | An area holographic/EM disruption field that scrambles friend-or-foe identification, making affected targets attack indiscriminately or freeze — the Illusion-default quickhack. |
| Conjure Minor Elemental | 2 | A deployable combat-drone perk — choose a pair of light utility drones or one heavier single unit — the Conjuration→drone-deployment default; only one active drone loadout at a time, redeploying despawns the old one. |
| Conjure Woodland Being | 2 | A deployable scout/utility support-drone, distinct in flavor from the combat-drone perk above (recon/crowd-control tool with an entangling nanofilament line rather than a damage dealer); one active instance at a time. |
| Death Ward | 2 | An implanted "dead man's switch" — a cybernetic or nanite auto-injector that triggers once per rest cycle, catching what would be a lethal hit and stabilizing the character at minimum HP instead. |
| Dimension Door | 2 | An advanced, longer-range personal short-hop teleporter (phase-displacement tech) that can also pull one adjacent ally along — a build-defining upgrade beyond the Blink quickhack above. |
| Dominate Beast | 2 | A "turncoat" capability — hacks a hostile robot (or, rarely, tagged/cybernetic wildlife) into fighting alongside the player for a sustained duration, breaking if the controlled unit takes enough damage to re-trigger its own defensive routines. |
| Evard's Black Tentacles | 5 | A canister that unrolls entangling nanofilament/mechanical restraint cable across an area, dealing Bludgeoning damage and restraining anyone who fails to break free, creating difficult terrain for the duration. |
| Fire Shield | 5 | A toggleable ablative armor coating (heat-dispersal or cryo-insulated variant, mutually exclusive) granting resistance to its matching damage type and discharging a retaliatory burst against melee attackers. |
| Freedom of Movement | 2 | An exosuit servo-override capability that cures Stun-equivalent lockups and grants immunity to terrain-slowdown and forced-restraint effects — Abjuration's protective-tech default. |
| Grasping Vine | 2 | A deployable stationary tether-turret (Conjuration's turret-deployment default) that plants itself, creates a difficult-terrain zone, and can fire a grapple line to yank a target toward it. |
| Greater Invisibility | 2 | An active-camouflage suit capability (holographic bending + EM signature dampening) granting near-total visual/targeting concealment, breaking on a failed stealth check when the user attacks or interacts. |
| Guardian of Faith | 2 | A deployable stationary defense turret (heavy armor, high damage-per-hit) that loses structural integrity with every strike it lands — Conjuration's "summon a guardian" default. |
| Ice Storm | 5 | A cryo-fragmentation charge dealing combined Bludgeoning and Cold damage, coating the area in a slick ice surface afterward. |
| Otiluke's Resilient Sphere | 1 | A short-range deployable stasis-field/hard-light containment bubble that halves movement and blocks all incoming/outgoing attacks on whoever it encloses — usable defensively on an ally or offensively as a trap. |
| Phantasmal Killer | 2 | A sustained Signal-Weapon-adjacent capability — a jack-in-delivered false-threat neural overload inflicting ongoing Psychic damage and freezing the target's ability to move or act cleanly, gated by a Nerve/Calculation build. |
| Polymorph | 5 | A called-shot chemical dart or aerosol payload that suppresses a target down to a near-harmless combat state (minimal stats/HP) for its duration, reverting them once that reduced HP pool is depleted. Keeps the mechanical shape, drops the literal-shapeshifting flavor per the framework's petrification precedent. |
| Staggering Smite | 5 | A neural-disruptor-coated melee weapon adding Psychic damage on a solid hit and staggering (disadvantage, no reactions) anyone who fails to shake it off — the Blinding Smite pattern repeated with a different payload. BG3's class-lock (Hexblade only) suggests this could alternately be gated as an Earned/Companion perk tied to a specific companion's kit rather than a generic weapon mod, flagged for the actual conversion pass to decide. |
| Stoneskin | 5 | A toggleable subdermal or exoskeletal nanite-plating augment granting resistance to conventional Bludgeoning/Piercing/Slashing damage while active. |
| Wall of Fire | 5 | A long incendiary-charge line-layer (thermal trip-wire or deployable flame-wall turret) dealing Fire/Thermal damage to anyone entering or lingering in its line, with a lingering Burning-equivalent DoT on failed avoidance. |

---

## Outcome Distribution

**Level 3 (34 entries):** Outcome 1 (Quickhack) = 7 · Outcome 2 (Level-up perk) = 8 · Outcome 3 (Earned perk) = 1
· Outcome 5 (Item) = 18 · Outcome 4/6 = 0.

**Level 4 (21 entries):** Outcome 1 (Quickhack) = 3 · Outcome 2 (Level-up perk) = 10 · Outcome 5 (Item) = 8 ·
Outcome 3/4/6 = 0.

**Combined (55 entries):** Quickhack 10 · Level-up perk 18 · Earned perk 1 · Trait 0 · Item 26 · Drop 0 — no
entry in this batch hit a hard wall requiring Outcome 6, consistent with the framework's note that the drop
list is a last resort, not a first pass.
