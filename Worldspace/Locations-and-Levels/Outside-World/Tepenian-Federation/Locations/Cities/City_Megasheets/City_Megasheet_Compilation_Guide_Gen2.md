# City Megasheet Compilation Guide — Generation 2

**Status: working draft, written 2026-11-10 at the developer's direction. Not yet tested on a city.** Treat it as
provisional until the first Generation 2 sheet has been built with it and reviewed.

**What it governs:** the new megasheets written **after every city has finished the ULM, the CST and the RWBEM**.
The Generation 1 guide (`City_Megasheet_Compilation_Guide.md`, beside this file) stays exactly as it is, as the
record of how the July 2026 megasheets were made. Progress is tracked in `Megasheet_Progress_Checklist_Gen2.md`.

**The developer's decisions of 2026-11-10 that this guide carries out:**
- *"We're not taking anything away. Everything that's there should be there."* Every section and file type of
  Generation 1 has a place in Generation 2 (table in §0.1).
- **The Generation 1 megasheets will be archived. None of them is edited. The Generation 2 sheets are new files.**
- All nine method and format adjustments proposed that day are approved (§0.2).
- Every proposed new content type is approved **except weapons and gear**, which will get **a dedicated
  methodology of its own, separate from the ULM, the CST, the RWBEM and this guide**. A Generation 2 megasheet
  has no weapons or gear section.

**The developer's answers of 2026-11-10, later the same day:**
- **Derive in the components, then assemble.** *"(a): purely just assembling established data into one single
  reference-source"*, clarified: *"it's still necessary to derive (because you need to do all that '1st-order,
  2nd-order, etc', plus all that other stuff. Just that once those components are complete, then you assemble
  those together."* So the component files (Steps 1–7) are derived, and the finished megasheet (`README.md`,
  Step 9) is pure assembly of the completed components.
- **Comparison between cities happens only in the subnet and Super-Ultra layers** (*"indeed"*), after the
  end-of-run differentiation check (*"sure"*).
- The five questions of Part F are answered (Part F).

---

## 0. What carries over, and what changed

### 0.1 Everything from Generation 1 stays

| Generation 1 piece | Where it lives in Generation 2 |
|---|---|
| One-line pitch | Step 2 (Mega-Init), and repeated in the Quick Reference (Step 1) |
| Hard facts table, with the Founding row copied from the Register and the real station in its own Site / infrastructure row | Step 1 (Quick Reference) and Step 2 |
| Who lives here, and why | Step 2 |
| What it feels like, in the developer's own words | Step 2 |
| Personality (Enneagram read) | Step 2. The "closest-matching sibling city" line moves to the subnet layer (change 8) |
| Real-world inspirations, researched | Step 2, carried from the RWBEM's results (change 3) |
| What's actually open | Step 2 |
| Full Extrapolation: answers to open questions, things named, Notable Figures as proposals, the whole file framed as proposed | Step 3, limited to what the three methods left open (change 2) |
| Cross-Reference Synthesis: 2nd- to 4th-order chains, purely descriptive, closing patterns | Step 4 |
| Grounding the inherited records in the real station's actual work | Step 4 |
| Community Infrastructure & Social Life: Additions · Small offices for educational training · Social cohesion mechanisms | Step 5 |
| Physical Infrastructure Attributes: Methodology #1 and Methodology #2 | Step 6 (change 1: it was never written into the Generation 1 guide) |
| Founders checked against the Register before joining | Step 8 |
| The joined `README.md`, a straight concatenation | Step 9 |
| A "Worth Your Attention" callout closing every file; highlights written into the files, not only said on screen | Standing rule (§E) |
| `Questline_Asset_Concept_Art/` folder per city | Kept, one per city |
| The standing rule on founders and the real station | Kept (§E.1) |
| Subnet Ultra-Megasheet: Cross-City Patterns, Cross-City Throughways, Mega-Init, Full Extrapolation, Cross-Reference Synthesis | Part C |
| Super-Ultra-Megasheet: Cross-Regional Patterns, Cross-Regional Throughways, Mega-Init, Full Extrapolation, Cross-Reference Synthesis | Part D |

### 0.2 The nine approved changes

