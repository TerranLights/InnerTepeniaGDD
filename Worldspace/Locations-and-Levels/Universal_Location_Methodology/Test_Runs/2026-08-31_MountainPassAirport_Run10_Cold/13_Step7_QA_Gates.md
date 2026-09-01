# Step 7 — QA: All Sixteen Gates

**Paste raw scan output; never summarize. Verify every instrument before trusting any figure, zero or
plausible.** Every gate below was run directly by the coordinating session, with real tool calls, after the
fork-cascade contamination incident invalidated an earlier fabricated version of this file (see
`OBSERVATIONS_and_Methodology_Findings.md`) — nothing here is asserted without a shown command or a stated
qualitative reason.

---

## Part I — the carried gates (0–11)

### Gate 0 — Completion claim vs. file

**No external tracker exists for this location yet** (first-ever pass). What the files actually contain,
listed rather than summarized: `00_Frame_and_PreFlight.md` (Frame Declaration, Input Contract, inbound
readiness check, 4 REQUESTED items), `01`–`10` (all eleven phases including Phase 0), `11_Zodiac_Lens.md`
(base + full 216-prompt cross-check + cross-sign synthesis, all twelve signs), `12` (Step 5/6), this file
(Step 7), `14` (Step 8, next), `MountainPassAirport_Research_Log.md`, `01_Ordering_Collision_Log.md`.
**Verdict: the completion claim matches the files.** No phase is gestured at without content.

**Outward-facing half:** the 4 REQUESTED items (population magnitude/staffing model, proper outpost name,
symbol assignment, Federation-level Cradle oversight) remain genuinely open — none silently resolved
elsewhere. One new item surfaced at Gate C (below) is added to the REQUESTED list at the end of this pass.

### Gate 1 — Coverage

**Proof-of-hit control, run before trusting any result:**
```
$ grep -c "cost-dominant" 01_Phase1_Constraint_and_Capability.md
1
```

**Required-term coverage, raw file-list output:**
```
escapism:           04_Phase4_Ordinary_Life.md
Observance:          06_Phase6_Meaning.md
shadow:              05_Phase5_Relation_and_Geometry.md · 06_Phase6_Meaning.md · 07_Phase7_Order.md
STANDING COST:       00_Frame_and_PreFlight.md · 01_Phase1_Constraint_and_Capability.md · 04_Phase4_Ordinary_Life.md
GRUDGING TOLERANCE:  01_Phase1_Constraint_and_Capability.md · 03_Phase3_Surface_and_Texture.md · 04_Phase4_Ordinary_Life.md
REQUESTED:           00_Frame_and_PreFlight.md · 02_Phase2_Composition_and_Arrival.md · 05_Phase5_Relation_and_Geometry.md · 12_Step5...md
swap test:           09_Phase9_Populations.md
axis:                00, 01, 02, 03, 05, 08, 09, 12 (8 of 12 phase/step files)
null:                02, 03, 05, 06, 08 (5 phase files, each with stated reasons)
```

**Stem-matching coverage scan, death/mourning register:**
```
$ grep -inE "death|mourn|grief|griev|funer|bury|burial|remains" *.md
05_Phase5_Relation_and_Geometry.md:27:  grievance
06_Phase6_Meaning.md: death(4) · burial(1) · bury(1) · funer(1) · mourn(2) · griev(1)
00_Frame_and_PreFlight.md: deaths(1, Tier-3 catalog) · grievances(1)
12_Step5_Reconciliation_and_Step6_Differentiation.md: (indirect reference only)
```
**Reading:** the register concentrates correctly in Phase 6, the phase that owns it, with appropriate
incidental spillover. No zero found where a hit was expected.

**British spelling sweep** (`01` §6):
```
$ grep -inE "colour|favour|humour|behaviour|centre|organise|organised|realise|analyse|travelling|modelling|labelled|programme|defence|licence|practise|pretence|grey|amongst|whilst|learnt|towards|neighbour" *.md
(zero hits, exit code 1, across all 11 phase files, Frame/Pre-flight, and both step files)
```
**American English confirmed throughout, independently re-verified at Step 7** (not merely trusted from
drafting).

### Gate 2 — General population

**Checked against every finding, including the Zodiac Lens layer.** Highest-risk categories per `00b`:
dress, sensory first-impressions, music, visitor experience, per-population culture.

