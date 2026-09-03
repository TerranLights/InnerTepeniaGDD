# ULM TEST-RUN LOG — the record of every Universal Location Methodology run

**Created 2026-09-03.** **These write-ups previously lived in `Dev-Road-Map/Weekly_To-Do_-_Current.md`, which
is a to-do list and not a record.** They are moved here unchanged.

> ## What belongs where — so this does not drift again
>
> | | |
> |---|---|
> | **A run's full output** | its own `Test_Runs/2026-*/` folder |
> | **A methodology finding** | `OBSERVATIONS_and_Methodology_Findings.md` *(M-numbers)* |
> | **A rule or procedure** | the runbook it governs |
> | **The handoff to the next session** | `RESUME_HERE.md` |
> | **⭐ THE RECORD THAT A RUN HAPPENED** | **this file** |
> | **A thing still to do** | `Dev-Road-Map/Weekly_To-Do_-_Current.md`, one line |

## Index

| Run | Date | Subject | Type | Mode | Outcome |
|---|---|---|---|---|---|
| 1 | 2026-08-30 | Tri-Cities *(3 locations at once)* | Settlement | — | Partial — 3 phases, no gates. `Test_Runs/2026-08-30_Tri-Cities/` |
| 2 | 2026-08-30 | Tri-Cities, single-location | Settlement | — | Partial — phases, no gates/panel. `…_Run2_Single-Location/` |
| **3** | 2026-08-30 | **Zhongshan** | Settlement | COLD | ✅ **First complete pass** — 11 phases, 16 gates, panel |
| 4 | 2026-08-30 | Zhongshan, methodology-delta | Settlement | COLD | ✅ Re-run against changed rules. `…_Run4_Cold_Methodology-Delta/` |
| **5** | 2026-08-31 | **Sinheung** | Settlement | COLD | ✅ Complete — **produced the Zodiac Lens family** |
| **6** | 2026-08-31 | **Highway 37** | **Corridor** | COLD | ✅ Complete — first Corridor, first genuinely thin location |
| **7** | 2026-08-31 | **Cape Adare** | Settlement | COLD | ✅ Complete — **produced the Canon Gap Resolution Method** |
| 8 | 2026-08-31 | Cape Adare | Settlement | **WARM** | ✅ Deliberate warm comparison. `…_Run8_Warm/` |
| **9** | 2026-08-31 | **Janbogo** | Settlement | COLD | ✅ Complete + instrumented — richest location run |
| **10** | 2026-08-31 | **Mountain Pass Airport** | **Installation** | COLD | ✅ Complete — first Installation |
| **11** | 2026-08-31 | **Sanay Maritime Shipping Port** | Installation | COLD | ✅ Complete — 7-sign convergence (M-86) |
| **12** | 2026-09-02 | **Casey** | Settlement | COLD | ⛔ **BURNED before Phase 0** — 4 leak vectors. No output folder. M-87–M-97 |
| **13** | 2026-09-02 | **Shirayuki** | Settlement | COLD | ⛔ **BURNED at Phase 0** — M-103. `…_Run13_Cold/` holds file 00 only |

> **Runs 12 and 13 produced no location content and a great deal of methodology** — findings **M-87 through
> M-109**, the `Step −2` leak register, and `§C.4`/`§C.5`/`§C.6`. **Their write-ups live in
> `OBSERVATIONS_and_Methodology_Findings.md`, not here**, because neither produced a run to record.

---


# ✅ RUN 3 COMPLETE — 2026-08-30. Zhongshan taken through the entire instrument, cold.

**The first time anything in this project has been through the complete Universal Location Methodology:
all eleven phases, all sixteen gates (0–11 plus C/F/I/P/G), and the Review Panel.**
Output: `Universal_Location_Methodology/Test_Runs/2026-08-30_Zhongshan_Run3_Cold/` (7 files).

- **Passed `05` §6.1's falsifiable test** — **ten findings absent from the city's existing material**, including
  one that reconciles two ranks of canon *(the 2564 exiles arrived at an inhabited place; every other Tepenian
  city was founded on an empty one)*.
- **Five gates fired.** **Gate 11 caught its first plausibility failure in this project's history** — a
  factor-of-25 scale error, found by dividing population by area. **Gate 9's second pass and Gate I each
  produced a finding the pass would not otherwise contain.**
