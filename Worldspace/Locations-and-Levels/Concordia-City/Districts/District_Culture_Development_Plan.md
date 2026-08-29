# District Culture Development Plan

**Written 2026-08-16.** Direct follow-on to the gap analysis comparing Concordia's 13 districts against the 36
outer cities' `Local_Cultures/CITY_CULTURE_TEMPLATE.md` (32 sections). That analysis found four tiers: strong
and comparable (Founding history, Political character, Notable Figures, Population/diaspora — the latter via
`District_Refugee_Diaspora_Composition.md`), present-but-inconsistent (Architecture, Sensory Profile, Export
Culture, Arcanet Culture), confirmed absent (Robot-Specific Culture, Religious/Philosophical Landscape, Visitor
Experience, Visitor-to-Resident Transition, Fashion), and likely-genuinely-N/A (Language, Climate Character,
Seasonal Rhythms — all 13 districts share Concordia's own single language and climate, so these shouldn't be
forced into district-level content).

> ### ⚠ RE-AUDIT, 2026-08-16 — the tiers above account for only 16 of the 32 sections
>
> Caught immediately after Cancer's full 7-phase pass *(the count is correct here — this describes the plan as it stood BEFORE Phase 7 Native Culture was inserted and Robot-Specific was renumbered 7→8; do not "correct" it to 8)*: Cancer cleared every phase and **still had no Cuisine,
> no Music, no Arts, no Counterculture, no Municipal Holidays, and no district-level Human-Robot Relations** —
> and `siligel`, established Tepenia-wide robot-food canon, appeared zero times in the entire file. Sixteen of
> the template's thirty-two sections were never classified into any tier, so no phase was ever assigned to
> them.
>
> **The specific reasoning error:** several missing categories were waved off as "already covered in fragments
> by `District_Refugee_Diaspora_Composition.md`." That file covers what feeder populations **brought in**. It
> does not cover what the district itself **developed**. Transplanted ≠ native, and a district whose only
> cuisine is other cities' cuisine has no cuisine.
>
> The corrected full-32 classification is in the "Complete template audit" section below. It adds **Phase 7**
> for the seven genuinely-missing native-culture categories, and a mandatory closing QA gate
> (`Phase_Instructions/00c_Completion_QA_Checklist.md`) so that no district can be marked complete with silent
> gaps again.

**Purpose of this file:** a real, finishable plan for closing every one of those gaps, district by district —
not another "ongoing/never-closed" work area like the weapon/gear catalog. The end state this plan targets:
every one of the 13 districts reaches parity with the outer cities' template on every category that genuinely
applies to a district, so that Local District Robot Culture — the actual downstream goal — has real ground to
stand on everywhere, not just in patches.

**Updated 2026-08-16 — folded in a second, pre-existing prerequisite.** `Dev-Road-Map/Weekly_To-Do_-_Current.md`
(lines 107-118) already carries a flagged, developer-confirmed item — **"Per-district ordinary daily life,"**
flagged 2026-07-31, confirmed starting 2026-08-12, not yet actually executed — that this plan had not accounted
for, since it isn't one of the outer-city template's 32 categories at all. It asks: what does an ordinary
resident's actual day-to-day life look like — routines, mundane concerns, personal struggles,
escapism/downtime — **distinct from** whatever the district's own headline civic identity or institutional
purpose is. Developer's own example: Scorpio residents cannot plausibly spend every waking moment in a death
ritual confessing their grief; people have lives outside a district's defining function. This is now folded
into this plan as its own phase (Phase 5, below) — it's every bit as load-bearing a Robot-Specific Culture
prerequisite as the template-derived gaps, arguably more so, since "what does a robot resident's ordinary day
actually consist of" is closer to Robot-Specific Culture's own subject matter than Architecture or Export
Culture are. Two sibling items in the same Weekly To-Do block — **"Per-district inter-city conflicts"** and
**"Per-district inter-city friendships"** (both also flagged 2026-07-31), covering friction/common-ground
between diaspora populations — are related but serve a different downstream purpose (Under-Questline
generation) and aren't folded in here; they're noted for awareness, not treated as part of this plan's scope.

---

## Complete template audit — all 32 sections (2026-08-16)

