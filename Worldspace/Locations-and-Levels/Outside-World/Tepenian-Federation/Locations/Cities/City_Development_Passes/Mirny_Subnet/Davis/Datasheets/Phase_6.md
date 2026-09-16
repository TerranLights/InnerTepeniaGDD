# Davis — Datasheet · Phase 6 (Meaning)

> ⚠ **DRAFT — Tier C. ⛔⛔ CORRECTED 2026-09-15, caught on a later city's own equivalent check.**
> **This file previously claimed `Factions/Robot_Religions/` was an empty directory — that was FALSE, and the
> error survived unnoticed until a fresh check on a different city's Phase 6 turned up 6 real files.** Whatever
> command produced the original "0 files" claim did not actually enumerate that directory correctly. Fixed
> below; recorded as a self-audit failure, not silently corrected.

| Category | Value | Citation |
|---|---|---|
| `Factions/Robot_Religions/` roster — the actual content | **NOT empty.** Two developed religions exist: **Polydimensional Animism** (5 files — README, Beliefs, Rituals, Culture, Open_Questions; status "functional working copy, not locked final design canon") and **Cymatics Reverence** (1 file; status "placeholder name, early development" — reveres sound/vibration, rooted in robots' genuine wider sensory perception range) | Re-verified this turn: `find` returns 6 files across 2 religions |
| `Factions/Robot_Religions/` — Davis-specific hit | **Checked properly this time: neither religion names Davis anywhere** — a genuine zero-hit result, distinct from "the roster is empty" | Re-verified this turn: `grep -rln -i davis` returns 0 files |
| `National_Holidays.md` — Davis mention | Checked, **zero hits for Davis** by name | Re-verified this turn: `grep -i davis` returns 0 matches against 166 lines |
| `Ice-Cold_Buddhism_Research/` — relevance check | Checked, **zero hits for Davis** across all 7 files — genuinely not relevant, not merely unopened | Re-verified this turn: `grep -rl -i davis` returns 0 files |
| The RESERVED mortuary question | Not dispatched, per the Field Guide's own sequencing exclusion — RESERVED means RESERVED regardless of mechanical-ness | `00_Frame.md` §0.5 item 4 |

**Not mechanical / not included here:** the Naming technique, belief landscape, death-and-the-dead, the Failure
State of the Core Value, Observance generation — this phase's actual content, and where nearly all of it lives.
