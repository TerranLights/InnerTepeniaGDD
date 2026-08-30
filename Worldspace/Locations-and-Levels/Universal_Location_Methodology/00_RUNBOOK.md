# RUNBOOK — Running One Location, Start to Finish

**Working draft, 2026-08-30. This is the operational entry point for the universal location methodology. Start
here.**

**Scope:** any location of any kind, at any scale — district, city, subnet, nation, station, highway, structure,
vessel, ruin, natural feature, network region. **Concordia's thirteen districts have their own working,
evidence-backed procedure** at `../Concordia-City/Districts/Phase_Instructions/00_RUNBOOK.md` and should keep
using it. This is for everywhere else.

**Status: unvalidated.** Every rule in the district runbook is attached to a specific pass that went wrong.
**Nothing here is.** See the README's status note, and treat the first several real runs as tests of the
instrument as much as of the location.

---

# LAW 0 — DEPTH OVER SPEED. NEVER RUSH TO A FAST RESULT.

**Stated in full rather than cross-referenced, because a procedure that cites its governing law instead of
stating it will be run without it.**

**Worldbuilding is upstream of the entire project.** Every character, questline, faction, companion arc,
personal struggle, daily hardship, pastime and small joy is **downstream of decisions made here.** A shallow
location does not produce a shallow location — it produces shallow people living in it, shallow problems for
them to have, and shallow reasons for anyone to care. **The cost of going fast here is not paid here.** It is
paid later, everywhere, by work that cannot be fixed without coming back and redoing this.

**Therefore:**

- **Contemplate before writing.** The first plausible answer is usually the generic one, and a generic answer is
  worse than no answer because it occupies the slot.
- **Do actual research.** Not recalled, not inferred from a name. **The one controlled comparison this project
  has ever produced** — same location, same author, same day, at two researched picks and at six — found that
  **the two strongest findings came from picks four, five and six and did not exist at two.** The "redundant"
  picks were not redundant; four of them were the pass.
- **Chase nth-order effects.** For every finding ask **"and what does that cause?" three times.** First-order is
  the observation. Second-order is usually the interesting one. **Third-order is where the place stops
  resembling anywhere else.**
- **Go deep on the specific, not wide on the general.** One institution understood to its third-order
  consequences beats six sketched.
- **Take the time.** There is no deadline and no credit for finishing quickly.

## The anti-patterns this law exists to stop

1. **Producing a location because it is the next one**, rather than because it has been thought through.
   **Completion is not the goal; a place somebody could live in is the goal.**
2. **Skipping research by declaring it redundant.** Prioritizing by difference is a real rule and it is also
   *convenient*. **A pick is only redundant once you have actually looked at it. Redundancy asserted from a
   title is a guess wearing the costume of a method.**
3. **Treating "the phase is covered" as "the phase is done."** A finding that answers the template question is
   the floor, not the ceiling.
4. **Accepting the first coherent answer** because it fits and the pass is long.
5. **Letting the gates substitute for thinking.** They confirm a pass is not *wrong*. **None of them can tell
   you it is not thin.**

**And the companion failure — research used as decoration.** Doing the research is not the same as letting it
change anything. After each source, ask plainly: **did this change a finding, or ornament one?** Both answers
are honest and must be recorded differently. A citation attached to a conclusion that would have been written
anyway makes a thin pass look researched.

## The closing test

> **Could a person live an entire life here — and would that life be unlike a life in any comparable place?**

If the honest answer is *"probably, I suppose,"* the pass is not finished regardless of what the gates say.

---

> **The one rule under all of it** (`../Cultural_Synthesis_Techniques.md`): **never carry one location's answers
> into another.** If two places produce similar-shaped answers to the same technique, at least one is wrong.
> Every gate serves that. **Law 0 is what makes it possible to obey** — two places produce similar-shaped
> answers mainly when neither was thought about long enough to become itself.

---

# What changes from the district runbook

For anyone who knows that procedure, the differences in one table.