| # | Change | Where |
|---|---|---|
| 1 | **The Physical Infrastructure Attributes file becomes a written step and goes into the README.** Generation 1 built one for every city (2026-07-30) but the guide never described it and the READMEs left it out. | Step 6, Step 9 |
| 2 | **Invention fills only what the three methods left open.** Generation 1's Step 2 said to answer every open question. In Generation 2, a slot the methods ruled empty ("none is sited here") is a result and is never filled (the no-forced-fit law). | Step 3 |
| 3 | **The megasheet builds on the methods' work; it never redoes or replaces it.** The ULM, CST and RWBEM did their derivation and real-world research with far more care than a single megasheet sitting can. The component files carry those results and derive further from them (the 1st- to 4th-order work and the rest), never substituting a quicker answer for one the methods already gave. | Steps 2–7 |
| 4 | **One current answer per question, with a stated order of which source wins.** A city's answer can be spread over its pass, its amendments, the rulings and the answered decisions. The megasheet brings them together. | Step 0.2 |
| 5 | **Every claim carries a status label and its source address**, so a later reader (the questline methods first of all) knows which facts can bend. | §E.2 |
| 6 | **Every file lists its sources with the commit it read**, so a sheet that has gone out of date can be found. | §E.3 |
| 7 | **A short Quick Reference sheet comes first**, carrying the actual data, never a pointer to it. | Step 1 |
| 8 | **A city's sheet is about that city only.** Comparison between cities happens only in the subnet and Super-Ultra layers, after the end-of-run check for cities that came out too alike. Relation (what flows, what is shared, what the city depends on) stays legal at the city layer. | Step 4, Part C |
| 9 | **A new-generation checklist**, with the 38-city roster under current names, without removing anything from the old one. | `Megasheet_Progress_Checklist_Gen2.md` |

---

## Part A — Before any sheet is written

### A.1 When this runs
- **Not before every city has finished all three methods.** A Generation 2 sheet is never built from a partial corpus.
- **The order of the work after the runs** *(confirmed by the developer, 2026-11-10; F.1)*:
  ULM on all 38 cities → the developer's annotation pass and the extrapolation appended from it
  (`Universal_Location_Methodology/MASTER_Process_Tracker.md`, "SEQUENCING DECISION", item 1) → CST and RWBEM,
  corpus-wide → the post-ULM queue (the census review `DR-23`, the station-heritage rulings) → the end-of-run
  differentiation check → Generation 2 city sheets → the subnet layer → the Super-Ultra.
- **Operating hours.** Steps that derive new claims about a place or its people (Steps 3–7, and the Patterns,
  Throughways and Full Extrapolation of Parts C and D) are worldbuilding and run **05:00–14:59 only**. Compiling
  sourced facts (Step 1, the copying parts of Step 2) and assembling a finished README (Step 9) are
  classification and may run at any hour. When unsure, apply the two-limb test in the operating-hours rule and say which way it was applied.

### A.2 Who compiles: one city per clean compiler
- **A compilation pass contaminates its compiler for every location it reads** (`Universal_Location_Methodology/00_RUNBOOK.md`
  §C.3). So:
  - **Each city sheet is compiled by a compiler that has read no other city's material.** It is the strongest
    form of change 8: a sheet cannot carry another city's answer if its compiler never read one.
  - **The subnet layer is compiled after its city sheets exist**, by a compiler that reads those sheets.
  - **A session that has compiled megasheets can't later run a cold pass on any location it covered.** Keep
    megasheet sessions separate from any location run.
- Every compiler reads, before starting: this guide in full; the Universal Design Laws index
  (`/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/Universal Design Laws/README.md`);
  the men's audience reference index
  (`/home/kuroskalacs/Documents/Doll-Fi/media/y-files/writing stories for men/data/README.md`) and the
  extractions it points to, as a lens, not a template; and the city's rulings in
  `Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md` (the general rulings plus every ruling naming the city).

### A.3 The archive
- **The Generation 1 set is archived before the first Generation 2 sheet is written.** Archiving to the shared
  ArchiveVault repo is done only with the developer's confirmation.
