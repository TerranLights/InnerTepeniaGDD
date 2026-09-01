# The Input Contract — What Must Be Supplied, and What the Methodology Produces

> **⚠ Read `00_RUNBOOK.md` first.** This file defines the boundary of the whole procedure.

**Added 2026-08-30, at the developer's direction**, after the methodology was drafted and the question was
asked directly: *which pieces of information cannot be created within this process and must be provided?*

**Answering it produced one finding large enough to sit at the top of the file.**

---

# 0. The headline: all eight generators are inputs

`02_Generators_Capability_and_Symbols.md` builds the methodology's entire spine from eight generators, and
requires at least three of them to run. **Every one of the eight is a thing the methodology cannot produce.**

| Generator | Who supplies it |
|---|---|
| G1 Assigned symbolic substrate | Supplied — the assignment is made in a separate pass |
| G2 Physical & environmental constraint | Supplied — real geography, or authored geography |
| G3 Function & purpose | Supplied — canon decides what a place is for |
| G4 Founding condition | Supplied — canon |
| G5 Network position | Supplied — the map and infrastructure files |
| G6 Defining event | Supplied — the timeline |
| G7 Real-world inspiration | **Split** — the *designation* is supplied; the *research* is the method's own work |
| G8 Demographic composition | Supplied — census and composition files |

**This is the correct architecture, not a defect.** A derivation engine is supposed to be constraint-fed; it
cannot also supply its own axioms without becoming circular. **But it means the input surface is much larger
than "a name and a map,"** and a pass that starts without it will either stall or quietly invent — and quiet
invention is the failure mode this whole methodology exists to prevent.

**The district methodology already knew a version of this and stated it once, in a limits section**
(`00e` §12): *"The substrate cannot tell you a district's history. It supplies temperament, capability, and
relational geometry. Founding events, migrations, and specific crises come from elsewhere."* **This file
generalizes that from one generator to all eight, and from history to the whole input surface.**

---

# 1. Four categories, not two

The naive split is *inputs* and *outputs*. **There are four**, and the two middle ones are where the real rules
live.

| Category | Definition | Example |
|---|---|---|
| **PROVIDED** | The methodology has **no mechanism** to generate it | Where the place physically is; who founded it; how many live there |
| **RESERVED** | The methodology **could** generate it, but authority belongs elsewhere | A person's proper name; the disposal-of-the-dead question; a location's official in-fiction name |
| **PRODUCED** | The methodology's actual output, always as **Proposed:** | The capability profile; the culture; the findings |
| **REQUESTED** | The pass discovers it needs something that does not exist, and **emits a specific request rather than inventing** | "This location's arrival mode is undetermined and Phase 2 cannot run without it" |

**RESERVED is not a weaker form of PROVIDED.** A provided input is missing; a reserved decision is *deliberately
withheld*, and the correct behavior differs completely — you stub or block on a missing input, but you **write
fully around** a reserved one, per the protocol in `00_RUNBOOK.md` Step 0.5.

**REQUESTED is an output type and should be treated as one.** A pass that ends with three well-formed input
requests has done real work. A pass that ends with three quiet inventions has done damage that is invisible
until someone else contradicts it.

---

# 2. PROVIDED — the full list

Organized by when the pass needs it, because that determines what happens if it is missing.

## 2.1 Tier 0 — Blocking. The pass cannot start.

| Input | Why it blocks |
|---|---|
| **Existence and designation** | That this location exists at all, and something to call it — even provisionally |
| **Position in the world** | Where it physically is. Everything in G2 and G5 descends from this |
| **Population magnitude** | Not composition — just the order of magnitude, because it sets the **scale band**, and the band changes what every later phase is asking (`01` §2) |
| **Parent** | What contains it — or an explicit statement that nothing does |

**If a Tier 0 input is missing: stop and request it.** Do not proceed on a guess. Four of the seven substantive
errors recorded in this project were scale, scope or frame errors, and all four would have been visible in a
completed Tier 0 block.

## 2.1b Tier 0b — Temporal frame. Extremely helpful, not obligatory.

**Reclassified 2026-08-30 at the developer's direction, and the reasoning is worth keeping in full because it
corrects a wrong assumption in the first draft.**

**An earlier version listed temporal frame as blocking. It is not.** Type and setting usually imply era closely
enough to proceed: a location in orbit around Jupiter is evidently future; a medieval village is evidently past;
a city suburb is present or near-present. **The pass can run on an inferred era**, and demanding an explicit one
would block work that could proceed perfectly well.

**But its real value is not dating, and calling it "which era" undersold it.** The frame's actual work is
setting the **epistemic horizon**:

> **What would the people here know about? What are they aware of? What has already happened to them, and what
> has not happened yet?**

