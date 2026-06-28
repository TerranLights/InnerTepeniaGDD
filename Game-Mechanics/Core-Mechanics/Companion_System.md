# Companion System

## Party Composition

The player's active party consists of:

- **The protagonist** (player character)
- **Calethina** — always present as a holographic projection from the wrist device; not a companion in the mechanical or code sense (no companion slot, no companion system triggers). Her projection quality varies by signal state before the midpoint download; stable and clean everywhere after. She is a constant presence regardless of which companion the player has recruited.
- **One recruited companion** — the single companion slot

**Maximum active party size: 3** (protagonist + Calethina + 1 companion)

This is a hard limit. The player can recruit only one companion at a time. Recruiting a new companion requires dismissing the current one.

---

## Design Rationale

Calethina's constant presence as a projection already gives the player a second meaningful relationship at all times. Adding a full companion on top of that creates a three-entity dynamic (protagonist + Calethina + companion) that preserves the Fallout-adjacent feel of a protagonist with support rather than a party. Allowing two companion slots would produce four de-facto party members — a meaningfully different emotional and tactical register, closer to a party-based RPG than the intended design.

The single companion slot means each companion choice is a genuine commitment. The player leaves 9–11 companions behind per playthrough (based on a main game pool of 10–12 recruitable companions), which drives meaningful replayability without trivializing the decision.

**Fallout precedent:** Fallout: New Vegas allows 1 humanoid + 1 non-humanoid companion simultaneously. Inner Tepenia's model — 1 companion slot + Calethina as a persistent non-slot presence — achieves the same effective dynamic while keeping Calethina architecturally distinct from the companion system.

---

## Total Recruitable Pool

**Main game target: TBD — higher than originally estimated.** The pool should be large enough that multiple playthroughs feel genuinely different. Specific count to be established as character design work progresses.

Currently confirmed recruitable companions (5):
1. Favi della Torre
2. Villena Hiresvett
3. Naizelle d'Edjordoś
4. Seica Cenilaithe
5. Ji-Eun Kim

Additional recruitable companions to be designed. Some TBN characters may be recruitable; classification TBD per character.

**DLC companions** (separate from main game pool, available only in their respective DLC):
- Kendra Heinrich (DLC 1: South Pole)
- Salagéa Aparast (DLC 5: Atlantic Coastal Region)

---

## Major NPCs Who Are Not Recruitable Companions

Some characters have complete questlines and deep player relationships but do not join the party. They are major NPCs, not companions.

### Trisha Miller — Radio Host

Trisha runs her radio show and does not leave that role. She cannot be recruited as a companion.

**Post-questline mechanic:** Trisha's relationship with the player — built through her questline, through the player's choices, through help given or betrayal committed — is expressed through her radio show. After the questline resolves, she talks about the player on air. What she says reflects how the events played out. Players who helped her get one version; players who betrayed her get another; players who made complicated choices in between get something that reflects that complexity.

This makes her radio show a form of world-state feedback: Concordia hears what Trisha says about the player, and NPCs may reference having heard the broadcast. She is one of the primary ways the game communicates reputation back to the player through the world's voice rather than through a UI element.

### Majyao Bisyugota — Teahouse Keeper

Majyao runs her teahouse and does not leave it. She cannot be recruited as a companion. Her questline is large and consequential; its resolution plays out through the teahouse and through Concordia's political landscape, not through party membership.

---

## Companion Slot Rules

- Only one companion may be active at a time
- Dismissing a companion returns them to a fixed location in Concordia (they do not disappear from the world)
- Dismissed companions retain all relationship progress and questline state
- A companion's personal questline can only advance while they are the active companion
- Re-recruiting a dismissed companion is always available unless a specific story event has permanently changed their status

---

## Romance System

### Scope

Romance is available for all recruitable companions and a small number of named NPCs where it makes contextual sense for the character. It is not a universal system applied to every named NPC — that would be excessive and dilute the significance of the relationships that have it.

**Pool:** All companions (main game + DLC) + select named NPCs (Trisha Miller is a strong candidate; others to be identified on a per-character basis during design).

### The Double Gate

Romance requires two independent conditions to be met simultaneously. Failing either one closes the route.

**Gate 1 — Questline prerequisite:** The player must have completed the relevant relationship-building questline content with this character. The relationship has to have been built through shared experience and choices, not just dialogue options. This gate is the same for all characters.

**Gate 2 — MACHINE stat / trait threshold:** Each character has a specific profile of what they find attractive, derived from their personality, sensibilities, and history. The player's MACHINE stats and traits must meet that profile. This gate is unique per character.

**Perks are explicitly excluded from Gate 2.** MACHINE stats and traits are chosen at character creation — they define who the player character fundamentally *is*. Perks are acquired through play — they represent what the character has learned and done. The romance gate is about fundamental identity, not accumulated experience. A player cannot perk their way into a romance they weren't built for.

### Threshold Design Per Character

When designing each romanceable character, specify:
- Which MACHINE stat(s) are required and at what level
- Which traits (if any) are required or are dealbreakers
- The in-world rationale (what this person finds attractive and why, based on their personality)

Examples of how thresholds might read:
- A character who values physical presence → Might threshold
- A character who values intelligence and wit → Calculation threshold
- A character who values genuine emotional depth → Humanity threshold
- A character who admires courage and directness → Nerve threshold
- A character who values perceptiveness → Investigation threshold
- A character who values capability and endurance → Engine threshold

Multiple stats may be required. Traits may open or close routes regardless of stat levels.

### The Signal

When a player has completed the questline prerequisite but does not meet the stat/trait threshold, the character makes an honest, casual, in-voice remark that reveals what they're looking for — without breaking the fiction or explaining the system. The line is short and in character. It closes the romantic door without closing the relationship.

Examples of the register (not final lines — those are written per character in voice):
- *"Sorry, friend. I like them smart."*
- *"Not trying to be rude here, but come back once you've lifted some weights."*
- *"You're good people. Just not my type."*

The player who hears this line has a clear signal. On a replay with a different build, they know what to work toward. The line is delivered once and not repeated unless the player re-initiates.

### Thematic Note

The romance system is a direct expression of the second guiding principle — the nature of love between robots and humans. Every romance in the game, regardless of the species of the characters involved, is asking: what does this specific person find in this specific other person, and what does that mean for both of them? The stat/trait gate ensures that the answer is always grounded in who the player character actually is, not in what they've done or what perks they've accumulated.

---

## Calethina: Not a Companion

Calethina does not occupy the companion slot and is not subject to companion system rules. She cannot be dismissed. She cannot be recruited in the conventional sense. She is present or absent based on signal state (before download) or always present (after download).

For implementation: she is a projection system, not a companion object. Any code that iterates over companions does not include Calethina.