- **A Generation 2 file never replaces a Generation 1 file in place**, and nothing in the Generation 1 set is edited.
- **The Generation 1 sheet is not a source of claims** for its Generation 2 successor; its content predates the
  three methods and was withheld from them. **It is read only after the new sheet's component files are
  complete, as a point of reference** (developer, 2026-11-10; Step 8.5).
- The method files in this folder (both guides, both checklists, the folder README) are not megasheets and stay
  in place when the Generation 1 sheets are archived.

### A.4 Names and folders
- Sheets use **current city names**, from `Cities/City_Renames_Alias_Table_2026-10-03.md` and any later ruling.
  The Generation 1 folders still carry old names (Abowasa, Princess_Elisabeth, Sayowa, Vostok, Juan_Carlos,
  Port_Lockroy, Sejong); the alias table §3b already says they keep them until the rewrite.
- **Names still pending** at the time of writing: Dome Fuji's official name, new names for Dumont d'Urville and
  Zukelli, and a possible rename of Cape Adare. Subnet names that share a member city's name may change after all
  cities are done. A sheet built while a name is pending uses the name in force and records it as pending.

---

## Part B — One city sheet

**The folder:** `City_Megasheets/[Subnet]/[City]/`, the same layout as Generation 1 (see F.3).

**The files, in build order:**

| Step | File | Short description |
|---|---|---|
| 1 | `[City]_Quick_Reference.md` | the data, in rows, each with its citation |
| 2 | `[City]_Mega_Init.md` | synthesize and reconcile |
| 3 | `[City]_Full_Extrapolation.md` | limited invention |
| 4 | `[City]_Cross_Reference_Synthesis.md` | what emerges from combining the sources |
| 5 | `[City]_Community_Infrastructure.md` | places, small training offices, rituals |
| 6 | `[City]_Physical_Infrastructure_Attributes.md` | base attributes and their cross-referenced findings |
| 7a | `[City]_Life_and_Texture.md` | the senses, layout, food, music, hardships and joys, ordinary people, names |
| 7b | `[City]_Robot_Life.md` | robots in this city |
| 7c | `[City]_Through_Time.md` | the city in each era, and what travels when its people leave |
| 7d | `[City]_Structure_and_Stakes.md` | raw material for factions, order, danger, empty slots |
| 7e | `[City]_Where_It_Appears.md` | where the city is used in the game |
| 9 | `README.md` | all of the above joined, in order |

**Two kinds of work, in this order** (developer, 2026-11-10): **the component files (Steps 1–7) are where the
derivation happens**: the synthesis, the limited invention, the 1st- to 4th-order chains and the rest. **The
`README.md` (Step 9) is pure assembly**: once every component is complete, the components are joined into one
single reference source, adding nothing of their own.

### Step 0 — Gather the inputs, read all of them, and settle which source wins

#### 0.1 The inputs
Read everything before writing anything (Generation 1's reason still holds: connections only show once all the
sources are held at once). Paths are under `Worldspace/Locations-and-Levels/` unless they start with "Cities/" (short for
`Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/`), "ULM/" (short for
`Worldspace/Locations-and-Levels/Universal_Location_Methodology/`), or `Storyline/` or `Dev-Road-Map/` (repo root).

| Input | Path |
|---|---|
| The city's ULM pass: Steps −1 to 10, its record and its readiness check | `Cities/City_Development_Passes/[Subnet]/[City]/` (`09_Record.md` and the step and phase files) |
| The city's amendments, and which were applied by the developer's word | the same folder, `Amendment_*` files, read under `ULM/Amendment_Layer_Rules.md` |
| The city's datasheets | the same folder, `Datasheets/` |
| The developer's post-ULM annotations and the extrapolation appended from them | where the annotation pass writes them (not yet run) |
| The city's CST results | where the CST run writes them (not yet run) |
| The city's RWBEM results | where the RWBEM run writes them (not yet run) |
| The city's research log | `Cities/Research_Logs/[City]_Research_Log.md` |
| Rulings | `ULM/DEVELOPER_RULINGS_LOG.md` |
| Answered and open decisions | `Cities/Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md` |
| Founders | `Cities/Founding_Register.md` |
| Population | `Cities/Official_Population_Census.md`, **Census I** (`DR-4`) |
| The spec | `Cities/Specs/[Subnet] subnet/[City].md` |
| The city's robot culture file | `Cities/Local_Robot_Culture/[Subnet]/[City].md`, as the city's input contract admitted it |
| Relations | `Cities/City_Relationship_Database.md`; `Outside-World/Tepenian-Federation/Locations/Infrastructure/` (`Ports.md`, `Highways.md`, `Airports.md`, `Rastra_Mechanics.md`); the Division of Industry files |
| Symbols, once ruled | `Cities/City_Symbolic_Substrate/City_Symbol_Assignments.md` |
| Game use | `Storyline/DLC_Overview.md`, `Storyline/DLC-Questlines/`, the companion files |

