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

**Main game target: 10–12 recruitable companions** (not counting Calethina).

Currently confirmed (7):
1. Favi della Torre
2. Villena Hiresvett
3. Trisha Miller
4. Majyao Bisyugota
5. Naizelle d'Edjordoś
6. Seica Cenilaithe
7. Ji-Eun Kim

3–5 additional companions to be designed as the GDD develops. Some TBN characters may be recruitable; classification TBD per character.

**DLC companions** (separate from main game pool, available only in their respective DLC):
- Kendra Heinrich (DLC 1: South Pole)
- Salagéa Aparast (DLC 5: Atlantic Coastal Region)

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
