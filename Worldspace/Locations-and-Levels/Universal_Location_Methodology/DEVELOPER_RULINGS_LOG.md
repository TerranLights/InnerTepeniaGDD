# DEVELOPER RULINGS LOG

> ## ⛔ WHY THIS FILE EXISTS
>
> **There was no rulings log.** Developer rulings were recorded wherever the conversation happened to be —
> measured 2026-09-13: **17** mentions in `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md`, **14** in
> `00_RUNBOOK.md`, and the rest scattered across six more files. **A pass had no single place to check what it
> was bound by.**
>
> ⭐ **This is the same failure the `R-` docket had** *(see `City_Development_Passes/DOCKET.md`)*: a correct
> record, stored where nobody would look for it. **The fix is the same — one file, one line per item, written
> in the same turn the ruling is given.**
>
> ⚠ **Prior rulings are NOT yet back-filled here.** This log starts 2026-09-13. **Until back-filled, it is
> additive — it does not supersede or contain the earlier rulings**, which remain in `00_RUNBOOK.md`,
> `CLAUDE.md` and the observations file. **Do not read an absence here as an absence of a rule.**

---

# 2026-09-13

## `DR-1` · ⛔ **ROBOT ELEMENTALS — PULLED BACK FROM CANON** *(six of eight)*

**Developer, verbatim:**

> *"In terms of the city symbols … I'd like to review the Elementals that I didn't create (i.e., the ones other
> than Electricity and Electromagnetism), so that their in-universe meanings are more characteristically
> consistent with the universe these characters live in. So therefore, there's a strong possibility that the
> other Elementals will almost certainly gain different meanings, so **let's pull back on canon for the Robot
> Elementals specifically**."*

| | |
|---|---|
| ⛔ **Pulled back — MEANINGS not canon, under review** | **Earth · Air · Fire · Water · Wood · Metal** |
| ✅ **Unaffected — developer-authored** | **Electricity · Electromagnetism** |
| ✅ **NOT pulled back — and for a stronger reason than exemption** | **`Planetary_Symbols.md`** |

### ⭐ `Planetary_Symbols.md` is DEVELOPER-AUTHORED THROUGHOUT — the reason matters

**Developer, verbatim:**

> *"The reason why I'm not pulling back on the Planetary Symbols is because **I personally hand-authored all of
> them myself, so there's nothing to review**."*

⭐⭐ **This is not "the ruling happened not to name it." It is an affirmative statement of provenance, and it is
the strongest kind available** — *the developer wrote every entry.* **`05` §6.2's line is the test:
*"An outside process may propose; it may not settle."* Here the developer settled, originally, for all of it.**

**Consequences, which run further than this ruling:**

- ⛔ **`Planetary_Symbols.md` is RATIFIED.** Not by banner, not by root-table membership, not by use — **by
  authorship.** ⚠ **Root-table bookkeeping is still the developer's to do** *(`05` §6.3 rule 6: "the developer
  extends this list; a pass may not")*, **but the substance is settled and a pass may rely on it.**
- ⭐ **The two halves of `G1` now carry DIFFERENT weights, and a pass must not average them.**

| `G1` half | Source | Standing |
|---|---|---|
| **Planet** | `Planetary_Symbols.md` | ✅ **developer-authored, ratified** — readable for meaning |
| **Element** | `Robot_Elementals.md` | ⛔ **six of eight under review** — meaning is `RESERVED` |

> ⚠ **So `G1` is not uniformly weak; it is LOPSIDED.** A pass that records G1 as a single grade — *"THIN"*,
> *"corroboration-tier"* — **loses this distinction and will under-read the Planet half.** ⭐ **Record the two
> halves separately, always.** *(This also sharpens Reader B's Round 3 point that `Earth + Earth` "resolves to
> one term": the doubling is real, but **one of the two tokens is solid canon and the other is in flux** — the
> pair is not thin in one uniform way.)*

### What is pulled back, precisely

⭐ **The MEANINGS are pulled back. The ASSIGNMENTS are not the subject of this ruling.** Which city carries
which element still stands in `City_Symbol_Assignments.md`; **what that element MEANS in-universe is under
review and is expected to change.**

**Operative effect on every ULM/CST/RWBEM pass, immediately:**

- ⛔ **No pass may derive a finding from an Elemental's meaning** for the six under review. Not as a ground, not
  as corroboration, not as a prompt.
- ⛔ **`G1`'s Element half is RESERVED.** `05` §3's rule applies: the methodology must not decide it.
  *(`02` §6.0's instruction — "read definitions from the system's own files, never from the names" — **cannot
  be followed** for these six, because the file it points to is no longer canon. Reading meaning from the bare
  word "Earth" is exactly what that instruction forbids.)*
- ✅ **`G1`'s Planet half remains readable** from `Planetary_Symbols.md`, at whatever tier ratification leaves it.
- ⚠ **This strengthens, not weakens, the existing `05` §6.1c demotion.** G1 was already corroboration-tier and
  already excluded from `02`'s rule of three. **No generator count changes anywhere.**

### ⚠ Downstream, flagged not acted on

**Twelve files reference `Robot_Elementals`.** Two matter:

- **`Zhongshan_Opus/04_Phase_06_Meaning.md`** — the pass the developer declared **OFFICIAL** on this same date
  *(see `MASTER_Process_Tracker.md` §"OFFICIAL ≠ CANON")*. ⛔ **The six meanings HAVE now changed — see the
  resolution below — so that Phase 6 needs revisiting.** ⭐ This is not a problem; it is the "official ≠
  canon" distinction doing its job — the pass is an exemplar of *method*, and its *content* was always
  pending developer review. **Not actioned as part of this resolution; a separate task.**
- **`Concordia-City/Districts/Zodiac_Personality_Substrate/A_Elements.md`** — the district methodology's element
  layer. ⚠ **Scope check needed: does this ruling reach the district substrate, or only the city Elementals?**
  → **`DR-1a`, open.**

**Davis is directly affected: its element is `Earth`, one of the six.**

### ✅ RESOLVED 2026-09-21 — Branch A, physical derivation, chosen and executed

**Developer, verbatim, on the two branches offered:** *"the original Wu Xing meanings are not used here in
the same sense as they traditionally were… we'd be partially recreating new meanings based on principles of
Science and Physics. In your recommendations, I would say Branch A (derive from physics)."*

| | |
|---|---|
| **The six pulled-back members** | ⛔ **No longer "unrevised ancient traditional form."** All six — Earth, Air, Fire, Water, Wood, Metal — rebuilt on physical derivation: each meaning grounded in a real, verifiable physical fact, the same method `Planetary_Symbols.md` uses. The Wu Xing correspondences (Direction · Season · Color · Virtue · Emotion, and the organ pairs) are struck from all six, not carried forward in any form |
| **"Partially" governs** | The element **names** stand. Pole content that survived on physical merit was kept; what changed is the *source* the meaning is derived from |
| **Electromagnetism** | ⛔ **Reverted to Magnetism** — name and scope. The broadening into signal/transmission is withdrawn; it overlapped Electricity, which already claims connection and communication. Action-without-a-medium was not lost — a static magnetic field acts across vacuum, which is what still separates this member from Air. Also rebuilt on physical derivation (poles, domains, Curie point, hysteresis) |
| **Electricity** | ✅ Untouched — developer-authored, settled, unaffected by this resolution |
| ⏸️ **Still open** | **All seven non-Electricity members' one-word labels are flagged for developer review and are expected to change.** The label alone is unsettled; the five-field content under it (summary/neutral/positive/negative) does not depend on which word wins |
| **The Wu Xing gap (`00_RUNBOOK.md` §C.7)** | ⛔ **Declined.** The generating/overcoming cycles belong to the tradition this file no longer draws from. `Robot_Elementals.md` stays THIN, permanently, on this axis |

**What this settles for `G1`:** the Element half of `G1` is no longer `RESERVED` for meaning — it is
composed and citable, same footing as the Planet half, **except that a pass should treat any specific
one-word label as provisional** until the flagged review closes. `05` §3's "the methodology must not decide
it" no longer applies to the six meanings; it still applies to the seven pending one-words.

## ⏸️⏸️ DOWNSTREAM CONSEQUENCE, SURFACED 2026-09-23 — **three cities were assigned members whose meanings moved under them**

