# Reputation System

**Source:** Fallout: New Vegas's two-axis Fame/Infamy reputation system, saved by the developer as Inner Tepenia's own design touchstone (`Reference/Images/exterior_reference/Fallout New Vegas - Reputation Chart.png`). Confirmed 2026-07-20: Inner Tepenia will implement something built on this system — not necessarily identical terminology, but the same underlying two-axis structure. This file transcribes that reference chart into an actual markdown table so it's directly usable without needing to view the image.

**Where this already matters:** the district- and faction-standing mechanics referenced throughout `Companion_System.md`'s Personal Questline Design Rule (the faction-antagonism pattern and the Wild Child pattern) already assume this system, including its exact tier names (Accepted, Liked, Smiling Troublemaker, Good-Natured Rascal, Idolized) and the Wild Child condition specifically (Idolized + Vilified simultaneously, per `Storyline/Endings/Secret-Endings/Wild_Child_Endings.md`).

---

## The Two-Axis Model

Reputation is **not a single scale**. Two independent tracks are maintained simultaneously per faction/district:

- **Positive Reputation ("Fame")** — Range 0 through Range 3
- **Negative Reputation ("Infamy")** — Range 0 through Range 3

The tier the player actually holds is the *combination* of both axes, not an average or a single blended number. A player can be simultaneously high on both axes at once (see Wild Child, bottom-right cell) — this is a real, distinct state, not a contradiction the system averages away.

## The Full Grid

**Legend (reproduces the source chart's own color-coding, not an invented classification):** 🟢 green = favorable reputation overall · 🔴 red = unfavorable reputation overall · ⚪ white/black = genuinely ambiguous, not read as clearly good or bad even by the people holding the opinion.

| Infamy ↓ / Fame → | **Range 0** | **Range 1** | **Range 2** | **Range 3** |
|---|---|---|---|---|
| **Range 0** | ⚪ **Neutral** — People don't know enough about you to form an opinion. | 🟢 **Accepted** — Folks have come to accept you for your helpful nature. | 🟢 **Liked** — Enough news of your good works has been passed around that people like you. | 🟢 **Idolized** — Renowned for your extensive support and goodwill, you are idolized by the community. |
| **Range 1** | 🔴 **Shunned** — You've left a poor impression on the community and may be shunned as a result. | ⚪ **Mixed** — A little bit good mixed with a little bit bad, people haven't figured you out yet. | 🟢 **Smiling Troublemaker** — People know you're good at heart even though you're occasionally a troublemaker. | 🟢 **Good-Natured Rascal** — Your reputation as a good-natured friend of the community manages to outshine your dark side. |
| **Range 2** | 🔴 **Hated** — Now that folks know you're bad, most people outright hate you. | 🔴 **Sneering Punk** — Even though you've done some good for the community, people still think you're a punk. | ⚪ **Unpredictable** — No one's sure what to make of your unpredictable nature, but you've left a strong impression. | ⚪ **Dark Hero** — Folks still think you're some kind of hero, but you sure can be nasty sometimes. |
| **Range 3** | 🔴 **Vilified** — For your overwhelmingly monstrous behavior, you have become vilified by the community. | 🔴 **Merciful Thug** — Despite your reputation as a thug, you are known to occasionally show a charitable side. | ⚪ **Soft-Hearted Devil** — Most people say you're the devil himself, but most admit you've also done a world of good. | ⚪ **Wild Child** — Your wild, seemingly capricious behavior leaves people scratching their heads in confusion and avoiding close contact. |

16 total named combinations. Row = Infamy tier, column = Fame tier; read the cell where they intersect.

## Named Tiers, Grouped

Grouped by the color-coding above, not by raw Fame/Infamy magnitude — the source chart's own color choices don't map cleanly onto "whichever axis is higher" (Dark Hero and Soft-Hearted Devil read as ambiguous despite high Fame, for instance):

**🟢 Favorable overall:** Accepted, Liked, Idolized (pure Fame axis) · Smiling Troublemaker, Good-Natured Rascal (mixed but still read as good)
**🔴 Unfavorable overall:** Shunned, Hated, Vilified (pure Infamy axis) · Sneering Punk, Merciful Thug (mixed but still read as bad)
**⚪ Genuinely ambiguous, not clearly good or bad even to the people holding the opinion:** Neutral, Mixed, Unpredictable, Dark Hero, Soft-Hearted Devil, Wild Child
**The extreme case — both axes maxed simultaneously:** **Wild Child** (Fame Range 3 + Infamy Range 3) — already has its own dedicated, fully-designed content in `Storyline/Endings/Secret-Endings/Wild_Child_Endings.md` (WC-1 through WC-4, tiered by how many districts reach this state) and is referenced as a recommended non-stat companion-questline route pattern in `Companion_System.md`.

## Open Design Questions

- **Terminology:** whether Inner Tepenia keeps these exact tier names, or reskins them to fit Tepenia's own voice (robot/human coexistence framing rather than a wasteland-frontier one). Not yet decided.
- **Scope:** whether this tracks per-district, per-faction, or both, given districts and factions are established as related but genuinely separate axes elsewhere in this project (`Companion_System.md`'s "Companion distribution across districts" section).
- **Mechanical thresholds:** exact point values or actions required to move between Range 0-3 on each axis are not yet designed.
- **Full system design** (how reputation is earned/lost, UI presentation, whether it's visible to the player as raw numbers or only through tier names and NPC reactions) is not yet started — this file only formalizes the reference chart itself.