**The sharpest case is a major event, and specifically which side of it this pass sits on.** A location written
*before* a war and the *same* location written *after* it are not the same place with different dates — they
differ in what its residents have lived through, what they expect, what they consider normal, and what they
cannot yet imagine. **A location may legitimately need both passes**, and the pair is more informative than
either alone.

**So the rule is:**

- **Declare the frame if it is known.** It sharpens every phase, and it sharpens Phase 6 (Meaning) and Phase 2
  (Composition) most.
- **If it is not known, declare it as inferred, and say what it was inferred from.** An inferred frame is a
  perfectly workable input; an *undeclared* one is not, because later readers cannot tell whether an anachronism
  is deliberate.
- **Where the location straddles a major event, say which side this pass is on** — and if the answer is "both,"
  that is two passes, not one hedged document.

**The one hard rule that survives from the blocking version:** *the same location at two eras is two documents.*
Hedging one document across a threshold event produces a place that is coherent at neither.

## 2.2 Tier 1 — Spine-critical. At least three required.

**These are the generators.** `02` requires three independent ones; **three of the following must be present or
the capability profile cannot be built**, and without the profile nothing downstream has a spine.

| Input | What specifically is needed |
|---|---|
| **Physical & environmental facts** | Terrain, climate, altitude, exposure, hazards, what the site provides and withholds |
| **Function / purpose** | What the place is *for* — and separately, **what its parent needs from it**, because those two disagreeing is itself a generator |
| **Founding condition** | Who, when, why, under what constraint, **with what, and without what** |
| **Network position** | What connects, in which direction, carrying what volume |
| **Population composition** | Who is here, in what proportion, from where |
| **Defining events** | What has happened *to* this place |
| **Symbol assignment** | If the location's class participates in a symbol system at all |
| **Real-world inspiration designation** | *Which* real-world case anchors it — the research is then the method's own work |

**If fewer than three are available: the pass may proceed but must say so**, and must expect a measurably
thinner result. Record which generators were unavailable — an absent generator is data about the state of the
canon, not just about the pass.

## 2.3 Tier 2 — Enriching. The pass runs without them and is worse.

- **Existing scattered canon about the place** — the "formalize before inventing" step has nothing to formalize
  without it
- **The parent's determined properties** — climate, currency, law, calendar, language family *(`01` §5.1)*
- **Sibling set membership** — without it the differentiation instrument cannot run and the no-sibling
  substitutes must be used instead
- **Inspirational-influence picks** — the research tier list
- **Prior passes on this location** — and their epistemic status
- **Adjacent locations' completed passes** — needed for Phase 5 and Gate 6
- **Physical/spatial layout** — a map, or an adjacency list

## 2.4 Tier 3 — Optional particulars: known things that touch the place

**None of these is required. Every one of them, if present, measurably improves the result** — and the reason
is worth stating precisely, because it changes how they are used.

### The principle: these are testimony, not attributes

**The eight generators are *attributes* of the place** — properties it has. Physical constraint, function,
composition. They describe it directly.

**A known particular is *testimony*.** A character who lives there, an object made there, a vehicle that runs
the route — none of these is a property of the place. **Each is a thing that touches the place and bears
witness to it**, and you reason *backward* from the particular to what must be true for it to exist.

> **The procedural consequence, and it is the whole value: you do not record a particular, you interrogate
> it.** *"Character X lives here"* is a roster entry and adds nothing. ***"What must be true of this place for X
> to have become who X is?"*** is a derivation, and it will produce things the attribute generators cannot.

**This is `Cultural_Synthesis_Techniques.md` §7, The Surviving Witness, pointed at living canon instead of
physical remains** — the same logic, different evidence.

### The interrogation procedure

Run per particular. Five steps, and step 2 is the one that does the work.

1. **Look it up in canon**, via the registry in `00_RUNBOOK.md` §B–D. **The particular is a handle; the canon
   entry behind it is the actual input.** A name you cannot look up is not yet a usable particular.
2. **Ask what must be true of the place for this to exist, or to be the way it is.** Not what the particular
   says *about itself* — what it *implies about its surroundings*.
3. **Chase to third order**, per LAW 0.
4. **Classify the evidence tier** — see the hazard below. Is this typical, or notable-therefore-atypical?
5. **Record whether it changed a finding or ornamented one**, per Gate 7. Both are honest; they are not the
   same.

### The catalog