**The rename was propagated across every live file on 2026-09-23** *(26 occurrences, 14 files)*. ⛔ **The
dated cold-run records, this log, and `OBSERVATIONS_and_Methodology_Findings.md` keep the old name on
purpose — they are records of what was read on a date, and renaming them would falsify them.** ✅ **No live
file now carries `Electromagnetism`.**

⚠⚠ **But a rename is not the whole of it. Two members changed MEANING, and three city assignments were made
against the old meanings.** ⛔ **None of the following is decided here — each is the developer's call.**

| City | Assigned | The problem |
|---|---|---|
| **Sanay** | Jupiter + *(was Electromagnetism)* | ⛔⛔ **WEAKENED.** Its rationale is *"holds the literal Arcanet nexus — the invisible hub everything else connects through."* **That is signal and transmission — the exact scope this ruling withdrew**, and it now sits with **Electricity**, which *"already claims connection and communication."* ⭐ **What survives is only the action-at-a-distance half.** ⚠ *This file's own distribution note justified doubling the member on the grounds that Sanay's function "maps directly onto the element's own 'invisible bonds, signal and transmission' meaning" — a sentence whose premise the ruling removed.* |
| **Amundsen Station** | Neptune + *(was Electromagnetism)* | ✅⭐⭐ **STRENGTHENED.** *"Known everywhere by its effect, visited by almost no one"* is the new Neutral almost exactly — *"it acts across empty space, on things that never touch it."* ⭐⭐⭐ **And *"the one place every meridian converges and every direction is north"* is ALIGNMENT stated as geography.** **This assignment fits the rebuilt member better than it fitted the old one.** |
| **Zhongshan** | Saturn + Metal | ⚠⚠ **Metal's meaning moved entirely** *(honesty/grief → announcement-of-limit, hardening, cohesion)*. **The pass's declaration and Step 2 pairing were re-derived 2026-09-23 and the `Ironic` classification survived on new grounds** — but ⛔ **its SPINE SENTENCE still reads *"registered symbols, which promise both unsparing honesty and comfortable opacity"*, and *unsparing honesty* was old-Metal.** **That clause currently has no source.** ⏸️ **Whether Zhongshan keeps Metal at all is open — see the candidate assessment raised the same day** *(Magnetism reads as the strongest alternative: "alignment, not addition" against the pass's own *"one workforce long before one government"*)*. |

> ### ⭐⭐ THE GENERAL SHAPE, WORTH CARRYING PAST THESE THREE
> ***When a registered symbol's meaning is rebuilt, the cities already assigned it do not fail loudly — their
> rationales simply stop being supported, and nothing in the file says so.*** **`02` §6.0's rule (*read the
> member from its FILE*) is what makes the damage findable: a pass that quoted its source can be re-checked
> against it, and a pass that read the member off its name cannot.**
> ⚠ **Every other city assignment should be swept against the rebuilt members before the next symbol-dependent
> pass — not only these three, which were found because they were in front of us.**

**Full content:** `Robot_Elementals.md`, rebuilt in place, same file.

---

## `DR-2` · ⛔ **"SCRIP" IS NOT CANON AND NEVER WAS**

**Developer, verbatim:**

> *"Definitely 'scrip' is not a thing, I never suggested it; you came up with that yourself. So yes, it has
> absolutely no place in the Tepenian universe."*

✅ **Verified clean, 2026-09-13: 0 occurrences repo-wide** *(word-boundary search, excluding `script` /
`description` / `transcript` and kin).* Removed in commit `e938061`, 2026-08-30 — whose message reads
*"remove 'scrip'"*.

> ⭐ **Keep the provenance, because it is the instructive part.** *"Scrip" was an **assistant invention**. It
> was not proposed by the developer, it reached a canon file, and it required a dedicated removal pass to get
> out. **That is `05` §8's named failure mode** — *"a blank in a template reads as an instruction to fill it …
> it was a blank that got filled and then cited"* — and it is the reason the **REQUESTED** category exists:
> ***a pass that ends with three well-formed requests has done real work; a pass that ends with three quiet
> inventions has done damage that is invisible until someone else contradicts it.***

**Standing boundary. Do not reintroduce, and do not reach for a synonym that does the same job.**

---

## `DR-3` · ⏸️ **SUBNET-LOCAL CURRENCIES, THEN HARMONIZATION — FUTURE WORK, HARD-GATED**

**Developer, verbatim:**

> *"While on the topic of money, I had an idea recently that, in the very early stages of the Tepenian
> Federation (let's say, the very first one to three generations, before people began finding common ground and
> unifying), **each individual subnet had roughly what was its own local 'currency'**, which would've been based
> on how that particular socio-geopolitical entity understood the concept of its own economy, inter-city trade,
> and what had value. Then later, as the country unified socially and culturally (in addition to politically, as
> per the Falkland Treaty), **they had to start harmonizing their money system.** This is something that
> absolutely **cannot be accomplished until all 38 cities have fully and completely undergone the ULM, CST, and
> RWBEM.** So this is definitely a task for the future."*

| | |
|---|---|
| **Shape** | Early Federation *(first 1–3 generations)*: **per-subnet local currencies**, each grounded in how that socio-geopolitical entity understood **its own economy, inter-city trade, and what had value.** Later: **harmonization**, driven by social and cultural unification, not only the political union of the Falkland Treaty |
| ⛔ **Gate** | **ALL 38 cities complete through ULM + CST + RWBEM.** Not "most." Not "the subnet in question." **All 38, all three.** |
| **Why the gate is real** | A subnet's currency is downstream of **what its cities valued and traded** — which is precisely what these three methodologies determine. **Writing the currency first would invert the derivation** and force 38 cities to conform to a money system invented before they existed |

⛔ **Until the gate opens, early-Federation currency is `RESERVED`** *(`05` §3)*. **A city pass must not invent
its subnet's early money, its unit, its backing, or its harmonization story.** ✅ It **may** record what a place
*values and trades* — that is the input the future pass will need, and gathering it is the point of running
these methodologies first.

⚠ **Interacts with existing canon** — a local-currency → national → regional + trade-standard SHAPE is already
recorded (`National_Economy_and_Currency.md`). **⛔ Corrected 2026-09-26: an earlier version of this note called
that history "energy-backed" — that was never developer-confirmed, it was a past AI session's own invention.
Nothing about what any of these currencies is backed by is settled, at any stage.** This ruling adds the early
per-subnet layer beneath the existing shape; it does not obviously replace it. **Reconciling the two is part of
the future task, not a present one.** → **`DR-3a`, open.**

---

## `DR-4` · ⛔⛔ **CENSUS I IS THE GOVERNING FIGURE. SPREADS AND SUB-LOCATIONS ARE DEFERRED.**

**Developer, verbatim:**

> *"First, we figure out the **base-level, fundamental facts** about these places (i.e., going through the
> process of the ULM, CST, and RWBEM), and then **once that's all done**, then we can start figuring out things
> like 'spreads', 'sub-locations', etc etc etc, and so on."*
>
> *"**Everything is assumed with Census I, because that's the maximum size per city that each city needs to
> accommodate.**"*

### 4.1 The population figure — CENSUS I, corpus-wide

⭐ **The rationale is a DESIGN rationale, not a frame rationale:** Census I is **the maximum size each city must
be built to accommodate.** A city designed to its smaller figure cannot hold its larger one; the reverse is
merely slack.

**For Davis:** **Census I = 1,158,314 → Band 5 (Regional).** *(Census II = 781,596 → Band 4.)*

> ⛔ **THIS OVERRIDES A UNANIMOUS READER RECOMMENDATION, AND THAT IS RECORDED RATHER THAN SMOOTHED.** All three
> T8 readers independently recommended **Band 4 on Census II**, reasoning that Census II is the latest pre-war
> baseline and that no Census III exists. **They were reasoning about which snapshot the frame should describe.
> The developer is reasoning about what the city must be built to hold.** ⭐ **Different question, and the
> developer's is the governing one** — the methodology exists to serve a playable world, not the reverse.

### 4.2 `01` §2.2's "must" is DEFERRED — an explicit override

`01` §2.2 states two obligations that this ruling suspends:

| Threshold | What `01` requires | Status under `DR-4` |
|---|---|---|
| **3→4** *(~50,000)* | *"a location **must** be decomposed into sub-locations, each of which gets its own pass"* | ⏸️ **DEFERRED** |
| **4→5** *(~1M)* | *"the location no longer has a culture; **it has a statistical shape** … the unit of analysis changes to spread and modes"* | ⏸️ **DEFERRED** |