Every section of `Local_Cultures/CITY_CULTURE_TEMPLATE.md`, classified for districts. Four verdicts:
**Covered** (real district material already exists elsewhere, under a different name), **Phase N** (this plan
handles it), **Absorbed** (legitimately answered inside another category rather than needing its own), and
**N/A** (genuinely doesn't apply to a district as opposed to a city).

| # | Template section | Verdict | Where it lives / why |
|---|---|---|---|
| 1 | National/Ethnic Composition | Covered | `District_Refugee_Diaspora_Composition.md`, weighted per district |
| 2 | Founding Story | Covered | Mega-Init Hard Facts + `Historical_Pressures.md` |
| 3 | Climate Character | Absorbed | Districts *do* have distinct micro-climates (Cancer humid, Leo notably warm) — answered inside Sensory Profile, Phase 1. The original "N/A" call was too hasty but the content lands correctly. |
| 4 | Seasonal Rhythms | N/A | Concordia is enclosed; no district-level seasonal variation established |
| 5 | Post-Culture Identity | Covered | Mega-Init One-Line Pitch + Canon Reference "What It Really Is" |
| 6 | Social Contract & Unwritten Rules | Covered | Canon Reference "Cultural Texture" — genuinely strong for every district |
| 7 | Who This District Attracts | Covered | Mega-Init "Who Lives Here, and Why" |
| 8 | Language | N/A | Shared city-wide. *Open question flagged:* district-specific jargon/slang may still be real — see QA checklist. |
| 9 | Architecture | **Phase 1** | |
| 10 | Cuisine (human / social / **robot-siligel**) | **Phase 7** | **Was missing entirely.** The siligel sub-section is the most serious omission — established national canon, zero district coverage. |
| 11 | Fashion | **Phase 2** | |
| 12 | Music | **Phase 7** | **Was missing.** Cancer's lullaby tradition is canon and was never developed as a musical culture. |
| 13 | Arts & Aesthetics | **Phase 7** | **Was missing** — visual arts, literature, crafts |
| 14 | Sensory Profile | **Phase 1** | |
| 15 | Division of Industry | Absorbed | Occupations in Canon Reference "Inhabitants"; economic structure in Phase 1's Export Culture and Phase 5's Ordinary Daily Life |
| 16 | Human-Robot Relations | **Phase 7** | **Was missing.** Distinct from Phase 8's Robot-Specific Culture: that covers robot culture *among robots*, this covers how the two populations actually relate *in this district*. |
| 17 | Robot-Specific Culture | **Phase 8** | |
| 18 | Religious / Philosophical Landscape | **Phase 2** | |
| 19 | Underground / Counterculture | **Phase 7** | **Was missing**, and it is the richest of the seven — every district with a strong dominant culture generates something that pushes against it. |
| 20 | Private Life & Minority Communities | **Phase 7** | **Was missing** — the integration bargain, public face vs. behind closed doors |
| 21 | Political Character | Covered | Cross-Reference Synthesis + Canon Reference |
| 22 | Relationship to Upper Earth | N/A | A Concordia-level and national-level relationship, not a district-level one |
| 23 | Relationship to Other Districts | Covered | `District_Natural_Allies.md`, `Historical_Inter-District_Effects.md`, Cross-Reference Synthesis |
| 24 | Arcanet Culture | **Phase 3** | |
| 25 | Export Culture | **Phase 1** | |
| 26 | Municipal Holidays | **Phase 7** | **Was missing.** A standing TODO already flags holiday gaps project-wide. |
| 27 | Visitor Experience | **Phase 4** | |
| 28 | Visitor-to-Resident Transition | **Phase 4** | |
| 29 | Notable Local Landmarks | Covered | `Regional-Characteristics/District_Prominent_Features.md`, extended by Phase 6 |
| 30 | Significant Local Events | Covered | `Historical_Pressures.md` |
| 31 | Notable Figures | Covered | Full Extrapolation's own Notable Figures finding |
| 32 | Diaspora Character in Concordia | N/A | Self-referential for a district — they *are* in Concordia |

**Totals:** 12 Covered · 2 Absorbed · 4 N/A · 14 assigned to Phases 1-8.

---

## Why Robot-Specific Culture goes last, not first

Robot-Specific Culture is the hard blocker for the eventual goal, but it's blocked *because* the groundwork
isn't there yet — exactly the same dependency that already existed for the outer cities, where Local Robot
Culture was only ever built on top of a city's own already-complete general cultural deep-dive. Districts don't
have that completed foundation yet. Building Robot-Specific Culture first here would repeat the mistake the
gap analysis was built to catch: writing robot culture with nothing underneath it to anchor into (no
established Architecture to say where robots live and work, no Sensory Profile to say what a district's own
industrial/domestic soundscape sounds like to a robot's senses specifically, no Religious/Philosophical
Landscape to say what belief systems a district's robot population might hold, no Fashion to say how robots in
that district dress or don't). So this plan sequences Robot-Specific Culture as the capstone phase, not the
opener — everything else in this plan exists to give it something real to build on.

---

## Governing methodology — how the actual writing gets done

This plan says *what* to close and in *what order*; it doesn't invent its own writing process — the project
already has one, mirrored for districts from the outer-city Megasheet method. Three existing files govern how
Phases 1-8's content actually gets synthesized. Read them before starting any phase, not just this plan.

**For the generative toolkit — how new culture actually gets invented — see
`../../Cultural_Synthesis_Techniques.md`.** Fourteen named techniques (Bounded Personal Franchise, Failure State
of the Core Value, Universal Micro-Practice, Ambiguous Universal Object, Retroactive Mechanism, Necessity Before
Meaning, Surviving Witness, Asymmetric Record-Keeping, Non-Thematic Export, Membership by Unremarked
Persistence, Negative Image, Native Before Transplanted, Unused-Tier Mine, Population Share Check), each with a
divergence table showing the same operation producing unlike results in unlike places. The phase files say what
to cover; the toolkit says how to invent it. **Never carry one district's answers into another.**

**For applying the zodiac personality substrate, see `Phase_Instructions/00e_Substrate_Application_Pass.md`**
(added 2026-08-29). `Zodiac_Personality_Substrate/` mines eight astrology texts into a per-district design
reference — temperament, capability profile, shadow, material texture, and a complete inter-district conflict
geometry. It is **out-of-fiction design shorthand only** and applies to Concordia's districts and nothing else
in the setting. `00e` is the repeatable procedure for using it; Cancer's own file carries the worked example.

**For extensive, phase-by-phase how-to instructions, see `Phase_Instructions/`** (added 2026-08-16) — one
dedicated, self-contained file per phase (`00_Index.md` plus `01_Phase_1_...md` through `08_Phase_8_...md`),
each going far deeper than this section into category definitions, sources, step-by-step process, per-district
status, output format, and phase-specific pitfalls. This section stays a compressed summary; the phase files are
the actual execution reference.

1. **`City_Megasheet_Compilation_Guide.md`** (Outside-World/.../City_Megasheets/), explicitly mirrored for
   districts (see `Cancer_Mega_Init.md`'s own header). Its Step 2 posture — **"invent, but every invention has
   to be traceable back to something already established"** — is the one that governs Phases 1-8 directly,
   since all new content lands in each district's `Full_Extrapolation.md`, the same file Step 2 produces. Concrete
   rules from it that carry over unchanged: name things specifically rather than leaving placeholder concepts
   abstract; frame every new section as proposed extrapolation, not locked canon; and — already a *pre-existing*
   convention, independent of anything decided this session — **propose Notable Figures only as explicitly
   labeled placeholder/proposed**, never presented as settled. This is the same spirit as this plan's own
   no-invented-names rule for Phase 6's "people" entries, just discovered to already be established practice
   rather than a new rule.
   - Its Step 3.5 (**Community Infrastructure & Social Life** — Additions / Small offices for educational
     training / Social cohesion mechanisms, "get concrete: physical spaces, small institutions, recurring
     rituals") was **originally developed for Concordia's 13 districts** (2026-07-29) and already exists for
     all 13, folded into `District_Canon_Reference.md` rather than a separate file. **This directly overlaps
     with Phase 6 (Thematic Breadth Catalog)** — Phase 6 should read as *extending* this existing material
     (adding named places, things, and role-placeholder people beyond what Additions/Small-offices/Social-
     cohesion already cover) rather than starting from a blank page. Check each district's existing Community
     Infrastructure section first.
   - Standing rule from this same guide, binding for every phase: **every new Full_Extrapolation section closes
     with its own "Worth Your Attention" callout**, written into the file itself, not left only in chat.
2. **`00b_Two_Stage_Methodology.md`** — Stage 1 (organic ~250-year pre-war formation, 2564-2812) vs. Stage 2 (the
   Long Night War's fallout acting on an already-formed community, 2812 onward). Most of Phases 1-8's content is
   present-day (Architecture-as-it-stands, current Fashion, current Ordinary Daily Life), but *why* something
   looks the way it does routinely reaches back into Stage 1 causation — keep the two layers distinct rather
   than treating a district's whole character as war-caused.
3. **`District_History_Enhancement_Opportunities_Template.md`** — narrower in original scope (a flag-only,
   Stage-1-only enrichment pass, already run for all 13 districts), but its **five-lens ideation structure** is
   a reusable technique whenever a phase category needs a starting point: district civic function/economy →
   [category], feeder-city population culture → [category] (**check `City_Refugee_District_Affinities.md`'s
   Stage 2 Overrides first** — Scorpio and Gemini are confirmed override cases, meaning their top-ranked feeder
   cities represent war-driven trauma pull, not genuine cultural affinity, and using them un-checked would be
   an easy mistake), real-world historical precedent (via `District-Inspirational-Influences.md`), district
   personality/geography/architecture → [category], and a catch-all "other" pulling from `Historical_Pressures.md`/
   `Historical_Inter-District_Effects.md`/open Mega-Init questions.

**Source-check discipline (from the Template's own validated finding):** `Historical_Pressures.md` and
`Historical_Inter-District_Effects.md` interleave Stage 1 and Stage 2 material in the same entries without
labeling which is which — confirm each individual detail's own dating before citing it, don't assume based on
which file or section it lives in.

4. **The color-coded district map** — `Reference/Images/Maps/Concordia_City_-_Extended_map_-_with_labels_-_Color-Coded_by_District.jpeg`.
   (A second version of this map with quest-route arrows overlaid also exists in the same folder — **still
   tentative, not yet confirmed canon, don't reference it in phase work until the developer says otherwise.**)
   Added 2026-08-16 — genuinely load-bearing spatial data that applies across **all eight phases**, not just
   Architecture. Confirmed from the map:
   - **Concordia is a literal radial city.** The Hub (unlabeled small white circle) sits at the exact geometric
     center; all 12 zodiac districts arrange in wedges radiating outward from it. This isn't just narrative
     framing (`World_Map_Boundaries.md`'s "radial city centered on the Hub") — it's the city's actual physical
     shape.
   - **District territory is wildly uneven, and that unevenness is meaningful.** Seven districts (Gemini, Leo,
     Aquarius, Scorpio, Aries, Virgo, Libra) hold small wedges directly touching the Hub — compact, central,
     symbolically important but physically small. Two districts (**Sagittarius** and **Capricorn**) are
     enormous outer-ring territories that **never touch the Hub at all** — they wrap around large arcs of the
     city's outer edge instead. Cancer, Taurus, and Pisces sit in between: present in the middle ring, absent
     from the innermost ring.
   - **Exactly 3 highway ramps connect Concordia to the rest of Tepenia, all landing at the outer edge:** Hwy 37
     (Mountain Cut Throughway) and Hwy 110 (Coastal Cut Highway) both land in **Sagittarius's** outer arc; Hwy
     183 (Janbogo Highway) lands at the **Capricorn/Sagittarius** boundary. **Sagittarius and Capricorn are
     Concordia's literal gateway districts** — this is concrete, load-bearing for Export Culture (Phase 1,
     physical export routes), Visitor Experience (Phase 4 — most visitors' actual first physical contact with
     Concordia is one of these two districts, not wherever they're ultimately headed), and Thematic Breadth
     (Phase 6 — customs/logistics infrastructure concentrates here).
   - **Physical distance from the Hub is real, usable texture for Phase 5 (Ordinary Daily Life)** — a Gemini or
     Leo resident's whole district is a short walk from the Hub; a Sagittarius or Capricorn resident may face a
     genuinely long commute to reach the city center or any other district, which is exactly the kind of
     mundane, non-thematic daily-life detail that phase is asking for.
   - Check this map whenever a phase's reasoning would benefit from knowing which districts are physically
     adjacent, central vs. peripheral, or gateway vs. interior — it's a standing spatial reference for the whole
     plan, not a one-time Phase 1 lookup.
5. **`../../Real-World_Basis_Extrapolation_Method.md`** (added 2026-08-16) — how to actually derive Phase 6's
   places/things/people/settings: pull every Primary/Secondary/Supporting pick from `District-Inspirational-
   Influences.md`, web-research each real place at the *concrete* level (named buildings/rituals/roles/tools,
   not just its general category), and fuse the specific details against what's already established, the same
   way the Compilation Guide's Step 1.6 already fuses real-world research into the Mega-Init — just aimed at
   concrete Thematic Breadth material instead of overall identity. Already demonstrated live against Cancer's
   own unused Secondary picks (Ospedale degli Innocenti, Epidaurus's abaton) in that file's worked example.

---

## New-category mini-definitions

Four of the confirmed-absent categories have no district-level precedent at all (cities have them, but a
district isn't a city, so the concept needs a district-appropriate translation before any content gets
written). Resolving these definitions is a prerequisite step, done once, not per-district:

- **Robot-Specific Culture.** Cities anchor this in founding-nation robot-culture threads layered onto Robot
  Universals. Districts aren't organized by nation, so this needs its own lens — most likely **theme/role-based**:
  a district's own defining civic identity or industry (Cancer's caregiving, Aquarius's whatever Aquarius's
  identity resolves to, etc.) is what a district's robot population organizes its own culture around, the way a
  workplace or a calling shapes a subculture rather than a homeland does. This lens gets decided once, then
  applied per district in Phase 8.
- **Religious/Philosophical Landscape.** Same shape as the city version — which of Tepenia's established robot
  religions (Polydimensional Animism, etc.) and human belief systems have real presence in this district, and
  how the district's own defining character (grief-heavy Cancer vs. whatever Libra's is) inflects practice.
  Directly reuses existing city-level religious content wherever diaspora composition already implies it.
- **Visitor Experience / Visitor-to-Resident Transition.** Cities define this as an outsider-to-Tepenia
  experience. A district's equivalent is intra-Concordia: what does it feel like for a resident of a
  *different* district, or a freshly-arrived refugee before diaspora placement, to first enter this district —
  and then, separately, what does it take for them to stop being a visitor and start being considered a
  resident. This is a genuinely new concept for district-level writing and needs a one-time definition pass
  (what marks "visitor" vs. "resident" status in a district that doesn't have Concordia-wide citizenship
  boundaries) before the 13 individual entries get written.
- **Fashion.** Reuses the same logic as the Weapon/Gear catalog's armor layer (heavy-duty clothing shaped by
  circumstance, not designed intent) but for everyday dress — what a district's own conditions, industry, and
  culture produce as a recognizable "look," distinct from any founding-nation costume a diaspora community
  might have brought with them (which `District_Refugee_Diaspora_Composition.md` already covers in fragments).
- **Ordinary Daily Life.** Not from the city template at all — a separate, pre-existing TODO item
  (`Weekly_To-Do_-_Current.md` lines 107-118). The defining move: for every district, deliberately write the
  texture of a resident's day that has *nothing to do with* the district's headline function. Cancer's whole
  identity is caregiving and grief — so what does a Cancer resident do on a Tuesday that isn't caregiving or
  grieving? Scorpio's whole identity is a 250-year confrontation methodology — so what does a Scorpio resident's
  actual daily routine, mundane worries, and downtime look like, given nobody spends 12 straight hours a day in
  active grief ritual? This applies equally to human and robot residents, and should cover routines, mundane
  concerns/worries, personal struggles, and forms of escapism/downtime distinct from institutional purpose.
- **Thematic Breadth Catalog.** Added 2026-08-16, per the developer's own framing: a district is built around a
  **theme**, not a **thing** — Cancer isn't literally wall-to-wall caregiving facilities any more than a
  real-world "government town" is wall-to-wall government buildings. This pass, done after Ordinary Daily Life,
  goes district-by-district and, using everything already established through Phase 5, identifies the wider
  cast of **places, things, people, and settings** a district needs to feel like a real, lived-in place rather
  than one note played over and over — the ordinary shops, minor institutions, informal hangouts, recognizable
  local character-types, and physical objects that exist because people live there, refracted through the
  district's theme rather than restating it literally. Ordinary Daily Life (Phase 5) already implies many of
  these — a resident's daily routine has to happen somewhere, among some people, using some things — so this
  phase is the direct, systematic follow-through: naming and cataloging what Phase 5 only implied. This is what
  actually gives level design and quest writing enough varied, concrete material to work with, and gives
  Robot-Specific Culture (Phase 8) a full physical/social world to embed itself in, not just a single thematic
  landmark repeated in different shapes. **Rule for the "people" entries (developer instruction, 2026-08-16):
  no actual names.** Write these as role/archetype placeholders only — "a veteran repair-shop owner," "a
  recurring streetside vendor," "the neighborhood's informal mediator" — never invented proper names. The
  developer wants to name these figures personally once the roles themselves exist. **Not a blank-page phase:**
  every district already has a Community Infrastructure & Social Life pass (`District_Canon_Reference.md`,
  brainstormed 2026-07-29 — Additions / Small offices for educational training / Social cohesion mechanisms).
  Phase 6 extends that existing material with what it doesn't cover — named individual places and landmarks
  (not just institution-types), physical objects, and people/role-placeholders — rather than re-deriving
  institutions and rituals that already exist. **Primary derivation technique:** `Real-World_Basis_Extrapolation_Method.md`
  (added 2026-08-16) — web-research each district's own `District-Inspirational-Influences.md` picks at the
  concrete level and fuse specific real-world details (named buildings, rituals, roles, tools) against
  established in-fiction fact, rather than inventing places/things/people from nothing.

---

## Execution order (8 phases)

Phased by category across all 13 districts, not district-by-district in isolation — this keeps each category's
depth and tone consistent across all 13 before moving to the next, the same way the outer cities' work was
pursued as systematic category sweeps rather than one city being finished in isolation from the others.

1. **Phase 1 — Lived-in texture.** Architecture, Sensory Profile, Export Culture. Groundable directly in each
   district's own existing Hard Facts tables and Full Extrapolation Findings — the lowest-lift phase, and the
   most direct foundation for later Robot-Specific Culture (where robots live/work, what a district sounds and
   feels like, what it's known for producing).
2. **Phase 2 — Identity and meaning.** Religious/Philosophical Landscape, Fashion. Builds on Phase 1's
   established texture plus the diaspora composition file's existing fragments.
3. **Phase 3 — Arcanet Culture.** Formalize into one dedicated Finding per district (all 13 currently lack a
   dedicated section; Gemini and Sagittarius have incidental mentions worth promoting rather than rewriting
   from scratch).
4. **Phase 4 — Visitor Experience / Visitor-to-Resident Transition.** Requires the one-time concept definition
   above before any per-district writing starts.
5. **Phase 5 — Ordinary Daily Life.** The pre-existing TODO item folded in above. Comes after Phases 1-4
   deliberately — a district's routines/mundane-concerns/downtime texture reads better once its Architecture,
   Sensory Profile, and Religious/Philosophical Landscape already exist to set the physical and emotional
   backdrop a resident's ordinary day happens against. Directly and explicitly distinct from each district's
   headline civic identity, per the developer's own Scorpio example.
6. **Phase 6 — Thematic Breadth Catalog.** For each district, systematically name the places, things, people
   (role/archetype only, no invented names — see mini-definition above), and settings that exist because a real
   population lives there, refracted through the district's theme rather than restating it literally. Directly
   follows through on what Phase 5's daily-life routines already implied but didn't itemize.
7. **Phase 7 — Native Culture.** *(Added 2026-08-16 by the full-32 re-audit. Robot-Specific Culture, previously
   Phase 7, was renumbered to Phase 8 so this could take its correct position in the sequence.)* The seven
   categories the original tier analysis missed entirely: Cuisine including robot/siligel culture, Music, Arts
   & Aesthetics, Human-Robot Relations, Underground/Counterculture, Private Life & Minority Communities, and
   Municipal Holidays. It sits before Phase 8 because four of the seven feed it directly — a district's
   siligel culture, its human-robot relations, its counterculture, and its private-life bargain are all inputs
   to Robot-Specific Culture, not outputs of it. **Native, not transplanted** is its governing discipline. See
   `Phase_Instructions/07_Phase_7_Native_Culture.md`.
8. **Phase 8 — Robot-Specific Culture.** The capstone. Requires the theme/role-based lens decision above, then
   draws on every prior phase — Architecture, Sensory Profile, Religious/Philosophical, Fashion, Ordinary Daily
   Life, and now the Thematic Breadth Catalog especially, since robot culture needs an actual populated world
   (places/things/people) to embed itself in — exactly mirroring how the outer cities' Local Robot Culture drew
   on their own completed general deep-dives.

**Sources to work from:** `District_Source_Index.md` (written 2026-08-16) catalogs every file in the repo
carrying real content about each district — universal per-district file sets, shared cross-district files, and
the genuinely uneven long-tail material (doll home-district assignments, Staging entries, Storyline/Game-Mechanics
cross-references). Consult it before starting any phase rather than re-discovering sources district by district;
it also flags real gaps worth knowing about going in (Virgo has no confirmed anchor doll; Capricorn's core
injustice mechanism is still undecided).

**Where content lives:** each district's own `*_Full_Extrapolation.md` — new Roman-numeral Findings appended
after the existing ones, matching the file's current convention (Cancer's example: `I` through `VII`, plus
"Worth Your Attention"). Content currently misplaced outside Full_Extrapolation — Libra's Export Culture
(currently only in `README.md`/`Libra_Mega_Init.md`) and Gemini/Sagittarius's incidental Arcanet mentions —
gets promoted into a proper Full_Extrapolation Finding as part of the relevant phase, not left where it is.

---

## Per-district checklist

Legend: **+ already has it** (may still need light expansion or promotion into Full_Extrapolation) · plain
entry = needs full development from scratch.

### 01 — Cancer — **ALL 8 PHASES COMPLETE — REWRITTEN FROM SCRATCH 2026-08-16**
- Architecture — **Done** (Finding VIII — apse vernacular, **the Window Reach**, Growing Towers, root tenants; Stage 2's rectilinear Overcrowding-era building as a standing architectural confession)
- Sensory Profile — **Done** (Finding IX — adds **windbells** and the constant arm's-height foliage contact)
- Export Culture — **Done** (Finding X — **cast windbells** and rooted stock give Cancer real physical exports, not only expertise)
- Religious/Philosophical Landscape — **Done** (Finding XI — "Keeping," the Ofrenda, and **the problem of the unkept**: adoption of lapsed Keepings, and the refusal to ritualize final failure)
- Fashion — **Done** (Finding XII — general-population; irregular non-tailored silhouette, visible mending, **the split token**)
- Arcanet Culture — **Done** (Finding XIII — oral/social general baseline, **the posted-outcomes record**, Mother's Circuit correctly scoped as caregiving-robot-specific)
- Visitor Experience / Transition — **Done** (Finding XIV — **a term of shared work**, then simply staying)
- Ordinary Daily Life — **Done** (Finding XV — **Attunement** as the district's most-performed daily practice, entirely non-grief)
- Thematic Breadth Catalog — **Done** (Finding XVI — The Turning, The Long Room, **The Long Shelf**, The Pit Gardens, The Foundry, votive forms, reach-band tools)
- Robot-Specific Culture — **Done** (Finding XVII, Phase 8 — robots hold most adopted Keepings because they outlive the households around them; first-pass, full Robot Universals triage still pending)
- Native Culture — **Done** (Findings XVIII-XX, Phase 7 — the **perpetual pot** and prepared-not-dispensed siligel; participatory rather than performative music; the outcome notice as the district's only literary form; Paired-Creche-derived human-robot intimacy plus the Mother's Circuit asymmetry; **the counterculture of those who decline to be cared for**, and Cancer's inability to hear refusal as anything but a symptom; three holidays including the deliberately unserious **Reach Day**)
- Cross-district consequences — **Done** (Finding XXI — tower venting into shared enclosed air; windbells vs. Taurus quiet hours resolved as an indoor-hung quieter variant; Long Room vs. Threshold Waiting Rooms distinguished)
- **QA — Completion Check: PASSED** (all 8 gates, `Phase_Instructions/00c_Completion_QA_Checklist.md`, recorded at the foot of the district's own file)
- **Why rewritten:** the first pass re-labelled existing canon rather than generating new culture, and "applied" the Real-World Basis method from memory instead of researching. Redone with actual research on all eight picks; **four had never been used at all** (Père Lachaise, Arcosanti, Findhorn, Hundertwasserhaus) and three of those four produced the file's strongest material. **This is the reference example for the other 12 districts** — see `Real-World_Basis_Extrapolation_Method.md`'s worked-example table.

### 02 — Taurus — **ALL 8 PHASES COMPLETE + QA PASSED (Phase 7 and QA added 2026-08-29)**

> **Correction, 2026-08-29.** This block previously read "ALL 8 PHASES COMPLETE (2026-08-16)" while listing only
> ten items, **none of which was Phase 7** — the phase was inserted into the Plan on 2026-08-16 and Taurus was
> never brought up to it. The completion claim was therefore false for two weeks. Phase 7 and the completion QA
> have now been run. **Leo's block below still carries the identical defect and the identical false claim.**
- Architecture — **Done** (Finding V)
- Sensory Profile — **Done** (Finding VI — extended the pre-existing Soundscape Finding III)
- Export Culture — **Done** (Finding VII)
- Religious/Philosophical Landscape — **Done** (Finding VIII — "The Recorded Bond")
- Fashion — **Done** (Finding IX)
- Arcanet Culture (dedicated) — **Done** (Finding X)
- Visitor Experience / Visitor-to-Resident Transition — **Done** (Finding XI)
- Ordinary Daily Life — **Done** (Finding XII, Phase 5)
- Thematic Breadth Catalog — **Done** (Finding XIII, Phase 6)
- Robot-Specific Culture — **Done** (Finding XIV, Phase 8 — first-pass; full Robot Universals triage still pending)
- **Native Culture — Done 2026-08-29** (Findings XV-XVII, Phase 7 — added retroactively; Cuisine incl. siligel, Music, Arts, Human-Robot Relations, Counterculture, Private Life, Municipal Holidays)
- **Zodiac Substrate Second Pass — Done 2026-08-29** (Findings XVIII-XXIII, Mode A per `Phase_Instructions/00e_Substrate_Application_Pass.md`; overlap check returned near-zero, so the pass was genuinely additive)
- **QA Completion Check — PASSED 2026-08-29**, Gates 1-8. Gate 1 failed on first run (`siligel`, `music`, `counterculture`, `holiday` all zero) and was fixed by Phase 7. `sport`, `game`, and `slang` remain honestly open.
- Second district to complete the full 8-phase process, and the second to pass QA.

### 03 — Leo — **ALL 8 PHASES COMPLETE + QA PASSED (Phase 7 and QA added 2026-08-29)**

> **Correction, 2026-08-29.** This block previously read "ALL 8 PHASES COMPLETE (2026-08-16)" while listing ten
> items, **none of which was Phase 7** — the identical defect corrected in Taurus the same day, and the one Taurus's
> pass flagged as remaining. **Gate 0 was written specifically to catch this and caught it on first use.**
- Architecture — **Done** (Finding V)
- Sensory Profile — **Done** (Finding VI)
- Export Culture — **Done** (Finding VII)
- Religious/Philosophical Landscape — **Done** (Finding VIII — formalizes the pre-existing Cymatics Reverence connection)
- Fashion — **Done** (Finding IX)
- Arcanet Culture (dedicated) — **Done** (Finding X — status/broadcast, not archive)
- Visitor Experience / Visitor-to-Resident Transition — **Done** (Finding XI)
- Ordinary Daily Life — **Done** (Finding XII, Phase 5)
- Thematic Breadth Catalog — **Done** (Finding XIII, Phase 6)
- Robot-Specific Culture — **Done** (Finding XIV, Phase 8 — first-pass; full Robot Universals triage still pending)
- **Native Culture — Done 2026-08-29** (Findings XV-XVII, Phase 7 — added retroactively; Cuisine incl. siligel, Music, Arts, Human-Robot Relations, Counterculture, Private Life, Municipal Holidays)
- **Zodiac Substrate Second Pass — Done 2026-08-29** (Findings XVIII-XXIII, Mode A; overlap check near-zero with one genuine partial, so the pass was additive)
- **QA Completion Check — PASSED 2026-08-29**, Gates 0-9. Gate 0 failed (see correction above); Gate 1 failed with **twelve of sixteen categories at zero**, including `music` at 1 in the performance district; **Gate 9 failed and produced Finding XX**. `sport`, `game`, `slang`, `funeral`, `elder`, `gender` remain honestly open.
- Third district to complete the full 8-phase process, and the third to pass QA.
- **Resolved during this pass, 2026-08-16:** the pending Leo Star War issue ([[project_leo_star_war_resolution_and_rename_pending]]) was fixed opportunistically — Findings II and IV in `Leo_Full_Extrapolation.md` (and the Mega_Init's Hard Facts row) were stale against the confirmed 2026-07-29 Combined Version and have been corrected. Per direct developer instruction, "The Star War" is not used anywhere in this file's new or corrected material — the replacement name itself remains undecided and deliberately deferred, referred to descriptively instead.

### 04 — Scorpio — **ALL 8 PHASES COMPLETE + QA PASSED (2026-08-29)** — *first Mode B district*

> **Gate 0 correction, 2026-08-29 — the inverse of Taurus's and Leo's.** This block previously listed
> Architecture, Sensory Profile and Export Culture as "needed" and the tracker counted Phase 1 at 3/13. **All
> three were already written** as Findings V-VII, tagged Phase 1, to full depth. The Plan was **under**-claiming.
> Gate 0 is therefore a reconciliation step in both directions, not only an anti-over-claiming one.

- Architecture — **Done** (Finding V, pre-existing)
- Sensory Profile — **Done** (Finding VI, pre-existing; **Gate 2 mask error corrected 2026-08-29**)
- Export Culture — **Done** (Finding VII, pre-existing)
- Religious/Philosophical Landscape — **Done 2026-08-29** (Finding VIII — names the shared premise under both schools)
- Fashion — **Done 2026-08-29** (Finding IX — corrects the mask scoping; masks are a small minority in-process practice, not district dress)
- Arcanet Culture (dedicated) — **Done 2026-08-29** (Finding X — maximum retention, minimum transmission; the injury ledger)
- Visitor Experience / Visitor-to-Resident Transition — **Done 2026-08-29** (Finding XI — cell admission, with the conflict geometry written in per Mode B)
- Ordinary Daily Life — **Done 2026-08-29** (Finding XII, Phase 5)
- Thematic Breadth Catalog — **Done 2026-08-29** (Finding XIII, Phase 6 — five picks researched at concrete level)
- Native Culture — **Done 2026-08-29** (Findings XIV-XVI, Phase 7)
- Robot-Specific Culture — **Done 2026-08-29** (Finding XVII, Phase 8 — first-pass)
- Substrate findings — **Done 2026-08-29** (Findings XVIII-XX, folded in as Mode B input rather than a bolted-on section)
- **QA Completion Check — PASSED 2026-08-29**, Gates 0-9. Gate 0 failed (under-claiming), **Gate 2 failed on pre-existing material** (the mask error, flagged by the developer), Gate 9 failed and produced Finding XIX. `sport`, `game`, `slang`, `gender` remain open.
- Note: Scorpio's diaspora composition is the Stage 2 Override case (Casey/Zukelli/Belgrano/Palmer City, grief-driven, not ordinary affinity) — Fashion and Religious/Philosophical content here should account for that same grief-driven character rather than defaulting to a generic treatment.

### 05 — Aries
- Architecture — needed
- Sensory Profile — needed
- Export Culture — needed
- Religious/Philosophical Landscape — needed
- Fashion — needed
- Arcanet Culture (dedicated) — needed
- Visitor Experience / Visitor-to-Resident Transition — needed
- Ordinary Daily Life — needed (Phase 5)
- Thematic Breadth Catalog — needed (Phase 6)
- Robot-Specific Culture — needed (Phase 8)

### 06 — Capricorn
- Architecture — needed
- Sensory Profile — needed
- Export Culture — needed
- Religious/Philosophical Landscape — needed
- Fashion — needed
- Arcanet Culture (dedicated) — needed
- Visitor Experience / Visitor-to-Resident Transition — needed
- Ordinary Daily Life — needed (Phase 5)
- Thematic Breadth Catalog — needed (Phase 6)
- Robot-Specific Culture — needed (Phase 8)
- Note: `Staging/07_Capricorn_Robot_Rights_National_Parallel.md` exists but is a labor/political-rights thread, not robot-*culture* content — confirmed not a substitute for the Phase 8 Robot-Specific Culture Finding, though it may be worth cross-referencing once that Finding is written.

### 07 — Aquarius
- Architecture **+** (has it)
- Sensory Profile **+** (has it)
- Export Culture — needed
- Religious/Philosophical Landscape — needed
- Fashion — needed
- Arcanet Culture (dedicated) — needed
- Visitor Experience / Visitor-to-Resident Transition — needed
- Ordinary Daily Life — needed (Phase 5)
- Thematic Breadth Catalog — needed (Phase 6)
- Robot-Specific Culture — needed (Phase 8)

### 08 — Libra
- Export Culture **+** (has it, but only in `README.md`/`Libra_Mega_Init.md` — promote into a proper
  Full_Extrapolation Finding as part of Phase 1, don't rewrite from scratch)
- Architecture — needed
- Sensory Profile — needed
- Religious/Philosophical Landscape — needed
- Fashion — needed
- Arcanet Culture (dedicated) — needed
- Visitor Experience / Visitor-to-Resident Transition — needed
- Ordinary Daily Life — needed (Phase 5)
- Thematic Breadth Catalog — needed (Phase 6)
- Robot-Specific Culture — needed (Phase 8)

### 09 — Gemini
- Arcanet Culture **+** (incidental mentions in Full_Extrapolation/Mega_Init/README — promote into one
  dedicated Finding as part of Phase 3, don't rewrite from scratch)
- Architecture — needed
- Sensory Profile — needed
- Export Culture — needed
- Religious/Philosophical Landscape — needed
- Fashion — needed
- Visitor Experience / Visitor-to-Resident Transition — needed
- Ordinary Daily Life — needed (Phase 5)
- Thematic Breadth Catalog — needed (Phase 6)
- Robot-Specific Culture — needed (Phase 8)
- Note: Gemini is the Stage 2 Override target for Zukelli specifically — same grief-adjacent consideration as Scorpio, narrower in scope.

### 10 — Pisces
- Architecture **+** (has it)
- Religious/Philosophical Landscape **+** (has it — the only district that does; use as the reference example when writing the other 12)
- Sensory Profile — needed
- Export Culture — needed
- Fashion — needed
- Arcanet Culture (dedicated) — needed
- Visitor Experience / Visitor-to-Resident Transition — needed
- Ordinary Daily Life — needed (Phase 5)
- Thematic Breadth Catalog — needed (Phase 6)
- Robot-Specific Culture — needed (Phase 8)

### 11 — Sagittarius
- Architecture **+** (has it)
- Arcanet Culture **+** (incidental mentions in Mega_Init/README — promote into one dedicated Finding as part of Phase 3)
- Sensory Profile — needed
- Export Culture — needed
- Religious/Philosophical Landscape — needed
- Fashion — needed
- Visitor Experience / Visitor-to-Resident Transition — needed
- Ordinary Daily Life — needed (Phase 5)
- Thematic Breadth Catalog — needed (Phase 6)
- Robot-Specific Culture — needed (Phase 8)

### 12 — Virgo
- Architecture — needed
- Sensory Profile — needed
- Export Culture — needed
- Religious/Philosophical Landscape — needed
- Fashion — needed
- Arcanet Culture (dedicated) — needed
- Visitor Experience / Visitor-to-Resident Transition — needed
- Ordinary Daily Life — needed (Phase 5)
- Thematic Breadth Catalog — needed (Phase 6)
- Robot-Specific Culture — needed (Phase 8)

### 13 — Hub
- Architecture — needed
- Sensory Profile — needed
- Export Culture — needed
- Religious/Philosophical Landscape — needed
- Fashion — needed
- Arcanet Culture (dedicated) — needed
- Visitor Experience / Visitor-to-Resident Transition — needed
- Ordinary Daily Life — needed (Phase 5)
- Thematic Breadth Catalog — needed (Phase 6)
- Robot-Specific Culture — needed (Phase 8)
- Note: the Hub's diaspora is almost entirely "overflow," not affinity-driven (per `District_Refugee_Diaspora_Composition.md`) — its Visitor Experience / Visitor-to-Resident Transition entry is likely the single most load-bearing of all 13, since the Hub's whole identity runs through people arriving without a natural first destination.

---

## Progress tracking

Each phase below gets checked off by category, across all 13 districts, before the plan moves to the next
phase — not by district. Mark complete only once every one of the 13 districts' relevant entries (accounting
for the "already has it" districts needing promotion rather than fresh writing) is written into its
`*_Full_Extrapolation.md`.

- [ ] Phase 1 — Architecture (3/13 done: Cancer, Taurus, Leo; 6 new + 4 existing confirmed sufficient remain)
- [ ] Phase 1 — Sensory Profile (3/13 done: Cancer, Taurus, Leo; 8 new + 2 existing confirmed sufficient remain)
- [ ] Phase 1 — Export Culture (3/13 done: Cancer, Taurus, Leo; 9 new + 1 promoted from Libra's README/Mega_Init remain)
- [ ] Phase 2 — Religious/Philosophical Landscape (3/13 done: Cancer, Taurus, Leo; 9 new + 1 existing, Pisces, as reference remain)
- [ ] Phase 2 — Fashion (3/13 done: Cancer, Taurus, Leo; 10 new remain)
- [x] Phase 3 — Arcanet Culture, dedicated section — **lens established** (Gemini treated as the network center each district's own finding is written relative to, per Phase 3 Step A, even though Gemini's own dedicated Finding hasn't been formally written yet) — 3/13 districts done: Cancer, Taurus, Leo; 8 new + 2 promoted (Gemini, Sagittarius) remain
- [x] Phase 4 — concept definition pass (Visitor Experience / Visitor-to-Resident Transition, one-time) — **finalized**, see `Phase_Instructions/04...md` §1
- [ ] Phase 4 — Visitor Experience / Visitor-to-Resident Transition (3/13 done: Cancer, Taurus, Leo; 10 new remain)
- [ ] Phase 5 — Ordinary Daily Life (3/13 done: Cancer, Taurus, Leo; 10 new remain; pre-existing TODO item, `Weekly_To-Do_-_Current.md` lines 107-118)
- [ ] Phase 6 — Thematic Breadth Catalog (3/13 done: Cancer, Taurus, Leo; 10 new remain; places/things/people-as-placeholders/settings per district)
- [ ] Phase 7 — Native Culture (4/13 done: Cancer, Taurus, Leo, Scorpio; 9 new remain — Cuisine incl. siligel, Music, Arts, Human-Robot Relations, Counterculture, Private Life, Municipal Holidays)
- [x] Phase 8 — lens decision pass (Robot-Specific Culture, theme/role-based) — **finalized**, see `Phase_Instructions/08...md` §1
- [ ] Phase 8 — Robot-Specific Culture (3/13 done: Cancer, Taurus, Leo, all first-pass only — full Robot Universals triage still pending per the "Planned follow-on" section above; 10 new remain)
- [ ] **QA Completion Check** (4/13 passed: Cancer, Taurus, Leo, Scorpio; 9 remain — `Phase_Instructions/00c_Completion_QA_Checklist.md`. **Four districts complete. Scorpio (2026-08-29) was the first Mode B run — substrate folded in as a first-pass input rather than bolted on — and is the reference example for that mode.** The remaining ten should run in **Mode B** — substrate as a first-pass input, folded into the phases as written, not bolted on afterward. **They do not enter clean:** each carries 4-7 pre-Plan findings from 2026-07-09 that predate the shadow, general-population, and research-first disciplines, and both Gate 9 failures so far were in exactly that kind of material — read and Gate-9 them first. See `Phase_Instructions/00e_Substrate_Application_Pass.md` §11b.)

Once all eight phases are checked complete, the districts are at genuine parity with the outer cities' template
on everything that legitimately applies to a district, plus the pre-existing Ordinary Daily Life prerequisite and
the Thematic Breadth Catalog — Local District Robot Culture can then begin the same way the outer-city version
did, on solid ground rather than in isolation.

---

## Planned follow-on (after all 13 districts clear all 8 phases): a full Robot Universals triage pass

**Developer instruction, 2026-08-16 — not yet started, explicitly gated on every district finishing all 8
phases first.** Cancer's own Phase 8 pass (`Cancer_Full_Extrapolation.md` Finding XVII) was run without loading
the complete *Robot Universals* reference text in full (`TepenianUniverseTimeline/Reference/Robot_Universals/`)
— it worked instead from Cancer's own already-established robot-population material plus the confirmed
Tepenia-Wide Robot Culture Canon, and said so honestly rather than overclaiming a full triage. Once every
district has been through all 8 phases once, run a dedicated second pass, district by district: go through
*Robot Universals* chapter by chapter and identify the specific shapes/forms each universal takes in that
particular district — the same **Universal-by-Universal Triage** step already described in
`Phase_Instructions/08_Phase_8_Robot_Specific_Culture.md` §3, just run properly against the complete text this
time, now that every district has a full Phase 1-7 foundation (not just Phase 5/6-level material) to triage
each universal against. This is a deliberate second look, not a correction of anything wrong in the first pass —
Phase 8's own first-pass findings (theme/role-based, grounded in each district's established material) remain
valid; this pass exists to catch whatever a proper universal-by-universal walk surfaces that a
material-first approach wouldn't.