| Particular | What to interrogate it for | Feeds |
|---|---|---|
| **A resident, past or present** | What the place taught them · what it failed to teach · what they had to leave to get · what they still do that only makes sense here | 2, 4, 7, 9 |
| **Someone who came** | **What the place offers that is worth relocating for** · what they gave up to get here · whether the promise held · **and whether they were pulled by the place or pushed from elsewhere** — those are different arrivals *(see the note below)* | 2, 4, 5, 7 |
| **Someone who left** | **What drives people out** · whether they were pushed or simply outgrew it · what they could not get here | 2, 5, 7 |
| **Someone who stayed when others left** | What holds a person here past the point of sense | 2, 4, 6 |
| **Someone who refuses to go there** | Reputation from outside; the Neighbor's view before you run the panel | 5 |
| **An object made or carried there** | Materials available · tooling · the problem it solves · who carries it | 1, 3, 8, 10 |
| **A vehicle or conveyance** | Distances that matter · terrain · what moves in bulk · maintenance skills present | 1, 3, 5, 7 |
| **A food or drink** | Agriculture or import · preservation constraint · what a meal *is* here | 8 |
| **A song, artwork, or story** | **What a place makes art *about* is diagnostic** — and what it never depicts | 6, 8 |
| **A building or landmark** | Construction era · what it was for · whether it is still used for that | 3, 10 |
| **A route, road, or connection** | Direction and volume · what is upstream and downstream | 5 |
| **A custom, law, or prohibition** | What it exists to prevent — **a rule is a fossil of a problem** | 7 |
| **A job or trade practiced there** | The standing cost being paid · what the economy actually runs on | 1, 7 |
| **A slang term or speech marker** | What the place has enough of to need a word for | 8 |
| **A minor incident** *(not a defining event)* | Ordinary friction; how the place handles a small thing | 4, 7 |
| **A death, grave, or memorial** | **The hardest category to source, and this is the best handle into it** | 6 |
| **A grievance or alliance** | Relation geometry, already half-written | 5 |
| **Concept art, a photograph, a map** | Texture directly — and it constrains, which is the point | 3, 10 |
| **A faction with a presence there** | **Why here?** What the place offers them that elsewhere does not | 5, 7 |
| **A known absence** | Something notably *not* here — often the sharpest single input available | any |

> ### The arrival pair — and why "who came" is not just "who left" inverted
>
> **Added 2026-08-30 at the developer's direction, correcting a real asymmetry in the first draft**, which wrote
> the repulsion case and skipped its mirror on the assumption that what drives people out is always sharper.
> **That is wrong for any place people choose**, and the correction has a worked example in canon.
>
> **Shirayuki** is the Federation's clearest attraction case — a city whose school system grew into a nationwide
> draw and whose downtown became art-filled and gallery-dense, such that people **make excuses to be able to
> move there.** Its symbol pairing reads *Uranus + Fire* — a natural outlier — and the outlier status is the
> attraction rather than the cost. **A pass that only ever asked "what drives people out" would have produced a
> Shirayuki with no explanation for why anyone is there.**
>
> **So run both, and keep them distinct:**
> - **Pull** — the place offers something obtainable nowhere else. Interrogate: *what specifically, is it still
>   true, and who is disappointed?*
> - **Push** — the person was leaving somewhere else and this was the destination. Interrogate: *what were they
>   escaping, and does this place know it is a refuge rather than a choice?*
>
> **A place made of pulls and a place made of pushes behave completely differently** — in confidence, in how it
> treats newcomers, in whether it believes its own reputation. **Ask which mix this is**, and note that a place
> can shift from one to the other across eras without noticing *(which pairs directly with the epistemic-horizon
> question in §2.1b)*.
>
> ### ⚠ And pull and push differ in DURABILITY, not only in direction
>
> **Added 2026-08-30 from a measured case, and it is worth more than the argument originally made for this
> entry.** The reasoning at the time was that attraction is as informative as repulsion. **The stronger fact
> is that attraction is *reversible* in a way obligation is not:**
>
> > **A population assembled by attraction has already demonstrated willingness to relocate for something
> > better. It will demonstrate it again.**
>
> **So ask of any pull location: *what happens here when somewhere more attractive opens?*** Every attachment
> a pull location offers tends to be **low-switching-cost** — pleasant, genuinely good, and costless to give
> up. Push locations accumulate **high-switching-cost** attachments — a trade, a claim, an obligation, people
> who know your business — which are unpleasant and which hold.
>
> **The finding this produces is often that a location's greatest strength and its largest structural
> vulnerability are the same property**, running in two directions. *(Worked case: a city famous for being the
> place people move to, which retained 61.8% of its population against a 71.9% national mean when migration
> became possible — third-lowest of thirty-three. The pull that fills it is the pull that emptied it.)*
>
> **Cross-check this against G8's census-change technique** (`02` G8) — pull/push predicts retention, and
> retention is measurable, so **this is one of the few places the methodology can check its own reading against
> a number.**

### ⚠ The special case: a known "first," "only," or "last"

**The highest-yield particular type, and worth asking about explicitly even when nothing else is known.**

If canon says this is *the only place that does X*, *the first place where Y happened*, or *the last place still
doing Z* — **that is differentiation handed to you for free**, and it satisfies Gate 6 before the pass begins.