| | District runbook | This runbook |
|---|---|---|
| **Type / scale / status / era** | All constant; never declared | **Declared, and every one changes the questions** — Step 0 |
| **Primary generator** | The zodiac capability reading | **Three independent generators, and the conflicts between them** — Step 2 |
| **Capability frame** | Two poles *(strength, deficit)* | **Four quadrants** — plus standing cost and grudging tolerance |
| **Inter-location relations** | **A measured hole**; only §6 of a cross-phase file covers it | **Phase 5, mandatory, mid-spine** |
| **Symbols** | The zodiac, built in | **Registered and open** — any system, assessed for shape before use |
| **Parent / children** | One parent, never written about | **Inheritance protocol, provisional assumptions, and a reciprocal parent gate** |
| **Phases** | 8 | **11**, restoring what the city template had and the district translation dropped |
| **Gates** | 0–11 | **0–11 carried, plus C · F · I · P · G** |
| **Canon** | "check canon" — no address given | **A registry, up front**, with a federated authority hierarchy and per-phase targets |

---

# THE CANON REGISTRY — where to look, and who wins

**Stated up front, because the rest of the methodology says "check canon" in a dozen places and an instruction
to check something is unrunnable without an address.** Every later file refers back to this section.

## 0. Canon is federated. There is no single source, and assuming otherwise is the failure.

**Authoritative material lives in at least three places at once**, and a location pass will normally need all
three in the same sitting:

- **the universe repo** — binding on When / Where / Who, across every Tepenian project;
- **this project's own repo** — binding on everything the universe repo excludes, and holder of most
  location-level detail;
- **sibling project repos** — not authoritative here, but a consistency obligation.

**"Absolutely authoritative" and "the only place to look" are different claims.** The universe repo outranks
this one on its three questions and is silent on most of what a location pass actually writes. **Checking only
the highest-ranked source is as wrong as checking only the nearest one.**

> ### ⚠ The practical trap, verified rather than hypothesized
>
> **The universe repo is not inside this one.** It sits at
> `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/`, a sibling of the whole
> `games/` tree. **A repo-local grep cannot see it.** Every search-based canon check run from inside this repo
> will return "not found" for universe canon — confidently, and wrongly. **It has to be opened deliberately.**
>
> **And canon migrates, leaving stubs.** `Worldspace/World_History_Reference.md` in this repo is **seven lines**;
> the real file is **344 lines** in the universe repo. The stub is correct and well-made — it was moved
> 2026-07-11 and a pointer was left behind, which is exactly right — **but a pass that finds the stub and does
> not follow the pointer comes away believing this project has almost no world history.**
>
> **So: when a canon file looks unexpectedly thin, check whether it is a redirect before concluding the canon
> is thin.** This generalizes past this one file — the same-filename-in-two-repos pattern will recur as more
> content migrates upstream.

## A. The authority hierarchy — already law, not invented here

**`TepenianUniverseTimeline/Reference/Repo_Scope.md` is a binding law** declaring the universe repo
authoritative for exactly three questions **across every Tepenian Universe project** — InnerTepeniaGDD,
TheCryptographHelixDD, OuterTepenia1_GDD, SouthernLights, CurrentNovelDocs:

> **WHEN** everything happens · **WHERE** everything happens · **WHO** is involved.

**It explicitly excludes** game mechanics, questline/branch structure, novel-specific craft, and
implementation detail — those belong to each project.

**So the precedence order, when two files disagree:**

| Rank | Source | Wins on |
|---|---|---|
| **1** | **`TepenianUniverseTimeline/`** | **When · Where · Who.** Chronology, geography, physical routes, character identity/backstory/relationships |
| **2** | **This project's own canon** | Mechanics, questlines, this game's design. **And everything the universe repo excludes** |
| **3** | Locked project canon *(Canon Reference, promoted findings)* | over |
| **4** | `Proposed:` findings *(most culture-pass output)* | over |
| **5** | `to-be-integrated/` | **staging, not canon** — usable as input, never as authority |
| **—** | **Deferred / reserved** | **nobody wins. Do not decide.** *(`05` §3)* |

**A location pass is rank 4 output.** It never overrides ranks 1–3. Where it contradicts one, **state the
contradiction and reconcile it in the text** — do not silently pick a side, and per `02` §5.3 look for a
both-are-true reading first.

## B. Universe-wide canon — `../../../../../Reference/TepenianUniverseTimeline/`

*(Absolute: `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/`. A separate shared
repo, not inside this one — so a pass must open it deliberately; it will not turn up in a repo-local search.)*