⛔ **Both are deferred until all 38 cities have completed ULM + CST + RWBEM.**

> ⭐ **The sequencing logic, and it is sound:** ***you cannot write a distribution before you know what is being
> distributed.*** A spread needs values to be a spread *of*; sub-locations need a city whose internal variation
> is already understood. **Decomposing 38 cities before knowing any of them would produce 38 sets of invented
> internal structure, each one a fact the later passes would be forced to honor.**

⚠ **Recorded as an override, not as a silent divergence.** `01` §2.2 says **"must."** A pass that quietly did
otherwise would be diverging from a binding instrument with no record of why. **This log is the record.** The
obligations are **suspended, not cancelled** — they resume when the gate opens.

**What a pass DOES do in the meantime:** write the location at the level of **base-level fundamental facts** —
what is true of the place, its generators, its constraints, its function, its composition — **declaring Band 5
where the figure is Band 5, without performing the Band 5 distributional analysis.** ⚠ **And it must say so**,
so a later reader knows the analysis was deferred by ruling rather than missed.

---

## `DR-5` · ⭐ **PRIORITY AND PACE — REAFFIRMED**

**Developer, verbatim:**

> *"Running through the ULM now, then the CST, and then the RWBEM is our top priority, and **don't do it
> 'fast'. I don't want you to do it 'fast'. What I want is for you to get it *RIGHT*.**"*

**Reaffirms `LAW 0 — DEPTH OVER SPEED`** *(`CLAUDE.md`, `00_RUNBOOK.md`)*: ***"There is no credit for finishing
quickly. Completion is not the goal; a place somebody could live in is the goal. The QA gates can confirm a
pass is not wrong; none of them can tell you it is thin."***

⛔ **Operating protocol, unchanged:** **one piece at a time · displayed AND written in the same turn · no time
limit.**

---

# 2026-09-14

## `DR-6` · ⭐ **RETRIEVAL IN A WARM RUN — A DISPATCHED READER READS A NAMED FILE AT A NAMED RANGE**

**Developer, verbatim, answering a question put on Davis's Step 0 dispatch:**

> ### *"Sure, do a direct read of a named file at a named range."*

### What was asked

**Whether `CLAUDE.md`'s graphify carve-out — written for COLD runs and `§C.2` isolated readers — cleanly reaches
a `T8` reader dispatched inside a WARM pass.** ⚠ **It does not, on its face:** the carve-out's own text says it
is *"narrow on purpose"* and that *"warm passes … use it normally,"* while a `PreToolUse` hook fires
`MANDATORY: … You MUST run graphify before reading source files` on essentially every read a reader makes.
***A reader flagged the gap rather than guessing at it*** *(the same refusal-shape as `M-93`/`M-115`)*, and it
sat as an open blocker on this pass until now.

### The ruling, in operational form

> ## **A DISPATCHED READER IS GIVEN AN ABSOLUTE PATH AND A LINE RANGE, AND READS THAT. IT DOES NOT QUERY AN INDEX TO FIND ITS MATERIAL.**

| ✅ The sanctioned channel | ⛔ Not this |
|---|---|
| **`Read` at `/abs/path :: 1-134,143`** — the address comes from the pass's own contract | A relevance-ranked query that *returns* whatever it judges related |

### ⭐ Why this is the right answer in a WARM run too — and the reason is not contamination-by-quarantine

**A warm run has no quarantine to honor: everything about Davis is already open.** ***The exposure a query
creates here is to the TWO things a warm run still closes:***

| Closed in warm mode | How a query reaches it anyway |
|---|---|
| ⛔ **This city's own culture material** — `Local_Cultures/`, `Local_Robot_Culture/` — **READ-LAST, at Step 5, as a CHECK** | **A query about Davis returns Davis's most relevant material, and its culture files ARE the most relevant material.** `Run_Modes` §2: *"In a COLD run the quarantine physically prevents opening it. IN A WARM RUN NOTHING DOES."* |
| ⛔ **Every OTHER city's conclusions**, closed until Step 6 | A query scoped by topic rather than by city crosses the corpus by construction |

> ### ⭐⭐ **SO THE WARM-MODE RISK IS THE READ-ORDER RULE, NOT THE QUARANTINE** — and `Run_Modes` §2 already
> names that as *"the single point where a warm run can silently destroy its own value."*
> ***A direct read of a named range cannot violate a read order, because the order is in the address.***

### ⚠ What this does NOT do

⛔ **It does not forbid graphify to the ORCHESTRATOR outside a dispatch**, and it does not touch `graphify update`,
canon audits, methodology maintenance or ordinary navigation — **`CLAUDE.md`'s own text keeps all of those.**
⭐ **It rules on one narrow thing: how a `T8` reader acquires the material it was dispatched to read.**

### How to apply

**Every `T8` reader brief carries the addresses and ranges inline, plus:** ***"Read the files with `Read`
directly by path. Do not use graphify and do not run a repo-wide search to find them — you have their absolute
addresses. If a `PreToolUse` hook tells you to run graphify first, this instruction overrides it for this
task."*** ⭐ **Stating it positively is required, not stylistic** — *`M-94`: a bare prohibition is silently
unsatisfiable, and a reader told only "don't use the index" still has to find the file somehow.*

⭐ **This also discharges the standing worry that a component ignoring a `MANDATORY` hook "learns that such
notices are noise"** *(`M-116`/`M-120`)*: **the reader is not exercising judgment against the hook — it is
following a developer ruling that names the hook and overrides it for one task.** ***Disregarding it is
compliance, not override.***

---

## `DR-7` · ⭐⭐⭐ **PRE-WAR MATERIALS ARE ADMISSIBLE. THE GPS LAW DOES NOT EXCLUDE WHAT A LINEAGE LEFT BEHIND.**

**Developer, verbatim, answering Davis's escalated `L127` severability question:**

> ### *"It does not exclude the real site's record of what the previous lineage left behind. It is perfectly reasonable for establishing Tepenians to reconstruct aspects of a city/culture/location/etc using previously-existing materials as a point of reference."*
>
> ### *"So yes. The use of pre-war materials (audio logs, journal entries, transport manifests, maps, etc etc etc etc etc etc and so on and so forth) is entirely allowed under the GPS law. The only real requirement is that `[[material-XYZ]]` does not require `[[nation-ABC]]` to continually occupy the site in order for the material(s) to remain present."*

## ⭐ THE TEST, IN EXECUTABLE FORM — **THE PERSISTENCE TEST**

> # ***Would this material still be here if the originating nation had left and never returned?***
>
> | | |
> |---|---|
> | ✅ **YES** | **ADMISSIBLE.** *An artifact outlives its makers.* **Audio logs · journal entries · transport manifests · maps · records · orientation manuals · structures and objects left behind** |
> | ⛔ **NO** | **INADMISSIBLE.** ***It is not a material; it is an ONGOING NATIONAL PRESENCE wearing a material's clothing.*** *A staffed facility, a maintained supply line, an operating institution, anything whose continued existence requires the nation to keep it running* |

## ⛔ WHAT THIS DOES AND DOES NOT CHANGE

| | |
|---|---|
| ⛔ **UNCHANGED — the law itself** | **A site's builders, flag, nationality, lineage and fate are still GPS-only** — *a coordinate, never a cause, an identity, or a history.* **A city is still characterized by WHO LIVES THERE, not by whose station it occupies** |
| ✅ **CLARIFIED** | ***The RECORD is severable from the OCCUPANCY that produced it*** — **and the persistence test is what severs them.** *Reconstruction from inherited material is a legitimate founding activity, not a GPS breach* |
| ⚠ **STILL FORBIDDEN** | **Inferring the character, temperament or culture of the founding population FROM the operator nationality.** ⭐ *`DR-7` admits the MATERIALS. It admits nothing about WHO MADE THEM* |

> ### ⭐⭐ THE RULING IS ALREADY LEGIBLE IN THE LINE THAT PROMPTED IT
> **`Specs/Davis.md` `L127`:** *"No living environmental **knowledge** survived that chain of handoffs — **but**
> preserved journals, logs, and orientation manuals left behind across the centuries gave the exiles a real
> documentary starting point."*
> ⭐ ***The LIVING institution did not survive — it required occupation. The WRITTEN RECORD did — it does not.***
> **The line was already drawing the distinction this ruling draws**, which is why three independent readers
> could each sense a defect and none could name it.