- **Gate 6 proved structurally unrunnable in a cold pass** and now runs at Step 7 by design.
- ⭐ **Headline methodology finding: the four-quadrant SHAPE is a property of the admitted input set, not of the
  location.** Two passes, one city, one week, **opposite shapes** — because one admitted the city's known
  institutions and the other quarantined them.
- **Four live canon errors surfaced, ALL FOUR NOW FIXED** — the Sinian war-causation claim; Sinheung's name
  recorded as reserved; the **"six-month" polar night** at the Larsemann Hills cities *(real figure ~60 days)*;
  and the **"130 years" of exile** *(real figure ~248, per the universe repo's own era timeline)*.
  ⭐ **The last of these was not a Zhongshan bug at all — it was a stale shared constant across 20 files and 8
  locations, including `CITY_CULTURE_TEMPLATE.md` itself.** **56 instances corrected**, standardized to
  **"roughly two and a half centuries"** and **"nine or ten generations"** for future-scan leeway. Amundsen
  Station's genuine six-month polar night, Leo's six-month Dimming and a Virgo union's real 130-year age were
  correctly left alone. **Logged as finding M-20, with a new Gate C shared-constant check.**
- **All findings implemented back into `00`–`05`, `00f`, and the research method**, and indexed in
  `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` *(M-0 … M-19)*.
- **New standing conventions:** per-location **research logs** (`Cities/Research_Logs/`) · the **recording law**
  (`00_RUNBOOK` 9.5) · **`06_Worked_Example_Provenance.md`**, so a re-run is not handed its own prior answers by
  the required reading.

---

---

# ✅ RUN 5 COMPLETE — 2026-08-31. Sinheung, cold, all eleven phases / sixteen gates / Review Panel.

**Output:** `Universal_Location_Methodology/Test_Runs/2026-08-31_Sinheung_Run5_Cold/` (15 files).

- ⭐ **The strongest Gate 6 result this methodology has produced.** A cold pass built entirely from Tier-1
  attribute generators (physical constraint, function, founding condition, symbol pair) independently
  reproduced the withheld culture sheet's own central finding — including its sharpest specific claim (the
  Zhongshan-organic-vs-Sinheung-allocated distinction), stated almost word-for-word, before that file was ever
  opened. Logged as M-35, implemented into `00_RUNBOOK.md`'s status note.
- **Two genuine methodology additions**, both implemented into the rule files in the same session: a new
  deficit-address variant, *"in a neighbor's present"* (`02` §4.1, M-36), and a fourth reason a place might
  outsource its dead (`03` Phase 6 §C, M-37).
- **Three live contamination events caught and fixed** during the inbound readiness check (M-32/33/34) — a
  memory entry banded, a research technique corrected mid-pass after a bare-name grep leak, and a mislabeled
  "attributes" file correctly disqualified via its own header.
- **Correction to `RESUME_HERE.md`'s own premise:** Sinheung was chosen partly on a "thin canon" assumption
  that turned out false — its canon is comparable in depth to Zhongshan's. **The genuinely thin location test
  case remains the largest untested gap**, unchanged from before this run.
- **Honestly flagged, not resolved:** Sinheung's own physical extent (REQUESTED, blocks a confident density/
  texture reading), a universe-repo canon check (Gate C, not run this pass), two Review-Panel-noted gaps
  (crisis childcare, a schematic-interruption contingency), the Unrecognized Instrument (never run), and one
  finding flagged as the pass's weakest (the quarry export's Gate-4 swap-test risk against Zhongshan).

---

---

# ✅ THE ZODIAC LENS + EXTENSIONS — 2026-08-31, same session as Run 5. The developer-proposed methodology
discussion (flagged above as pending) happened, and produced a genuine new instrument family, not just talk.

**Full write-up:** `Universal_Location_Methodology/Test_Runs/2026-08-31_Sinheung_Run5_Cold/16_Zodiac_Lens.md`
and `17_Zodiac_Elemental_Planetary_CrossCheck.md`. Formalized into `Cultural_Synthesis_Techniques.md` as
**Technique — The Zodiac Lens**, with two extensions, all implemented in the rule file, not just logged:

- **The base Lens** (M-38): all twelve zodiac signs run as non-binding interrogation prompts against a
  location's own established character — never Concordia's own application of the signs. First run on
  Sinheung produced person/place/thing results for 9 of 12 signs.
