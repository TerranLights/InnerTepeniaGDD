# The Phase Spine — Eleven Phases

> **⚠ Read `00_RUNBOOK.md` first.** **LAW 0 — depth over speed** governs every phase below. A phase that is
> *covered* is not a phase that is *done*.

---

# 0. Why eleven, and why these

**The eight district phases are not a skeleton; they are a patch.** They were built to close categories that
measured 0/13 or 1/13 across Concordia's districts — Robot-Specific Culture at 0/13, Visitor Experience at 0/13,
Fashion at 0/13, Architecture at 4/13. They are excellent at what they were built for and they do not cover the
space.

**Measured against the 32-section city template, the district phases inherit roughly half of it.** Absent from
the district set entirely: Founding Story · Climate Character · Seasonal Rhythms · Social Contract and Unwritten
Rules · Who This Place Attracts · Language · Division of Industry · Political Character · Relationship to Other
Cities · Notable Landmarks · Significant Events · Notable Figures.

**One of those absences is a known, measured defect rather than a scoping choice.** `00e` §6 records that no
district phase covers inter-district relationships, with consequences it quantifies — a completed district file
mentioning its own opposite district zero times. **The city template has that section (§23). It was present at
city scale and lost in translation to district scale.** The spine below restores it as **Phase 5**, deliberately
in the middle rather than at the end, because a phase at the end of a list is the phase that gets dropped.

**The ordering is by dependency, with two deliberate promotions:**

- **Ordinary Life is Phase 4, not Phase 5.** `00_RUNBOOK.md` promotes it to *"a generator, not a coverage box"*
  and credits it with the single best finding of the twelve-district set. It depends on capability and
  composition and on very little else, so it runs as early as its dependencies allow.
- **Relation is Phase 5, not Phase 8.** It needs enough of the place to exist to have relations, but it must
  precede Meaning, Order and Making — because those three are all inflected by who the place is set against, and
  because the three-way differentiation set (`00e` §6) needs the geometry established *before* categories are
  written, not after.

## 0.1 Applicability by type

**M** mandatory · **P** mandatory *and primary* — the phase that carries this type · **o** optional ·
**→** replaced by the noted substitute · **–** not applicable

| Phase | Settlement | Polity | Installation | Corridor | Structure | Vessel | Natural | Network | Interstitial |
|---|---|---|---|---|---|---|---|---|---|
| **0** Frame | M | M | M | M | M | M | M | M | M |
| **1** Constraint & Capability | M | M | M | M | M | M | M | M | *special* |
| **2** Composition & Arrival | M | M | M | →users | o | M | →users | →users | M |
| **3** Surface & Texture | M | →delegate | M | M | M | M | M | *adapt* | M |
| **4** Ordinary Life | M | →distribution | M | →transit day | o | M | →users | o | M |
| **5** Relation & Geometry | M | M | M | **P** | M | M | M | M | **P** |
| **6** Meaning | M | M | o | o | o | M | →external | o | M |
| **7** Order | M | **P** | **P** | o | o | M | – | o | o |
| **8** Making | M | →distribution | o | rare | rare | M | – | o | o |
| **9** Populations | M | M | M | o | o | M | – | o | M |
| **10** Catalog | M | →delegate | M | M | M | M | M | M | M |

**"Delegate"** means the answer belongs to the sub-locations' own passes and the parent records only the
*pattern of variation* (`01` §5.4). **A Band 5–6 polity that answers Phase 8 directly has been written at the
wrong scale.**

## 0.2 Mechanics that apply to every phase

Stated once here rather than repeated eleven times.

1. **Formalize before inventing.** Check whether the location already has scattered, unlabeled material for this
   category. Name the existing pattern and cite where each piece lives before adding anything. This is the
   single most reliable move in the district folder and it holds everywhere.
2. **Check canon before deriving anything structural.** Countercultures, religions, shadow mechanisms and
   notable figures all have existing canon more often than a pass expects. Where canon supplies the mechanism,
   **the pass's job is to explain why *this* location was the one it happened to** — not to invent a parallel.
3. **Name the axis, in bold, before writing the content.** *(`00_RUNBOOK.md` Step 4.)* A category is not
   differentiated by having different content; **it is differentiated by answering a different question.** If
   you cannot name the axis in three or four words, the category has not been differentiated — it has only been
   described differently. Check the axis against the differentiation instrument (`04`) before writing.