| File | Domain |
|---|---|
| `Reference/Repo_Scope.md` | **the authority law itself — read once** |
| `Reference/World_History_Reference.md` | universe history |
| `Timeline Eras/` | the four eras: First Interwar · Second Interwar · Solar Colonization · Post-Solar |
| `Reference/Falkland_Treaty/` | the founding instrument |
| `Reference/Laws_of_Robotics.md` | **robot fundamental laws — binding** |
| `Reference/Robot_Universals/` | robot cultural universals, four parts |
| `Reference/Doll_Representation_Categories.md` | the four representation categories |
| `Reference/No_National_Stereotypes.md` | **binding: GPS facts only, always** |
| `Reference/Enneagram_Undercurrents.md` | shared character typing |
| `Worldspace/Locations/` · `Worldspace/Characters/` | shared location and character facts |
| `Megacorps/` | cross-project corporate actors |

## C. Project canon — this repo

| File / folder | Domain |
|---|---|
| `Worldspace/World_History_Reference.md` | project history |
| `Worldspace/Robot_Biology_and_Culture/` | **siligel, coolant, robot coffee, Glitch-Coolant** — mandatory before any robot cuisine or physiology claim |
| `Worldspace/Factions/` · `Factions/Robot_Religions/` | faction and religion roster — **check before inventing either** |
| `Worldspace/National_Economy_and_Currency.md` | currency and economy |
| `Worldspace/National_Holidays.md` | Federation-wide observances — **what a local holiday must be distinct from** |
| `Worldspace/City_Logistics.md` | supply, dual economy, black market |
| `Worldspace/Energy_Grid_Failure_Rationale.md` | the grid and its failure |
| `Worldspace/Design_Principles.md` | standing design law |
| `Worldspace/Characters/` | character canon, incl. `Enneagram_Character_Index.md` |
| `Worldspace/Locations-and-Levels/…/Cities/` | city specs, census, symbolic substrate, Enneagram, relationships |
| `…/Concordia-City/Districts/District_Canon_Reference.md` | **district locked canon** |
| `Neo-Races-and-Cultures/` | per-subnet cultures; `Orbital_Cryptograph_Helix_Era/` for the novel-series crossover |
| `Background-Lore/Cities/` | historical vignettes |
| `Reference/Real-World/` | research extractions — **check `Book_Extraction_Index.md` before mining any book** |

## D. Sibling projects — check for cross-series consistency, do not port

`games/Outer Tepenia series/` *(OT1 · OT2 · New Centauri)* · TheCryptographHelixDD · SouthernLights ·
CurrentNovelDocs. **Shared facts belong in the universe repo, not copied between projects.** If a location pass
produces something that binds a sibling project, that is a rank-1 question and goes upstream.

## E. The four-question canon check — run at every phase

**Consistent, cheap, and it unifies rules currently scattered across five files.**

1. **Does canon already answer this?** → **formalize, do not invent.** Canon supplies mechanisms more often
   than a pass expects — countercultures, religions, shadow mechanisms, notable figures. Where it does, **the
   pass's job is to explain why *this* location was the one it happened to**, not to build a parallel.
2. **Does this contradict canon?** → **canon wins, by the rank order in §A.** State the contradiction and the
   reconciliation in the text. Look for both-are-true first.
3. **Does this bind anything beyond this location?** → if yes it may be **RESERVED** (`05` §3). A claim that
   constrains other locations, or that settles a question the developer has deferred, **is not this pass's to
   make.** Write it as a numbered reserved finding instead.
4. **Does this need registering back into canon?** → a genuinely new religion, faction, institution or category
   is a legitimate discovery — **the template is a floor, not a ceiling** — but it must be **named, defined, and
   cross-referenced from wherever its kind normally lives**, or the next reader will never find it.

> **⚠ And the failure this check exists to prevent, which has already happened here.** A mortuary mechanism was
> invented, written as though canonical, and **passed the contradiction gate on three consecutive districts —
> because each pass checked against the previous pass rather than against canon.** **Check against the source,
> never against the last pass that cited it.**

# Step −1 — The input contract, before the frame

**`05_The_Input_Contract.md`. Run its §7 pre-flight checklist first — it is the input-side equivalent of
Gate 0, and it is just as cheap.**

**The thing to internalize:** **all eight generators are inputs.** The methodology's entire spine is built from
material it cannot produce — physical facts, founding conditions, function, network position, composition,
events, symbol assignments. **This is the correct architecture** (a derivation engine cannot supply its own
axioms) but it means a pass that starts without its inputs will either stall or quietly invent.