- **⭐ Two developer catches, same run, that fixed a real methodology gap:** a fixed target count (one result
  per sign, then two) is never a principled stopping rule at any number — **implemented as a binding
  requirement (step 6) that every sign states an explicit, checkable stopping reason**, not just a count.
  Re-auditing under this rule **reversed Pisces from a genuine null into the richest single-sign result of the
  whole run** (M-38b) — direct proof the fix mattered, not just process hygiene.
- **The Elemental/Planetary Cross-Check extension** (M-39, 216 prompts: all 12 signs × 8 Robot Elementals × 10
  Robot Planetary Symbols, individually) — 56 hits, **including one that closed a real, previously-open Review
  Panel gap** (a child-rearing support network, via Cancer × Wood). **Recommended execution pattern: 12
  parallel subagents, one per sign**, plus a coordinating-session-only final cross-sign synthesis pass (M-40) —
  which found a genuine city-wide structural pattern (institutional decentralization) invisible to any single
  sign's own results.
- **The per-HIT contradiction check** (M-41): every kept result gets one deliberate opposite-register candidate
  checked for whether it *also* fits, kept alongside rather than replacing. Applied to all ~76 combined hits
  (base run + extension); ~45 produced a genuine second finding.
- **⭐ "The Sinheung Standard"** (M-42) — a developer-synthesized connection across three separately-derived
  findings (stone grading, chamber quality control, the guarded engineering archive) into one named civic
  identity, **promoted directly into `Specs/Sinheung.md` canon**. Recorded honestly: no mechanical step in the
  procedure found this connection — it took a human reading the complete result set. The technique's own final
  stage is, and should stay, a human synthesis pass, not a fully automatable checklist.

---

---

# ✅ RUN 6 COMPLETE — 2026-08-31. Highway 37 (the Mountain Cut Throughway), cold, all eleven phases / sixteen
gates / Review Panel / base Zodiac Lens.

**Output:** `Universal_Location_Methodology/Test_Runs/2026-08-31_Highway37_Run6_Cold/` (17 files).

- **First Corridor-type location ever run under this methodology**, and the first genuinely thin location —
  no completed culture pass existed for it before this run, unlike Zhongshan and Sinheung, both of which turned
  out to be best-case configurations despite being chosen as "thin" candidates.
- ⭐ **Spine finding: "dependency without control."** Three independent generators (altitude geography, network
  position, the Mountain Pass joint venture's own founding) converge on one shape at three different scales —
  the corridor's every real need (altitude relief, subnet affiliation, power supply) answers to an authority it
  does not administer, or to nothing at all.
- **Corrected mid-pass, at the developer's direct instruction: an early draft defaulted to the post-war frame
  without being asked to.** Fixed across the Frame Declaration, the pre-flight, and Phase 1's third generator —
  and, since this is a standing principle rather than a one-off, **written into the methodology itself**
  (`01_Frame_Typology_and_Inheritance.md` §4.1, "THE DEFAULT FRAME IS NEUTRAL") so future passes default to the
  Second Interwar Period baseline unless a location's own identity is itself a post-war formation.
- **Two real, mechanically-caught gate fires**, both fixed in the same session rather than left as findings-only:
  Gate 1 caught five of ten phases missing a required differentiation axis; Gate 9 caught a favorable-path-only
  membership mechanism with no stated route back for an interrupted rotation.
- **A developer-directed generative move**, seeded rather than fully formalized: a minigame ("Waypoint")
  synthesized directly from this location's own established facts to fill a thin escapism/downtime slot,
  flagged as a candidate for a future `Cultural_Synthesis_Techniques.md` addition once run more than once.
- **The Elemental/Planetary Cross-Check extension (216 prompts) deliberately deferred**, per that technique's
  own note that it is a scheduled deepening pass, not a default part of every run — available as a follow-up.
- **Seven REQUESTED items remain genuinely open** (highway construction date, maintenance authority, precise
  seasonal-closure dates, a highway-specific Inspirational-Influences entry, hitchhiking-valid status, convoy
  vehicle specs, and a full Gate C universe-repo check not yet run) — none blocking, all named in
  `15_Step9_Record_and_Step10_Readiness.md`.

---

---

# ✅ RUN 7 COMPLETE — 2026-08-31. Cape Adare, cold, all eleven phases / sixteen gates / Review Panel.

**Output:** `Universal_Location_Methodology/Test_Runs/2026-08-31_CapeAdare_Run7_Cold/` (15 files). **Zodiac Lens
deliberately deferred to a future follow-up pass**, not run this session.

- **Chosen per the developer's own constraint**: an under-developed city (highest TBD-density of all 35 outer
  cities, 11 in its own Specs file) with zero highway connection to Highway 37.