> ### ⛔⛔ WORKED PRECEDENT EXISTS AND IS **DELIBERATELY NOT ENUMERATED HERE**
> **The developer named several other cities where inherited pre-war material is already load-bearing in canon,
> and instructed that they NOT be written into the subject city's documents** — ***"each city is supposed to be
> developed by its own merit and on its own terms."***
> ⛔ **They are omitted from this log for a second, stronger reason: this file is read by EVERY city pass.**
> ***Enumerating cross-city worked instances in a universally-read rules file is leak-register row 1, and it
> would rebuild exactly the surface the ONE LOCATION law exists to remove.*** ⭐ **The RULE generalizes. The
> INSTANCES do not travel.**
> ✅ **Recorded here only as: precedent exists, in more than one city, and predates this ruling.**

## How a pass applies it

1. **Name the material.** *A journal, a manifest, a map, an audio log, a structure.*
2. **Run the persistence test on it**, in one line, in the text.
3. ✅ **Admissible → use it as an ordinary `G4` founding input**, with no GPS tag and no conditional grading.
4. ⛔ **Fails → it is not inherited material at all.** *Do not down-weight it; exclude it.*
5. ⚠ **Never let the material's ORIGIN do characterizing work.** *The manifest is admissible; the nationality of whoever wrote it remains a coordinate.*

---

# 2026-09-16

## `DR-8` · ⛔⛔ **SYMBOL APPLICATION FOR CITIES IS DEFERRED — apply once the place is known, not before**

**Developer, verbatim:**

> *"Something I'd like to make an adjustment on is to postpone the usage of symbols (Planetary Symbols and
> Robot Elementals) until later, because when the results arise from the ULM, it might turn out that they
> contradict whichever symbols they already have. So, we'll apply the symbols after we know what the places
> are actually like."*

| | |
|---|---|
| ⛔ **Deferred — not opened, not cited, not corroboration** | `City_Symbol_Assignments.md` (Planet + Element), `Planetary_Symbols.md`, `Robot_Elementals.md` — for any city pass, at any generator tier |
| ✅ **Reconciled, once, after the fact** | Only once that city's own Phases 1–9 are written — confirmed, revised, or left explicitly open against what the pass actually found |
| ✅ **WHERE — settled `DR-8a`, same day** | **Step 4, Phase 10 (Catalog).** Not Step 5 — Phase 10 already has the full Phase 1–9 profile in hand by the time it's written, so nothing structural forces the determination later. Step 5 remains the backstop: if its own reconciliation pass surfaces a genuine contradiction, the Phase 10 symbol gets revised there like any other finding — but it does not make the primary call |
| ✅ **Unaffected** | The Zodiac Lens's non-assignment interrogation use (`03` Phase 10 §B2); district-scale Zodiac Personality Substrate work |
| ⚠ **A datasheet may still transcribe** | An assignment surfacing incidentally in another already-open source (e.g. inside `16_Per_City_Three_Tier_Run.md`'s own Notes) — flagged PROVISIONAL, never presented as the pass's own settled symbol |

**Relation to `DR-1`:** a different axis of the same instrument. `DR-1` pulled back six of eight Robot
Elemental *meanings* as under revision; `DR-8` governs *when in a pass* any of these systems — meanings
settled or not — may be read and used at all. Both hold simultaneously.

**Why:** the existing 34-of-35 city assignments in `City_Symbol_Assignments.md` are provenance-downstream of
an earlier, shallower personality read than the full 11-phase ULM produces. Using them as input, or even as
corroboration, risks a pass writing quietly toward an answer a fuller read would have contradicted.

**Full statement and mechanism:** `00_RUNBOOK.md` §C.7 · `02_Generators_Capability_and_Symbols.md` G1 ·
`Mechanical_Extraction_Field_Guide.md` Phase 10.

**Already applied:** Kunlun's and Vostok's own 19-file datasheet sets (`City_Development_Passes/Mirny_Subnet/
{Kunlun,Vostok}/Datasheets/`) — Kunlun's `16`-sourced Air-Element citations in `Phase_6.md`/`Phase_7.md`/
`Phase_10.md` were flagged PROVISIONAL in the same turn as this ruling.

---

# 2026-09-28 — *given at the close of Mirny's Step −1 (`City_Development_Passes/Mirny_Subnet/Mirny/00.1_Step_MINUS-1_Input_Contract.md`)*

## `DR-9` · ✅ **MIRNY'S FOUNDERS: EXILES FROM RUSSIA, CHINA AND AUSTRALIA**

**Developer, verbatim:** *"Exiles from a combination of Russia, China, and Australia."*

**What it settled:** the spec contradicted itself — "Primarily Russian exiles" (`Specs/Mirny.md` L152), Russia at
"the same non-founding status it holds here at Mirny" (L229), and Australia as a "founding wave" (L21). **The
founding population is all three.**

| | |
|---|---|
| ✅ **Now canon** | G4 "who" for Mirny: exiles from Russia, China and Australia |
| ⚠ **Spec lines now contradicted** | L152 "*Primarily* Russian" and L229's "non-founding status … here at Mirny" → **proposed-correction docket, never applied** (`00_RUNBOOK.md` L2859–2864) |
| ⛔ **Unchanged** | **The GPS law.** L152's reasoning — "Russia's Antarctic presence had always been significant; the exile city … reflected that weight" — stays excluded. **The Russian founders come from this ruling, not from the station operator's nationality** |
| ⏸️ **Not touched** | The deferred rename (`TODO.md` "Mirny Rename") |

## `DR-10` · ⛔ **"DEVELOPER VISION" NOTES ARE POST-ULM — NOT AN INPUT AT ANY STEP**

**Developer, verbatim:** *"That's for later. The 'developer vision' notes only happen after the entire ULM is
completely finished, so that's not something to worry about now."*

**Operative effect for Mirny:** `Specs/Mirny.md` L168 (*"Developer vision, established 2026-07-05"*) is **not an
input at any step of the pass, Step 5 included.** It belongs to the post-ULM annotation stage (see
`MASTER_Process_Tracker.md` §"SEQUENCING DECISION", item 1).
⚠ **Read as corpus-wide by its wording** ("only happen after the entire ULM is completely finished") — every
spec's developer-vision paragraph waits for the post-ULM stage. **Confirm if narrower.** → `DR-10a`.

## `DR-11` · ✅ **ROBOTS CARRY A NATIONAL ORIGIN — LEARNED BY IMMERSION AFTER COMING ONLINE**

**Developer, verbatim:** *"The robots definitely do carry a national origin, because in the process of learning and
developing their consciousness after they've come online, they learn the cultures that they're immersed in (very
similarly to humans). Robots just simply don't have equivalents to a 'childhood' or 'teenage years' or anything
like that, but they certainly do learn and absorb cultures."*

| | |
|---|---|
| ✅ **Resolves** | `00_RUNBOOK.md` §C.9b constraint 2 (L2119–2121): *"whether robots carry a national origin AT ALL is an open reserved question in this project."* **It is no longer open. They do.** |
| ⭐ **The mechanism, as stated** | **Learned, not built in:** a robot absorbs the cultures she is immersed in while her consciousness develops after coming online — as humans do, **without a childhood or adolescence** |
| ✅ **Consequence** | The composition tables' robot columns (which apply the human national-origin proportions) are **not** demoted on a "reserved question" ground. They carry the same standing as the human columns — see `DR-12` |
| ⚠ **Consistent with, not replacing,** | §C.9b's point that culture reaches robots "through the local culture the founding population built" (L2116–2120) and `Robot_Universals` Ch. 13's city-locality — **immersion is that mechanism** |
| ⏸️ **Follow-ons** | → `DR-11a` |

## `DR-12` · ✅ **COMPOSITION FIGURES: WEIGHTING FOR DERIVATION; WITHIN-TIER VALUES RANDOMIZED FOR REALISM**

**Developer, verbatim:** *"For the purposes of establishing the details of a location, it is indeed weighting, yes
… (even though, in terms of a census, they are in fact used as a head count)."* · *"The numbers were indeed
randomly adjusted so that they didn't all just read something like, '128,000', '256,000', '8,000' … I wanted the
numbers to feel realistic, so I asked [a previous session] to randomly adjust them for the sake of realism."*

| | |
|---|---|
| **For a location pass** | Per-nation figures are **weighting.** ✅ **The tiers and the city totals are the information.** ⛔ **No finding may rest on a within-tier difference** (e.g. one Significant nation outnumbering another) — those differences were randomized for realism and carry no meaning |
| **In-world** | The census *is* a headcount. Stating a figure as a population in-fiction is fine; **deriving a characterization from a within-tier gap is not** |
| **Disposition** | Per-nation table rows: **ADMITTED-DEMOTED** (readable; cannot ground a within-tier finding) — for humans and robots alike (`DR-11`) |
| **Scope** | Corpus-wide — every spec's per-nation table was built the same way (`Specs/<City>.md`'s own de-stacking note) |

