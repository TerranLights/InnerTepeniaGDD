# Local-City Robot Culture — DRAFT Methodology (Input Categories & Approach)

**Status: rudimentary draft, now including a first full step-by-step process.** This file covers both an
inventory of what already exists to build on (Input Categories A–E) and a proposed 6-step per-city investigation
process built on top of it. Neither has been run on a real city yet — no actual city content gets written from
this file. Treat everything below as designed-on-paper until it survives contact with a first real city.

**Goal:** a repeatable way to derive what robot culture looks like *in a specific Tepenian city*, building on
top of the already-completed *Robot Universals* (`TepenianUniverseTimeline/Reference/Robot_Universals/`) —
which deliberately stops at "the floor and the method," explicitly leaving population-specific content to each
project's own repo. This is that population-specific layer, for Tepenia's cities.

---

## The Reasoning Mechanism We're Building On Top Of (not reinventing)

Robot Universals Part IV already supplies the *how to reason* — we don't need to re-derive this, only feed it
the right inputs:

- **The Differentiation Engine (Ch. 18):** for every universal that holds substantively robot-wide, ask which
  concrete condition plausibly shapes its expression in a given population. The condition must always be
  something concrete — a city, a locality, a class position, a specific history — never "robot-ness" itself
  treated as essentialist. Includes a **Universal Pool Mechanism** (a population draws its own selection from a
  shared pool, and the pool itself can shift over time) and an **Honesty Check** (report when a universal
  produces no meaningful local variation, rather than manufacturing difference to satisfy expectation).