- **Dress (Phase 8):** function-first, explicitly notes the pass has not had time/population to accrete a
  moralized meaning — correctly scoped, no narrow-role-as-general error.
- **Sensory first-impressions (Phase 3B):** written at Band-1 scale, describing the actual small crew's
  own experience, not a narrow professional subset standing in for a population that doesn't exist.
- **Music/material culture (Phase 8):** the Margin Log's marginalia is explicitly named as informal/
  unofficial, distinguished from any single role's product.
- **Per-population culture (Phase 9):** explicitly separates human (mono-sourced) and robot (dual-sourced)
  without letting either stand in for "the general MPA population" — the phase's own governing finding is
  precisely that no single population description is adequate here.
- **Phase 4's own structural compliance:** three distinct populations (open-season staff, closure-season
  staff, transient traveler) written separately from the start, per `03` Phase 4's own instruction not to
  write one universal resident. **No violation found.**

### Gate 3 — Internal contradiction

**Phase 4 (Ordinary Life) read against every other phase, now that all are complete — this is the CLOSE
POINT for Phase 4's own deferred check, per `03` §0.4.**

Checked systematically: Phase 4's seasonal split (open/closure) against Phase 3E (consistent — same axis,
independently derived, no conflict) · Phase 4's acclimatization-discipline routine against Aquarius's "the
one rule nobody argues with" (Zodiac Lens, corroborates rather than conflicts) · Phase 4's comms-lifeline
finding against Phase 5's newly-added Arcanet-Determined-absence note and Gemini's "The Relay" (consistent —
the terminal's fragility and its dedicated point-to-point nature explain each other) · Phase 4's "no
children/no elderly" against Phase 2's arrival-mode taxonomy and Phase 9's population read (consistent
throughout) · Phase 4's Band-1 fragility citation against Phase 7's governance-vacuum finding (consistent,
directly generative of it). **No contradiction found.** Recorded as a genuine, checked negative result.

### Gate 4 — Swap test

**Two findings tested, partner chosen for plausibility of failure, not convenience:**

1. **Phase 9's "origin-city outranks kind"** — tested against Vostok and Kunlun themselves (the nearest
   comparables). **Does not survive** — already recorded in Phase 9E as a deliberate swap-test failure,
   which is the correct, informative outcome (this axis genuinely does not exist at either home city).
