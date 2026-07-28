# Permanent MACHINE Stat Increases

**What this is:** a design draft, not a locked decision — written 2026-07-27. Establishes the two mechanisms
by which a player character's MACHINE stats can permanently grow beyond the 5+5 character-creation budget
(`Character_Creation_Overview.md`), distinct from — and compatible with — the existing re-spec system
(`Core-Mechanics/Player_Re-Spec_-_Complete_Design.md`), which *redistributes* the player's existing stat
budget at a real Identity Fragmentation cost rather than growing it. These two systems don't conflict: re-spec
moves points you already have; the mechanisms below add new points to the total pool.

**Hard ceiling, unchanged:** MACHINE stats remain capped at 10 regardless of source — character creation,
Intense Training, or implants. Neither mechanism below can push a stat past that ceiling.

---

## Mechanism 1 — Intense Training (Perk)

**Ported directly from FNV, per developer confirmation 2026-07-27** — reverses an earlier call in
`Perks/FNV_Perk_Cross_Reference_Audit.md`'s "Not Portable As-Is" bucket, which had reasoned that a free stat
increment would undercut the re-spec system's own cost structure. The developer confirmed this perk is wanted
after all; the audit file has been corrected to match (see that file's own updated entry).

**Effect, verified against the real perk 2026-07-27:** Level 2, no other requirement, repeatable **up to 10
times total** across a playthrough — each rank grants a single, permanent +1 to any one MACHINE stat of the
player's choice, chosen at the moment that rank is taken. Written into `Perks/Regular_Perks_-_Level-Up.md`'s
Growth/Learning category with these verified numbers.

**A nice confirmation, found while verifying this perk:** the real FNV wiki entry notes that points from
Intense Training put into Endurance specifically grant "more implants" at Doctor Usanagi — validating the
Engine-substitutes-Endurance design choice below independently, since the two systems already interact the
same way in the source material this is adapted from.

---

## Mechanism 2 — Implants ("not-Doctor-Usanagi" NPCs)

**A second, distinct route to permanent stat growth**, gated through a recurring NPC archetype rather than a
level-up perk choice — multiple such NPCs exist across Concordia's districts (a "not-Doctor-Usanagi" in
Cancer, another in Scorpio, and presumably others elsewhere), each capable of performing the same kind of
procedure.

**The two-part limit, confirmed 2026-07-27:**

1. **Total implant count is capped by the player's Engine stat.** Engine substitutes for FNV's Endurance here
   (Doctor Usanagi's own real gate stat), matching Engine's already-established role as the
   bodily-durability/recovery-speed stat in Inner Tepenia's system. A player with Engine 6 can safely receive
   up to 6 total implants, across all 7 MACHINE stats combined.
2. **Each of the 7 MACHINE stats can only ever receive ONE implant, period — no stacking a second +1 onto the
   same stat, regardless of how many Engine-based slots the player has left.** This is a real, physical
   "this specific augmentation site has already been modified" limit, independent of the total-slot count.
   Practical effect: a player who has already had Calculation implanted once will be refused by *any*
   "not-Doctor-Usanagi," anywhere in the city, not just the one who performed the original procedure —
   visiting a different district's practitioner doesn't reset or bypass this per-stat limit.

**Refusal flavor, confirmed by example:** a player who received a Calculation implant from the Cancer
practitioner, then requests a *second* Calculation implant from the Scorpio practitioner, is turned down with
something to the effect of: *"I'm sorry, but your frame just can't handle this. I'd be putting you in
danger."* The refusal is about the specific stat already being modified, not about the player's remaining
implant capacity — even a player with Engine-based slots to spare gets this same refusal if they try to
double up on one stat.

**Practical ceiling this creates:** since only 7 MACHINE stats exist, the real maximum number of implants any
player can ever receive is `min(Engine stat value, 7)` — a player with Engine 8+ can't actually use their full
slot allowance unless implants exist for all 7 stats; a player with Engine 4 or lower will always have some
stats permanently inaccessible to implant-based growth, regardless of how many different practitioners they
visit.

**NPC identity, confirmed 2026-07-27:** each "not-Doctor-Usanagi" is a named, individual character per
district — not a generic, replicated archetype. **Their in-game function is limited to the implant procedure
itself, with one deliberate exception: ordinary conversation.** They carry no other mechanical role (no
questline, no faction tie confirmed, no companion potential established here) — their value beyond the
procedure is purely the natural, organic lore-dropping a named local practitioner can offer through dialogue,
the same way plenty of non-recruitable named NPCs elsewhere in the game exist mainly to texture their
district rather than drive a quest.

---

## Open Questions

- ~~Whether "not-Doctor-Usanagi" NPCs are meant to be named, distinct individual characters or a more generic,
  replicated archetype~~ — **resolved 2026-07-27:** named individuals per district, mechanically limited to
  the implant procedure plus ordinary conversation/lore-dropping, no other in-game function.
- Whether every district has one, or only some — not yet decided.
- Cost/price for an implant procedure, and whether it requires anything beyond credits (a quest, a reputation
  threshold, specific materials) — not yet designed.
- ~~Whether Intense Training can be taken multiple times~~ — **resolved 2026-07-27, verified against the real
  perk:** yes, up to 10 times total, Level 2 requirement, no other gate.
