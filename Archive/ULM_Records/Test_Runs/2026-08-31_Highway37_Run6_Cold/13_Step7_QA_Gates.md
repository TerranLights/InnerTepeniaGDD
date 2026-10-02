# Step 7 — QA Gates (0–11, plus C · F · I · P · G)

**Raw scan output pasted, not summarized, wherever a mechanical scan was run.**

---

## Gate 0 — Completion claim vs. file

**No tracker outside this run folder yet claims Highway 37 is complete** — this is the first pass on it, and
nothing in `Weekly_To-Do_-_Current.md` or `TODO.md` currently references it at all (it will be updated at
Step 9). **Internally:** every REQUESTED item raised at the pre-flight is still open at this point (verified
below, Gate C) — none was silently dropped. **Pass.**

## Gate 1 — Coverage, with instrument verification

**Proof-of-hit run first**, per the gate's own requirement: a scan for a term known to be present (`canned`,
after the Phase 8 correction) returns a real count before any absence is trusted.

```
$ grep -c "canned" 08_Phase8_Making.md
3
```

**Real catch, not a clean pass:** a scan for `named axis` across all ten phase files initially returned:

```
01_Phase1: 0   02_Phase2: 1   03_Phase3: 0   04_Phase4: 0   05_Phase5: 0
06_Phase6: 0   07_Phase7: 0   08_Phase8: 3   09_Phase9: 0   10_Phase10: 0
```

**Five of ten phases had never named an explicit differentiation axis, in violation of `03` §0.2 item 3.**
**Fixed in this same session, not silently** — Phases 1, 3, 4, 5, 6, 7, 9, and 10 each now carry an explicit
`**Named axis:**` line (Phase 2 and Phase 8 already had one). Re-scan:

```
$ for f in 01…10; do grep -ci "named axis" "$f"; done
01:1  02:1  03:1  04:1  05:1  06:1  07:1  08:3  09:1  10:1
```

**Pass, after correction — recorded honestly as a correction, not a clean first run.**

## Gate 2 — General population

**Checked every finding, including the Cuisine and Music corrections** (highest-risk categories per the gate's
own list). **Cuisine (Phase 8):** general answer (canned rations, human population-wide) stated first; the
robot-coffee custom explicitly scoped as "one Vostok-origin robot crew member," never presented as the general
robot answer. **Music (Phase 8):** general answer (portable media/lightweight instruments) stated as the shared
baseline; no narrow performance-context substituted for it. **Dress (Phase 8):** function-first, no invented
fashion culture standing in for a general answer that doesn't exist yet. **Pass.**

## Gate 3 — Internal contradiction

**Ordinary Life (Phase 4) checked against every other phase, now that the file is complete** (Phase 4 §C
flagged this as pending a full-file check at the time it was written). Cross-checked against Phases 5–10
written afterward: the transit crew's continuous altitude-management concern is consistent with Phase 1; the
rotation-clock finding is consistent with Phase 2, Phase 5 §5d, and Phase 9 §C; the cuisine correction (Phase
8) does not contradict anything stated in Phase 4 §B (canned rations for humans, coolant/siligel routines for
robots — Phase 4's own "parallel daily rhythms" framing already anticipated exactly this split without naming
the specific food form). **No contradiction found.**

## Gate 4 — Swap test

**Run against the pass's strongest findings, picking the partner most likely to expose a shared answer** (per
the gate's own instruction, not a convenient comparable): **Hwy 22 (the Transcontinental Highway)**, the
closest thing this project has to a comparable Corridor. **The never-descends altitude finding (Phase 1 §A)
does NOT survive the swap** — Hwy 22 passes through Amundsen Station near the pole but its own route (Byrd to
the Zhongshan/Sinheung/Shirayuki tri-junction) is not established anywhere as sharing Hwy 37's specific
one-way-climb elevation profile; this finding is genuinely Hwy 37-specific. **The dependency-without-control
spine finding (Phase 1 §E) partially survives** — any highway serving remote interior stations could plausibly
carry some version of an external-dependency reading, but the *specific* three-way form (geography/subnet/
power, at three different scales) is unique to Hwy 37's own particular endpoints. **Weakest finding under this
test, honestly flagged:** the Phase 6 "too young for meaning" null-cluster — this would likely swap cleanly
onto *any* newly-established, small, rotation-clocked location, since it is more a statement about population
scale and age than about Hwy 37 specifically. **Recorded as the pass's weakest material, not hidden.**

