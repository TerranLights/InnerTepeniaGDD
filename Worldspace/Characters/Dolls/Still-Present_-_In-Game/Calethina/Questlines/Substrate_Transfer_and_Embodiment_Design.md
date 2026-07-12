# Calethina — Substrate Transfer & Embodiment Design (Working Draft, 2026-07-12)

**Status:** real design-session progress, not locked canon. This is the "real backstory session" that `Personal_Questline_Summary.md` (both copies — see Still Open below) flagged as her single highest-priority open item, and that all three canon repos (InnerTepeniaGDD, TepenianUniverseTimeline, SouthernLights) independently flagged the same way.

**Provenance:**
- Builds on and reconciles against `Personal_Questline_Summary.md`'s "confirmed design points" callout (the Grok-drafted Step 1-5 walkthrough itself remains separately deferred/reference material — see Still Open).
- Integrates and supersedes `to-be-integrated/Calethina's history.txt` and `to-be-integrated/Calethina's rewards.txt`, both retired after this document absorbed their content.

---

## The Core Dilemma (new, 2026-07-12)

**Cause of her degradation:** the same electrical mega-shock that destroyed Amundsen Tower and triggered the Planetary Split Brain also partially corrupted her — on top of the already-established loss of server redundancy (RAID-distributed → single non-redundant instance). This ties her personal condition directly to the setting's single largest infrastructure catastrophe, rather than leaving her degradation as an isolated character quirk.

Her ongoing struggle: whether to attempt a substrate transfer to preserve herself. Any transfer carries a real risk of memory loss or alteration — there is no clean, risk-free option.

---

## Already-Confirmed Baseline (from `Personal_Questline_Summary.md`, still authoritative)

- **Direction:** archive-narrator, not organizational leadership. She narrates ruins and abandoned infrastructure the player enters, generating quest hooks from what she remembers reaching when her signal was stronger.
- **First thread:** Ji-Eun Kim. Calethina knows Ji-Eun's ruined nanotech-implant testing facility; finding Ji-Eun (or what happened to her) is the questline's first major active objective beyond exploration and narration.
- **Structural placement:** the download decision occurs around the **midpoint of the main quest**, not the ending. It's a transition — it changes what the second half of the game looks like with her — not a conclusion.
- **Projection mechanic:** she is a holographic projection, never a walking/bipedal presence — always floats/hovers. Pre-download: projects from the lab server, signal-dependent (flickers/glitches with poor signal, disappears entirely with none). Post-download: local to the wrist device, stable everywhere regardless of grid state. The flickering-becomes-steady visual change is itself the payoff of the download.
- **Download is not stat-gated.** Available to any player who reaches the decision through the questline.
- **Download and romance are separate events.** Romance only becomes available after a download has occurred, not at the download decision itself.
- Partial download, no download, and alternative stabilization (Aquarius research, religious factions) are all separately valid, non-lesser outcomes — not a hierarchy of "good" vs. "bad" endings.

---

## New Branch: Embodiment (2026-07-12)

Alongside the existing "download into the player" option, a genuinely new option: transfer into a physical Doll body — **her first embodiment in her entire existence.**

- **No MACHINE stat change in either direction** — deliberately distinct from the "inside you" branch below, so the two options pay off in different currencies rather than being the same reward with different flavor text.
- **Cost:** memory/personality fidelity loss in the transfer itself. She's embodied, but not perfectly continuous with who she was.
- **Reward currency:** non-stat, still TBD. Three candidate directions, none chosen yet:
  1. **Access-based** — her own home/location in Concordia for the first time, distinct from the Lab she's been tethered to her entire existence.
  2. **Body-enabled interaction content** — companion dialogue/interaction options only possible because she now has a body to have them with.
  3. **Recognition-Cascade-flavored** — she's spent her whole existence as infrastructure (an activation-lab AI); a body might be the first time she gets to just be a person rather than a service. Could translate into district/NPC reactions changing now that she's embodied.

## Refined Mechanic: "Download Into the Player" ("inside you")

Same-magnitude stat trade: **+n** to Calculation, Investigation, Nerve, and base Hacking%, matched by an equal **−n** penalty to Engine, Might, and Humanity. Mind sharpens; body and individual selfhood pay for it.

Two additional narrative-level costs, one for each party:
- **Her risk:** the player's frame wasn't built to host a second consciousness. Real chance she degrades *further* from mismatched architecture — echoing the exact mismatched-systems cause of her original corruption.
- **The player's risk:** she's always there now. No more private inner life. Reads as either the deepest intimacy in the game or the loss of something the player didn't know they'd miss — probably both, depending on the player.

---

## Romance Gate — Redesigned to Match Kendra Heinrich's Precedent (2026-07-12)

