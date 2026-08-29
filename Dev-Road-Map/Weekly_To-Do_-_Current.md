# Weekly To-Do — Current

**Started 2026-07-23.** A short working shortlist pulled from the much larger `TODO.md` backlog — items the
developer wants to actually work through over the next several days. Each entry below cross-references its
full write-up in `TODO.md` for context; this file is the queue, not a replacement for the fuller entries.
When an item here is finished, resolve it in `TODO.md`/`DONE.md` as usual and strike it here (or clear the
file and start a fresh one for the next stretch of work).

---

## Active Threads as of the 2026-08-16 → 2026-08-24 outage stretch

- [ ] **STANDING HABIT — cross-check `Districts/Cross_District_Differentiation_Table.md` on every district pass,
  and keep it updated.** *(Developer instruction, 2026-08-29.)* Not a task to complete; **a habit to maintain.**

  **What it is.** One page giving each completed district's answer per category — capability shape, music,
  counterculture, records, food, transition, dissent grammar, shadow — so a new district can be checked against
  **one file** instead of by re-reading six or ten `Full_Extrapolation.md`s.

  **Why it matters more than it looks.** `00c` Gate 6(b) requires every new district to be checked for
  near-collisions against every district already finished. **That cost rises with each district, and it has
  already failed once**: the Power Core and the Yards were written a day apart and given nearly the same food
  custom — *feed someone after a bad shift without comment* — and the check did not catch it, because checking
  a sixth district against five predecessors by re-reading them is precisely the check that gets skipped when
  it is expensive. Both files now carry an inline distinction and the table records the miss.

  **The habit, concretely:**
  - **Before** writing a category for a new district, read that category's row. If the answer rhymes with any
    existing entry, either differentiate it **inline in the district's own finding** or change it.
  - **After** completing a district, add its column **in the same commit** as the pass.
  - **When a category reaches five or six entries and starts to feel crowded, add it as a new row** rather than
    waiting for a collision.

  **Why this is worth protecting:** the governing rule of the whole methodology is *never carry one location's
  answers into another — if two places produce similar-shaped answers, at least one is wrong.* **This table is
  the only mechanical instrument enforcing that rule**, and it will be most valuable exactly when there are
  enough districts that nobody can hold them all in mind — which is the point at which collisions become
  invisible and the districts quietly homogenize.

- [ ] **⚠ FULL graphify rebuild with semantic extraction — NOT `--update`. Diagnosed 2026-08-29.**
  Deferred by the developer to a later session; recorded here with the measurements so it is actionable rather
  than a reminder.

  **The problem is coverage, not configuration.** The enforcement config is already maximal — a `PreToolUse`
  hook in `.claude/settings.json` runs `graphify hook-guard` on `Bash|Grep` **and** `Read|Glob`, firing on
  essentially every lookup, plus the `CLAUDE.md` rule. **The graph is being consulted first and is returning
  bad answers.** Measured node counts in `graphify-out/graph.json`:

  | File | Lines | Nodes in graph |
  |---|---|---|
  | `District_Megasheets/01_Cancer/Cancer_Full_Extrapolation.md` | ~900 | **45** |
  | `Worldspace/Characters/Dolls/Character_Development_Methodology_-_DRAFT_Ideas.md` | 3,459 (17 books) | **1** |
  | `…_Villains_and_Antiheroes_-_DRAFT_Ideas.md` | 1,194 (4 books) | **7** |

  **The two largest extraction files in the repo are indexed at roughly 1/45th the density of a comparable
  district file.** Large consolidated files appear to be summarized into near-nothing by semantic extraction.
  **Real consequence, 2026-08-29:** a graph query for Weiland's twelve shadow archetypes returned *Shadowrun*
  and *Minmax Build* nodes, and I concluded the material was unextracted. It was — 585 lines of it, including
  all twelve names with full profiles. **The book was then partly re-mined from source unnecessarily.**

  **Two further findings from the same diagnosis:**
  - **Raising `--budget` does not fix it.** Tested at 8000 against the default ~2000 on the same query: same
    irrelevant start-nodes, still no hit. Truncation is a real but secondary problem; **coverage is primary.**
  - **`graphify update .` is AST-only and costs no API calls** — meaning **it adds essentially nothing
    semantically for a prose repo like this one.** If the repeated `/graphify .` runs took the update path,
    that would explain why they appeared to accomplish nothing. **A rebuild must run full semantic extraction.**

  **Also badly stale:** graph last built **2026-08-29 00:33**. None of that day's substantial new files —
  `00f_Review_Panel.md`, `King_Warrior_Magician_Lover_Extraction.md`, `Book_Extraction_Index.md`, or the Scorpio
  and Aries full passes — are in it at all (zero hits each).

  **Interim workaround already in place:** `Reference/Real-World/Book_Extraction_Index.md` makes all 23 book
  extractions findable without depending on the graph. **Grep the consolidated DRAFT files directly** rather
  than querying for their contents until the rebuild lands.

  **When rebuilding, worth testing:** whether splitting or chunking the two DRAFT files at extraction time
  produces usable node density, since their current representation is the single worst coverage gap in the
  graph.

Two parallel threads were in progress across a run of Claude weekly-limit resets coinciding with power outages
at the developer's home. Recorded here as a resume point in case of another outage.