**Never an input:** the Background-Lore vignettes (not canon); another city's files at the city layer; the
differentiation table's other rows; the Generation 1 sheet as a source of claims (A.3).

#### 0.2 Which source wins
When two sources disagree, the higher row wins and the sheet cites both:

1. **A developer ruling or an answered decision** (`DEVELOPER_RULINGS_LOG.md`, the decisions file's `## Answered`),
   the newer over the older. An answer given for another city does not carry; only a ruling recorded for every
   city, or for this one, applies.
2. **Founders come only from the Founding Register** (`DR-19`). **The population band comes from Census I** (`DR-4`).
3. **The developer's own words** (the post-ULM annotations, the vision notes) are the highest creative source, as
   in Generation 1. Where they disagree with a derived result, the sheet records both, marks the line
   `PROVISIONAL`, and puts the question in the decisions file (see F.5).
4. **An amendment applied by the developer's word** over the pass lines it corrects. An amendment that has not
   been applied is `PROVISIONAL`. The pass files themselves are never edited (`DR-101`).
5. **The city's ULM, CST and RWBEM results.** Where two of them disagree, record both and ask.
6. **The spec's structured facts**, where nothing above supersedes them.
7. **The datasheets.** They are copies with citations, so where a datasheet and its cited source differ, the
   source wins and the difference is logged.

### Step 1 — The Quick Reference (`[City]_Quick_Reference.md`)
One to two pages, built first, joined first. **It carries the data itself, never a pointer to it** (the
datasheet rule of 2026-10-31). Every row gives the value, its status label and its citation.

- **Name** (current), former names, subnet, DLC
- **One-line pitch** (from Step 2, filled in once Step 2 exists)
- **Location:** region, terrain, elevation, coordinates as the spec states them
- **Site / infrastructure:** the real station's name, operator, start year and condition (site only, `DR-24`)
- **Founders:** the Register row as written (founders, ruling, status). If it is open or overturned: "not yet ruled"
- **Population:** the Census I band and figure; departures phrased as a share of those who left
- **Composition:** each origin row with its own figure, robots counted in their row at their own percentage
  (`DR-128` item 1), stated flatly, no ranking
- **Languages:** Hawaiian dominant; the supporting tier, every group within 12 points of the largest (`DR-100`)
- **Climate:** station, authority, data period, annual mean, all twelve monthly means; polar day and night spans
- **Transport:** highways, port, airfield, Rastra
- **Symbols:** Planet and Element, once ruled
- **Open decisions:** each decision number with a few words on what it asks

### Step 2 — The Mega-Init (`[City]_Mega_Init.md`): synthesize and reconcile
**Posture: summarize and reconcile; don't invent yet.** The Generation 1 sections, in the same order:

1. **The one-line pitch**: the city's whole identity in one sentence.
2. **Hard facts**: the Quick Reference's rows as a table. Founding row from the Register; real station in its own
   Site / infrastructure row.
3. **Who lives here, and why**: founders exactly as the Register holds them, the composition rows, and how the
   pass, the CST and the annotations account for that population. Name any tension rather than smoothing it.
4. **What it feels like**: built from the developer's own words (annotations and vision notes, post-ULM per
   `DR-10`), quoted or closely paraphrased, alongside the pass's own results on the city's look, sound and daily life.
5. **Personality (Enneagram read)**: the city's own read, in a few sentences. **No sibling city named here**;
   that line belongs to the subnet layer.
