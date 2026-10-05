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
| **Mawson** | **~~An option noted, not a ruling.~~ ✅ RULED in `DR-33`, 2026-10-03: Australia and Kazakhstan are co-founders.** Kazakhstan (≈ +3…+6; Mawson ≈ +4). Mongolia was a mis-sighting on the map |

---

## `DR-33` · ✅ **MAWSON: CO-FOUNDED BY AUSTRALIA AND KAZAKHSTAN · SIGNY'S SOUTH AFRICAN ROLE CONFIRMED · FOUNDING-NATION AUDIT AND PROPOSALS ARE ANY-HOUR WORK**

**Developer, verbatim (2026-10-03):** on Signy: *"it is perfectly geographically feasible for it to have been established partially in part by South Africa."* · on Mawson: *"let's write Mawson as having co-founder nations between Australia and Kazakhstan."* · on hours: *"this task can run outside of designated hours, because it's really me who's doing the majority of the thinking."*

| | |
|---|---|
| **Mawson** | **Founders: Australia and Kazakhstan, jointly.** Australia stands on `DR-19` (geography and access; its nearest zone is +8 against Mawson's +4, a gap of 4, a ruled exception to the "two, maybe three" test); Kazakhstan stands on geography (Mawson lies directly south of it; zone gap 0). Closes `R-23`. **Supersedes** the *"option noted, not a ruling"* row of `DR-32` |
| **Signy** | South Africa's **partial** founding is **confirmed** as geographically feasible (gap 4 on the zone test; the Cape Town–South Orkney crossing). The co-founder(s) remain open |
| **Hours** | The **Founding Register audit and proposals** are not restricted to the 05:00–14:59 window (the developer makes the decisions; the session does the arithmetic and assembly). **Scope: this task only.** Proposals are candidates the developer rules, never canon |
| **Follow-on** | `Mawson.md`'s `Founding population` line is a spec revisit item (it names Australia alone): add to the revisit queue; **no spec edited now**. `Sayowa` (`DR-30`) already names Kazakhstan as an industrializer; the two rulings are independent and neither is justified by the other |

---

## `DR-34` · ✅ **SIX FOUNDING ROWS RULED FROM THE PROPOSALS · SEJONG, NEUMAYER, VOSTOK DIRECTION · "RUSSIA" IS THE CORE STATE**

**Developer, verbatim (2026-10-03):** *"cities that I actually really, really like your 'proposed founder(s)' suggestions for: Port Lockroy, Juan Carlos, Lazar, Kunlun, `{{ Bunger Hills City }}` (yet-to-be-named), and Scott. We can confirm those on the founding roster file as canon."*

| | |
|---|---|
| **Port Lockroy** | **Chile** |
| **Juan Carlos** | A primarily Anglo-Latin society of immigrants from the Americas (`DR-20`); **first founders: Uruguay** |
| **Lazar** | **Russia (the core state) and the CIN, as two communities that coalesced**; the spec's Indian half is replaced (no South Asian population, `NNS` L44) |
| **Kunlun** | **The founding stock of Vostok (the launching community, via Highway 37), plus the Sinian Federation (China)**; a robot-only city, so *founding nation* is the robots' learned origin (`DR-11`). **Depends on Vostok's final ruling** |
| **{{Bunger Hills City}}** | **Indonesia and Malaysia, jointly**. The city is yet to be named |
| **Scott** | **New Zealand** |

**Direction given, then ruled in `DR-35`** (same day):
- **Sejong:** *"Chile first, then English-speaking arrivals"*, **then** they *"would invite people first from Palmer City (which has representation from every country) and then later from Korea, to help translate the records, logs, manifests"* of the inherited setting.
- **Neumayer:** *"the Netherlands and Austro-Bavaria (since they'd be able to make the quickest re-upstart of the setting)."*
- **Vostok:** *"Mongolia definitely"*, but **not Russia**: *"it would be one of the resulting countries, in all likelihood probably either Siberia or Kunnarantaiga"* (the Russia map series, `/media/y-files/Map Files/Russia/`).

**⭐ "Russia" is the core state, not the old whole.** In the authoritative series (`02 reorganization/09 follow-up`) **Russia** is the Moscow-area core (zones +2…+3); Buryatia, Irkutsk and Chita belong to **Künnarantaiga**; **Siberia** is the west-Siberian band (Novosibirsk, Omsk, Tomsk, Tyumen, Krasnoyarsk). Wherever a pool or a founder says "Russia", read the **core state** unless a successor is named. **Consequence for later:** `DR-9` names *Russia* for Mirny in pre-war terms; the CST recast will need a successor state (Mirny's zone is +6).

| | |
|---|---|
| **Follow-on** | The six specs' `Founding population` lines contradict their rows until revisited (a post-ULM revisit item; **no spec edited now**). Gateway statements in the rows are **general knowledge, not researched** (`LAW 0-R`) |
| **Hours** | Founding-Register work stays any-hour (`DR-33`) |

---

## `DR-35` · ✅ **VOSTOK, SEJONG AND NEUMAYER RULED**

**Developer, verbatim (2026-10-03):** *"Go with Künnarantaiga for Vostok (as a joint-establishment with Mongolia), confirm Sejong (with Palmer City, then Korea, etc), and confirm Neumayer (with The Netherlands and Austro-Bavaria)."*

| City | Ruling |
|---|---|
| **Vostok** | **Künnarantaiga and Mongolia, jointly.** Künnarantaiga is a successor of the old Russia in the developer's maps; **not Russia itself** (Siberia and Tuva were the other zone-aligned successors and are not chosen) |
| **Sejong** | A primarily Anglo-Latin society of immigrants from the Americas: **first founders Chile; then English-speaking arrivals; then people invited from Palmer City** (canon: representation from every country) **and later from Korea**, to translate the inherited records, logs and manifests. Korea's later role is as translators, not founders |
| **Neumayer** | **The Netherlands and Austro-Bavaria, jointly** |
| **Kunlun (follow-on)** | Its stock follows Vostok: **Künnarantaiga and Mongolia, plus the Sinian Federation** (`DR-34`) |
| **Closes** | `DR-20a` (who first established Sejong and Juan Carlos): Sejong **Chile**, Juan Carlos **Uruguay** (`DR-34`). The *"Direction given, not yet ruled"* paragraph of `DR-34` is now ruled |

---

## `DR-36` · ✅ **`{{ Abowasa }}` IS RENAMED SANTA LUCE**

**Developer, verbatim (2026-10-03):** *"just from the possibilities alone, I can already confirm that `{{ Abowasa }}` officially gets renamed to Santa Luce, and this is for a few reasons. Not only due to the similarity to "Santa Maria", but also, "Luce" meaning "light" (and therefore, not committing an act of blasphemy), plus, to native Polish-speakers, the pronunciation of the word "Luce" would be identical across both Intermarians and Italians"*

| | |
|---|---|
| **Ruling** | The city formerly `{{ Abowasa }}` is named **Santa Luce**. Italian *santa* "saint" + *luce* "light". Closes `R-16`. Chosen from the candidate set in `Cities/City_Renaming_Candidates_2026-10-03.md` (§2) |
| **Developer's stated reasons** | (1) it follows the "Santa Maria" line (`R-16`); (2) *luce* is "light", so no blasphemy; (3) the developer's belief that the pronunciation is the same for Italians and Intermarians (see the correction below) |
| **Founders unchanged** | Italy and the CIN, jointly (`DR-22`). The new name is *not* a reason for any founding fact (`DR-32`: names are flavor, never data) |
| **Real-world note** | Santa Luce is also a real Tuscan comune (pop. ~1,600, Pisa province), an altered form of Santa Lucia. A coincidence of name, not an input |
| **⚠ Pronunciation: a correction to reason (3), recorded, not ruled** | In Italian *luce* is /ˈlu.tʃe/ ("LOO-cheh"). Polish, Czech, Slovak, Hungarian, Slovene and Serbo-Croatian write the sound /ts/ as ⟨c⟩, so a speaker reading the spelling *Luce* says "LOO-tseh", **not** the Italian sound. Romanian and Moldovan read ⟨ce⟩ as /tʃe/, the same as Italian. So the shared-pronunciation premise holds for the Romanian-speaking Intermarians only. **Awaiting the developer:** the divergence can stand as in-world texture (two spoken forms of one written name), and Phase 8 could use it; or the premise is dropped. Neither is written into canon yet |
| **Still to do** | The rename sweep (about 179 files plus 29 Background-Lore files that are **never** edited): needs the developer's OK on the plan. Until then the old text still reads *Abowasa* and `{{ Abowasa }}` stays the working designation in files; the **Tepenia maps already use Santa Luce** |

---

## `DR-37` · ✅ **`{{ Sayowa }}` IS RENAMED TEMIRÖTKEL (темірөткел)**

**Developer, verbatim (2026-10-03):** *"for `{{ Sayowa }}`, how about "темірөткел" ("Iron Crossing/Passage")?"* → *"Excellent. Temirotkel (темірөткел) is confirmed as official for `{{ Sayowa }}`"*

**Developer, verbatim (2026-10-03), romanization:** *"and the romanization would be "Temirötkel" for темірөткел"*

| | |
|---|---|
| **Ruling** | The city formerly `{{ Syowa/Showa }}` / `Sayowa` is named **Temirötkel** (Kazakh **темірөткел**). **The official romanization is `Temirötkel`, with the ö, by developer ruling.** *(Wiktionary's Latin for the parts is* temır *and* ötkel*; the developer's form uses a plain* i*. A diacritic-free variant "Temirotkel" is not ruled either way.)* Kazakh *темір* "iron" + *өткел* "crossing, passage; ford": "Iron Crossing". Closes the Sayowa half of `R-17` and `DR-32`'s "Sayowa will be renamed" |
| **Research basis** | *өткел* verified in two sources (Wiktionary; Kazakh Wikipedia, which uses it for a ford, a pedestrian or military crossing, a mountain pass and the Northwest Passage). *темір* verified in Wiktionary. **The compound is a coinage**: zero hits for "Темірөткел" or "темір өткел" on Kazakh Wikipedia, built on the real one-word pattern of *теміржол* and *Темиртау*. Search was unavailable (budget spent); a second dictionary for *темір* is still owed |
| **Founders unchanged** | First established by the CIN **or** Kazakhstan (still open), then industrialized primarily by Kazakh industrialists (`DR-30`). The name does **not** decide the first establisher; it reads naturally as the industrialists' name for the city. The name is flavor, not data (`DR-32`) |
| **Open, not ruled** | (a) which of the CIN or Kazakhstan first established it; (b) the in-game pronunciation and stress (Kazakh stress falls on the last syllable: "teh-meer-ot-KEL"); (c) whether the English gloss "Iron Crossing" is shown anywhere (it echoes "Iron Cross") |
| **Still to do** | The single rename sweep, **held by the developer until all four names are settled**. Until then the old name stays as the working designation in files |

---

## `DR-38` · ✅ **`{{ Princess Elisabeth }}` IS RENAMED UTSTEIN (native form UTSTEINEN)**

**Developer, verbatim (2026-10-03):** *"For `{{ Princess Elisabeth }}`, yeah, I would say that "Utstein" ("Utsteinen") works the best."* · on which form is the city's name: *"Utstein is the English (national) name, and Utsteinen is the "native" name (similar to the way that Göteborg is noted as "Gothenburg" in English/International"*

| | |
|---|---|
| **Ruling** | The city formerly `{{ Princess Elisabeth }}` is named **Utstein** (the English / national form) and **Utsteinen** (the native Norwegian form). Same pattern as Göteborg / Gothenburg: one place, a native name and an English one. Closes the Princess Elisabeth half of `R-17`. Chosen from the candidate set in `Cities/City_Renaming_Candidates_2026-10-03.md` (§4, candidate 1) |
| **Meaning** | Norwegian *ut* "out" + *stein* "stone": **"the outer stone"** (*Utsteinen* with the definite ending: "the Outer Stone"). The Norwegian Polar Institute place-name API records it as the real nunatak's own name (origin: Norwegian, proposed by "Sør-Rondane 1957"), named for its position north of the Viking Heights. The city takes its mountain's name; the princess and the station are not in it |
| **Founders unchanged** | The Scandinavian Trade Union nations, jointly (`DR-22`). The name is flavor, never data (`DR-32`) |
| **Which form where** | Per the developer: **Utstein** in English / national text; **Utsteinen** as the native form. Exactly which in-game contexts use which is not ruled (a Phase 8 / catalog question) |
| **Real-world note** | Utstein Abbey and Utstein Church (near Stavanger), the "Utstein Style" cardiac-arrest guidelines and a submarine class share the root. A coincidence of name, not an input. The pronunciation guide "OOT-stine" is the researcher's approximation and is UNVERIFIED |
| **Still to do** | The single rename sweep, **held by the developer until all four names are settled** (three are now ruled; Bunger Hills City remains). Until then the old name stays the working designation in files |

---

## `DR-39` · ✅ **`{{ Bunger Hills City }}` IS RENAMED RELUNG PANEN**

**Developer, verbatim (2026-10-03):** *"I think we can go with "Relung Panen""* · after the question *"would it make grammatical sense to call a place "Relung Panen"?"*

| | |
|---|---|
| **Ruling** | The city formerly `{{ Bunger Hills City }}` is named **Relung Panen**. Indonesian *relung* + *panen*. Closes the last open name of the four (`DR-36` Santa Luce, `DR-37` Temirötkel, `DR-38` Utstein, `DR-39` Relung Panen) and `DRQ-05c` (the name). The Casey spur is now "the Relung Panen Spur" |
| **Meaning** | *Relung* (KBBI, noun): "a hollow or depression in earth or mountainside; a niche in a temple or building for placing statues". *Panen* (KBBI, noun): "harvesting crops from fields or gardens". Head noun first, modifier second: "the harvest hollow / the hollow of the harvest" (compare *relung hati*, *relung ekologi*). **The oasis is a hollow walled in by ice and its job is the harvest**: the name states both |
| **Founders unchanged** | Indonesia and Malaysia, jointly (`DR-34`). The name is flavor, never data (`DR-32`) |
| **Research basis** | Both words verified in KBBI (`kbbi.kemendikdasmen.go.id`); the phrase "relung panen" has **zero hits** on Indonesian Wikipedia: **a coinage** on a standard construction. Web search was unavailable (budget spent) |
| **Open, not ruled** | (a) Kamus Dewan labels *panen* **Javanese** (Malaysians would say *tuaian*), so a Malay-natural form "Relung Tuaian" exists and was not verified; (b) pronunciation ("ruh-LUNG PAH-nen" is the researchers' respelling, unverified); (c) whether it is ever shortened to "Relung" |
| **Still to do** | The single rename sweep the developer ordered: *"Wait until all four names are settled, then just do one single sweep."* All four are now settled |

---

## `DR-40` · ✅ **PORT LOCKROY IS RENAMED PUERTO ABRIGO**
**Developer, verbatim (2026-10-03):** *"Port Lockroy --> Puerto Abrigo [conclusive]"*

| | |
|---|---|
| **Ruling** | Port Lockroy is named **Puerto Abrigo**. Spanish *puerto* "port" + *abrigo* "a coastal spot where ships shelter from wind, waves and currents" (nautical sense; also "overcoat", "protection"). Chosen from `City_Renaming_Candidates_Batch2_2026-10-03.md` §1. Founders unchanged: Chile (`DR-34`) |
| **Basis** | The harbor's defining fact is its natural shelter behind Goudier Island. Verified on es.wiktionary, en.wiktionary and WordReference's DLE text; the RAE itself was unreachable (403). No town or port of this exact name was found; the idiom *de abrigo* ("troublesome") exists only inside that phrase |
| **Still to do** | The batch-2 sweep, **held until all four batch-2 names are settled** (Sejong is still open), and the Mirny-pass inputs held as before |

## `DR-41` · ✅ **JUAN CARLOS IS RENAMED PERGAMINO**
**Developer, verbatim (2026-10-03):** *"Juan Carlos --> Pergamino // (as it means "Parchment") [conclusive]"*

| | |
|---|---|
| **Ruling** | Juan Carlos is named **Pergamino**. Spanish *pergamino* "parchment": animal skin prepared for writing, hence a written title or document (es.wiktionary; from Greek *pergamēnḗ*, "of Pérgamo"). It fits the city's canonical function (Tepenia's first bureaucratic archive). Founders unchanged: Uruguay first (`DR-34`) |
| **⚠ Collision, recorded for the developer** | **Pergamino is also a real city in Buenos Aires Province, Argentina** (the seat of the Pergamino partido; es.wikipedia disambiguation), on the Río de la Plata side of the Uruguay-first founders' own region. A coincidence of name, not an input (`DR-32`); not a reason to change the ruling |
| **Not checked** | Rioplatense and Chilean slang (no regional label on es.wiktionary; no lunfardo source reachable) |
| **Still to do** | The batch-2 sweep, held as above |

## `DR-42` · ✅ **VOSTOK IS RENAMED ARIUN NUUR (Ариун Нуур); THE CENTRAL SCIENTIFIC DISTRICT KEEPS "VOSTOK"**
**Developer, verbatim (2026-10-03):** *"Vostok --> Ariun Nuur (Ариун Нуур) [conclusive]"* · earlier the same day: *"…with the central scientific district still being called "Vostok" out of a sense of honoring and respect for history and the past scientists who dedicated (and possibly even sacrificed) their lives so that Tepenians could have a city of scientific research"*

| | |
|---|---|
| **Ruling** | The city is named **Ariun Nuur** (Mongolian **Ариун Нуур**). *Ариун* "pure, clear, clean; holy" (en.wiktionary; ru.wiktionary gives "sacred") + *нуур* "lake": "the pure lake", for the subglacial Lake Vostok beneath it. **The central scientific district keeps the name "Vostok"**, as a deliberate honor to the past scientists. Founders unchanged: Künnarantaiga and Mongolia (`DR-35`) |
| **Basis** | Mongolian words, verified once or twice on Wiktionary (*ариун* PARTLY: the two Wiktionaries differ on "pure" vs "sacred"); *нуур* confirmed. The two-word phrase "Ариун Нуур" returned no Wikipedia hit, so it is a plain adjective-plus-noun phrase, not an attested place name |
| **Open** | the district's boundaries and exactly what "Vostok" names inside Ariun Nuur are not set; whether the name is written "Ariun Nuur" or "Ariun-Nuur" in Tepenian text |
| **Still to do** | The batch-2 sweep, held as above |

---

## `DR-43` · ✅ **SEJONG IS RENAMED CONTRAPUNTO — ALL FOUR BATCH-2 NAMES SETTLED**
**Developer, verbatim (2026-10-03):** *"I'm especially liking "Contrapunto""* → *confirmed as final* (answer to "Is Contrapunto your final pick for Sejong?": **"Final: record it as DR-43"**)

| | |
|---|---|
| **Ruling** | Sejong is named **Contrapunto**. Spanish *contrapunto*: the technique of independent melodies heard together; **in Chile, Argentina and Uruguay also a verse duel between two improvising poets, each answering the other** (es.wiktionary; DAMER). The name from the Chilean first founders, in Spanish (developer's earlier answer). Founders unchanged: Chile first, then English-speaking arrivals, then Palmer City, then Korea as translators (`DR-35`) |
| **Chosen from** | `City_Renaming_Candidates_Batch2_2026-10-03.md` §3c (the "meeting place / melting pot" round) |
| **Known costs** | four syllables; Aldous Huxley's *Point Counter Point* appeared in Spanish as *Contrapunto*; a Caracas news portal and a Peruvian TV show; no Chilean or Argentine place found. Chilean slang could not be checked (no corpus reachable), so a Chilean reader should confirm |
| **Batch 2 is now complete** | Port Lockroy → **Puerto Abrigo** (`DR-40`) · Juan Carlos → **Pergamino** (`DR-41`) · Sejong → **Contrapunto** (`DR-43`) · Vostok → **Ariun Nuur** (`DR-42`; the central scientific district keeps "Vostok"). Mirny remains "eventually" |
| **Sweep ruling (developer, same day)** | **Sweep the non-held files now; the 6 held Mirny-pass inputs later** (after the Mirny pass finishes), when the held-file tool will cover both batches |

---

## `DR-44` · ✅ **THE REMAINING FOUNDING ROWS RULED: ALL 38 CITIES NOW HAVE A RULED FOUNDING (HALLEY'S "CENTRAL ROLE" AND TEMIRÖTKEL'S FIRST ESTABLISHER STAY PARTIAL)**

**Developer, verbatim (2026-10-03):** *"At the moment, Australia is rather heavily overrepresented in founding nations. I'm not saying that Zukelli shouldn't be Australian-founded. Just that maybe one of the other Australian-founded cities can be founded by someone else. Not a requirement; just a thought for consideration."* · *"Dumont d'Urville can definitely have been founded by Japan. That makes excellent sense."* · *"Byrd was rather less founded by any Upper-Earth country, and more by a joint team of first-wave Tepenians from the Peninsula and the Halley coast."* · *"For Signy, yeah, that works."* · *"Everything else looks fine."* · *"for Shirayuki and Sinheung … I would change that to geography being an additional factor, on top of the agreement at the Court of Jeju-Do"* · *"all of the 'Ruled founders' listings are right"* (for Rothera, Santa Luce, Utstein, Dome Fuji, Fort McMurdo)

| Row | Ruling |
|---|---|
| **Dumont d'Urville** | **Japan** (zone gap 0; Adélie Land at 140°01′E lies on almost the same meridian as Tokyo). Not France |
| **Byrd** | **A joint team of first-wave Tepenians from the Peninsula (the Palmer subnet) and the Halley coast (the Halley subnet).** Not founded by any Upper-Earth country; the zone test does not apply. Supersedes the spec's "American exiles" |
| **Signy** | **South Africa (partly) and Brazil.** Brazil: zone gap 0 |
| **Zukelli** | **Australia** (zone gap 1), from the developer's shortlist. Not Italy |
| **Denison** | **Australia** (zone gap 0; Commonwealth Bay is almost due south of Tasmania) |
| **Cape Adare** | **Mixed; no single dominant national community**: an empty slot by ruling (the empty-slot law), not a gap |
| **Palmer City · Amundsen Station · Concordia** | **Not nation-based.** Palmer City: three groups united by their relationship to robots (`DR-16`). Amundsen Station: rotating multi-subnet technical crews. Concordia: robots and human partners who went inland, then waves of coastal refugees; the French/Italian station is not a reason (`DR-19`) |
| **Shirayuki · Sinheung** | Japan and Korea stay, **by the Jeju-do court's diplomatic allocation, with geography (zone gap 3 to the Prydz Bay coast) as an ADDITIONAL factor** on top of it. Not a rewrite of the basis. Closes `FQ-13c` |
| **Rothera · Santa Luce · Utstein · Dome Fuji · Fort McMurdo** | Re-statused ⛔ → ✅: the register's founders were right, the **specs** still contradict them (revisit items). **Consequence for Rothera:** Argentina stays a founder alongside North America, so `DR-22`'s "only Belgrano, Marambio and Esperanza" described the specs as they then stood; Argentina founds **four** cities. Closes `FQ-13b` *(inferred from "all the ruled founders listings are right"; confirm if wrong)* |

**Open thought (not a requirement), `FQ-20`:** Australia was a founder of six cities (Mawson with Kazakhstan, Mirny, Casey, Davis, Denison, Zukelli; Mawson was then removed, `DR-45`). The developer asks whether **one of the other Australian-founded cities** could be founded by someone else, while stressing that Zukelli itself may well stay Australian-founded. **No row changed.** The register's own measured pools: Denison could be Papua New Guinea or Künnarantaiga (zone gap 0), New Zealand, Korea or Indonesia (gap 1), or a joint founding; Casey and Davis (`DR-19`) are already ruled.

**Still not researched:** the gateway statements (`FQ-15`). **Still to do:** the spec revisits for every row whose spec contradicts the register (the check script lists them).

---

## `DR-45` · ✅ **MAWSON: AUSTRALIA REMOVED AS A FOUNDER; KAZAKHSTAN STAYS, JOINTLY WITH A CO-FOUNDER TO BE CHOSEN**

> ⚠ **REVERSED 2026-10-04 by `DR-53`: Australia is restored as a Mawson founder** (alongside Kazakhstan and Russia). The record below stands as history.

**Developer, verbatim (2026-10-03):** *"in that case, we can remove Australia from the founding of Mawson, though Kazakhstan would still jointly establish the city with somebody else"* (answering the list of six Australian-founded cities: Mawson, Mirny, Casey, Davis, Denison, Zukelli)

| | |
|---|---|
| **Ruling** | Mawson is **no longer** founded by Australia (`DR-33` amended). **Kazakhstan** remains a founder (zone gap 0: Mawson lies directly south of it), **jointly with a second founder not yet chosen** (`FQ-21`) |
| **Why** | `FQ-20`: Australia was a founder of six cities. It is now five (Mirny as one of three exile groups; Casey, Davis, Denison, Zukelli) |
| **Spec revisit** | `Specs/Mawson subnet/Mawson.md`'s `Founding population:` line says *"Australian exiles"* and must be rewritten once the co-founder is chosen |

---

## `DR-46` · ✅ **MAWSON: KAZAKHSTAN AND RUSSIA · MIRNY: FOUNDED BY IDELSK-URALIA, WITH RUSSIA, AUSTRALIA AND THE SINIAN FEDERATION AS EXILE GROUPS**

**Developer, verbatim (2026-10-03):** *"so far as Mawson's co-founder, I think a good option is Russia, and for Mirny, instead of being founded by Russia, it's Idelsk-Uralia (since they're slightly more closely timezone-aligned, and they'd have a reasonably strong-enough economy to support doing so), though Russia is still present along with Australia and the Sinian Federation as exile groups"*

| City | Ruling |
|---|---|
| **Mawson** | **Kazakhstan and Russia (the core state), jointly.** Closes `FQ-21`. Russia's core (+2…+3) is zone gap 1 to Mawson's +4 |
| **Mirny** | **Founded by Idelsk-Uralia**, which takes the founding-nation role Russia held; **Russia, Australia and the Sinian Federation are present as exile groups.** Idelsk-Uralia (+2…+5) is zone gap 1 to Mirny's +6, Russia's core gap 3. **Amends `DR-9`** (*"exiles from Russia, China and Australia"*): the three exile groups stand; what is new is the founding nation |
| **Australia's share** | five cities: Mirny (as an exile group), Casey, Davis, Denison, Zukelli |

⚠ **Mirny's ULM pass is live (Phase 5 is next).** Its frame, spine and Phases 2–4 were written on `DR-9`'s wording. **No pass file was touched** (frozen records and inputs). The founders line in `Specs/Mirny subnet/Mirny.md` (*"Primarily Russian exiles"*) and the pass's treatment of Russia need a deliberate in-window read when the pass reaches a step that uses the founders; whether Idelsk-Uralia is **also** one of the exile groups, or only the sponsoring founding nation, is read here as the latter (*confirm if wrong*).

**Spec revisits:** `Specs/Mawson subnet/Mawson.md` (*"Australian exiles"*) and `Specs/Mirny subnet/Mirny.md`.

---

## `DR-47` · ✅ **THE MIRNY SUBNET'S COLLOQUIAL NAME "THE AUSTRALIAN SUBNET" HAS AN IN-WORLD BASIS**

**Developer, verbatim (2026-10-03):** *"there is now a sufficiently solid case for the common people colloquially referring to that particular subnet as 'the Australian subnet', since Australia dominates the founding of the entire area"*

| | |
|---|---|
| **Ruling** | The nickname **"Australian"** (already in the specs: `Mirny ("Australian")`) is grounded in who founded the subnet: **common people call the Mirny subnet "the Australian subnet" because Australia is its leading founder** |
| **Register count (for the record)** | Australia founds **three of the subnet's nine cities**: **Casey** and **Davis** (sole founder) and **Mirny** (one of the exile groups, `DR-46`). The other six: Zhongshan (China), Shirayuki (Japan), Sinheung (Korea), Ariun Nuur (Künnarantaiga and Mongolia), Kunlun (that stock plus the Sinian Federation), Relung Panen (Indonesia and Malaysia). A plurality, not a majority; the colloquial name is the developer's call and stands |
| **Changed** | Nothing in canon files (the nickname is already used everywhere). Mawson and Janbogo still have no nickname (`project_subnet_nicknames`) |

---

## `DR-48` · ✅ **PRIMARY PORTS: USHUAIA (PENINSULA AND SCOTIA SEA SITES) AND HOBART (ADÉLIE, COMMONWEALTH BAY AND BUNGER HILLS SITES)**

**Developer, verbatim (2026-10-03):** *"So far as the 'Peninsula and Scotia Sea' sites, write all of those possibilities to file (so that we can refer to them in the future if we need to), and set Ushuaia as the main/primary port. For the 'Adélie and Queen Mary Land' sites, write all of those possibilities to file … and set Hobart as the main/primary port. So far as your combined results, from among your 'Proposed wording' prospects, write all of those possibilities to file … We'll take a look later and see which results are the best ones."*

| | |
|---|---|
| **Ushuaia** | **Primary port** for Pergamino, Puerto Abrigo, Contrapunto and Signy. Every other candidate is a recorded possibility: `Gateway_Ports_Peninsula_and_Scotia_Sea_2026-10-03.md` |
| **Hobart** | **Primary port** for Dumont d'Urville, Denison and Relung Panen. Every other candidate is a recorded possibility: `Gateway_Ports_Adelie_and_Queen_Mary_Land_2026-10-03.md` |
| **Basis wordings** | **Not chosen.** All options are recorded, several per row: `Founding_Basis_Wording_Options_2026-10-03.md`. The Register's Basis column is unchanged |
| **Not done** | `Locations/Infrastructure/Ports.md` (existing canon) is **not** updated; it names neither port. The post-war nation holding Ushuaia is unchecked (`DR-23`). A port does not change any founder |
| **Evidence** | First pass: `Research_Logs/Founding_Gateway_Research_A_…`, `B_…`, `C_…` (zero web searches possible). **RERUN the same day with working search** (the developer raised the limit): `…A2_…`, `…B2_…`, `…C2_…` (about 250 searches). The two ports files were corrected to the RERUN's figures and Round 2 wordings were appended to the wording-options file (developer: *"do all three"*); **`Bunger Hills` is on the Knox Coast of Wilkes Land**, corrected in the Relung Panen spec, dossier, composition file and input-status file |

---

## `DR-49` · ✅ **THE THREE MAINLAND AUSTRALIAN TERMINALS CARRY THE BULK FREIGHT; HOBART IS THE PRIMARY GATEWAY**

**Developer, verbatim (2026-10-03):** *"the three carry the bulk freight. Do some additional research to see if you can identify any particular applications of the port at Hobart, since it's on an island, rather than on the mainland"* (answering `FQ-23`)

| | |
|---|---|
| **Ruling** | The three new mainland terminals (**Bunbury** for Perth, **Outer Harbor** for Adelaide, **Jan Juc / Torquay / Flinders** for Melbourne, established 2026-09-26 in the CurrentNovelDocs repo; about 10 to 11 days each way) **carry the bulk freight** (iron ore, bulk building materials, surplus food). **Hobart** remains the primary port (`DR-48`) and the Antarctic gateway |
| **Follow-up requested** | Research **particular applications of the port at Hobart, because Tasmania is an island** rather than mainland. Results: `Research_Logs/Hobart_Island_Port_Research_*_2026-10-03.md` and `Ports.md` §3c |
| **Closes** | `FQ-23` (Hobart's relation to the three terminals). Fremantle's place next to Bunbury remains open |

---

## `DR-50` · ✅ **HOBART AND USHUAIA ARE THE PORTS OF TRANSFER FOR PEOPLE LEAVING UPPER EARTH**

**Developer, verbatim (2026-10-03):** *"the way it sounds to me: Hobart would be the actual port-of-transfer for people (both humans and robots) coming from the Asian span of the Eastern Hemisphere who are making their way out of Upper Earth on route to Antarctica, similar to Ushuaia serving as a port-of-transfer for people on their way to what eventually becomes Palmer City (and surrounding cities)."*

| | |
|---|---|
| **Reading recorded** | **Hobart**: the port of transfer for people (humans and robots) from the Asian span of the Eastern Hemisphere on their way to Antarctica. **Ushuaia**: the same role for people bound for Palmer City and the surrounding cities. **The three mainland terminals** still carry the bulk freight (`DR-49`) |
| **Matches** | `Upper_Earth_Immigration_Composition.md` "Real-world Antarctic access gateways" (Ushuaia/Punta Arenas → the Peninsula; Hobart/Fremantle → the East Antarctic coast, for Australia, Japan, Indonesia/SE Asia, China, South Korea) and `Airports.md` (Machu Picchu Airport, the only international airport, connects to Ushuaia; Palmer City reached by water only) |
| **Early stage (developer, same day)** | ***"In the early stages, it's kind of moot, because at the time of the signing of the Falkland Treaty, none of those airports have been built yet."*** At the Falkland Treaty (2564-06-21) there is no Machu Picchu Airport and no Tepenian airstrip, so **every early arrival comes by sea**; the processing question applies to **later eras** only |
| **Open** | (Later eras) where Hobart arrivals are formally processed once Machu Picchu exists as the only international airport; which Tepenian ports receive people from Hobart; whether robots are handled differently; whether the role continues in the Second Interwar Period; when the airports were built. See `Ports.md` §3d |

---

## `DR-51` · ⏸️ **THREE INTERNATIONAL AIRPORTS, NOT ONE: RECORDED AND DEFERRED**

**Developer, verbatim (2026-10-03):** *"this actually implies that there really need to be three international airports, and not just one. In the beginning, there would only be Marambio Airport and that's it. Later, there may be people immigrating, who are not coming from the Americas / Western Hemisphere. This is something to sort out later, once the country and the worldbuilding has been better-determined"*

| | |
|---|---|
| **Recorded** | Tepenia needs **three** international airports, not one; **early on, Marambio Airport is the only airport**; later immigration from outside the Americas / Western Hemisphere is what requires the others |
| **Status** | ⏸️ **DEFERRED ON PURPOSE.** *"Sort out later, once the country and the worldbuilding has been better-determined."* **Do not close it quietly** |
| **Not decided** | which three; where the other two stand; when each was built; whether the early-era airport is Marambio (`Airports.md` lists **Marambio Airport as domestic** and **Machu Picchu as the only international airport**; both statements describe one era each) |
| **Changed** | **nothing.** `Airports.md` is untouched; the conflict is recorded in `Ports.md` §3d and `follow-up_questions.md` (`FQ-24`) |

---

## `DR-52` · 💡 **THE TOWNS IDEA: REAL STATIONS ON STABLE GROUND, NOT ALREADY CITIES, BECOME TEPENIAN TOWNS** *(recorded 2026-10-03; idea, not yet a method)*

**Developer, verbatim (2026-10-03):** *"Now, something that I've come up with an idea for: once the cities themselves are complete, go through real-world data and look for actual Antarctican Stations that exist in steady, non-shifting locations, and whatever hasn't already been listed as currently-declared cities, those become towns. This way, we accomplish a few objectives: the country is essentially fully populated · in the DLCs, there are places to meet people and explore the in-world story and environment between major cities · in the WebTV show ("Southern Lights"), the in-world country feels that much more full. This is especially useful in regards to making the trek from the coast to either Ariun Nuur (Vostok), Kunlun, and/or Dome Fuji (which will get another name), since there should be some sort of a path that naturally guides the player to {{ Dome Fuji }} (even if it is very much side-content). This is actually something we can do in parallel to the ULM, since: the nature and character of their existence is independent of the cities · it doesn't actually matter what country established them, though we can realistically keep some of their names · whatever it is that each "town" (i.e., not-yet-established station) is dedicated to, that can be part of the basis of what the Tepenian town is oriented around · because they're towns, and not full-sized cities, they don't really need to be all that particularly developed"*

| | |
|---|---|
| **The idea** | After the 38 cities, take **real Antarctic stations at stable, non-shifting locations** that are **not already a declared city**; each becomes a **town** |
| **Purposes** | (1) the country is essentially fully populated; (2) **DLC** places to meet people and explore story and environment **between** major cities; (3) the WebTV show *Southern Lights* feels fuller; and especially (4) **a natural path from the coast to Ariun Nuur, Kunlun and Dome Fuji** (Hwy 37, the Mountain Cut Throughway: Dome Fuji → Kunlun → Ariun Nuur → Concordia), guiding the player to Dome Fuji even as side-content |
| **Developer's terms** | **Parallel to the ULM** (the towns' character is independent of the cities); **the establishing country does not matter**, though **some real names may be kept**; **what each station is dedicated to may be part of the basis of its town's orientation**; **towns are lightly developed**, not full cities |
| **Status** | 💡 **Idea recorded.** Not started. No inventory, no criteria, no list yet |

### ⚠ Open (flagged, none decided)

1. ✅ **RESOLVED (developer, 2026-10-03): the station-history law is NOT in tension; no exception is needed.** **Developer, verbatim:** *"remember that it is possible for newcoming Tepenians to inherit research notes, records, audio logs, maps, etc etc, and are able to incorporate them into how they develop their city. There are already precedents for this: Belgrano, Neumayer, Kunlun, Vostok, etc"* **This is the inheritance regime already ruled:** `DR-24` (infrastructure outlasts founders), `DR-25` (a station hands down **records**, not a tradition), `DR-26` (newcomers inherit **research, equipment, techniques and results**), `DR-28` D4/D8 (*"inherited records, research and equipment stay admissible as such"*). **So a town may take up what its station was dedicated to the same way a city does: as research, equipment and records it inherited and carried on, never as a continuous "heritage" or tradition, and never as the operator or nation being a reason for the town's founders, identity, culture or ties** (`DR-19`). *Precedents in the specs: Belgrano (recovered maps); Neumayer (the elevated-on-legs design inherited and extended into a city); Kunlun (the deep seed archive and scientific cataloging); Ariun Nuur (the accumulated research archive).* **Wording rule for towns:** *"took up the station's research, equipment and records"*, not *"the research heritage continues"* (`DR-26`).
2. ✅ **RESOLVED (developer, 2026-10-03): hours.** ***"Establishing each town's personality, character, etc, that's something to do during the productive hours. Collecting data that's relevant to those towns can be done any time."*** **So: DATA COLLECTION any hour; TOWN CHARACTER (personality, orientation, culture) only 05:00 to 14:59.**
3. ⏸️ **The census:** *"we'll figure that out later."* Census II's total is fixed and hands-off until all 38 cities finish the ULM (`DR-23`); where town populations come from is **deferred on purpose**.
4. ✅ **RESOLVED (developer, 2026-10-03): what counts as "steady".** ***"Basically, ice that's not moving at a speed to the point where the city itself needs to be moved. Ideally having bedrock at some distance below the ice."*** **Criterion:** the site's ice must move **slowly enough that the settlement never has to be relocated** (Halley's 400 to 700 m a year is the counter-example), **ideally with bedrock some distance below the ice.** *Bare rock sites qualify by definition.*
5. ✅ **RESOLVED (developer, 2026-10-03): scope for the data pass.** ***"For now, don't know. Just collect every usable station location, and we'll figure out the rest as we go."*** **Collect EVERY usable station location (all types and statuses, tagged); decide scale, names and which to keep later.** **Data lives in** `Locations/Towns/`.
6. **Which cities each town hangs off** (the coast-to-Dome-Fuji path, the Weddell and Ross coasts).

---

## `DR-53` · ✅ **MAWSON: AUSTRALIA RESTORED AS A FOUNDER (REVERSES `DR-45`); FOUNDERS ARE KAZAKHSTAN, RUSSIA AND AUSTRALIA, JOINTLY**

**Developer, verbatim (2026-10-04):** *"actually, go ahead and re-add Australia to Mawson, since 1.) they would have a vested interest in reopening/reusing an older location 2.) it would justify the city continuing to be called Mawson, which, itself, would also: 3.) justify the subnet being called Mawson, 4.) further establish Australian culture as a presence in the Mirny subnet"*

*Context of the ruling:* it followed a discussion of the national radio-comms network (`Locations/Towns/Open_Research_Topics.md` §1, `Towns_Data_Pass_Findings_and_Handoff_2026-10-04.md` §9), in which the developer holds that the people running East Antarctica's comms posts would largely be Australian-stock and would carry Australian practice. That discussion is **not** a stated reason in the ruling and grounds nothing here.

| | |
|---|---|
| **Ruling** | Mawson is founded by **Kazakhstan, Russia (the core state) and Australia, jointly.** `DR-45` (Australia removed) is **reversed**; `DR-46` (Kazakhstan and Russia) **stands**. *Read as adding Australia to the `DR-46` pair, not as replacing Russia (`DR-33`'s original pair was Australia and Kazakhstan); confirm if wrong.* |
| **Legal basis (what the Register's Basis cell cites)** | **`DR-19`, geography and access only.** `DR-19` already names Australia → Mawson in the developer's own words (2026-09-30: *"Australia playing a central role in the establishment of the cities of Casey, Davis, and Mawson, since (in geographical terms) Australia is extremely close to those locations and has (comparatively) easy access"*); `DR-33` ruled it with Australia's nearest zone +8 against Mawson's +4, **a gap of 4, a ruled exception** to the "two, maybe three" test |
| **Reason 1 ("vested interest in reopening/reusing an older location")** | Recorded as the developer's reason. ⚠ **It is not, and cannot be written as, the BASIS for the founders:** a real station's operator or history is never a reason for founders, identity, culture or ties (`DR-19`, `DR-24`, `DR-25`). It stays admissible as what `DR-24` already allows: a statement about the physical infrastructure (and `DR-26`'s inherited records and equipment) that a later community took up |
| **Reasons 2 and 3 (the name "Mawson" for the city and the subnet)** | Recorded as the developer's reasons: the name now follows from a founder nation, in-world. ⚠ The real namesake himself stays **flavor only, never data or a tie** (`DR-32`). The subnet was already named Mawson; nothing renamed |
| **Reason 4 (Australian culture in "the Mirny subnet")** | ⚠ **The Register places the city Mawson in the MAWSON subnet, not the Mirny subnet** (Mawson, Temirötkel, Dome Fuji). Australian presence in the Mirny subnet already stands (Casey and Davis as sole founder, Mirny as an exile group; `DR-47`). **What this ruling adds is Australian presence in the Mawson subnet.** *If the developer meant something about the Mirny subnet specifically, say so.* |
| **Australia's share (`FQ-20`)** | Back to **six cities**: Mawson, Mirny (exile group), Casey, Davis, Denison, Zukelli. `DR-45`'s stated reason (*"to ease Australia's share"*) is superseded by this ruling. `FQ-20` stays optional; **default: no further change** |
| **Changed** | `Founding_Register.md` (Mawson row, change log); `FQ-20`; `MASTER_Process_Tracker.md` `R-23`; `DR-45` carries a reversal mark |
| **Not changed (flagged)** | `Specs/Mawson subnet/Mawson.md`'s `Founding population:` line (*"Australian exiles"*) and every file that restated `DR-45`/`DR-46`'s two-nation wording: **spec revisit** to the three-founder row, in-window, no spec edited now. The Mawson subnet still has no colloquial nickname (`DR-47` concerns the Mirny subnet only) |
| **Hours** | Recording a developer's founding ruling is not restricted to 05:00–14:59 (same reasoning as `DR-33`: the developer makes the decision; this is assembly) |

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
| **`DR-20a`** | Who first established Sejong and Juan Carlos | ✅ **RULED 2026-10-03** (`DR-34`, `DR-35`): Sejong **Chile** first; Juan Carlos **Uruguay** first |

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
