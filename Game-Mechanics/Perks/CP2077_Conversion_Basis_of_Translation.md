# CP2077 Conversion — Basis of Translation

**Purpose:** before any individual Cyberpunk 2077 skill-level reward or perk gets converted into an Inner
Tepenia challenge perk or level-up perk (the `TODO.md` / `Weekly_To-Do_-_Current.md` item "Convert Cyberpunk
2077's skill-based bonuses into 'challenge perks,' and also into ordinary level-up perks where that fits
better"), this document establishes the ground rules for *how* that conversion happens. Same role as
`BG3_Conversion_Basis_of_Translation.md` plays for the Baldur's Gate 3 material — a methodology document, not
a list of finished conversions.

**Source material, all in `Reference/`:**
- `cp2077-1.63-skill-level-rewards.txt` — pre-2.0, all 12 skills, automatic level 1-20 rewards
- `cp2077-1.63-perk-trees.txt` — pre-2.0, all 12 skills, chosen perk trees
- `cp2077-2.0-skill-rank-bonuses.txt` — post-2.0, 5 role skills (Solo/Netrunner/Headhunter/Shinobi/Engineer),
  automatic rank 5-60 rewards
- `cp2077-2.0-perk-trees.txt` — post-2.0, 4 of 5 Attribute perk trees (Technical Ability's cyberware branch
  is a flagged, unresolved gap — see that file's own STATUS note and `TODO.md`), plus the 9-perk Relic tier
  (Phantom Liberty DLC-exclusive — see Section 5's revised treatment below: mechanics kept as source
  material, DLC-specific lore/branding dropped)

**Framing — this is a smaller lift than the BG3 pass, for a specific reason:** CP2077 is already a grounded
(if stylized) sci-fi setting, not a fantasy one. Percentage-based combat bonuses (Crit Chance +X%, Recoil -X%,
Damage +X%), RAM/Stamina resource economies, and cyberware are already the *shape* Inner Tepenia's own perks
already take (see `Perk_Framework.md`'s existing perk examples) — there's no "no magic exists" wall to climb
the way BG3 required. The real work here is scope discipline (this is explicitly NOT a wholesale port —
see the developer's own framing below) and resource-system translation (RAM, Stamina, Perk Points, and
crafting-quality tiers don't have exact Inner Tepenia equivalents and need deliberate mapping, not assumption).

**Explicit developer framing, preserved from the original TODO.md entry:** "this is explicitly a mixed sort,
not a 1:1 conversion — some entries become challenge perks, some become ordinary level-up perks instead, and
some won't translate at all... Treat the CP2077 material as a rich basis to mine from, not a checklist to
convert wholesale."

---

## 1. Check Existing Systems First — Before Triaging Anything

**Some of this material is already spoken for.** Before running any CP2077 entry through the triage below,
check whether it's already covered by an existing Inner Tepenia system:

- **Sandevistan, Berserk, and Overclock** (the three CP2077 "mode" abilities, spanning Reflexes/Body/
  Intelligence-adjacent Cyberware) are **already fully adapted** as the **Neural Overclock** system
  (`Core-Mechanics/Neural_Overclock.md` — Framejack/Berserk/Overclock modes, gated on 8+ in Agility/Might/
  Calculation respectively, resourced by a "Neural Strain" meter). Any 2.0-era perk that modifies or extends
  Sandevistan/Berserk/Overclock (e.g., Air Kerenzikov, anything under Deadeye/Focus that reads as an
  Overclock-adjacent burst mode) should be evaluated as a potential **addition to Neural Overclock's existing
  mode list**, not a freestanding new perk that duplicates it.
- **Breach Protocol and Quickhacking's core loop** (hack a target, spend a resource, apply an effect) is
  already covered conceptually by `Core-Mechanics/Hacking_and_Traceability_System.md` (the OR-gated
  Calculation/Hacking-skill access system, plus traceability). Individual Breach Protocol/Quickhacking perks
  should be evaluated as **modifiers to that existing system** (faster access, cheaper hacks, better
  traceability control) rather than an entirely parallel hacking framework.
- **Ability Score Improvement-equivalents** — none of the CP2077 material grants raw stat points the way BG3
  feats did, so this particular cross-check (relevant for the BG3 pass) doesn't apply here.

---

## 2. Target Category Triage

Narrower than the BG3 pass's 6-outcome space, per the developer's own explicit scoping. Four outcomes:

| # | Outcome | What it means |
|---|---------|---------------|
| 1 | **Level-up perk** | Player-chosen at a perk opportunity, gated by MACHINE stat + skill thresholds |
| 2 | **Challenge perk** | Automatic, earned via a measurable play pattern (kill counts, skill-use counts, etc.) — `Perk_Framework.md` Category A |
| 3 | **Existing-system modifier** | Not a new perk at all — an addition/tweak to Neural Overclock or the Hacking/Traceability system per Section 1 above |
| 4 | **Doesn't translate for Inner Tepenia** | Not a deletion — parked, see Section 5's retention policy |

**Decision aid:**
1. Does it modify/extend Sandevistan, Berserk, Overclock, Breach Protocol, or Quickhacking's core loop? →
   **Outcome 3.** Route to the relevant existing-system doc, not this pipeline.
2. Is the CP2077 acquisition condition itself automatic/play-pattern-based (a skill-level reward, a rank
   bonus) rather than a menu pick? → **Outcome 2 (challenge perk).** This is the natural home for
   *most* of `cp2077-1.63-skill-level-rewards.txt` and `cp2077-2.0-skill-rank-bonuses.txt` — those were never
   player-chosen in CP2077 either, so a challenge perk (which is also automatic/earned) is the closer
   structural match, not a level-up perk.
3. Is it a player-chosen tree perk (from `cp2077-1.63-perk-trees.txt` / `cp2077-2.0-perk-trees.txt`) that
   defines a build choice? → **Outcome 1 (level-up perk).**
4. Does it depend on CP2077-specific tech/lore/proper nouns with no coherent Inner Tepenia analogue even
   after reinterpretation, or is it flatly incompatible with an Inner Tepenia system law (see Section 4)? →
   **Outcome 4.**

**Note on "+1 perk point" rewards:** flagged in the original TODO.md entry as a known non-translator — Inner
Tepenia awards perk points on a fixed every-2-levels cadence (`Perk_Framework.md`), so a mid-tree "+1 perk
point" reward has no clean equivalent. Default treatment: drop the perk-point-grant itself, but check whether
the *rest* of that reward tier (CP2077 rewards often bundle a numeric bonus and a perk point on the same
level) still has standalone value as a challenge perk once the perk-point half is removed.

---

## 3. Skill-to-Skill Mapping

CP2077's 12 pre-2.0 skills and 5 post-2.0 role skills need a landing skill/stat in Inner Tepenia's 26-skill,
7-MACHINE-stat system (`Character-Creation/Skills.md`, `Character-Creation/MACHINE_Stats.md`) before any of
their rewards can be threshold-gated correctly.

| CP2077 Skill (era) | Closest Inner Tepenia skill/stat | Notes |
|---|---|---|
| Athletics (1.63) | Athletics (Might) | Direct name match; Inner Tepenia's Athletics is already "the can-you-overpower-this skill," a close conceptual match |
| Annihilation (1.63) | Mechanical Weapons or Guns (Might/Nerve, weapon-dependent) | CP2077's Annihilation covers Shotguns + LMGs specifically — Inner Tepenia doesn't yet split weapon categories this finely (see Section 6) |
| Street Brawler (1.63) | Unarmed (Engine) | Direct conceptual match |
| Handguns (1.63) | Guns (Nerve) | Direct conceptual match |
| Assault (1.63) | Guns (Nerve) | Same governing skill as Handguns in Inner Tepenia — CP2077 splits these, Inner Tepenia doesn't (see Section 6) |
| Blades (1.63) | Bladed Melee (Agility) | Direct conceptual match |
| Engineering (1.63) | Mechanical Weapons (Might) or Explosives (Nerve), split by perk | CP2077's Engineering covers both Tech weapons and grenades — these are two different Inner Tepenia skills |
| Crafting (1.63) | Repair (Investigation) | Closest existing skill; Inner Tepenia has no standalone Crafting skill — see Section 6 |
| Breach Protocol (1.63) | Hacking (Calculation) | Per Section 1, routes through the existing Hacking/Traceability system rather than becoming standalone perks |
| Quickhacking (1.63) | Hacking (Calculation) | Same as above |
| Stealth (1.63) | Sneak (Agility) | Direct conceptual match |
| Cold Blood (1.63) | Nerve (MACHINE stat directly, not a skill) | Cold Blood's whole identity (stacking combat buff from recent kills) is closer to a Nerve-gated perk/trait line than any single skill |
| Solo (2.0 role) | Athletics + Guns, split | Groups heavy weapons/carrying capacity/health — spans multiple Inner Tepenia skills |
| Netrunner (2.0 role) | Hacking (Calculation) | Routes through existing Hacking/Traceability system per Section 1 |
| Headhunter (2.0 role) | Guns + Sneak, split | Headshots/handguns + stealth-adjacent visibility reduction |
| Shinobi (2.0 role) | Acrobatics (Agility) + Bladed Melee | Movement-ability-driven, matches Acrobatics' "finesse past/through obstacles" definition |
| Engineer (2.0 role) | Repair (Investigation) + Mechanical Weapons | Armor/Cyberware capacity + smart weapons + crafting |

**Cross-cutting note:** several CP2077 skills split across two or more Inner Tepenia skills (Annihilation,
Engineering, Solo, Headhunter). When converting an individual perk, use the specific perk's own effect to
decide which Inner Tepenia skill it threshold-gates against — don't force the whole source skill onto one
target.

---

## 4. Resource & System Mapping

| CP2077 mechanic | Inner Tepenia substitute | Reasoning |
|---|---|---|
| **RAM** (Netrunner resource pool) | Folds into the existing AP cost + Hacking/Traceability system, OR becomes a dedicated Hacking-specific resource if the actual conversion pass decides one is needed | No RAM-equivalent resource currently exists in Inner Tepenia's hacking docs — this is an open design question for whoever does the actual conversion, not resolved here. Do not invent a full parallel resource system unprompted; flag it as a decision point instead. |
| **Stamina** (dodge/sprint/attack economy) | Folds into AP cost — actions that cost Stamina in CP2077 become AP-cost modifiers in Inner Tepenia, since AP already governs the same "how much can I do this turn" economy | Direct precedent from the BG3 framework's own spell-slot-to-AP mapping; Inner Tepenia has no separate Stamina pool and shouldn't gain one just to preserve CP2077 flavor |
| **Perk Points** (CP2077's own skill-level reward currency) | Does not translate — per the developer's own explicit flag; Inner Tepenia's perk point cadence is fixed at every 2 levels, not earned through skill use | See Section 2's note above |
| **Cyberware capacity/slots** | Open question — Inner Tepenia's player characters are themselves robots (Bridge Unit, "frame"+"body," no separate human-plus-implants duality the way CP2077's V has), so "cyberware capacity" as CP2077 defines it may not map onto a robot protagonist at all. Needs a developer decision before any Engineering/cyberware-branch perk is converted; do not assume equivalence. | Flagged, not resolved — this is a bigger structural question than a simple resource swap |
| **Crafting quality tiers** (Uncommon/Rare/Epic/Legendary/Iconic) | Open question — no item-rarity/quality-tier system currently exists anywhere in Inner Tepenia's `Game-Mechanics/` docs (confirmed via search 2026-08-02). Crafting-tier-unlock perks (e.g., "Scrapper," "Grease Monkey," "Edgerunner Artisan") cannot be converted until this is resolved. | Flagged, not resolved |

---

## 5. What Doesn't Translate for Inner Tepenia — Not a Deletion List

Per Section 2's Outcome 4. Same "flag reasons, don't force it" approach as the BG3 framework's own drop list.

**Retention policy, per direct developer instruction, 2026-08-02 (same policy as
`BG3_Conversion_Basis_of_Translation.md` Section 6): "rejected for Inner Tepenia" is not "thrown away."**
Nothing gets deleted from the underlying `Reference/cp2077-*.txt` source files regardless of triage outcome.
Material that doesn't land here may still be useful for the Outer Tepenia trilogy or *Toronto Fell Out* —
flag rejected entries as parked for a different project, not discarded. The BG3 framework's one true
exception (genuine planar/supernatural-magic premises, e.g. banishing something to another plane of
existence) largely **doesn't apply to this source material** — CP2077 is already a grounded sci-fi setting
with no magic-as-magic content to begin with, so nothing in the list below needs that exception invoked.
Every item here is retained as potential cross-project material by default.

- **CP2077-specific proper nouns and branded tech** — Sandevistan, Kerenzikov, Cyberpsychosis (as a named
  CDPR-coined condition, though the underlying "heavy augmentation has a mental cost" concept already exists
  via Neural Overclock's own Humanity-linked drawbacks), Night City-specific gang/corp names, "Trauma Team,"
  "Relic," "Militech," etc. — none of these should be ported by name even if the underlying mechanic survives
  conversion.
- **"Relic" perk tier — REVISED, no longer a blanket drop.** Per direct developer instruction, 2026-08-02:
  the Relic chip itself (the DLC's specific plot device) doesn't translate and its name/lore should never be
  ported, but the *underlying mechanics* of its 9 perks (Optical Camo combat-exit tech, enemy Vulnerability
  detection/exploitation, expanded Arm-cyberware abilities) are fair game and were pulled as source material
  (`cp2077-2.0-perk-trees.txt`'s Relic Perks section) rather than excluded outright. Whether any given one
  gets used, and if so how, is a case-by-case call made during the actual conversion pass — not a rule
  applied uniformly here. This is the same "keep the mechanical shape, drop the branded lore" pattern the
  BG3 framework already established for its own deity-specific spells (`BG3_Conversion_Basis_of_Translation.md`
  Section 6).
- **Vehicle-combat-specific perks** (Stuntjock, Road Warrior's driving-specific clauses, Fury Road) — Inner
  Tepenia's vehicle/driving combat systems (if any exist) weren't confirmed during this framework pass; flag
  for later rather than assume a landing spot.
- **Smart Weapon targeting-lock mechanics** (Acquisition Specialist, Target Lock Transfer, Terminal Velocity)
  — depend on CP2077's specific "Smart Weapon" tech category and its homing-projectile behavior; only
  convertible once/if Inner Tepenia's own weapon system (see Section 6) defines an equivalent guided-weapon
  category.

---

## 6. Secondary Use — Weapon System Seed Material

**Worth flagging explicitly, distinct from the perk-conversion pipeline above:** a large fraction of the
CP2077 perk trees (Handguns, Assault, Blades, Annihilation/Shotguns, LMGs, Tech weapons) are perks *about*
specific weapon categories Inner Tepenia doesn't yet have a fleshed-out system for — see `TODO.md`'s own
"More weapons" and "Armor and clothing" backlog entries. Rather than force-fitting every Shotgun-specific or
Assault-Rifle-specific perk into a perk conversion, the weapon-category granularity itself (Pistols/Revolvers
split from Assault Rifles split from SMGs split from Shotguns split from LMGs, each with a distinct playstyle
identity) is valuable **input to that separate weapon-system design task**, independent of whether any
individual perk survives conversion. Don't lose this material to a strict perk-or-drop binary — some of it
answers a different open TODO item.

---

## 7. Process for Individual Conversion Passes

1. Check Section 1 first — is this already covered by Neural Overclock or Hacking/Traceability?
2. If not, run the Section 2 decision aid to land on an Outcome.
3. If Outcome 4 (drop), log it in Section 5 with a one-line reason.
4. If Outcome 1-2, use Section 3 to identify the correct governing skill/stat for thresholds.
5. Apply Section 4's resource mapping for any RAM/Stamina/Perk-Point/cyberware/crafting-tier element —
   treat the four flagged-open items as blocking questions to raise with the developer, not decisions to
   make unilaterally during a triage pass.
6. Cross-check Section 6 — if the entry is fundamentally about a weapon category rather than a trained
   ability, consider routing it to weapon-system design material instead of forcing a perk.
7. Name it and file it, same as the BG3 framework's own Section 7 steps 6-7.

**Status: framework complete, 2026-08-02. No individual CP2077 entries converted yet — that is the next
phase of work, and per Section 4, several resource-mapping questions (RAM, cyberware capacity, crafting
tiers) need developer input before that phase can fully proceed.**
