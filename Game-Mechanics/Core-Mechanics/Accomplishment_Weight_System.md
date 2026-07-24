# Accomplishment Weight System (History Points, Formalized)

**Status:** designed 2026-07-23, structure and worked example settled, exact point values deliberately
deferred. **This is the actual design for the "History Points" mechanic flagged in `TODO.md`** (2026-07-20,
"not designed, no urgency") — that entry described the FNV Veronica/Arcade/Boone/Raúl precedent (a small
handful of qualifying actions gating when a companion's questline opens) but left the mechanism itself
unbuilt. This file is that mechanism, generalized beyond just recruitment-gating to cover **any personal
questline's internal step-by-step progression**, not only its opening trigger.

**Origin:** built to solve a real pacing problem surfaced while reworking Calethina's questline structure — see
Open Problem, below.

---

## The Open Problem This Solves

Personal questlines that escalate off narrow, specific world-state triggers (e.g., "the player causes a
citywide blackout," "the player visits a Long-Night-War-tied location") create two opposite failure modes:

- **Speedrunners/veteran players** who know the critical path can blow past most optional content, meaning
  the specific triggers a questline depends on may never fire, or fire far later than intended — a "midpoint
  of the main quest" placement stops actually landing at the midpoint for this player.
- **Completionists** who explore everything eventually trigger those same events, but the real-hours gap
  between questline steps balloons, reading as the questline stalling or being forgotten even though nothing
  is actually broken.

**The fix:** replace narrow, specific triggers with a **weighted accumulation of general accomplishments**
the player is already generating through normal play, regardless of playstyle. A speedrunner generates weight
through the small number of high-value things they do (district main questlines, which are the closest thing
to guaranteed critical-path content). A completionist generates a comparable total through sheer volume of
lower-value things (under-questlines, location discovery). Both reach the same gates, just via different
mixes — which is what "gated by story progress" is actually supposed to mean.

---

## The Weight Tiers

**High Weight**
- Completing a district central/main questline — any district, generic.
- **Companion-specific bonus:** extra weight if that district's main questline is completed while a
  particular companion is an active party member, when that district is personally meaningful to her (e.g.,
  Vosora Lashár Tanslock ↔ Gemini).
- **Character-specific accomplishment events** — the richest category. Bespoke, individually-designed
  moments unique to one companion, structurally identical to Fallout: New Vegas's Veronica Santangelo
  location-reveal beats (Camp McCarran, Vault 3, Cottonwood Cove, the Van Graffs' energy weapons shop).
  These are written per-companion, not generated from a generic template — see Calethina's worked example
  below for what a full set looks like.

**Medium Weight**
- Completing a district Under-Questline — any district, generic.
- Same companion-specific bonus mechanic as above, at Medium scale.

**Low Weight**
- Location discovery.

**Numeric point values for each tier are deliberately not set yet** — structure and worked examples come
first, per standing practice on this project (same sequencing already used for district re-spec IF costs).

---

## Worked Example: Calethina

Calethina's personal questline ("Echoes of the Bridge") is the first full application of this system,
developed alongside her — see her own `README.md` for the full character reference this draws from.

**Her two personally-meaningful districts: Gemini and Aquarius.** Gemini fits because her entire nature is
information/archive/data-holding, and her defining tragedy is specifically about *lost knowledge* — the
tightest possible thematic match. Aquarius fits independently of whether the player ever actually finds Ji-Eun
Kim — it's tied to Aquarius's own established character (curious, wants to study/understand unusual cases)
and to the already-confirmed possibility that fragments of her original core are hidden there. Completing
either district's main or under-questline while she's linked/active earns the companion-specific bonus.

**Her character-specific High-Weight accomplishment events — six confirmed candidates, all pre-download and
Concordia-only** (she cannot appear anywhere her signal can't reach, and pre-download that means Concordia
only — cross-country sites are structurally impossible until "inside you" makes her mobile, see below):

1. **Ji-Eun Kim's ruined facility** — the anchor site, once found.
2. **Capricorn — old maintenance/engineering logs** tied to her own installation and early operation at her
   Lab (Cancer/Taurus/Capricorn corner).
3. **Virgo — an Undergrid core-fragment cache** — a literal piece of her original hardware, consistent with
   her own established categorical block (no body, can't retrieve it herself).
4. **Gemini — the Janbogo Subnet Nexus archives** — a plausible site for fragments of her *original*
   broad-knowledge base (the thing Fort McMurdo's reroute order wiped), distinct from the Upper Earth
   intelligence she picked up afterward.
5. **Aquarius — the experimental/prototype labs** — the other named core-fragment location, plus a plausible
   source of technical insight into what the Split Brain shock did to her systems.
6. **Libra — administrative/government record vaults** — the documentary trail of the Fort McMurdo reroute
   and wipe order, recovering context/history rather than raw data; also the most natural place a paper
   trail toward the Ghost Protocol truth could first surface.

**A second wave exists, gated behind her own story, not the accomplishment system itself:** once the "inside
you" embodiment branch is chosen, her construction chain's cross-country sites (Byrd, Fort McMurdo,
Amundsen-Scott Station) become reachable for the first time — the DLC-portability content already documented
in her own `README.md`. These aren't Wave 1 accomplishment-weight candidates; they're a narrative payoff that
only exists after the questline these very accomplishments help pace has already concluded.

---

## Open Questions

- Actual point values per tier, and the actual weight threshold(s) each of Calethina's Step transitions
  requires — deferred per the developer's own explicit sequencing (structure/examples first).
- Whether every companion needs a full character-specific accomplishment list the way Calethina now has one,
  or whether this stays reserved for companions whose personal questlines are far enough along to support it
  (same "who it makes the most sense for" judgment call the original History Points TODO entry already
  flagged).
- Whether the companion-specific district bonus is a flat additive bonus or a multiplier on the base
  district-questline weight — not yet decided.
- How this interacts with the Fragmentation Matrix's own "History Points" input (`Fragmentation_Matrix.md`
  already lists History Points as a Grief-seeding Relationship-Depth Marker) — likely the same underlying
  accumulator feeding both systems, but not yet explicitly confirmed as a single shared number.