**Four categories, and the two middle ones carry the rules:**

- **PROVIDED** — the method has no mechanism to generate it. **Missing ⇒ stub, assume provisionally, or block.**
- **RESERVED** — it *could* generate it, but authority is the developer's. **Missing ⇒ write fully around it**,
  per Step 0.5. Not the same behaviour as PROVIDED, and confusing the two is the error.
- **PRODUCED** — the output, always as **Proposed:**.
- **REQUESTED** — **an output type.** When the pass needs something that does not exist, **emit a well-formed
  request rather than inventing.** A pass ending in three good requests has done real work; a pass ending in
  three quiet inventions has done damage that stays invisible until someone contradicts it.

**And the provenance rule, which specifically threatens any outside-AI input pipeline:** an input must not be
derived from this methodology's own output for the same location. **The district folder already found this
defect in miniature** — the Phase 5 counterculture seed works only when written by someone months earlier who
was not thinking about counterculture; written in the same pass it is *"planting your own seed and then finding
it."* **Track provenance direction, or the circularity becomes invisible.**

# Step 0 — Frame

**0.1 Fill the declaration block** (`01` §6). Type and modifiers, **both** bands, status, temporal frame,
parent, children, sibling set. **Every line changes a later question.**

**0.2 Read the disciplines.** `00b` general population *(and its Band-1 inversion, `01` §2.3)* · `00d` shadow
proportion · `00f` review panel · `../Cultural_Synthesis_Techniques.md`.

**0.3 Run Gate 0** — reconcile any completion claim against the file, **and the file's own open-questions list
against what has actually been resolved elsewhere.** Cheapest gate, highest yield, fails in both directions.

**0.4 Read everything the location already has, before writing over it.** Existing material predates whatever
disciplines have been written since, and inherited findings are where Gate 9 fires hardest.

**0.5 Note reserved decisions and what would foreclose them** — and know you will probably find material
bearing on them anyway. **When you do: write it as a numbered finding, marked reserved**, stating what was
found, what it would decide, and that it is explicitly not adopted here. **A parenthesis is lost; a reserved
finding is a handoff.**

**0.6 State provisional assumptions about an unwritten parent** (`01` §5.2), and prefer building on physical
constraint over provisional inheritance wherever the choice exists.

# Step 1 — Audit what is inherited

**Run the asymmetry check on existing findings before writing new ones.** For every inherited finding describing
a threshold, gate, conversion, verdict, admission or status change: *the mechanism runs both ways — did the file
write both?* Ask what happens to someone it decides **against**, whether that outcome is as durable, and
**whether there is a route back.**

**This fires on inherited material at a very high rate**, because early material is typically written to explain
how a place *works*, which is a framing that documents the favourable path and stops.

# Step 2 — Build the spine

**Phase 1, and the whole of `02`.** This is the step everything else hangs on.

1. Select **at least three independent generators**.
2. Run each to a **full four-quadrant profile, separately, before comparing.**
3. Compare. **Agreement is grounding. Conflict is the richest site in the method. Shared silence is a shape
   result.**
4. Read the **shape**; apply its matching question; **where the shape repeats a sibling, run the three-step rule
   and table the comparison on four axes including tense.**
5. Read each deficit's **address**, and **count the addresses.**

**Do not research yet.** Researching before you know the deficit produces interesting material with nowhere to
attach.

# Step 3 — Research, aimed at what Step 2 named

**3.1 Research the deficit.** The single most reliable move available: the profile says what the place cannot
do; it does not say what the missing thing looks like. **Find a real culture that has it, and the contrast
writes the finding.**

**3.2 Research can supply a substitute institution**, not only texture — a real culture that lacked the same
formal capacity and evolved a workaround no design process would have invented.

**3.3 Prioritize by difference, not tier — but prioritizing is not skipping.** The most valuable pick is usually
the one least like the others. **Look at each pick at least far enough to know what it would have given.**

**3.4 The source is not a specification.** Three outcomes are all legitimate: close resemblance with a new paint
job · one mechanism taken and divergence everywhere else *(commonest)* · somewhere the source never went
*(often best)*. **The two tests that bind are internal:** is it characteristically consistent with *itself*, and
is it consistent in-world? **Divergence stated is stronger than resemblance implied.**

