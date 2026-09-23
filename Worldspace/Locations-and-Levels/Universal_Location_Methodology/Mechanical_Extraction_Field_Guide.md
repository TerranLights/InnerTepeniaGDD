# Mechanical Extraction & Datasheet Field Guide

**Corpus-wide instrument. Added 2026-09-15, at the developer's direction.** Companion to
`00_RUNBOOK.md` and `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` — this file does not replace either. It exists to stop
one specific, repeated cost: rebuilding, by hand, a fact that a prior step already located and cited, every time
a later step needs the same fact again.

> ### ⭐⭐⭐ THE GUARDRAIL, STATED FIRST, BECAUSE IT MATTERS MOST
> **A datasheet answers "what does the source say," never "what does it mean."** Every phase's own Process/
> interpretive steps remain fully mandatory and unabridged. **T8 Round 1 continues to open ALL primary
> MUST-OPEN sources in full, exactly as it does today** — a datasheet is consulted *alongside*, never *instead
> of*. It exists to remove the redundant re-transcription of an address or a number already correctly extracted
> and verified — never to remove the reading that produces an actual finding. **`LAW 0`/`LAW 0-R` are untouched
> by this entire instrument.**

> ### ⛔⛔⛔ NO LONG NIGHT WAR OR POST-WAR CONTENT IN A DATASHEET. AT ALL. EVER. — added 2026-09-15
> **Developer instruction, given with maximum force, after this exact leak recurred across all three cities'
> datasheets built so far.** A datasheet's default scope is the Second Interwar Period — peacetime, the
> Tepenian Federation as a proper country. **The Long Night War, "post-war," a city's destruction, its ruined
> status, its refugee populations, and any later-era condition are NEVER admissible content here, in any form
> — not as a recorded fact, not as a quote, not as a reason for excluding something else, not even inside a
> sentence explaining that a field is excluded.** ⛔ **Do not name the war to justify skipping it.** When a
> Specs field (`Status:`, `Current Status`, `Connection to Concordia`, `Legacy`) states a later-era condition,
> record only that it is **excluded per the standing default-scope rule** — never quote it, never describe
> what it says, never explain it was caused by the war. This is not the same failure as a cross-city reference,
> but it is caught the same way: **sweep every datasheet for `war`, `destroyed`, `destruction`, `ruins`,
> `post-war`, `damaged`, `refugee`, `casualty`, `abandoned` (city-status sense, not e.g. a real pre-exile ruin,
> which is a separate GPS-admissible category) before treating a city's datasheet folder as done.**

> ### ⛔⛔⛔ A SUMMARY IS NOT ITS SOURCE — **twice-measured 2026-09-16, both times within one session**
> **Both failures had the identical shape: an accurate summary that elided the qualifying half, trusted instead
> of the full text — and both times the narrow reading was the MORE VIVID one, so the incentive ran toward the
> elision.**
>
> | # | What was trusted | What the full source said | Cost |
> |--:|---|---|---|
> | **1** | Three isolated readers' quotations of a treaty clause, byte-verified 30/30 | ***The clause's fourth ground — a broad residual, "or otherwise established their life among the robot population" — was read past.*** A headline was built on a criterion that does not exist | A withdrawn headline in a written phase file, plus the same error sitting in a **Tier U sheet every city reads** |
> | **2** | A research folder's checklist summary of its own extraction | ***The full extraction had TESTED and WITHDRAWN the very mechanism the summary's one-liner named.*** The summary said *"frost wedging in the joints of rock"*; the extraction said a freeze-thaw account here *"would have been confident, coherent, physically plausible — and wrong"* | A rewritten phase file — and the correction had been on disk the whole time |
>
> ⭐⭐ **THE TWO RULES THIS YIELDS, BOTH OPERATIONAL:**
> 1. ***A FOLDER'S DATA IS NOT THE SAME AS THE FILES INSIDE THE FOLDER.*** **Check whether a research folder's
>    own index points at output files living elsewhere** — `Davis_Geosciences_Research/` holds 2 files and its
>    data is 4, the other 2 being one directory up. **A datasheet row that gives a folder's file count without
>    chasing its pointers is an incomplete row.**
> 2. ***WHEN A PHASE BUILDS ON A SINGLE ENUMERATED CLAUSE OR A SINGLE NAMED MECHANISM, OPEN THE FULL TEXT.***
>    **Quote every ground, including the residual; read the extraction, not the checklist line.** ⛔ **T8 does
>    not catch this: Round 2 proves a span was READ, never that it was read to the END.**