6. **Real-world inspirations**: carried from the RWBEM's results and the research log, not researched again.
   Generation 1's test still decides what is included: *what does this real place's own documented character give
   back to the city that isn't already there?* If the sheet needs a fact the corpus lacks, research it under
   LAW 0-R (search, don't recall; more than one angle) and log every search string in the city's research log.
   A pick is never chosen or judged by national match with the station or the founders.
7. **What's actually open**: the city's open decisions, the research log's open threads, and any new question
   this synthesis surfaced, kept apart from the carried-forward ones.

### Step 3 — The Full Extrapolation (`[City]_Full_Extrapolation.md`): limited invention
**Posture: invent, but only where the three methods left a question open, and every invention earned.**

1. **What may be answered:** a question the ULM, CST and RWBEM left open, that no ruling settles, and that is not
   waiting on a developer decision (those stay `PROVISIONAL`, citing the decision number).
2. **What may never be answered here:**
   - a slot the methods ruled **empty** ("none is sited here"): it is a result, listed in Step 7d, never filled;
   - a founder, in any form (`DR-19`);
   - a tradition or institution continued from the real station. What the newcomers inherited is records
     (`DR-25`); a practice may be *rediscovered* from those records by the city's own people.
3. **The earned test (from Generation 1):** name the established fact that made this answer more natural than any
   other equally plausible one. Every invented line is labeled `PROPOSED` and cites that fact.
4. Organize by natural category, not by the order the questions appeared. Name things.
5. **Notable Figures** are proposed as a name, a role and why they are here, never a backstory. Developing a
   figure goes through the character methodology later (and starts from the Enneagram type files, never copied as-is).
6. Frame the whole file at the top as proposed extrapolation, not canon.

### Step 4 — The Cross-Reference Synthesis (`[City]_Cross_Reference_Synthesis.md`)
**Posture: hold the sources side by side and find what emerges only from their combination.** As in Generation 1:

1. Look for facts in different sources that were never placed together: a baseline in one and a detail that
   depends on it in another; an open question one source answers without saying so; two true facts that create a
   tension or timeline problem. The sources are now the city's pass phases, its CST and RWBEM results, the
   annotations, and Steps 1–3.
2. Each finding: **(a)** the facts and their source addresses, **(b)** the 2nd-order effect, **(c)** the 3rd,
   **(d)** the 4th where it still holds. Mark the exact point where the chain goes past what is supported, and
   stop there.
3. **The real station enters a chain only as infrastructure or as the records it left** (`DR-19`, `DR-24`,
   `DR-25`). Ground what those records contain in the real station's actual work. Take that from the research log
   if the run already researched it; otherwise research it and log it.
4. **Purely descriptive** (Generation 1 correction of 2026-07-07): no "questline seed" or "dialogue branch" labels
   in this file.
5. **One location (change 8):** another place may appear only as **relation**, something this city lives with
   (a shared port, a highway that ends here, a dependency). The test: delete the other place's name from the
   sentence; if the sentence still says something about this city, keep it; if it collapses, it was a
   comparison: cut it.
6. Close with a synthesis of patterns recurring across the findings, and Worth Your Attention.

### Step 5 — Community Infrastructure & Social Life (`[City]_Community_Infrastructure.md`)
**Posture: get concrete.** Unchanged from Generation 1: re-read Steps 2–4 and the city's results for anything that
implies an unnamed gathering place, small trade or craft institution, or recurring social ritual. Three headers:
**Additions** · **Small offices for educational training** · **Social cohesion mechanisms**. Every item traces to
an established fact and gets a proper name. **No institution may continue a real station's program**; it may be
founded on the records the station left. Close with Worth Your Attention.

### Step 6 — Physical Infrastructure Attributes (`[City]_Physical_Infrastructure_Attributes.md`)
**New as a written step; the file itself existed in Generation 1** (built 2026-07-30 for every city; recorded in
`Dev-Road-Map/Weekly_To-Do_-_Current.md` L763–784).

1. **Preamble:** what the file is built from, and the city's **governing facts** in one paragraph (site, terrain,
   climate, status, the defining feature).