**Interrogate it hardest:** what made it possible *here and nowhere else*? What did the other places have that
prevented it, or lack that made it unnecessary? **A uniqueness claim always implies a comparison, and the
comparison is usually more interesting than the claim.**

### The four hazards

**1. The single-witness fallacy — the main one.** **Known characters are, by definition, notable — therefore
atypical.** A place derived from its named residents becomes a place of exceptional people, which is wrong
everywhere above Band 1. This is the general-population discipline in a new costume.
> **The fix is not to avoid characters; it is to label the evidence tier.** A notable resident is genuine
> evidence of **what this place can produce at its extreme** — which is useful, and is not the same claim as
> what it typically produces. **Say which you are asserting.**

**2. Over-fitting.** Building the place around accommodating one known particular. The particular is evidence
*about* the place, not a specification *for* it.

**3. Circularity.** If the character's backstory was itself written from this location's culture pass, feeding
it back is self-confirmation. **See §6.1 — the rule applies to particulars most of all**, because character and
location canon cross-pollinate constantly.

**4. Canon drift.** A character file and a location file can disagree because one was updated and the other
was not. **When they conflict, that is a genuine finding site, not an error to smooth** — apply the
both-are-true test before deciding either is wrong.

### How particulars relate to the generators

**They are not a ninth generator** — a particular does not produce a capability profile on its own.

**But they can substitute for a missing generator at reduced strength.** Where G8 (composition) is unavailable,
four or five known residents are a weak but real sample. Where G4 (founding condition) is unavailable, the
oldest known particular is a floor on the place's age and a witness to its early character. **Say that this is
what you are doing**, and expect a thinner result.

**And they can conflict with a generator, which is the best thing they do.** A physical generator saying the
place is hostile and a known resident who chose to stay is a conflict — and per `02` §5.3 the question is not
which is wrong but *what single property would produce both.*

## 2.5 Type-specific inputs

Some types need things a Settlement does not, and a pass that assumes the Settlement input set will silently
under-specify them.

| Type | Additionally requires |
|---|---|
| **Polity** | Member list · what it determines for members · basis of legitimacy · succession rule |
| **Installation** | Controlling institution · mission · staffing and rotation model · who it answers to |
| **Corridor** | Both endpoints · traffic type and volume · maintenance authority · chokepoints and seasonal closure |
| **Structure** | Purpose · builder · physical specification · current structural condition |
| **Vessel** | Route and range · crew model · home port · what it carries |
| **Natural feature** | Physical specification · who holds claim or access · hazard profile |
| **Network locus** | Topology position · access norms · **where the physical substrate actually sits** |
| **Interstitial** | The full set it is between · what each neighbor sends it |
| ***modifier:* Ruined** | Former state · destruction event · current occupancy · **what physically remains** |
| ***modifier:* Contested** | Whose account this pass is writing, stated explicitly |
| ***modifier:* Seasonal** | Both populations, and the handover |

---

# 3. RESERVED — the methodology must not decide these

**Could be generated. Must not be.** The distinction is authority, not capability.

| Reserved | Why |
|---|---|
| **Proper names of people** | **Standing binding rule.** Phase 10 people-entries are role placeholders permanently — *"a veteran repair-shop owner"* — because the developer names these personally once the roles exist |
| **A location's official in-fiction name** | Several are explicitly open. A pass may use a working designation and must not settle one |
| **Canon-level rulings that constrain many locations** | Anything whose answer would bind places beyond this one — the disposal-of-the-dead question is the standing example: a sealed city must do *something* and the project has not decided what. **Write practice *around* the dead; do not invent the mechanism** |
| **Supply-chain and mechanical facts with existing contradictory canon** | Where two files already disagree, a culture pass must not adjudicate |
| **Anything the developer has explicitly deferred** | Listed at the head of each pass per Step 0.5 |
| **Whether the location exists at all** | Not the methodology's call |

**The protocol when a pass turns up material bearing on a reserved question** — and it will, repeatedly:

> **Do not bury it in a parenthesis and do not use it.** Write it as a **numbered finding, marked reserved**,
> stating what was found, what it would decide, and explicitly that it is **not adopted here.** A parenthesis is
> lost; a reserved finding is a handoff, and the next pass inherits a loaded, labeled instrument rather than an
> absence.

---

# 4. PRODUCED — what the methodology actually outputs

Everything downstream of the generators. **All of it carries the standing `Proposed:` status** — the district
convention that no finding is locked canon on arrival.

- The **four-quadrant capability profile**, its shape, and its deficit addresses
- All eleven phases' content
- **Named** institutions, practices, customs, places and things *(names of places and practices are produced;
  names of people are not)*
- **New belief systems, factions and institutions** where the analysis genuinely produces one — *"the template is
  a floor, not a ceiling"* — provided each is named, defined and cross-referenced so it enters canon cleanly