> ### ⛔⛔⛔ AN UNDEVELOPED PART OF THE PROJECT IS NOT A CHARACTERIZATION OF THE CITY — developer ruling, 2026-09-16
> **Developer, on a phase that had built its headline out of four absences:** ***"those details 'don't exist'
> because we haven't figured them out yet."***
>
> ***These passes run on an incomplete corpus. Absence in the admitted set is the DEFAULT CONDITION, not
> evidence.*** ⛔ **A phase that reads "unwritten" as "does not happen" will manufacture a confident, coherent,
> internally consistent false character — for any city it touches — and it will propagate, because absence is
> the claim class nothing downstream re-checks.**
>
> ⭐⭐ **`M-171` separates two states. There are THREE:**
>
> | State | Status |
> |---|---|
> | *"I did not look"* | ⛔ **A HOLE** |
> | *"I looked, and the source is silent on it"* | ⛔⛔ **ALSO A HOLE — this is the one that gets mistaken for a finding** |
> | *"I looked, and a source AFFIRMS the absence"* | ✅ **A FINDING, and the only one of the three that may be characterized** |
>
> ### ⭐ THE TEST, IN ONE QUESTION
> > ***Does a source AFFIRM this absence — or has no source addressed it yet?***
>
> **Worked both ways, same session, same city:** ✅ a national infrastructure file that EXISTS and does not list
> the city is an affirmable absence *(the city's heat is supplied, not local)*. ⛔ A relations file describing
> connections as *"a natural first-time cross-reference once full connectivity exists"* is an **authoring
> note** — the connection is undeveloped, and reading it as *"the city is characteristically unconnected"* is
> the error.
>
> ⚠ **And the tell is seductiveness:** **the undeveloped reading is almost always the more vivid, more
> characterful sentence.** ***That is exactly why it gets written.***

## What this is, in one line

This file lists, **per Step and per Phase, generalized across every city**, which categories of information are
*pure lookup* — no inference, no synthesis — so a future pass can go straight to extracting real values instead
of re-deriving the category list. **It names categories, never values.** Real values live in datasheets, built
per the convention below.

## The two-tier split

| Tier | What | Built | Where |
|---|---|---|---|
| **U — Universal Reference Sheets** | Content identical across every city: law text, fixed rosters, fixed definitions | **Once**, corpus-wide | `Corpus_Reference_Sheets/` *(this folder)* |
| **C — Per-City Datasheets** | Content that varies by city: census rows, composition tiers, spec facts, climate normals, route connections | **Once per city** | `<City pass folder>/Datasheets/` |

A Tier C datasheet **cites into** a Tier U sheet rather than re-quoting it.

## ⛔⛔ The bright-line test — what counts as "zero thought," precisely

A category qualifies for a datasheet **only if**:
- **(a)** the source states the value directly — a number, a name, a list, a status token, a date, a coordinate,
  a law's literal text. No inference, no "reading between the lines."
- **(b)** transcribing it produces **no new claim** about the location beyond what the source already asserts.
- **(c)** a **fixed arithmetic formula** applied to two stated numbers (retention % from two census figures,
  density from population ÷ area) counts as mechanical **for the computation itself** — the formula is
  established practice, not a fresh judgment call. ⛔ **The SIGNIFICANCE of the result is never mechanical** — a
  datasheet may say `retention = 67.48%`, never *"this reveals a defect-free departure."*

**Always excluded, no matter how simple the source reads:** any finding, verdict, characterization, "shape"
assessment, generator profile, comparison (even to the location's own earlier state), any phase's actual "Asks"
question, any QA gate's pass/fail call, any Review Panel disposition, any T8 headline.

## ⛔⛔⛔ A second, independent exclusion — sequencing beats mechanical-ness

Some MUST-OPEN sources carry a rule about *when* they may be opened, not just what they say. Pre-staging their
content early would violate that rule regardless of how simple the content is to transcribe.
**Permanently excluded from any datasheet, at any tier:**

| Source | Rule | Why pre-staging is a violation, not a shortcut |
|---|---|---|
| `Local_Cultures/<Subnet>/<City>.md` | **READ-LAST, as a CHECK** | In a warm run nothing else enforces this — the sequencing rule IS the enforcement |
| `Local_Robot_Culture/<Subnet>/<City>.md` | Same | Same |
| `City_Megasheets/<Subnet>/<City>/…` | **WITHHELD, corpus-wide** | Withheld means withheld — a datasheet is still a read |
| A phase's own RESERVED question (e.g. Phase 6's mortuary question) | **RESERVED — do not answer** | The reservation is a standing refusal, not a content gap |
| `Cross_City_Culture_Differentiation_Table.md` | **WRITE-ONLY** (Step 6) | Never read another city's cell, mechanical or not |
| `City_Vision_Notes/` | **STRUCK corpus-wide** | Moot — already fully excluded |

## Two further standing rules

- **A datasheet entry is a value + its citation** (source file, exact line/range) — nothing else. No adjectives,
  no synthesis, no cross-city comparison, ever, at either tier.
- **A computed value states its formula and both input citations**, so a later reader can verify the arithmetic
  rather than trust it — the same discipline `DR-6`/T8 already apply to reading.

---

# ⛔⛔⛔ TWO RULES THAT GOVERN THE LIST BELOW — **read before using it**

**Added 2026-09-16, from a measured failure. Both exist because the list below was treated as sufficient and it
is not.**

## ⛔⛔ RULE 1 — **THE SPINE'S `MUST OPEN` LIST IS THE CONTRACT. THIS CATEGORY LIST IS A FLOOR.**

**The per-phase categories below are a GENERALIZATION written by this guide. Each phase's own `📂 MUST OPEN`
block in `03_The_Phase_Spine.md` is the actual requirement.** ***They do not match, and where they differ the
spine wins.***

> **Procedure, per phase, every city: open the phase's `MUST OPEN` block, tick each address off against the
> datasheet, and record the coverage count in the datasheet itself** *(e.g. **"13 of 13"**)*. **A datasheet that
> does not cover the spine's list is INCOMPLETE and must say so at the top.**

⚠ **MEASURED — Davis, 2026-09-16.** **Datasheets built from this category list under-listed on FOUR of five
phases run:**

| Phase | What the category list missed |
|---|---|
| **3** | `<City>_Geosciences_Research/` entirely — **the phase's richest input** |
| **4** | `National_Economy_and_Currency.md` · `11_Caloric_Rebuild_and_Livestock_Tier.md` |
| **5** | `Geothermal_Heating.md` *(a 198-line zero that turned out load-bearing)* · `Ports.md`'s actual row |
| **7** | ⛔⛔ **7 of 13 items, including the one the spine flags "READ ITS CARVE-OUTS FIRST"** |

⭐ **`M-169` already states the principle and it is the same one: *opened-and-empty is a RESULT; unopened is a
HOLE.*** **A category list cannot produce that distinction; only an address list can.**

## ⛔⛔ RULE 1b — **A DATASHEET CARRYING A CONCLUSION STOPS BEING INPUT AND BECOMES PRE-SEEDED OUTPUT**

**Added 2026-09-16, from a developer ruling and a measured audit.**

> **Developer, 2026-09-16:** ***"Those datasheets should be copy-pasted information that the ULM actually
> requires."*** **And, on the un-run cities specifically:** ***"Casey and Mirny should not have 'conclusions.'
> They should only have copy-pasted data so that you don't need to go looking for shit during what are supposed
> to be the productive hours."***

⭐⭐⭐ **THIS ALSO RESOLVES AN APPARENT CONFLICT BETWEEN TWO INSTRUMENTS, AND NEITHER NEEDS AMENDING.**
**`00_RUNBOOK.md` Step 10 item 7 forbids a pre-existing output folder for the next run — *"a contamination risk
and a status lie."*** **This methodology REQUIRES `<City>/Datasheets/` to exist in advance.**

| | |
|---|---|
| ✅ **A COMPLIANT datasheet** — transcription only | **INPUT.** ***Item 7 does not apply*** |
| ⛔ **A NON-COMPLIANT datasheet** — carrying synthesis | ***PRE-SEEDED CONCLUSIONS. Item 7 catches it, and is right to*** |

⇒ ⭐⭐ ***The conflict was never between the instruments. It was drift in the artifact.***

> ### ⛔⛔ AND FOR AN UN-RUN CITY IT IS CIRCULARITY, NOT MERELY UNTIDINESS
> **`05` §6.1: *an input must not be a prior culture-pass CONCLUSION about the same location.*** **A conclusion
> sitting in a datasheet for a city whose pass has not started is exactly that — ***the pass would read its own
> answer and call it research.***

### ⭐ THE COMPLIANCE CHECK — run before declaring a datasheet set done

```bash
# Inference markers have no place in a value+citation artifact.
grep -rn "⇒\|therefore\|which means\|the real\|this is the" <City>/Datasheets/*.md
```

⚠⚠ **THE SCAN OVER-REPORTS, AND ITS HITS MUST BE READ, NEVER STRIPPED ON THE MATCH.** **Measured on a real
audit: 7 hits, and SIX were legitimate** — *a procedural refusal (`"not recorded as fact here; a T8 dispatch
must adjudicate"`), the word `real` inside a QUOTED source correction, and methodology notes that make no claim
about the city.* ⭐ **Only one was a genuine authored label wrapped around a legitimate quote.**
⇒ ***`M-237` applies to this check as much as to any other: a pattern match is evidence about the pattern.***

**What a compliant row looks like:** ✅ **a neutral label naming the FIELD** · **the source's own words or
figures** · **the citation.** ⛔ **No verdict, no "⇒", no characterization of the place.**
✅ **A REFUSAL is permitted and encouraged** — *"not recorded as fact here, because X"* is a handling
instruction, not a conclusion.

---

## ⛔⛔ RULE 2 — **A `RELIABLE` STAMP IS NOT A BLANKET WARRANTY. READ THE FOLDER'S OWN `README` FIRST.**

**A source folder may be marked settled at the top and void an entire layer of itself a few lines down.** ⛔ **A
datasheet that extracts figures from such a folder without carrying its carve-out is worse than no datasheet:
it presents withdrawn numbers with a citation attached.**

> ### ⚠ THE MEASURED CASE
> **`Division_of_Industry/README.md` opens `STATUS: RELIABLE` on line 1 and, on line 3, voids its entire food
> layer** — *"circular, double-counted, and stated in the wrong units."* **ZERO of the corpus's 57 existing
> datasheets carried that carve-out**, which left **38 independent chances to cite a withdrawn figure.**
> ⇒ ⭐⭐ **Fixed structurally, and this is the pattern to copy: a carve-out identical across every city belongs
> in ONE Tier U sheet, cited by all of them** — `Corpus_Reference_Sheets/Division_of_Industry_Reliability_Quick_Reference.md`.

⭐⭐ **And when writing that sheet, state what IS citable, not only what is not.** **The first draft of the DoI
sheet repeated `README`'s own sentence — *"`DRQ-09` blocks every export figure"* — which was LOOSER than the
evidence and caused a phase to hole a figure that was in fact settled.** ***A gate that over-blocks costs real
findings; give the precise term that fails and leave the rest citable.***

---

# Per-Phase field guide (0–10)

> ⚠ **A FLOOR, NOT A CEILING — see RULE 1 above.** **Walk `03_The_Phase_Spine.md`'s own `MUST OPEN` block for
> the phase and tick every address; this list will be missing some of them.**

*(Categories only — generalized across cities. Real values are what Tier C datasheets fill in per city.)*

**Phase 0 — Frame.** *Tier C:* Census I row (H/R/total) · Census II row · coordinates/real-world basis name.
*Tier U:* `Repo_Scope.md`'s boundary statement · ⭐⭐⭐ **the applicable Timeline Era — for this run, THE
SECOND INTERWAR PERIOD, corpus-wide, not a per-city judgment.** Full content already extracted at
`Corpus_Reference_Sheets/Second_Interwar_Period_Quick_Reference.md` — **cite that file directly; do not re-open
`Timeline Eras/2 The Second Interwar Period/README.md` per city.** **Not mechanical:** the declaration block
(type+modifiers), generator selection, the asymmetry check, reserved decisions.

**Phase 1 — Constraint & Capability.** *Tier C:* Specs' `Access type:` token · Specs' other directly-stated
physical facts · Climate READER's full stated-normals table (⚠ resolve via the ALIAS SET, not the city name) ·
this city's `G3` figures from `16_Per_City_Three_Tier_Run.md` Half B (⛔ schema query, never grep-by-name) ·
`Energy_Grid_Failure_Rationale.md`'s per-city entry if named. **Not mechanical:** the entire three-generator
four-quadrant capability profile and everything downstream of it — this IS the phase.

**Phase 2 — Composition & Arrival.** *Tier C:* the census composition tier table (Primary/Significant/Notable,
full nation lists, any inline annotation **and whether it carries a date** — the date is the discriminator
between authoring-note and in-world content) · Census I/II rows (cross-ref Phase 0's) · computed retention %
(formula fixed, cite the two inputs). *Tier U:* ⭐⭐⭐ **both fully extracted, read firsthand in full — cite
directly, do not re-open the primary sources per city:** `Corpus_Reference_Sheets/Falkland_Treaty_Quick_
Reference.md` (all seven Titles, condensed article-by-article, plus a "what this settles" summary) ·
`Corpus_Reference_Sheets/No_National_Stereotypes_Quick_Reference.md` (the GPS rule, the station-builder/
exile-origin distinction, the sequencing rule, the divergence principle). **Not mechanical:** the seven-mode
arrival taxonomy, attract/repel, native/transplanted separation, who-is-not-here, the differentiation axis
name.

**Phase 3 — Surface & Texture.** *Tier C:* concept-art directory's file count / empty-`.gitkeep` status · Specs'
directly-stated physical/sensory facts · the Megasheet Physical Infrastructure file's **existence** (withheld —
never opened) · per-city research folder name/existence if one exists. **Not mechanical:** all four sensory
sub-fields, the public/institutional split, the seam, seasonal variance, Retroactive Mechanism.

**Phase 4 — Ordinary Life.** ⚠ *Corrected 2026-09-15 while extracting Davis: the per-city figure sits in `09`'s
**§2 "RESULTS — all 38 cities" table**, not §3.5. §3.5 itself is titled "THE FREEDOM MARGIN. A worldbuilding
finding, not a calculation" — explicit cross-city comparison, never a per-city mechanical fact; exclude it.*
*Tier C:* `09` §2's stated workforce-requirement row for this city · `11`'s
caloric/livestock tier if per-city-keyed · `National_Medical_and_Care_Institutes.md` — does this city appear by
name, and what's stated. *Tier U:* ⭐⭐⭐ **fully extracted, read firsthand in full — cite directly:**
`Corpus_Reference_Sheets/Robot_Physiology_Quick_Reference.md` (appearance/clothing baseline, cold-physiology
mechanics, siligel/coolant/smoking, leisure/freedom-gradient, human-robot relations baseline). **Not
mechanical:**
headline-function-then-write-away-from-it, the four ordinary-life elements, population-specific days, what the
rhythm fails to provide.

**Phase 5 — Relation & Geometry.** *Tier C:* `Highways.md`'s stated routing for this city (which highway, stated
neighbors along it) · airport/port existence and directly-stated facts · this city's own entry in
`City_Cross_Subnet_Relationships.md`, `City_Relationship_Database.md` (exact line range, verbatim), and
`City_National_Connections.md` (⚠ open ITS OWN header first). **Not mechanical:** mechanism-not-rivalry framing,
the own-eras three-way set, the parent-disagreement analysis, the arrival-type enumeration + visitor-to-member
mechanism, the dependency/who-knows-it analysis.

