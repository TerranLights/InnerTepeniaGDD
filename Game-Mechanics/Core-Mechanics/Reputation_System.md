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

## Reputation-Based Merchant Discounts, Confirmed 2026-07-28

**Any 🟢 favorable reputation tier with a district grants the player a purchase discount at every merchant
in that district** — not scoped to any one vendor or service type. This applies uniformly, including to
"not-Doctor-Usanagi" implant procedures (`Character-Creation/Permanent_MACHINE_Stat_Increases.md`), which
already separately require *not* being in a 🔴 unfavorable tier to be served at all; a favorable tier both
clears that gate and earns a discount on top of it.

**Discount scales with how favorable the tier is, paired by overall favorability level rather than by raw
Fame magnitude alone** (matching the grid's own pure-Fame / mixed-Fame-plus-Infamy pairings):

| Tier(s) | Discount |
|---|---|
| **Accepted** or **Smiling Troublemaker** | −5% |
| **Liked** or **Good-Natured Rascal** | −10% |
| **Idolized** | −20% |

**Idolized has no mixed-tier counterpart at this top level** — at Infamy Range 2 or 3 with max Fame, the grid
reads as ambiguous (Dark Hero, Wild Child) rather than favorable, so there's no "mixed" equivalent to pair
with Idolized the way Accepted/Smiling Troublemaker and Liked/Good-Natured Rascal are paired.

**⚪ ambiguous tiers (Neutral, Mixed, Unpredictable, Dark Hero, Soft-Hearted Devil, Wild Child) and 🔴
unfavorable tiers grant no discount** — only the five named 🟢 favorable tiers above do.

---

## Design Decisions, 2026-10-18

Decided with the developer, one question at a time; the full reasoning is in `Reputation_System_Decisions_2026-10-18.md`.

- **Scope.** Every Concordia district (and each DLC city or region) has its own Fame and Infamy. A **cross-district group** also gets its own track, but only once it is a **confirmed faction with real quests and real choices attached**. The list of groups is deliberately left open: factions are created after the ULM/CST/RWBEM process is finished (see the decisions log). Rejected: districts only, and per-faction for everything (a Fallout: New Vegas copy that would disrupt the world's internal consistency).
- **Earning and losing.**
  - Deeds come in **five size tiers** (very minor, minor, average, major, very major, as in Fallout: New Vegas); the point value per tier depends on context and may differ.
  - Each quest outcome or deed **names the districts and groups it affects, with a size for each**; points are not only credited where the deed happened.
  - **Witness rule:** crimes and hacks add Infamy only when someone sees them or they are traced (see `Hacking_and_Traceability_System.md`); unseen acts add no Infamy.
  - One action can raise **both counters at once**, in one district or across two.
  - Percentage modifiers from skills, traits and perks are wanted but **deferred**.
- **Thresholds.** Each range threshold is a **share of what that district (or group) can actually give** (about 15%, 45% and 80% for Ranges 1, 2 and 3 as a starting guess), filled in once its content is written. Range 0 means "below the first threshold," so the first Infamy threshold is the district's **tolerance** for misbehavior before Idolized is lost.
- **Spread.** No automatic spread. A deed can be tagged **"word travels,"** reaching named districts at reduced value; in the story, Leyline chatter carries the news.
- **Removal.** Reputation does not decay and cannot be bought off. A few **rare, designed, costly, story-gated acts of atonement** (for example one per district, tied to its questline) can drop the Infamy range by one step and leave a visible mark. This is a large piece of future design.
- **Presentation.** The player sees **tier names per district and group**, never raw points; dialogue, prices and attitudes carry the rest. The Fallout: New Vegas tier names stay for now and will be gone over again in the rename pass.

## Still Open

- Whether Fame and Infamy thresholds may differ within one district.
- The percentage modifiers from skills, traits and perks (how they would be implemented).
- The actual point values per size tier in each context.
- The atonement acts themselves (one per district, with a visible mark).
- The cross-district group list (waits for faction creation).
- Exact UI, including whether the player sees any "how close" hint.
- Whether the tier names are reskinned to Tepenia's voice.
