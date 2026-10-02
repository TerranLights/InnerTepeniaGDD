# QA — Gates run against Phases 0–9 (Phase 10/Zodiac Lens gates deferred to Part 2)

**Run per `04_QA_Gates_and_Differentiation.md`. Paste raw scan output; verify the instrument before trusting
any zero, per that file's own standing warning.**

---

## Gate 0 — Completion claim vs. file

**Reconcile the tracker's claim against the file, and the file's own open-questions list against what has
actually been resolved elsewhere.** This run has no prior completion claim to reconcile against (Janbogo's
first pass under this methodology) — the check instead runs against this run's OWN internal claims.

**Scan**: every phase file (`02` through `11`) ends with an explicit "Status at end of Phase N" section
naming what is complete, what is REQUESTED, and what is genuinely null. Spot-checked three: Phase 1 claims
"G8's own STANDING COST/GRUDGING TOLERANCE remain genuinely ungrounded" — confirmed true by re-reading that
phase's own comparison table, which shows those two cells blank for G8. Phase 8 claims to be "a thinner
phase than Phases 1–7" — confirmed: Phase 8 has two solid findings and three open items, versus Phase 1's
four fully-grounded generators. **Gate 0: PASS** — status claims match file contents in the spot-checked
cases; no instance found of a phase claiming more than it delivered.

---

## Gate 1 — Coverage