4. **A null is a result.** *(`Cultural_Synthesis_Techniques.md`, "Using this file" §5.)* A category that
   produces nothing distinctive for this location is allowed to produce nothing. **Record the null and say
   why.** Expect several per location; a location where every phase fires richly is a location someone has
   over-written. **But distinguish two nulls:** *covered in substance, absent in the expected form* is a finding;
   *absent and unexplained* is a hole. **The test is one question — does the pass say why the thing is missing?**
5. **General-population discipline** (`00b`), **with the Band-1 inversion** from `01` §2.3.
6. **Shadow proportion** (`00d`): the surface is true, the shadow is also true, and the shadow is a byproduct.
7. **The player-facing test** (`Cultural_Synthesis_Techniques.md` §0b): push every finding until it has a
   physical or behavioral expression — **seen, heard, entered, handled, spoken, done, or hooked.** A finding
   that can only be read about is weak. **And the violation is usually the gameplay.**
8. **Run the four-question canon check** (`00_RUNBOOK.md` §E), against the targets in §0.3 below.
   *Does canon already answer this? · Does this contradict canon? · Does this bind anything beyond this
   location? · Does this need registering back?* **Canon is federated — universe repo, project repo, and
   siblings — and the universe repo is outside this repo and invisible to a local search.**

## 0.3 Per-phase canon targets

**Which canon each phase must actually open.** Addresses are in `00_RUNBOOK.md` §B–D; **U** = universe repo,
**P** = this project.

| Phase | Check against |
|---|---|
| **0** Frame | **U** `Repo_Scope.md` *(the authority law — once)* · `Timeline Eras/` · **P** location registries, census |
| **1** Constraint & Capability | **U** `Worldspace/Locations/` · **P** city/district specs, climate data, `Energy_Grid_Failure_Rationale.md`, physical infrastructure |
| **2** Composition & Arrival | **U** **`No_National_Stereotypes.md` — binding, GPS facts only** · `Falkland_Treaty/` · **P** `Official_Population_Census.md`, diaspora/affinity files, founding-nation material |
| **3** Surface & Texture | **P** climate data, `Specs/`, physical infrastructure attributes, concept art |
| **4** Ordinary Life | **P** `City_Logistics.md`, `Robot_Biology_and_Culture/`, `National_Economy_and_Currency.md` |
| **5** Relation & Geometry | **U** `Worldspace/Locations/`, routes · **P** highways/airports/ports/Arcanet, `City_Cross_Subnet_Relationships.md`, `City_Relationship_Database.md`, `City_National_Connections.md` |
| **6** Meaning | **P** **`Factions/Robot_Religions/` — check the roster before inventing a belief** · `National_Holidays.md` *(what a local observance must differ from)* · **and the deferred mortuary question — do not answer it** |
| **7** Order | **P** `National_Economy_and_Currency.md`, `City_Logistics.md`, `Factions/`, criminal-justice canon · **U** `Megacorps/` |
| **8** Making | **P** **`Robot_Biology_and_Culture/` — mandatory before any siligel / coolant / Glitch-Coolant claim** · `Weapons_and_Tools_Philosophy.md`, gear catalogs, language/slang material |
| **9** Populations | **U** **`Laws_of_Robotics.md`** · **`Robot_Universals/`** *(all four parts)* · `Doll_Representation_Categories.md` · **P** human-robot relations baseline |
| **10** Catalog | **U** `Worldspace/Characters/` · **P** `Enneagram_Character_Index.md`, notable-figure and landmark canon · **and the no-invented-person-names rule** |

**Two standing reminders that cut across the table.** `Reference/Real-World/Book_Extraction_Index.md` must be
checked before mining any book — **it exists because a book was twice assessed as unmined when it was not.**
And **check against the source, never against the last pass that cited it** — a mortuary mechanism was once
invented and then passed the contradiction gate on three consecutive districts because each pass checked the
previous pass.

---

# PHASE 0 — FRAME

**Asks:** *What kind of thing is this, at what scale, in what state, in what era, and inside what?*

**Produces no location content.** Its entire output is the declaration block from `01` §6 plus the generator
selection from `02` §5.1. It exists because every subsequent phase question is ambiguous without it.

**Process.**
- **A.** Fill the declaration block. Type + modifiers, both bands, status, frame, position, sibling set.
- **B.** Enumerate available generators; select at least three, **chosen for independence rather than strength**.
- **C.** Read the location's existing material in full before writing anything, and **run the asymmetry check on
  it** — for every inherited finding describing a threshold, gate, conversion, verdict, admission or status
  change, ask whether the file wrote both directions. *(This fires on inherited material at a very high rate;
  see `04` Gate 9.)*