- [x] **`/graphify` knowledge-graph build over the full GDD corpus — COMPLETE 2026-08-24**
  Built a full knowledge graph of this repo via the `graphify` skill: 2,763 files detected, 2,504 semantically
  extracted (259 confirmed legitimate empty dev-stub templates), yielding **9,128 nodes, 14,195 edges, 1,142
  communities**. Outputs: `graphify-out/graph.json`, `graphify-out/GRAPH_REPORT.md`, `graphify-out/graph.html`.
  Full checkpoint history (B1–B15 extraction, C0–C6 graph build) in `graphify-out/BUILD_PLAN.md`. Verified
  correct post-build (node/edge counts cross-checked against the report, cache re-confirmed at 2,504/2,763,
  no regression).

  **Superseded same day by a full `--update` catch-up run, also 2026-08-24, after the STP-06 "Hao" character
  work (below) landed:** incremental detection found 267 files changed since the above build (2 code, 265
  docs) — far more than just Hao's 7 files, since ~260 other docs across the repo had drifted out of sync with
  the graph. Ran the full 13-parallel-subagent semantic re-extraction, merged via `build_merge`, verified no
  real data loss (1,898/1,901 "missing" nodes confirmed as legitimate duplicate-ID cleanup where the source
  file is still represented elsewhere; the 3 genuinely at-risk nodes — Mountain Pass Airport and two Dome
  Fuji/Sanay concept-art images — backed up to `graphify-out/orphaned_nodes_backup_2026-08-24.json` before
  forcing the write). **Current state: 8,192 nodes, 14,027 edges, 1,235 communities.**

  **A real bug was hit and fixed during this run, worth remembering:** the rebuild initially wrote generic
  `Community N` placeholder labels over ~1,400 previously-curated community names. First-pass recovery
  attempt used `graphify`'s own `remap_communities_to_previous()` hub-overlap matching against the pre-update
  backup (`graphify-out/2026-08-24/.graphify_analysis.json` + `.graphify_labels.json`, both auto-preserved by
  graphify's own backup step) — but the first fix was itself subtly wrong: it checked "does an old label exist
  for this community's final numeric ID," not "did this ID arise from a genuine overlap match," so ~299
  communities with **zero real overlap** to anything old still coincidentally landed on an old ID and
  inherited a wrong, unrelated label. Caught by the developer explicitly asking to verify names actually match
  content. Fixed properly by re-deriving the match set directly (only crediting communities that appear in the
  greedy overlap-matching's `matched_new_ids`, not just "some old label exists at this ID") — **936 of 1,235
  communities got a verified, correct recovered label; the other 299 were left as honest generic placeholders**
  rather than guessed/borrowed ones, since they're genuinely new content with no prior name to recover.
  Spot-checked 10 of the 936 against their actual node content — all correct.

  **What the 299 generic ones actually are, for context:** overwhelmingly small clusters (113 are single-node,
  54 are pairs) totaling 1,203 nodes, almost entirely the ~250 previously-unindexed doll-character template
  stub files (`Personal_Background/Timeline.md`, `Loyalties.md`, `Relationships.md`, etc. — mostly boilerplate
  `[Character Name] — X` scaffolding with no real content yet) that this update run was the first to ever
  process. Not mislabeled real content — genuinely new, mostly-empty clusters that never had a name to recover
  in the first place.

  **⏸️ DEFERRED TO SATURDAY 2026-08-29 — full labeling scan, not yet started.** Developer requested a full,
  complete scan of the entire graph JSON to verify/assign accurate labels across the board — not just filling
  in the 299 generic ones, but actually re-checking the whole label set for correctness, since the bug above
  proved labels can silently drift wrong. **Why deferred:** developer is at 94% of their weekly Claude Pro
  model allotment as of Tuesday 2026-08-25, too tight to safely start a task this size. **Why Saturday
  specifically:** developer is switching from Pro to the Max5x plan this Saturday (2026-08-29) — see
  `[[project_tier_switch_opus_2026_08_29]]` memory — which resets the budget picture entirely (Opus access,
  5-hour session windows, much larger weekly allotment). **Resume point:** `graphify-out/graph.json` currently
  has 1,235 communities; 936 have verified-correct recovered labels, 299 have honest generic placeholders. The
  task on Saturday is a genuine full pass — re-verify the 936 (spot-check basis established this session
  showed all correct, but only 10/936 were actually checked) and properly name the 299 new ones (per Step 5 of
  the `/graphify` skill: read each community's node list, assign an accurate 2-5 word label from actual
  content, regenerate `graph.json`/`GRAPH_REPORT.md`/`graph.html`). No GEMINI_API_KEY/GOOGLE_API_KEY is
  configured, so this labeling has to be done by the host assistant reading community contents directly
  (as this session's `graphify label .` run confirmed: "no LLM backend configured, keeping placeholders").

- [ ] **District Culture Development Plan — 3/13 districts through all 8 phases, 1/13 QA-passed**
  `Worldspace/Locations-and-Levels/Concordia-City/Districts/District_Culture_Development_Plan.md` — an 8-phase
  gap-closing pass (Architecture, Sensory Profile, Export Culture, Religious/Philosophical Landscape, Fashion,
  Arcanet Culture, Visitor Experience, Ordinary Daily Life, Thematic Breadth Catalog, Native Culture incl.
  siligel cuisine/music/arts/human-robot relations/counterculture/private life/municipal holidays,
  Robot-Specific Culture) across all 13 Concordia districts, closing the same template gaps the outer cities
  already have filled. **Status:** Cancer, Taurus, and Leo have all started; **only Cancer has completed
  Phase 7 (Native Culture) and passed the completion QA gate** (`Phase_Instructions/00c_Completion_QA_Checklist.md`).
  Taurus and Leo predate Phase 7, the research-first rule, and the general-population-not-professional-role
  discipline, and have not been QA'd. **10 districts** (Aquarius, Aries, Capricorn, Gemini, Libra, Pisces,
  Sagittarius, Scorpio, Virgo, and the remaining district) haven't been started at all. See the plan file's
  own checklist (bottom section) for exact per-phase counts. **Explicitly gated follow-on, not yet started:**
  a full Robot Universals triage pass, district by district, once all 13 clear all 8 phases.

  **⚠️ AUDITED 2026-08-24 — read `Districts/District_Culture_Plan_Audit_2026-08-24.md` before resuming this.**
  A full verification pass was run over the plan as applied to Cancer, comparing the discarded first-pass
  results against the 2026-08-16 from-scratch rewrite and checking every load-bearing citation against source.
  **The rewrite holds up** — all 8 real-world picks genuinely researched, Gate 1's mechanical check passes, the
  diaspora arithmetic and every cross-file citation verified accurate, and Findings I-VII integrate cleanly
  with VIII-XXI with no contradictions. **Issues found, none fatal**, and per developer instruction 2026-08-24
  **left unfixed for a closer look together on Saturday**:

  - **The Plan file + `Phase_Instructions/` phase-count and status drift.** Phase 7 (Native Culture) was
    inserted 2026-08-16 and Robot-Specific renumbered 7→8, but the downstream cleanup was never swept. A full
    grep classifies **19 items into five categories** (full tables with exact file:line and before/after text
    are in the audit file, §Issue 1&2):

    - **⭐ Category D — 3 false status claims. FIX THESE FIRST, BEFORE ANYTHING ELSE IN THIS ITEM.** These are
      not counting errors; they are factually wrong statements about project state, sitting in the exact files
      a new session opens to orient itself.
      · **D1** `Phase_Instructions/00_Index.md:62-66` — *"No other district/phase combination has been executed
      yet as of this writing."* Cancer has all 8 phases **and** a passed QA gate; Taurus and Leo have all 8 each.
      · **D2** `Phase_Instructions/08_Phase_8_Robot_Specific_Culture.md:104` — *"All 13 districts: blocked
      pending Phases 1-7. Do not attempt Phase 8 for any district…"* Read literally, this forbids work already
      done three times.
      · **D3** *(most harmful item in the whole audit)* same file, **:137**, in a section literally headed
      **"8. Worked example"** — *"None yet … no district has cleared that gate."* **Cancer's Finding XVII is a
      completed, QA-passed Phase 8 worked example.** A Saturday session opening this file to start a new
      district would think it was pioneering the phase from nothing, and would lose the Swap Test framing, the
      Inheritance/Iceberg tagging convention, and the honest-scope-note pattern Cancer already established.
    - **Category A — 8 genuinely stale phase counts, safe to change.** Per-district headers in the Plan (lines
      336, 352, 363, 365, 376, 538) plus `00_Index.md:9` and `00b_General_Population_Discipline.md:3`.
      Plan line 538 contradicts its own section heading three lines above it.
    - **Categories B + C — 7 strings that are CORRECT. DO NOT TOUCH.** Six are `Phases 1-7` meaning *Phase 8's
      prerequisite range* (a correct range, not a stale total); one is Plan line 14's historical re-audit note,
      which describes the pre-renumber world and **is the explanation for why the 8th phase exists at all.**
    - **Category E — 1 pointer needing a decision** (`01_Phase_1_...md:27` names a block that doesn't exist
      under that name).

    **A bulk find-and-replace is unsafe** — it would corrupt all seven Category B/C strings, *and* would still
    miss D1 entirely, since D1 contains no phase-count string to match on. Hand-fix only.
  - **Finding XII's palette** cites the diaspora file for "warm tones" content that **does not exist there**
    (zero colour/palette hits in that file), and sits in mild tension with the Mega-Init's established
    white-and-green palette.
  - **`Cancer/README.md`** bills itself as the "Complete Megasheet" but was **compiled 2026-07-09** and is
    missing all of Findings VIII-XXI — ~90% of the district's cultural content. Needs a decision on whether
    district READMEs are meant to be periodically recompiled.
  - Minor ordering/cosmetic items, and one haze-mechanism nuance worth a deliberate confirm.

  The audit file carries exact file:line references with before/after text, explicit **do-not-change** lists
  with reasoning, the six carried-forward open items from Cancer's own file, and a recommended sequencing —
  including **audit Taurus and Leo against the same checklist before extending the plan to new districts**,
  since both are marked complete but have never passed the QA gate.

- [ ] **⭐ SATURDAY 2026-08-29 — build the universal Cultural Synthesis Methodology instruction set**
  *(Developer instruction, 2026-08-24. Deliberately not started — no sufficient token window left this week;
  this is Opus work, gated on the Pro→Max5x switch, see [[project_tier_switch_opus_2026_08_29]].)*

  **The deliverable:** take the cultural synthesis methodology already expanded and proven on the **Cancer**
  district and generalize it into a **massive, intricate, repeatable instruction set that works for any
  setting** — any of the 13 Concordia districts, any of the 35 outer Tepenian cities, DLC locations, and
  **possibly orbital-infrastructure settlements** as a third, genuinely different setting class.

  **Why now and not earlier:** Cancer is the first location taken all the way through with real research, the
  general-population discipline, the generative toolkit, and a passed QA gate — so for the first time there is
  a complete, verified worked example to generalize *from* rather than theorize about. Its audit
  (`Districts/District_Culture_Plan_Audit_2026-08-24.md`) confirms the pass holds up, which is what makes it
  safe to treat as the reference standard.

  **What already exists and feeds this — most of the raw material is written, it needs assembling:**
  - `Worldspace/Locations-and-Levels/Cultural_Synthesis_Techniques.md` — **already scoped deliberately
    general** ("Concordia districts, the 35 outer Tepenian cities, DLC locations, or a location in any future
    project"). 14 named techniques, each a *question with a structure*, each with a divergence table. Has a
    governing filter (Characteristic Plausibility) and a player-facing test. **This is the core; the new
    instruction set should be built around it rather than duplicating it.**
  - `Worldspace/Locations-and-Levels/Real-World_Basis_Extrapolation_Method.md` — its sibling: supplies the raw
    material (concrete web research on a location's real-world influence picks) that the techniques operate on.
  - `Districts/Phase_Instructions/` — 11 files: `00_Index`, `00b_General_Population_Discipline`,
    `00c_Completion_QA_Checklist`, and `01`–`08` per-phase how-tos.
  - `Districts/District_Culture_Development_Plan.md` — the *what* and *what order*, incl. the 32-section
    template audit and the phase-dependency reasoning.
  - `Districts/00b_Two_Stage_Methodology.md` — Stage 1 (organic pre-war formation) vs Stage 2 (war fallout).
  - `.../City_Megasheets/City_Megasheet_Compilation_Guide.md` — the **outer-city** master pipeline
    (synthesize → invent → cross-reference) that the district plan was itself mirrored from.
  - `.../Local_Cultures/CITY_CULTURE_TEMPLATE.md` — the 32-section template.
  - `.../Local_Robot_Culture_Methodology/` — 4 files, the outer-city robot-culture parallel.
  - **Cancer's own `Cancer_Full_Extrapolation.md`** — the QA-passed worked example, Findings VIII-XXI.

  **The key structural insight to build on:** there are already **two parallel instantiations** of the same
  underlying method — the outer-city Megasheet pipeline and the district 8-phase plan — and the district one
  was *explicitly mirrored from* the city one. Two independent instantiations of one method is exactly the
  raw material for abstracting a general third. The real work is separating **what is genuinely universal**
  (the technique toolkit, the general-population discipline, the Swap Test, the phase-dependency logic, the
  "invent, but traceable to something established" posture, the QA gates) from **what is setting-specific**
  (the 32-section template's per-setting Covered/Phase/Absorbed/N/A classification, Concordia's enclosed-air
  shared-environment consequences, the Arcanet-culture phase, the district-vs-city Visitor Experience framing).

  **⭐ THE GOVERNING ARCHITECTURAL CONSTRAINT — developer instruction, 2026-08-29.** This methodology must work
  for **any location, any setting**: a Concordia district, one of the 35 outer cities, a state or country, an
  orbital-infrastructure location, or something not yet invented. **Different location types do not have the
  same base information available**, and the method must never assume a substrate that only some settings have.

  Build it as **three separable layers**:

  1. **The universal core** — the questions every location must answer, the generative techniques, the binding
     disciplines, the QA gate. This layer is the same everywhere and must reference **no** type-specific input.
  2. **A pluggable input layer** — whatever substrate that location type happens to have. This varies
     enormously, and the core must degrade gracefully when a given input is simply absent:
     - *Concordia districts:* the **zodiac substrate** (`Districts/Zodiac_Personality_Substrate/`), the
       Enneagram group assignment, `District_Refugee_Diaspora_Composition.md`, `Historical_Pressures.md`
     - *The 35 outer cities:* real-world station heritage, `District-Inspirational-Influences.md`-style picks,
       BAS READER climate data, `Official_Population_Census.md`, founding-nation tiers
     - *Orbital settlements:* closed-environment constraints, population origin, minimal-inter-location-travel
       — and **no real-world analog and no zodiac**
     - *States/countries:* not yet defined
  3. **The output template** — also type-varying (the 32-section city template vs. its district adaptation).

  **The zodiac is the worked example of why this matters.** It applies to **Concordia's 13 districts and
  nothing else** — no city, country, or orbital location draws on it. If it leaks into the universal core, the
  method silently assumes a 12-fold structure with built-in aspect geometry that no other setting has, and
  produces nonsense the moment it is pointed at a city.

  **Related trap, worth stating explicitly:** the zodiac substrate is *unusually* productive — it generated the
  Concordia accountability finding, the dignity-based flaw generator, and a complete inter-district conflict
  geometry. That productivity is tempting to generalise from, and doing so would be a mistake: it comes
  precisely from the rigid 12-fold structure and pre-existing relational geometry that make it non-portable.
  **Generalise from the *questions* it answered, never from its structure.**

  **The orbital case — developer clarification, 2026-08-24. An earlier draft of this note framed this as the
  methodology's hardest blocker on the grounds that orbital settlements have no real-world orbital analog to
  research the way Epidaurus or Arcosanti were researched. That framing was wrong and is corrected here:
  orbital settlements do not need other orbital settlements to derive a basis from. It was never an obligatory
  input.** What the derivation actually needs is three things:

  1. **Who lives there** — the population itself.
  2. **What sort of culture — more precisely and more in-universe-consistently, what sort of "neo-culture"** —
     they have.
  3. **How such a people would live, operate, function, and build their lives in what is effectively a closed
     environment**, with only minimal physical commuting/travel/transportation between separate orbital
     infrastructure locations.

  From those three, derive/extrapolate/synthesize the **localized orbital neo-cultures**. The closed-environment
  constraint set *is* the generative input — it does the job real-world comparanda do for a surface city. A
  population plus a specific set of conditions, run forward over generations, produces a distinct people; that
  is the same logic the neo-culture project already runs on, just with conditions supplied by the environment
  rather than by a real-world parallel community.

  **This is already anticipated in canon — do not build it from scratch.** `Neo-Races-and-Cultures/` is the
  established home for exactly this, and its README already scopes the orbital case as **Phase 3**: *"extend
  the same method to the orbital infrastructure population that carries the Cryptograph Helix timeline
  forward."* `Neo-Races-and-Cultures/Orbital_Cryptograph_Helix_Era/` exists as a **reserved, currently empty
  folder** waiting for it. Relevant existing method files: `_Method/Cultural_Iceberg_Method.md` (Hall's
  surface/deep-culture sorting — a sorting framework, so it applies unchanged regardless of where the raw
  material came from), `_Method/Human_Universals_Culture_Framework.md` (Brown's universals as a believability
  floor and a question-generator), and `_Method/City_Types_Reference.md`.

  **The neo-culture standard to hold to,** per that README: a genuine new people — *"a real, new 'third thing,'
  culturally distinct from any of the origin populations that fed into it,"* the way Taiwanese, Singaporean,
  Québécois, and Afrikaner are real distinct peoples rather than variant flavors of a parent nationality. The
  developer's own worked example is a *"Zhongshanese"* people. Orbital neo-cultures should meet the same bar,
  and should be **localized** — plural, differing between orbital locations, not one undifferentiated "orbital
  culture." The minimal-inter-location-travel constraint is precisely what would make them diverge from each
  other, so it is a generative asset, not just a hardship to describe.

  **Useful precedent for a setting that doesn't fit the standard input shape:** `Neo-Races-and-Cultures/`
  already flags **Concordia** as needing different treatment, since its population is drawn from every other
  city rather than having its own founding-nation composition. Orbital is the second such case. Whatever the
  general instruction set does about input-shape variation should cover both.

  **Real dependency to be aware of:** item 1 ("who lives there") is not yet answered — orbital population
  composition is its own unstarted, deliberately-reserved high-token task ([[project_orbital_composition]]).
  The methodology can be *built* without it, but an actual orbital neo-culture pass is gated on it.

  **Constraints that must survive generalization** (all currently binding, all learned the hard way):
  never carry one location's answers into another (if two places produce similar-shaped answers to the same
  technique, at least one is wrong); general population by default, narrow professional/ritual cases scoped
  explicitly; actually run the research rather than working from memory; the template is a **floor, not a
  ceiling** (new religions/factions/whole new categories are legitimate discoveries); and new work that
  contradicts old work must **say so in the text** rather than silently rewriting canon.

---

## This Week's Absolute Top Priority *(set 2026-08-09, through ~2026-08-16)*

Three items the developer named as the most direly urgent work of the week, in this order. See
`project_weekly_top_priorities_2026_08_09` memory for full context — these take precedence over everything else
in this file, including the rest of "High Priority" below, until done or explicitly reprioritized.

- [ ] **1. Historical vignette audit against Robot Universals + national canon — starting 2026-08-12**
  Take the completed *Robot Universals* reference book (`TepenianUniverseTimeline/Reference/Robot_Universals/`)
  together with everything now known about the country/national canon, and re-check the existing historical
  vignettes to see whether they still hold up — and whether they can now be improved given everything learned
  since they were written. Independent of items 2-3 below; can run in parallel with them. **Developer confirmed
  2026-08-11 this is starting tomorrow (2026-08-12).**

- [x] **2. Synthesize a working character-creation methodology model — COMPLETE 2026-08-09, see `DONE.md`**
  `Worldspace/Characters/Dolls/Character_Development_Methodology_-_DRAFT_Ideas.md`'s brainstorm is now a full
  5-stage pipeline (`Methodology/01`–`05`) plus a scale-driven `00a`/`00b` intake layer, with
  `00_Overall_Process_Scaffold.md` refreshed to match. Full writeup in `DONE.md`. Unblocks item 3 below.

- [ ] **3. Re-pass existing Companion/Romance questlines using the new methodology**
  Once item 2 produces a working model, run it against the Companion and Romance questlines already written
  for the existing Dolls, to check whether they still hold up and whether they can now be improved with the
  sharper toolkit. Depends on item 2's output. Broader in scope than the existing "Doll Character Spec /
  Companion-Romance backstory depth" entry further down (which lists only the six companions still missing
  this pass entirely) — this is a re-pass across *all* existing companion/romance questlines, not just the
  unfinished ones.

---

## High Priority

- [x] **DLC city Physical Infrastructure deep-dive — Methodology #1 AND Methodology #2 COMPLETE for all 34 non-Byrd cities**
  Completed 2026-07-30, directly following Byrd's own deep-dive (`Byrd_Physical_Infrastructure_Attributes.md`,
  80 attributes/57 Findings) — the source of `DLC_City_Under_Questline_Design_Method.md`'s own Input 9.
  Byrd got this treatment because it's a single-city DLC carrying full internal complexity alone; every other
  DLC city across all 5 subnets has now gone through the identical two-part process. **Methodology #1 (Base
  Attributes)** — first-principles derivation from each city's own governing facts, then a cross-city
  comparison round. **Methodology #2 (Cross-Referenced Extrapolation Findings)** — combining those attributes
  against each city's own existing lore for multi-order-effect Findings, same "Combining → 2nd/3rd/4th-order
  effect" format Byrd's own file uses, appended directly into each city's own Attributes file. Depth scaled
  per city rather than uniform in every subnet: each subnet's own hub/story-anchor city (or split of 2-3
  cities, confirmed per-subnet against `DLC_Overview.md`, asking the developer directly whenever that file
  left the central location ambiguous) got Mawson-level depth; every other city got proportionate, moderate
  treatment reflecting its own existing depth, never a token pass. **Final totals — every city now has a
  `[City]_Physical_Infrastructure_Attributes.md` file combining both methodologies:**
  - **Mawson subnet:** Dome Fuji 16 Findings, Mawson 13 (deepest), Sayowa 7
  - **Mirny subnet:** Mirny 11 (deepest), Kunlun 8, Vostok 8, Casey/Davis/Shirayuki/Sinheung/Zhongshan 7 each
  - **Halley subnet:** Neumayer 11, Sanay 10, Troll 9 (three deep-treatment cities), Halley/Abowasa/Belgrano/
    Lazar/Princess Elisabeth 8 each
  - **Janbogo subnet:** Janbogo 10, Fort McMurdo 10 (two deep-treatment cities), Cape Adare/Denison/Dumont
    d'Urville/Scott 8 each, Zukelli 9
  - **Palmer subnet:** Palmer City 16 (deepest, single clean hub per `DLC_Overview.md`), Esperanza/Juan
    Carlos/Port Lockroy/Rothera/Sejong/Signy 8 each, Marambio 7

  This entire high-priority item is now fully resolved — the natural next step, whenever picked up, is
  actually running `DLC_City_Under_Questline_Design_Method.md` against this material (Byrd is still the only
  city confirmed ready to run it with zero fallbacks, but all 34 other cities now have real Input 9-equivalent
  material of their own for the first time).