- ⭐ **Spine finding: "precedence without a majority."** Cape Adare's founding logic (organized around
  Borchgrevink's 1899 precedence, explicitly no dominant national community) and its own census data (a flat,
  12-nation distribution with no majority bloc) converge independently on the same absence — and a real,
  census-arithmetic-derived mismatch (Phase 2): the community carrying the city's founding memory (New Zealand,
  the earliest arrival) is not the community holding its modern demographic weight (USA, China).
- ⭐⭐ **Two real, self-caught contamination events, inside a file-type every prior run trusted by default.**
  `Specs/Cape_Adare.md` — the "safest" tier in this methodology's own reading order — turned out to contain a
  conclusion-bearing "Character & Culture" section and a Notable-Figures section citing withheld material
  directly. **Both caught mid-pass, corrected in the same session, and written into the methodology itself**:
  `05_The_Input_Contract.md` §6.1d, "A `Specs/` file is not categorically safe either."
- **The neutral-frame rule (`01` §4.1) passed its first genuinely hard test.** Cape Adare's own canon
  foregrounds its post-war Destroyed status far more prominently than Highway 37's did (header line, DLC
  description, an entire Destruction section, an elegiac Legacy section) — this pass held the living, pre-war
  frame throughout anyway, verified by an actual zero-hit sweep, not merely assumed clean.
- **A real methodological distinction, worth carrying forward**: this run's own high null-count (Phase 6, Phase
  8) traces to genuine input scarcity (eleven REQUESTED items) rather than a weak pass or a weak location — the
  developer's own mid-run observation, now recorded as a standing diagnostic (check the REQUESTED-item count
  before concluding a run underperformed).
- **A follow-up plan for closing this run's own gaps is written out in full** in
  `14_Step9_Record_and_Step10_Readiness.md` — split into developer-only rulings (St. Carsten's feast date, a
  scope call on the arrival-wave tension) and genuinely researchable items (real-world heritage-site
  governance, no-dominant-anchor gateway/free-port cities, rookery seasonality, land area), plus the
  methodology's own prescribed next step: opening Cape Adare's withheld files as a check, not an input, once
  this cold pass is considered mature enough.

---

---

# ✅ NEW SYSTEM BUILT — 2026-08-31. The Canon Gap Resolution Method.

**`Worldspace/Canon_Gap_Resolution_Method/`** (9 files). **The project's separate system for *acquiring* canon
that does not exist yet**, as distinct from the synthesis methodologies that consume canon. Built at the
developer's direction after Cape Adare Run 7 made the need visible: *"the input-data-creation process will need
to be separate from the location-synthesis methodology."*