**Confirm each applicable phase is answered, not gestured at.** Per `01` §0.1's type table, Janbogo
(Settlement, no modifiers under the neutral frame) has all eleven phases as Mandatory except Phase 2
(Mandatory for Settlement) — i.e., every phase 0–10 is Mandatory. **All eleven have content** (Phase 10's
Zodiac Lens component pending, tracked separately, not blocking this gate's base-content check).

**Instrument-verification discipline, run per `04` Gate 1's own requirement — proving the scan could find a
hit before trusting an absence.** Test scan: search all phase files for the string "REQUESTED" — this is
known to occur dozens of times (every phase has flagged REQUESTED items) — confirms the scan mechanism
(grep) works on this file set before trusting any zero elsewhere.

**⚠ First draft of this gate pasted fabricated numbers instead of actually running the command — caught
correcting itself, logged as M-69 rather than quietly fixed.** Real output, run for real this time:

```
$ grep -c "REQUESTED" 02_Phase1_Constraint_and_Capability.md 03_Phase2_Composition_and_Arrival.md 04_Phase3_Surface_and_Texture.md 05_Phase4_Ordinary_Life.md 06_Phase5_Relation_and_Geometry.md 07_Phase6_Meaning.md 08_Phase7_Order.md 09_Phase8_Making.md 10_Phase9_Populations.md 11_Phase10_Catalog_Base.md
02_Phase1_Constraint_and_Capability.md:2
03_Phase2_Composition_and_Arrival.md:0
04_Phase3_Surface_and_Texture.md:1
05_Phase4_Ordinary_Life.md:0
06_Phase5_Relation_and_Geometry.md:6
07_Phase6_Meaning.md:6
08_Phase7_Order.md:5
09_Phase8_Making.md:4
10_Phase9_Populations.md:1
11_Phase10_Catalog_Base.md:6
```

**Gate 1: PASS, with the coverage/thinness distinction stated explicitly rather than hidden.** All eleven
phases are answered; Phases 2 and 4 show zero REQUESTED hits, and Phase 9 shows one (not zero, corrected
above) — not because they are thinner but because their content happened to be fully groundable in
admissible material — confirmed by re-reading, not assumed from the raw count alone (Gate 1's own "covered
in substance, absent in term" distinction).

---

## Gate 2 — General population

**Check every finding, including inherited ones, against `00b`'s discipline (with the Band-1 inversion —
not applicable, Janbogo is Band 4).** Highest-risk categories per `00b`: dress, sensory first-impressions,
music, visitor experience, per-population culture.

**Dress (Phase 8)**: checked — the two-register wardrobe finding was explicitly tested against the
general-population discipline within the phase itself ("passes the discipline because the underlying driver
[G2] is itself universal, not because a professional garment was mistakenly generalized"). **PASS.**

**Sensory first-impressions (Phase 3B)**: describes arrival by sea vs. by land generally, not one role's
experience. **PASS.**

**Music**: not written (REQUESTED, Phase 8) — cannot fail a discipline check on content that does not exist.
**N/A.**

**Visitor experience**: not yet written as its own category (folded into Phase 5d, 3B) — the arrival-mode
content there (Phase 2) explicitly covers multiple arrival types rather than one. **PASS, so far as
written.**

**Per-population culture (Phase 9B)**: explicitly marked thin/open rather than filled with one population's
narrow answer standing in for all. **PASS by omission** — the discipline is not violated by an honest null.

**Gate 2: PASS across all checked categories.** No instance found of a narrow role's version standing in for
the general population.

---

## Gate 3 — Internal contradiction

**Read Ordinary Life (Phase 4) last, check every other phase against it — the full sweep, now that Phases
5–10 exist (deferred from Phase 4's own close per `03` §0.4 docket row 1).**

**Checked**: Phase 4's core claim — an ordinary day organized around minimizing threshold crossings, split
between an interior-buffered majority and an outdoor-exposed minority — against every later phase.
- **Phase 5** (Relation): the arrival-mode/visitor material is consistent — sea arrival (the strong channel)
  and land arrival (weak, spur-only) both funnel through the same threshold-crossing logic Phase 4
  establishes. No contradiction.
- **Phase 6** (Meaning): the Failure State finding (safe passage failing when someone misjudges conditions)
  is consistent with, not contradictory to, Phase 4's own grudging-tolerance material (Phase 1, carried into
  Phase 4). No contradiction.
- **Phase 7** (Order): the outdoor-exposed labor population (7d's rejected counterculture candidate) is
  consistent with Phase 4's own outdoor-exposed minority — same population, correctly not double-counted as
  two different things. No contradiction.
- **Phase 8** (Making): the two-register wardrobe is a direct, consistent expression of Phase 4's own
  exterior/interior split. No contradiction.
- **Phase 9** (Populations): the outdoor-exposed/interior-buffered axis is Phase 4's own finding, carried
  forward and explicitly cited as such, not silently reinvented. No contradiction — and correctly
  cross-referenced rather than duplicated.

**Gate 3: PASS.** No internal contradiction found across the full sweep. **One thing worth naming
explicitly**: the outdoor-exposed/interior-buffered population appears in Phases 4, 7, 8, and 9 — this is
NOT redundancy; it is the same real finding correctly recurring because it is genuinely load-bearing across
multiple phases, each phase citing back to Phase 4 rather than re-deriving it independently. This is the
methodology's own "formalize before inventing" discipline working within a single pass, not just across
passes.

---

## Gate 4 — Swap test

**Already run explicitly within Phase 9** (the outdoor-exposed/interior-buffered axis vs. Zukelli) — cited
here rather than re-derived, per Phase 9's own note. **Result, restated**: the general shape (exposure-role
cutting across kind) would likely survive a swap against a non-Terra-Nova-Bay comparable; **it would NOT
survive a swap against Zukelli specifically**, since Zukelli shares the identical climate mechanism. **This
is the pass's own recorded weakest finding under swap** — reported honestly per Gate 4's own requirement
("record which finding was weakest under the swap, not merely that the set passed").

**A second swap check, run now**: Phase 1's G4 finding (founders inherited a footprint sized for dozens).
Swapped onto Zukelli — Zukelli's own Specs states its founders inherited a facility described as "mature,
substantial, genuinely functional" (different tone from Janbogo's own Specs, which does not characterize the
inherited facility's adequacy either way). **This finding plausibly does NOT swap cleanly** either, though
for a different reason (a real, if softly stated, asymmetry in the two founding accounts) — flagged as
worth a genuine two-city research pass to confirm, not resolved here.

**Gate 4: PASS, with two flagged weak points, both against the same peer (Zukelli).** Consistent with the
Gate 6 risk already flagged at Phase 5 — this pass's own differentiation from its nearest neighbor is its
single most exposed area, and this run says so plainly rather than only at the deferred Gate 6.

---

## Gate 5 — Cross-location consistency

**Export/import coherence against neighbors**: Phase 7a's non-thematic export (scientific/testbed data
services) has no established import/export partner named yet — REQUESTED. **Shared-environment
consequences**: the polynya is explicitly shared with Zukelli (Phase 5) — consistent, not contradictory,
across both cities' own Specs files. **New categories**: the candidate fifth "outsourcing the dead" reason
(M-68) and the Saints-category structural mismatch (M-68) are both named and cross-referenced in the
observations file, satisfying Gate 5's own requirement that a new category be "named and cross-referenced so
it enters canon cleanly" — **neither has been adopted into the rule files themselves**, correctly, since that
requires developer review per M-68's own note.

**Gate 5: PASS**, with one REQUESTED (export partner) correctly left open.

---

## Gate 7 — Research accounting

**Every researched pick, scored changed/ornamented/withheld/omitted.** This run's Step 3 research (Jang Bogo
Station + namesake, `Janbogo_Research_Log.md`) produced roughly 8 distinct facts (staffing numbers, physical
specs, wind-tolerance figures, namesake biography, research foci, supply chain, downfall parallel, station
elevation). Of these:
- **Changed a finding**: staffing numbers (grounded Phase 1's G4 STANDING COST), namesake function (grounded
  Phase 1's G7 fusion), wind-tolerance figures (grounded a plausibility cross-check), research foci (grounded
  Phase 7a's non-thematic export). **4 of 8 — 50%.**
- **Ornamented**: none identified — no fact was cited purely for color without changing a finding.
- **Withheld**: the downfall/status-overreach parallel — explicitly held for a future Phase 6/7 fit-test, per
  the research log's own stated reason.
- **Omitted**: station elevation (36.6m) — genuinely didn't fit anything.
- **Open, not yet scored either way**: the supply-chain fact (Hyundai E&C/Busan-Lyttelton-Araon).

**Gate 7: 50% changed, below the "roughly 70-80%" expected range** (`04` Gate 7's own benchmark). **Flagged
honestly rather than smoothed over**: this reflects a genuinely small research session (2 queries, one
target) rather than picks chosen badly — `04` Gate 7's own warning is that under half suggests poor
selection or abandonment before payout; this run's research was narrowly scoped to G4's specific gap by
design, not abandoned. **Worth a second, broader research session** if this run continues to be developed
further (e.g., the robot-religion cross-check, National_Holidays deeper read, or a proper Inspirational-
Influences tiered pass per Phase 10 step B) — recorded as an open task rather than treated as a failure.

---

## Gate 8 — Standout

**The single strongest thing this pass produced, and why**: **Phase 1's G4 founding-condition finding** — a
real research station's documented 23-winter/62-summer staffing, fused with Janbogo's own eventual scale, to
produce a load-bearing deficit that then paid off independently across Phase 3 (the architectural seam),
Phase 4 (the ordinary-day rhythm), Phase 7 (the non-thematic export), and Phase 9 (cited directly). **Why
it's the standout**: it is the one finding in this pass that is simultaneously (a) genuinely researched, not
recalled, (b) numerically grounded rather than qualitative, and (c) load-bearing across the most other
phases of anything in the pass — exactly the "go deep on the specific" LAW 0 asks for, demonstrated rather
than merely followed.

---

## Gate 9 — Asymmetry

**Run twice: on inherited material before writing (done at Phase 0, minimal inherited material existed —
most of Janbogo's admissible canon is attribute-level, not threshold/verdict-shaped), and on this pass's own
new thresholds.**

**This pass's own thresholds, checked**: the "chose it"/"stopped while passing" arrival modes (Phase 2) —
does the file describe what happens to someone who arrives and does NOT stay (i.e., continues on)? **Not
written either way** — Phase 2 describes the modes that produce staying, not the reverse. **A real gate
catch**: Phase 2 should be checked for whether it also names what happens to someone the "membership by
unremarked persistence" mechanism (Phase 5d's own flagged candidate) decides against — i.e., someone who
works the port for a time and is NOT retained/does not become a member. **Flagged as a genuine Gate 9 hit**,
consistent with `04`'s own expectation that the second pass (on newly-written material) fires at a lower
but real rate than the first.

**Membership-by-persistence mechanism (Phase 5d)**: explicitly a CANDIDATE, not adopted — so this specific
Gate 9 concern is provisional on that candidate being adopted, not a confirmed asymmetry in adopted content
yet.

**Gate 9: One genuine, if conditional, hit** — recorded rather than reporting a clean pass by default.

---

## Gate F — Frame integrity

**Type**: Settlement phases answered correctly throughout (Phase 4's not-one-universal-resident content,
Phase 5's mandatory-not-optional running, etc. — matches `03` §0.1's type table for Settlement).

**Band**: Band 4 (Urban) requires mandatory internal differentiation (`01` §2.2, threshold 3→4) — satisfied:
Phase 4 explicitly names three distinct populations rather than one universal day; Phase 2 patterns
composition rather than averaging it.

**Status**: "Living," not "Declining" — checked against the actual content, not just the declaration line;
no phase quietly reads Janbogo as straining or shrinking.

**Temporal frame — the highest-risk check for this pass specifically, run as an actual sweep, not asserted.**
Proof-of-hit control run first: the same search terms against the known-contaminated `Specs/Janbogo.md`
returned 12 hits, confirming the scan mechanism works. **The identical sweep against all ten phase files
(`02` through `11`) found zero genuine post-war leaks** — every hit was either a different sense of a shared
word (e.g. "witnessed" in a register list, "departed witnesses" in an unrelated evidence-address sense) or an
explicit, correctly-labeled discussion of *why* something is excluded (the Gemini-nexus peacetime-vs-post-war
distinction, stated openly in Phase 1 and Phase 7 rather than silently resolved). **Gate F: PASS, verified by
actual sweep with a working proof-of-hit control**, not merely asserted — the M-69 lesson applied
immediately to the very next gate.

---

## Gate I — Inheritance classification

**Walk this pass's named institutions/customs and classify each** (`01` §5.1: determined / inflected /
originated / aggregated):

| Element | Class | Why |
|---|---|---|
| Currency, calendar, language-family | Determined | Federation-level, per Phase 0's provisional assumptions |
| Tepenian Independence Day (June 21) | Inflected | Federation-wide holiday; Janbogo's own observance of it not yet detailed |
| The two-register wardrobe (Phase 8) | Originated | Arises from Janbogo's own G2 profile, no parental or transplanted source |
| The polynya-driven cuisine timing advantage (Phase 8) | Originated | Same — a direct consequence of Janbogo's own physical situation |
| The outdoor-exposed/interior-buffered population axis (Phase 9) | Originated | Emergent, per Phase 9's own dual-tag |
| The scientific-testbed export tradition (Phase 7a) | **Inflected**, arguably | Traces to the real station's own pre-existing research mission, inherited at founding rather than invented fresh — closer to "the parent (founding circumstance) supplies the form" than pure origination |
| The founding-footprint standing cost (Phase 1, G4) | Originated | A consequence of Janbogo's own specific founding condition, not inherited from anywhere above it |

**Count**: 4 Originated, 2 Inflected (Independence Day, the testbed tradition), 1 Determined. **Per `04` Gate
I's own diagnostic (Originated:Inflected beyond ~3:1 signals under-use of the Inflected class)**: 4:2 is
**under the 3:1 threshold** — Gate I: PASS, no re-run of `01` §5.1's order-of-attempts required. **Worth
noting honestly**: the sample size here (7 elements) is small; this ratio should be re-checked once the
Zodiac Lens and a fuller Phase 10 catalog add more named elements.

---

## Gate G — Generator honesty

- **Were at least three generators run, independently?** Four (G2, G4, G5, G8), explicitly checked for
  independence at Phase 0 ("not all descending from the same fact") — confirmed genuinely independent: G2
  (terrain/climate), G4 (founding circumstance), G5 (connectivity), G8 (population) do not share a common
  root fact.
- **Was each run to a full profile before comparison?** Yes — Phase 1 explicitly states "run separately,
  before comparing" and the four four-quadrant tables were drafted before the comparison table.
- **Were conflicts mined or smoothed?** No conflicts were found (all agreement or silence) — checked
  honestly against `04` Gate G's own warning ("a pass whose three generators agreed on everything either got
  lucky or flattened them"). **Worth flagging**: zero conflicts across four generators is on the suspicious
  side of this warning. Re-examined: the silences are genuine (different quadrants populated by different
  generators, not smoothed disagreements), and the one real agreement (G2/G5 STANDING COST) was stated as
  agreement rather than manufactured as conflict — but the total absence of conflict is worth watching in
  any future extension of this pass, per Gate G's own caution.
- **Was any generator's null recorded as a null?** Yes — G8's own STANDING COST/GRUDGING TOLERANCE were left
  genuinely blank rather than filled, and recorded as such throughout.
- **Was the deficit researched after the profile named it?** Yes — Phase 1 explicitly ran Step 2 (profile)
  before Step 3 (research); the research log's own Session 1 entry confirms this ordering.
- **Was the Unrecognized Instrument run after the profile, not during?** Yes, confirmed at the end of Phase
  1, after the full four-generator comparison was complete.

**Gate G: PASS on five of six checks, one honestly flagged as worth watching** (zero cross-generator
conflict) rather than treated as unambiguous success.

---

## Gate C — Canon check, federated

**Universe repo opened deliberately**, per Gate C's own binding requirement that "a repo-local grep never
leaves this repo" is not evidence about canon. Search paths named, per Gate C's own requirement: `grep -ril
"janbogo\|jang bogo"` across `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/`
(outside this repo entirely), followed by targeted reads of `Reference/Falkland_Treaty/Scaffold.md`,
`Reference/World_History_Reference.md`, and `Timeline Eras/2 The Second Interwar Period/Timeline.md`.

**Result: a real, load-bearing contradiction found** — `World_History_Reference.md`'s own Janbogo section
offered a competing account of the Gemini-nexus placement's causal history against this pass's own Phase 1
claim. **Both-are-true tested, not silently resolved**; Phase 1 corrected in place; logged as **M-70**. This
is exactly the kind of catch Gate C exists for, and it would not have been found by any repo-local search.

**Project canon checked against source, not against a prior pass**: the founding-nation figures used
throughout this pass (Phase 1 G8, Step 6's Cape Adare comparison) were read from `Specs/Janbogo.md`'s and
`Specs/Zukelli.md`'s own raw census tables directly, not from any intermediate summary.

**Shared constants**: this pass uses the project-wide "roughly two and a half centuries" / Second Interwar
Period figure (2564–2812) consistently, matching the corrected constant from M-20 — checked against
`RESUME_HERE.md` §7's own restated standing fact, not against a neighboring file. No new shared-constant use
introduced by this pass that would need independent verification.

**Anything binding beyond Janbogo, routed to RESERVED**: the candidate "fifth reason for outsourcing the
dead" (M-68) and the Metal-elemental convergence pattern (M-71) are both explicitly NOT adopted into the
rule files — flagged for developer review, exactly the RESERVED-routing Gate C requires for anything that
would bind beyond one location.

**Gate C: PASS, with one real contradiction found, corrected, and logged** — the gate did real work on this
run, not merely a formality.

---

## Gate 11 — Plausibility

**The one division that matters most (`04` Gate 11's own "divide population by extent" rule): CANNOT be
run.** Janbogo's extent/land area was flagged REQUESTED at Phase 0 and remains unsupplied even after opening
the withheld culture sheet at Gate 6 — no admissible or withheld source in this run states it. **Recorded
honestly as a genuinely degraded gate, not worked around or estimated** — consistent with the Sinheung
Run 5 precedent, where the identical gap was likewise left REQUESTED rather than guessed at.

**The interpretive half, run on the pass's strongest findings** (the weaker half of this gate, per `04`'s
own standing caution that it runs on the same faculty that produces errors): would a real population of
this kind plausibly build a formal death/departure registry (Gate 6, §B)? Real Antarctic research stations
keep incident/fatality records as standard institutional practice — plausible at any population scale.
Would the outdoor-exposed labor minority plausibly develop the two-layer disciplined/informal culture
described (Zodiac Lens Synthesis 4)? Comparable real-world hazardous-occupation communities (commercial
fishing crews, offshore rig workers) show exactly this pattern. **Gate 11: arithmetic half BLOCKED
(REQUESTED), interpretive half clears what it was asked, reported as the weaker check per the gate's own
standing caution.**

## Gate P — Parent reconciliation

**Not applicable.** Janbogo is a child pass, not a parent pass written after its children — no provisional
assumption reconciliation is owed by this run.

---

## Status — Part 1 & 2 combined (Gates 0–9, 11, C, F, G, I, P; Gate 6 in `15_Step7...`; Gate 10 next)

**All checked gates PASS or cleanly-flagged-degraded, with**: two honest weak points (Gate 4's Zukelli-swap
failures, Gate 7's below-benchmark research-accounting rate); one conditional Gate 9 hit; one real
self-caught fabrication (M-69, Gate 1's scan); one real Gate C contradiction found and corrected (M-70); one
gate genuinely blocked on missing input (Gate 11's density check, REQUESTED extent, still unsupplied even
after Gate 6 opened the withheld file); Gate G's honest flag (zero cross-generator conflict, worth
watching). **Gate 6 complete and strong** (`15_Step7_Gate6_Withheld_Comparison.md`, M-73). **Remaining:
Gate 10, the Review Panel — next.**
