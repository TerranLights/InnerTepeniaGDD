# Denison — Datasheet · Step −1 (Input Contract)

> ⚠⚠ **DRAFT — Tier C.** Denison's own ULM pass has NOT started. No admissibility ruling exists on
> the Specs read-range — that is Step −1's own derivation work, not a mechanical lookup.

## Specs file — bibliographic facts

| Category | Value | Citation |
|---|---|---|
| Location | `Cities/Specs/Janbogo subnet/Denison.md` — ⛔ folder is `Janbogo subnet`, space + lowercase `s` | Verified this turn |
| Length | 362 lines total | `wc -l`, verified this turn |
| Identity | Denison | `Specs/Denison.md` L1 |

## Verbatim, admissible header fields

```
**Based on:** Cape Denison, Commonwealth Bay, George V Land, East Antarctica (~67°00'S, 142°40'E) —
main base of Douglas Mawson's Australasian Antarctic Expedition (1911–1914)
**Status:** Destroyed                                    ⛔ POST-WAR — see exclusion table below
**Arcanet Subnet:** Janbogo
**Access type:** ON
**Highway access:** Hwy 183 (the Janbogo Highway).
**Significance:** Among the windiest permanent habitation sites at sea level on Earth (avg ~80 km/h,
gusts 300+ km/h); founded on the legendary Mawson expedition site; "Home of the Blizzard" — the one
Tepenian city whose civic identity is built on open pride in environmental extremity rather than
quiet endurance
**DLC:** Janbogo subnet — DLC 6 (Janbogo Region); Destroyed city, ruins accessible   ⛔ POST-WAR HALF
```
— `Specs/Denison.md` L3–9. **Highway access: Hwy 183.**

```
Note (created 2026-07-05): This file did not previously exist — all of Denison's established lore
lived only in Local_Cultures/Janbogo_Subnet/Denison.md, which remains the authoritative source for
its culture. This file exists to give Denison the same Specs-level population/geography
documentation every other Tepenian city has.
```
— `Specs/Denison.md` L11, trimmed of a clause naming the corpus-wide sweep by cross-reference.

## Census I / II — repeated here, full derivation in `Step_0.md`

```
Census I (Pre-Orbital Era): 444,529 humans / 461,693 robots / 906,222 combined
Census II (Orbital Era): 285,085 humans / 338,392 robots / 623,477 combined
```
— `Specs/Denison.md` L17–18. ⛔ *The word `(destroyed)` that follows Census II in the source is
excluded — post-war tag on an otherwise-admissible population figure.*

Cross-verified against `Official_Population_Census.md`, Denison's own two rows:
```
L500: | 17 | Denison | Janbogo | 444,529 | 461,693 | 906,222 |
L615: | 16 | Denison | Janbogo | 285,085 | 338,392 | 623,477 |
```
— exact match on H/R/combined for both censuses.

## Overflow — Denison's own two rows, held, unassigned

```
| Denison | I | 78,446 | 81,475 | 159,921 | ⭐ −15%, developer ruling 2026-09-05. Extent declared
~50 km² two-zone; not a Gate 11 failure | ⏸️ HELD — unassigned
| Denison | II | 50,309 | 59,716 | 110,025 | scaled at −15%, retention preserved | ⏸️ HELD —
unassigned
```
— `Official_Population_Census.md` L705–706. **Denison's own figures only — nothing else from that
table is reproduced here.**

## ⛔⛔ WAR-CONTENT SECTIONS SEEN AND EXCLUDED — per `M-171`, never quoted beyond naming the section

| Section | What it contains (named, not quoted) | Disposition |
|---|---|---|
| `## Current Status / Destruction` (Specs L342–347) | A retention-percentage pair computed at the moment of destruction | ⛔ **EXCLUDED WHOLE** |
| `## Legacy` (Specs L350–352) | Retrospective, post-destruction framing | ⛔ **EXCLUDED WHOLE** |
| `## Connection to Concordia` (Specs L336–338) | Post-war diaspora detail | ⛔ **EXCLUDED WHOLE** |

⭐ **The retention percentage admissible for this city is computed fresh in `Step_1_and_2.md`, from
the two Census I/II rows above.**

## Developer Vision Notes — verbatim, in full

```
# Denison — Developer Vision Notes
Purpose: A running record of the developer's own creative vision for this city — distinct from
Specs/Denison.md (established facts) and Local_Cultures/Janbogo_Subnet/Denison.md (32-section
post-culture spec). This file captures open questions asked, answers given, and anything newly
established through direct conversation.
Session date: 2026-07-05

## The developer's vision
The city functions as one continuous, interlinked structure rather than separate buildings —
comprehensively joined throughout — with a handful of landmark structures recognizable even at a
distance through blowing snow. The most extreme wind-engineering identity of any Tepenian city.

## Corrections/additions applied directly to other files this session
- Specs/Denison.md and Local_Cultures/Janbogo_Subnet/Denison.md — the fully-interlinked
single-structure city concept and the wind-engineering identity.
- This session flagged that Denison had no Specs/ file at all — created immediately after.
- A second flagged gap — no post-war refugee faction — was explicitly confirmed by the developer as
not obligatory, so it's left open, not tracked as a to-do.

## Still open
- No post-war refugee faction (confirmed not obligatory, left open by choice)   ⛔ POST-WAR
```
— `City_Vision_Notes/Denison.md`, full 25 lines.

**Not mechanical / not included here:** the admitted read-range, the four-category classification
(PROVIDED/RESERVED/PRODUCED/REQUESTED), any generator presence/absence call, the type-modifier
declaration — none of this exists until Denison's own Step −1 actually runs.