**Phase 6 — Meaning.** *Tier C:* does any named religion's own file cite this city specifically · does
`National_Holidays.md` carry a local entry for this city. *Tier U:* ⭐ **fully extracted, cite directly:**
`Corpus_Reference_Sheets/Robot_Religions_Roster_Quick_Reference.md`. ⛔⛔ **A `find`/`grep` that returns 0 must
actually have enumerated the directory — a claim of "the roster is empty" without doing so is a documented
failure mode, caught 2026-09-15 after surviving uncorrected in a completed city datasheet.** A zero match for
one city's name is legitimate; an unverified "empty directory" claim is not. ⚠ **Thin on mechanical content
beyond the roster — most of this phase is interpretive by design.**

**Phase 7 — Order.** *Tier C:* this city's stated Division-of-Industry sector figures (record as-is; flag, don't
fix, anything that reads like the object-colonization trap) · `Division_of_Industry_Sweep_2026-08-31.md` §4.4's
entry for this city, if any · `Theoretical-Calculations/`'s entry for this city, if any · does this city appear
by name in `Factions/` · which single city `City_Logistics.md` is scoped to. *Tier U:* `01_Burden_Scoring_
Model.md`, `08_Volume_Based_Requirement_Reference.md`, `Industry_Staffing_and_Productivity/`, `Megacorps/`
roster. **Not mechanical:** governance/succession analysis, knowledge-transmission analysis, counterculture
derivation, sanction-proportionality pricing.