- [ ] **The Long Night War's inciting incident — three identities still TBD**
  Core premise established 2026-07-04 (a diplomat assaulted a gynoid, killed in self-defense — she's Akina);
  the three specific identities involved are not yet chosen. See `TODO.md`'s "Decision Required" section.

- [x] **Capricorn's core injustice — RESOLVED 2026-07-29 as "The Narrow Door." This entry was stale; corrected 2026-08-29.**
  This tracker said "4 contenders shortlisted, none chosen" for a month after the decision was actually made.
  `Districts/Deep_Dives/06b_Capricorn_Alternative_Conditions.md` line 79 carries the confirmation, and
  `DONE.md` records it too — only this file was out of date. **The resolution is a composite of three
  independently-true mechanisms, not a single pick:** Option #2 (guild patronage over merit) + Option #7
  (calibration/scheduling drift), together called **nAlpha**, with Option #8 (a physical master-workstation
  ceiling mistaken for policy) layered on top as a separately-true condition. The layers compound rather than
  merely coexist — scarcity turns nAlpha's mild bias into near-total exclusion, and the resulting homogeneous
  master pool is the only body with authority to recalibrate the schedule or fund an expansion, so neither ever
  happens. **The distinctive result: the injustice is invisible from the inside, not merely unaddressed** —
  each layer looks like an ordinary, reasonable problem of its own kind.
  *(Note: `nAlpha` is real project vocabulary — part of an nAlpha-through-nEpsilon option-combination naming
  convention also used in `Deep_Dives/10c_Pisces_Black_Market_Origin.md`. It is not a typo; do not "fix" it.)*