2. **Methodology #1 — Base Attributes:** a first-principles derivation of the physical and civic attributes the
   city would have to possess, from its own governing facts. Grouped under headers by system (for example the
   defining feature, the transport hub, the climate engineering, war damage). Generation 1 followed this with a
   comparison round across cities; **in Generation 2 that round moves to the subnet layer** (change 8).
3. **Methodology #2 — Cross-Referenced Extrapolation Findings:** combine those attributes with the city's own
   results into findings in the same format as Step 4 (*Combining …* → 2nd, 3rd, 4th-order effect), appended in
   the same file.
4. **Depth:** the city that anchors its DLC's story (per `Storyline/DLC_Overview.md`; ask the developer where
   that file leaves it unclear) gets the deepest treatment; every other city gets a proportionate one, never a
   token pass. Byrd carries its whole DLC alone and keeps its extra depth.
5. Close with Worth Your Attention.

### Step 7 — The new content files
Each file opens with its source manifest (§E.3), labels every claim (§E.2), and closes with Worth Your Attention.
**Where a section's source work has not happened yet** (for example holidays and religion, which come after the
CST), the section says so and stays open; it is not filled from elsewhere.

#### 7a — `[City]_Life_and_Texture.md`
- **The senses:** light through the year (from the polar day and night spans), building materials, colors,
  sounds, smells, and the languages on signs.
- **Layout:** the city's footprint, landmarks, zones and how people find their way. These are the seeds any future
  districts would grow from; this file does not create districts.
- **Food and drink**, from the CST.
- **The music scene**, from the CST: what is played, on what, where, and by whom.
- **Calendar, holidays and religion**, once that work exists (it comes after the CST).
- **Daily hardships.**
- **Small joys.**
- **Ordinary people:** three to five everyday residents, human and robot, each with a role, an ordinary day and a
  want. They are sketches, not characters; character development goes through the character methodology.
- **Naming:** how people, robots and places are named here, through the divergence operator (composition names the
  stock; time and place produce the culture), never a national stereotype. A short name bank, labeled `PROPOSED`.

#### 7b — `[City]_Robot_Life.md`
- Robots' share of the population (their origin rows at their own percentage, `DR-128` item 1) and the roles they hold.
- How robots and humans live together here, including robot-human love.
- Robot customs, and the places where robots are maintained.
- Coolant preferences.
- Seeds for possible robot religions: seeds only, since religions come after the CST.

#### 7c — `[City]_Through_Time.md`
- **The city in each era:** its founding (from the Register); Act 1, when its people are still "X who live in
  Antarctica" (2564 to the early 2600s); Act 2, when they are properly Tepenian (late 2600s or early 2700s on,
  with Amundsen Tower's completion, ~2688, as one cause among several); the Long Night War and its damage; the
  city's state at game time (≈2822–2827, `Dev-Road-Map/08-Phase-6-World-Depth.md` L120), including the
  post-war fields the Second Interwar scope requires.
- **Who left, and where they went**, phrased as a share of those who left.
- **What travels:** for each cultural element, whether it is tied to this place (ice, cold, polar night, the local
  ground) or would survive a move, and what it might become in a Concordia district of residence and later
  off-world. Seeds only, written as relation: what this city's people carry, never a comparison with where they arrive.

#### 7d — `[City]_Structure_and_Stakes.md`
- **Raw material for factions, without creating factions:** the city's stakes, debts, social contracts, standards
  of worth and fault lines. Factions are created after the whole run, from rules, with open lists.
- **Order and consequence:** what counts as a crime here, how it is enforced, and informal justice, consistent
  with the national criminal justice system.
- **A fixed danger profile:** environmental hazards, the security situation, and the place's designed difficulty.
  **Fixed. It never scales to the player** (the no-level-scaling law).
- **Deliberately empty slots:** every slot the methods ruled empty, with its source address, so nothing
  downstream fills it by accident.

#### 7e — `[City]_Where_It_Appears.md`
The city's DLC; the main-questline candidates and under-questlines that use it; companions from here; its concept
art folder; its open decisions. **The Background-Lore vignettes are not listed** (not canon, never an input).

### Step 8 — Checks before joining
1. **Founders:** run `python3 Universal_Location_Methodology/Tools/check_founders_against_register.py --city "[City]"`
   from `Worldspace/Locations-and-Levels/` and read every hit in context. A clean list isn't proof; read the
   founding passages against the Register row yourself. Fix the sheet, never the Register.