- **D.** State reserved decisions the pass must not foreclose, and what would foreclose them.

**Failure mode.** Treating the block as bureaucracy and filling it after the fact. **Four of the seven
substantive errors recorded in this project were scale, scope or frame errors** that this block makes visible
before the writing starts.

---

# PHASE 1 — CONSTRAINT & CAPABILITY *(the spine)*

**Asks:** *What can this place do without trying, what can it not do at all, what must it keep paying, and what
does it permit but punish?*

**The whole of `02` is this phase's reference.** Everything downstream hangs on it.

**The core move.** Run three independent generators to three separate four-quadrant profiles, **then compare** —
agreement is grounding, conflict is the richest finding site in the method, and shared silence is a shape result.

**Process.**
- **A.** Run each selected generator to a full four-quadrant profile, **separately, before comparing.**
  Comparing early lets the first read contaminate the others.
- **B.** Build the comparison table; mark every cell *agree · conflict · silent*.
- **C.** Resolve conflicts with the both-are-true test — *what single property would produce both readings, and
  are the two claims about different objects or at different scales?*
- **D.** Read the **shape** (`02` §4) and apply its matching question. **Where a shape repeats a
  previously-written location, run the three-step rule and write the comparison as a table on at least four
  axes, including tense.**
- **E.** Read the **address** of each deficit (`02` §4.1) — and **count the addresses**, because a count above
  one should raise suspicion rather than reassurance.
- **F.** **Then** research the deficit. The profile says what the place cannot do; it does not say what the
  missing thing looks like. **Find a real culture that has it, and the contrast writes the finding.** Research
  can also supply a *substitute institution* — a real culture that lacked the same formal capacity and built a
  workaround no design process would have invented.
- **G.** **Then, and only then,** run the Unrecognized Instrument — is the place already doing the thing it
  cannot do, somewhere, for an unrelated reason, and has never noticed it generalizes? **Run it after, never
  before:** found first it softens the deficit, found second it sharpens it.

**Band variance.** At **Band 1** the profile is a profile *of a dozen people plus a building*, and the standing
cost quadrant usually dominates. At **Band 5–6** the four quadrants are answered about the *shared layer only*;
anything true of a subset is delegated. At **Band 0** the profile is written in past tense with a present-tense
appendix for what the ruin still does to visitors.

**Type variance.** A **Corridor's** strength is throughput and its standing cost is almost the whole profile. A
**Natural feature's** profile is entirely G2 and is written as what it does to everyone who deals with it. An
**Interstitial** location uses `01` §1.3 instead.

**Feeds:** everything. Nothing downstream is written without it.

**Failure modes.**
- Stopping at first-order on the physical generator. *"It is cold"* is a starting condition, not a finding.
- Writing a capability profile as a **diagnosis** rather than a profile — the district rule holds: strengths and
  deficits stated as what the place can and cannot institutionally do, **then one consequence.** If the
  consequence reads like another location's, it is wrong.
- Filling the STANDING COST quadrant with function. They are different questions (`02` §3.1).
- Letting the profile become a list of prohibitions. Prohibitions are Phase 7.

---

# PHASE 2 — COMPOSITION & ARRIVAL

**Asks:** *Who is actually here, in what proportion, from where — and by what route did they come to be here?*

**Restores** city template §1 (composition) and §7 (who this place attracts and repels), neither of which the
district set inherited as a phase.

**The core move — the arrival-mode taxonomy.** *How* a population arrived shapes a location more than where it
came from, and this is the phase's main generative instrument. Very few places are one mode; **the mix is the
finding.**

| Arrival mode | What it produces |
|---|---|
| **Chose it** | Self-selection. The place has a *type* and knows it. Ask what it **repels** — that answer is usually sharper than what it attracts. |
| **Assigned / posted** | An institution sent them. Produces a population that did not choose each other and a **rotation clock** — everyone knows when they leave. |
| **Fled to it** | Arrived because somewhere else failed. **Gratitude and resentment in the same population**, often in the same person. |
| **Born here** | Never chose, and frequently cannot leave. **The most under-written mode** — a place written entirely from arrivals has no natives, and the natives' relationship to the arrivals' story is a whole finding. |
| **Inherited it** | Came with the place — acquired, annexed, absorbed. Produces a population whose membership was decided elsewhere. |
| **Sentenced to it** | Punitive. Produces a permanent status distinction that outlives the sentence. |
| **Stopped while passing** | Meant to leave and did not. Produces people with an unexecuted plan, which is excellent character material. |