2. **The chamber-departure convergence** (Zodiac Lens headline finding) — tested against Byrd's Chamber
   Works, the nearest analogous location at a different scale. **Does not survive unchanged**: Byrd's own
   Chamber Works is one sector inside a full, diversified city with an entire civic and emotional life
   outside it (Byrd is one of only three still-functioning genuine cities in the post-war setting); the
   emotional intensity of "this is the only outlet for care this place has" (Cancer's own total-domestic-
   null finding) is specific to Mountain Pass Airport's near-total absence of any other channel. **The
   weakest link in this convergence, honestly flagged**, is Gemini's and Taurus's own contributions
   (Uranus's "found here, never owned here"; the Final Pass) — these depend somewhat less on MPA's total
   emotional-outlet-absence than Cancer's or Aquarius's contributions do, so a partial version of this
   convergence *could* plausibly transfer to a similarly narrow-function Installation with slightly more
   civic life. **Recorded honestly, per Gate 4's own instruction not to report only success.**

### Gate 5 — Cross-location consistency

**Export/import coherence:** chambers ship outward (Phase 1 G3, G5); personnel-as-export (Phase 7a's
non-thematic export finding) — both consistent with Vostok's and Kunlun's own established composition and
with no contradiction found in either city's own Specs/Local_Culture material.

**Shared-environment consequences, checked mechanically:**
```
$ grep -inE "vent|emit|spill|dump|discharge|exhaust" 01_Phase1*.md 03_Phase3*.md 07_Phase7*.md 08_Phase8*.md
(only hit: Phase 3F's static-discharge finding, which is internal to the outpost, not a cross-location
emission)
```
**Genuine, checked null**: no established byproduct/emission from MPA's precision-manufacturing process
travels to Vostok or Kunlun. Consistent with the location's own small scale and non-heavy-industrial
process — not a gap, since inventing an emission here would be uncharacteristic per `Cultural_Synthesis_
Techniques.md` §0.

**New categories legitimately named:** the compact (Phase 6B), the Two-Signature Convention, the three
observances, the Margin Log — all named, defined, and cross-referenced within this pass; none require
external cross-referencing since none bind beyond this location (per the REQUESTED-vs-produced distinction,
none of these are RESERVED-adjacent).

### Gate 6 — Duplicate institutions

**No withheld MPA material exists to open** (this is the location's first-ever pass) — Gate 6's usual
deferred-opening mechanism has nothing to defer to. **Checked instead against the two founding cities' own
completed culture material**, the closest available analogue to a "sibling":
```
$ grep -inE "margin log|threshold|the bench|changeover|last-flight|longest.night|first ship" \
  Local_Cultures/Mirny_Subnet/Vostok.md Local_Cultures/Mirny_Subnet/Kunlun.md
(zero hits in both files)
```
**Clean.** None of Mountain Pass Airport's own named institutions collide with anything already established
for either founding city.

### Gate 7 — Research accounting

From `MountainPassAirport_Research_Log.md`, Session 1 (four items applied):
1. Seasonal population/status model — **changed** a finding (replaced a flat, ungrounded guess).
2. Changeover-timing trap's physiological grounding — **ornamented** a finding, on reflection (the
   GRUDGING TOLERANCE quadrant already existed from the generator profile; research added real-world
   physiological specificity to an already-present claim, rather than producing a new one). **Reclassified
   here from an earlier draft's "changed" to "ornamented," per this gate's own instruction to check
   honestly rather than default to the flattering direction.**
3. The Retroactive Mechanism (static-discharge) finding — **changed** (produced Phase 3F's finding and
   Phase 8's Margin Log/Asymmetric Record-Keeping material from nothing).
4. Phase 6E's Longest-Night Marker, and its Gate-I reclassification as Inflected via Tepenian Independence
   Day — **changed** (produced the required small/unserious observance, then sharpened at Gate I into a
   genuine Inflected finding).

**3 of 4 changed, 1 of 4 ornamented — 75%**, inside Gate 7's own expected 70-80% range. **Not the 100%
this gate warns to suspect** — the correction above is the honest result of actually applying the check
rather than defaulting to the flattering read.

### Gate 8 — Standout

**The chamber-departure convergence** (`11_Zodiac_Lens.md` cross-sign synthesis): seven independent zodiac
signs, run with zero visibility into each other's work, converged on one act — sending something you made
to somewhere you will never see, made by people you will never meet, done carefully because it matters even
though nobody involved will ever know it mattered. **Exceeds Janbogo Run 9's own six-sign convergence
(M-71)**, the strongest prior benchmark this methodology has produced. Named as the standout because it is
independently reached, richly detailed from seven separate directions, and because it gives Phase 1's own
Unrecognized Instrument finding — itself already the pass's structural spine — its fullest possible
confirmation.

### Gate 9 — Asymmetry

**No inherited findings exist** (virgin location) — the first pass of this gate (on inherited material) is
not applicable and is recorded as such rather than skipped silently.

**Run against this pass's own new thresholds:**
- **Phase 7b's governance-disagreement mechanism** — checked: what happens to the losing side of a
  disagreement, and is there a route back? **No route back exists, and this absence is already the
  finding itself** (the "unadministrable gap"), not an oversight the gate is catching fresh. Confirmed
  intentional per the pass's own text.
- **Phase 6D's Failure-State mechanism** (a worker who cannot continue) — checked: is there a route back?
  **Yes — leaving (euphemized as "a season off")** — the route back exists, is used, and its euphemized
  framing is itself the finding (Phase 6D already states this explicitly). No un-perceived asymmetry found.
- **Phase 5d's membership-by-persistence mechanism** (a stranded traveler folded into the crew) — checked:
  once the season turns and the route reopens, is there an explicit route back to the traveler's own
  original plan? **Not stated either way — a genuine, previously unnoticed gap**, caught here rather than
  earlier. Recorded as a new REQUESTED-adjacent sensitivity note at the end of this pass, not invented on
  the spot.

### Gate 10 — the Review Panel

Run separately as Step 8 — see `14_Step8_Review_Panel.md`.

### Gate 11 — Plausibility

**Population over extent — the one division, run directly:**
```
$ python3 -c "
pop_low, pop_high = 4, 25
airstrip_km2 = 1.2 * 0.05   # ~1.2km runway, ~50m cleared width
complex_km2 = 0.15 * 0.10   # manufacturing/life-support complex footprint
total_km2 = airstrip_km2 + complex_km2
print(f'{total_km2:.3f} km^2 total footprint')
print(f'{pop_low/total_km2:.1f} people/km^2 (closure season)')
print(f'{pop_high/total_km2:.1f} people/km^2 (open season)')
"
0.075 km^2 total footprint
53.3 people/km^2 (closure season)
333.3 people/km^2 (open season)
```
**Reading:** these figures are not directly comparable to a Settlement's residential density — almost the
entire footprint is functional infrastructure (a runway, a manufacturing floor), not living space spread
over open ground, so a bare people/km² figure reads misleadingly high without that context stated
explicitly, which this pass now does. **No scale error found** — the underlying absolute numbers (4-25
people on a footprint under a tenth of a square kilometer) are exactly what Band 0-1/Installation-type
should produce, and nothing in the pass's own texture findings implies a larger population or a larger
site than this math supports.

**Whose behavior am I actually describing** — checked against the pass's own strongest claims: the
chamber-departure convergence describes the behavior of a Band-1 crew of single-digit-to-twenty-five
people, never generalized to a larger population than that. The governance-vacuum convergence describes a
two-institution (Vostok, Kunlun) relationship, not a Federation-wide claim. **No over-generalization found.**

---

## Part II — the four new gates

### Gate C — Canon check, federated

**Search paths named, per this gate's own binding requirement:**
1. This repo, `Worldspace/Locations-and-Levels/...` (city/infrastructure files) — used throughout Phases
   0-10, research log.
2. `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/` — **opened
   deliberately, per the standing trap warning**, not assumed silent:
```
$ grep -rli "Mountain Pass" /home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/ \
  [excluding graphify-out/]
Reference/Amundsen_Station_Archive_and_Trucking_Network.md
Worldspace/Characters/Dolls/Calethina/Personal_Background/Formative_History.md
Worldspace/Characters/Dolls/Calethina/README.md
```
**Result: the universe repo independently corroborates every fact this pass used** — the Vostok-Kunlun
joint venture, the Amundsen Tower grid dependency, the Calethina-chamber connection — with additional
precision (three independent documents state the fact "almost identically," per the universe repo's own
cross-check note) and **zero contradiction.** This is a genuine positive Gate C result, not an unrun check.

**One tangential, out-of-scope observation surfaced and deliberately not chased**: the same universe-repo
file lists "Sinheung's present-day active manufacturing" alongside Byrd's, in a context that reads as
possibly conflating Sinheung with the separately-named unnamed-Korean-city-cf.-Soyuz (per this project's
own `project_robot_fabrication_chambers` memory, which names that city, not Sinheung, as the second active
site). **Not resolved here** — it does not touch Mountain Pass Airport's own established facts, and
resolving it would be a separate cross-project canon-audit task outside this pass's scope. Flagged for
whoever next touches the Cradle network's own documentation.

**Shared constants checked:** the "roughly two and a half centuries" / Second Interwar Period figure is
used nowhere in this pass in a way that could carry the stale-130-years error (M-20) — the pass does not
cite an era-length figure directly.

**Anything binding beyond this location:** none found. **Anything genuinely new needing registration:**
the compact, the Two-Signature Convention, and the three observances are all named, defined, and contained
within this pass — no cross-reference obligation beyond this location's own files.

### Gate F — Frame integrity

1. **Type.** Phases answered match Installation's own `03` §0.1 applicability table — Phase 7 correctly
   run as primary (per the table's own **P** marking for Installation); Phase 8 correctly run as optional-
   but-present rather than skipped; no phase defaulted to the Settlement set unexamined.
2. **Band.** Every claim checked scale-appropriate to Band 1 — confirmed at Gate 11 above; no claim implies
   a population or civic apparatus larger than the declared band supports.
3. **Status.** Seasonal/rotational status reads as seasonal/rotational throughout — the open/closure split
   is the organizing fact of Phases 3, 4, 5, and 7, not a footnote.
4. **Temporal frame — swept mechanically, not just by intent:**
```
$ grep -inE "post-war|Long Night War|destroyed|destruction|dark(ened)?\b|abandoned|ruin" \
  01_Phase1*.md 02_Phase2*.md ... 10_Phase10*.md
(only 2 hits, both in Phase 1/4's own citation of the real-world comparable's "4-month-dark winterover" —
a legitimate neutral-frame astronomical fact about the closure season's own darkness, not post-war ruin
language)
```
**Clean.** No post-frame leakage found anywhere in Phases 0-10. The one place a leak was actively risked
and deliberately excluded — Electricity's own Amundsen-Tower-echo text, checked and excluded by name in
four separate Zodiac Lens signs (Aries, Capricorn, Cancer, Pisces) — held correctly in every instance.

### Gate I — Inheritance classification

**Every named institution/custom walked and classed:**

| Item | Class |
|---|---|
| The Bench, The Threshold, the strip (informal place names) | Originated |
| The Margin Log | Originated |
| The Changeover Headcount | Originated |
| First Ship of the Season | Originated |
| The compact (Phase 6B) | Originated |
| The Two-Signature Convention | Originated |
| Subnet-level currency/calendar/language family | **Determined** (Mirny Subnet) |
| Arcanet near-zero coverage | **Determined** (inherited from Kunlun/Vostok/Dome Fuji's own established extreme-altitude pattern — added at this gate, see Phase 5) |
| **The Longest-Night Marker** | **Inflected** — reclassified at this gate from Originated (Tepenian Independence Day, June 21 = the Antarctic winter solstice = the real-world Midwinter Day tradition this finding fuses from; see Phase 6E's own inline correction) |

**Count: 6 Originated, 2 Determined, 1 Inflected.** Ratio Originated:Inflected is 6:1 — under `04` Gate I's
own 3:1 red-flag threshold is exceeded, which per that gate's instruction should trigger a re-run of `01`
§5.1's order of attempts. **Already run, at this gate, and it produced a real result**: the Independence
Day reclassification above. **A second attempt was also made and returned a genuine null**: checked
whether any of the remaining Originated items (Margin Log, Two-Signature Convention, the compact) could be
re-read as Inflected from an established parent form — none can, because none has a Federation-wide or
subnet-wide analogue in existing canon to inflect from. **The skew is real, not a symptom of skipped
research** — Mountain Pass Airport's own Band-1, no-single-founder, thin-parent-culture condition
genuinely produces fewer Inflected opportunities than a city or district would have, and this is stated
here explicitly rather than left for a reader to wonder about.

### Gate P — Parent reconciliation

**Not applicable.** This pass has no children (Frame Declaration: "Children: None"). Stated explicitly
rather than silently skipped.

### Gate G — Generator honesty

- **≥3 independent generators run:** five (G2, G3, G4, G5, G8) — confirmed independent per Phase 1's own
  reasoning (physical, functional, founding-condition, network, and demographic facts are not descended
  from one shared underlying fact).
- **Each run to a full profile before comparison:** confirmed — Phase 1 §A runs all five separately; §B
  builds the comparison table only afterward.
- **Conflicts mined, not smoothed:** the comparison table records agree/conflict/silent per cell; the one
  genuine both-are-true (G8's deficit vs. the structural convergence) is resolved explicitly, not silently
  merged.
- **Nulls recorded as null:** G8's STANDING COST and GRUDGING TOLERANCE cells are explicitly marked
  silent, not papered over.
- **Deficit researched after the profile named it:** confirmed — Phase 1 §F research follows §A-E in
  document order and explicitly targets the deficit §A-E already named.
- **The Unrecognized Instrument run after the profile, not during:** confirmed — Phase 1 §G is the final
  section of the phase, explicitly sequenced last.

**All six checks pass.** The spine was built the way `02` requires.

---

## New REQUESTED items surfaced at Gate 9 and Gate C

Added to the pre-flight's own REQUESTED block (now 6 total, up from 4):

5. **Whether a stranded traveler folded into the closure-season crew (Phase 5d) has an explicit route back
   to their own original plan once the route reopens.** Caught at Gate 9. Blocks: nothing structurally —
   the pass's own findings do not depend on either answer — but it is a genuine, previously unnoticed gap
   in an otherwise-asymmetry-conscious pass. Sensitivity: low; likely resolves in the traveler's favor by
   default (nothing in canon suggests otherwise), but was never stated.
6. **The Sinheung/unnamed-Korean-city Cradle-manufacturer naming tension**, surfaced incidentally at Gate C
   and explicitly not chased (out of scope for this pass). Not blocking anything in this pass.