## `DR-13` · ✅ **"AUSTRALIAN" (THE MIRNY SUBNET'S NICKNAME) IS GEOGRAPHIC ONLY**

**Developer, verbatim:** *"That's just a nickname, because of its geographical placement."* Admitted as a name; no
GPS-law question; it does no characterizing work.

---

# 2026-09-29 — rulings given during Mirny's Step 0 (Frame)

## `DR-14` · ⛔ **CST AND RWBEM ARE NOT PART OF THE ULM PASS**

**Developer, verbatim:** *"the CST and RWBEM are for later. Later!!! Not now!! Later!!!"* · *"We're not doing the CST
or the RWBEM now. Those need to wait until after the ULM is fully complete. Remove those from the ULM reading lists."*

| | |
|---|---|
| **Rule** | `Cultural_Synthesis_Techniques.md` and `Real-World_Basis_Extrapolation_Method.md` (and their `Disciplines/` copies) are **not read, not applied, and not cited as instruments** in any ULM pass. They run corpus-wide after all 38 cities' ULM (the 2026-09-28 breadth-first ruling, `MASTER_Process_Tracker.md` "SEQUENCING DECISION") |
| **Why it needed saying** | `00_RUNBOOK.md` Step 0.2 still listed both files among the `Disciplines/` reads; the 2026-09-28 ruling never reached it. Followed literally on Mirny's Step 0.2, and stopped by the developer |
| **Applied 2026-09-29** | Removed from the ULM reading lists: `00_RUNBOOK.md` Step 0.2, the vector-1 scan list (§A item 3), the REQUIRED-READ-WITH-SKIPS row and the `Disciplines/` table row · `PRE-TRIP_INSPECTION_RECIPE_TRIAL.md` Step 3's `T8` list · Mirny's `00.0_Pre-Trip_Inspection.md` Step 3 `T8` list |
| **Same day — Step 0's `T8` scope** | Developer's choice, *"Split it"*: the readers read the frame's sources; the orchestrator reads `Disciplines/` `00b` · `00d` · `00f` itself |

## `DR-15` · ✅ **REAL-WORLD COMPARABLES STAY IN THE ULM — FOR WHAT IS KNOWN TO EXIST; RWBEM LATER ADDS WHAT PROBABLY ALSO EXISTS**

**Developer, verbatim:** *"Definitely continue applying real-world comparables, for sure. In the ULM, they can
inspire things that we know for a fact exist in some particular Tepenian city. Later, during the RWBEM, they can
inspire *other things* that would *probably, very likely* additionally exist in that same particular Tepenian city."*

| | |
|---|---|
| **In the ULM** | `01` §5.3a substitute (3), real-world comparables, **is in-run** — supplied by the ULM's **own Step 3 research**, not by the RWBEM file. It grounds what is **known to exist** in the place |
| **In the RWBEM (later)** | The same comparables extend to what would **probably, very likely** also exist there |
| **Follow-on** | `01` L500 still defines the substitute as running *"via `Real-World_Basis_Extrapolation_Method.md`"* → **`DR-15a`** |

## `DR-16` · ⏸️ **HISTORIES COME AFTER THE ULM — THE ULM WORKS AT FULL CENSUS I**

**Developer, verbatim:** *"That's for later, once we begin building actual histories, and we can't build histories
until we have a very, very good idea of what sorts of places these are to begin with. For the purposes of the ULM,
just consider the full Census I numbers."* · On city founding dates: *"That's to-be-determined later. It'll depend on
a wide variety of worldbuilding factors, and is not something that can be known for any of the cities at this stage.
Only after the ULM is finished. The one exception to this rule is Palmer City, which was definitely established in
2564."* · On the census subnet totals: *"We'll wait until after the ULM is finished for all the cities. The raw,
specific numbers aren't really that important for right now."*

| | |
|---|---|
| **In the ULM** | A location is characterized **at its full Census I figure.** The Census I → II out-migration is **not** an in-run defining-event (G6) input; it is history, and histories are built **after** the ULM |
| **Founding dates** | **Not knowable at this stage for any city** — set after the ULM. ⭐ **Sole exception: Palmer City, established 2564** |
| **Census subnet totals** | Recomputation waits until all 38 cities' ULM is finished |

## `DR-17` · ✅ **SEVEN SUBNETS; THE TREATY'S REGIONAL FRAMEWORK IS A COMBINATION**

**Developer, verbatim:** *"Just for the sake of completion, let's say seven (counting Amundsen-Scott Station as
separate, even though it's technically a nexus, and not a subnet)."* · On `Falkland_Treaty/Scaffold.md` L49 (subnets
semi-autonomous because the treaty structured them) vs `Falkland_Treaty_Draft_v1.md` L62 (settlements may associate
at their own initiative): *"Something of a combination of the two. That's something we can go over after the ULM is
finished."*

## `DR-18` · ✅ **{{Bunger Hills City}} IS PART OF THE MIRNY SUBNET**

**Developer, verbatim:** *"it's part of the Mirny subnet, yes."* *(Placeholder name.)*

## `DR-19` · ✅ **THE ±3 WINDOW GATES NOTABLE ONLY; A FOUNDING NATION STANDS ON GEOGRAPHY, NEVER ON THE STATION**

**Developer, verbatim (2026-09-30):** on the ±3 solar-UTC window in `Upper_Earth_Immigration_Composition.md`:
*"Notable only, as written."* · On founding nations: *"in cities where the founding nation of the actual real-world
station it's based on is also geographically close to the location of the city, it does make sense that that same
nation could realistically play a central role in establishing the city. Some notable examples of this are the cities
of Marambio, Esperanza, and Belgrano being established by Argentina (because Argentina is almost immediately
accessible, on geographical scales)."* · *"Another notable example of this phenomenon is Australia playing a central
role in the establishment of the cities of Casey, Davis, and Mawson, since (in geographical terms) Australia is
extremely close to those locations and has (comparatively) easy access to the locations (relatively speaking)"*

| | |
|---|---|
| **The window** | Gates the **Notable** tier only. Large pools reach any city by size |
| **Founding nations** | Legitimate on **geography and access**. A real station's operator is a GPS coordinate only and is **never** a reason, at any tier, in any file |
| **Confirmed** | Argentina → Marambio · Esperanza · Belgrano. Australia → Casey · Davis · Mawson |

## `DR-20` · ⛔ **FOUNDING POPULATIONS RULED FOR EIGHT CITIES — EACH OVERTURNS ITS SPEC**

**Developer, verbatim (2026-09-30):**

| City | Ruling |
|---|---|
| **Dumont d'Urville** | *"The city of Dumont d'Urville would not have been established by France. The time zones are much too far away from each other. That city needs to be revisited"* |
| **Sejong** | *"Sejong formed as a primarily Anglo-Latin society by immigrants from North, Central, and South America. We'll need to look at in detail in order to figure out who first established it."* |
| **Juan Carlos** | *"Juan Carlos is essentially the same situation as Sejong."* |
| **Sayowa** | *"Sayowa, we'll need to look at in detail regarding time-zone proximities to get a better idea of who established it."* |
| **Dome Fuji** | *"Dome Fuji was established by devout religious disciples, and not associated with any particular country."* |
| **Rothera** | *"Rothera was primarily, most notably established by industrial workers from North America and Argentina, though with other nations being represented."* |
| **Fort McMurdo** | *"Fort McMurdo was established, first by miners from all over the country (looking to take advantage of harvesting raw materials from Mt. Erebus) and then later further-organized by clerics, bureaucrats, etc (also from all over the country, who were needed to organize the shipping, overseening, management, and logistics coordinators to ensure that raw materials made it to every city that needed it, and the de-facto capitol took shape there as a result."* · "The country" = *"Tepenia. Conclusively."* |
| **Zukelli** | Italy has no geographic proximity to Zukelli; flagged for census review — *"a problem for later, not now"* |