**Process.**
- **A.** Establish the composition from canon; **read the composition source for its own stated limits** and do
  not build a finding on a percentage that the source says is a relative ranking.
- **B.** Classify the arrival modes and their approximate mix.
- **C.** **Separate the native layer from the transplanted layer, explicitly** (`Cultural_Synthesis_Techniques`
  §12). Read the composition material *to know what to write around*, not what to repeat. **A place whose only
  culture is its immigrants' cultures has no culture.**
- **D.** Run **Borrowed Form** where a later category comes up empty — but not to skip the capability reading;
  a borrowed form should explain a gap the capability reading already predicted.
- **E.** Ask **who is not here.** An absent population is as characterizing as a present one, and much less
  often asked.

**Band variance.** **Band 1:** name them. The list *is* the composition, and the variance across a dozen people
is the culture. **Band 4+:** composition varies internally and must be patterned rather than averaged. **Band
5–6:** composition is a distribution; the finding is its *shape* and its modes.

**Differentiation axis.** Name the mode-mix in three or four words — *"posted majority with a stopped-passing
minority"* — and check it against siblings.

**Feeds:** Phase 4 (whose ordinary day), Phase 5 (who the visitor is), Phase 9 (which populations exist).

---

# PHASE 3 — SURFACE & TEXTURE

**Asks:** *What is this place made of, and what is it like to be inside it — to the eye, ear, nose, and skin?*

**Inherits** district Phase 1 (Architecture, Sensory Profile) and city template §9, §14, plus §3–4 (climate
character, seasonal rhythms), which the district set dropped because thirteen districts share one climate.

**Process.**
- **A.** **Formalize first.** Sensory and architectural material is very often already present in a location's
  existing files under headings that are not called either.
- **B.** Answer the four sensory sub-fields **separately** — Sound, Smell, Feel, First impressions. Do not
  collapse them; a place can be visually calm and acoustically tense, and losing that loses the finding.
- **C.** **Check for a public/institutional split.** Many locations have a street-level sensory register that
  differs from what their institutions feel like inside.
- **D.** **Look for the seam.** Is there a visible boundary between the founding-era build and anything added
  under later pressure? *(The two-stage lens, generalized: any location with a founding era and a crisis era.)*
- **E.** **Seasonal variance**, restored from the city template: what does this place become at its worst point
  in the year, and is that the same place?
- **F.** Run **Retroactive Mechanism** — what is established as simply true here that nothing explains, and what
  physical system would produce exactly that? **It generates a second-order consequence for free.**

**Type variance.** A **Corridor's** texture is its waypoints and its surface underfoot. A **Network locus's** is
latency, interface convention, and what the channel does to a voice. A **Structure's** is its interior
circulation. **Band 0:** what remains, and what the remains testify to.

**Failure modes.** Writing the sensory profile of the location's *headline institution* as the general answer.
Inventing texture that the physical constraint from Phase 1 does not support.

**Feeds:** Phase 4, Phase 5 (first impressions), Phase 10 (you cannot name places before you know what they
look like).

---

# PHASE 4 — ORDINARY LIFE

**Asks:** *What is an ordinary person's day here, apart from what this place is famous for?*

**The best generator in the district set**, and promoted here to run as early as its dependencies allow.

**The core move, stated as sharply as the district file states it:** **name the headline function in one
sentence, then deliberately write away from it.** If a draft could be summarized as *"residents do [the headline
function] all day, described in more detail,"* it has failed. Restart from what a resident does *between*,
*despite*, or *entirely unrelated to* that function.

**The test:** *would this reasonably be someone's entire day, every day, forever?* If yes, it is wrong.

**Why it outperforms.** Phase 1 says what the place cannot do. **Phase 4 is where you find out what that costs
an ordinary person between one hour and the next** — and the third-order consequence of a capability deficit
almost always shows up in somebody's Tuesday rather than in an institution.

**Process.**
- **A.** State the headline function. Write away from it.
- **B.** Cover **four distinct elements** — routines, mundane concerns, personal struggles, and
  escapism/downtime. They are genuinely different and a pass that collapses into a schedule or a hobby list has
  covered one. **Escapism is the one most often cut for space and it is explicitly required.**