- [ ] **Byrd↔Janbogo aviation refueling stop — needs a real fix**
  See `TODO.md`'s "Decision Required" section for the underlying problem.

- [x] **Cross-district non-malice audit — COMPLETE, actually finished 2026-07-29, see `DONE.md`**
  This line was stale — `Cross_District_Non_Malice_Audit.md` itself already stated all 9 of 9 items resolved
  and promoted, predating this Weekly To-Do file's own 2026-07-23 creation. Caught and fixed 2026-08-11.

- [ ] **Per-district inter-city conflicts — measure, assess, derive, and synthesize** *(flagged 2026-07-31)*
  Using `District_Refugee_Diaspora_Composition.md`'s own weighted composition per district, work through what
  "cultural conflicts" would plausibly arise (a) **between different refugee-diaspora populations sharing the
  same district** (e.g. two source cities whose established values or social norms genuinely clash, not just
  differ) and (b) **between a district's refugee-diaspora population(s) and that district's own native/local
  population and established culture**. This is a distinct pass from the diaspora file's own "brought with
  them" transplant framing (which is about what each community contributes) and from the Deep Dive diaspora
  findings (which chase implications, not necessarily friction) — this pass is specifically about identifying
  and naming genuine points of tension. Natural companion to the item below, and further raw material for
  Under-Questline generation once both passes exist.

