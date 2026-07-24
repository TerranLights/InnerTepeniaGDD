# Accomplishment Weight System (History Points, Formalized)

**Status:** designed 2026-07-23, structure, worked example, and numeric point values all settled. **This is
the actual design for the "History Points" mechanic flagged in `TODO.md`** (2026-07-20,
"not designed, no urgency") — that entry described the FNV Veronica/Arcade/Boone/Raúl precedent (a small
handful of qualifying actions gating when a companion's questline opens) but left the mechanism itself
unbuilt. This file is that mechanism, generalized beyond just recruitment-gating to cover **any personal
questline's internal step-by-step progression**, not only its opening trigger.

**Origin:** built to solve a real pacing problem surfaced while reworking Calethina's questline structure — see
Open Problem, below. **Scope, worth stating explicitly:** this is a general system, not a Calethina-only one.
The tiers, the "personally meaningful district" mechanic, and the point values below all apply to *any*
companion whose personal questline uses this system — Calethina is simply the first fully worked example,
not the scope of the mechanic itself.

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

**The full "Companion Trigger" activates at 100 History Points, established 2026-07-23.** Every
accomplishment below contributes toward that same 0-100 scale for a given companion. The specific
questline-progression gate this feeds (for Calethina, the Step 3→4 transition into "The Choice") fires once
the companion's own accumulated total reaches the trigger.

**Weight alone gates it — no independent story-beat floor, confirmed 2026-07-23.** Any timing language
elsewhere (e.g., Calethina's Step 4 firing "at the midpoint") describes what *typically* happens for average
play, not a hard requirement the main quest must independently satisfy first. A sufficiently skilled,
prepared, and focused player can hit the trigger far earlier than that, and the gate should fire immediately
when they do — same shape as Fallout: New Vegas's own Raúl Tejada, recruitable at Level 1 if the player
already knows to go straight to Black Mountain, repair Rhonda, talk down Tabitha, and unlock the door,
without ever touching anything else the game normally expects first. **Standing design law:** if the player
puts in the effort — even unusual, early, highly specific effort most players won't replicate — they deserve
the reward. This system should never be quietly re-gated behind an additional floor just to protect an
"expected" pacing curve.

**What hitting 100 pre-recruitment actually means — clarified 2026-07-23, since the retroactive tiers alone
can reach it without the companion ever having been met.** Example: completing a meaningful district's main
questline (40) plus three of its Under-Questlines (20 × 3 = 60) totals exactly 100, entirely through
retroactive categories, with zero recruitment required. **This does not mean her questline's own steps
advance or complete in her absence** — the Extra-High-Weight character-specific site visits (the actual
content-bearing steps of her arc) require her active presence and can never be retroactive, so nothing about
her own story can progress without her actually being there. What a pre-satisfied trigger means is that
**her personal questline becomes immediately available the moment she's actually recruited** — no additional
buildup required, because the game recognizes she'd plausibly already know the player by reputation. A
reward for engagement that happened to overlap with what she cares about, not a way to skip her story
entirely.

**Extra-High Weight — established 2026-07-23, split out from High Weight**
- **Visiting a site especially meaningful to a companion personally, while she's an active companion — 30
  points.** Bespoke, individually-designed moments unique to one companion, structurally identical to
  Fallout: New Vegas's Veronica Santangelo location-reveal beats (Camp McCarran, Vault 3, Cottonwood Cove,
  the Van Graffs' energy weapons shop). These are written per-companion, not generated from a generic
  template. Promoted to their own tier above ordinary High Weight because they're the single most personally
  relevant plot-beats a companion has — not just weightier instances of district content, but a different
  *kind* of accomplishment entirely. **Requires the companion to be actively recruited and present at the
  time — never retroactive** (see Retroactivity, below). At 30 points each, three of these alone clear the
  full 100-point trigger — deliberately not requiring every candidate site to be found. See Calethina's
  worked example below for what a full set looks like.

**High Weight**
- **Completing a district's central/main questline — any district, generic — 5 points.**
- **Completing a district's central/main questline for a district personally meaningful to the companion —
  40 points.** **Retroactive** (see below) — the companion does not need to be recruited or active at the
  time this happens.
- **Reaching "Idolized" status specifically in a district personally meaningful to the companion — 50
  points.** Reaching Idolized status is *not*, by itself, a weighted factor — reaching it anywhere, in any
  district, contributes nothing on its own. It only counts when it's Idolized status in a district that's
  actually meaningful to the specific companion in question. This is a distinct trigger from completing that
  district's main/under-questline — a player could complete Gemini's main questline without ever reaching
  Idolized there, and could also reach Idolized in Gemini through unrelated reputation-building without ever
  touching its main questline; both are real, separately-countable High-Weight events, together worth 90 of
  the 100 points needed, for a companion who cares about Gemini specifically. **Also retroactive.**

**Medium Weight**
- **Completing a district's Under-Questline — any district, generic — 5 points.**
- **Completing a district's Under-Questline for a district personally meaningful to the companion — 20
  points.** **Also retroactive**, by the same logic.

**Low Weight**
- **Location discovery — 1 point.**

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

**The in-world reasoning behind the test, not just the mechanical convenience:** Idolized status and district
main-questline completion are the kind of thing that becomes genuinely, organically *known* within that
district and beyond — reputation spreads, a resolved central conflict gets talked about, word travels
through a lived-in community the ordinary way. A companion personally connected to that district would
plausibly have heard about the player through completely normal in-world channels, with no magical
hand-waving required to explain how she knows. **Visiting a specific location doesn't have this property.**
Nobody organically gossips about a stranger having walked through a particular fashion center or care
facility — that's a private, quiet act with no natural information-spread mechanism behind it, which is
exactly why it can't be retroactively known by a companion who wasn't there for it. The retroactivity test
isn't an arbitrary mechanical convenience; it tracks a real distinction in how information plausibly moves
through Concordia.

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
   and wipe order, recovering context/history rather than raw data; possibly an adjacent thread pointing
   toward the Triage Protocol (renamed 2026-07-23 from "Ghost Protocol") — though the actual truth of her
   authorship is confirmed to surface specifically during her Romance questline, not here.

**A second wave exists, gated behind her own story, not the accomplishment system itself:** once the "inside
you" embodiment branch is chosen, her construction chain's cross-country sites (Byrd, Fort McMurdo,
Amundsen-Scott Station) become reachable for the first time — the DLC-portability content already documented
in her own `README.md`. These aren't Wave 1 accomplishment-weight candidates; they're a narrative payoff that
only exists after the questline these very accomplishments help pace has already concluded.

**The numbers reward personal engagement over generic completion, worth noting explicitly.** Deep investment
in just one of her two meaningful districts — reaching Idolized there (50) plus completing its main
questline there (40) — is 90 of the 100 points needed from two events in one place. By contrast, completing
every one of Concordia's 13 districts' main questlines generically (5 each) only totals 65 — not even enough
alone. The math itself expresses the design intent: a player who specifically engages with what matters to
Calethina reaches her climax faster than one who spreads generic effort evenly across the whole game.

---

## Open Questions

- Whether every companion needs a full character-specific accomplishment list the way Calethina now has one,
  or whether this stays reserved for companions whose personal questlines are far enough along to support it
  (same "who it makes the most sense for" judgment call the original History Points TODO entry already
  flagged).
- How this interacts with the Fragmentation Matrix's own "History Points" input (`Fragmentation_Matrix.md`
  already lists History Points as a Grief-seeding Relationship-Depth Marker) — likely the same underlying
  accumulator feeding both systems, but not yet explicitly confirmed as a single shared number.