**Phase 8 — Making.** *Tier C:* minimal — does `Weapons_and_Tools_Philosophy.md` or a gear catalog name this
city specifically. *Tier U:* `Robot_Biology_and_Culture/`'s mandatory-before-any-claim facts. ⚠ **Thin, same as
Phase 6.**

**Phase 9 — Populations.** *Tier C:* near-none — does this city have any existing citation in
`Robot_Universals/` or elsewhere. *Tier U:* ⭐ **fully extracted, all four sources read firsthand, cite
directly:** `Corpus_Reference_Sheets/Robot_Physiology_Quick_Reference.md` (Laws of Robotics, `Robot_Universals`
Ch. 13's city-locality identity lens, Ch. 14's Gen/Mark). `Doll_Representation_Categories.md`'s content is not
yet its own Tier U sheet — read directly, 35 lines, short. **Not mechanical:** the lens decision,
per-population culture synthesis, inter-population relations, dual-tagging, swap test.

**Phase 10 — Catalog.** *Tier C:* full list of any character already tagged to this city, from Characters canon
and `Enneagram_Character_Index.md`, verbatim — ⚠ **a `grep` for "Mirny" (or any subnet-hub city's name) will
false-positive on "`<City> Subnet`" qualifiers naming a DIFFERENT city within that subnet — check the actual
sentence, not just the match.** *Tier U:* ⭐ **fully extracted, cite directly:** `Corpus_Reference_Sheets/
Zodiac_Signs_Quick_Reference.md` — all 12 signs' full positive/negative attributes, not just names; a fixed
checklist run identically against every city. **Not mechanical:** the four-category catalog synthesis, the
Zodiac Lens's actual application, border-adjacency texture.

> ⛔⛔ **SYMBOL DEFERRAL — developer ruling, 2026-09-16.** `City_Symbol_Assignments.md` (Planet + Element),
> `Planetary_Symbols.md`, and `Robot_Elementals.md` are **not opened as datasheet input.** If a city's Element/
> Planet surfaces incidentally inside another already-open source (e.g. `16_Per_City_Three_Tier_Run.md`'s own
> Notes), transcribe it as a bare pre-existing fact **flagged PROVISIONAL, pending reconciliation against that
> city's own Phase 1–9 findings** — never present it as settled. **The actual reconciliation happens at
> Step 4, Phase 10 §B3** (`DR-8a`), not in a datasheet. Full statement: `00_RUNBOOK.md` §C.7.

---

# Per-Step field guide (−1, 0, 1, 2, 3, 5–10)

**Steps 0, 1, 2 map directly onto Phases 0, 1, 2's content** — no separate category list; point to the Phase
guide above.

**Step −1 (Input contract).** *Tier C:* the Specs file's content at its **ratified admitted range** (the range
itself is a per-city ruling, not mechanical the first time — once ruled, re-citing it is pure lookup).

