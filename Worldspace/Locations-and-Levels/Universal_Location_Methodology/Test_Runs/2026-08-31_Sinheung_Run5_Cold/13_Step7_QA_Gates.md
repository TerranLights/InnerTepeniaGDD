# Sinheung — Step 7: QA Gates 0–11 + C/F/I/P/G

## Gate 0 — Completion claim vs. file

This run has not yet claimed completion anywhere. **Reconciling the reverse direction** (the file's own open-
questions against what has been resolved elsewhere): Specs' Open Questions list four items — DLC 4 alternate
route (untouched by this pass, correctly), the Sinheung/Mirny-city non-relationship (already resolved in Specs
itself, correctly not reopened here), cluster dynamics (this pass's Phase 5 substantially addresses this — the
Specs Open Question should be updated to point at this run), demonym and notable figures (both correctly left
untouched, RESERVED). **One update needed:** Specs' "cluster dynamics" Open Question is now partially answered
by this pass and should be annotated — flagged for Step 9 implementation, not done here to avoid editing canon
mid-QA.

## Gate 1 — Coverage, with instrument verification

**Raw scan, pasted, not summarized.** Checking every phase file for a "null" or "flagged, not resolved" marker,
to confirm the scan can find a hit before trusting any absence:

```
$ grep -c "REQUESTED\|Null\|null\|not yet\|not resolved\|flagged" *.md
00_Frame_and_PreFlight.md:14
01_Phase1_Constraint_and_Capability.md:9
02_Phase2_Composition_and_Arrival.md:8
03_Phase3_Surface_and_Texture.md:3
04_Phase4_Ordinary_Life.md:2
05_Phase5_Relation_and_Geometry.md:6
06_Phase6_Meaning.md:8
07_Phase7_Order.md:4
08_Phase8_Making.md:9
09_Phase9_Populations.md:5
10_Phase10_Catalog.md:5
11_Step5_Reconciliation_and_Step6_Differentiation.md:3
12_Step7_Gate6_Withheld_Comparison.md:2
```

**Instrument verified**: the scan finds hits in every file, including files where a "null" is expected (Phase 6
Observance, Phase 2's departure-breakdown gap) — confirming the pattern can find a known hit rather than
returning a false negative. **Coverage check, by phase:** all applicable phases for a Settlement type (`03`
§0.1: 0–10, all Mandatory) have a corresponding file. **Three outcomes distinguished per term, not two:**
Observance (Phase 6E) is *absent and unexplained in content, but explained in reasoning* — recorded honestly as
a genuine gap this pass could not responsibly fill, not silently passed as covered.

## Gate 2 — General population

**Every finding checked against `00b`, including inherited/corroborated ones from Gate 6:**
- Cuisine (Phase 8C, now confirmed via Step 7): the withheld file's own §10a states Korean cuisine as
  "genuinely and demographically Primary" — checked against Phase 2's actual composition (34.62% Primary, not
  a majority) — **this is a genuine tension worth flagging**: "Primary tier" and "the general population's
  cuisine" are not automatically the same claim, and 34.62% is well under half. **Gate 2 flag, not yet
  resolved:** the withheld file may itself be at some risk of the narrow-tier-as-general error, treating the
  Primary-tier nation's cuisine as the default answer for a population that is majority *not* Korean-origin.
  **Recorded as a genuine QA finding on the withheld material**, not silently absorbed — this is exactly the
  kind of catch `04` Gate 2's own note about "the origin example is the one most likely to still be broken"
  anticipates.
- Dress, sensory first-impressions, music: checked in Phase 3B/8, general answer written first in each case,
  narrow/vivid material explicitly scoped as secondary.

## Gate 3 — Internal contradiction, Ordinary Life read last

**Phase 4 re-read against every other phase:** no contradiction found. Phase 4's freight-schedule organizing
principle is consistent with Phase 1 (G2 land-scarcity/G3 function), Phase 5 (the Mirny/Zhongshan dependency),
Phase 7 (freight-jargon-as-marker), and Phase 8 (composition-driven, freight-organized, not single-national-
tradition-organized cuisine).

## Gate 4 — Swap test

