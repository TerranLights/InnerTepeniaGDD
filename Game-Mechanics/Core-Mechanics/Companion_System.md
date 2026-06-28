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

## Calethina: Not a Companion

Calethina does not occupy the companion slot and is not subject to companion system rules. She cannot be dismissed. She cannot be recruited in the conventional sense. She is present or absent based on signal state (before download) or always present (after download).

For implementation: she is a projection system, not a companion object. Any code that iterates over companions does not include Calethina.