**Step 3 (Research).** No new mechanical content — "the deficits Step 2 named" are this city's own prior output.
⭐ Overlaps the queued eBook pre-staging tally — cross-link rather than duplicate.

**Step 5 (Reconciliation).** ⛔ **Excluded by the sequencing rule above** — `Local_Cultures/` and
`Local_Robot_Culture/` cannot be pre-staged at any tier.

**Step 6 (Differentiate, write-only).** *Tier U, built in full 2026-09-15:*
⭐ `Corpus_Reference_Sheets/Differentiation_Instrument_Quick_Reference.md` — the governing rule, `04` Part III's
full text (III.0–III.4), and the destination addresses, all pasted verbatim, identical for every city. **Cite
this sheet, do not re-extract from `04`/`00_RUNBOOK.md` per city** — the first three cities each independently
re-derived this before the redundancy was caught; it belongs in exactly one place. The actual column is this
city's own fresh output — not pre-extractable. ⚠ **Depends on Step 4's phases being written, nothing later** —
the sheet's own text states the table is *"FILLED DURING synthesis, not before it."* ⛔ **A false claim that
this depends on Step 9 propagated into two city datasheets before being caught 2026-09-15** — never state a
dependency in a datasheet without checking it against the runbook first.

> ### ⛔⛔⛔ EVERY `Step_6.md` DATASHEET MUST CARRY THE TABLE'S NINE-SECTION INVENTORY — added 2026-09-21
> **Measured on Davis, 2026-09-16→21: a completed Step 6 wrote 2 of the table's 9 sections and declared the
> column added, in good faith.** The anti-contamination read protocol (`05` §6.1a — approach the table
> column-anchored, read header rows only) surfaced only the first two section headers and gave no signal that
> seven more existed. **The rule meant to prevent contamination produced a silent under-fill, and neither Gate
> 0 nor Step 10 caught it — both verified the ARTIFACT existed rather than opening the DESTINATION.**
>
> ✅ **The fix is mechanical and belongs here, not per-city.** `Cross_City_Culture_Differentiation_Table.md`'s
> nine section headers are structure, not another city's answer — reading and recording them violates nothing,
> **and every `Step_6.md` this Field Guide's convention produces must include the inventory table below**, so
> a future pass knows it owes nine rows before it ever opens the destination file:
>
> | § | Section | Columns beyond `City` |
> |--:|---|---|
> | 1 | Capability shape & deficit address | Shape · Deficit address · Pass |
> | 2 | Phase 2 — Composition & Arrival | Arrival mode-mix · The organizing axis |
> | 3 | Phase 3 — Surface & Texture | Axis · Seasonal worst point |
> | 4 | Phase 4 — Ordinary Life | Axis |
> | 5 | Phase 6 — Meaning | The unnamed load-bearing thing · Observance axis · Death & the dead |
> | 6 | Phase 7 — Order | Governance: what is UNADMINISTRABLE · Transmission: how skill passes · Counterculture axis |
> | 7 | Phase 8 — Making | Food axis · Dress axis · Language / speech marker |
> | 8 | Phase 5 — Relation & Geometry | Named relational axis · What it refuses to develop, and who supplies it |
> | 9 | Phase 9 — Populations | Lens · Is there a category here that matters MORE than kind? |
>
> ⛔ **A completed Step 6 must add a row to ALL NINE, in the same commit.** Fewer than nine is an under-fill,
> not a smaller city's exemption. **Retrofitted 2026-09-21 into all 5 then-existing Step 6 datasheets** (Casey,
> Kunlun, Mirny, Vostok, Dumont d'Urville) **and into Davis's own ratified `06_Differentiate.md`**, whose table
> write was backfilled from 2 rows to 9 the same day.

