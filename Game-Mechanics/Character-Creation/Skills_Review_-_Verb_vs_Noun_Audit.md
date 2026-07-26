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
- ~~Still open: 2 more backfill skill slots needed to fully restore the 44 total~~ — **resolved 2026-07-26:
  the 44 target itself is dropped.** That figure was written for the old design, where skills were doing
  double duty as what are now perks. With skills and perks correctly split apart, the current draft's real
  skill count is **25** (Technical/Engineering 4, Information/Data 2, Social/Diplomatic 5, Survival/Exploration
  7, Combat & Security 7, Specialized/Cultural 0 — perks-only category now) — confirmed as the actual target,
  no further backfilling needed. Notably closer to Fallout: New Vegas's own 13-skill count than to 44.
  **`Skills.md`'s own intro text ("There are 44 skills total") will need updating to reflect this once the
  full rewrite happens** — not done yet, this file is still just the review/staging draft.
- **Specialized/Cultural** category confirmed as a perks-only bucket (no top-level investable skill). It holds
  a genuine mix, not a uniform quest-gate rule: **Sonic Attunement** and **Golden Eye Calibration** are truly
  quest-gated (completion of the questline is the gate itself, so no stat/skill threshold on top). **Ossuary
  Resonance** is NOT quest-gated — it keeps its real `(Level 16, 7 Humanity, 7 Nerve)` requirement; it just
  didn't have an obviously-fitting category elsewhere, so it lives here as a catch-all rather than because it
  shares the quest-gate logic.
- **The four other former Specialized/Cultural skills — [NAME TBD] (all-stats unique progression), Robot
  Religion Insight, Cultural Performance & Resonance, Memory & Consciousness Manipulation — are cut entirely**,
  not relocated. Confirmed reasoning: these read as general player actions rather than something worth either
  a skill investment or a perk unlock.

---

# Full Current (Tentative) Skill List

## Technical / Engineering (9)
- Biology (Humanity) // {{a subdivision of Fallout's "Science"}}
- Repair (Investigation)
- Lockpick (Investigation)
- Chemistry (Calculation) // {{a subdivision of Fallout's "Science"}}

###### Associated Perks
- Jury-Rigging (80 Repair)
- Thermal Engineer (Level 12, 7 Calculation)
- Siligel Chemist (Level 8, 6 Calculation, 50 Chemistry)
- Precision Maintenance (7 Engine, 90 Repair)
- Power Grid Management (Level 12, 6 Engine, 6 Calculation)
- {{Undergrid Navigation & Salvaging}} // [to-be-renamed] (Level 10, 8 Agility, 7 Investigation, 7 Engine)
- Hydroponic Systems (50 Chemistry, 50 Biology)

## Information / Data (8)
- Hacking (Calculation) // {{a subdivision of Fallout's "Science"}}
- Cryptography (Calculation) // {{a subdivision of Fallout's "Science"}}

###### Associated Perks
- Arcanet Navigation (6 Calculation, 50 Hacking)
- Data Archaeologist (7 Calculation, 80 Cryptography)
- Decentralized Systems (7 Calculation, 75 Hacking)

## Social / Diplomatic (7)
- Deception (Nerve)
- Narrative (Humanity)
- Barter (Nerve)
- Speech (Humanity)
- Insight (Humanity)

###### Associated Perks
- Diplomat (8 Humanity, 7 Nerve, 80 Speech)
- Empathy Protocols (8 Humanity, 75 Insight)
- Reputation Management (7 Nerve, 80 Narrative)
- {Companion Command & Loyalty} // [to-be-renamed] (7 Nerve, 7 Humanity)
- History Buff // {{{mechanics currently undetermined}}}

## Survival / Exploration (6)
- Survival (Engine)
- Medicine (Investigation)
- Sneak (Agility)
- Outdoorsman (Engine)
- Athletics (Might) // {{brute physical capability: forcing open jammed doors/hatches, swimming or hauling yourself somewhere under load, breaking down a barrier, feats of raw strength. The "can you overpower this" skill.}}
- Sleight of Hand (Agility)
- Acrobatics (Agility) // {{precision movement: balance on narrow ledges/collapsed structures, vaulting over obstacles or cover, tumbling/dodging, reduced fall damage, escaping restraints through flexibility rather than force. The "can you finesse your way past/through this" skill.}}

###### Associated Perks
- Frontier Survival (8 Engine, 7 Nerve, 75 Outdoorsman)
- Cold Adaptation (7 Engine, 6 Nerve, 50 Outdoorsman)
- Environmental Exploitation (6 Engine, 7 Investigation, 50 Survival)
- {{{Ripple Reading}}} // [[[extremely tentative; flagged for either development or possible removal]]] (Investigation + Engine + Agility)
- {{{Isolation}}} // [[[extremely tentative; flagged for either development or possible removal]]] (Nerve + Engine)
- Psychological Resilience (Nerve + Engine) // {{{functionality and mechanics currently undetermined}}}
- Scavenger (7 Investigation, 50 Survival) // {{approximately akin to Fallout's "Scrounger"}}
- Hazard Navigation (Ice, Tunnels, Blackouts) (8 Agility ||OR|| 8 Investigation;; 50 Survival ||OR|| 75 Athletics ||OR|| 75 Acrobatics)

## Combat & Security (6)
- Blunt Melee (Might)
- Bladed Melee (Agility)
- Unarmed (Engine)
- Guns (Nerve)
- Energy Weapons (Calculation)
- Mechanical Weapons (Might)
- Explosives (Nerve)

###### Associated Perks
- Non-Lethal Neutralization (8 Might, 6 Agility ||OR|| 7 Humanity, 7 Nerve)
- Improvised Weaponry (6 Might, 6 Agility, 7 Calculation)
- Endurance Fighting (10 Might ||OR|| 7 Agility, 7 Nerve, 7 Engine)
- Tactical Grid Combat (8 Agility, 7 Calculation)
- Electronic Warfare (8 Calculation, 7 Investigation)
- Threat Assessment (8 Investigation, 7 Nerve)

## Specialized / Cultural (8)

###### Associated Perks
- Ossuary Resonance (Level 16, 7 Humanity, 7 Nerve)
- Sonic Attunement (// quest-based perk)
- Golden Eye Calibration (// quest-based perk)
- Holographic Projection (7 Calculation ||OR|| 8 Nerve, 8 Engine;; 60 Hacking ||OR|| 100 Sleight of Hand) // {{using a data network to "project" a "decoy version" of yourself somewhere else;; the "decoy" can't manipulate anything. Its only function is distraction}}

### Not Yet Added to `Skills.md` (pending this review)


### Traits
- Information Warfare // {{functionality currently undetermined}}

---

## Open Questions

- Which of the skills above (beyond the ones already flagged/cut) still read as a player *action* rather than
  an investable *skill*? Developer's own pass, ongoing.
- ~~For every skill that survives this review, which single MACHINE stat should govern it~~ — **resolved:**
  every current skill entry now has exactly one MACHINE stat.
- ~~What should fill the 2 remaining backfill slots~~ — **resolved 2026-07-26: nothing. 25 is the confirmed
  final skill count, no 44-total target to hit.**