- The differentiation axes and the inline comparisons
- The QA and Review Panel blocks
- **Input requests** *(§5)*
- **Recorded nulls** — a category that produced nothing, with the reason

---

# 5. REQUESTED — the output nobody thinks of as an output

**When a pass discovers it needs something that does not exist, the correct move is to emit a request, not to
invent.** A well-formed request states four things:

1. **What is missing**, precisely.
2. **Which phase is blocked** and how badly — cannot-run, or runs-thinner.
3. **What the pass did instead** — stubbed, assumed provisionally, or skipped.
4. **What would change if the answer came back differently** — the sensitivity, so the developer knows what is
   riding on it.

**Collect these in a block at the end of the pass.** They are the highest-value thing a pass hands the next
person, and they are the mechanism by which the methodology grows the canon instead of quietly fabricating it.

---

# 6. Input acceptance — the provenance question

The developer's framing: an input may be **written by a human** or **synthesized by a separate, outside AI
process.** **The contract does not care which.** It cares about four properties, and a human-written input can
fail them exactly as easily as a generated one.

| Property | Test |
|---|---|
| **Stable** | Will this still say the same thing next month? An input still under active debate is a *reserved decision*, not an input |
| **Attributed** | Can you tell where it came from? An unattributed fact cannot be re-checked when it turns out to matter |
| **Scoped** | **Does it state its own limits?** The composition file does exactly this — it says outright that its figures are *"relative-ranking figures, not a literal population count."* **A pass that reads a source past its own stated limits has committed one of the seven recorded developer catches** |
| **Non-circular** | **See below — this is the one that specifically threatens an AI-generated input pipeline** |

## 6.1 The circularity rule

> **An input must not be derived from this methodology's own output for the same location.**
>
> **GENERALIZED 2026-08-30, after the first test run found the original wording too narrow to catch the
> commonest case:**
>
> ### **An input must not be a prior culture-pass CONCLUSION about the same location — regardless of which
> methodology produced it.**

**Why the original rule missed this.** It was scoped by *provenance* — "this methodology's own output" — so a
completed culture pass written by **any other process** slipped straight through. **The defect is identical.**
Reading a location's finished Cultural Spec Sheet and then "deriving" that location's culture is the district
folder's *"planting your own seed and then finding it,"* one level up. **The result is perfectly coherent and
contains no information.**

**This is not hypothetical.** The Tri-Cities carried roughly 4,000 lines of existing canon *per city* —
32-section spec sheets, Enneagram reads, and a purpose-built differentiation guide. **None of it was this
methodology's output, so the rule as written permitted all of it as input.**

### The operational split — and it is clean enough to apply without judgement calls

| **ADMISSIBLE as input — attributes** | **INADMISSIBLE as input — conclusions** | **⚠ ADMISSIBLE BUT SELF-ORIGINATED** *(added 2026-08-30)* |
|---|---|---|
| Physical and environmental facts | *"This city's character is X"* | A fact that is **genuinely canon and genuinely usable**, but which **originated in this same location's own prior culture pass** and was later promoted or migrated |
| Founding mechanism, date, and circumstance | *"Its temperament reads as Y"* | **Use it — you are usually obliged to.** But **tag every finding that rests on it**, because it is **corroboration, never independent derivation** |
| Function, industry, what it makes | Any prior pass's **capability, personality, or culture** finding | The commonest source: **a claim migrated upstream into shared canon** — see §6.1b |
| Network position, routes, adjacency | A prior pass's **shape**, **axis**, or **differentiation** claim | Second commonest: **a symbol or type assignment derived from a prior personality read** |
| Census, composition, **population change** | Anything phrased as an interpretation rather than a fact | |
| ⚠ Symbol assignment — **but see §6.1c** | | |
| Dated events | | |

**Columns 1–2 are G1–G8 and their negation. The admissible column is exactly the generator stack, which is the
point.** **Column 3 exists because the first two assume a claim stays where it was written, and claims move.**