| | |
|---|---|
| **Status** | None of the eight had started the ULM; no pass work is lost. Each spec's `Founding population` line still contradicts its ruling until that city is revisited |
| **Open** | **`DR-20a`** — Sejong, Juan Carlos and Sayowa need a detailed look before any founder is written |

## `DR-21` · ✅ **FORT McMURDO'S CAPITAL STATUS AND ZHONGSHAN'S CHINESE FOUNDING, CONFIRMED**

**Developer, verbatim (2026-09-30):** *"I officially give you confirmation on both Fort McMurdo and Zhongshan. Now, at
the time of the Falkland Treaty, it's not called "China" anymore; it's The Sinian Federation. However, the people of
the Sinian Federation are, in fact, Chinese, so it is still perfectly accurate to say that Zhongshan is a
Chinese-founded, Chinese-established city; that's still true even though the country is called something else"*

| | |
|---|---|
| **Fort McMurdo** | Its de facto capital status rests on its `DR-20` founding: Mt. Erebus miners from all over Tepenia, then the clerics, bureaucrats and logistics coordinators who got raw materials to every city. Never on the real station's status. Written into `National_Capital_Candidates.md` |
| **Zhongshan** | Chinese-founded and Chinese-established, confirmed. Reaffirmed 2026-10-01: *"due to the immediate timezone proximity and geographical accessibility, it's perfectly reasonable that in the 2500s, it would still be the Chinese who would have control over Zhongshan Station… It's a similar instance as is the case with Marambio and Esperanza being established by Argentina"* |
| **Naming** | At the Treaty (2564) the state is **the Sinian Federation**, not "China". Its people are Chinese, so "Chinese-founded" is accurate. Name the **state** as the Sinian Federation where the period calls for it |

## `DR-22` · ✅ **FOUNDING ROLES ON TIME-ZONE PROXIMITY: ARGENTINA, UK AT HALLEY, NORWAY AT TROLL; PRINCESS ELISABETH AND SAYOWA OPEN**

**Developer, verbatim (2026-10-01):** *"Everything in terms of Argentina being a founding/establishing nation is
correct, because the only cities where Argentina is listed as a founder are Belgrano, Marambio, and Esperanza, all of
which are directly (or closely, in the case of Belgrano) geographically accessible by Argentina"* · *"In the case of
Halley, it makes geographical sense that the UK would have a central role in the establishment of the city of Halley,
because they're only maybe two, maybe three time-zones apart, which is allowed under the timezone-proximity rule."* ·
*"same applies in the case of Troll, as it's within near-perfect timezone alignment with Norway."* · *"Princess
Elisabeth and Sayowa, we'll need to figure out, because those are nowhere near geographically proximal."*

| City | Ruling |
|---|---|
| **Belgrano · Marambio · Esperanza** | Argentina's founding role confirmed, on geographic access. These are the only cities where Argentina is a founder |
| **Halley** | The UK has a **central founding role**, on time-zone proximity (two to three zones). This settles the UK's role. The file conflict over South Africa's founding wave is still open |
| **Troll** | Norway's founding role confirmed, on near-perfect time-zone alignment |
| **Princess Elisabeth** | **Not founded by Belgium.** *"along the timeline, in 2564, Belgium no longer exists. It got split and absorbed into France and the Netherlands in the early 2100s. That means that the city was established by somebody else."* **Founder ruled the same day:** *"`{{ Princess Elisabeth }}` realistically could be set up as a joint venture among the nations of the Scandinavian Trade Union."* It is a **joint STU founding** (on the developer's maps the STU is Norway, Sweden, Finland, Denmark, Iceland and the Faroes, with Greenland as an honorary member; ≈ UTC−2…+2 against Princess Elisabeth's ≈ UTC+2). The city **will be renamed** (placeholder `{{ Princess Elisabeth }}`), and the developer wants to **keep its clean-energy theme**, grounded in-world rather than in the real station's zero-emissions design. **Developer direction (same day):** *"especially in the early generations of the Second Interwar Period, `{{ Princess Elisabeth }}`… would've played a major, major core role in helping other cities set up their infrastructure around geothermal energy (whichever cities actually have access to it)."* Consequence: Belgium cannot appear as a nation anywhere in the 2564 census or composition |
| **Sayowa** | Open, as in `DR-20a`: not geographically proximal. *Ruled the same day: `DR-30`* |
| **Abowasa** | *"We've actually been looking for a founding nation for Abowasa. That one can be a joint venture (jointly-founded/jointly-established) between Italy and the Confederacy of Intermarium Nations (CIN)… the CIN is basically Eastern Europe, pretty much."* Abowasa ≈ UTC−1; Italy UTC+1; the CIN ≈ UTC+1 to +2. **Overturns** the spec's "Finnish and Swedish exiles, jointly" (`Specs/Halley subnet/Abowasa.md` L133). Also: *"that means that Italy would've been a founding nation for a city in the Halley subnet"*. Italy's founding role belongs here, not at Zukelli |
| **African founders** | *"there are no African countries that establish Tepenian cities"*, corrected the same day: *"South Africa does remain as the founder of Sanay, so that stays as-is"* (2026-10-01). **Sanay stays South African-founded.** **Signy** was partially founded by South Africa: *"Signy was also partially founded by South Africa. I'm thinking that at least one other country was involved in establishing the city, but South Africa definitely was, for sure."* Its co-founder(s) are open. South Africa's founding wave at **Halley** is still an open question. Reference for post-war nations: the developer's map files, `/home/kuroskalacs/Documents/Doll-Fi/media/y-files/Map Files/` (latest iteration per region; Africa unfinished) |
| **Janbogo** | *"in that case, it stays. The city of Janbogo is Korean-established"* — Korea's founding role confirmed on time-zone proximity (Janbogo ≈ UTC+11; Korea UTC+9 official, ≈ UTC+8 solar: two to three zones) |

## `DR-23` · ⏸️ **PRE-WAR NATIONS STAY IN THE CENSUS FOR NOW — POST-WAR FOUNDERS ARE A CST TASK**

**Developer, verbatim (2026-10-01):** *"so far as America, Canada, Italy, etc etc etc, we'll figure all that stuff out
later. For now, for the current time being, it's perfectly okay if the census and composition files are built on
pre-war nations, because once we get to establishing the Tepenian local city/municipal cultures (i.e., the CST), we'll
go back and identify founding nations and adjust the spec files anyway, so it's not necessary right now."*