- [ ] **Per-district inter-city friendships — measure, assess, derive, and synthesize** *(flagged 2026-07-31)*
  The positive counterpart to the conflicts item directly above. Using `District_Refugee_Diaspora_Composition.md`'s
  own weighted composition per district, work through what "cultural crossovers" — genuine common ground,
  not just peaceful coexistence — would plausibly arise (a) **between different refugee-diaspora populations
  sharing the same district** (e.g. two source cities whose established values or social practices actually
  reinforce or complement each other) and (b) **between a district's refugee-diaspora population(s) and that
  district's own native/local population and established culture**. Same distinction as the conflicts item:
  this is about identifying and naming specific, genuine points of connection — ways people would actually
  find common ground — not a repeat of the diaspora file's own "brought with them" transplant framing or the
  Deep Dive findings. Further raw material for Under-Questline generation once both passes exist.

- [ ] **Per-district ordinary daily life — measure, assess, derive, and synthesize** *(flagged 2026-07-31,
  starting 2026-08-12)*
  Go through each of the 13 districts and work out what an ordinary resident's actual day-to-day life is
  like — daily routines, mundane concerns, personal struggles, and forms of personal escapism/downtime —
  distinct from whatever that district's own defining civic identity or institutional purpose is. Explicit
  example from the developer: Scorpio residents cannot plausibly spend every waking moment in a death ritual
  confessing their grief; people have lives outside of a district's headline function, and those ordinary
  lives are currently underexplored across the corpus. This is a third, distinct pass alongside the conflicts
  and friendships items directly above — not about inter-community dynamics at all, but about what any single
  resident's own life actually consists of day to day. Further raw material for Under-Questline generation
  (and general NPC/character writing) once all three passes exist. **Developer confirmed 2026-08-11 this is
  starting tomorrow (2026-08-12), alongside the vignette audit above.**