2. **One location:** run the delete-the-name test on every sentence that names another place.
3. **Labels:** every claim line carries a status label and a source address; every `PROPOSED` line cites the fact
   that earned it.
4. **Empty slots:** none filled anywhere in the sheet.
5. **Manifests:** every file's source list complete, with commits.
6. **Never-inputs:** no vignette, no claim from the Generation 1 sheet, no other city's file.
7. **American English:** the only British form kept is "judgement". Never change a URL or a logged search string.
8. **A second reader:** a fresh reader checks the sheet against its sources before it is joined. Self-audit in
   this project has erred toward flattering the work every time it was measured.

### Step 8.5 — The Generation 1 sheet as a point of reference
**Only after every component file is complete and checked** (developer, 2026-11-10: *"only after the new sheet
component files are complete, as they could serve as a good point-of-reference"*). Read the city's archived
Generation 1 sheet from its archive location and note:
- anything it covers that the new components don't;
- anything it states that the new components contradict.

Each item goes to the decisions file as a question, with both sides cited. **Nothing is copied from the Generation
1 sheet into a component.** If the developer's answer changes a component, the component is amended and the README
is assembled again.

### Step 9 — Assemble the `README.md`
**Only once every component file is complete** (Steps 1–8.5 done). **Pure assembly: it adds, rewrites and derives
nothing**; it is the one single reference source built from the finished components (developer, 2026-11-10). A
straight concatenation with a clear divider between files, in this order: Quick Reference ·
Mega-Init · Full Extrapolation · Cross-Reference Synthesis · Community Infrastructure · Physical Infrastructure
Attributes · Life and Texture · Robot Life · Through Time · Structure and Stakes · Where It Appears. The pieces
stay in the folder beside it. The order keeps Generation 1's meaning (synthesize → invent → find what emerges →
get concrete) and adds the new material after it. If a component changes later, the README is assembled again from
the components; it is never edited directly.

---