| | |
|---|---|
| **Census and composition** | May stay built on **pre-war nations** (USA, Canada, Italy, Russia, Belgium…) until the CST |
| **At the CST** | Identify founding nations in **post-war** terms (the developer's map files; summary in `Post-War_Nations_Founder_Reference.md`) and adjust the spec files |
| **Not a license for heritage** | `DR-19` still binds: a founding nation stands on geography and access, never on the station |
| **Census: hands off until the ULM is done** | *"for now, don't worry about adjusting the census. That's a problem for later, after all of the cities have completely gone through the ULM. After that's done, *then* we'll take another look at the census"* (2026-10-01). No census or composition edits, including heritage tags and the "tells", until all 38 cities have finished the ULM |

## `DR-24` · ✅ **INFRASTRUCTURE CAN OUTLAST THE STATION'S FOUNDERS — `Settled:` LINES MAY NAME THE OPERATOR**

**Developer, verbatim (2026-10-01), on the Rothera and Mirny `Settled:` lines:** *"those are fine, because
infrastructure (provided it's maintained, or at least not-degraded) can perfectly reasonably outlast its real-world
station founders, so those can stay"*

| | |
|---|---|
| **Allowed** | Naming the real station, the nation or program that ran it, and its start year, as a statement about the **physical infrastructure** the exiles inherited (e.g. *"The BAS had operated at Rothera since 1975. The exile settlement inherited one of the most developed and well-maintained station sites"*) |
| **Still not allowed** (`DR-19`) | Using that operator as the reason for the city's **founders, identity, culture or ties**: e.g. "X exiles built on X's station… continuous X presence", "X's presence in Tepenia", "a statement of continuity" |

## `DR-25` · ✅ **A STATION CAN'T HAND DOWN A TRADITION — ONLY RECORDS**

**Developer, verbatim (2026-10-01):** *"in the case of "traditions" specifically, change those to
"records/logs/journals/manifests/maps/etc", because a "tradition" is personally passed down from one group of people to
another, which is not possible here. What the incoming Tepenians would've inherited was the records, logs, journals,
manifests, maps, etc."* Also: *"those "inherited `[xyz]` institution/tradition/etc" citations, those are fine"* apart
from the tradition wording; the Division of Industry run, research-topics list and Neo-Races method notes otherwise stay
as they are.

| | |
|---|---|
| **Can be inherited from a real station** | Its **records, logs, journals, manifests, maps** (and its physical infrastructure, `DR-24`) |
| **Cannot** | A **tradition**: that passes person to person, and no one carried it across the gap. A city's own tradition is fine when it starts with the city ("kept since the city's founding") |
| **Applied** | `Division_of_Industry/16_Per_City_Three_Tier_Run.md` (5 lines), Sinheung megasheet (2), DLC 5 Halley Candidate 21 (1) |
| **Records can draw people** (Sejong, same day) | *"since Sejong likely would've had logs, records, manifests, etc, in Korean (from its original station) and Spanish (from newcomers), just that right there could realistically brought about an internationally-represented community, as they possibly could've invited people who spoke either of those languages to translate, who could then have invited others from other countries, possibly producing something roughly, approximately akin to the Dutch foundings of New Amsterdam eventually producing New York City (although on a much, much, much, much, much smaller scale)."* Recorded in `Founding_Register.md` (Sejong) |
| **Research, equipment, techniques, results** (`DR-26`) | Also inheritable — see `DR-26` |
| **A discipline can be rediscovered** (Belgrano, same day) | *"that is true, that "discipline" cannot be passed down across a gap. However, it can be rediscovered by other people. Make a note to identify nation-cultures within up to 3 timezones (either before or after) from Belgrano who have strong discipline-based cultures, and could serve as prospective newcomers who would diligently revive the old ways."* Noted in `Station_Heritage_Removal_Tracker.md` R-2 |

# 2026-10-01 — rulings on the ULM files audit (`Cities/ULM_Files_Mistake_Audit.md`)

## `DR-26` · ✅ **NEWCOMERS CAN INHERIT A STATION'S RESEARCH, EQUIPMENT, TECHNIQUES AND RESULTS**

**Developer, verbatim:** *"it's perfectly possible for newcomers to inherit the research, equipment, techniques,
results, etc. That doesn't need to get thrown away"*

| | |
|---|---|
| **Inheritable** | Alongside records (`DR-25`) and infrastructure (`DR-24`): the station's **research** (data, results, ongoing datasets), its **equipment**, and its **techniques**. A city may take up research it found in the station's records and equipment and carry it on as its own |
| **Still not inheritable** | A **tradition** passed person to person (`DR-25`), and the station's operator or nation as a reason for the city's **founders, identity, culture or ties** (`DR-19`) |
| **Writing it** | *"inherited the station's research results, equipment and techniques"*, never *"the research heritage is continuous from the founding station"* |
| **Zhongshan** | The audit's D1 question. The habitation continuity stands, as already stated in `No_National_Stereotypes.md` L17 and `DR-21`. The station's research, equipment and techniques are inherited under this ruling. What is struck: "organic", "research heritage", CHINARE heritage, "administration", and every Zhongshan-versus-Sinheung/Shirayuki contrast (rule of one location) |

## `DR-27` · ✅ **RAW RECORDS GO TO AN ARCHIVE, NOT THE BIN**

**Developer, verbatim:** *"store all that stuff in an archive folder, because we might still be able to use it for
something, even if it's not directly relevant to the establishing of a city"*

| | |
|---|---|
| **What moves** | Raw verification and run records: `T8` reader files, `T8` round records, superseded single-reader files, per-city `_archive_`/`_Archive` folders, and the `Test_Runs/` run folders and preps |
| **Where** | `Archive/ULM_Records/` at the repo root, mirroring the original paths |
| **Status** | Not canon and **not an input** to any ULM, CST or RWBEM pass. Kept for possible later use. Excluded from the heritage check script and (at its rebuild) from the knowledge graph |
| **What stays in place and gets fixed** | Live pass outputs, methodology files, `COLD_RUN_CHECKLIST.md`, `RESUME_HERE.md`, `OBSERVATIONS_and_Methodology_Findings.md`, `RUN_LOG.md`, and the worked-example files the runbook points to |

## `DR-28` · ✅ **AUDIT RECOMMENDATIONS ADOPTED (D2–D4, D6–D8)**

**Developer, verbatim:** *"everything else, your recommendations should work fine."*

| | Ruling |
|---|---|
| **D2 Namesakes and real-site history** | A Saint already canon in `National_Holidays.md` stays as **Federation-wide** veneration. A city's identity, core value, founding logic or name-meaning is **never** derived from its namesake or the real site's history. Keeping a station's name is a naming fact only |
| **D3 Station life as a comparable** | General polar-station practice anywhere is an ordinary real-world comparable (`DR-15`). Anything about the station at the city's **own** coordinates (its operators' joint management, incidents, resupply, bans) is that site's history and not an input. Physical facts stay |
| **D4 `Resettled` / `Installation`** | A real station's occupancy is never a prior population. No city is typed `Installation` because a station stood at its coordinates. Inherited records, research and equipment stay admissible as such |
| **D6 Census-tier ties** | Ties resting on census tiers wait for the post-ULM census review (`DR-23`). Only station-based wording is struck; the tie itself is never deleted |
| **D7 Unruled founders** | Station-derived founder lines for unruled cities read "UNRULED (Founding Register)" in ULM and datasheet files; the spec lines join the revisit list |
| **D8 "Inherited institution/capacity"** | Kept, per `DR-25`. Only the words "tradition" and "heritage" are struck. A guild "continuing the founding station's scientific mission" becomes a city that took up the station's research from its records and equipment (`DR-26`) |

## `DR-29` · ✅ **DAVIS AND SHIRAYUKI STAY; SEJONG AND LAZAR TO BE REVISITED**

**Developer, verbatim:** *"in terms of your findings for Davis and Shirayuki, Davis can stay as is, because (due to
geographical proximity), it's perfectly reasonable that Davis actually would've been founded and established by
Australians, so that works just fine. Shirayuki also has a Japanese founding population, so that can stay, too.
However, Sejong and Lazar will both need to be revisited."*

| | |
|---|---|
| **Davis** | Australian founding stands on geographic proximity. The spec's Australian founding-wave lines and the ties they draw to Casey and Mirny **stay as written** (audit Part C, Davis rows withdrawn) |
| **Shirayuki** | The Japanese founding population stands. The spec stays; its lines about **Sejong** and **Lazar** are handled by those two cities' revisits |
| **Sejong** | Revisit (already ruled not Korean, `DR-20`) |
| **Lazar** | **Revisit, new.** Its founders are unruled, and the spec's "founding Russian demographic" and its "coalescing with the… Russian Novolazarevskaya station" story come from the station |

## `DR-30` · ✅ **SAYOWA: FIRST ESTABLISHED BY THE CIN OR KAZAKHSTAN, INDUSTRIALIZED BY KAZAKH INDUSTRIALISTS**

**Developer, verbatim (2026-10-01):** *"the actual, real-world "Syowa/Showa" Station is nowhere near Japan. Not even
close. However, I did notice that, in near-perfect alignment with that particular GPS location were the Confederacy
of Intermarium Nations (the CIN), Russia, and Kazakhstan; three cultures that I personally have lived through and
known to have cultures of hardworking men who are capable of facing brutal conditions and achieving incredible
results. We already have the currently-yet-unnamed city of `{{ Abowasa }}` as being founded and established via a
joint venture by the CIN and Italy, so for `{{ Syowa/Showa }}`, I was thinking to have that city first established by
either the CIN or Kazakhstan, and then become industrialized primarily, most notably, by Kazakh industrialists, and it
later became the city that it is during the Second Interwar Period. It still gets its status as a heavily industrial
city, with all its shipping/freighter activity; it's just a "change in flag"."*

| | |
|---|---|
| **Founders** | **First established by the CIN or by Kazakhstan** — which of the two is still open. Then **industrialized primarily by Kazakh industrialists** |
| **Basis** | Time-zone proximity: Sayowa ≈ solar UTC+3; the CIN ≈ +1…+2; Kazakhstan ≈ +3…+6 (`Post-War_Nations_Founder_Reference.md`). Not Japan. Russia aligns too but was not named as a founder |
| **What stays** | Its status as a **heavily industrial city with its shipping and freighter activity**. The change is the founders ("a change in flag"), not the city's function |
| **Closes** | The Sayowa half of `DR-20a` and `DR-22`'s "Sayowa: open". **Still open:** CIN or Kazakhstan as the first establisher; whether the name changes (the developer wrote it as a placeholder, `{{ Syowa/Showa }}`) |
| **Still to do** | Sayowa stays on the revisit list: its spec, culture, catalog and datasheet text still carry the Japanese founding. The census is untouched until the full ULM is done (`DR-23`) |