- [ ] **District Main vs. Under-Questline candidates — generate more** ⭐ *(unblocked 2026-08-08 — see below)*
  Structure and both governing files (`District_Main_Questlines.md`, `District_Under_Questline_Design_Method.md`)
  are established; each district currently has only its *first* main-questline candidate. Main questlines:
  generate several candidates per district using the existing Internal-Conflict format, then narrow to
  exactly one. Under-Questlines: generate a floor of 5 (ideally 15-20) per district, anchored to a
  "significant starting point" (a named figure or a data-point at a significant location) — and, unlike main
  questlines, **keep all of them**, no narrowing. See `project_district_questline_production_workflow`
  memory for the full workflow. **Updated 2026-07-31 — new input material ready:** `District_Refugee_Diaspora_Composition.md`
  (weighted diaspora composition + specific named cultural transplants per district) and the matching
  2026-07-31 diaspora-informed extension of all 13 `Deep_Dives/[NN]_[District]_Deep_Dive.md` files (4-5 new
  findings each) give this generation pass real, specific, named hook material it didn't have before — see
  `TODO.md`'s own new entry for the full picture. **This item was deliberately held pending a thorough robot
  culture foundation, per the developer's own explicit sequencing decision — that foundation (the "Robot
  Universals" reference book, `TepenianUniverseTimeline/Reference/Robot_Universals/`) is now complete as of
  2026-08-08, so this is unblocked and ready to actually run.** Not yet run.

