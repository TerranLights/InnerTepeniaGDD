# Skills Review — Verb vs. Noun Audit

**What this is:** a working review document, not a design decision — created 2026-07-26 at the developer's
request, to print the full current 44-skill list in one place for a pass they intend to do themselves. The
concern raised: a lot of these entries read as things the player *does* (an action, a verb) rather than a
distinct skill the player *invests points in* (a stable domain, a noun) — the same critique that already got
Data Archaeology, Data Leakage, Subnet Optimization, and Information Verification & Analysis flagged for
cutting or moving to perks/traits elsewhere. The developer wants to look through the entire list with that
lens now, since "this entire thing will need to be addressed." Nothing below is edited or decided — this is
the current state of `Skills.md`, reproduced for review.

---

## Decisions Already Made in Conversation (2026-07-26), Not Yet Written to `Skills.md`

So this file is self-contained without needing to dig back through chat history:

- **Cryptography & Decryption** → rename to **Cryptography** alone (Decryption folds in; distinct discipline
  from Arcanet Navigation & Hacking, confirmed keeping it a skill).
- **Data Archaeology** → cut as a skill, becomes the perk **Data Archaeologist** (identity-noun perk naming
  convention, gated at 8 Calculation / 75 Cryptography — effect still undesigned).
- **Data Leakage & Information Warfare** → split. "Data Leakage" cut entirely (reads as a tactic, not an
  investable skill). "Information Warfare" moved to a new tentative Trait (`Traits.md`, Information/Cyber
  Warfare Traits section) — flagged for future review, not locked in.
- **Subnet Optimization** → cut (overlaps too much with Decentralized Systems Design and Arcanet Navigation &
  Hacking to justify a separate line).
- **Information Verification & Analysis** → cut (reads as something resolved through Investigation-stat
  checks plus Rumor & Network Intelligence, not a distinct skill).
- **New skill: Medicine** (Cancer district — Hospital & Care identity; treats both human and robot patients).
  Governing stat tentative — Calculation or Investigation, undecided.
- **New skill: Biology** (Aquarius district — Science/Innovation identity; distinct hard-science skill from
  Gemini's info/hacking flavor). Governing stat confirmed: **Calculation**.
- **New standing rule:** every skill is governed by exactly **one** MACHINE stat, not a 2-3 stat blend — the
  existing multi-stat blend belongs only to the separate "Skill Point Gain per Level" formula (which sizes
  the total point pool, not any individual skill's own scaling). See `feedback_skills_single_stat_rule`
  memory. This means **every multi-stat entry below is provisional** and will eventually need trimming to one
  stat — not done in this pass.
- Still open: 2 more backfill skill slots needed to fully restore the 44 total after the 4 cuts above (net:
  -4 skills, +2 skills so far = 2 more needed).

---

# Full Current (Tentative) Skill List

## Technical / Engineering (9)
- Biology (Humanity) // {{a subdivision of Fallout's "Science"}}
- Repair (Investigation)
- Lockpick (Investigation)
- Chemistry (Calculation) // {{a subdivision of Fallout's "Science"}}

###### Associated Perks
- Jury-Rigging (Agility + Investigation)
- Thermal Engineer (Calculation)
- Siligel Chemist (Calculation)
- Precision Maintenance (Agility + Engine)
- Power Grid Management (Engine + Calculation)
- Decentralized Systems (Calculation + Engine + Investigation)
- {{Undergrid Navigation & Salvaging}} // [to-be-renamed] (Agility + Investigation + Engine)
- Hydroponic Systems (Agility + Engine)

## Information / Data (8)
- Hacking (Calculation) // {{a subdivision of Fallout's "Science"}}
- Cryptography (Calculation) // {{a subdivision of Fallout's "Science"}}

###### Associated Perks
- Arcanet Navigation (Calculation + Investigation)
- Data Archaeologist (Calculation + Investigation)

## Social / Diplomatic (7)
- Deception (Nerve)
- Narrative (Humanity)
- Barter (Nerve)
- Speech (Humanity)
- Insight (Humanity)

###### Associated Perks
- Diplomatic Negotiation (Humanity + Nerve)
- Empathy Protocols (Humanity + Investigation)
- Reputation Management (Humanity + Nerve)
- {Companion Command & Loyalty} // [to-be-renamed] (Nerve + Humanity)
- History Buff

## Survival / Exploration (6)
- Survival (Engine)
- Medicine (Investigation)
- Sneak (Agility)
- Outdoorsman (Engine)
- Athletics (Might) // {{brute physical capability: forcing open jammed doors/hatches, swimming or hauling yourself somewhere under load, breaking down a barrier, feats of raw strength. The "can you overpower this" skill.}}
- Sleight of Hand (Agility)
- Acrobatics (Agility) // {{precision movement: balance on narrow ledges/collapsed structures, vaulting over obstacles or cover, tumbling/dodging, reduced fall damage, escaping restraints through flexibility rather than force. The "can you finesse your way past/through this" skill.}}

###### Associated Perks
- Frontier Survival (Engine + Nerve)
- Cold Adaptation (Engine + Nerve)
- Environmental Exploitation (Engine + Investigation)
- Ripple Reading (Investigation + Engine + Agility)
- Isolation (Nerve + Engine)
- Psychological Resilience (Nerve + Engine)
- Scavenger (Investigation)
- Hazard Navigation (Ice, Tunnels, Blackouts) (Agility + Investigation + Engine)

## Combat & Security (6)
- Blunt Melee (Might)
- Bladed Melee (Agility)
- Unarmed (Engine)
- Guns (Nerve)
- Energy Weapons (Calculation)
- Mechanical Weapons (Might)
- Explosives (Nerve)

###### Associated Perks
- Non-Lethal Restraint (Agility + Might)
- Subdual (Agility + Might)
- Improvised Weaponry (Might + Agility)
- Combat Jury-Rig (Might + Agility)
- Defensive Posturing (Might + Nerve)
- Endurance Fighting (Might + Nerve)
- Tactical Grid Combat (Agility + Calculation)
- Electronic Warfare (Calculation + Investigation)
- Threat Assessment (Investigation + Nerve)

## Specialized / Cultural (8)

###### Associated Perks
- Ossuary Resonance (Humanity + Nerve)
- Sonic Attunement (Agility + Humanity)
- Golden Eye Calibration (// quest-based perk)
- Holographic Projection (Calculation + Nerve + Engine) // {{using a data network to "project" a "decoy version" of yourself somewhere else;; the "decoy" can't manipulate anything. Its only function is distraction}}

### Not Yet Added to `Skills.md` (pending this review)


### Traits
- Information Warfare // {{functionality currently undetermined}}

---

## Open Questions

- Which of the skills above (beyond the four already flagged) read as a player *action* rather than an
  investable *skill*? Developer's own pass, not yet done.
- For every skill that survives this review, which single MACHINE stat should govern it (per the new
  single-stat rule)?
- What should fill the 2 remaining backfill slots once the cuts/additions above are finalized?