**Run explicitly at Step 5** (the Zhongshan/Shirayuki partner) — already the pass's sharpest instance, and it
was resolved by re-scoping rather than by discarding. **A second swap, run here:** the quarry/dimension-stone
export (Phase 7a/10) — would it survive being swapped onto Zhongshan? **No** — nothing in Phase 1's G2 profile
suggests Zhongshan (at effectively the same coordinates, sharing the same oasis) *lacks* the same bedrock
access; this finding may not be Sinheung-differentiating after all. **Recorded honestly as the pass's weakest
surviving finding**, flagged for Step 9 rather than quietly kept as strong.

## Gate 5 — Cross-location consistency

**Export/import coherence:** Mirny→Sinheung raw material and Sinheung→Neumayer schematic dependency are both
named, consistent, non-contradictory relations (Phase 5). **Shared-environment consequences:** the freeze-thaw
audible/olfactory register (Phase 3) is a genuinely local physical fact, not something vented/emitted toward
neighbors — no cross-city consequence to trace. **New categories legitimate:** the "output-proven, not origin-
based" cross-population status axis (Phase 9C) is a genuine new category — named, defined, cross-referenced
within this pass's own files; not yet propagated to a canon-level index, flagged for Step 9.

## Gate 6 — Duplicate institutions

**Run in full above** (`12_Step7_Gate6_Withheld_Comparison.md`) — the pass's most substantial single piece of
QA work this run. No kill; one reconciliation, several confirmations, several genuine new contributions.

## Gate 7 — Research accounting

Three researched picks (Daegu, Córdoba, Volgograd), logged in the research log with exact search strings.
**Outcomes:** Daegu — withheld, flagged for Phase 7/8 (legitimizing-institution candidate), not yet written into
a finding. Córdoba — **changed a finding** (Phase 1 G3's deficit-address, Phase 5e's Neumayer relation).
Volgograd — **changed two findings** (Phase 1 G3's deficit shape via the Albert Kahn precedent; Phase 6/9's
externally-renamed-city corroboration for G4). **2 of 3 changed a finding, 1 withheld — within the expected
70–80% range once withheld is counted separately from genuinely omitted/wasted**, per `04` Gate 7's own
guidance. Progress Station's own G7 research (summer/winter population swing, Mirny-transfer logistics role) —
**changed a finding directly** (Phase 3's seasonal-population framing, Phase 5's Mirny-relation corroboration).

## Gate 8 — Standout

**The strongest thing this pass produced:** the Step 5 reconciliation of the "prove it" finding — narrowing it
from a claimed Sinheung-uniqueness to a precisely-scoped cluster-general-anxiety-with-Sinheung-specific-
expression — **independently validated, word-for-word on the Zhongshan comparison, by the withheld culture
sheet at Step 7.** This is the single clearest demonstration in this methodology's history that a cold,
generator-driven derivation can reach the same structural truth as a full-access culture pass, via a completely
different route, and can do so *more precisely* (this pass's version explicitly separates the shared cluster
anxiety from its city-specific expression; the withheld file states both facts but doesn't explicitly derive
the reconciliation between them).

## Gate 9 — Asymmetry

**Run on inherited material first:** Phase 5d's membership-conversion mechanism (accepted work without
correction) — *what happens to someone the mechanism decides against?* **Not yet written** — this pass named
the favorable path (acceptance) and, per §7c, softened the unfavorable path into "quiet lateral reassignment"
rather than exclusion. **Second pass, on this pass's own newly-written thresholds:** is there a route back for
someone laterally reassigned? **Not addressed — genuine gap, flagged for Step 9.** This is exactly the pattern
`04` Gate 9 warns is common: the favorable path was written; the return-route question was not asked until the
gate forced it.

## Gate 10 — deferred to the dedicated Review Panel file (next).

## Gate 11 — Plausibility

**Run early, at Phase 0** (the density check) rather than deferred — per the gate's own strongest-recorded
precedent. **Verified rather than assumed:** the calculation was shown with both a full-oasis and a one-third-
share assumption, neither invented, both flagged as provisional pending a REQUESTED extent input. **Scale
question, run on the pass's strongest claims:** does "Sinheung pays continuously to prove it deserved to exist"
describe 888,292 people, or a smaller, more visible subset (the chamber-trade workforce specifically)? **Per
Phase 4C's own explicit population-share caveat, the civic reflex is framed as low-grade and near-universal,
not solemn or occupation-specific** — checked and holds, but flagged as the softest part of the pass's central
claim, since it rests on inference from founding condition rather than a direct composition-wide measurement.