- **C.** **Do not write one universal resident.** Different arrival-mode populations (Phase 2) have different
  days.
- **D.** Use **physical scale** for commute and logistics texture — real, concrete, non-thematic mundane
  material that costs nothing to derive.
- **E.** Ask what the ordinary rhythm **fails to provide** for people whose lives do not fit it.

**Band variance.** **Band 1:** there is no ordinary day — there are twelve specific days, and their divergence
is the content. **Band 5–6:** there is no single ordinary day either, for the opposite reason; ask instead what
is common to *all* the ordinary days across the distribution, which is usually a very short list and is exactly
the interesting part. **Band 0:** the transit day — the maintenance crew, the convoy, the scavenger.

**Differentiation axis.** What the day is *organized around* — a shift, a tide, a light cycle, a queue, an
arrival schedule, nothing at all.

**Feeds:** Phase 6 (countercultures seed here), Phase 7, Phase 9, and it is the **best contradiction detector in
the file** for every other phase (`04` Gate 3).

---

# PHASE 5 — RELATION & GEOMETRY *(the restored phase)*

**Asks:** *What is this place to the places around it, to the thing that contains it, and to anyone crossing its
edge?*

**This phase exists because its absence was measured.** It restores city template §23 and closes the hole `00e`
§6 names. **It is mandatory for every type and primary for two.**

**The core move.** **Write a relation as a mechanism, not a rivalry.** The useful question is never *who dislikes
whom* — it is ***what does each side refuse to develop, and who supplies it instead?*** Relations of this kind
are feedback loops, not standoffs.

## ⚠ Weighting depends on whether this location actually has neighbors — and usually it does not

**Added 2026-08-30, after the first test run exercised this phase on the most densely-clustered location set in
the project and mistook a best case for a measurement.**

**Most locations are isolated.** Tepenia's cities sit 100–600 km apart; stations, structures and natural
features frequently have no peer at all. **A phase written as though every location has close neighbors will
return thin for the majority case** — so the sub-questions are weighted, not uniform:

| Sub-question | **Isolated location — the majority** | Clustered location — rare |
|---|---|---|
| **5a** Peers | **Optional.** Often the honest answer is a *category* ("the coastal cities"), not a name | Mandatory |
| **5b** Three-way set | **→ use the own-eras substitute below** | Mandatory |
| **5c** The parent | **PRIMARY — this is where an isolated location's relational content lives** | Mandatory |
| **5d** Edge & crossing | Mandatory | Mandatory |
| **5e** Dependency | **PRIMARY** | Mandatory |

**The good news, verified rather than assumed: four of the five sub-questions are peer-free.** 5a's core move
*(mechanism, not rivalry)* works against a supplier, a parent, or an absent peer just as well as against a
neighbor — **it never needed a neighbor, it needed a counterparty.** Only 5b genuinely requires siblings.

> **And for an isolated location, "write both directions" has a specific and valuable second half:** very often
> the honest outward answer is ***nobody out there thinks about this place at all.*** **That is a finding, not
> a blank.** A location that matters intensely to itself and to nobody else is a specific, common, and
> characterizing condition — write it.

**Five sub-questions:**

**5a — Peers.** Who is this place set against, adjacent to, in easy affinity with? For each: what flows, in
which direction, and what does not. **Distinguish the loud friction from the quiet one — the quiet one is
usually nastier and better material.** *(Optional for isolated locations — see the weighting above.)*

**5b — The three-way differentiation set.** *(The most reusable trick in the district folder.)* This location
plus its two hardest frictions makes a **natural three-way contrast for any single behavior category**, because
the geometry guarantees they differ on the same axis without overlapping. **Pick the category first, then read
all three off the geometry** — deriving one location's answer alone tends to produce something generic, because
there is nothing to differentiate against.

> **⚠ THE SUBSTITUTE, for the majority case where there are no two peers to contrast against.**
> **This is the only sub-question that genuinely requires siblings**, and a reader reaching it alone previously
> had nowhere to go.
>
> **Run the three-way set against the location's own eras instead of against neighbors:**
> ***this place at its founding · this place at its crisis · this place now.***
>
> **Same procedure — pick one category first, then read all three states off the timeline.** `01` §5.3a already
> names a location's own earlier states as *"the strongest substitute, usually available"*; **this is where it
> actually gets used.** It pairs directly with the two-stage lens in `01` §4, and with the *"in its own past"*
> deficit address in `02` §4.1 — **if the address came back "in its own past," this substitute is not optional;
> it is the phase.**
> **The sets are a network, not independent triples.** A location accumulates characterizations from other
> locations' passes. **Check what this location was already assigned in someone else's set** before writing a
> new one; where they conflict, the earlier one usually wins because it is already load-bearing.

