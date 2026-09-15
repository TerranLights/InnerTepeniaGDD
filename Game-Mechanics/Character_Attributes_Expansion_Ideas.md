# Character Attributes — Expansion Ideas (Skills, Traits, Perks)

**Status: brainstorm-stage. Nothing in this file is locked design** — a holding pen for possible future
additions across all of the character-attribute systems (Skills, Traits, and Perks — Level-Up, Challenge-Based,
and Temporary), created 2026-09-14 at the developer's request. Treat each candidate as something to evaluate
and formally design when its turn comes, not as shipped canon.

**Origin of this file:** a git-history review of `Skills.md`'s original 44-skill list (commit `3b5aa30`)
turned up a number of "X & Y" paired skill concepts that were split, merged, or cut outright during the
2026-07-26 restructure down to 25 single-stat skills. The developer's own read: *"Some of the suggestions I
eliminated actually could theoretically be used somewhere somehow."* This file exists to hold those candidates
(and any future ones) somewhere findable, sorted by which attribute type they'd actually fit into now, rather
than leaving them buried in commit history.

**The full raw findings from that review are preserved at the bottom of this file, unedited, for reference.**

---

## Candidate Additions, Organized by Attribute Type

### Skills

- **Network Intelligence** *(originally half of "Rumor & Network Intelligence," Investigation + Humanity, cut
  entirely, never replaced by any perk)* — the structural side of that old pair: tracing information flow, who
  knows what and how it moves. Worth reconsidering as its own skill specifically because **Leyline** (the
  national social-media network, `project_leyline`, mechanism still TBD) has no gameplay hook yet — this could
  be the mechanism that finally gives Leyline something to *do* in play.
- **Rumor Mill** *(the other half of "Rumor & Network Intelligence," previously dropped when this file first
  folded the pair down to Network Intelligence alone — restored as its own item)* — the social side of that old
  pair: cultivating, tracking, and deliberately seeding word-of-mouth, distinct from Network Intelligence's more
  structural/formal information-gathering. A separate skill in its own right, not a second half of a compound
  one.

### Traits