> ### ⚠ 6.1a — ADMISSIBILITY IS A PROPERTY OF CONTENT, NEVER OF FILENAME OR FOLDER
>
> **Added 2026-08-30 after this defect contaminated a cold run within its first ten minutes.**
>
> A handoff listed `[City]_Physical_Infrastructure_Attributes.md` as safe to open at any time. **The filename
> says attributes. The file was two passes welded together** — a genuine attribute derivation, *and* a
> cross-reference section quoting the city's culture pass and full-extrapolation **conclusions verbatim**,
> including their axis claims. **Its own header named a withheld culture file as a source.**
>
> **The rules:**
>
> 1. **A file is admissible only if *every section* of it is.** There is no partial read: **you cannot un-see
>    the second half.** A document that is 60% attributes and 40% conclusions is an **inadmissible document.**
> 2. **Where a source genuinely mixes the two, the fix is upstream — split the file.** Do not attempt to read
>    around the conclusions.
>    > **⚠ The narrower case — one admissible COLUMN and one inadmissible one, in the same table row.** *(Added
>    > 2026-08-31, from a real case.)* Not every mixed source is a whole file — a registry table can legitimately
>    > have one admissible field (e.g., a symbol assignment's *members*) and one inadmissible field on the same
>    > row (e.g., that assignment's derived *rationale*). **A bare-name `grep` returns the entire matching
>    > line**, exposing the inadmissible field along with the admissible one — the same "cannot un-see" problem
>    > as rule 1, at finer grain. **The mechanical fix: anchor the search pattern to only the admissible
>    > columns** (e.g. `grep -oP '^\| CityName \| \S+ \| \S+ \|'` to capture just the first three pipe-delimited
>    > fields of a markdown table row) **rather than searching by name alone.** Splitting the file (rule 2)
>    > remains the fix for whole-section mixing; column-anchored extraction is the fix for row-level mixing,
>    > and the two should not be confused.
> 3. **Build a quarantine list by RULE, not by RECALL.** Apply the content split above section by section.
>    **A list assembled from memory is written by the one person who has already read everything, and a
>    document you have already read does not announce itself as contaminating.** This is the circularity rule
>    one level up, and it is how the defect above got onto a "safe" list in the first place.
> 4. **Check the header of every admissible file for its own sources.** A file that cites a withheld document
>    is downstream of it, whatever it is called. **This check costs seconds and would have caught both
>    instances.**

> ### ⚠ 6.1b — CANON MIGRATION LAUNDERS PROVENANCE
>
> **Added 2026-08-30. Verified, and it produced a live cross-project canon error before it was caught.**
>
> **A claim written in a location's culture pass, then migrated upstream into shared canon, becomes admissible
> — without a word of it changing.**
>
> | Stage | What it is | Admissible? |
> |---|---|---|
> | Written in the location's own culture file | a culture-pass conclusion | **No** |
> | Migrated into the shared/universe canon | a *When / Where / Who* fact | **Yes — and correctly so** |
>
> **Nothing detects the transition, because nothing is wrong with it.** Routing a broadly-binding claim upstream
> is exactly what `00_RUNBOOK.md` §E question 3 instructs. **The methodology's own correct behavior builds the
> laundering channel.**
>
> **And migration does not merely relocate a claim — it PROMOTES it.** In the location file it was a
> subordinate clause in a founding paragraph. In the shared canon it was rewritten as **an answer to a standing
> open question** *("this directly answers…")*. **Nobody decided to promote it; an open question and a
> newly-arrived relevant sentence attract each other.** The promoted version carried a word — *"drove"* where
> the truth was *"participated in"* — **that was wrong, and that then bound five sibling projects.**
>
> **Three rules:**
> 1. **Provenance travels with a migrated fact.** The receiving file records which location's pass produced it,
>    in one bracketed clause. *(The instance above did this by accident, and the accident is the only reason it
>    was catchable.)*
> 2. **Migration must not promote.** A claim keeps its original strength. **"Contributes one name to" is not
>    "directly answers."** If it genuinely settles an open question, that is a separate decision needing
>    separate confirmation.
> 3. **A pass that finds a shared-canon fact citing its own location must tag it `[SELF-ORIGINATED]`** and
>    treat every dependent finding as corroboration.

> ### ⚠ 6.1d — A `Specs/` FILE IS NOT CATEGORICALLY SAFE EITHER
>
> **Added 2026-08-31, Cape Adare Run 7, self-caught mid-pass.** `00_RUNBOOK.md` §0.4 heads its admissible-first
> reading order with "specs / physical facts," and no run before this one had ever found a `Specs/` file
> containing conclusion-bearing content — so the tier was trusted by default rather than checked. **A `Specs/`
> file cleared after its first ~20 lines (matching the expected Based-on/Status/Population pattern) turned out
> to contain a "Character & Culture" section** further down — civic temperament, a named developer-vision
> paragraph asserting settled cultural facts (community character, pace of life, specific instrumentation),
> and a citation to the location's own withheld `Local_Cultures` file for "full detail." **Exactly the §6.1a
> pattern, inside the one tier this methodology had never tested for it.**
>
> **The rule, generalized:** read a `Specs/` file to its actual end before clearing it, and treat any section
> headed **"Character," "Culture," "Significance," "Developer vision,"** or similar as suspect by default —
> apply the same header/content check §6.1a already requires of `_Physical_Infrastructure_Attributes.md` files.
> **No file-type in this registry is safe by category. Every file is safe by content, checked.**

> ### ⚠ 6.1c — A SYMBOL ASSIGNMENT MAY BE DOWNSTREAM OF A PERSONALITY READ
>
> **Added 2026-08-30.** In this project, `City_Symbol_Assignments.md` states in its own header that every
> assignment was **"derived from each city's own established personality"** — from a set of prior Enneagram
> reads. **So G1 is provenance-downstream of a culture pass for all 34 assigned cities**, and §6.1's bare
> listing of "Symbol assignment" as admissible is **wrong as written for this project.**
>
> **The clean salvage, and it generalizes:** **the *pair* is a two-token assignment and the *meanings* live in
> the system files, which describe symbols rather than this location.** So:
> - **Usable:** the assigned members, and their definitions read from the system's own files *(per §6.0)*.
> - **NOT usable:** any *rationale* column in the assignment table. Those are capability verdicts wearing an
>   index's clothing — *"self-sufficient, ordered complexity, content unexamined"* is a four-term personality
>   reading, not an assignment.

> **Conclusions are read LAST, and read as a CHECK.** After the pass produces its own findings, compare. **A
> match is corroboration. A mismatch is a finding site.** Consulted at the start they are contamination;
> consulted at the end they are evidence.

**And this gives a single-location pass a falsifiable success measure it otherwise lacks:** *did the pass
produce anything the existing material does not already contain?* **A pass that only reproduces what is
already written has failed, even if every sentence is true.**

If an outside process writes a founding story *by reading the location's completed culture pass*, and that
founding story is then fed back in as a Tier 1 generator, **the pass is confirming itself.** The result will be
perfectly coherent and will contain no information.

**This is not hypothetical — the district methodology already found the same defect in miniature and corrected
it.** The Phase 5 counterculture-seed technique works in Mode A because the seed was written months earlier by
someone not thinking about counterculture. In Mode B, where both are written in one pass, it is *"planting your
own seed and then finding it,"* which is *"circular and yields a worse answer than deriving honestly."* **The
technique was explicitly scoped to Mode A only for exactly this reason.**

**Generalized: track provenance direction.** An input generated downstream of a location's culture pass is not
an input to that pass. It may be a legitimate input to a *different* location's pass, or to a later re-run under
a materially changed methodology — but it must be labeled, or the circularity becomes invisible.

## 6.2 What outside AI synthesis can and cannot supply

**Can:** anything in the PROVIDED list, on the same terms as a human — physical facts, founding stories,
composition, events, network position. The four acceptance properties are the whole test.

**Cannot:** anything RESERVED. A reserved decision is reserved *to the developer specifically*; it is a question
of authority, and no generating process discharges it. **An outside process may propose; it may not settle.**

---

## 6.3 ⚠ RATIFICATION IS A SEPARATE AXIS FROM CIRCULARITY — and this file had no tier for it

**Added 2026-08-31, on a direct developer flag during Run 9 setup:** *"those vignettes still need to be
double-checked. I haven't determined which ones are canon."*

**Everything in §6.1 tests one thing: is this input CIRCULAR — is it downstream of a culture-pass conclusion
about this same location?** That is a real test and it is not this one. **A file can pass §6.1 completely —
genuinely upstream, no conclusions, clean provenance — and still not be canon, because nobody has ratified
it.** Admissibility has two axes and this file previously described only one.

| | **Circular?** | **Ratified?** | **Admissible as canon input** |
|---|---|---|---|
| A culture pass's own conclusions | yes | yes | **No** — §6.1 |
| A settled spec / census figure | no | yes | **Yes** |
| **A proposal, suggestion, or draft** | **no** | **NO** | **No — this section** |

### The recorded instance

**Janbogo's `Course_of_Events/` set — eleven files, ~1,836 lines — is not confirmed canon.** The status is
**stated in the files' own headers**, which read *"Course of Events **Suggestion** #1, translated from
`…_Course_of_Events_Suggestions.md`"*, and whose character fields are deliberately left blank as design
prompts. **Every city has a folder of this kind.** They are proposals awaiting a ratification decision the
developer has not yet made.

> ### ⭐ Why this went unnoticed: a filter caught it once, for the wrong reason
>
> **Sinheung Run 5 excluded its vignettes correctly — and by accident.** Its pre-flight disqualified them as
> *"downstream of withheld material"* — a §6.1 CIRCULARITY judgement. **It never asked whether they were
> canon.** On a location whose culture file is not withheld, that reasoning does not fire, and the same
> unratified material sails straight through as admissible.
>
> **A correct result produced by the wrong rule is not a working rule. It is an untested one.**
>
> **And it has already failed once.** Cape Adare **Run 8 (warm)** lists
> `Cape_Adare_Course_of_Events_Suggestions.md` in its input set with no status marking at all — admitted as
> though settled. A warm pass admits everything by design, which is exactly why *status marking*, not
> exclusion, is the rule below.

### The rule

1. **Check ratification separately from circularity, and check it second** — a file that fails §6.1 is out
   regardless, so ask this only of inputs that already passed.
2. **Read the header.** In this corpus the status is usually declared: *suggestion · proposal · draft ·
   opportunities · candidate · tracker · TENTATIVE · flagged*. **A filename ending in `_Suggestions.md`, or a
   folder of numbered narrative variants generated from one, is unratified until told otherwise.**
3. **Unratified material is NOT quarantined — it is DEMOTED.** It cannot ground a finding, cannot settle a
   fact, and cannot be cited as canon. **It may be read as a prompt** — the same standing a real-world
   inspiration has: a source, never a specification. Distinguish it in the text every time.
4. **Where an unratified file is the ONLY support for a finding, the finding is REQUESTED, not PRODUCED** —
   it goes to the developer as a ratification question, not into the pass as a fact.
5. **Never ratify by use.** Citing a suggestion in a completed pass, and then treating the completed pass as
   canon, is `6.1b`'s laundering problem on the authority axis instead of the provenance axis. **The developer
   ratifies. A pass does not, and neither does repetition.**

---

# 7. The pre-flight checklist

Run before Phase 0. **Cheap, and it is the input-side equivalent of Gate 0.**

```
## Input Contract Check

**Tier 0 (blocking):**
- Existence & designation:        present / MISSING
- Position in the world:          present / MISSING
- Population magnitude (→ band):  present / MISSING
- Parent:                         present / explicitly none / MISSING

**Tier 0b (strongly recommended, not blocking):**
- Temporal frame:                 given / INFERRED (from: ...) / straddles an event (which side: ...)
- Epistemic horizon:              what would people here know about, and what has not happened yet?

**Tier 1 (need ≥3):**  [list which are present]   → count: n
**Tier 2 (enriching):** [list absences]

**Tier 3 (optional particulars — none required; each one improves the result):**
- Known residents / arrivals / leavers:   [names, and whether each is pull or push]
- Known objects, vehicles, food, art:     ...
- Known buildings, routes, landmarks:     ...
- Known customs, laws, trades, slang:     ...
- Known deaths, memorials, incidents:     ...
- Known grievances or alliances:          ...
- Concept art / images / maps:            ...
- **Any known "first," "only," or "last":**  ...   ← ask explicitly even if nothing else is known
- **Any known notable absence:**             ...
- *For each: looked up in canon? · evidence tier (typical / notable-therefore-atypical)? · changed a finding or ornamented one?*

**Type-specific:**      [per §2.5 for this type]

**Ratification check (§6.3) — run on every input that already passed §6.1, second, never instead:**
- Files whose header or filename declares them *suggestion / proposal / draft / opportunities / candidate /
  tracker / TENTATIVE / flagged*:  [list, or "none found — and state that the headers were actually opened"]
- **DEMOTED (readable as prompt, cannot ground a finding):**  ...
- **Findings resting ONLY on unratified material → these are REQUESTED, not PRODUCED:**  ...
- *`Course_of_Events/` and `*_Course_of_Events_Suggestions.md` are unratified by default in this corpus.*

**Reserved decisions in force for this pass:**  ...

**Scope & configuration:**
- Written:            ALONE (default) / co-written with ... [if co-written, justify per `01` §5.3b]
- Configuration:      TYPICAL / EXCEPTIONAL — in what way: ...
                      [if exceptional, name the findings that will depend on the exceptional
                       property. A pass cannot correct for a bias it has not declared.]
- Sibling set:        present / NONE — substitutes used: ... [per `01` §5.3a]

**Provenance check:**
- Any input derived from this location's own prior output?              yes / no
- **Any input that is a prior culture-pass CONCLUSION about this place?  yes / no**
  [if yes: remove it. Conclusions are read LAST, as a check — see §6.1]
- Canon read in the Step 0.4 triage order, culture files last?           yes / no

**Sources that state their own limits:**  [and confirmation those limits were respected]

**Verdict:** proceed / proceed-thin (say why) / BLOCKED (emit requests)
```

---

# 8. Why this file makes the methodology safer rather than smaller

**The boundary was always there; it was just unwritten.** A pass that does not know what it is not allowed to
invent will invent it — not maliciously, but because a blank in a template reads as an instruction to fill it,
and because a coherent invention is indistinguishable from a recalled fact three weeks later.

**The district folder has a recorded instance of exactly this.** A mortuary mechanism was invented, written as
though canonical, and *passed the contradiction gate on three consecutive districts* — because each pass checked
against the previous pass rather than against canon. It was neither malicious nor careless; **it was a blank
that got filled and then cited.**

**An explicit input contract is what stops that.** It converts *"I don't know, so I'll write something
plausible"* into *"I don't know, so I'll write a request" —* and a request is visible, answerable, and cannot be
mistaken for canon by the next reader.