**5c — The parent.** What does the containing polity require of this place, what does it supply, and **where do
those two disagree?** *(This is G3's split question from `02`, cashed out relationally.)* Also: what does this
place believe about the parent, and is it accurate?

**5d — The edge and the crossing.** Who arrives, by what route, and what do they meet first? **Enumerate the
actual arrival types** — they are rarely one. *(The district translation of "visitor" required a definition task
of its own; at every scale, ask what "outsider" even means here before answering what their experience is.)*
And then: **what converts a visitor into a member?** Prefer a **mechanism over a ceremony** — derived from the
local economy, with no announcement and often no awareness that it has happened.

**5e — Dependency.** What does this place need from elsewhere that it cannot make, and **who knows that?** A
dependency nobody has named is a shadow; a dependency everyone has named is politics.

**Type variance.** For a **Corridor** and an **Interstitial** location this phase is the primary one and most of
the content lives here. For a **Vessel**, relation is to *ports* rather than to neighbors, and the finding is
usually what it is like to have relations with places that do not have a relation with you.

**Failure modes.**
- Writing rivalry instead of mechanism.
- Writing only the outward direction. **Relations are asymmetric and both halves must be written** — what they
  think of us is a separate finding from what we think of them, and the gap between the two is often the best
  material available.
- Skipping 5c because the parent is unwritten. **Use the provisional-assumption protocol** (`01` §5.2) instead.

---

# PHASE 6 — MEANING

**Asks:** *What does this place believe, what does it hold sacred without saying so, and what does it do about
death?*

**Process.**
- **A.** **Run the Naming technique first, before generating anything.** Search the location's existing canon
  for religious-register language attached to non-religious objects — *sacred, honor, sworn, kept, owed,
  witnessed, proper, must, never*. **A registry described as "close to sacred" is a theological statement about
  a filing system, and it is already written down.** Then state, as one sentence a resident would agree with,
  the proposition that would have to be true for that language to make sense. **Only if the search comes back
  empty do you generate from scratch.**
  > **The technique's real object is the location's *unnamed load-bearing thing*, and a belief system is only
  > its commonest form.** Where the place already has a named faith, expect instead a **stake** (what is at risk
  > here that is at risk nowhere else), a **compact** (what it agreed to and never wrote down), or a **debt**
  > (what it owes and does not discuss). **Do not invent a second religion to fill a slot already occupied.**
  > **Counter-check: the name must not be portable.** If it would work equally well for a sibling, it has been
  > written too abstractly.
- **B.** **Belief landscape.** Draw on the existing roster before inventing; but a genuinely new belief emerging
  from the analysis is a good outcome, not a problem, **provided it grows out of something the place verifiably
  already has** — a physical trait, a founding wound, a function, a practice nobody had named.
- **C.** **Death and the dead.** *(The category the 32-section template has no slot for at all.)* **The question
  is obligatory; a section is not.** Ask: who handles it · what is remembered, by whom, for how long *(distinguish
  the **record** from the **rite**)* · **who is not mourned properly, and why not** *(the most productive of
  these, and usually a shadow finding)* · and **is the absence itself the finding** — if so, say *why*, because
  a place that outsources its dead for lack of room, for lack of anyone yet to bury, or because it would rather
  not look, are three different places. **A thin invented rite is worse than an honest sentence.**
- **D.** **The Failure State of the Core Value.** What is this place's central promise; under what circumstance
  does it become impossible to keep; what grew up around that circumstance; **and does the culture ritualize the
  failure or refuse to?** *The refusal is often the stronger half.*
- **E.** **Observance.** Two to four, and **at least one small and unserious.** One ordinary, slightly silly,
  genuinely enjoyed local holiday does more for a place's livability than a third memorial day.

**Band variance.** **Band 1:** belief is what these specific people believe, and they may disagree — the
disagreement is the content. **Band 5–6:** belief is a distribution; write the shared thin layer and the
distribution's shape, not a single creed.

**Failure modes.** Giving every location a bespoke religion. All-solemn observances. Manufacturing thirteen
divergent funerary traditions in one shared environment, which is its own differentiation failure.

---

# PHASE 7 — ORDER

**Asks:** *How does this place organize work, decide things, pass on skill, and handle the people who do not
fit?*

**Restores** city template §15 (division of industry) and §21 (political character), and takes prohibition and
sanction from Phase 1 per `02` §3.3. **Primary phase for Polity and Installation types.**

**Four components.**

**7a — Work and economy.** The division of labor; what it makes; what it sends outward. **Include the
non-thematic export** — something ordinary, emotionally neutral, and unrelated to the headline function, which
proves the economy is real rather than allegorical. **And do not force export into goods** where the real export
is people or expertise.

**7b — Governance and decision.** Who decides, by what legitimacy, and how succession works. **The most
productive question here is not who holds power but *what is unadministrable*** — the rule that cannot actually
be enforced, the decision nobody is empowered to make, the edge case nobody wrote. **Prohibitions live here**,
and are distinct from the capability frame's grudging tolerance: a prohibition is a chosen policy with an
author.

**7c — Knowledge and transmission.** How does someone learn to do the thing this place does? Apprenticeship,
qualification, the unwritten rules nobody explains — **and what becomes of the ones who cannot learn it.** *(The
Mentor's standing question, promoted to a phase component because it is too load-bearing to leave to the review
panel.)*

**7d — Private life, minorities, and counterculture.**
- **Check canon for an existing counterculture before deriving one.**
- **Derive from the specific pressure, never from generic rebellion.** *What does this place require of
  everyone, and who cannot or will not give it?* That population is the counterculture.
- **Do not default to a refusal.** A counterculture can **refuse** what the place demands, **perform what the
  place cannot**, or **demand the place's own stated rule be applied more literally than the mainstream applies
  it.** The second is rarer, more interesting, and much likelier to be missed — **check for it deliberately
  wherever the capability reading has named a faculty the place lacks**, because that is exactly where someone
  will be doing it unofficially.
- **And check whether the dissent is a *population* at all.** It may be that the contradiction sits *inside each
  person* rather than between factions — in which case there is no counterculture, and the consequence is worth
  having: such a place **cannot be reformed from within and cannot be opposed from within either, because there
  is nobody to organize.** Ask: *is the contradiction between groups here, or inside each person?*
- **Keep it sympathetic, not criminal.** These are people the demand does not fit.

**Sanction proportionality — a hard check.** *(`00d`, generalized.)* Before writing any exclusion or penalty,
**price it in this location's physical conditions.** The same sanction is not the same act in two places:
exclusion where outside is lethal is a death sentence; exclusion in a network locus is being unfollowed. **Ask
what it physically costs the excluded person here, and whether this place would actually pay that price for that
offence.** And do not scale one person's temperament into a civic sanction — an individual's impatience scales
to *a smaller room and a shorter hearing*, not to a policy.

**Band variance.** **Band 1:** governance is a conversation between named people, and the interesting question
is what happens when two of twelve disagree permanently. **Band 6:** this is the primary phase, and the subject
is the maintenance machinery of the thin shared layer.

---

# PHASE 8 — MAKING

**Asks:** *What does this place cook, sing, wear, build, play, and say?*

**Governing discipline: native, not transplanted.** This phase covers what the location **itself developed**.
Read the composition material to know what to write *around*.

**Components.** Cuisine — **all populations present**, and the non-human population's version is the most
skipped item in this project's entire template · Music · Arts, craft and material culture · Dress and
appearance · **Play, sport, humour, leisure** · **Language and speech markers** *(city template §8, absent from
the district set entirely: accent, code-switching, slang, and what dialect reveals; and what marks someone as
from here)*.

**Process.**
- **A.** Native layer first, transplanted second, kept visibly separate, then how the two now interact.
- **B.** **Start from function, not aesthetics** — for dress especially. What would someone doing this place's
  actual daily work need to wear, and what does that need becoming custom look like after two centuries?
- **C.** **General-population discipline, hardest here.** A place's professional performers are not its musical
  culture; a uniform is not its fashion. **This category has failed more often than any other in the district
  set.**
- **D.** **Name the axis.** Food across twelve districts runs admission · rank · position-in-a-process · ambient
  availability · unspoken repair · no cuisine at all · guesthood · duration · attention · inclusion-in-the-count
  · unpaid time. **Eleven answers, eleven axes, no repeats — which is why the row has never collided.**

**Band variance.** **Band 5–6:** delegate; write the pattern of variation and the few genuinely shared items.
**Band 1:** what these specific people make, including the fact that one of them is the only person who can.

**Failure mode.** Treating this phase as the fun one and writing it first. It depends on Phases 1–7 and reads
as decoration without them.

---

# PHASE 9 — POPULATIONS

**Asks:** *What is life here like for each distinct kind of person present, and how do those kinds relate?*

**Generalizes** district Phase 8 (Robot-Specific Culture) and city template §16–17 from "robots and humans" to
**whatever population categories the setting actually contains.** In this project that is robots and humans; the
project's own representation framework names four categories of which only one is in use, and any future project
may have others.

**The lens decision, which must be made explicitly per location type.** The outer-city version anchors robot
culture in **founding-nation** threads; the district version anchors it in **theme/role**, because districts are
not nation-founded. **Neither is universal.** Decide and state the anchor: what does *this* location's
non-dominant population organize its culture around — origin, function, the built environment, a shared
constraint, or a shared exclusion?

**Process.**
- **A.** Declare the populations present and the lens for each.
- **B.** Per-population culture, drawing on every prior phase.
- **C.** **Inter-population relations — find the local inflection, not the national baseline.** Restating the
  setting's baseline is not a finding. **The strongest available move is that the place reorganizes its
  population along a different axis entirely** — ask *is there a category here that matters more than kind?* If
  so, that is the finding, and the inter-kind question answers itself underneath it.
- **D.** **Dual-tag every finding:** an **inheritance** tag (directly inherited / adapted / genuinely emergent)
  and a **depth** tag (surface / deep). **Findings clustering entirely in "directly inherited" or entirely in
  "surface" mean the real work has not happened yet** — that is what the tags are for.
- **E.** **Swap test.** Would this survive unchanged if the location's name were swapped for its nearest
  comparable? If yes, it has not localized.

**Type variance.** For an **Installation**, the population split is often staff/non-staff or
permanent/rotational rather than by kind, and that split may matter more.

---

# PHASE 10 — CATALOG

**Asks:** *What is actually here — named, specific, and enterable?*

**The systematic follow-through on everything above**, and what gives every other phase somewhere to happen.

**Governing premise:** a place is built around a **theme, not a thing.** A caregiving district is not wall-to-wall
clinics any more than a real government town is wall-to-wall ministries. **Catalog the wider cast refracted
through the theme, not restating it literally.**

**Four categories, kept separate:**
1. **Named places and landmarks** — specific, not institution-types.
2. **Physical things** — what residents own, use, encounter.
3. **People as role-archetypes** — **binding rule: no invented proper names.** *"A veteran repair-shop owner,"*
   *"the neighborhood's informal mediator."* The developer names these personally once the roles exist.
4. **Settings** — atmospheric and situational textures distinct from named landmarks: a kind of street corner,
   a recurring situation.

**Plus, restored from the city template:** **significant local events** (§30) and **notable figures** (§31, as
placeholders under the same naming rule).

**Process.**
- **A.** **List every implied-but-unnamed place, thing, person and setting from Phases 3–8 before inventing
  anything.** Expect real recoverable material; a resident's routine has to happen somewhere, among someone,
  using something.
- **B.** Run the real-world research against the location's full pick list, **prioritizing the lower tiers** —
  top-tier picks get absorbed into a location's identity summary early and spent, while lower tiers sit
  unexamined and still hold unspent specificity.
- **C.** Organize under the four headings; **name places and things specifically, leave people as roles.**
- **D.** Check border-adjacency texture where the location abuts a neighbor whose character might bleed across
  — **a real but easy-to-overuse technique; do not force it.**

**Band variance.** **Band 5–6:** delegate to sub-locations; catalog only what is genuinely national. **Band 0:**
this phase is large — what is *left* is most of what a ruin has.

---

# 11. What the phases do not cover, stated honestly

Recorded so the next pass does not assume completeness.

- **Mechanical and systems design** — quests, encounters, loot, level geometry. This spine produces the material
  those draw on; it does not produce them.
- **The physical map.** Adjacency and layout are inputs here, not outputs.
- **Anything below the location scale** — a single building's interior, an individual character. Characters have
  their own methodology.
- **Validation.** Nothing in this file has been run on a real location yet. **See the README's status note.**
