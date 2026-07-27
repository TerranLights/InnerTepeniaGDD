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

## Clean Candidates — Ready to Add (no missing system, clear stat/skill mapping)

The strongest, most actionable bucket — nothing here is blocked on anything not already established.

| Perk | Real FNV Requirement | Real FNV Effect | Why it's ready |
|---|---|---|---|
| **Heave, Ho!** | Str 5, Explosives 30 | +50% thrown weapon velocity/range | Directly relevant to the established Throwing Weapons system; Might already governs throw distance per `TODO.md`'s stat mapping. **High priority.** |
| **Friend of the Night** | Per 6, Sneak 30 | Eyes adapt quickly to low-light | Clean single-stat mapping (Investigation or Engine for "Perception"), Sneak already exists. |
| **Light Touch** | Agl 6, Repair 45 | +5% crit chance in light armor, -25% enemy crit chance | Clean mapping, Repair already exists. |
| **Old World Gourmet** | End 6, Survival 45 | +25% addiction resist, +50% health from snack foods, alcohol grants health | Ties directly into established Glitch-Coolant/siligel food-and-drink culture. |
| **Travel Light** | Survival 45 | +10% move speed in light/no armor | Clean, simple. |
| **Bloody Mess** | — (no gate in the real perk) | +5% overall damage, cosmetic death animations | Simple, matches the real perk's own lack of a stat gate. |
| **Demolition Expert** | Explosives 50, 3 ranks | +20% explosive damage per rank | Explosives skill exists and is currently under-supported by perks. **High priority.** |
| **Ferocious Loyalty** | Cha 6 | Companions gain +50 DR when player drops below 50% HP | Cha → Humanity, clean. |
| **Gunslinger** | — | +25% NODE accuracy, one-handed weapons | NODE-equivalent of the real VATS bonus. |
| **Hand Loader** | Repair 70 | 2x case/hull recovery when using Guns; unlocks hand-load recipes | Clean, Repair-gated. |
| **Mad Bomber** | Repair 45, Explosives 45 | Unlocks special explosive crafting recipes | Clean dual-skill gate. |
| **Vigilant Recycler** | Science 70 → Cryptography or Chemistry (TBD) | 2x energy ammo recovery, better recycling recipes | Energy Weapons skill exists; needs a skill-mapping call (Science split three ways in our system). |
| **Commando** | — | +25% NODE accuracy, two-handed weapons | NODE-equivalent, pairs with Gunslinger. |
| **Living Anatomy** | Medicine 70 | Reveals target health/DT; +5% damage vs. humans/non-feral ghouls (→ humans/robots) | Medicine skill exists, strongly NODE/Investigation-flavored. **High priority.** |
| **Super Slam!** | Str 6, Melee Weapons 45 | Chance to knock down target on melee hit | Clean, Might + Bladed/Blunt Melee. |
| **Terrifying Presence** | Speech 70 | Intimidate through dialogue; foe flees | Good Social/Diplomatic ↔ Combat crossover, currently a gap. |
| **Here and Now** | — | Instantly level up | Simple, unique one-time effect, no mapping issues. |
| **Finesse** | — | +5% critical chance | Simple, clean. |
| **Mister Sandman** | Sneak 60 | Instant-kill a sleeping NPC, bonus XP | Dark but clean, ties into Sneak. |
| **Nerd Rage!** | Int 5, Science 50 | +15 DT and Might effectively maxed when health ≤20% | Clean dual-stat, good glass-cannon-adjacent design space. |
| **Fast Metabolism** | — | +20% HP restored from healing items | Assuming a healing-item system exists (near-certain), clean. **High priority.** |
| **Heavyweight** | Str-scaling | Weapons over a weight threshold weigh half as much | Clean, Might-gated. |
| **Hobbler** | Per 7 | +25% chance to hit legs in NODE mode | NODE-equivalent. |
| **Hit the Deck** | Explosives 70 | +25 DT against explosives | Clean. |
| **Piercing Strike** | Unarmed 70 | Unarmed/melee attacks negate 15 DT | Clean, Unarmed skill exists. |
| **Splash Damage** | Explosives 70 | +25% explosive AoE | Clean. |
| **Center of Mass** | Guns 70 | +15% NODE damage when targeting the torso | NODE-equivalent. |
| **Light Step** | Per 6, Agl 6 | Never trigger floor traps/mines | Clean dual-stat. |
| **Action Girl** | Agl 6, 2 ranks | +15 AP per rank | Direct AP-economy fit, currently a gap. **High priority.** |
| **Meltdown** | Energy Weapons 90 | Foes killed by energy weapons emit a harmful corona | Clean. |
| **Weapon Handling** | Might-scaling | Weapon Might requirements are 2 points lower | Assumes weapons carry Might requirements — plausible, clean if so. |
| **Paralyzing Palm** | Unarmed 70 | NODE unarmed attack paralyzes for 30 seconds | NODE-equivalent, clean. |
| **Walker Instinct** | Survival 50 | +1 to two stats while outdoors | Ties into the Frostlands/outdoor theme, parallels the existing Claustrophobia/Agoraphobia trait pair. |
| **Them's Good Eatin'** | Survival 55 | Killed creatures have a chance to drop a potent healing item | Clean, assuming creature loot exists. |
| **Tunnel Runner** | Agl 8 | +25% sneak speed in light/no armor | Clean, complements existing Undergrid-flavored perks. |
| **Broad Daylight** | — | No Sneak penalty from using a light source | Simple, clean. |
| **Certified Tech** | — | +25% crit vs. robots, high chance of bonus crafting component from destroyed robots | Strong fit for a robot-heavy setting, currently a gap. **High priority.** |