- **Isolation** and **Psychological Resilience**, split apart *(originally one paired skill, "Isolation &
  Psychological Resilience," Nerve + Engine — cut as a skill; only ever resolved into one generic "Isolation
  Protocol" perk, the two halves never cleanly separated)* — these read more like Trait material than skill
  material: a standing psychological disposition (how a character handles prolonged isolation vs. how
  resilient they are generally) fits `Traits.md`'s existing pattern of dual-edged psychological profiles better
  than a skill investment does.
- **Pre-War History** *(originally half of "Pre-War Lore & History," Calculation + Investigation, cut entirely,
  no perk ever made)* — the documented, factual-record side of that old pair. A flavorful knowledge-domain that
  reads more like a background/history-buff Trait than an investable skill; could also work as a Perk (see
  World & Discovery below) — worth a direct call on which.
- **Pre-War Lore** *(the other half of "Pre-War Lore & History," previously dropped when this file first folded
  the pair down to Pre-War History alone — restored as its own item)* — the myths/legends/folklore side of that
  old pair, distinct from History's factual-record focus. Same open question as History above: Trait or Perk.

### Perks — Level-Up

- **Consciousness Manipulation** *(originally half of "Memory & Consciousness Manipulation," Calculation +
  Investigation, cut entirely as Specialized/Cultural, no perk ever made)* — **the strongest candidate in this
  whole list.** This sits directly on the project's own robot-consciousness north-star
  (`user_creative_principles`). A cut idea about manipulating consciousness, in a setting whose entire creative
  core is robot personhood and consciousness, deserves real reconsideration rather than being a casualty of a
  naming-convention cleanup. Likely shape: a Level-Up perk gated on Calculation + Investigation, possibly
  Bridge Unit/Jack-In-adjacent (`project_bridge_unit_and_jackin`) given the thematic overlap.
- **Memory Manipulation** *(the other half of "Memory & Consciousness Manipulation," previously dropped when
  this file first folded the pair down to Consciousness Manipulation alone — restored as its own item)* — a
  narrower, distinct perk from Consciousness Manipulation above: specifically altering, implanting, or erasing
  memory, rather than consciousness more broadly. The two could coexist as separate perks, or even as a
  branching pair (see `feedback_dual_outcome_companion_perks` for the project's existing branching-perk
  pattern, though this would be a player perk, not a companion one) — worth its own design pass rather than
  assuming one implies the other.
- **"AI Interaction," as its own idea distinct from "AI Diplomat"** *(originally half of "Holographic
  Projection & AI Interaction" — Holographic Projection became its own perk; AI Interaction survives only
  loosely through the existing "AI Diplomat" perk)* — AI Diplomat is specifically about *negotiation*. A
  broader "AI Interaction" perk — general fluency interfacing with AI systems, not specifically diplomatic
  standing — could be a distinct, non-redundant perk worth designing separately.
- **Ripple Reading, as its own named perk** *(flagged "extremely tentative" in the original audit, absorbed
  generically into the "Ripple Weaver" perk, never given its own identity)* — predicting power-grid ripples and
  blackouts is currently folded into a broader Environmental Exploitation-adjacent perk. Splitting it back out
  as its own perk (reading ripples specifically, almost divinatory in flavor, distinct from exploiting the
  hazards they create) could be a more distinctive identity-noun perk per `feedback_perk_naming_convention`.
- **Cultural Performance** *(originally half of "Cultural Performance & Resonance," cut entirely as
  Specialized/Cultural, explicitly as "a general player action," no perk ever made)* — Specialized/Cultural
  survives today only as a perks-only bucket (Ossuary Resonance, Sonic Attunement, Golden Eye Calibration,
  Holographic Projection). This concept fits that bucket's existing shape (quest-gated, culture-specific)
  better than it ever fit as a skill.
- **Cultural Resonance** *(the other half of "Cultural Performance & Resonance," previously dropped when this
  file first folded the pair down to Cultural Performance alone — restored as its own item, renamed slightly
  from bare "Resonance" to avoid colliding with the existing Ossuary Resonance and Sonic Attunement perks)* — a
  distinct concept from Cultural Performance above: an attunement to a culture's practices generally, rather
  than the act of performing within one. Worth checking against Ossuary Resonance and Sonic Attunement before
  designing, to confirm it's genuinely non-redundant with either rather than a third variation on the same
  idea.
- **Repurposing, as a distinct idea from Jury-Rigging** *(originally paired as "Jury-Rigging & Repurposing";
  Jury-Rigging survived as a perk, Repurposing has no distinct trace anywhere)* — could be a lower-tier perk or
  perk rank in its own right (turning found materials into something usable more broadly, distinct from
  Jury-Rig's specific "repair with mismatched parts" framing) rather than being silently absorbed.
- **Defensive Posturing, as a standalone combat perk** *(originally half of "Defensive Posturing & Endurance
  Fighting"; Endurance Fighting became its own perk, Defensive Posturing's distinct identity is gone — the
  perks that used to gate on it were retargeted to raw Athletics/Acrobatics/Survival instead)* — a genuine
  defensive-stance/technique perk, distinct from raw endurance, could still be designed as its own thing rather
  than staying folded away.

### Perks — Challenge-Based

- No specific candidates identified yet from the recovered list — the cut concepts above read as level-up or
  quest-adjacent material, not task/challenge-triggered. Worth revisiting once `Challenge_Perks_-_Task-Based.md`
  gets its own expansion pass.

### Perks — Temporary

**Note: "Temporary" is not yet a formalized perk category.** `Perk_Framework.md` currently defines Tier 1
(Level-Up) and Tier 2 (Earned: Challenge, Companion, Quest/Choice, District Capstone, Skill Milestone, World &
Discovery, Idolization) — there's no existing tier for a perk that expires, is consumable-triggered, or is
otherwise non-permanent. Before candidate ideas get sorted into this bucket, the category itself needs a first
design pass: what triggers a temporary perk (an item, a location, a story state?), how long it lasts, and
whether it stacks with permanent perks of the same effect. Flagging this as an open structural gap surfaced by
this review, not something to guess at here.

---

## Loose Ends Needing Resolution (Not New Ideas — Already-Broken References)

These aren't candidate additions — they're bugs the git-history review surfaced: places where a cut skill's
name is still doing load-bearing work somewhere it shouldn't be.

- **"Combat Jury-Rig" is still a live dangling reference.** Two perks in `Regular_Perks_-_Level-Up.md`
  (**Improvised Lethality**, **Steady Retrieval**) still list `Improvised Weaponry & Combat Jury-Rig` as a
  literal requirement string, even though that skill was split apart and no longer exists under that name.
  Needs an actual retargeting decision (most likely to Might, matching how its sibling perks were resolved),
  not just a flag.
- **"Faction Rhetoric" is inconsistently dead.** It was one of the original 44 skills (Social/Diplomatic,
  Humanity + Nerve — not a paired name, a single skill), cut during the restructure with no explicit callout in
  any commit message. But it's still referenced as if it exists in `MACHINE_Stat_Influence_Map.md`,
  `Nerve_Expanded_Systems_Tentative.md`, and the old `skill_list_preliminary_suggestions_-_possible_basis_for_perks.md`
  scratch file. Either it needs a real replacement (perk or trait) or those references need cleaning up to stop
  citing a skill that no longer exists.

---

## Reference: Full Findings From the Git-History Review (2026-09-14)

**Preserved verbatim from the review that produced this file, for an unedited record of what was checked and
where each concept actually ended up.**

### The original 44-skill list, before any splitting (commit `3b5aa30`)

**Technical/Engineering:** Thermal Engineering · Precision Maintenance & Repair · Jury-Rigging & Repurposing ·
Siligel Chemistry · Decentralized Systems Design · Undergrid Navigation & Salvaging · Hydroponic Systems ·
Highway Maintenance & Transit Systems · Power Grid Management

**Information/Data:** Data Archaeology · Arcanet Navigation & Hacking · Information Verification & Analysis ·
Rumor & Network Intelligence · Cryptography & Decryption · Pre-War Lore & History · Subnet Optimization · Data
Leakage & Information Warfare

**Social/Diplomatic:** Diplomatic Negotiation · Empathy Protocols · Faction & Reputation Management · Deception
& Narrative Crafting · Faction Rhetoric · Moral Philosophy & Ethical Reasoning · Companion Command & Loyalty

**Survival/Exploration:** Frontier Survival & Cold Adaptation · Environmental Exploitation & Ripple Reading ·
Stealth & Infiltration · Isolation & Psychological Resilience · Scavenging & Resource Foraging · Hazard
Navigation

**Combat & Security:** Non-Lethal Restraint & Subdual · Improvised Weaponry & Combat Jury-Rig · Defensive
Posturing & Endurance Fighting · Tactical Grid Combat · Electronic Warfare · Threat Assessment

**Specialized/Cultural:** Ossuary Resonance · Sonic Attunement · Golden Eye Calibration · Holographic
Projection & AI Interaction · Bridge Protocol Mastery · Robot Religion Insight · Cultural Performance &
Resonance · Memory & Consciousness Manipulation

### What happened to each pair, traced through to today

| Pair | Final fate |
|---|---|
| Precision Maintenance & Repair | Split, both kept — Repair (skill), Precision Maintenance (perk) |
| Jury-Rigging & Repurposing | Partial — Jury-Rigging survived as a perk; Repurposing has no distinct trace anywhere |
| Undergrid Navigation & Salvaging | Partial — skill cut, but "Undergrid Runner" perk survived, re-gated on raw stats |
| Highway Maintenance & Transit Systems | Total loss — skill cut, and its perk "Transit Authority" cut too, called "confirmed-unimplementable" |
| Arcanet Navigation & Hacking | Split, both kept — Hacking (skill), Arcanet Navigation (perk) |
| Information Verification & Analysis | Partial — skill cut, but "Pattern Intuition" perk survived, retargeted |
| Rumor & Network Intelligence | Total loss — cut, no perk ever made |
| Cryptography & Decryption | Kept — renamed "Cryptography," Decryption folded in |
| Pre-War Lore & History | Total loss — cut, no perk ever made |
| Data Leakage & Information Warfare | Partial — Data Leakage cut outright; Information Warfare reborn as a Trait with a "Data Leak" action |
| Faction & Reputation Management | Kept — perk "Reputation Management," Faction folded in |
| Deception & Narrative Crafting | Split, both kept as skills — Deception, Narrative |
| Moral Philosophy & Ethical Reasoning | Partial — skill cut; "Moral Authority" perk survived with the skill-gate dropped |
| Companion Command & Loyalty | Kept in spirit — skill cut, but several perks carry the concept (Companion Cohesion, Trusted Command, Shared Experience, Bond Ledger, Grief Ledger, plus one still literally flagged `[NAME PENDING]`) |
| Frontier Survival & Cold Adaptation | Split, both kept as separate perks |
| Environmental Exploitation & Ripple Reading | Partial — Environmental Exploitation kept as a perk; Ripple Reading never got its own resolution, absorbed loosely into "Ripple Weaver" |
| Stealth & Infiltration | Kept — became skill "Sneak," Infiltration folded in |
| Isolation & Psychological Resilience | Still murky — flagged "tentative/undesigned" mid-process; only ever resolved into one generic "Isolation Protocol" perk, the two halves never cleanly separated |
| Scavenging & Resource Foraging | Kept — Scavenging → perk "Scavenger"; Resource Foraging absorbed into "Resource Recovery"/"Salvage Instinct" |
| Non-Lethal Restraint & Subdual | Merged into one new perk, "Non-Lethal Neutralization" |
| Improvised Weaponry & Combat Jury-Rig | Still genuinely unresolved — "Improvised Weaponry" became its own perk; "Combat Jury-Rig" was never given a real replacement, two perks still reference the dead compound name |
| Defensive Posturing & Endurance Fighting | Partial — "Endurance Fighting" became its own perk; "Defensive Posturing" as a distinct idea is gone |
| Holographic Projection & AI Interaction | Partial — Holographic Projection became its own perk; "AI Interaction" survives loosely through "AI Diplomat" |
| Cultural Performance & Resonance | Total loss — cut entirely as a "general player action," no perk ever made |
| Memory & Consciousness Manipulation | Total loss — cut entirely, no perk ever made |

**Also cut, not part of an "&" pair:** Robot Religion Insight (perk "Robot Theologian" survived, skill-gate
dropped) · Bridge Protocol Mastery / `[NAME TBD]` (total loss, but was never even named — low recovery value) ·
Faction Rhetoric (total loss as a skill, but still inconsistently referenced elsewhere — see Loose Ends above).
