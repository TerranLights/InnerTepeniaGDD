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

**Extra-High Weight — established 2026-07-23, split out from High Weight**
- **Character-specific accomplishment events.** Bespoke, individually-designed moments unique to one
  companion, structurally identical to Fallout: New Vegas's Veronica Santangelo location-reveal beats (Camp
  McCarran, Vault 3, Cottonwood Cove, the Van Graffs' energy weapons shop). These are written per-companion,
  not generated from a generic template. Promoted to their own tier above ordinary High Weight because
  they're the single most personally relevant plot-beats a companion has — not just weightier instances of
  district content, but a different *kind* of accomplishment entirely. **Requires the companion to be
  actively recruited and present at the time — never retroactive** (see Retroactivity, below). See
  Calethina's worked example below for what a full set looks like.

**High Weight**
- Completing a district central/main questline — any district, generic.
- **Companion-specific bonus:** extra weight if that district's main questline is completed and that
  district is personally meaningful to a given companion. **Retroactive** (see below) — the companion does
  not need to be recruited or active at the time this happens.
- **Reaching "Idolized" status specifically in a district personally meaningful to the companion —
  established 2026-07-23.** Reaching Idolized status is *not*, by itself, a weighted factor — reaching it
  anywhere, in any district, contributes nothing on its own. It only counts when it's Idolized status in a
  district that's actually meaningful to the specific companion in question. This is a distinct trigger from
  completing that district's main/under-questline — a player could complete Gemini's main questline without
  ever reaching Idolized there, and could also reach Idolized in Gemini through unrelated reputation-building
  without ever touching its main questline; both are real, separately-countable High-Weight events for a
  companion who cares about Gemini specifically. **Also retroactive.**

**Medium Weight**
- Completing a district Under-Questline — any district, generic.
- Same companion-specific bonus mechanic as above, at Medium scale. **Also retroactive**, by the same logic.

**Low Weight**
- Location discovery.

---

## Retroactivity — established 2026-07-23

**The test:** an accomplishment is retroactive — it counts toward a companion's total even if she hasn't
been recruited yet, or isn't in the active party at the time it happens — **only when it is simultaneously
both "world-based" and "personal" at once.** "World-based" means the accomplishment is a persistent
world-state fact (a reputation tier, a quest-completion flag) that remains true regardless of who was
present when it happened or how much later someone checks it. "Personal" means it also happens to intersect
with something specific to a given companion. When both are true at once, the underlying fact doesn't
depend on the companion having witnessed it — it's simply true about the world, and she can be credited for
it whenever she's recruited.

**Qualifies (retroactive):**
- Reaching Idolized status in a district directly personally meaningful to the companion — a reputation
  tier is a standing world-state fact.
- Completing the central/main district questline in a district directly personally meaningful to the
  companion — same reasoning, a permanent story-resolution fact.

**Does not qualify (requires active presence at the time):**
- Visiting a location directly personally meaningful to the companion (e.g., a specific hospital, care
  center, or fashion center meaningful to Ayako Hayashi) while she isn't an active companion. Visiting a
  location isn't an independent world-state fact the way a reputation tier or quest completion is — it's an
  experiential, witnessed moment that only exists *because* the companion was there for it. If she wasn't
  there, it didn't happen for her, and it can't be recognized after the fact once she's recruited.

**Practical consequence:** the Extra-High Weight tier (character-specific accomplishment events) is
categorically never retroactive, for exactly this reason — those events are, by definition, shared
witnessed moments, not standing world facts. The High- and Medium-Weight companion-specific district bonuses
are categorically retroactive, since reputation tiers and quest-completion flags are standing world facts by
nature. This is a clean rule, not a judgment call to make per-accomplishment: check whether the thing itself
is a persistent world-state fact independent of presence, and the retroactivity answer follows automatically.

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
Reaching **Idolized status specifically in Gemini or Aquarius** (not any other district) is a separate,
additional High-Weight event for her — distinct from, and stackable with, completing either district's own
main/under-questline.

**Her character-specific Extra-High-Weight accomplishment events — six confirmed candidates, all
pre-download and Concordia-only** (she cannot appear anywhere her signal can't reach, and pre-download that means Concordia
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