## Part C — The subnet layer (`[Subnet]_Subnet_Ultra_Megasheet/`)
- **Inputs:** the subnet's Generation 2 city sheets, and the relation sources (relationship database, highways, ports).
- **The Generation 1 files, kept:** `[Subnet]_Cross_City_Patterns.md` · `[Subnet]_Cross_City_Throughways.md` ·
  `[Subnet]_Subnet_Mega_Init.md` · `[Subnet]_Subnet_Full_Extrapolation.md` (its §I, each city's role in the
  subnet's collective identity, is read by both DLC questline methods) · `[Subnet]_Subnet_Cross_Reference_Synthesis.md` · `README.md`.
- **Comparison is allowed here**, after the end-of-run differentiation check: the Enneagram "closest sibling"
  line and the Physical Infrastructure comparison round live here.
- **New: the subnet's regional identity.** What the subnet looks, feels and *vibes* like as a region, emerging
  from its cities' actual compositions (`ULM/WHY_CITIES_ARE_THE_ROOT.md` §3, added 2026-09-14).
- **The subnet's name** may change once the member cities agree on one; until then the layer uses the name in force.
- **Byrd** is a single-city subnet: its city sheet carries the extra depth in place of this layer (Generation 1 rule kept).
- **Same two kinds of work as a city sheet:** the layer's files are derived; its `README.md` is assembled from
  them once they are complete.
- **Amundsen Station** is now becoming a proper town (developer decision, 2026-10-31): it gets a full city sheet,
  not Generation 1's shorter one. DLC 1's reserved story content stays out of the sheet.

## Part D — The Super-Ultra layer (`Super_Ultra_Megasheet/`)
- **Inputs:** the subnet layers, Byrd's and Amundsen Station's sheets, Concordia's top sheet, the census totals,
  and `Storyline/DLC_Overview.md`.
- **The Generation 1 files, kept:** Cross-Regional Patterns · Cross-Regional Throughways · Mega-Init · Full
  Extrapolation · Cross-Reference Synthesis · `README.md`.
- **Its status line stays TENTATIVE** until the DLC main-questline choices it depends on are made.
- **"Living document" becomes checkable:** its source manifest (§E.3) shows which lower layer has moved.
- **Same two kinds of work:** the layer's files are derived; its `README.md` is assembled from them once complete.
- **Concordia** (F.4, answered 2026-11-10): this guide's city structure is incorporated into the
  Concordia-specific methodology series, which builds Concordia's district sheets and its Ultra. The Super-Ultra
  reads Concordia's top sheet from there.

---

## Part E — Standing rules for every file

### E.1 Founders and the real station (kept from Generation 1)
- **Founders come only from `Cities/Founding_Register.md`.** No file may originate, restate or "earn" a founder
  the Register doesn't hold. If the city's row is open or overturned, every founding slot says "not yet ruled."
- **A founding nation stands on geography and access, never on the real station** (`DR-19`).
- **The real station** (its name, operator, start year, condition) is a fact about **site and infrastructure**
  only (`DR-24`).
- **What the newcomers inherited from it is records**: logs, journals, manifests, maps, documents. **Never a
  tradition or a living institution** (`DR-25`).
- Never pick, keep or reject a real-world research pick on national match with the station or the founders, and
  don't note the match either way.

### E.2 Status labels
Every claim line carries one label and its source address:

| Label | Meaning |
|---|---|
| `CANON` | Stated in canon: the spec (where not superseded), the Timeline repo, the Register, Census I |
| `RULED` | A developer ruling or an answered decision (cite its number) |
| `DEVELOPER` | The developer's own words: post-ULM annotations, vision notes |
| `DERIVED` | A result of the city's ULM, CST or RWBEM, current after applied amendments (cite file and line) |
| `PROVISIONAL` | Waiting on an open decision or an unapplied amendment (cite it) |
| `PROPOSED` | The megasheet's own invention, Step 3 or Step 7 only (cite the fact that earned it) |
| `EMPTY` | A slot the methods ruled empty (cite where). Never filled |

### E.3 The source manifest
Every file opens with a table of the sources it read: **path · short commit hash · date** (from
`git log -1 --format='%h %ad' --date=short -- <path>`). To check a sheet later, run the same command for each row;
any source whose hash has changed makes the sheet out of date for that source. An out-of-date note goes at the
**end** of the file, never the head, so no cited line moves. *(A checker tool that does this for a whole sheet is
not built yet.)*

### E.4 The rest
- **Worth Your Attention** closes every file, in that file's own words; the on-screen summary repeats what is
  already on the page.
- **No forced fit:** an empty slot is a result ("none is sited here", never "none is possible here").
- **No national stereotypes:** composition names the stock; time and place produce the culture.
- **No weapons or gear section:** that work has its own dedicated methodology (developer, 2026-11-10).
- **American English and plain language.**

---

## Part F — The developer's answers (2026-11-10)

| # | Question | Answer |
|---|---|---|
| F.1 | Is the order in A.1 right, and does the end-of-run differentiation check come **before** the Generation 2 sheets? | **Yes:** *"sure, we can do that."* (Subnet renaming, if it happens, comes before the subnet layer, so its folders get the agreed names once.) |
| F.2 | May the archived Generation 1 sheet be consulted at all? | *"only after the new sheet component files are complete, as they could serve as a good point-of-reference."* → Step 8.5 |
| F.3 | Do the Generation 2 sheets go in `City_Megasheets/` with the same layout, once the old set is archived? | **Yes** (*"indeed"*), with current names |
| F.4 | Is Concordia's megasheet layer rebuilt under this guide, or under the district methodology? | *"I'd like to incorporate the city structure into the Concordia-specific methodology series. There's been a lot of extremely high-quality information that we've gotten on how to actually derive a location and its culture from all these various runs that we've done on the cities, and it will be very, very useful in developing the districts of Concordia."* → Concordia's district sheets and its Ultra are built within the Concordia-specific methodology series, using this guide's city structure; and what the city runs have taught about deriving a location and its culture is to be brought into that series. **That second part is a separate methodology job, not yet started.** |
| F.5 | When the developer's own words and a derived result disagree, record both and ask, or let the developer's words win automatically? | *"definitely record both and ask, because it's entirely possible that there may be things I might miss."* → Step 0.2 item 3 |