**Step 7 (QA, 17 gates).** *Tier U:* the 17 gates' full names + one-line definitions — a fixed enumerated
checklist reused, unchanged, by every city's Step 7 forever.

**Step 8 (Review Panel).** *Tier U:* `Disciplines/00f_Review_Panel.md`'s panel-position roster + the six
disposition definitions (accepted/noted/rejected/refereed/unmet/declined).

**Step 9 (Record).** *Tier U:* `00_RUNBOOK.md` §Step 9/§9.5's fixed procedure text. ⚠ The "next `M-` number"
lookup is mechanical but not stable enough for a static datasheet — recommend a single live-maintained counter
file instead of a per-city artifact.

**Step 10 (Readiness check).** *Tier U:* `06_Worked_Example_Provenance.md`'s stated content. The memory index
and `00_RUNBOOK.md` §Step 10 change too often/require too much judgment to pre-stage.

---

# Datasheet format & folder convention

- **Tier U:** `Universal_Location_Methodology/Corpus_Reference_Sheets/<Source>_Quick_Reference.md` — header
  states source file + line-count/version at extraction time + extraction date + *"Tier U — identical for every
  city."*
- **Tier C:** `<City pass folder>/Datasheets/Step_<N>.md` and `.../Datasheets/Phase_<N>.md` — one file per
  step/phase per city, in a dedicated subfolder (a distinct artifact type, same logic that already justifies
  `00.2`'s ledger being its own file).

## ⭐⭐⭐ THE PER-CITY FILE MANIFEST — 19 files, every city, no exceptions

> ⚠ **REVISED 2026-09-15, on Mirny.** The original 22-file version (one file per Step AND one per Phase, even
> where they draw on identical facts) produced real duplication for Steps 0–2 — Step 0/Phase 0 and Step 1/
> Step 2/Phase 1 are near-total copies of each other, since none of them has a genuinely different underlying
> fact set. **Merged: `Step_0.md` now absorbs Phase 0's content (both feed `00_Frame.md`); `Step_1_and_2.md`
> now absorbs Step 2 and Phase 1's content (feeding `01_Inherited.md` and `02_Spine.md`).** Everything from
> Phase 2 onward, and every step from 5 onward, has no redundant counterpart and stays its own file.
> ✅ **Davis retrofitted 2026-09-22, on request — 22 files → 19, matching this manifest exactly.**
> **`Step_0.md` absorbed `Phase_0.md` as its §B; `Step_1_and_2.md` absorbed `Step_1.md`, `Step_2.md` and
> `Phase_1.md` as §A/§B/§C.** ⭐ **Each MUST-OPEN mapping was preserved as its own section rather than dissolved
> into the merged table — the Phase contracts differ from the Step declaration blocks even where the underlying
> facts are identical.** ⚠ **Phase 1's two live extraction gaps** *(`Energy_Grid_Failure_Rationale.md`'s Davis
> entry, `16_Per_City_Three_Tier_Run.md` Half B's `G3` figures)* **were carried forward explicitly, and the four
> pointers in `00.0_Pre-Trip_Inspection.md` were repointed in the same pass.**

```
<City pass folder>/Datasheets/
  Step_-1.md   Step_0.md   Step_1_and_2.md   Step_3.md
  Step_5.md    Step_6.md   Step_7.md   Step_8.md   Step_9.md   Step_10.md
  Phase_2.md   Phase_3.md  Phase_4.md
  Phase_5.md   Phase_6.md  Phase_7.md  Phase_8.md  Phase_9.md  Phase_10.md
```

**`Step_-1`, `Step_0`, `Step_1_and_2`, `Step_3` (4) + `Step_5`…`Step_10` (6) + `Phase_2`…`Phase_10` (9) = 19
total per city, not 22.** *(One file's content maps to two real output files — `Step_1_and_2.md` feeds both
`01_Inherited.md` and `02_Spine.md` — declared explicitly in that file's own header, not left implicit.)*

⛔ **One slot is structurally blocked, not merely unfinished, and its file must say so explicitly rather than
be silently absent.** `Step_5.md` never carries real content — `Local_Cultures/`/`Local_Robot_Culture/` are
read-last by rule, and pre-staging them defeats the enforcement. **Write the stub anyway**, stating plainly
that the absence is deliberate — per `M-171`'s own distinction, *"I did not look, and it turned out to be
empty" is not the same result as "I looked, and it was empty,"* and a missing file reads as the first, not
the second.

⚠ **Why this lives in a separate `Datasheets/` folder rather than inside the real output files
(`00_Frame.md`, `04_Phase_02_…md`, etc.) directly — considered and rejected 2026-09-15.** File-existence is
the corpus-wide signal for "has this step/phase actually been derived" (every city's README, `MASTER_Process_
Tracker.md`). Pre-writing mechanical content into a real output file before its own derivation runs would
break that signal, and for a city with completed steps already (Davis), several of those real files are
already finished, T8-verified canon that cannot be retrofitted without touching completed work. **The
separate folder stays; only the REDUNDANCY inside it was cut.**

**Mirny, 2026-09-15, is the reference example for the consolidated 19-file shape. Use its structure when
building the set for city 3 onward — do not re-derive the manifest from scratch.**

# Verification protocol — reuses T8 exactly, no new machinery

**Round 1:** 3 isolated agents, identical brief = the category guide above + the named source addresses at named
ranges (`DR-6` unchanged). Each emits the datasheet content + `PROOF:` blocks, same format as every T8 dispatch.
**Round 2:** `triple_read_verify.py`, unchanged. **Round 3:** lightweight cross-check only if a genuine
divergence exists — write only on unanimous consensus.

⚠ **A datasheet built by citing INTO another already-T8-verified pass file (rather than dispatching a fresh
Round 1 against a primary universe/project source) is a DRAFT, not a verified Tier C artifact, until it has been
through the protocol above in its own right.** Mark it so explicitly in the file header.

# Wiring rule

Once verified, a city's `00.0_Pre-Trip_Inspection.md` T8 dispatch block for that step/phase gets an **added** row
pointing to the datasheet — the primary-source rows stay, always.

## ⛔⛔⛔ SECOND WIRING STEP — THE CITY'S OWN `README.md`, DONE THE SAME COMMIT THE `Datasheets/` FOLDER IS CREATED

**Added 2026-09-21, after a measured gap: five cities (Casey, Kunlun, Mirny, Vostok, Dumont d'Urville) had a
full datasheet set sitting on disk with nothing anywhere — not `00_RUNBOOK.md`, not
`MASTER_Process_Tracker.md`, not the city's own `README.md` — pointing a future pass at it.** A pass starting
cold on any of them had no way to know the datasheets existed short of noticing the folder by chance.
`00.0_Pre-Trip_Inspection.md` doesn't exist yet at that point either — it isn't created until Step −1 actually
runs — so the wiring rule above has nothing to attach to until well after the gap already matters.

⭐⭐⭐ **The fix: the moment a city's `Datasheets/` folder is created — not once verified, not once Step −1
runs, THE SAME COMMIT — add a row to that city's own pass-folder `README.md`, as the FIRST row of its "existing
sources" table, before Specs.** The `README.md` is the one file certain to already exist and certain to be
opened first, since it's what `00_RUNBOOK.md`'s own process for opening a new city's pass folder leads to.

**The row, exact text, city name substituted:**

```
| ⭐⭐⭐ **Datasheets** | `Datasheets/` — **READ FIRST, before Step −1.** Pre-staged, copy-pasted input (value +
citation only, no synthesis) for every step/phase already built. ⛔ **Does NOT replace any MUST-OPEN read** —
Step 4 still opens every primary source in full, per the Field Guide's own guardrail |
```

⛔ **This is not optional and not deferrable to "once the pass starts."** A `Datasheets/` folder that exists
without this row is in the same state the five measured cities were in — correct, verified, copy-paste-only
content that a future pass has no way to discover. **Retrofitted into all five cities named above, 2026-09-21.**

# Operating hours

**Any-hour.** A Tier U extraction is methodology/universe-canon transcription — no place-claim. A Tier C
extraction transcribes a fact the source already asserts — it derives nothing new. Neither is multi-step
synthesis. Same classification as `project_ebook_prestaging_and_pace_standard.md` — schedule both in the same
off-hours sessions.

---

*First applied: Davis, 2026-09-15 — see `City_Development_Passes/Mirny_Subnet/Davis/Datasheets/`.*
