# CULTURAL SYNTHESIS — INPUT AVAILABILITY

**Checked 2026-09-05**, for the run starting 2026-09-06. **Companion to `ULM_Piece_Index.md`.**
**Subject: `Worldspace/Locations-and-Levels/Cultural_Synthesis_Techniques.md`** — *17 techniques plus one
extension.*

> ## ✅ NOTHING BLOCKS THE RUN. **One input is missing and it degrades gracefully.**

---

## What each technique needs, and whether it exists

| Technique | Requires | |
|---|---|---|
| **1–12** *(Bounded Personal Franchise → Native Before Transplanted)* | **the location's own established character** — Phases 1–9 | ✅ **Produced by the ULM pass itself.** These consume its output; they need nothing pre-staged |
| **13 · The Unused-Tier Mine** | **① tiered real-world picks** | ✅ **37/37 city blocks carry a Primary.** *`Inspirational-Influences.md`, tokens `[PRIMARY]` · `[SECONDARY]` · `[SUPPORTING]` — 62 / 83 / 26* |
| | ⛔ **② a record of which picks are UNUSED** | ⛔ **DOES NOT EXIST FOR CITIES** — see below |
| **14 · The Population Share Check** | the general-population discipline | ✅ `Concordia-City/Districts/Phase_Instructions/00b_General_Population_Discipline.md` |
| **Borrowed Form** · **The Unrecognized Instrument** | the location's own material | ✅ produced by the pass |
| **The Zodiac Lens** | **12 signs, full attributes** | ✅ **12/12** — `Reference/Real-World/Zodiac_Signs_Full_Attributes.md` |
| **Extension · Elemental/Planetary Cross-Check** | **8 Robot Elementals** | ✅ **8/8** — *Earth · Air · Fire · Water · Wood · Metal · Electricity · Electromagnetism* |
| | **10 Planetary Symbols** *(9 planets + the Asteroid Belt)* | ✅ **10/10** |

⭐ **So the Cross-Check's full load is supported: 18 self-checks per sign × 12 signs = 216 combinations.**

---

## ⛔ THE ONE GAP — technique 13's second input

**Its question is:** *"Which of this location's picks has **nothing in the existing material actually derived
from it**?"* **That needs the tiers *and* a record of what has already been spent.**

⚠ **The usage record exists for DISTRICTS and not for CITIES.** *The worked instance — "four of eight Cancer
picks had never been used; three of those four produced the district's strongest material" — comes from the
District History Enhancement work, which tracked it. **No per-city equivalent was ever built.***

> ### ⭐⭐ AND THE TIMING IS FAVORABLE, NOT UNFORTUNATE
> **For most of the 38 cities the answer is *"all of them are unused,"*** *because **the ULM run IS the first
> systematic derivation** from those picks.* ***The technique is at maximum yield right now.***
>
> ⛔ **So do not build the tracking first.** *It is worth building **after** a city's pass, to record what that
> pass spent — which is exactly what makes the technique sharp on the **second** visit, not the first.*
> ⭐ **Until then, derive it at run time: check each pick against the city's existing material.** *Cheap,
> because there is little existing material to check against.*

---

## ⚠ One correction made while checking

**Esperanza's first pick carried `[TOP-PRIMARY]` — the only use of that token in the file**, marking it as the
strongest of its three Primaries. ⛔ *A mechanical tier sweep keyed to the three standard tokens would have
dropped it.* ✅ **Normalized to `[PRIMARY]` 2026-09-05, with the ranking preserved as prose on the same line.**
**The file now carries exactly three tier tokens and nothing else.**

⚠ *Recorded because the first automated pass over this file reported **"zero of 37 blocks are tiered"** — a
case-sensitive regex against `Primary` when the file writes `[PRIMARY]`. **The tiering was complete all along.**
Fourth parser false-positive of the day; the pattern is that a presence test is only as good as its casing.*

---

📎 `Cultural_Synthesis_Techniques.md` *(the techniques)* · `Real-World_Basis_Extrapolation_Method.md` *(how
picks are mined, and the district per-pick table that shows what the city version would look like)* ·
`ULM_Piece_Index.md` *(the ULM's own pieces)*