- [ ] **Doll Character Spec / Companion-Romance backstory depth — psychological depth and inner conflict**
  ⭐ *(unblocked 2026-08-08, same reason as above)*
  Also deliberately held pending the robot culture foundation — much of what the Character Spec and
  Companion/Romance Fill-In sheets ask about (kinship, build, personality formation) was unresolved for
  robots specifically until Robot Universals was finished. Now unblocked. Relevant material: the fill-in
  templates themselves (`Worldspace/Characters/Dolls/Character_Spec_Fill-In_Sheet_Template.md`,
  `Worldspace/Characters/Dolls/Companion_and_Romance_Questline_Fill-In_Sheet_Template.md`, and the composite
  `z-template/` folder), and TODO.md's own existing "Remaining named Doll characters — personality and
  backstory development" entry (Medium Priority — Character Development) listing the six companions still
  needing this pass: Kendra Heinrich, Meyzan Yocazhda, Michelle Stanton, Salagéa Aparast, Vosora Lashár
  Tanslock, and Calethina.

- [x] **Character Development Methodology — psychological depth & inner conflict, instruction sheet — COMPLETE
  2026-08-09** *(flagged 2026-08-08)*
  Duplicate of Top Priority item #2 above — same gap, same resolution. See `DONE.md`.

- [ ] **Villain/Anti-Hero supplement sheet — extraction complete 2026-08-11, organizing pass still open**
  A second, separate document specifically for villains and anti-heroes, sitting alongside the main
  character-creation methodology rather than replacing or forking it — antagonist/anti-hero design has
  distinct concerns (irredeemability thresholds, sympathetic-villain calibration) that don't map cleanly onto
  the protagonist/companion-focused arc machinery the main methodology is built around. **This line was stale**
  (said "not yet started — no file exists yet"): the file
  `Worldspace/Characters/Dolls/Character_Development_Methodology_-_Villains_and_Antiheroes_-_DRAFT_Ideas.md`
  exists (1194 lines) and **all four queued books are now fully mined** — *Bullies, Bastards And Bitches*
  (Morrell, all 12 chapters + appendix), *Fallen Heroes: Sixteen Master Villain Archetypes* (Cowden, full
  book), *The Anti-Hero in the American Novel* (Simmons, all 4 chapters + Conclusion), and *Heroes and
  Anti-Heroes in Medieval Romance* (Cartlidge, all 14 chapters + Introduction, finished 2026-08-11). Two
  further candidates (*The Biology of Horror*, Morgan; *Sixguns and Society*, Wright) are deliberately
  deferred, not forgotten. **What's actually still open:** the file's own status line still reads "pure
  brainstorm, not yet organized into an actual instruction sheet" — the extraction is done, the organizing
  pass into a real structured document is the one remaining piece of work. See
  `project_villain_antihero_supplement_sheet_flagged` memory (also due for a refresh).

---

## 2026-08-01 Backlog Batch

Pulled from `TODO.md`'s "Large backlog batch — flagged 2026-08-01" entry — see there for the full write-up
per item. Everything from that batch is included here **except** "expand upon individual city history
specs," which stays in `TODO.md` only for now.

**Combat & systems mechanics**
- [ ] **Sneaking and line-of-sight** — stealth/detection mechanics not yet designed.
- [ ] **More weapons** — expand the current weapon roster.
- [ ] **Armor and clothing** — a system for this doesn't yet exist.
- [ ] **Faction outfitting** — what specific factions actually wear/carry, distinct from the general
  armor/clothing system above.
- [ ] **Real-world scientific basis for BG3 damage types** — what objects/items would cause the
  scientifically-supported equivalent of each BG3 damage type (and comparable relative amounts), and what
  kind of setting each would characteristically be found in. Ties into `Per_City_Weapons`/`Damage_Types.md`.

**Worldbuilding — civic life & economy**
- [ ] **The actual legal mechanisms of how Tepenia deals with criminals** — courts, arrest, enforcement
  procedure; more detailed than the existing 3-tier outcome framework (`project_tepenian_criminal_justice_system`
  memory).
- [ ] **What kinds of festivals exist, generally** — beyond what's already scattered per-city/per-district.
- [ ] **Are there any homeless people in Tepenia**, and if so, what does that look like.
- [ ] **Where do cities/districts actually get their water.**
- [ ] **What standard is Tepenian currency actually based on** — deliberately the first domino; the actual
  *name* (see the separate "National currency name and mechanics" entry above/below) is downstream of this,
  not decided in parallel. Also: don't use the word "scrip" in new writing — see that entry for why.
- [ ] **General standards of living, and the cost of things.**
- [ ] **What does it actually mean to be "rich" in Tepenia** — follows directly from the item above.
- [ ] **How is sewage and septic waste treated/handled.**
- [ ] **What other food-producing locations exist**, beyond what's already established (Davis's breadbasket
  role, etc.).
- [ ] **A general accounting of what currently exists across the project as flagged "side-content."**

**Documentation**
- [ ] **Go in and actually comment the code** — including pseudocode.

---

## Medium Priority

- [ ] **Companion Forbidden Traits pass — 3 companions remain, 1 in-progress**
  IT-021 [Fenny], FW-25 [Pink Lucy], and Lyuba Baranova all have existing romance stat gates and just need
  this pass done. Majyao Bisyugota is in-progress — Demagogue confirmed, but a new trait ("Broad Strokes,"
  `Character-Creation/Traits.md`) still needs its bonus finalized before her list can close out. See
  `Core-Mechanics/Forbidden_Trait_Design_Method.md` for the full process and `TODO.md`'s own tracking entry.

- [ ] **Implant procedure cost** — the reputation-gate requirement is set (`Permanent_MACHINE_Stat_Increases.md`);
  just needs an actual credit amount decided.

- [ ] **Block Stance's exact numbers** — AP cost and DT/DR bonus size (`Combat/Block_Stance.md`). Resolving
  this also unlocks finalizing Unstoppable Force's own effect.

- [ ] **Cold/storm gradient numbers for `World_Map_Boundaries.md`** — the Engine-gated mechanism is chosen;
  just needs actual figures.

- [ ] **Starting skill-point formula** — FNV's real formula is verified (2 + 2×stat + 0.5×Luck); just needs a
  decision on what (if anything) replaces the Luck term for Inner Tepenia.