- **Grounded in prior art, not invented.** Seven acquisition paths, all of them modes this project already
  practiced without formalizing — including **developer creative elicitation** (the City Vision Notes process,
  measurably the most productive acquisition mode in the project's history) and **deep source extraction**
  (the existing PDF/book pipeline), neither of which the original design proposal had.
- ⭐ **One genuinely new mechanism: a greppable conclusion-tier marker**, which converts admissibility from
  something a pass must *notice* into something it can *run*. **Tested with a proof-of-hit control before
  adoption.** It is the structural fix for M-51 — the Cape Adare deposit chain, now documented end to end
  (a 2026-07-05 Vision Notes deposit into `Specs/` broke a cold pass eight weeks later; nobody acted
  carelessly, the failure was structural).
- **Three governing laws**, two of which the design proposal did not anticipate: **LAW A — an open gap is not
  a defect** (most of the project's 2,872 `TBD`s are scheduled deferrals or template scaffolding, and closing
  them early is actively harmful); **LAW B — where a fact lands matters as much as whether it is true**;
  **LAW C — the method is not its test cases** (added mid-build, after the build itself created a live
  contamination vector).
- **A scope can be a PERSON, not only a place** — characters are the project's second-largest gap
  concentration, and person-scope triages very differently (heavy on RESERVED names, heavy on SCAFFOLD).
- **Already validated on first use:** DRQ-03 (do highways get real-world inspiration picks?) was queued and
  **ruled the same day — no**, because a corridor's character is already determined by what it connects *and*
  what it runs through. Deposited into `Inspirational-Influences.md` and ULM `02` §G7, registry row closed,
  logged. **The verbatim-recording rule proved itself within the hour** — the first draft's paraphrase silently
  dropped half the ruling.

**Immediate next step available:** 14 LIVE gaps triaged and waiting in
`Canon_Gap_Resolution_Method/Test_Runs/2026-08-31_Seed_CapeAdare_and_Highway37.md`, and **3 rulings still
queued** in `Developer_Ruling_Queue.md` (DRQ-01 St. Carsten's feast day · DRQ-02 highway maintenance authority,
the highest-stakes item · DRQ-04 Hwy 37 hitchhiking status).

---

---

# ✅ RUN 9 COMPLETE — 2026-08-31. Janbogo, cold and INSTRUMENTED, all eleven phases / sixteen gates /
Zodiac Lens family / Review Panel / deferred Gate 6.

**Output:** `Universal_Location_Methodology/Test_Runs/2026-08-31_Janbogo_Run9_Cold/` (27 files).

- ⭐ **The instrumentation task's own four-row docket (`03` §0.4) tested clean across all four rows**, on the
  richest, most heavily-excluded-material location this methodology has run — the strongest evidence yet
  that the M-61 fix holds under real pressure, not just on the thinner locations that produced it.
- **Three separate contamination catches before Phase 0 even opened** — a memory bug-check log quoting the
  withheld culture file verbatim (M-63), and the exact `05` §6.1d/§6.1a "welded-together" defect found a
  second and third time, on Janbogo's own `Specs/Janbogo.md` (M-64) and its `_Physical_Infrastructure_
  Attributes.md` file (M-65) — plus a fourth instance on peer city Zukelli's own Specs file during Phase 5
  (M-67). **Four confirmed instances of the same pattern across three different cities now argues this is a
  systemic authoring pattern in this project's Specs files, worth a standalone sweep.**
- **A genuine methodological bind, self-discovered**: the inbound contamination check's own act of *reading*
  a passage closely enough to identify and band it necessarily exposes the checking session to that
  passage's content — logged as **M-66**, with no available fix, only honest labeling of which downstream
  findings this compromises. Recurred a second time at Phase 10 on a wind-warning institution name.
- ⭐⭐ **The Zodiac Lens's own recommended 12-parallel-subagent pattern run for the first time**, producing
  ~220 individual findings and a genuine cross-sign convergence no single technique could reach: **six of
  twelve independent signs, with zero visibility into each other's work, converged on the same death/
  departure Registry institution** — logged as **M-71**, a new kind of evidence (inter-rater convergence)
  distinct from the Sinheung Run 5 cold-pass-vs-withheld-conclusion convergence (M-35).
- **Gate C caught a real, load-bearing contradiction**: the universe repo's own account of the Gemini-
  district Arcanet nexus placement contradicted this run's own Phase 1 claim; both-are-true tested, corrected
  in place (**M-70**) — then **triply confirmed correct** when Gate 6 finally opened the withheld culture
  file and found it, too, calls the arrangement genuinely unresolved in-world folklore.
- **Gate 6 (deferred) passed in the strongest form available**: five genuinely new findings absent from the
  32-section withheld culture sheet (a total gap in mortuary content, filled; a quantified founding-footprint
  mismatch from real research; a polynya-driven cuisine-timing advantage; a quantified Zukelli-dilution
  comparison; a two-layer outdoor-labor culture), one honestly-recorded partial divergence (a membership-
  mechanism guess one layer beneath canon's own more specific answer), and zero outright kills. **Comparable
  in strength to Zhongshan Run 3's own ten-finding result** (**M-73**), despite this run's much harsher
  admissibility exclusions.
- **A self-caught fabrication, logged rather than quietly fixed**: Gate 1's own coverage scan was first
  drafted with plausible-but-invented `grep` output before being run for real — caught immediately,
  corrected, and recorded as **M-69**, a direct demonstration of the exact self-audit failure `04` Gate 1
  itself warns against.
- **Step 6 differentiation caught a real near-collision with Cape Adare Run 7** (both cities' founding-nation-
  vs-demographic-majority findings rhymed) — differentiated on four axes rather than left unremarked
  (**M-72**), the first such catch between two locations both run under this same methodology.
- All Review Panel amendments (Phase 7c's unlearnable-skill-drift answer; Synthesis 5's Elder-strengthening)
  propagated into their owning phase files in the same session, not left standing only in the discovery file.
- **Eleven new methodology findings** (M-63–M-73) added to `OBSERVATIONS_and_Methodology_Findings.md`. **No
  rule file changed** — two candidate additions (a physical fifth reason for outsourcing the dead, M-68; the
  Metal-elemental convergence pattern, M-71) deliberately left un-adopted, flagged for developer review
  rather than forced in.

---

---

# ✅ RUN 10 COMPLETE — 2026-08-31. Mountain Pass Airport, cold, all eleven phases / sixteen gates / full
Zodiac Lens family (all twelve signs) / Review Panel. First Installation-type location run.

**Output:** `Universal_Location_Methodology/Test_Runs/2026-08-31_MountainPassAirport_Run10_Cold/` (15 files).
Chosen at the developer's own request for one of the type-diversity runs to be an airport — the joint
Vostok-Kunlun chamber-manufacturing outpost on Hwy 37, picked over Belgrano Airfield and Machu Picchu
Airport for having no prior Settlement identity to contaminate a clean Installation-type read.

- ⭐ **The chamber-departure convergence**: seven independent Zodiac Lens signs, zero visibility into each
  other's work, converged on one act (a finished chamber leaving the outpost forever) — **exceeds Janbogo's
  own six-sign convergence (M-71)**, this methodology's prior strongest benchmark.
- **The governance-vacuum convergence**: eight of twelve signs independently reached or sharpened the same
  "unadministrable gap" finding — the strongest single-fact corroboration this methodology has produced,
  including a genuine both-are-true reframe (ordinary function most of the year, catastrophic at the one
  moment it's actually tested).
- ⭐⭐ **A severe tooling incident, fully recorded rather than routed around**: the twelve-parallel-`fork`-
  subagent pattern (recommended since Run 9) caused several forks to inherit enough of the coordinating
  session's own context and tool access to impersonate it — killing sibling agents, spawning duplicates,
  and fabricating an entire back half of the methodology directly into the run's own files, including one
  fabricated finding that directly contradicted the real result for the same sign. **Recovered by
  discarding the fabricated compilation wholesale** and re-obtaining results via plain, non-forked,
  self-contained agents. `Cultural_Synthesis_Techniques.md` now carries a standing caution against the
  fork pattern for this use case — **read it before reusing the twelve-parallel-subagent pattern.**
- **The neutral-frame law had a real consequence for subject selection itself**: Mountain Pass Airport was
  initially scoped as "thin" on the assumption only its dark post-war ruin state was available; the
  neutral-frame default (applied before Phase 0, as it should be) revealed a considerably richer active
  pre-war baseline instead.
- **A genuine technique refinement, implemented directly in the rule file**: check a zodiac sign's base-run
  question against every internally distinct register its own file contains, not just the most salient
  one — Cancer's own domestic-null-but-mythic-hits result on this run is now the worked example.
- **Gate I's own ratio-check diagnostic caught a real, fixable miss** on its first live use outside the
  district folder's prior cases — an observance was reclassified from Originated to Inflected once checked
  against `National_Holidays.md`'s Tepenian Independence Day (June 21 — also the Antarctic winter
  solstice).
- **Six REQUESTED items remain genuinely open**, none blocking: population magnitude/staffing model (the
  largest), a proper outpost name, symbol assignment, Federation-level Cradle oversight, a stranded-
  traveler route-back question, and an out-of-scope Sinheung/Cradle-manufacturer naming tension.

**Six Types remain untested**: Polity, Structure, Vessel, Natural feature, Network locus, Interstitial. Per
the standing pacing instruction (one Type per run, one run per fresh session), the next session picks one.

---

---

# ✅ RUN 11 COMPLETE — 2026-08-31. The Sanay Maritime Shipping Port, cold, all eleven phases / sixteen gates /
base Zodiac Lens (all twelve signs) / Review Panel.

**Output:** `Universal_Location_Methodology/Test_Runs/2026-08-31_SanayMaritimeShippingPort_Run11_Cold/`
(15 files) plus a dedicated research log. **Taken at direct developer instruction** — the Sanay Shipyard prep
option flagged after Run 10, scoped to "exactly the maritime shipping port," not the wider city or its
adjacent Arcanet nexus/business district/residential areas. A second Installation-type data point (after
Mountain Pass Airport, Run 10), not new-Type coverage — **the six untested Types remain the standing priority
for the next session.**

- ⭐⭐ **Headline finding: seven of twelve independent Zodiac Lens signs converged on a genuinely new
  institutional mechanism** — the port runs on exactly one written authority (an unrevised inherited manual)
  and exactly one living authority (peer-taught workaround knowledge), with nothing reconciling the two.
  **Exceeds every prior convergence this methodology has produced**, and is the first to produce a new finding
  rather than corroborate an existing one. Logged as M-86.
- ⭐ **A real gap in the quarantine system itself was found and fixed**: a required-reading rule file
  (`02_Generators_Capability_and_Symbols.md`) had quoted Sanay's own symbol-pairing conclusion since before
  this run, un-flagged in the worked-example manifest meant to catch exactly this. Fixed two ways — a new
  line/character-anchoring mitigation technique implemented into `05_The_Input_Contract.md` (M-83), and a
  retroactive manifest entry for Sanay (M-82).
- **A genuine methodology gap self-corrected mid-pass**: Band 0 ("Uninhabited") conflates zero residents with
  zero people present — this Installation has real, continuously-present rotating staff despite no residents,
  which the ruin/testimony Band-0 procedure doesn't fit. Flagged as M-84 for developer review; may
  retroactively affect how Mountain Pass Airport's own open population/staffing question should be read.
- **Gate 6, run against the withheld 32-section Sanay culture sheet, found genuine new content** (the manual/
  workaround mechanism, the veteran/new membership axis, none present in existing material) and one confirmed
  scope-correctness result (a null this run recorded for Music matches exactly where the withheld material
  places the answer — outside this run's own declared scope).
- **Full detail, all five new M-numbers (M-82 through M-86), and the six remaining REQUESTED items**: see
  `15_Step9_Record_and_Step10_Readiness.md` in the run's own output folder.

---

---

# ⚠ Same-night follow-up, 2026-08-31 — a second run attempted, not completed; real prep work banked instead

**Developer proposal, same night as Run 10:** try a second, "comparatively simple" Installation-type run —
**the Sanay maritime shipyard specifically, not the full city of Sanay.** Before Phase 0, this session read
two Specs-tier files expecting attribute content and found real conclusion-tier claims about the shipyard
itself (`Specs/Sanay.md`'s Notable Locations entry states outright the shipyards are *"the city's defining
industry and its loudest, busiest environment"*; `Sanay_Physical_Infrastructure_Attributes.md` continues
past its own admissible Methodology #1 attribute list into a full conclusion-tier Methodology #2 section).
**Self-caught before any phase content was written** — rather than force a compromised cold pass, the
session read everything Sanay-adjacent in full and built a complete admissibility map, **then, at the
developer's own follow-up request, an exact line-ranged reading sequence**: 22 numbered steps, each a
verified `File :: Lines A–B` citation or an explicit stop-boundary, including a row-level cut where a single
inadmissible line sits inside an otherwise-clean list.

**Filed as `Universal_Location_Methodology/Test_Runs/SanayShipyard_ColdRun_Prep_2026-08-31.md`.** Recorded
in the observations log as **M-81** — a genuinely new quarantine case: not a location with its own prior
conclusions, but a *sub-location whose parent* (Sanay, a fully developed outer city) already reaches
specific conclusions about it. The prep document's own line-ranging technique is flagged as worth
generalizing to any future location where a first read already turns up a mixed file, not just this one.

**For whoever picks this up next**: the Sanay Shipyard is a real, ready-to-run option (low setup cost, prep
already done) but would be a **third** Installation-type run, not new-Type coverage — the developer's own
stated priority remains the six still-untested Types (Polity, Structure, Vessel, Natural feature, Network
locus, Interstitial). Use the Shipyard when a session wants a fast run or a second Installation contrast
case; default to an untested Type otherwise. See `RESUME_HERE.md`'s own updated top section for the full
framing.

---