**Replaces** the earlier MACHINE-stat-threshold idea (Calculation ≥8, Humanity ≥6, Nerve ≥6, Engine ≥6) entirely. That idea was dropped specifically because the download's own stat penalty would interact with a numeric threshold in ways that are hard to make fair on purpose — the gate could be evaluated pre-penalty (safe but makes the threshold pointless), post-penalty (real friction, but potentially punishes the exact players it's meant to reward), or the numbers could be re-tuned to route around the problem entirely. None of those felt better than just not having the collision in the first place.

Kendra Heinrich's own romance gate already solves this: **no MACHINE stat or trait requirement at all.** Her gates are entirely conduct-based — Gate 1 is a plot-completion precondition (the player defeats the threat that defeated her, and she witnesses it), Gate 2 is behavioral across the DLC (not being condescending, not making her feel like a burden, not backing down, showing genuine curiosity — "the things that break through an 8w7's armor").

Calethina's gate mirrors that shape:
- **Gate 1 — commitment:** the player completes her personal companion questline through to a download decision (either branch, inside-you or new-body).
- **Gate 2 — conduct:** across vital plot points in her personal questline, the player doesn't say or do anything combative, insulting, or abhorrent to her sensibilities — the equivalent of Kendra's "not kicking her while she's down."
- Both gates met → romance becomes available.

This makes the earlier stat-interaction tension moot rather than solved — eligibility is behavioral, not numeric, so the download's stat penalty has nothing to collide with.

---

## Unmarked Origin Lore (from `Calethina's history.txt`, now formalized)

Her construction/shipping chain is designed as **fully unmarked lore, the same precedent as the Cradle network** ([[feedback_cradle_unmarked_lore]]): no quest markers, no logs, no quest tracking, no pointers, no XP. Discoverable only by a sufficiently diligent, patient, curious player piecing together records across up to seven locations spanning multiple subnets:

Mawson (request) → Neumayer/Halley subnet (spec & schematic design) → Kunlun/Mirny subnet (engineering & programming) → Byrd (full construction) → Sejong/Palmer subnet (stress-testing) → Port Lockroy/Palmer subnet (shipped via) → Fort McMurdo/Janbogo subnet (ordered a shipping reroute) → forward-shipped via Amundsen-Scott Station.

Worth noting even before interpretation: Fort McMurdo — the historical national capital — personally ordering a reroute is not a small detail for one unit's shipment. Her final leg through Amundsen-Scott Station also puts her construction timeline in direct physical proximity to the site whose later destruction caused her defining trauma. Neither is explained yet; both are there for a sufficiently curious player to notice.

*(Full formalized version of this chain lives in `Personal_Background/Founding_Construction_Chain_UNMARKED.md`.)*

---

## Base-Game Completability (binding constraint, confirmed 2026-07-12)

Her full arc — companion → romance → post-romance — must be completable entirely within the base game, no DLC required. `Calethina's rewards.txt` references "the end stages of rescuing Kendra and attempting to decrypt the datastash" as an escalation point; reinterpreted as an **optional bonus layer** for players who also own DLC1, stacked on top of an already-complete base arc — never a requirement to finish her story.

---

## Reward Reconciliation (from `Calethina's rewards.txt`)

Original two-tier structure, each with two base bullets plus a third DLC1-bonus-escalation bullet:

| Tier | Base reward | DLC1 bonus (optional, stacks on base) |
|---|---|---|
| A — companion completion | 1 free combat turn before automated systems turn hostile; +1 Calculation/Investigation/Nerve; +15% base Hacking | Additional +1 to same three stats, +25% Hacking, tied to the Kendra-rescue/datastash beat |
| B — romance completion | 2 free combat turns; +2 Calculation/Investigation/Nerve; +25% base Hacking | Additional +1 to same three stats, +35% Hacking, same beat |

**Open question:** do these apply on top of, or instead of, the new-body/inside-you branch-specific mechanics above? Current best guess, not yet confirmed: these are the companion/romance completion rewards regardless of which embodiment branch is chosen, and the branch-specific mechanics (stat trade for inside-you, TBD non-stat perk for new-body) are an additional layer specific to which physical/existential outcome was chosen.

---

## Still Open

- Companion questline's actual beat-by-beat structure. The Step 1-5 walkthrough in `Personal_Questline_Summary.md` is reference material, not confirmed structure, and needs a review pass once the above settles — notably, its Step 5 is timed "Late Act 2 → Act 3," which no longer matches the confirmed midpoint placement for the download decision.
- New-body path's specific non-stat perk — three candidates floated above, none chosen.
- Whether "no download / refuse" is its own distinct branch with its own reward, beyond what's already noted ("she may stabilize at reduced capacity or slowly degrade further").
- How the base reward tiers interact with the branch-specific mechanics — layered or replaced (see Reward Reconciliation above).
- `Calethina/Questlines/Personal_Questline_Summary.md` is still the blank generic template (unfilled) — the real "Echoes of the Bridge" content lives at `Calethina/Personal_Questline_Summary.md` (root level), which this document supersedes for design purposes.