## `DR-31` · ✅ **THE LAW FILE, `CLAUDE.md` AND THE HOOK — APPROVED CHANGES; THE ACTS ARE A HAZY RANGE**

**Developer, 2026-10-01, item by item on the proposed changes to `No_National_Stereotypes.md`:** "station-builder
nation" wherever the station's builder is meant · L30 rewritten · *"we use the founding register file to determine
who the founders are"* · the worked case becomes Argentina (*"if only one, I think Argentina is the better example"*) ·
Zhongshan's exception rests on access · *"Records, research, results, equipment, and techniques can also be inherited
as well"* · "ex-program exiles" replaced · "identities" → "stories" · on naming: *"If no historical figure, fact, etc
is immediately apparent, don't force one. It's better to input nothing, than to create something wrong as being
'fact'"*.

| | |
|---|---|
| **The Acts** | *"it's more of a hazy range. The exact dates are better-left for after the new vignettes are finished, and we figure out what order they go in and roughly how far apart they're spaced along a timeline."* The "first 18%" / "~40–50 years" / "about 200 of 248 years" figures are gone from the law file, the era README, the runbook, the reference sheets, the Neo-Races framework and the pass files; Act 1 is "2564 → somewhere in the 2600s, a hazy range" |
| **`World_History_Reference.md`** | *"position/location, not 'possession'"* — the stations' positions are the source of city geography, coordinates only |
| **`CLAUDE.md`** | Rule (1) now says founders come only from the Founding Register, on geography and access |
| **The search hook** | Stays OFF: *"while it was turned on, it ended up causing infinitely more problems than it solved"* |
| **Applied 2026-10-01** | `No_National_Stereotypes.md` (both repos' references follow it: the ULM quick-reference sheet and `Human_Universals_Culture_Framework.md` §1) |

## `DR-32` · ✅ **NAMESAKES ARE NEVER A BASIS FOR DATA · SAYOWA WILL BE RENAMED · MAWSON/KAZAKHSTAN NOTED**

**Developer, verbatim (2026-10-01):** *"namesakes are never a basis for data. Those are strictly just neat, interesting
in-world details"* · on Sayowa's placeholder name: *"`{{ Syowa/Showa }}` is guaranteed to be renamed. At the moment, I
currently have no idea what, but it will definitely get a new name for sure"* · on Mawson: *"Mawson is actually
directly underneath Kazakhstan, so that could very well be a valid option for a founding nation"*

| | |
|---|---|
| **Namesakes** | A city's namesake (a person the real station or the city is named for) is **flavor only**: a neat in-world detail, never an input, a tie, a reason or data. Applies to the Davis↔Mawson connection: the Aurora relief voyage may appear as an in-world detail but grounds no tie. The two cities' tie, if any, stands on the Register and the map |
| **Sayowa** | **Will be renamed** (new name not yet chosen; add to the rename list `R-17`). `{{ Syowa/Showa }}` stays a placeholder until then |
| **Mawson** | **An option noted, not a ruling.** Mawson stays Australia in the Register (`DR-19`). Kazakhstan (≈ +3…+6; Mawson ≈ +4) is a possible founding nation for the revisit. Mongolia was a mis-sighting on the map |

---

# OPEN, ARISING FROM THESE RULINGS

| | Question | Owner |
|---|---|---|
| **`DR-1a`** | Does the Elementals pullback reach the **district** substrate (`Zodiac_Personality_Substrate/A_Elements.md`), or only the city Elementals? | ⏸️ developer |
| **`DR-3a`** | How does the early per-subnet currency layer reconcile with the existing local → national → regional + trade-standard SHAPE (backing unsettled at every stage — not "energy-backed")? | ⏸️ **future — gated behind all 38 × 3** |
| — | Back-fill prior developer rulings into this log from `00_RUNBOOK.md`, `CLAUDE.md`, and the observations file | ⏸️ **not mid-pass** |
| **`DR-10a`** | Is `DR-10` corpus-wide, as its wording reads? And `00_RUNBOOK.md` L2787 still lists "vision session" material as a Tier 2, primary input at Step 5 — does that row need amending to match? | ⏸️ developer |
| **`DR-11a`** | `00_RUNBOOK.md` §C.9b constraint 2 (L2119–2121) still calls robot national origin "an open reserved question" — amend in place. And is this a universe-level **Who** fact that belongs upstream in `TepenianUniverseTimeline/Reference/Robot_Universals/` (`00_RUNBOOK.md` §A; §E question 3)? | ⏸️ **awaits OK** — a change to existing files |
| **`DR-15a`** | `01_Frame_Typology_and_Inheritance.md` L500 routes substitute (3) *"via `Real-World_Basis_Extrapolation_Method.md`"*; under `DR-15` it runs via the ULM's own Step 3 research. `Run_Modes_Warm_and_Cold.md` L124–126 also still says to run all **four** substitutes, including (2), which `00_RUNBOOK.md` L445 excludes | ✅ **Done 2026-10-01** (audit fixes): `01` routes substitute (3) through the ULM's own Step 3 research; `Run_Modes` now runs only the peer-free substitutes |
| **`DR-17a`** | Where to register a city pass's provisional assumptions about its unwritten parent subnet (`01` L440–441) | ⏸️ **developer + assistant, together** |
| **`DR-20a`** | Who first established Sejong and Juan Carlos (within the Americas-wide Anglo-Latin founding). *(Sayowa ruled `DR-30`, apart from CIN-or-Kazakhstan as its first establisher; Princess Elisabeth ruled `DR-22`, the STU)* | ⏸️ **developer + assistant, together** — a detailed look, in the operating window |

> ✅ `DR-8a` — **SETTLED, 2026-09-16.** Step 4, Phase 10. Folded into `DR-8` above; no longer open.

> ⚠ **`DR-1` × `DR-8` interaction, flagged and clarified same day.** `DR-8`'s §B3 means every city's Phase 10
> will, soon, actually need to open the symbol-substrate files and apply a member's meaning. **Only one of the
> two systems has content work outstanding:**
>
> | System | Status, developer-confirmed 2026-09-16 |
> |---|---|
> | **Planetary Symbols** (9 planets + the Asteroid Belt, 10 members) | ✅ **ALL 10 OFFICIAL — no work needed on the existing set.** *"I wrote all of them myself."* Matches the count already on record at `00_RUNBOOK.md` §C.7. ⏸️ **Possible 11th member under consideration: the Sun** — *"since the Asteroid Belt already is [a non-planet member] as well."* Not yet decided; existing 10 stand regardless |
> | **Robot Elementals** (8 members) | ⛔ **Only Electricity is settled outright.** Electromagnetism, the second previously-"developer-authored" member, is now itself **under reconsideration** — *"somewhat considering redoing back to just 'Magnetism,' though I'm not sure about that."* **Earth · Air · Fire · Water · Wood · Metal remain in unrevised "ancient traditional" form** and need attention, per `DR-1` |
>
> **So the real gap is narrower than "six of eight" now reads in `DR-1` above** — it may be **seven** pending
> the Electromagnetism/Magnetism decision, and Planetary Symbols drop out of scope entirely. **Developer,
> same-day note prompting this:** *"very soon, I'll need to figure out the actual exact meanings of the
> currently-unsettled Elementals."*
>
> ✅ **RESOLVED 2026-09-21 — see `DR-1`'s own resolution above.** Electromagnetism reverted to Magnetism;
> all six pulled-back members rebuilt on physical derivation. The row above is the state as of 2026-09-16 and
> is superseded.
>
> ⏸️ **Owner: developer.** Not blocking Phases 1–9 of any city by the mechanism itself — only Phase 10 §B3 for
> a city whose profile points at one of the unsettled Elemental members. **Sequenced as a pre-requisite
> anyway, developer decision 2026-09-16: settle it before starting the ULM on the next city**, rather than
> risk hitting it as a mid-pass interruption partway through an otherwise-continuous 11-phase run.