- [ ] **Tentative Factions — design all 9 (including sub-factions)**
  FD-3 Veilkeepers, FD-4 Lattice/Bonded Lattice, FD-6 Reclaimers, FD-7 The Vigil (pending keep/redesign/cut
  decision), FD-8 Siligel Purists, FD-9 Neon Nomads, FD-10 Chorus of the Deep, FD-11 Memory Weavers, FD-12
  Iron Gardeners. See `Storyline/Endings/Secret-Endings/Faction_Devotion_Endings.md`.

- [ ] **National Holidays — various kinds**
  `Worldspace/National_Holidays.md` has 4 categories scaffolded (Civic/National, Persisted Aesthetic,
  Internationally-Transcendent, Celestial/Faction-Specific). Category 4 is the least resolved and has its
  own flagged dedicated-investigation need (which faction(s), what astronomical event, Kunlun-centered or
  not) — but scope for this pass is left open per the developer's own phrasing, not narrowed to Category 4
  alone.

- [ ] **Doll Enneagram gaps — review pass**
  **Momo (TCY-45) resolved 2026-08-11:** 4w5 Main + 9w1 Undercurrent (the project's first confirmed
  Undercurrent, see `Worldspace/Enneagram/Undercurrents.md`), Instinctual Subvariant still undetermined for
  both. **Eirwyn "Eira" Cardoss also resolved 2026-08-11:** 5w4 Main (Social) + 3w4 Undercurrent (Sexual), ~55%/45%
  split (a real deviation from the ~80/20 working baseline) — the first doll typed against the Off-World
  template, which had no Enneagram field until now. **HKD-172 also resolved 2026-08-11** (not
  originally on this list, but was also untyped): 9w8, Social. Two characters remain missing a type entirely:
  Maria (FR-03) and **Calethina** — flagged in the original TODO entry as "no standard README,"
  which is now stale (she has a full master `README.md` as of this session) but she still has no formally
  assigned Enneagram type, so worth confirming whether that's still a real gap or already implicitly
  answered by everything now written about her. Two missing a subvariant: Charlene (XT-17, 5w4) and Angelina
  (XT-21, 7w8). Broader pass: confirm existing subvariant assignments are correct across all typed dolls
  before Phase 3 personality work begins. Don't design companion perks, attraction profiles, or romance
  gates for the type-missing characters until this is resolved.

- [ ] **Lyuba Baranova — classify as anti-hero when her personal questline design begins** *(flagged 2026-08-11)*
  Additional lens layered on top of her standing recruitable/romanceable companion status, not a replacement
  for it. Apply the now-fully-mined `Character_Development_Methodology_-_Villains_and_Antiheroes_-_DRAFT_Ideas.md`
  supplement (Morrell, Cowden, Simmons, Cartlidge all complete) when charting her arc. Note also written
  directly into her own `README.md`'s Design Notes & Open Questions. She's not yet in active questline
  design — this is a forward flag for whenever that work actually starts (see the personal-questline queue in
  `TODO.md`: Fenny, Lyuba, Rui, plus DLC companions).

- [ ] **Wire existing methodology files to the new Enneagram entry point** *(flagged 2026-08-09)*
  `Worldspace/Enneagram/README.md` now exists as the designated link target for any character-creation
  methodology that needs Enneagram material (see `project_enneagram_deep_dive_folder_plan` memory). Not yet
  actually wired in anywhere — the Stage 1–5 pipeline in `Worldspace/Characters/Dolls/Methodology/` (Stage 3 in
  particular) and the `TepenianUniverseTimeline` seed-to-README process still don't cross-reference it.
  Deliberately deferred; low-risk, additive, easy to pick up whenever.

**Housekeeping done alongside this list, 2026-07-23:** Juan Carlos's post-Long-Night-War status — already
resolved in-session (Destroyed, targeted for its archive/customs function) but still sitting as an open
checkbox in `TODO.md` — has been moved to `DONE.md`.

---

## Long-Term Priority

- [ ] **Re-number the DLCs by release order — narrowed to 2 candidate orders, 2026-07-23, decision deferred**
  Both written into `Storyline/DLC_Overview.md`'s "Release Order vs. DLC Numbering" section. South Pole
  (DLC 1) confirmed last either way; release order and development order are explicitly decoupled, so neither
  candidate is blocked by the 4 subnet DLCs still lacking a real main-questline anchor.
  - **"Geometric"** — traces the continent's coastline in one rotational sweep from Concordia's own Janbogo
    subnet, nearly closing the loop before diving inward to the South Pole (the continent's actual center):
    Janbogo → Mirny → Mawson → Halley → Palmer → Byrd → South Pole.
  - **"Thematic"** — an emotional arc built from each subnet's confirmed meta-personality read (wound →
    response → destabilization → isolation → purpose → verdict, the verdict echoing the opening wound):
    Palmer → Halley → Mawson → Byrd → Mirny → Janbogo → South Pole.
  **Open:** which one actually becomes the release order — a spatial story vs. an emotional one, not both at
  once. Developer's own lean is toward Thematic, open to Geometric; deliberately not decided yet.

- [ ] **Amundsen Time Code (ATC) — geographic rationale finalized 2026-07-23, implementation still open**
  ATC is logically derived from EST's geographical stretch, exactly as UTC is derived from GMT's. Three
  finalized reasons, per `TODO.md`: (1) EST is the single longest-spanning real-world time zone (its
  farthest-north land is the world's farthest-north land, barring Greenland's tip); (2) EST contains New
  York City, one of history's largest and most ethnically/linguistically diverse settlements; (3) EST is
  *adjacent to* (not encompassing) the Antarctic Peninsula — the closest real-world time zone to Palmer
  City, Tepenia's first-settled ground. Named for Amundsen Station, the South Pole's geographically
  "centerless" neutral relay. Still open: in-game display, whether the Planetary Split Brain disrupted
  timekeeping consistency across subnets, and how ATC relates to polar night/midnight sun.

