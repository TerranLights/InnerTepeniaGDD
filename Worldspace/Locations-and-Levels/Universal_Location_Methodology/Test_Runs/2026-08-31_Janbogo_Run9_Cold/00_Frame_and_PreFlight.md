# Run 9 — Janbogo, Cold and Instrumented — Phase 0: Frame and Pre-Flight

**Run started 2026-08-31. Fresh session, cold on Janbogo per `RESUME_HERE.md`'s own requirement.** Subject
locked by the developer: Janbogo, no substitutions (`RESUME_HERE.md` §2). This file is Step 0 (Frame),
the `05` §7 pre-flight, and the inbound half of `00_RUNBOOK.md` Step 10 — all three run before any phase
content is written, per the exact task order in `RESUME_HERE.md` §5.

---

## 0. Inbound readiness check (`00_RUNBOOK.md` §10.1, `RESUME_HERE.md` §3a/§4) — run FIRST, on myself

1. **Auto-loaded memory scanned for "Janbogo" and adjacent names** (Zukelli, Janbogo Subnet). 91 files hit;
   the overwhelming majority attribute-only (foothold-city mentions, shipping-tonnage comparisons). **Two
   un-banded, conclusion-bearing entries found and banded before reading anything else**:
   `project_janbogo_bug_check_resolved.md` (quoted Local_Cultures prose verbatim) and
   `project_zukelli_janbogo_destruction_resolved.md` (interpretive "deliberate, permanent point of the
   message" framing). Logged as **M-63**.
2. **`06_Worked_Example_Provenance.md` checked** — zero hits for "janbogo." No manifested worked example in
   `00`–`05`/`00f` carries Janbogo's own answers. Clean.
3. **Headers of admissible-tier files checked for cited sources, per §10.1 item 4** — this caught two further
   violations before they could contaminate anything: `Specs/Janbogo.md`'s "Character & Culture" section
   (cites `Local_Cultures/Janbogo_Subnet/Janbogo.md` directly; logged **M-64**) and the entirety of
   `Janbogo_Physical_Infrastructure_Attributes.md` (its own header cites the same withheld file as a source,
   per `05` §6.1a rule 4; logged **M-65**). Both excluded — see §2 below for exactly what remains admissible.
4. **Registry paths confirmed to exist**: `Specs/Janbogo.md`, `Local_Cultures/Janbogo_Subnet/Janbogo.md`
   (withheld, confirmed present, not opened), `City_Symbol_Assignments.md` (Janbogo row present),
   `Official_Population_Census.md` (referenced by Specs, not yet independently opened),
   `City_Megasheets/Janbogo_Subnet/Janbogo/` (Megasheet + Ultra_Megasheet folders present, per memory —
   inadmissible, culture-pass conclusions, not opened). **No `Cities/Research_Logs/Janbogo_Research_Log.md`
   exists yet** — confirmed absent, will be created per `05` Step F / `00_RUNBOOK.md` §3.7 as research
   happens.
5. **Output folder confirmed not pre-existing** before creation (`00_RUNBOOK.md` §10.2 item 7) —
   `Test_Runs/2026-08-31_Janbogo_Run9_Cold/` did not exist prior to this run.
6. **Corpus-wide retrieval flagged unusable per quarantine**: this repo's `graphify` hook fires on every
   `Read`/`Grep`/`Bash` call. **A graph query naming "Janbogo" would return culture-pass extracts** —
   navigation for this run is by `find`/`ls`/direct path only, never by `graphify query "Janbogo..."`. This
   is a deliberate, declared violation of the repo's own tooling convention, per `RESUME_HERE.md` §3c — the
   circularity rule outranks the search convention for this run specifically.

**This is the strongest inbound check this methodology has produced on a single subject: three separate
admissibility violations (M-63/64/65) caught before Phase 0 even opened**, across three different file
types (memory, `Specs/`, `_Physical_Infrastructure_Attributes.md`). Recorded as its own observation
(M-65's own closing note) rather than treated as routine.

---

## 1. Frame Declaration

```
## Frame Declaration

**Location:**        Janbogo
**Type:**             Settlement (no modifiers carried into this pass — see Temporal frame below;
                      "Damaged" is a post-war property, out of the declared frame)
**Population band:** 4 — Urban (~50,000–1M). Census II combined = 957,570.
**Extent band:**      UNKNOWN — no stated land area found in any admissible file.
                      **REQUESTED** (see §3). Blocks a confident Gate 11 density check at Phase 0
                      itself; flagged now rather than discovered late, per the Sinheung Run 5 precedent
                      (its own extent was likewise REQUESTED and never supplied).
**Status:**           Living. NOT Declining — the Census I→II drop (1,310,511 → 957,570, −27.0%) is the
                      project-wide, canon-documented orbital-emigration pattern (`RESUME_HERE.md` §6 trap
                      2: "Census I and II are BOTH pre-war... orbital emigration, not war loss"), not war
                      damage and not a symptom of a shrinking, straining population. Per `01` §3's standing
                      note, migration to a documented destination is not Declining.
**Temporal frame:**  ⚠ **Second Interwar Period (2564–2812 GDD), the neutral pre-war baseline — DECLARED,
                      not inferred, and DELIBERATELY CHOSEN over the post-war present.** Per `01` §4.1's
                      binding default ("THE DEFAULT FRAME IS NEUTRAL"): Janbogo's own identity is not a
                      post-war formation — it was founded shortly after the Falkland Treaty (2564) on
                      existing real-world-derived infrastructure, and its defining civic material (the
                      teahouse tradition, communal-warmth culture, the katabatic-wind/polynya relationship,
                      Hwy 183, the Gemini-district diaspora) all predates and does not depend on the war.
                      Unlike Concordia's districts, nothing about Janbogo's own character requires the
                      post-war frame to make sense.
                      **What this EXCLUDES from this pass, explicitly, per `01` §4.1 rule 2**: the Long
                      Night War strike on Zukelli and Janbogo's role as its intended surviving witness; the
                      "damaged, partially operational" status; any framing of Hwy 183 or the Gemini diaspora
                      as compensating for a "strained" post-war Concordia; Majyao's relocation to Concordia
                      (an event `Specs/Janbogo.md` places "before or during the Long Night War" — ambiguous
                      as to which side of the frame it sits on, and therefore NOT used to ground any finding
                      in this pass; recorded as a REQUESTED clarification, §3). **These are legitimate
                      subjects for a SEPARATE post-war pass on Janbogo**, built on top of this one, per `01`
                      §4 rule 3 — not folded in here.
                      **Epistemic horizon for this pass**: residents know the war has not happened. Nobody
                      here has any concept of a "strategic external link to Concordia" being uniquely
                      critical because everything else got destroyed — Janbogo in this frame is simply one
                      of several functioning coastal supply points, not the last one.
**Parent:**           The Tepenian Federation (Band 6, unwritten). Provisional assumptions below.
**Children:**         None — no named sub-locations within Janbogo exist in any admissible source.
**Sibling set:**      The Janbogo Subnet's other cities — Fort McMurdo, Scott, Zukelli, Dumont d'Urville,
                      Denison, **Cape Adare** (already run complete under this exact methodology, Run 7 —
                      a genuine completed sibling, usable for Phase 5/Gate 6 differentiation, distinct from
                      Janbogo's own withheld culture-pass conclusions). Also the wider 35-outer-city set for
                      `04` Part III's large-set differentiation mode.
**Written:**          ALONE (default).
**Configuration:**   **EXCEPTIONAL, and the exceptionality is about SELECTION, not about Janbogo's own
                      kind of place.** Janbogo was deliberately chosen as the richest never-run location
                      specifically to stress-test whether the methodology's phase ORDERING holds when many
                      phases fire with real content simultaneously (`RESUME_HERE.md` §1, §2) — this is the
                      opposite selection logic from every prior run (Zhongshan, Sinheung, Highway 37, Cape
                      Adare were all chosen for thinness). **Findings that depend on this**: the entire
                      instrumentation task (`NN_Ordering_Collision_Log.md`) only produces evidence because
                      this location is rich enough for close-order collisions to actually occur (`RESUME_
                      HERE.md` §2b's own reasoning — "collisions only occur where a later phase has enough
                      material for an earlier check to collide with"). **As a Settlement/Band 4/subnet-hub
                      port city on its own terms, Janbogo is otherwise TYPICAL for its type** — nothing
                      about being a port-and-supply hub, a Korean-founded city, or a subnet capital is
                      itself an unusual configuration among the 35 outer cities.

**Provisional assumptions about the parent (Tepenian Federation, unwritten):**
1. Currency, calendar, and language-family policy are Federation-determined, per standing project canon
   (energy-backed currency → regional currency + trade standard, per `[[project_national_currency_history]]`
   memory) — Janbogo does not originate any of these.
2. The Federation's own relationship to a coastal supply/port city of Janbogo's kind is assumed ordinary
   (no special provisional status), since no canon suggests otherwise for the neutral pre-war frame.
3. Per `01` §5.2 rule 3, no finding in this pass is built as depending on an unwritten-parent assumption
   where a physical-constraint alternative exists — physical constraint (G2) is preferred as the spine
   wherever the choice arises.

**Generators available:** G1 (symbol pair) · G2 (physical/environmental) · G3 (function/purpose) ·
G4 (founding condition) · G5 (network position) · G6 (defining event) · G7 (real-world inspiration,
designation known, research not yet run) · G8 (demographic composition + census change)
**Generators selected for the spine (≥3, independence-checked):**
- **G2 — Physical & environmental constraint.** Rich, near-universal, primary per `02` §2. Katabatic wind,
  Terra Nova Bay polynya, full monthly climate table — all confirmed admissible (Specs Geographic
  Basis/Annual Climate, clean of the M-64/M-65 exclusions).
- **G4 — Founding condition.** Post-Falkland-Treaty (2564) Korean exile settlement built on existing
  real Jang Bogo Station infrastructure, not founded from nothing — genuinely independent of G2 (a fact
  about who/why/with-what, not about terrain).
- **G5 — Network position.** Hwy 183 connector status (non-main-line but most heavily used), coastal port
  position, Janbogo Subnet hub, Arcanet nexus physically sited in Concordia's Gemini district rather than
  Janbogo itself — independent of G2/G4 (a fact about connectivity, not terrain or founding).
- **G8 — Demographic composition + census change.** Full per-nation Census I/II breakdown; retention =
  957,570/1,310,511 = **73.0%** (to be scored as a z-score against the full 35-city set once that set is
  assembled — deferred to Phase 1/Step 2 per `02` G8's own third technique). Independent of the other three
  (a fact about population, not terrain, founding, or connectivity).
- **G1 (symbol pair) run as a PAIRED generator per `02` §6.3**, supplementary to the four above, not counted
  toward the independence-of-three requirement since it is thin-thin and derives its structure from the
  pairing relation rather than standing alone. Earth (planet) + Air (element) — see §4 below.
**Deliberately NOT selected for the spine under this frame**: G6 (Defining event) — the only clearly
canon-supplied defining event (the Long Night War strike) is explicitly post-frame and excluded per the
Temporal frame declaration above. The Census I→II orbital-emigration wave is a candidate G6 substitute and
will be evaluated at Phase 1 rather than pre-selected here, since its status as a genuine "event" for
*Janbogo specifically* (versus a Tepenia-wide background pattern true of every city) is not yet clear.

**Reserved decisions this pass must not foreclose:**
- Whether Majyao's relocation to Concordia occurred before or during the war (Specs states both are
  possible) — genuinely ambiguous in the source, not decided here, recorded as REQUESTED.
- Which `Course_of_Events/` narrative variants for Janbogo (or any city) are ratified canon — developer
  has explicitly stated this is undecided project-wide (`RESUME_HERE.md`, blocking note). Janbogo's own
  Course_of_Events folder (if it exists) is DEMOTED per `05` §6.3, readable as a prompt only, never as
  grounding for a finding.
- Any question requiring the post-war frame (governance of "damaged" Janbogo, current population, whether
  the Gemini diaspora still exists in its pre-war form) — out of scope for this pass entirely, not merely
  deferred.
```

---

## 2. What is actually admissible, after M-63/64/65 — the Step 0.4 triage, applied

Per `00_RUNBOOK.md` §0.4's reading order (specs → symbols → census → founding → physical facts → culture
files never):

| Source | Admissible content | Excluded content |
|---|---|---|
| `Specs/Janbogo.md` | Population & Composition (full census tables) · Geographic Basis + full Annual Climate/Monthly Summary/Notable Weather Phenomena (G2) · Founding — **first two paragraphs only** (settled date, founding population/mechanism) · Economy & Industry (pre-war-compatible reading: port position, inter-city trade node — the "since the war, narrowed to..." sentence excluded as post-frame) · Notable Locations/Figures, read as Tier 3 *particulars* per `05` §2.4, never as conclusions · Highway access paragraph (Hwy 183, G5) | **"Character & Culture" section in full** (M-64) · **Founding's third paragraph** (civic-culture-development sentence, M-64) · Connection to Concordia's "already-strained" framing and the whole post-war Legacy/Current-Status/Destruction sections (out of frame, not merely inadmissible) |
| `Janbogo_Physical_Infrastructure_Attributes.md` | **NONE — entire file excluded** (M-65) | Everything |
| `City_Symbol_Assignments.md`, Janbogo row | The two assigned members only: **Earth** (planet), **Air** (element) | The rationale column ("sister city with Zukelli," "fused synthesized fashion identity") — a capability verdict per `05` §6.1c, not usable |
| `Planetary_Symbols.md` / `Robot_Elementals.md` | Earth's and Air's own registered terms, read from file (quoted in §4 below) | — |
| `Official_Population_Census.md` | Not yet independently opened — Specs already carries Janbogo's own rows; will open directly for the full 35-city set when G8's z-score scoring runs at Phase 1 | — |
| `Local_Cultures/Janbogo_Subnet/Janbogo.md` | **WITHHELD — not opened.** This run's comparison target, per `05` §6.1, opened only at the deferred Gate 6 (Step 7). | Everything |
| `Course_of_Events/` (if present for Janbogo) | Not yet located/checked — will be triaged per `05` §6.3 (DEMOTED by default, per the corpus-wide unratified-status finding) before any use | — |
| Memory (`project_janbogo_*`, `project_zukelli_janbogo_*`) | Attribute-only content in the now-banded files (M-63) — dates, the ~8km distance figure, the Italy/Zukelli mix-up correction history | The banded conclusion passages themselves |

---

## 3. Input Contract Check (`05` §7)

```
**Tier 0 (blocking):**
- Existence & designation:        present
- Position in the world:          present (Terra Nova Bay, Ross Sea coast, ~74°37'S 164°13'E)
- Population magnitude (→ band):  present (Band 4, Census II combined 957,570)
- Parent:                         explicitly present but unwritten (Tepenian Federation, Band 6)

**Tier 0b (strongly recommended, not blocking):**
- Temporal frame:                 GIVEN — Second Interwar Period, neutral baseline, declared explicitly
                                   per `01` §4.1 (see Frame Declaration above), not inferred.
- Epistemic horizon:              residents have no knowledge of the Long Night War, the Zukelli strike,
                                   or Janbogo's eventual post-war role as "the last coastal supply link."

**Tier 1 (need ≥3):** G2 (physical), G4 (founding), G5 (network), G8 (composition) all present → count: 4.
G1 (symbol pair) present, supplementary. G7 designation present (Jang Bogo Station), research not yet run.
G6 deliberately not selected — see Frame Declaration.

**Tier 2 (enriching):** Present: existing scattered canon (Specs is substantial), parent's determined
properties (standard Federation canon), sibling set (Janbogo Subnet cities, esp. Cape Adare Run 7 complete),
Inspirational-influence pick (Jang Bogo Station named, not yet researched). ABSENT: physical/spatial layout
or map; adjacent locations' completed passes beyond Cape Adare.

**Tier 3 (optional particulars):**
- Known residents: Majyao Bisyugota (teahouse keeper, pull for TBN Pink Lucy is the reverse case —
  she came FROM Janbogo originally per prior canon, actually check: Pink Lucy came TO Janbogo from Dumont
  d'Urville — a PULL case), Meteorologist Han Soo-jin (placeholder), Architect Wu Lian-Marchetti (placeholder)
  — all to be interrogated per `05` §2.4's procedure at Phase 10, not merely rostered.
- Known objects: none specifically named yet beyond the split-token-style institutions implied by Notable
  Locations.
- Known buildings/landmarks: Majyao's (Original) Teahouse — site only, current state TBD in-frame since
  it predates any war-damage question entirely.
- Known "firsts/onlys/lasts": Terra Nova Bay's polynya as the only year-round ice-free Ross Sea access point
  — flagged for hard interrogation per `05` §2.4's special-case rule.
- Known notable absence: no stated land area (see Extent band, above) — itself a REQUESTED item.
- *Evidence-tier and changed/ornamented labeling deferred to Phase 10, per the procedure.*

**Type-specific (Settlement):** no additional requirements beyond the standard set.

**Ratification check (§6.3):**
- Files whose header/filename declares them suggestion/proposal/draft/tentative: **`Janbogo_Course_of_
  Events_Suggestions.md` and any numbered `Course_of_Events/` variants, if they exist for Janbogo** — not
  yet independently located; will be checked before Phase 6 (Meaning) at the latest, since that phase is
  the likeliest to reach for narrative material. Assumed DEMOTED by default per the corpus-wide finding
  until checked.
- DEMOTED: as above, pending confirmation.
- Findings resting only on unratified material: none yet — no phase content written.

**Reserved decisions in force for this pass:** see Frame Declaration §1 above (Majyao's relocation timing;
Course_of_Events ratification; anything requiring the post-war frame).

**Scope & configuration:**
- Written:            ALONE
- Configuration:      EXCEPTIONAL (selection-driven, not type-driven — see Frame Declaration)
- Sibling set:         present (Janbogo Subnet + Cape Adare Run 7 + full 35-city set for large-set mode)

**Provenance check:**
- Any input derived from this location's own prior output?              no (this is Janbogo's first pass
                                                                          under this methodology)
- Any input that is a prior culture-pass CONCLUSION about this place?    yes, found and excluded — see §2
                                                                          (M-63/64/65)
- Canon read in the Step 0.4 triage order, culture files last?           yes — specs → symbols → census
                                                                          (via specs) → founding → physical
                                                                          facts; culture file NOT opened.

**Sources that state their own limits:** `Specs/Janbogo.md`'s de-stacked per-nation table explicitly notes
its percentages are "of this city's own population... not Tepenia-wide" and that robot figures apply
human-population proportions rather than being independently sourced — respected, not read past.

**Verdict:** PROCEED. Spine generators (4, independence-checked) exceed the minimum of 3. Extent band is
the one genuine REQUESTED gap and will be carried forward rather than blocking — Phase 1's G2/G8 work can
proceed on population alone, with the density check (Gate 11) flagged as degraded until/unless extent is
supplied.
```

---

## 4. Symbol pairing — read from file, not from name (`02` §6.0)

**Earth** (planet): One word *Oasis*. Positive: "viability built from convergence, not from any one
advantage... resilience that comes from redundancy — several different systems each capable of covering
for the others." Negative: "a stability entirely contingent on everything continuing to line up at once...
it simply hasn't failed yet."

**Air** (element): Positive: "the invisible connective medium that carries a voice, a signal, a scent, or a
warning from one place to another without either end needing to touch the other directly... the atmosphere
that quietly makes every other kind of contact between two separated things possible at all." Negative:
"scattered restlessness... a connection so diffuse it commits to nothing... the same invisibility that lets
Air carry a signal also lets it carry nothing at all, with no way to tell the difference from the outside."

**Pairing relation (`02` §6.3), provisional — to be confirmed against the actual capability profile at
Phase 1, not finalized here.** Candidate reading: **Tensioned, leaning Ironic.** Earth's whole promise is
redundant convergence — multiple independent systems backing each other up so no single failure is fatal.
Air is the connective medium between separated things — but Air's own negative pole is a connection so
diffuse nothing is actually guaranteed to arrive. If Janbogo's real civic mechanism turns out to be "many
independent systems, connected by something that cannot itself confirm delivery," that is Earth's strength
undercut by exactly the medium meant to link its redundant parts — the Ironic subtype, where the second
symbol makes the first's characteristic strength fail in a specific, nameable way. **Flagged as a hypothesis
to test against the actual Phase 1 generator run, not asserted as a finding here** — Phase 0 does not
produce location content, per `03`'s own governing rule for this phase.

---

## Status at end of Phase 0

**Complete**: inbound readiness check, Frame Declaration, Input Contract pre-flight, symbol read.
**Three real findings produced before any location content was written** (M-63/64/65) — recorded in
`OBSERVATIONS_and_Methodology_Findings.md`, not merely noted here.
**Open**: Extent band (REQUESTED), G7 research (not yet run, correctly deferred per `02` Step 2 — "do not
research yet"), Course_of_Events ratification status for Janbogo specifically (not yet checked).
**Next**: Step 1 (asymmetry audit on inherited material — minimal here, since the admissible material is
mostly raw attribute, not prior findings) and Step 2 (build the spine — Phase 1, the four selected
generators run to full four-quadrant profiles, separately, before comparing).