**3.5 Two failure modes:** **transcription** (a costumed version of somewhere real) and **importing a vivid
detail that does not follow.** **If the only argument for a detail is that it is interesting, cut it or earn
it.**

**3.6 Then run the Unrecognized Instrument** — never before Step 2 is finished.

# Step 4 — Write the phases

**Phases 2–10, per `03`.** Fold the generators in as you write; do not bolt on a separate "substrate section."

Standing reminders, all of which have their own recorded failure behind them:
- **Formalize before inventing.** **Check canon before deriving anything structural.**
- **Name the axis, in bold, before writing the content** — and check it against the differentiation instrument.
- **A null is a result**, but distinguish *covered in substance, absent in form* from *absent and unexplained*.
- **General-population discipline throughout.** **Shadow proportion throughout.**
- **Phase 5 is mandatory and is written mid-spine specifically so it cannot be dropped.**
- **Push every finding to a physical or behavioural expression.** The violation is usually the gameplay.

# Step 5 — Reconciliation

**Expect contradictions between generators, and between a generator and canon, to resolve both-are-true.** The
recurring shape: **one property producing two opposite effects on two different objects, or at two different
scales.** Do not ask which is true — ask **what single property would produce both**, then check whether the two
claims are about different objects.

**Canon outranks a generator.** State the contradiction and the reconciliation in the text; do not silently pick
one. **Where it genuinely cannot be reconciled, flag it open.**

**Translation discipline:** the generator's vocabulary never appears in the location's own claims. Bracketed
citations only. **Sweep with word boundaries on every alternative and inspect every hit.**

# Step 6 — Differentiate

`04` Part III. Read the relevant rows **before** writing each category; differentiate inline in the finding
itself, not in a footnote; **check the most recently written sibling first.** If there is no sibling set, run
the substitutes and **say in the pass that you did.**

# Step 7 — QA

`04` Parts I–II. Gates 0–11 carried, plus **C** (canon check, federated) · **F** (frame integrity) · **I** (inheritance classification) ·
**P** (parent reconciliation, on parent passes) · **G** (generator honesty).

**Paste raw scan output. Verify the instrument before trusting any zero. Report what Gate 11 cleared as well as
what it flagged.**

# Step 8 — The Review Panel

`00f_Review_Panel.md`, carried unchanged; only the casting changes. Six Flat Archetypes plus the mandatory
**Passer-Through** and **Neighbor**; the **Lover faculty's question every time.**

**Five dispositions:** accepted · noted · rejected · refereed · **unmet.**
**The test that keeps this from homogenizing a whole set:** *would satisfying this objection make the location
more like its siblings?* If yes, it is **unmet**, and the refusal is written as characterization rather than as
a gap to close.

# Step 9 — Record

1. Append the **QA block** and the **Review Panel block**.
2. Add the location's **column to its differentiation set, in the same commit.**
3. Update whatever tracker claims completion — **per Gate 0, list what the file actually contains, not a summary
   claim.**
4. **If this pass changed the methodology, update these files in the same commit**, and record **what was
   learned and on which location.** A methodology change that does not update the runbook has not been made —
   the next pass will follow the runbook, not the commit message.

---

# Where everything lives

| File | What it is |
|---|---|
| **`00_RUNBOOK.md`** | **this file — the procedure** |
| `README.md` | scope, status, and the four findings that forced the generalization |
| `01_Frame_Typology_and_Inheritance.md` | types, bands, status, frame, nesting, the declaration block |
| `02_Generators_Capability_and_Symbols.md` | the generator stack, the four-quadrant frame, shapes, open symbol binding |
| `03_The_Phase_Spine.md` | the eleven phases |
| `04_QA_Gates_and_Differentiation.md` | gates 0–11 + C/F/I/P/G, and the differentiation instrument |
| `05_The_Input_Contract.md` | **the boundary — PROVIDED / RESERVED / PRODUCED / REQUESTED, and the pre-flight checklist** |
| `../Cultural_Synthesis_Techniques.md` | **the generative toolkit — sixteen techniques, already general-scope** |
| `../Real-World_Basis_Extrapolation_Method.md` | the research method |
| `../Concordia-City/Districts/Phase_Instructions/00f_Review_Panel.md` | the panel, carried unchanged |
| `.../00b_…` · `.../00d_…` | general population · shadow proportion — both binding here |
| `.../00_RUNBOOK.md` | **the district procedure — the parent of this one, and still authoritative for districts** |