---

## Needs a Developer Decision (mapping/subtype question, not a missing system)

| Perk | Real FNV Requirement | Real FNV Effect | The open question |
|---|---|---|---|
| **Black Widow** / **Cherchez La Femme** | — | +10% damage vs. opposite/same sex, unique dialogue | Ties into the established sexuality rules (robots/human women bisexual, human men hetero with gate) — mechanically clean, but worth a deliberate call on whether damage-vs-sex is a comfortable design for this game rather than assumed. |
| **Hunter** / **Entomologist** / **Animal Friend** / **Tribal Wisdom** (partial) | Survival-gated | Bonuses vs. animals/mutated insects | Depends on whether Tepenia has huntable wildlife or mutated-creature combat encounters at all — not confirmed either way. |
| **Junk Rounds** / **Miss Fortune** | Luck-gated | Craft ammo from scrap / VATS incapacitate chance | Luck doesn't exist as a MACHINE stat — needs a substitute the same way Better Criticals got one (Nerve). |
| **Rapid Reload** | Agl 5, Guns 30 | 25% faster reloads | Depends on whether reloading is modeled as an explicit AP-costed action at all. |
| **Shotgun Surgeon** / **The Professional** / **And Stay Back** | Guns-gated | Bonuses tied to shotguns/revolvers/pistols specifically | Depends on whether Guns has named weapon subtypes (shotgun, pistol, etc.) or is a single flat skill. |
| **Vigilant Recycler** | Science 70 | 2x energy ammo recovery | Science splits three ways in Inner Tepenia (Chemistry/Hacking/Cryptography) — needs a call on which one governs "energy weapon maintenance," if any. |
| **Plasma Spaz** / **Laser Commander** | Energy Weapons-gated | Bonuses for plasma/laser weapons specifically | Depends on whether Energy Weapons has named subtypes. |
| **Unstoppable Force** | Str 7, Melee Weapons 90 | x4 damage through enemy blocks | Depends on whether a "block" defensive mechanic exists for enemies. |
| **Chemist** / **Chem Resistant** | Medicine-gated | Chems/stims last longer; addiction resistance | Depends on whether combat-buff chems and an addiction system are modeled (distinct from Glitch-Coolant, which is more a social/flavor substance). |
| **Explorer** | — | All locations marked on map | Directly depends on the still-undecided Quest Marker Design question (`TODO.md`) — genuinely can't resolve until that's settled. |
| **Implant GRX** | End 8 | Non-addictive subdermal chem injector, 2 ranks | Strong candidate for the "Augmentation/Cybernetics" perk category floated earlier this session — needs that category to exist first, or a chem system to hook into. |

---

## Blocked on a Missing System (not a rejection — genuinely can't build yet)

| Perk(s) | Missing system |
|---|---|
| Rad Child, Lead Belly, Rad Resistance, Atomic!, Irradiated Beauty, Rad Absorption | No radiation mechanic confirmed anywhere in the docs. |
| Night Person, Solar Powered | No day/night cycle confirmed. |
| Home on the Range, Roughin' It | No camping/sleep-for-bonus system confirmed. |
| Long Haul *(already flagged in `TODO.md`)* | No fast-travel system. |
| Adamantium Skeleton, Eye for Eye *(Adamantium Skeleton already flagged in `TODO.md`)* | No limb-specific damage system. |

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
| Intense Training | Grants a free SPECIAL point at level-up; Inner Tepenia's MACHINE stats are meant to be re-spec'd through Calethina's Lab and district methods (each with a real cost) rather than freely incremented via perk — giving this away as a perk would undercut that system's whole point. |

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
