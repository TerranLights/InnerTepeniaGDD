# Throwing Weapons (Blades)

**Scope, established 2026-07-23: this is a cross-project standing design law, not an Inner-Tepenia-only
mechanic.** The fundamental principle behind thrown blade weapons is identical across all four Tepenia
games — Inner Tepenia (top-down, turn-based, isometric) and all three planned Outer Tepenia trilogy titles
(1st-/3rd-person toggleable, real-time, 3D open-world), despite the very different engines and camera
systems. Only the *implementation* differs per game's own perspective/structure; the underlying rule does
not. Whenever Outer Tepenia's own design documents begin, this principle should carry forward from here
rather than being re-derived.

**Focus, per the original 2026-07-04 scoping (see `TODO.md`):** thrown blade weapons specifically —
throwing knives, tomahawks, and similar bladed forms — this file's own scope, and what Early Access ships
with. Fantasy-genre consumable throwables (BG3's alchemist's fire and similar) are explicitly excluded; a
separate Sci-Fi grenade system could cover that niche later, but it's a distinct idea from this one.

**A full "throw anything" system — confirmed Launch-exclusive, 2026-07-23.** A genuine Baldur's Gate 3-style
system letting the player throw any item, not just blades, is planned for the eventual full Launch release
specifically, not Early Access (see `Dev-Road-Map/Early_Access_vs_Launch_Content_Split.md`). Reasoning: it's
a real system requiring its own extensive planning and execution (every throwable item needs its own
weight/damage/behavior handling), not just a bigger version of the blade system this file covers. The
Universal Principle and per-game implementations below still apply once that system exists; this file
documents the blade-only Early Access baseline they'll build on top of.

---

## The Universal Principle

**A thrown blade stays exactly where it lands until the player retrieves it.** Whether it lands on open
ground, sticks into a wall or other surface, or hits an enemy, the weapon physically remains there — it is
not automatically returned to inventory, consumed, or despawned. Retrieval is a real, deliberate player
action in every game in the series. This is the one rule that never changes between Inner Tepenia and any
Outer Tepenia title.

---

## Inner Tepenia — Turn-Based Isometric Implementation

Because combat takes place on a bounded tactical grid, every throw necessarily lands *somewhere* within
that space — there's no "flies off into an unbounded open world and is lost" case to design around. Instead,
the constraint sits on the front end of the action: **whether the player can attempt the throw at all is
gated by distance to the target tile, checked against the throwing character's own stat modifiers** (Might,
Agility, and whichever others the eventual formula uses — see the stat-mapping dimensions still open in
`TODO.md`'s own Throwing Weapons entry). A throw beyond the character's effective range simply isn't a legal
action to select, rather than something that's attempted and then lost. Once thrown, the weapon lands on its
target tile (or wherever it resolves to) and sits there, retrievable like any other dropped item, consistent
with the Universal Principle above.

---

## Outer Tepenia Trilogy — Real-Time 3D Open-World Implementation

Because these games take place in a continuous, unbounded 3D space rather than a discrete grid, a thrown
weapon can genuinely travel somewhere the player has no practical way to reach — this game family needs a
distinct mechanic Inner Tepenia doesn't, to handle that case.

**Two separate ranges:**
- **Range/distance of effectiveness** — how far the weapon can be meaningfully thrown to begin with (damage,
  accuracy, or similar falloff considerations — exact mechanics TBD).
- **Range of reach** — a separate, retrieval-focused distance. If the weapon lands within this range, the
  player can walk over and pick it back up, per the Universal Principle. If it lands *beyond* this range, it
  is lost for good — with one confirmed exception, below.

**The iconic-weapon exception:** unique/signature ("iconic") thrown blades that land beyond the range of
reach do not stay lost — they automatically return to the player's inventory after a cooldown period
(example figure given: 15 seconds), rather than requiring a trek to go find them. **This exception only
applies when the throw doesn't hit anything.** If an iconic weapon actually connects with a surface or an
enemy, it behaves exactly like any ordinary thrown blade — it sticks where it landed and must be manually
retrieved like anything else. The auto-return-on-cooldown behavior is specifically a "the throw missed and
sailed out of practical reach" safety net, not a general convenience granted to iconic weapons at all times.

---

## Open Questions

- Inner Tepenia's exact stat-mapping formula for throw range/accuracy/crit chance/crit damage (tracked in
  `TODO.md`'s own Throwing Weapons entry, not duplicated here).
- Outer Tepenia's exact numeric values for range of effectiveness, range of reach, and the iconic-weapon
  cooldown duration (15 seconds given as an illustrative example only, not a locked number).
- Which specific weapons across the Outer Tepenia trilogy qualify as "iconic" — not yet designed, since none
  of those games have started real content design yet.
- Whether Outer Tepenia's own separate grenade-system idea (the Sci-Fi equivalent of BG3's consumable
  throwables) ever gets designed, and whether it shares any of this file's mechanics or is fully independent.
