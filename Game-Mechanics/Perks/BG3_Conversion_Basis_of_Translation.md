# BG3 Conversion — Basis of Translation

**Purpose:** before any individual Baldur's Gate 3 cantrip, spell, or feat gets converted into an Inner Tepenia
quickhack, perk, or trait (the `TODO.md` / `Weekly_To-Do_-_Current.md` item "Convert BG3 cantrips into
'quickhacks,' and BG3 spells and feats into perks and traits"), this document establishes the ground rules
for *how* that conversion happens. It is a methodology document, not a list of finished conversions — no
individual spell/feat is converted here. Modeled on the same "reference doc that governs a conversion pass"
role `FNV_Perk_Cross_Reference_Audit.md` plays for Fallout: New Vegas material.

**Source material:** `Reference/bg3-feats-full-list.txt` (53 feats), `Reference/bg3-spells-name-index.txt`
(316-entry name index), `Reference/bg3-spells-mechanical-detail.txt` (full mechanical detail for every
cantrip/spell, including NPC-only and item-granted categories) — all retrieved 2026-08-01/02.

**Framing, per direct developer instruction:** Inner Tepenia is openly Hard Sci-Fi, not "a Sci-Fi game" in
the loose sense — every BG3 entry requires **extreme reinterpretation**, and some entries theoretically may
not fit at all. This document exists to make that reinterpretation systematic rather than ad hoc, so that
100+ individual conversion decisions land consistently instead of each one re-deriving the rules from
scratch.

---

## 1. Target Category Triage

Every BG3 entry converts into exactly one of six outcomes. Work through these in order — the first one that
genuinely fits is the answer; don't keep searching for a "better" category once one clearly applies.

| # | Outcome | What it means | BG3 shape that points here |
|---|---------|---------------|----------------------------|
| 1 | **Quickhack** | Jack-in-delivered, hacking-adjacent, targets robots and/or humans through the Bridge Unit's interface capability (`Core-Mechanics/Hacking_and_Traceability_System.md`) | At-will/low-cost effects with a short duration and a narrow, debuff-or-utility footprint — BG3's cantrip shape maps here most naturally |
| 2 | **Level-up perk** | Player-chosen at a perk opportunity (every 2 levels), gated by MACHINE stat + skill thresholds, defines a build | Spells/feats that are genuinely a standing *capability upgrade* the player opts into — a new option that's always available once taken |
| 3 | **Earned perk** (Challenge / Companion / Quest / Capstone / Milestone / World — see `Perk_Framework.md`) | Automatic, non-chosen, awarded for specific play patterns | Spells/feats whose BG3 acquisition already resembles an earned reward (class/subclass features gated on doing a specific thing) rather than a menu choice |
| 4 | **Trait** | Character-creation only, double-edged (bonus + real penalty), max 4 selected of 25–60 total | Spells/feats that describe a *permanent constitutional fact* about the character rather than a discrete usable ability — closer to "how this person is built" than "something this person does" |
| 5 | **Item / equipment / weapon category** | A physical object, weapon type, chem, or armor property — not a perk/trait/quickhack at all | BG3 entries that are fundamentally about *what you're holding* (most Evocation damage spells, most item-granted spells) rather than a trained capability |
| 6 | **Doesn't translate — drop** | No conversion attempted | Entries that depend on magic/planar/divine premises with no coherent Hard Sci-Fi analogue even after reinterpretation (resurrection-from-nothing, plane-shifting, petrification-as-literal-transmutation, etc. — see Section 5) |

**Decision aid — ask in this order:**
1. Does converting this require inventing new lore (a new god, a new plane, literal magic)? → **Outcome 6.**
2. Is the BG3 version fundamentally "a thing you're carrying/wielding," not a trained skill? → **Outcome 5.**
3. Is it at-will or near-at-will, short-duration, narrow-footprint, and delivered through an interface/jack-in
   read? → **Outcome 1 (quickhack).**
4. Is it something the player actively chooses to build toward and use repeatedly, gated by stats/skills? →
   **Outcome 2 (level-up perk).**
5. Does its BG3 acquisition condition already look like "reward for doing X," not "menu pick"? → **Outcome 3
   (earned perk)** — then route to the specific sub-category per `Perk_Framework.md`'s existing rules.
6. Is it describing a permanent trade-off about how the character is built, not a usable action? → **Outcome
   4 (trait).**

**Open ambiguity, flagged rather than resolved — Level-Up vs. Earned for class-level abilities:** BG3
abilities gained automatically from leveling up a class (as opposed to player-chosen spells/feats) don't
have a single, fixed answer between Outcomes 2 and 3. Depending on the specific ability's description,
effect, and context, the same *kind* of BG3 acquisition (an automatic class-level feature) could
legitimately land as either a Level-up perk (if it reads as a build-defining choice worth gating behind a
perk slot) or an Earned perk (if it reads more like a reward for having played a certain way, matching
Category A–F's automatic-award logic in `Perk_Framework.md`). **Per direct developer instruction, this is
deliberately left open — decide case-by-case during the actual conversion pass, not by a blanket rule here.**

**On feats specifically:** BG3 feats are closer in shape to Inner Tepenia's traits or level-up perks than to
quickhacks — feats are permanent, chosen investments, never at-will abilities. Ability Score Improvement
feats (Ability Improvement, Resilient) map to stat-increase mechanics that may already be covered by existing
systems (`Permanent_MACHINE_Stat_Increases.md`) rather than needing a new perk at all — check there first
before creating a duplicate.

---

## 2. Diegetic Source Mapping

**No magic exists in Inner Tepenia.** Every BG3 spell effect needs a real-world (or grounded near-future)
technology, chemistry, or biology explanation before it can be converted — not just a reskinned name. This
mirrors what `Damage_Types.md` already did for the 13 BG3 damage types (Fire → thermal/plasma discharge,
Necrotic → nanite-driven molecular disassembly, Radiant → laser/particle beams, Psychic → neural/EM
disruption, and so on — see that file for the complete, already-established mapping; don't re-derive it).

The table below extends the same logic to BG3's **spell schools** (the classification each spell already
carries on bg3.wiki), giving each one a default diegetic bucket. Individual spells can deviate from their
school's default when a better fit exists — this is a starting lens, not a rigid rule.

| BG3 School | Default Inner Tepenia diegetic source | Notes |
|---|---|---|
| **Evocation** (direct damage: Fireball, Chain Lightning, Magic Missile) | Weapons, explosives, energy weapons, thrown chems | Usually **Outcome 5** (item/weapon), not a perk — see Section 1. A handful of self-only or utility Evocation spells (Absorb Elements-equivalents) may still be quickhacks/perks. |
| **Abjuration** (protective: Shield, Mage Armour, Globe of Invulnerability) | Nanoweave/reactive armor plating, deployable energy shielding, ablative coatings, cover-generation tech | Level-up perks (passive/toggle defensive capability) or quickhacks (short-duration active shield) depending on duration/cost |
| **Illusion** (Invisibility, Mirror Image, Minor Illusion) | Holographic projection/camouflage tech, EM/optical countermeasures, chameleon coating, decoy drones | Quickhacks for combat-duration effects; equipment for passive/always-on versions |
| **Necromancy** (Animate Dead, Vampiric Touch, Circle of Death) | Nanite-driven reanimation/repurposing of dead matter, engineered pathogens, targeted cellular entropy — same reinterpretation `Damage_Types.md` already applies to Necrotic damage | High-tier, likely gated behind Scorpio/Aquarius-flavored perks or quest-locked earned perks, not generic level-up options — this is dark, morally loaded material in BG3 and should stay that way here |
| **Enchantment** (Charm Person, Dominate Person, Hold Person) | Neural-interface manipulation via jack-in, pheromone/chemical compounds, targeted EM neural disruption — NOT generic "mind control magic" | Mostly quickhacks (Hold Person-style incapacitation reads as a Signal Weapon effect) or Deception/Speech-skill-adjacent perks for the social-manipulation end |
| **Conjuration** (summons: Conjure Elemental, Find Familiar) | Drone/turret deployment, hacked-in ally summons, Companion-adjacent mechanics | Level-up perks (deployable combat drone) or Companion System-adjacent content — check `Core-Mechanics/Companion_System.md` before inventing a parallel summon system |
| **Divination** (Detect Thoughts, See Invisibility) | Sensor tech, Investigation-skill extensions, hacking-based intel gathering, Arcanet node reads | Quickhacks (short-duration sensor pulse) or skill-milestone perks (Investigation threshold unlocks a passive read) |
| **Transmutation** (Enlarge/Reduce, Polymorph, Haste) | Chemistry/combat stims, cybernetic augmentation, exosuit servo boosts | Quickhacks (short-duration combat stim) or consumable items (a chem the player crafts/buys), rarely a permanent perk given how strong most Transmutation effects are |

**Cantrips specifically** (unlimited-use, at-will) split into two default landings, not one:
- **Basic weapon attacks** — Fire Bolt, Eldritch Blast-shaped cantrips read as an energy weapon's basic
  attack, not a perk at all (**Outcome 5**).
- **Quickhacks with a cooldown, not a resource cost** — utility/debuff cantrips (Guidance, Resistance,
  Friends, Minor Illusion) fit the quickhack model directly, using CP2077's own cooldown-based quickhack
  pacing (see the CP2077 challenge-perks conversion item in `TODO.md` for the parallel source material) rather
  than BG3's unlimited-use-but-1-action-cost model.

---

## 3. Mechanical Resource Mapping

BG3 runs on D&D 5e's resource and resolution systems. None of these exist in Inner Tepenia in their original
form — each needs an explicit substitution rule, applied consistently across every conversion.

| D&D/BG3 mechanic | Inner Tepenia substitute | Reasoning |
|---|---|---|
| **Spell slots** (limited-use resource, refreshes on Long/Short Rest) | **AP cost** (per-use, from the existing per-turn AP pool) **+ a separate limiting resource** — either a cooldown (turns until reusable, CP2077-style) or a consumable charge/battery item, never "unlimited casts" | AP alone isn't a sufficient limiter since it refreshes every turn (`Action_Points_Base-Level_System.md`) — spammable AP-only costs would break the resource tension spell slots exist to create. Every converted spell needs a cooldown or consumable tied to it, not just an AP price. |
| **Concentration** (one concentration spell active at a time, broken by damage/incapacitation) | A single **"active effect" slot** per character, occupied while a sustained quickhack/perk effect is running, cleared automatically if the character is downed/incapacitated (exact break-conditions TBD per effect) | Preserves the "you can only have one big ongoing thing running" tension without inventing new terminology beyond what the existing systems already imply |
| **Saving throws** (target rolls to resist) | **Flat threshold gate on the target's own stat/skill**, per `Skills.md`'s binding "no dice rolls" law | A BG3 spell requiring a Wisdom save becomes "target's Nerve/Humanity (whichever fits) must be below X for the effect to land" — deterministic, not randomized. For enemies specifically (whose stats aren't bound by the player's 5+5 creation budget, per `MACHINE_Stats.md`), this becomes a genuine encounter-design lever: a high-Nerve boss is simply immune to a given quickhack by design, not by lucky roll. |
| **Attack rolls** (spell/weapon attack roll vs. target AC) | Routes through the **existing ranged-combat RNG hit-chance system** already used for guns — this is the one place Inner Tepenia already tolerates randomness (`Skills.md`: "The only context where random number generation applies is ranged combat hit chance... and aimed-shot probability") | No new system needed — an attack-roll-based spell becomes a weapon-shaped attack using hit-chance math that already exists. |
| **Duration in "turns"** | Maps directly, 1:1 | Inner Tepenia is already turn-based with a fresh AP pool each turn (`Action_Points_Base-Level_System.md`); BG3's own "10 turns," "2 turns," etc. language ports over without conversion. |
| **Verbal / Somatic components** | Mostly **dropped** as a mechanic; reinterpreted only where it matters for a specific level-design beat — e.g. a Silence-equivalent quickhack that specifically disables anything with a "requires an unobstructed jack-in connection" tag | Component-tracking has no equivalent gameplay hook in Inner Tepenia's current systems; don't invent one just to preserve BG3 flavor unless a specific converted effect actually needs the counterplay (a "can't hack while silenced" interaction is worth keeping if a Silence-equivalent quickhack gets made). |
| **Ritual casting** (cast without a slot, outside combat, extra time) | **Non-combat-only variant**, zero AP/resource cost, unusable mid-combat | Direct conceptual match — no new system needed, just restrict the converted version to out-of-combat use. |
| **Class/subclass restriction** (only Warlocks get Eldritch Blast, etc.) | Perk/trait **stat + skill threshold gates**, per the existing level-up perk convention — not a class system, since Inner Tepenia has none | A spell that's Warlock-exclusive in BG3 doesn't need an artificial "class" gate; it needs stat/skill thresholds that make it naturally suit the same kind of build (e.g., a Calculation/Hacking-heavy character rather than a "this is a Wizard spell" label). |

---

## 4. Damage Type Mapping

**Already solved — do not redo this work.** `Game-Mechanics/Combat/Damage_Types.md` explicitly states it
"adapts BG3's 13-type framework, translated into grounded physics/chemistry/engineering," and covers all 13
BG3 damage types (Acid, Cold, Fire, Force, Lightning, Necrotic, Poison, Psychic, Radiant, Thunder,
Bludgeoning, Piercing, Slashing) plus Inner Tepenia's own additions (Radiation, EMP/Disrupt, Plasma,
Nanotech, Gravitic/Inertial, Neural/Interface). Any converted spell/feat with a damage component uses that
file's existing mapping directly — reference it, cite it, do not re-derive a new damage taxonomy during this
conversion pass.

---

## 5. Condition / Status Effect Mapping — Open Gap

**Not yet solved — flagged here, not resolved.** A search of the current GDD found no dedicated
status-effect/condition taxonomy document. BG3 conditions (Blinded, Charmed, Frightened, Grappled,
Incapacitated, Paralyzed, Petrified, Poisoned, Prone, Restrained, Stunned, Unconscious, and BG3's own
game-specific ones like Enwebbed/Staggered/Numbed) currently have no single Inner Tepenia equivalent list to
map onto — individual docs reference specific effects ad hoc (e.g., Traits.md's Frightened-adjacent language)
but nothing centralizes them.

**This is a prerequisite, not a blocker to starting individual conversions** — early conversion work can
proceed using BG3's own condition names as working placeholders (same pattern as other flagged gaps
elsewhere in this GDD, e.g. the limb-specific damage system noted in `Traits.md`), but a proper
`Status_Effects_and_Conditions.md` reference (or equivalent) should get built once enough converted entries
exist to reveal which conditions actually recur often enough to deserve one canonical definition each. Add to
`TODO.md` if/when this becomes a blocking dependency rather than a background note.

---

## 6. What Doesn't Translate — Drop List

Per Section 1's Outcome 6. Not exhaustive — a working list to extend as specific spells/feats are evaluated
and hit a wall. An entry belongs here only after genuinely attempting Sections 2–3's reinterpretation lens and
finding no coherent landing, not as a first resort.

- **True resurrection from nothing** (Revivify's "1 HP, no cost beyond a spell slot" model is fine —
  something closer to "raise the dead with no material cost or cause" is not, given Inner Tepenia's own
  grounded stance on death and the Reclaimer/Upper Earth Defector lore's careful treatment of
  exile-vs-death).
- **Planar travel / extradimensional spaces** (Banishment's "another plane of existence," Otiluke's
  Resilient Sphere's force-construct logic) — no planar cosmology exists in Inner Tepenia's setting; these
  either become straightforward containment/restraint effects (drop the "other plane" framing entirely) or
  get cut.
- **Literal petrification-as-transmutation** (Flesh to Stone, Flesh to Gold) — the *mechanical shape*
  (progressive restrain-then-incapacitate) is salvageable via nanite/chemical hardening reinterpretation, but
  "turns into literal stone/gold" as flavor should not survive conversion.
- **Deity-specific or setting-specific lore spells** (The Closed Fist of Bane, Bhaal's Power Word Kill
  Ritual, Selûne's Dream, Shar's Aegis, Kereska's Favour) — these are mechanically interesting (see Section 3
  for the resource/resolution patterns they demonstrate) but their *names and flavor* are Forgotten Realms
  pantheon-specific and should not be ported as-is; if the underlying mechanic is worth keeping, it needs a
  wholly new Inner Tepenia-native name and justification, not a reskin.

---

## 7. Process for Individual Conversion Passes

Once this framework is in place, an actual conversion pass (working through `bg3-spells-mechanical-detail.txt`
and `bg3-feats-full-list.txt` entry by entry) should, for each entry:

1. Run the Section 1 decision aid to land on an Outcome (1–6).
2. If Outcome 6, log it in Section 6 above with a one-line reason and stop.
3. If Outcome 5 (item/equipment), route to whatever weapon/armor/chem system is the right home — not this
   document's concern past that point.
4. If Outcome 1–4 (quickhack/perk/perk-subtype/trait), apply Section 2's diegetic source lens to write the
   in-fiction explanation first, before naming the mechanic.
5. Apply Section 3's resource mapping to convert every numeric/resource element (damage via Section 4,
   duration 1:1, saving throw → flat threshold, spell slot → AP + cooldown/consumable, attack roll → existing
   hit-chance system).
6. Name it — per `feedback_placeholder_name_flagging` memory conventions if AI-proposing new names, and
   never reusing a BG3/Forgotten-Realms-specific proper noun (Section 6's deity-name rule applies broadly).
7. File it in the correct destination doc per Outcome (`Regular_Perks_-_Level-Up.md`,
   `Hacking_and_Traceability_System.md` or a new quickhack-specific file, `Traits.md`, or the relevant earned-perk
   category file per `Perk_Framework.md`).

**Status: framework complete, 2026-08-02. No individual spells/feats converted yet under this framework —
that is the next phase of work.**