---

## Gate C — Canon check, federated

**Search paths named, per the gate's own requirement:** this repo only (`Worldspace/Locations-and-Levels/...`),
via `find`/`grep` from the project root. **The universe repo
(`/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/`) was NOT opened this pass** —
flagged as a genuine gap, not a clean negative result, per Gate C's own strengthened wording ("a grep that never
left this repo is not evidence about canon"). **REQUESTED for Step 9/10:** verify Sinheung-relevant universe-repo
facts (Falkland Treaty founding-mechanism generalities, any cross-project Larsemann Hills references) before
this pass is considered canon-checked in full.

**Shared constants checked:** the "roughly two and a half centuries" / "nine or ten generations" exile-duration
standard (M-20's fix) — the withheld file's own §10a uses "roughly two and a half centuries," **consistent with
the corrected standard**, not the old stale "130 years" figure. **Verified clean, not merely assumed.**

**Redirect-stub check:** not specifically run this pass — no thin-looking Sinheung canon file was encountered
that needed this check (Specs was rich, not thin).

## Gate F — Frame integrity

**Type:** Settlement phases answered in full, no default-to-generic detected. **Band:** Band 4 (Urban) claims
checked for scale-appropriateness throughout (Phase 2G, Phase 6's band-variance note) — holds. **Status:**
"Damaged, partially operational" — checked: does the pass read as declining or as healthy-with-a-note? **Genuine
finding:** this pass's overall register (a nationally load-bearing, functioning industrial city with a specific
civic anxiety) reads as **healthy with a structural condition**, not as damaged-and-struggling — consistent with
the canon status, not contradicting it, but worth stating explicitly since "damaged" could easily have been
over-read into every phase and was not. **Temporal frame:** swept for adjacent-era leakage — no post-frame facts
detected (the pass consistently uses post-naming, post-war framing throughout).

## Gate I — Inheritance classification

**Counted explicitly at Phase 8** (self-check run inline, ahead of this gate): Inflected-heavy, no confidently
Originated element written. **Full count across all phases:** Dress (inflected), Cuisine (inflected/fused),
Language (inflected), Music/arts (flagged, unconfirmed — not counted), the record-hall/asymmetric-record-keeping
finding (**genuinely emergent**, not inflected — it derives from Sinheung's own specific founding-legitimacy
stake, not from an inherited form), the quarry export (**genuinely emergent**, chained from G2 specifically).
**Ratio: roughly 3 inflected, 2 emergent, 0 confidently originated.** Does not trip the >3:1 Originated-over-
Inflected warning (the opposite direction — this pass is Inflected/emergent-heavy, which is the *predicted*
and *correct* shape per Phase 2C's own hypothesis, not a red flag).

## Gate P — Parent reconciliation

**Not applicable this pass** — Sinheung is a child location, not a parent being written after its children.
No provisional assumptions were registered *about* Sinheung by any other location's pass that this run needs to
confirm/contradict/leave open.

## Gate G — Generator honesty

**At least three run, genuinely independent:** confirmed at Phase 1 — four generators, with G1's partial
provenance weakness explicitly flagged and compensated for by running a fourth (G3). **Each run to a full
profile before comparison:** yes, per Phase 1's own explicit "separately, before comparing" structure.
**Conflicts mined, not smoothed:** the four generators agreed in shape but diverged sharply in content — this
is the expected, information-rich pattern, correctly not treated as suspicious agreement. **Nulls recorded as
nulls:** Phase 6E (Observance) is the clearest instance — a genuine null, stated as such, not papered over.
**Deficit researched after the profile, not before:** confirmed — Step 3 research (Daegu/Córdoba/Volgograd) ran
strictly after Phase 1's profile was complete. **Unrecognized Instrument:** not run this pass — flagged as a
genuine gap for Step 9, since `02` §4.2 requires it be run after the capability profile and this pass never
returned to it.

---

**Feeds:** the Review Panel (next) and Step 9 (Record) — the REQUESTED-for-Step-9 items above (universe-repo
canon check, Gate 9's return-route question, the Unrecognized Instrument, the quarry-export swap-test weakness)
should all be resolved or explicitly carried forward before this run is declared complete.