- **Weighing the Axes (Ch. 19):** the existing default weighting when identity draws on multiple axes at
  once — **city/locality is dominant** (the default starting point for any robot population's identity),
  **build is secondary and locality-derivative**, **Gen/Mark is real but lightest-weighted**. This already tells
  us locality *should* be the anchor — which is exactly what this methodology exists to operationalize.

What Part IV deliberately does *not* supply: a fixed taxonomy of what "condition" actually means for a Tepenian
city. That's the gap this draft starts filling in.

**Second reasoning tool, added 2026-08-09 — the Cultural Iceberg Method.** Already this project's own proven
sorting discipline for the national-culture catalog work (`Neo-Races-and-Cultures/_Method/Cultural_Iceberg_Method.md`,
adopted 2026-07-16, source: Edward T. Hall's 1976 iceberg analogy). Culture is ~10% visible **Surface
Culture** (food, fashion, festivals, music, arts, language) and ~90% invisible **Deep Culture**
(communication styles, notions of courtesy/friendship/fairness, concepts of self/time, attitudes toward
authority/cooperation/age, approaches to religion/courtship/decision-making). The method's own stated purpose —
guarding against a neo-culture that's really just "the same values, different food" — is exactly the failure
mode the Swap Test (Step 6 below) exists to catch, so the two tools are doing complementary work: the Iceberg
split forces genuine Deep Culture content to exist in the first place; the Swap Test checks whether what got
written is actually specific to *this* city once it exists. **Every finding this methodology produces should
carry a Surface/Deep tag alongside its inheritance tag (Step 5)** — a city's findings that cluster entirely in
Surface Culture haven't done the real work yet, the same way a city's findings clustering entirely in
"directly-inherited" haven't (see Step 5).

---

## Input Category A — National Culture Composition

**Source:** `Locations/Cities/Local_Cultures/[Subnet]/[City].md` — all 32 cities done, 32-section structure
(Foundations → Cultural Identity → Social Structure → Political & External → Visitor & Diaspora → Reference).

**Relevant seam already built in:** Section III already contains a "robot-specific culture" subsection per
city, alongside human-robot relations and industry breakdown. Right now this is presumably thin/generic per
city (not yet run through Robot Universals' method) — the natural first move is to check what's actually
written there already before assuming it needs to be built from scratch.

**What this gives the Differentiation Engine:** the "which national cultures are actually present, and in what
proportion" condition — the most direct lever for the Universal Pool Mechanism, since a city's national
composition is quite literally which slices of the pool are locally available to draw from.

---

## Input Category B — Geography & Geology

**Source:** `Locations/Cities/Specs/[City].md` — `## Geographic Basis`, `### Annual Climate`, `## Founding`
sections. (Not the Physical Infrastructure Attributes files — those are derived output, not raw geography; the
actual geographic/climate/founding facts live here, one layer upstream.)

**What this gives the Differentiation Engine:** physical-environment conditions — climate severity, terrain,
isolation, proximity to other cities/subnets — the kind of condition that would plausibly shape robot-specific
adaptations (maintenance rhythms tied to weather, social patterns tied to isolation or density, etc.).

---

## Input Category C — Local Infrastructure

**Source:** `Locations/Cities/City_Megasheets/[Subnet]/[City]/[City]_Physical_Infrastructure_Attributes.md` —
all cities done, a cumulative numbered list of derived attributes (Life Support, Structural Engineering, Heat &
Power, Robot-Specific Infrastructure, Civic & Institutional Self-Sufficiency, Safety & Redundancy,
Communications, etc.), each already explicitly reasoned from Specs + Local_Cultures + Community Infrastructure.

**What this gives the Differentiation Engine:** built-environment conditions — what a robot's actual daily
material context looks like in this specific city (power reliability, maintenance access, communal vs. private
space allocation) — a second, complementary condition source to raw geography.

**Worth noting:** several of these files already have a "Robot-Specific Infrastructure" heading. Same situation
as Local_Cultures' robot-culture subsection — check what's already there before assuming a blank slate.

---

## Input Category D — Source Inspirations (three distinct sub-sources, not one)

1. **`Locations/Cities/Inspirational-Influences.md`** — the strongest, most direct hit. A per-city list of
   real-world *whole-city* parallels, tiered PRIMARY/SECONDARY/SUPPORTING, each with a reasoning note (e.g.
   Denison ← Kowloon Walled City for its single-organism density, Zukelli ← Kraków, Janbogo ← Central Asian
   chaykhana + Dubai mall culture for the specific *institutions* those parallels contribute, not just vibes).
   This is a genuinely rich, underused input — the PRIMARY entries especially read like ready-made seeds for
   "what would a distinctly local *robot* custom look like here."
2. **`Reference/Real-World/Stations/`** (shared, not per-city) — real-world Antarctic station/expedition
   infrastructure data. Grounds logistics/founding realism more than culture directly; likely a secondary,
   supporting input rather than a primary driver of robot-culture flavor.
3. **Per-city `## Real-World Parallel Locations`** inside `Neo-Races-and-Cultures/[Subnet]/[City]/[City]_Catalog.md`
   — per-*nation* real-world cultural/geographic parallels (distinct from #1's per-*city* whole-place parallels).
   Finer-grained than Inspirational-Influences.md; probably feeds Input A more than a standalone input of its
   own.

**Mandatory translation step, added 2026-08-09:** every one of these three sub-sources is a parallel to a
real-world *human* institution, city, or phenomenon. None of that transfers to robot culture automatically.
Any finding sourced from Input D must explicitly answer "what is the robot-specific analog of this," not just
restate the human-culture parallel with a robot noun swapped in — e.g. Janbogo's chaykhana-tradition parallel
isn't itself a robot custom; the actual finding is whatever robot-specific practice would plausibly grow *around*
a culture where tea-hospitality is treated as near-sacred (siligel/coolant-sharing ritual? a robot-specific
etiquette for declining?). This is what Category D actually contributes to the Differentiation Engine — flavor
and institutional shape to translate, not content to copy.

---

## Input Category E — Tepenia-Wide Robot Culture Canon

**Added 2026-08-09.** A third altitude, sitting between the Dolliverse-universal layer (*Robot Universals*)
and the single-city-local layer this whole methodology exists to build: robot-culture facts already
established as **Tepenia-nation-wide canon**, not universal to the Dolliverse and not specific to any one city.
Confirmed existing members of this tier:

- **Robot Biology and Culture** — siligel, coolant, robot coffee, smoking (`project_robot_biology` memory)
- **Glitch-Coolant** — the robot alcohol equivalent; bohemian circles favor variety, working-class circles favor
  potency (`project_glitch_coolant` memory). **Established canon since 2026-07-04**
  (`Robot_Physiology_and_Cultural_Practices.md`) — confirm this file is actually checked per city, not assumed
  absent; a real search-miss on this exact point already required correcting three already-drafted cities
  (Mawson, Dome Fuji — see their own Reference Notes — plus this note itself, added after the miss).
- **Robot Elementals & Solar Symbols — corrected and expanded 2026-08-10.** This is genuinely **two
  independent per-city symbol slots, not one system**, both drawn from `to-be-integrated/city-symbol-pairs.md`
  (self-marked "not canon, not binding, exploratory first pass," but real and populated for all 35 outer
  cities except Abowasa, paused pending its own founding-nation fix):
  - **The 8 Robo-Elements** (Earth, Air, Fire, Water, Wood, Metal, Electricity, Magnetism) — `project_robot_elementals_and_platonic_solids` memory.
  - **10 Solar Symbols** — the 9 planets plus the Asteroid Belt (Decentralization), sourced from
    `planetary-symbols.md` / `planetary-appended-symbols.md`.
  - Each city gets **one pick from each of the two slots, chosen independently** — whichever symbol in that
    slot is most characteristically fitting to the city, not a matched or thematically-linked pair. 80 possible
    combinations total.
  - **Platonic Solids remain a third, wholly separate, still-undesigned system — do not conflate with either
    of the above.** Continue excluding it as unsettled.
  - **Process discipline going forward:** every city's Category E pass must check `city-symbol-pairs.md` for
    *both* slots before proposing anything fresh. A city is only a genuine "first-ever proposal" if it's
    actually absent from that file. Three already-drafted cities (Janbogo, Mirny, Shirayuki) had this check
    skipped entirely and proposed elements that turned out to conflict with an existing pick; two more
    (Zhongshan, Byrd) skipped the check but happened to land on the right element by coincidence, while still
    missing the Solar symbol half and mislabeling the result as a fresh proposal. All corrected 2026-08-10 — see
    each file's own Reference Note.
- **Human-Robot Relations Baseline** — egalitarian, skewed-robot, with Kunlun/Dome Fuji as confirmed exceptions
  forbidding humans (`project_human_robot_relations_baseline`)
- **The Fragmentation Matrix** — the Bond/Grief system (`project_accomplishment_weight_system` and sibling
  memories)

**Deliberately excluded from this list, 2026-08-09:** the Robot "She" Pronoun Convention. It's a national given
that applies uniformly — nothing about it plausibly localizes per city, so it doesn't need a per-city
investigation slot the way the items above do. Listed here only so a future reader doesn't wonder why an
otherwise-comprehensive canon inventory is missing it.

**Why this matters for the investigation, not just as trivia:** every one of these is a second legitimate
"pool" a city's local robot culture can draw from and specialize — exactly the same relationship Robot
Universals itself has to a city (universal → localized expression), just one altitude down. It's also a
**mandatory consistency check**: nothing generated for a specific city may contradict this tier without that
contradiction being deliberately flagged and resolved, the same discipline already applied to Robot Universals
itself.

---

## Additional Candidate Inputs Surfaced During the Survey (not yet decided in/out)

- **`[City]_Community_Infrastructure.md`** — social-cohesion mechanisms and civic-space Additions per city;
  plausibly a fifth real input (distinct from raw Physical Infrastructure) since it's specifically about
  *social* infrastructure, which robot culture would plausibly hook into directly.
- **`City_Enneagram_Personalities/`** — each city's own Enneagram-based personality framing. Could plausibly
  cross-reference against Robot Universals' own psychological-universals material, if any exists there.
- **`City_Vision_Notes/`** — city-level vision/tone framing; likely too abstract to be a direct input but worth
  a glance.
- **Subnet Meta-Personalities** (`project_subnet_meta_personalities` — all 5 multi-city subnets complete) —
  an above-city layer; relevant if robot culture should inherit anything at the subnet level before the city
  level narrows it further.
- **`Background-Lore/Cities/[City]_Historical_Vignettes_and_Informational_Sheets.md` /
  `_Course_of_Events_Suggestions.md`** — actual incident-level history, distinct from the real-world Stations
  reference. Plausible source for "a specific past event that shaped this city's local robot custom," which is
  a different (and probably richer) condition-type than any of the above.
- **`District_Refugee_Diaspora_Composition.md`** — weighted cultural-transplant data, but scoped to Concordia's
  13 districts specifically, not standalone subnet cities. Open question: does this methodology need a
  Concordia-district variant distinct from the standalone-city version, given Concordia's diaspora-driven
  composition works differently from a single-nation-founded city like most subnet cities?

---

## The Per-City Investigation Process (draft, not yet run on a real city)

Six steps, run in this order, once per city, start to finish before moving to the next city (per the
one-city-at-a-time sequencing decision above).

### Step 1 — Concentric-Ring Gathering

Before any reasoning starts, gather the city's raw material outward in rings, reusing the search-widening
discipline already validated in this project (`feedback_general_investigation_methodology.md`):
own dedicated files (Specs, Local_Cultures, Physical Infrastructure Attributes, Community Infrastructure,
Catalog) → adjacent/cluster-level docs that mention the city without being filed under it (subnet-level
Megasheet material, Historical Vignettes, Course of Events) → cross-reference/database files in the same
folder tier (`City_Relationship_Database.md`, `City_National_Connections.md`) → a repo-wide grep for the city's
name with no path restriction → sibling cities in the same subnet, checked directly for contrast, not just each
against its own internal facts → any subnet- or project-level synthesis document that cites this city. Read, not
just grep — grep only prioritizes where to look.

### Step 2 — Universal-by-Universal Triage

With the city's actual raw material now in view, walk the full catalog — every Robot Universals chapter/universal
**and** every Input Category E (Tepenia-wide canon) entry — and triage each one against this specific city, into
one of **four** outcomes (revised 2026-08-09, after the Janbogo test run surfaced a real gap — see below):

- **Localizes here** — a concrete condition from Input Categories A–E plausibly shapes its local expression.
- **Doesn't localize here (Honesty Check null)** — this item is a genuinely valid input for an entity like this
  one, it was actually checked against the city's real material, and nothing local emerged. Write down why. This
  is a real, required output, not a skipped step.
- **Out of scope / not applicable** — this item was never a valid input for this *kind* of entity to begin with,
  independent of what the city's material says. Distinct from the Honesty Check null above: a null means "I
  checked and nothing local surfaced"; out-of-scope means "there was nothing to check here in the first place."
  (Confirmed real case, from the Janbogo test run: the Fragmentation Matrix is a player-facing companion/district
  mechanic with existing per-Concordia-district calibration — it isn't a culture-content input for a standalone
  subnet city at all, which is a different situation than Gen/Mark genuinely not varying in Janbogo.)
- **Uncertain, investigate further** — a transient state, not a final outcome; resolve to one of the three above
  before the city's pass is considered done.

This is what "the Robot Universals cross-check happens in real time" actually means in practice — a concrete,
per-city pass, not a vibe.

### Step 3 — Per-Input-Category Pass

For every universal triaged "localizes here" in Step 2, work through Input Categories A–E to identify the
actual local condition responsible, applying Category D's mandatory translation rule wherever Source
Inspirations material is involved.

**Kinship-specific reminder, added 2026-08-10 after a real pattern-check across the first 10 cities run.**
Every Kinship finding so far had converged on some shape of vertical mentor/mentee (craft apprenticeship,
credit-diffusion, housing lineage, archive-domain inheritance). **Per direct developer instruction: shared
experience and shared goals are the bigger, stronger, more fundamental driver of kinship — mentoring is not a
separate, competing mechanism sitting alongside shared experience, it's one particular *form* shared experience
can take** (the shared experience of teaching and being taught, of working the same problem side by side over
time). So the root question for every city's Kinship pass isn't "mentor/mentee or shared-experience" as a
binary choice — it's always "what is the actual shared experience or shared goal here," and *then* asking
what shape it takes: sometimes that shape is a mentoring relationship, sometimes it's a peer cohort bonded by
surviving the same crisis or pursuing the same goal as equals with no teaching relationship at all, sometimes
both are present as genuinely separate bonds. Start from the shared experience, not from "what's the local
apprenticeship system" — the latter question skips straight to one possible answer-shape without asking what
it's actually an answer to.

**Further refinement, added 2026-08-10 after a real near-miss on Casey's re-scan.** "Shared experience" means
an ongoing, cumulative shared *life* experience — a shared way of living, working, or existing together over
time — not a single discrete incident (one storm weathered together, one rescue, one crisis night). A specific
named incident is valuable, but it belongs in the city's Historical Vignettes/Course of Events material (or as
grounding for a different aspect, like §2's Cooperation/Morality ethic) — it is not itself the Kinship
mechanism. The test: would this bond exist between two robots who never happened to share that one specific
event, but who live the same ongoing condition? If yes, the ongoing condition is the real Kinship finding, and
the specific incident is supporting municipal history, not the mechanism itself.

### Step 4 — Cross-Reference Synthesis

Second pass, after the straightforward one-condition-to-one-universal mappings from Step 3 are down: chase
2nd/3rd/4th-order effects that emerge from **combining** input categories, not from any single category read in
isolation — the same technique already named in this project (`feedback_cross_reference_synthesis_technique.md`)
and already proven as "Methodology #2" in the Physical Infrastructure Attributes files. The most distinctly
*local* findings (as opposed to generic robot-culture findings that happen to be filed under this city) will
come from here, not from Step 3.

### Step 5 — Dual Tagging (Inheritance + Iceberg Layer)

Every finding that survives Steps 3–4 gets exactly **two** tags before being written down.

**Inheritance tag (one of):**
- **Directly-inherited pool-draw** — a robot participates in an existing local/national human-cultural practice
  essentially unchanged.
- **Adapted pool-draw** — the practice gets genuinely modified by a robot-specific condition (embodiment,
  lifespan, Gen/Mark, Arcanet connectivity, etc.).
- **Genuinely emergent, robot-only** — a practice that wouldn't exist at all without robots specifically (in the
  shape of Glitch-Coolant or Robot Elementals — Category E's own members are the reference examples).

**Iceberg-layer tag (one of):**
- **Surface Culture** — food, fashion, festivals, music, arts, language, the visible ~10%.
- **Deep Culture** — communication style, notions of courtesy/friendship/fairness, concepts of self/time,
  attitudes toward authority/cooperation/age, approaches to religion/courtship/decision-making — the invisible
  ~90%, and the layer that actually makes a local robot culture distinct rather than a reskin.

Both tags are mandatory, not optional flavor — together they're the actual guardrail against the single biggest
failure risk for this whole effort: producing content that's just Local_Cultures restated with "robot" stapled
onto it. A city's findings should show a real mix across both axes — not clustering entirely in
"directly-inherited," and not clustering entirely in "Surface Culture."

### Step 6 — The Swap Test

Closing check before considering a city's pass complete: for each surviving finding, would it still make sense
essentially unchanged if the city's name were swapped for a demographically/geographically similar neighbor in
the same subnet? If yes, the finding hasn't actually localized — send it back through Steps 3–4, or drop it and
document why nothing genuinely local emerged for that universal (a legitimate Honesty Check outcome, per Step 2).

---

## Open Questions

### RESOLVED — Output shape (2026-08-09)

**Build everything in a wholly separate, dedicated folder — not in-place expansion of Local_Cultures.** New
sibling folder created: `Locations/Cities/Local_Robot_Culture/`, mirroring `Local_Cultures/`'s own structure
exactly (subnet subfolders — `Janbogo_Subnet/`, `Mirny_Subnet/`, `Mawson_Subnet/`, `Halley_Subnet/`,
`Palmer_Subnet/`, `Byrd_Subnet/`, `Amundsen_Station/` — all created, currently empty). Each city gets its own
new file here once built, sitting entirely alongside (never overwriting) its existing `Local_Cultures/[City].md`
and its existing "robot-specific culture" subsection there.

**This also resolves the Reconciliation Logic question below — deliberately, not by accident.** Since nothing
gets merged or edited in place, there's no live collision to arbitrate at generation time. Once a city has both
its original Local_Cultures entry *and* its new dedicated Local_Robot_Culture file, the developer reviews both
side by side and decides case-by-case how (or whether) to fold the new material back into Local_Cultures — the
previously-drafted "working default priority order" (A > D > B/C) becomes a tool for *that* later review pass,
not a rule that has to hold at generation time. Kept below for reference, demoted from "open question" to
"reference note for the eventual reconciliation review."

### RESOLVED — Sequencing (2026-08-09)

**One city at a time, full depth each time — not a bulk pass, not tiered-by-hub like the Physical
Infrastructure pass.** This also resolves the Robot Universals cross-check question below: since only one
city is ever in progress at once, the "does every universal need a local-differentiation pass here" check
happens in real time, per city, rather than needing to be scoped as a separate up-front project stage. No
city order chosen yet — that's the next real decision once the methodology itself (the actual step-by-step
process, not just this input inventory) is designed.

### Reference note, not a live rule — the demoted reconciliation-priority hypothesis

Kept for whenever a city's two versions (Local_Cultures vs. Local_Robot_Culture) actually get compared:
National Culture Composition (A) plausibly outweighs Source Inspirations (D), which in turn plausibly outweighs
Geography/Geology and Local Infrastructure (B/C) as a *pair* — reasoning preserved from the original draft.
Explicitly not binding; the actual side-by-side review is the real arbiter now, this is just a starting lens
for that reviewer.

---

## Planned Follow-On Pass (not started, not scoped in detail — roadmap note only)

**Added 2026-08-09, per developer direction.** Once every city has a completed Local Robot Culture spec sheet,
a second pass is planned: deriving the actual **places, things, and people** that would concretely exist given
each city's now-established local robot culture — places of work, places of leisure, settings of social
connection, and so on. This is explicitly sequenced *after* the full city-by-city culture pass, not in
parallel with it — the culture has to exist first for this second pass to have real material to work from,
the same dependency relationship this methodology itself has on Robot Universals. Not scoped beyond this note;
revisit once the tracking checklist (`02_City_Tracking_Checklist.md`) is closer to fully checked off.

---

## Explicitly Not Yet Done

- **Janbogo run 2026-08-09** — first full test of the 6-step process, output at
  `Local_Robot_Culture/Janbogo_Subnet/Janbogo.md`. Confirmed as a draft pending developer review, not settled
  canon. The run surfaced one real process gap (the Step 2 three-way triage revision above) and validated
  several design choices in practice (the dual-tagging discipline catching a real near-mistake on the
  Vernacular Language finding's Iceberg tag; Cross-Reference Synthesis producing the strongest findings, as
  hypothesized). See the developer discussion following that run for the full readout.
- **Reference section (Part III of the template) restructured 2026-08-09** — Janbogo's run came back with this
  section nearly empty, correctly: landmark/event/figure invention isn't really this methodology's job
  (that's Historical Vignettes/Course of Events territory). See `01_LOCAL_ROBOT_CULTURE_TEMPLATE.md` for the
  lighter replacement.
- **Tracking checklist added:** `02_City_Tracking_Checklist.md`, in this same folder — all 35 cities +
  Amundsen Station, subnet by subnet, status per city.
- 35 of 36 entries still need this process run. Janbogo is the only one attempted so far, and its own status is
  Draft, not Complete, pending developer review of the test-run output before it's trusted as a template for
  how the remaining cities should go.
- This file itself is expected to be reorganized or split further as more real cities get run — treat it as a
  working draft, not a stable reference, until a handful of cities have gone through without further process
  changes.