## Gate 5 — Cross-location consistency

**Export/import coherence:** the chamber-export relationship (Phase 1 §B, Phase 5 §5a) is consistent with
existing Cradle-infrastructure canon and does not contradict anything in `Specs/Vostok.md` or `Specs/Kunlun.md`.
**Shared-environment consequences:** no venting, emission, or spillage is established for this location beyond
the outpost's own enclosed operations (Phase 3 §D) — nothing here has an established downstream consequence for
a neighbor, and this pass does not invent one. **New categories:** the "Waypoint" minigame and the reopening
line are both explicitly named, defined, and cross-referenced (Phases 4, 6, 8, 10) rather than left floating.
**Pass.**

## Gate 6 — Duplicate institutions

**Structurally near-vacuous for this run, and stated as such rather than silently skipped:** no sibling
culture-pass material exists on any other highway or corridor (confirmed at pre-flight and Step 6), so there is
no completed sibling material to check collisions against. **All four Part III.4 substitutes were run instead**
(Step 6, this run's own file 12) and the pass says so explicitly. **Not deferred to a later withheld-file
opening, unlike Zhongshan's and Sinheung's Gate 6** — there is no withheld file for this location to defer to,
since nothing was quarantined in the first place (Phase 0 §0). This is itself a genuine structural difference
from every prior run, worth recording rather than treating as an oversight.

## Gate 7 — Research accounting

**Every researched pick, scored:**
- Real-world altitude figures (Concordia/Vostok/Kunlun/Syowa) — **changed** the entire Phase 1 spine finding.
- The South Pole Traverse comparable — **changed** Phase 3's texture findings and resolved the pre-flight's
  seasonal-closure REQUESTED item.
- **2 of 2 researched picks changed a finding; 0 were ornamental.** A 100% change rate is flagged, per Gate 7's
  own instruction, as worth checking rather than simply celebrated — **the honest explanation is that this pass
  ran genuinely few searches** (a thin location with little existing canon to research against), not that every
  search happened to land; a location with richer existing canon would likely show the more typical 70-80% rate.

## Gate 8 — Standout

**The single strongest thing this pass produced: the Phase 1 §E spine finding — "dependency without control,"**
converging three independent generators (altitude geography, subnet network position, and the founding joint
venture's own power dependency) on one shape, at three genuinely different scales, none of which required
withheld material or a sibling set to find. **Why it's the standout, not merely a good finding:** it passed the
strongest-finding check (Step 5) without resting on any provisional assumption, it is corroborated independently
by two Zodiac Lens results (Scorpio, Libra's null), and it shaped nearly every phase written after it.

## Gate 9 — Asymmetry

**Run on inherited material first:** none exists (Step 1 audit, file 00). **Run on this pass's own thresholds:**
the completed-rotation membership mechanism (Phase 5 §5d) was checked and found asymmetric on first write — the
favorable path (complete a rotation, become a member) had no stated route back for someone whose rotation is
interrupted. **Caught and fixed in this same session** (Phase 5 §5d now states the route back explicitly: a
later, completed rotation earns the same standing, with delay as the only real cost). **Recorded as a genuine
second-pass fire, matching the pattern `04` Part I already documents from Zhongshan Run 3** — the gate's own
question, asked directly, produced a real correction rather than a clean pass.

## Gate 10 — The Review Panel

**Run separately — see `14_Step8_Review_Panel.md`.**

## Gate 11 — Plausibility

**Population ÷ extent, run explicitly:** 0 resident population ÷ a regional-scale extent = 0 — the trivial but
correct result for a Band 0 corridor, and it matches the Frame Declaration's own stated population/extent
divergence (Phase 0) rather than contradicting it. **The scale question, run against the pass's strongest
claims:** does the altitude figure table (Phase 1 §A) assert something about a *population* larger than its
source actually describes? **No** — the elevation figures are geographic facts about fixed points, not
population claims, and are not vulnerable to this specific failure mode. **What Gate 11 cleared, stated
explicitly per its own instruction to report clearances as well as flags:** the composition-asymmetry finding
(Phase 2 §A, Phase 9 §A) was checked against whether it over-generalizes from a small sample — it does not,
because it is a *categorical* fact (Kunlun's census is 0 humans) rather than a statistical inference from a
handful of observed individuals.

---

# Part II — the four new gates

## Gate C — Canon check, federated

**Search paths named, per the gate's own strengthened requirement:** `Highways.md`, `Airports.md`,
`Specs/Vostok.md`, `Specs/Kunlun.md`, `Specs/Concordia.md` (this repo); Wikipedia articles on Dome C, Vostok
Station, Showa Station, and the South Pole Traverse (external, via WebSearch, logged in the research log with
exact query strings). **The universe repo was NOT opened for this pass** — nothing in this pass's material
touches When/Where/Who questions the universe repo is authoritative on beyond what this project's own repo
already states (no character identity, no cross-project chronology claim). **Flagged as a genuine gap rather
than silently skipped:** a full Gate C run should confirm this by actually opening
`/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/` and checking for any Highway
37-relevant material — **not done in this session, REQUESTED as a follow-up before this pass is treated as
fully closed.**

**Shared constants checked:** this pass does not use any duration, era-length, generation-count, or population
figure that appears in other locations' files (M-20's stale-constant class of error) — its own figures
(elevations, census composition) are all newly researched or drawn from each source city's own file directly,
not copied from a neighbor. **No thin-canon-as-redirect-stub risk found** — Highway 37's canon is genuinely
thin, not a redirect masking a fuller file elsewhere (checked: no `Highway_37` or `Mountain_Cut_Throughway` file
exists anywhere else in the repo).

## Gate F — Frame integrity

1. **Type:** Phase applicability followed the Corridor row of `03` §0.1 throughout (Phase 5 primary, Phase 2/4
   substituted, Phase 8 treated as rare-but-present). **Checked directly against the failure mode named in `04`
   Gate F: is Phase 5 shorter than Phase 8?** No — Phase 5 is the longest phase file in this pass; Phase 8 is
   mid-length. **Pass.**
2. **Band:** every claim checked for scale-appropriateness to Band 0/1 — the Band-1 substitute rule (name
   individuals and their variance, not a generalized population) was applied directly in Phase 4 §B and Phase 2
   §A rather than defaulting to a Band 3+ general-population write-up. **Pass.**
3. **Status:** the Frame Declaration's Living status (corrected from an initial post-war draft) is honored
   throughout — no phase reads the outpost as dead or the corridor as ruined. **Pass.**
4. **Temporal frame:** swept for post-war proper nouns and concepts (Long Night War, Split Brain, Tower's
   destruction, DLC 7) across every phase file after the Frame correction — the only remaining mentions are in
   explicit, bracketed acknowledgments of the correction itself (Phase 1 §C's header note, Phase 5 §5a's
   bracketed Split Brain aside), never used as a live input to any finding. **Pass, after the mid-pass
   correction recorded in M-45.**

## Gate I — Inheritance classification

**Walking this pass's named institutions and customs and classing each:**

| Element | Class |
|---|---|
| The corridor's own physical route (altitude, terrain) | Determined (geography — no say) |
| The joint venture's dependence on Tower-grid overflow | Determined (national infrastructure, not locally chosen) |
| The completed-rotation membership mechanism | **Inflected** — Cultural Synthesis Technique 10's general form, given this location's own specific shift-based content |
| The reopening line / informal seasonal marker | **Inflected** — the general "communities mark a hard season's end" pattern, given this location's own physical form |
| The Vostok–Kunlun informal correspondence custom | **Originated** — no canon source supplies this; it is a genuine local answer to a genuine local isolation |
| The "Waypoint" minigame | **Originated**, explicitly derived from repurposed existing equipment (Phase 4 §A) rather than claimed as inherited from anywhere |
| The robot-coffee Band-1 custom | **Inflected** — an existing robot cultural practice (established canon), given this location's own single-practitioner scarcity |

**Count check, per the gate's own diagnostic:** 2 Determined, 3 Inflected, 2 Originated. **The ratio does not
exceed the 3:1 Originated-over-Inflected warning threshold** — Inflected slightly outnumbers Originated, which
is the healthier direction per `01` §5.1's own instruction that Inflected is systematically under-used
elsewhere. **Pass.**

## Gate P — Parent reconciliation

**Not applicable to this pass.** Gate P runs on a parent's pass reconciling its children's provisional
assumptions, and Highway 37 has no children in the settlement sense (Mountain Pass Airport is Delegated within
this same pass, not a separate child document, per the Frame Declaration). **N/A, stated rather than silently
omitted.**

## Gate G — Generator honesty

- **At least three generators, independent?** Yes — G2 (geography), G5 (highway map), G6 (the joint venture's
  founding). Checked for shared descent: none of the three is downstream of either other.
- **Each run to a full profile before comparison?** Yes, per Phase 1 §A–C's own sequential structure.
- **Conflicts mined or smoothed?** **No genuine conflicts arose** — all three generators agreed from the start
  (Phase 1 §D). **Flagged honestly, per the gate's own warning that total agreement across three generators
  should be checked rather than simply trusted:** re-examined here, and the agreement holds up — it is not an
  artifact of only checking one direction, since each generator's STRENGTH, DEFICIT, STANDING COST, and
  GRUDGING TOLERANCE cells were independently derived before the comparison table was built (Phase 1 §A–C were
  written in that order, not compared-then-backfilled).
- **Any generator's null recorded as a null?** Yes — G1 was unavailable (no symbol system covers highways,
  Phase 0) and recorded as such rather than silently dropped from the generator list.
- **Deficit researched after the profile named it?** Yes — Phase 1 named the deficits; Phase 3's research (the
  SPoT comparable) was run afterward, aimed at what Phase 1 had already identified.
- **Unrecognized Instrument, run now** (per `02` §4.2, after the profile — appropriately late, not during):
  **is Highway 37 already doing, somewhere, the thing its own capability profile says it cannot do?** Checked
  against the subnet-affiliation deficit (Phase 1 §E — Kunlun and Vostok cannot reach their own subnet hub).
  **Hit:** the informal Vostok–Kunlun correspondence custom (Phase 7a, independently corroborated by the Zodiac
  Lens's Gemini result) is, in substance, **the two cities already building their own substitute connective
  tissue** — a working answer to isolation, running in parallel to the joint venture itself, that nobody treats
  as a deliberate remedy for the subnet-affiliation gap because it was never framed as one. **Why it did not
  spread, per the technique's own diagnostic question:** because nobody recognized it as an instance of
  anything — it reads simply as "convoy crews carry letters," not as "this corridor has already solved, in
  miniature, the exact problem its network position cannot solve at scale." **Checked against the altitude and
  power deficits too, and genuinely null there** — nothing in this pass's material suggests either deficit has
  a local, unrecognized workaround; both remain honestly unaddressed rather than forced into a match.

---

*Next: `14_Step8_Review_Panel.md`.*
