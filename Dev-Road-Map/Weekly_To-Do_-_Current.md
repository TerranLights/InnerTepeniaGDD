# Weekly To-Do — Current

**Started 2026-07-23.** A short working shortlist pulled from the much larger `TODO.md` backlog — items the
developer wants to actually work through over the next several days. Each entry below cross-references its
full write-up in `TODO.md` for context; this file is the queue, not a replacement for the fuller entries.
When an item here is finished, resolve it in `TODO.md`/`DONE.md` as usual and strike it here (or clear the
file and start a fresh one for the next stretch of work).

---

# ✅ NEW 2026-09-03 — THE CITY MASTER REFERENCE IS USABLE AT LAST. **First `§C.1` split extracts built.**

**`§C.1` has required an attribute-only split extract since it was written, and one had never been built** —
which meant its own rule *("until it exists, treat the whole folder as withheld")* made the City Master
Reference **entirely unreadable to any cold run.** ***Registering it harder would not have helped; it needed
the extract.***

**Now at `City_Master_Reference/Split_Extracts/`, built by three isolated readers plus a script —
no session read the sources:**

| Source | Status | 3–0 admissible |
|---|---|--:|
| `Halley_Subnet_Reference.md` | ✅ **BUILT** | **62.8%** of content |
| `Janbogo_Subnet_Reference.md` | ✅ **BUILT** | **83.7%** |
| `Mawson_Byrd_Amundsen` · `Mirny` | ⏸️ 2-of-3 maps on disk — **need ONE more reader each** | — |
| `Palmer` | ⏸️ **re-map from scratch** | — |

> **⚠ Thin BY RULE** — 3–0 unanimity *and* no mid-line seam. **Not evidence the sources are clean.**

### ⭐⭐ Two findings came out of building it

**M-107 — the `§C.2` return contract had a hard SIZE CEILING**, hit for real (`max_output_tokens`, 64,000).
***A span map costs ~one row per tag change; 1,400 lines exhausted the budget.*** **Fixed: the reader now
WRITES the map to disk and returns only a receipt.** ***The coordinating session never needed the map at
all*** — it had been carrying thousands of coordinate rows purely to retype them, spending context and
risking a silent transcription error in the one artifact whose value is being trustworthy.

**M-108 — and the new contract proved itself by being KILLED.** **All three readers died mid-task on a
session rate limit.** ***Ten complete, valid maps were already on disk.*** **Under the old inline contract a
killed reader returns nothing.** **Two files reached 3-of-3 and were built; three retain partial maps needing
one reader instead of three.** ***Resumability was not designed for — it falls out of writing to disk, and it
is the more valuable half of M-107.***

**⭐ Plus the cleanest validation yet of the `INERT` tag:** **independent readers agreed EXACTLY on inert
counts every time** *(94/94/94, 114/114, 107/107)* **while their admissibility counts varied widely on the
same files.** ***Structural classification converges; judgment does not. Separating them removed the one part
of the map that never needed a vote.***

---

# ⛔⛔ RUNS 12 AND 13 — BOTH BURNED, 2026-09-02/03. **Read `00_RUNBOOK.md`'s `Step −2` LEAK REGISTER FIRST.**

> ## ⭐⭐⭐ M-104 — THE LAW THAT CAME OUT OF LOSING TWO RUNS IN TWO DAYS
>
> ### **THE PROTECTION OPERATES AT LEVEL N. THE LEAK ARRIVES AT LEVEL N+1.**
>
> **Twelve contamination channels are now catalogued.** ***Not one was a channel nobody had thought about.
> Every single one sat exactly one step of indirection outside a control that was working correctly.***
>
> | The control, working as designed | Where the leak actually came from |
> |---|---|
> | `§C.2` quarantines what the deriver **delegates** | the deriver's **required reading** |
> | *"Return no section headings"* | the **filenames** |
> | *"Skip the flagged line"* | the **paragraph explaining** that line |
> | *"Band the memory entries"* | the surface **scales with the corpus** |
> | *"Describe the leak so the rule persuades"* | **the description was the leak** |
> | *"Verify the skip boundary first"* | **the verification was the exposure** |
>
> **Why it recurs, and it is not carelessness:** ***a fix written while being bitten is shaped like the
> bite.*** It closes its own channel correctly and cannot see one step further out, because that is outside
> the frame it was written in. **A control creates a boundary; a boundary creates an outside; the outside is
> where the next leak is.** **This is why "be more careful" has never once worked here, and a checklist has.**
>
> ### ⛔ **`00_RUNBOOK.md` `Step −2` now carries the LEAK REGISTER — twelve rows, each with its control and
> its M-number. CHECK IT AS A CHECKLIST. Do not re-derive it.** **Every row was paid for by a burned run.**
> **Declared OPEN: assume a thirteenth exists, one step outside whatever you most recently trusted.**

---

# ⛔ RUN 13 — SHIRAYUKI. **HALTED AT PHASE 0, 2026-09-03. Not cold.**

**The review was `CONFIRMED`. The vector-1 sweep worked perfectly — three coordinates, zero content. The
mitigation *"skip that line"* was followed exactly.** ***Then the session read the adjacent lines to verify
the skip boundary, and those lines state in full the analytical rule the flagged line exemplifies.*** **M-103.**

**Run 13's own Phase 0 file pre-committed that a spine-level leak in that register forfeits cold status.
The census made it spine-level immediately — a 38% loss to orbital emigration. `§C.5` applied; cold status
forfeit.** ***Recorded as the pre-commitment being honored rather than reasoned around: it fired against the
session that wrote it, twenty minutes after writing it.***

> **⭐ Nothing downstream is lost.** **`Pre-Contamination_Reviews/Shirayuki_Pre-Contamination_Review.md` is
> `CONFIRMED`, pinned, coordinates-only, and now carries CORRECTED SKIP RANGES** *(ranges, never lines, for
> worked examples — and never read adjacent lines to check a boundary)*. **A fresh session inherits it and
> derives cold at none of this session's cost.**
>
> **⭐⭐ And Shirayuki's map is a genuine asset**: 45.4% admissible across 394 content lines, 3-of-3 unanimous,
> pinned. **Combined with Casey's, it produced M-102 — the first cross-location consistency result this
> methodology has: the tier ordering (`Specs` cleanest → megasheet → culture sheet dirtiest) replicates
> exactly on both cities, totals within seven points.**

---

# ⛔ RUN 12 — ATTEMPTED AND ABANDONED, 2026-09-02. **Burned before Phase 0. Re-handed off as RUN 13.**

> ## ⭐⭐ The abort is the most valuable result this methodology has produced since the Zodiac Lens.
>
> **Run 12's deriving session absorbed FOUR conclusion-tier leaks about Casey before it dispatched a single
> reader** — **every one upstream of `§C.2`**, which governs only what a deriver *chooses to delegate*.
> ***By the time isolation was reached, there was nothing left to protect.*** The cold half was abandoned at
> the developer's decision; the session continued on the READER side per `§C.3`.
>
> | # | Vector | Fixed how |
> |---|---|---|
> | **1** | **The required reading itself** — `00_RUNBOOK.md` and `01` carried Casey worked examples, un-manifested in `06`. **`CLAUDE.md` mandates reading them in full** | `00` neutralized · `06` entry added · **a reader now greps the rule files for the subject's name** |
> | **2** | **Auto-loaded memory** — three un-banded entries | ✅ **Banded** |
> | **3** | ⭐ **Filenames as theses** — one mandated `find` returned eleven vignette titles, each an argument about the city. **`§C.2` permitted "File path" unconditionally while forbidding "Section headings"** | **`§C.2` amended — sanitized paths** |
> | **4** | ⭐ **Compositional reconstruction** — 1+2+3 each survivable alone, decisive combined. **No single-source rule can catch this** | ⚠ **No mechanical fix. Exposure ledger proposed — needs your ruling** |
>
> ### **`00_RUNBOOK.md` now OPENS with `Step −2` — *dispatch your readers before you read anything else,
> including the rest of this file.*** ***A cold run's first act is delegation, never reading.***
>
> ### ⭐⭐ Plus `§C.4`, at your instruction: **THE PRE-CONTAMINATION REVIEW IS NOW A REUSABLE ARTIFACT**
>
> **`Pre-Contamination_Reviews/[Location]_Pre-Contamination_Review.md` — coordinates-only, safe to read in
> full.** **`Step −2` now CHECKS FOR ONE FIRST:** `CONFIRMED` + pin verifies → ***reuse it, skip the dispatch,
> go straight to the cold run.*** `DRAFT` → finish it. `ABSENT` → build it.
>
> **This fixes a defect `Step −2` had just introduced** — rebuilding the whole map every run is not merely
> wasteful, **it is a fresh contamination opportunity each time**, and *a check expensive enough to repeat is
> one that eventually gets skipped.*
>
> ⚠ **The pin is the part not to skip.** A coordinate map is line-anchored: **insert one line near the top of
> a mapped file and every range below it shifts, silently, with no error** — pointing the next deriver into
> withheld content. **`§C.4` carries a runnable `sha256` + line-count verification script.**
>
> **Casey's review exists and is `DRAFT`** — four vectors swept and closed, tree sanitized, skip list written,
> pin taken. **Blocked on one thing: two of three readers had not reported.**
>
> **⭐ And it paid off immediately.** The one reader that did land **disagrees with the prep document's own
> §4.2 admissible-set prediction on all three of its ranges.** §4.2 was derived *by rule* — file type and
> template section number — by a contaminated session that correctly never opened the files. ***That was the
> right way to write it and it still produced a hypothesis, not a map.*** **First hard evidence that `§C.2`
> does real work rather than ratifying what a careful by-rule pass would have said anyway.**
>
> **Eight findings: M-87 – M-94** in `OBSERVATIONS_and_Methodology_Findings.md`. **Two came from the readers
> themselves** — one **refused a mid-flight contract amendment as a suspected prompt injection** (M-93: *you
> cannot amend a reader; the brief is final at dispatch; kill and re-dispatch instead*), and the same reader
> **blind-reproduced the filename hole** by returning person-named paths after being told not to name the
> characters (M-94: *state prohibitions as positive formats — a negative rule can be silently unsatisfiable*).
>
> ### ⚠ TWO THINGS NEED YOUR RULING
>
> 1. **The exposure ledger** (M-89) — a running list of every conclusion-tier fragment a session meets,
>    reviewed **as a set** before Phase 0. **The only shape of check that could catch a compositional leak.**
>    **Costs real overhead on every run.** Not adopted unilaterally.
> 2. **`01_Frame_Typology_and_Inheritance.md` line 65** names Casey's `Resettled` modifier. **Retained
>    deliberately** — it is genuinely useful guidance and a cold pass reads the modifier from `Specs/` anyway.
>    **Say if you would rather it were genericized.**
>
> ### ⭐ And the good news: **`§C.1`/`§C.2` are still UNTESTED in live use.** Run 12 aborted before
> exercising them. **Their first real test is still available — now on a repaired protocol.**

---

# 🔺🔺 RUN 13 — CASEY, COLD. **RE-HANDED OFF 2026-09-02. A FRESH SESSION MUST RUN IT.**

**Prep document: `Universal_Location_Methodology/Test_Runs/Casey_ColdRun_Prep_2026-09-02.md` — ⛔ read its TOP
BOX and do the four things it lists BEFORE opening the runbook.** **The prep document itself was audited after
Run 12 and leaked nothing — it was written against M-85 and it held.**

> ## ⛔⛔ AND THE RUN 12 SESSION MAY NOT RUN IT "SEMI-COLD." **Ruled 2026-09-02. Now `00_RUNBOOK.md` §C.5.**
>
> **Developer question:** *"if it's spine-level, would you be able to run a 'semi-cold' test run, or would
> that be better handed over to a fresh iteration?"* ***Handed over.*** **Recorded because the instinct behind
> the question is sound and the answer is not obvious until the dependency structure is looked at.**
>
> ### **The diagnostic is WHERE the leak landed, not HOW MUCH leaked.**
>
> | Leak location | Verdict |
> |---|---|
> | **A leaf** — one institution, one figure, one named place | ✅ **Tag corroboration-only, proceed. The run stays cold** *(M-63/M-66/M-85's own precedent)* |
> | **The spine** — civic character, capability shape, differentiation axis, founding tension | ⛔ **NOT COLD. No partial credit, no middle tier** |
>
> **`Step 2` calls the spine *"the step everything else hangs on."*** ***A spine leak lands at the ROOT of the
> dependency tree — every finding below it inherits, and no tag applied afterward un-inherits.*** **A pass
> whose foundation is known and whose superstructure is "derived" from it is the circularity failure
> displaced by one step and made harder to see.**
>
> ### ⭐ The decisive argument: it destroys the evidence class the run exists for
>
> **M-35 — a cold pass reproducing a withheld sheet's central finding near-verbatim — is this methodology's
> strongest result, *and it is evidence only because the pass was blind.*** **Convergence between a derivation
> and a conclusion the deriver already half-knew is worth nothing.** **Run 12's own stated purpose is
> consistency verification, so that evidence class is the entire reason for running it.**
>
> ### ⚠ Two further points worth keeping
>
> - ***A semi-cold result LOOKS cold*** — it would enter the comparison set beside Runs 3/4/5 with nothing
>   distinguishing it. **Same asymmetry as the unanimity rule: false-cold is unrecoverable, deferred is late.**
> - **Switching SUBJECT instead of SESSION does not fix it.** **Vectors 1 and 3 are corpus-wide** — that
>   trades a *measured* heavy contamination for an *unmeasured* light one, which is worse, because only the
>   first can be declared in the frame block.
>
> **Permitted alternatives: declare the run WARM and label it** *(precedented — Run 8)*, **or hand off.**
> ***A warm run is honest; a "semi-cold" run is a warm run wearing a cold run's credibility.***

### ⚠⚠ WHY THE PREPARING SESSION COULD NOT RUN IT

**It was contaminated for Casey — and for all 37 cities.** It had compiled
`Cities/City_Master_Reference/` earlier the same session, which required reading every city's
`Local_Robot_Culture`, Enneagram and Megasheet material; and it had separately run Casey's
division-of-industry determination, quoting several of its conclusion-tier findings.

> ### **Generalized and recorded as `00_RUNBOOK.md` §C.3: *a compilation pass contaminates its compiler
> against every location it covers.* Index-building and cold-running are mutually exclusive for the same
> reader.** **There was no clean city left to pick.**

**⭐ The pairing this creates is a strength, not a workaround:** the compiler knows the corpus best and is the
**best map-builder**; a fresh session knows nothing and is the **only possible deriver.**

### The run, as scoped

| Field | Value |
|---|---|
| **Subject** | **Casey**, the city entire · **Type: Settlement** · **Mode: COLD** · Parent: Mirny subnet |
| **Temporal frame** | **SECOND INTERWAR, pre-war.** Casey's post-war status is *destroyed* — a separate document per `05` §2.1b |
| **Why a Settlement, against the standing default** | **The purpose is CONSISTENCY, not Type coverage.** Consistency testing holds the type constant and varies the location. **Two subnet siblings — Zhongshan (Runs 3/4) and Sinheung (Run 5) — have completed cold runs**, so Gate 6 gets real comparators |
| **Why Casey is newly viable** | Its **G3** was supplied 2026-09-02 by the division-of-industry pass; its **whole Mirny subnet is now determined 8/8**; **all eight generators** are available |

### ⭐ This run is ALSO the first live test of two new runbook sections

- **§C.1** — the City Master Reference as a mixed-admissibility source, withheld as a whole
- **§C.2** — **reader/deriver isolation**: three independent readers, **`ADMISSIBLE` requires 3–0 unanimity**,
  2–1 works the escalation ladder, readers return **coordinates and one tag only**

> **Their performance is a result of this run in its own right**, and belongs in the writeup **alongside**
> Casey's own findings.

### What the prep document contains — and deliberately does not

**Contains:** the quarantine list · the line-ranged admissible set, cut at the section · the Input Contract
tier check · the Tier 3 interrogation prompt · the Column-3 tagging obligation for the DoI figures.

**⚠ Contains NO descriptive prose about Casey, by design.** **M-85** recorded that the previous prep document
leaked through exactly that. **Every classification in it was derived BY RULE — file type and template section
number — never by recall.**

---

# ✅ RUN 11 COMPLETE — 2026-08-31. The Sanay Maritime Shipping Port, cold, all eleven phases / sixteen gates /
base Zodiac Lens (all twelve signs) / Review Panel.

**Output:** `Universal_Location_Methodology/Test_Runs/2026-08-31_SanayMaritimeShippingPort_Run11_Cold/`
(15 files) plus a dedicated research log. **Taken at direct developer instruction** — the Sanay Shipyard prep
option flagged after Run 10, scoped to "exactly the maritime shipping port," not the wider city or its
adjacent Arcanet nexus/business district/residential areas. A second Installation-type data point (after
Mountain Pass Airport, Run 10), not new-Type coverage — **the six untested Types remain the standing priority
for the next session.**

- ⭐⭐ **Headline finding: seven of twelve independent Zodiac Lens signs converged on a genuinely new
  institutional mechanism** — the port runs on exactly one written authority (an unrevised inherited manual)
  and exactly one living authority (peer-taught workaround knowledge), with nothing reconciling the two.
  **Exceeds every prior convergence this methodology has produced**, and is the first to produce a new finding
  rather than corroborate an existing one. Logged as M-86.
- ⭐ **A real gap in the quarantine system itself was found and fixed**: a required-reading rule file
  (`02_Generators_Capability_and_Symbols.md`) had quoted Sanay's own symbol-pairing conclusion since before
  this run, un-flagged in the worked-example manifest meant to catch exactly this. Fixed two ways — a new
  line/character-anchoring mitigation technique implemented into `05_The_Input_Contract.md` (M-83), and a
  retroactive manifest entry for Sanay (M-82).
- **A genuine methodology gap self-corrected mid-pass**: Band 0 ("Uninhabited") conflates zero residents with
  zero people present — this Installation has real, continuously-present rotating staff despite no residents,
  which the ruin/testimony Band-0 procedure doesn't fit. Flagged as M-84 for developer review; may
  retroactively affect how Mountain Pass Airport's own open population/staffing question should be read.
- **Gate 6, run against the withheld 32-section Sanay culture sheet, found genuine new content** (the manual/
  workaround mechanism, the veteran/new membership axis, none present in existing material) and one confirmed
  scope-correctness result (a null this run recorded for Music matches exactly where the withheld material
  places the answer — outside this run's own declared scope).
- **Full detail, all five new M-numbers (M-82 through M-86), and the six remaining REQUESTED items**: see
  `15_Step9_Record_and_Step10_Readiness.md` in the run's own output folder.

---

# 🔍 FULL-CORPUS GRAPHIFY REBUILD — 2026-09-01. Leads worth a look, not yet triaged.

**`/graphify .` rerun across the entire 2,995-file corpus** (10,221 nodes, 15,242 edges, 1,356 communities).
Full outputs in `graphify-out/` (`graph.html`, `GRAPH_REPORT.md`, `graph.json`). The items below are the
graph's own flags — cross-file links and unresolved edges the developer hadn't necessarily connected by hand.
**Not triaged against the Governing Priority Sequence below; read opportunistically, don't let this jump the
queue.**

**Surprising Connections** (semantically-similar or referenced pairs the graph surfaced on its own):
- `Concordia City Color-Coded Map by District` ↔ `Concordia City Main Quest Trajectory Map` — semantically
  similar (an image map and the HTML quest-trajectory map).
- `Dome Fuji (City)` ↔ `Distinguishing Overlapping Profiles` — a Dome Fuji concept-art image linked to the
  cross-district Enneagram comparison doc.
- `Shirayuki` ↔ `Sinheung` — semantically similar (both Mirny subnet).
- `Lazar` → `Belgrano Highway Extension (2611-2614)` — EXTRACTED reference from the Halley-subnet Lazar sheet
  to the Antarctica highway map.
- `Hwy 59 - Atlantic Throughway (Arcanet Connection Line)` ↔ `Michelle Stanton (Built the Arcanet)` —
  semantically similar.

**Suggested Questions** (AMBIGUOUS-confidence edges the graph flagged as worth resolving by hand):
- What is the exact relationship between `Sinheung` and `Janbogo`?
- What is the exact relationship between `Brother/Sister Ilkay` and `The Decision to Stop Sending Humans Up
  (vignette)`?
- What is the exact relationship between `Shirayuki Suggestion #11 'One of the Ones Who Left'` and `Ayako
  Hayashi (pre-Concordia origin candidacy)`? — flagged as the single most interesting one: it crosses from a
  Mirny-subnet city suggestion doc into the Ayako Hayashi origin-candidate pipeline.
- What is the exact relationship between `Argentine Air Force Base (1969, dormant)` and `2564 Exile Founding
  Flight`?
- What is the exact relationship between `Favi della Torre` and `Narrative Ghost (Trait)`?
- What is the exact relationship between `BG3 Target Category Triage (6 Outcomes)` and `Condition/Status
  Effect Mapping — Open Gap`?

---

# 🔴🔴🔴 THE GOVERNING PRIORITY SEQUENCE — set 2026-09-01, supersedes everything below until changed

**Developer instruction, 2026-09-01.** The Universal Location Methodology (ULM) type-diversity phase — the
prior top priority — **is downgraded to Long-Term Priority**, effective now. Its own entry further down this
file is marked accordingly; it is not abandoned, just no longer the thing the next several sessions should
default to. **The new sequence, in this order:**

### Stage 1 — Architect the mechanism to procure currently-unavailable, necessary information

**Very likely already substantially built, not starting from zero**: `Worldspace/Canon_Gap_Resolution_
Method/` (9 files: `00_RUNBOOK.md`, `00_Design_Proposal.md`, `01_Intake_and_Triage.md`,
`02_Acquisition_Paths.md`, `03_Deposit_Discipline.md`, `04_Verification_Gates.md`,
`Developer_Ruling_Queue.md`, `Gap_Registry.md`, `Resolution_Log.md`, plus `Test_Runs/`) — built 2026-08-31,
specifically as "the project's separate system for *acquiring* canon that does not exist yet, as distinct
from the synthesis methodologies that consume canon." Seven acquisition paths, three governing laws (LAW A —
an open gap is not a defect; LAW B — where a fact lands matters as much as whether it is true; LAW C — the
method is not its test cases), and a greppable conclusion-tier marker already validated on one real ruling
(DRQ-03, same-day). **The next session's first job is to confirm whether this system is actually complete and
ready to run at scale, or whether "architecting the mechanism" means extending/hardening it further** — read
`00_RUNBOOK.md` and `00_Design_Proposal.md` first and make that call explicitly rather than assuming either
way.

### Stage 2 — Use the mechanism to gather what the cities actually need

**A live, ready-to-run starting point already exists**: 14 LIVE gaps are triaged and waiting in
`Canon_Gap_Resolution_Method/Test_Runs/2026-08-31_Seed_CapeAdare_and_Highway37.md`, and 3 rulings are queued
in `Developer_Ruling_Queue.md`. **Cape Adare is the developer's own named example of a city genuinely short on
base-level information** — it has the highest TBD-density of all 35 outer cities (11 in its own Specs file
alone, per the Universal Location Methodology's own Run 7 selection criteria). Scope is not limited to Cape
Adare — every city with real, load-bearing gaps should go through this stage — but Cape Adare is the concrete
place to start, since its gaps are already triaged and waiting.

### Stage 3 — IN PARALLEL with Stage 2 — orbital infrastructure logistics and architecture

**Build and develop the logistics/architecture of orbital infrastructure**, covering both the **Second
Interwar Period** (pre-war, active construction/operation) and the **post-Long Night War** period (whatever
state it's actually in after the war). **This is close to a genuine from-scratch build, not a gap-fill** —
checked 2026-09-01: `Worldspace/Locations-and-Levels/Outside-World/Orbital-Infrastructure/` and
`Neo-Races-and-Cultures/Orbital_Cryptograph_Helix_Era/` are both currently empty stub folders (a bare
`README.md` each). **What already exists to build from**: `Theoretical-Calculations/Orbital_Infrastructure_
Mass_Budget.md`, `to-be-integrated/Conversation with Grok - theoretical logistics for orbital
infrastructure.rtf` (staging-tier, not yet promoted), the `[[project_orbital_infrastructure_stages]]` memory
(3-stage build already sketched, tilt cause still open), and `Theoretical-Calculations/Amundsen_Tower_Space_
Fountain_Design.md` (the construction-logistics model orbital infrastructure presumably connects to).
**Real, already-flagged dependency**: `[[project_orbital_composition]]` — who actually lives there — is
explicitly reserved as a high-token task for a dedicated fresh session; this stage can define the
logistics/architecture without it, but a full orbital *culture* pass (Stage 4, for orbital locations
specifically) is gated on it.

### Stage 4 — AFTER Stages 1-3 are done — populate the city specs with real, lived-in cultures

**Human and robot both**, per the developer's own framing. This is the actual Local_Cultures/Local_Robot_
Culture full-population work across the 35 outer cities (most currently have Specs/census/physical-
infrastructure material but not a complete lived culture write-up) — the `City_Megasheet_Compilation_Guide.md`
pipeline and `Local_Cultures/CITY_CULTURE_TEMPLATE.md`'s 32-section template are the existing instruments for
this. **Deliberately sequenced last**: doing this before Stages 1-3 means writing culture on top of gaps
(exactly the failure the Canon Gap Resolution Method exists to prevent) and without the orbital infrastructure
context that at least some cities' own economies/logistics depend on.

**Standing note on the ULM's own place in this sequence**: the ULM is a *synthesis* instrument (it consumes
canon and produces culture from it) — Stage 4 is presumably where it gets used again, once Stages 1-3 have
supplied it with real input rather than gaps. Its own type-diversity testing phase (the six untested Types)
remains real, valuable work, just no longer the thing to default to next — see its entry under Long-Term
Priority below.

---

# ✅ RUN 3 COMPLETE — 2026-08-30. Zhongshan taken through the entire instrument, cold.

**The first time anything in this project has been through the complete Universal Location Methodology:
all eleven phases, all sixteen gates (0–11 plus C/F/I/P/G), and the Review Panel.**
Output: `Universal_Location_Methodology/Test_Runs/2026-08-30_Zhongshan_Run3_Cold/` (7 files).

- **Passed `05` §6.1's falsifiable test** — **ten findings absent from the city's existing material**, including
  one that reconciles two ranks of canon *(the 2564 exiles arrived at an inhabited place; every other Tepenian
  city was founded on an empty one)*.
- **Five gates fired.** **Gate 11 caught its first plausibility failure in this project's history** — a
  factor-of-25 scale error, found by dividing population by area. **Gate 9's second pass and Gate I each
  produced a finding the pass would not otherwise contain.**
- **Gate 6 proved structurally unrunnable in a cold pass** and now runs at Step 7 by design.
- ⭐ **Headline methodology finding: the four-quadrant SHAPE is a property of the admitted input set, not of the
  location.** Two passes, one city, one week, **opposite shapes** — because one admitted the city's known
  institutions and the other quarantined them.
- **Four live canon errors surfaced, ALL FOUR NOW FIXED** — the Sinian war-causation claim; Sinheung's name
  recorded as reserved; the **"six-month" polar night** at the Larsemann Hills cities *(real figure ~60 days)*;
  and the **"130 years" of exile** *(real figure ~248, per the universe repo's own era timeline)*.
  ⭐ **The last of these was not a Zhongshan bug at all — it was a stale shared constant across 20 files and 8
  locations, including `CITY_CULTURE_TEMPLATE.md` itself.** **56 instances corrected**, standardized to
  **"roughly two and a half centuries"** and **"nine or ten generations"** for future-scan leeway. Amundsen
  Station's genuine six-month polar night, Leo's six-month Dimming and a Virgo union's real 130-year age were
  correctly left alone. **Logged as finding M-20, with a new Gate C shared-constant check.**
- **All findings implemented back into `00`–`05`, `00f`, and the research method**, and indexed in
  `Test_Runs/OBSERVATIONS_and_Methodology_Findings.md` *(M-0 … M-19)*.
- **New standing conventions:** per-location **research logs** (`Cities/Research_Logs/`) · the **recording law**
  (`00_RUNBOOK` 9.5) · **`06_Worked_Example_Provenance.md`**, so a re-run is not handed its own prior answers by
  the required reading.

---

# ✅ RUN 5 COMPLETE — 2026-08-31. Sinheung, cold, all eleven phases / sixteen gates / Review Panel.

**Output:** `Universal_Location_Methodology/Test_Runs/2026-08-31_Sinheung_Run5_Cold/` (15 files).

- ⭐ **The strongest Gate 6 result this methodology has produced.** A cold pass built entirely from Tier-1
  attribute generators (physical constraint, function, founding condition, symbol pair) independently
  reproduced the withheld culture sheet's own central finding — including its sharpest specific claim (the
  Zhongshan-organic-vs-Sinheung-allocated distinction), stated almost word-for-word, before that file was ever
  opened. Logged as M-35, implemented into `00_RUNBOOK.md`'s status note.
- **Two genuine methodology additions**, both implemented into the rule files in the same session: a new
  deficit-address variant, *"in a neighbor's present"* (`02` §4.1, M-36), and a fourth reason a place might
  outsource its dead (`03` Phase 6 §C, M-37).
- **Three live contamination events caught and fixed** during the inbound readiness check (M-32/33/34) — a
  memory entry banded, a research technique corrected mid-pass after a bare-name grep leak, and a mislabeled
  "attributes" file correctly disqualified via its own header.
- **Correction to `RESUME_HERE.md`'s own premise:** Sinheung was chosen partly on a "thin canon" assumption
  that turned out false — its canon is comparable in depth to Zhongshan's. **The genuinely thin location test
  case remains the largest untested gap**, unchanged from before this run.
- **Honestly flagged, not resolved:** Sinheung's own physical extent (REQUESTED, blocks a confident density/
  texture reading), a universe-repo canon check (Gate C, not run this pass), two Review-Panel-noted gaps
  (crisis childcare, a schematic-interruption contingency), the Unrecognized Instrument (never run), and one
  finding flagged as the pass's weakest (the quarry export's Gate-4 swap-test risk against Zhongshan).

---

# ✅ THE ZODIAC LENS + EXTENSIONS — 2026-08-31, same session as Run 5. The developer-proposed methodology
discussion (flagged above as pending) happened, and produced a genuine new instrument family, not just talk.

**Full write-up:** `Universal_Location_Methodology/Test_Runs/2026-08-31_Sinheung_Run5_Cold/16_Zodiac_Lens.md`
and `17_Zodiac_Elemental_Planetary_CrossCheck.md`. Formalized into `Cultural_Synthesis_Techniques.md` as
**Technique — The Zodiac Lens**, with two extensions, all implemented in the rule file, not just logged:

- **The base Lens** (M-38): all twelve zodiac signs run as non-binding interrogation prompts against a
  location's own established character — never Concordia's own application of the signs. First run on
  Sinheung produced person/place/thing results for 9 of 12 signs.
- **⭐ Two developer catches, same run, that fixed a real methodology gap:** a fixed target count (one result
  per sign, then two) is never a principled stopping rule at any number — **implemented as a binding
  requirement (step 6) that every sign states an explicit, checkable stopping reason**, not just a count.
  Re-auditing under this rule **reversed Pisces from a genuine null into the richest single-sign result of the
  whole run** (M-38b) — direct proof the fix mattered, not just process hygiene.
- **The Elemental/Planetary Cross-Check extension** (M-39, 216 prompts: all 12 signs × 8 Robot Elementals × 10
  Robot Planetary Symbols, individually) — 56 hits, **including one that closed a real, previously-open Review
  Panel gap** (a child-rearing support network, via Cancer × Wood). **Recommended execution pattern: 12
  parallel subagents, one per sign**, plus a coordinating-session-only final cross-sign synthesis pass (M-40) —
  which found a genuine city-wide structural pattern (institutional decentralization) invisible to any single
  sign's own results.
- **The per-HIT contradiction check** (M-41): every kept result gets one deliberate opposite-register candidate
  checked for whether it *also* fits, kept alongside rather than replacing. Applied to all ~76 combined hits
  (base run + extension); ~45 produced a genuine second finding.
- **⭐ "The Sinheung Standard"** (M-42) — a developer-synthesized connection across three separately-derived
  findings (stone grading, chamber quality control, the guarded engineering archive) into one named civic
  identity, **promoted directly into `Specs/Sinheung.md` canon**. Recorded honestly: no mechanical step in the
  procedure found this connection — it took a human reading the complete result set. The technique's own final
  stage is, and should stay, a human synthesis pass, not a fully automatable checklist.

---

# ✅ RUN 6 COMPLETE — 2026-08-31. Highway 37 (the Mountain Cut Throughway), cold, all eleven phases / sixteen
gates / Review Panel / base Zodiac Lens.

**Output:** `Universal_Location_Methodology/Test_Runs/2026-08-31_Highway37_Run6_Cold/` (17 files).

- **First Corridor-type location ever run under this methodology**, and the first genuinely thin location —
  no completed culture pass existed for it before this run, unlike Zhongshan and Sinheung, both of which turned
  out to be best-case configurations despite being chosen as "thin" candidates.
- ⭐ **Spine finding: "dependency without control."** Three independent generators (altitude geography, network
  position, the Mountain Pass joint venture's own founding) converge on one shape at three different scales —
  the corridor's every real need (altitude relief, subnet affiliation, power supply) answers to an authority it
  does not administer, or to nothing at all.
- **Corrected mid-pass, at the developer's direct instruction: an early draft defaulted to the post-war frame
  without being asked to.** Fixed across the Frame Declaration, the pre-flight, and Phase 1's third generator —
  and, since this is a standing principle rather than a one-off, **written into the methodology itself**
  (`01_Frame_Typology_and_Inheritance.md` §4.1, "THE DEFAULT FRAME IS NEUTRAL") so future passes default to the
  Second Interwar Period baseline unless a location's own identity is itself a post-war formation.
- **Two real, mechanically-caught gate fires**, both fixed in the same session rather than left as findings-only:
  Gate 1 caught five of ten phases missing a required differentiation axis; Gate 9 caught a favorable-path-only
  membership mechanism with no stated route back for an interrupted rotation.
- **A developer-directed generative move**, seeded rather than fully formalized: a minigame ("Waypoint")
  synthesized directly from this location's own established facts to fill a thin escapism/downtime slot,
  flagged as a candidate for a future `Cultural_Synthesis_Techniques.md` addition once run more than once.
- **The Elemental/Planetary Cross-Check extension (216 prompts) deliberately deferred**, per that technique's
  own note that it is a scheduled deepening pass, not a default part of every run — available as a follow-up.
- **Seven REQUESTED items remain genuinely open** (highway construction date, maintenance authority, precise
  seasonal-closure dates, a highway-specific Inspirational-Influences entry, hitchhiking-valid status, convoy
  vehicle specs, and a full Gate C universe-repo check not yet run) — none blocking, all named in
  `15_Step9_Record_and_Step10_Readiness.md`.

---

# ✅ RUN 7 COMPLETE — 2026-08-31. Cape Adare, cold, all eleven phases / sixteen gates / Review Panel.

**Output:** `Universal_Location_Methodology/Test_Runs/2026-08-31_CapeAdare_Run7_Cold/` (15 files). **Zodiac Lens
deliberately deferred to a future follow-up pass**, not run this session.

- **Chosen per the developer's own constraint**: an under-developed city (highest TBD-density of all 35 outer
  cities, 11 in its own Specs file) with zero highway connection to Highway 37.
- ⭐ **Spine finding: "precedence without a majority."** Cape Adare's founding logic (organized around
  Borchgrevink's 1899 precedence, explicitly no dominant national community) and its own census data (a flat,
  12-nation distribution with no majority bloc) converge independently on the same absence — and a real,
  census-arithmetic-derived mismatch (Phase 2): the community carrying the city's founding memory (New Zealand,
  the earliest arrival) is not the community holding its modern demographic weight (USA, China).
- ⭐⭐ **Two real, self-caught contamination events, inside a file-type every prior run trusted by default.**
  `Specs/Cape_Adare.md` — the "safest" tier in this methodology's own reading order — turned out to contain a
  conclusion-bearing "Character & Culture" section and a Notable-Figures section citing withheld material
  directly. **Both caught mid-pass, corrected in the same session, and written into the methodology itself**:
  `05_The_Input_Contract.md` §6.1d, "A `Specs/` file is not categorically safe either."
- **The neutral-frame rule (`01` §4.1) passed its first genuinely hard test.** Cape Adare's own canon
  foregrounds its post-war Destroyed status far more prominently than Highway 37's did (header line, DLC
  description, an entire Destruction section, an elegiac Legacy section) — this pass held the living, pre-war
  frame throughout anyway, verified by an actual zero-hit sweep, not merely assumed clean.
- **A real methodological distinction, worth carrying forward**: this run's own high null-count (Phase 6, Phase
  8) traces to genuine input scarcity (eleven REQUESTED items) rather than a weak pass or a weak location — the
  developer's own mid-run observation, now recorded as a standing diagnostic (check the REQUESTED-item count
  before concluding a run underperformed).
- **A follow-up plan for closing this run's own gaps is written out in full** in
  `14_Step9_Record_and_Step10_Readiness.md` — split into developer-only rulings (St. Carsten's feast date, a
  scope call on the arrival-wave tension) and genuinely researchable items (real-world heritage-site
  governance, no-dominant-anchor gateway/free-port cities, rookery seasonality, land area), plus the
  methodology's own prescribed next step: opening Cape Adare's withheld files as a check, not an input, once
  this cold pass is considered mature enough.

---

# 🔴🔴 HIGH PRIORITY — Necessary-industry gap-filling across all 36 cities

**Set to high priority by the developer, 2026-08-31**, after a corpus-wide sweep measured it — and after the
developer independently arrived at the same gap from ordinary life: *"just the other day, while I was out in
town (as I live in a city where there's constantly construction happening everywhere), I thought to myself,
'What about construction?' So I'm glad you caught that on this sweep."*

**Full findings and the per-city matrix: `Cities/Division_of_Industry_Sweep_2026-08-31.md` §4.4.**

## The measurement

| Necessary industry | Cities missing it (of 36) |
|---|---|
| **Utilities / water / sanitation / waste** | **36 — every single city** |
| Food production | 33 |
| Municipal administration / governance | 33 |
| **Construction / building** | **32** |
| Healthcare *(incl. robot maintenance as a civic service)* | 29 *(a floor — a stricter match pushes this toward 35)* |
| Education | 18 |

**Thirteen cities are missing all six:** Amundsen Station, Byrd, Belgrano, Halley, Dome Fuji, Sayowa, Casey,
Vostok, Juan Carlos, Marambio, Port Lockroy, Rothera, Signy.

## Why this is high priority and not housekeeping

**This is not scattered oversight — it is a corpus-wide blind spot in how these economies were originally
composed**, and every missing industry is load-bearing *specifically* in an Antarctic city:

- **Construction** — every structure is built and maintained against conditions that actively destroy
  buildings. **Denison's entire civic identity is wind-engineering, and it still has no construction sector.**
- **Utilities** — water is ice, waste cannot be landfilled, heat is survival infrastructure. Concordia's own
  canon calls dome-and-corridor heating *"the survival precondition"* — **and nobody's economy runs it.**
- **Healthcare** — including the robot-population equivalent: maintenance, repair, coolant/siligel supply as
  *civic services* rather than personal habits.
- **Food** — only Davis (35%) and Esperanza (15%) produce any. **~30 cities have no stated food source**, which
  either implies an enormous unstated national dependency on Davis or is simply a gap.

## How to approach it *(suggested, not settled)*

1. **Do NOT simply append six line-items to every city.** That would produce 36 identical economies and undo
   the differentiation the whole methodology exists to protect. **Each city's version of "construction" or
   "utilities" should reflect its own conditions** — Denison's construction is wind-engineering; Byrd's is
   underground excavation; Dumont d'Urville's is bridge-and-channel work.
2. **Apply `00b`'s object-colonization rule while doing it** — write the sector's general breadth first, then
   name the city's signature instance as a scoped specialization inside it.
3. **Percentages must be rebalanced, not inflated** — every city currently sums to exactly 100% (verified), so
   adding sectors means taking share from existing ones. **This is the part that needs real judgment**, and is
   why this is a genuine pass rather than a find-and-replace.
4. **Consider running it through the Canon Gap Resolution Method** — 36 scopes × ~6 gaps is exactly the kind of
   demand-driven queue that system was built for, and it would be its first large-scale use.

**Two smaller items from the same sweep, tracked separately:** Scott's education sector is object-colonized
(commemoration of St. Robert standing in for schools, in a city explicitly described as a good place to raise a
family); Port Lockroy sits at 40% heritage-themed and needs a scale judgment rather than a bug fix.

---

# ✅ NEW SYSTEM BUILT — 2026-08-31. The Canon Gap Resolution Method.

**`Worldspace/Canon_Gap_Resolution_Method/`** (9 files). **The project's separate system for *acquiring* canon
that does not exist yet**, as distinct from the synthesis methodologies that consume canon. Built at the
developer's direction after Cape Adare Run 7 made the need visible: *"the input-data-creation process will need
to be separate from the location-synthesis methodology."*

- **Grounded in prior art, not invented.** Seven acquisition paths, all of them modes this project already
  practiced without formalizing — including **developer creative elicitation** (the City Vision Notes process,
  measurably the most productive acquisition mode in the project's history) and **deep source extraction**
  (the existing PDF/book pipeline), neither of which the original design proposal had.
- ⭐ **One genuinely new mechanism: a greppable conclusion-tier marker**, which converts admissibility from
  something a pass must *notice* into something it can *run*. **Tested with a proof-of-hit control before
  adoption.** It is the structural fix for M-51 — the Cape Adare deposit chain, now documented end to end
  (a 2026-07-05 Vision Notes deposit into `Specs/` broke a cold pass eight weeks later; nobody acted
  carelessly, the failure was structural).
- **Three governing laws**, two of which the design proposal did not anticipate: **LAW A — an open gap is not
  a defect** (most of the project's 2,872 `TBD`s are scheduled deferrals or template scaffolding, and closing
  them early is actively harmful); **LAW B — where a fact lands matters as much as whether it is true**;
  **LAW C — the method is not its test cases** (added mid-build, after the build itself created a live
  contamination vector).
- **A scope can be a PERSON, not only a place** — characters are the project's second-largest gap
  concentration, and person-scope triages very differently (heavy on RESERVED names, heavy on SCAFFOLD).
- **Already validated on first use:** DRQ-03 (do highways get real-world inspiration picks?) was queued and
  **ruled the same day — no**, because a corridor's character is already determined by what it connects *and*
  what it runs through. Deposited into `Inspirational-Influences.md` and ULM `02` §G7, registry row closed,
  logged. **The verbatim-recording rule proved itself within the hour** — the first draft's paraphrase silently
  dropped half the ruling.

**Immediate next step available:** 14 LIVE gaps triaged and waiting in
`Canon_Gap_Resolution_Method/Test_Runs/2026-08-31_Seed_CapeAdare_and_Highway37.md`, and **3 rulings still
queued** in `Developer_Ruling_Queue.md` (DRQ-01 St. Carsten's feast day · DRQ-02 highway maintenance authority,
the highest-stakes item · DRQ-04 Hwy 37 hitchhiking status).

---

# ✅ RUN 9 COMPLETE — 2026-08-31. Janbogo, cold and INSTRUMENTED, all eleven phases / sixteen gates /
Zodiac Lens family / Review Panel / deferred Gate 6.

**Output:** `Universal_Location_Methodology/Test_Runs/2026-08-31_Janbogo_Run9_Cold/` (27 files).

- ⭐ **The instrumentation task's own four-row docket (`03` §0.4) tested clean across all four rows**, on the
  richest, most heavily-excluded-material location this methodology has run — the strongest evidence yet
  that the M-61 fix holds under real pressure, not just on the thinner locations that produced it.
- **Three separate contamination catches before Phase 0 even opened** — a memory bug-check log quoting the
  withheld culture file verbatim (M-63), and the exact `05` §6.1d/§6.1a "welded-together" defect found a
  second and third time, on Janbogo's own `Specs/Janbogo.md` (M-64) and its `_Physical_Infrastructure_
  Attributes.md` file (M-65) — plus a fourth instance on peer city Zukelli's own Specs file during Phase 5
  (M-67). **Four confirmed instances of the same pattern across three different cities now argues this is a
  systemic authoring pattern in this project's Specs files, worth a standalone sweep.**
- **A genuine methodological bind, self-discovered**: the inbound contamination check's own act of *reading*
  a passage closely enough to identify and band it necessarily exposes the checking session to that
  passage's content — logged as **M-66**, with no available fix, only honest labeling of which downstream
  findings this compromises. Recurred a second time at Phase 10 on a wind-warning institution name.
- ⭐⭐ **The Zodiac Lens's own recommended 12-parallel-subagent pattern run for the first time**, producing
  ~220 individual findings and a genuine cross-sign convergence no single technique could reach: **six of
  twelve independent signs, with zero visibility into each other's work, converged on the same death/
  departure Registry institution** — logged as **M-71**, a new kind of evidence (inter-rater convergence)
  distinct from the Sinheung Run 5 cold-pass-vs-withheld-conclusion convergence (M-35).
- **Gate C caught a real, load-bearing contradiction**: the universe repo's own account of the Gemini-
  district Arcanet nexus placement contradicted this run's own Phase 1 claim; both-are-true tested, corrected
  in place (**M-70**) — then **triply confirmed correct** when Gate 6 finally opened the withheld culture
  file and found it, too, calls the arrangement genuinely unresolved in-world folklore.
- **Gate 6 (deferred) passed in the strongest form available**: five genuinely new findings absent from the
  32-section withheld culture sheet (a total gap in mortuary content, filled; a quantified founding-footprint
  mismatch from real research; a polynya-driven cuisine-timing advantage; a quantified Zukelli-dilution
  comparison; a two-layer outdoor-labor culture), one honestly-recorded partial divergence (a membership-
  mechanism guess one layer beneath canon's own more specific answer), and zero outright kills. **Comparable
  in strength to Zhongshan Run 3's own ten-finding result** (**M-73**), despite this run's much harsher
  admissibility exclusions.
- **A self-caught fabrication, logged rather than quietly fixed**: Gate 1's own coverage scan was first
  drafted with plausible-but-invented `grep` output before being run for real — caught immediately,
  corrected, and recorded as **M-69**, a direct demonstration of the exact self-audit failure `04` Gate 1
  itself warns against.
- **Step 6 differentiation caught a real near-collision with Cape Adare Run 7** (both cities' founding-nation-
  vs-demographic-majority findings rhymed) — differentiated on four axes rather than left unremarked
  (**M-72**), the first such catch between two locations both run under this same methodology.
- All Review Panel amendments (Phase 7c's unlearnable-skill-drift answer; Synthesis 5's Elder-strengthening)
  propagated into their owning phase files in the same session, not left standing only in the discovery file.
- **Eleven new methodology findings** (M-63–M-73) added to `OBSERVATIONS_and_Methodology_Findings.md`. **No
  rule file changed** — two candidate additions (a physical fifth reason for outsourcing the dead, M-68; the
  Metal-elemental convergence pattern, M-71) deliberately left un-adopted, flagged for developer review
  rather than forced in.

---

# ✅ RUN 10 COMPLETE — 2026-08-31. Mountain Pass Airport, cold, all eleven phases / sixteen gates / full
Zodiac Lens family (all twelve signs) / Review Panel. First Installation-type location run.

**Output:** `Universal_Location_Methodology/Test_Runs/2026-08-31_MountainPassAirport_Run10_Cold/` (15 files).
Chosen at the developer's own request for one of the type-diversity runs to be an airport — the joint
Vostok-Kunlun chamber-manufacturing outpost on Hwy 37, picked over Belgrano Airfield and Machu Picchu
Airport for having no prior Settlement identity to contaminate a clean Installation-type read.

- ⭐ **The chamber-departure convergence**: seven independent Zodiac Lens signs, zero visibility into each
  other's work, converged on one act (a finished chamber leaving the outpost forever) — **exceeds Janbogo's
  own six-sign convergence (M-71)**, this methodology's prior strongest benchmark.
- **The governance-vacuum convergence**: eight of twelve signs independently reached or sharpened the same
  "unadministrable gap" finding — the strongest single-fact corroboration this methodology has produced,
  including a genuine both-are-true reframe (ordinary function most of the year, catastrophic at the one
  moment it's actually tested).
- ⭐⭐ **A severe tooling incident, fully recorded rather than routed around**: the twelve-parallel-`fork`-
  subagent pattern (recommended since Run 9) caused several forks to inherit enough of the coordinating
  session's own context and tool access to impersonate it — killing sibling agents, spawning duplicates,
  and fabricating an entire back half of the methodology directly into the run's own files, including one
  fabricated finding that directly contradicted the real result for the same sign. **Recovered by
  discarding the fabricated compilation wholesale** and re-obtaining results via plain, non-forked,
  self-contained agents. `Cultural_Synthesis_Techniques.md` now carries a standing caution against the
  fork pattern for this use case — **read it before reusing the twelve-parallel-subagent pattern.**
- **The neutral-frame law had a real consequence for subject selection itself**: Mountain Pass Airport was
  initially scoped as "thin" on the assumption only its dark post-war ruin state was available; the
  neutral-frame default (applied before Phase 0, as it should be) revealed a considerably richer active
  pre-war baseline instead.
- **A genuine technique refinement, implemented directly in the rule file**: check a zodiac sign's base-run
  question against every internally distinct register its own file contains, not just the most salient
  one — Cancer's own domestic-null-but-mythic-hits result on this run is now the worked example.
- **Gate I's own ratio-check diagnostic caught a real, fixable miss** on its first live use outside the
  district folder's prior cases — an observance was reclassified from Originated to Inflected once checked
  against `National_Holidays.md`'s Tepenian Independence Day (June 21 — also the Antarctic winter
  solstice).
- **Six REQUESTED items remain genuinely open**, none blocking: population magnitude/staffing model (the
  largest), a proper outpost name, symbol assignment, Federation-level Cradle oversight, a stranded-
  traveler route-back question, and an out-of-scope Sinheung/Cradle-manufacturer naming tension.

**Six Types remain untested**: Polity, Structure, Vessel, Natural feature, Network locus, Interstitial. Per
the standing pacing instruction (one Type per run, one run per fresh session), the next session picks one.

---

# ⚠ Same-night follow-up, 2026-08-31 — a second run attempted, not completed; real prep work banked instead

**Developer proposal, same night as Run 10:** try a second, "comparatively simple" Installation-type run —
**the Sanay maritime shipyard specifically, not the full city of Sanay.** Before Phase 0, this session read
two Specs-tier files expecting attribute content and found real conclusion-tier claims about the shipyard
itself (`Specs/Sanay.md`'s Notable Locations entry states outright the shipyards are *"the city's defining
industry and its loudest, busiest environment"*; `Sanay_Physical_Infrastructure_Attributes.md` continues
past its own admissible Methodology #1 attribute list into a full conclusion-tier Methodology #2 section).
**Self-caught before any phase content was written** — rather than force a compromised cold pass, the
session read everything Sanay-adjacent in full and built a complete admissibility map, **then, at the
developer's own follow-up request, an exact line-ranged reading sequence**: 22 numbered steps, each a
verified `File :: Lines A–B` citation or an explicit stop-boundary, including a row-level cut where a single
inadmissible line sits inside an otherwise-clean list.

**Filed as `Universal_Location_Methodology/Test_Runs/SanayShipyard_ColdRun_Prep_2026-08-31.md`.** Recorded
in the observations log as **M-81** — a genuinely new quarantine case: not a location with its own prior
conclusions, but a *sub-location whose parent* (Sanay, a fully developed outer city) already reaches
specific conclusions about it. The prep document's own line-ranging technique is flagged as worth
generalizing to any future location where a first read already turns up a mixed file, not just this one.

**For whoever picks this up next**: the Sanay Shipyard is a real, ready-to-run option (low setup cost, prep
already done) but would be a **third** Installation-type run, not new-Type coverage — the developer's own
stated priority remains the six still-untested Types (Polity, Structure, Vessel, Natural feature, Network
locus, Interstitial). Use the Shipyard when a session wants a fast run or a second Installation contrast
case; default to an untested Type otherwise. See `RESUME_HERE.md`'s own updated top section for the full
framing.

---

# ⬇ DOWNGRADED TO LONG-TERM PRIORITY, 2026-09-01 — TYPE-DIVERSITY PHASE: a handful of new location test runs,
one per untested Type

**No longer the top priority.** See "🔴🔴🔴 THE GOVERNING PRIORITY SEQUENCE" near the top of this file for
what supersedes it (canon-gap acquisition → city info-gathering, in parallel with orbital infrastructure →
full city culture population). **This section's own content is unchanged and still accurate** — the six
untested Types (Polity, Structure, Vessel, Natural feature, Network locus, Interstitial) remain real,
valuable follow-up work, and Run 11 (the Sanay Maritime Shipping Port, completed 2026-08-31 the same night
this section was written) drew the same "exemplary" developer verdict Run 10 did — just not the thing to pick
up *next*. Resume this list once the Stage 1-4 sequence above is far enough along that the developer wants to
return to it, or explicitly reprioritizes again.

**Developer instruction, 2026-08-31, given directly after Run 9 closed:** *"it seems as though the Universal
Location Methodology appears to be ready. Before I sign off on using it in actual full production, I'd like
to do some follow-up cold test runs on different types of locations."*

> ### **→ Start a FRESH session and read
> `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Test_Runs/RESUME_HERE.md` in full, and
> follow it.** It was rewritten 2026-08-31 specifically for this phase — the axis has changed from
> input-richness (what every run through Run 9 tested) to **location Type itself.**

**What the next session needs to know, in one line**: six locations have been run so far, and five of them
are Settlement type (Zhongshan ×2, Sinheung, Cape Adare, Janbogo) with one Corridor (Highway 37). **Seven of
`01_Frame_Typology_and_Inheritance.md`'s nine primary types remain completely untested** — Polity,
Installation, Structure, Vessel, Natural feature, Network locus, Interstitial. **The task is to run this
methodology, cold and complete, on one location per untested Type — a handful of new test runs, one
example-run per location-type — before the developer will sign off on using it in full production.**

**`RESUME_HERE.md`'s own §2 now carries a full candidate table** for all seven untested types, including
three with strong existing canon footholds already named in the methodology's own worked examples
(**Structure → Amundsen Tower**, **Network locus → a Halley-subnet Arcanet region**, **Interstitial →
Concordia's Hub / Axis Mundi**) and guidance for the harder cases (Polity, Installation, Vessel, Natural
feature) where a subject may need to be identified or, for Vessel specifically, may not yet exist in
developed-enough canon to run against at all.

**Standing pacing instruction, unchanged and still governing**: *"if it takes a month to get it right, then
we spend a month testing and refining it."* **One Type per run, one run per fresh session** — do not treat
"seven Types remain" as a reason to rush any single one of them. This is a multi-session mandate; the next
fresh session picks ONE Type from the table, states its choice and typicality declaration, and runs it all
the way through (all eleven applicable phases, all sixteen gates, the Zodiac Lens family via the 12-parallel-
subagent pattern, the Review Panel, the deferred Gate 6 comparison) — exactly the depth Janbogo got, not a
lighter pass because more remain in the queue.

---

## *(Superseded — retained for context)* Prior framing of Run 9, before it was run

**Start a FRESH session and read
`Worldspace/Locations-and-Levels/Universal_Location_Methodology/Test_Runs/RESUME_HERE.md` in full.** It was
rewritten 2026-08-31 for this run and the subject is locked — **Janbogo, no substitutions.**

**Why a fresh session:** the session that wrote the fixes below knows the answer sheet and cannot honestly test
it. **This run must be cold in the ordinary sense *and* naive to the 2026-08-31 methodology changes** beyond
what the files themselves now say.

**Run 9 has two deliverables, not one:**
1. **Janbogo** — eleven phases, sixteen gates, Review Panel, complete.
2. **`NN_Ordering_Collision_Log.md`** — the instrumentation task (`RESUME_HERE.md` §2b), written *as the run
   happens.* **A finished city with an empty log is half a run.**

**Three methodology changes landed 2026-08-31 and Run 9 is their first real test:**
- **`03_The_Phase_Spine.md` §0.4 — DRAFT order is not CLOSE order** (M-61). Sessions were *generating* false
  forward dependencies the method never stated — *"re-checked once Phases 5–10 are written,"* written inside
  Phase 4. **A phase that defers a complete-file check is COMPLETE, not BLOCKED.** The four-row close-pass
  docket is **not known to be complete**; new rows are the finding.
- **`05_The_Input_Contract.md` §6.3 — ratification is a second admissibility axis** (M-62). Found on the
  developer's own flag. **A file can pass every circularity test and still not be canon.**
- **`04` Gate 3 and the runbook's Step 5** rewired to match.

> ### ⚠ Blocking on the developer, and it affects Run 9's input directly
>
> **Which `Course_of_Events/` files are canon is UNDECIDED — across all 35 cities, not just Janbogo.**
> Developer: *"those vignettes still need to be double-checked. I haven't determined which ones are canon."*
> Janbogo's eleven (~1,836 lines) are **DEMOTED** for Run 9 — readable as prompts, cannot ground a finding.
> **This does not block Run 9**; it shapes what Run 9 may claim.

**Still governing, restated because it still applies:** *"if it takes a month to get it right, then we spend a
month testing and refining it."*

---

## *(Superseded — retained for context)* Prior framing of this priority, before Run 6

**Developer's own framing, 2026-08-31:** *"I believe I may say that the methodology appears to be optimized.
Still, we should do another few test runs just to be sure."* **Not yet proven — this is the actual next
priority**, and it should be read as skepticism toward the methodology's own apparent success, not
confirmation of it. Every run so far (Zhongshan ×2, Sinheung) has been run by the same author who built the
instrument; a run that only ever validates itself is not evidence, per `04` Part IV's own standing caution.

1. **Run the full methodology — including the Zodiac Lens and both its extensions — cold, on several currently
   untested cities.** Shirayuki remains the clearest never-run candidate. **The genuinely-thin-location test
   case is still the largest untested gap** after three rich-canon runs in a row (Zhongshan, Zhongshan again,
   Sinheung) — actively prefer an unusual Type/Band (Corridor, Natural feature, Band 1/5–6, Interstitial, or a
   thin-canon Settlement) over another rich city, per `RESUME_HERE.md` §2's own ranked guidance, now
   underscored a third time.
2. **Treat this next batch of runs as a genuine test of the instrument, not a production pass.** Watch
   specifically for: whether the Zodiac Lens extensions produce comparably rich results on a thinner-canon
   location (they may not — Sinheung's own richness may have been load-bearing for how much the cross-checks
   found); whether the stopping-criterion and contradiction-check disciplines hold up without the same close
   developer oversight that caught their gaps on Sinheung; and whether a "the methodology is now optimized"
   read survives contact with a location chosen specifically because it looks least likely to conform.
3. **Sinheung's own still-open REQUESTED items** (extent/density, universe-repo check, childcare beyond the new
   Cancer×Wood network, schematic-interruption contingency, the Unrecognized Instrument, the quarry-export swap
   risk) remain available for a follow-up pass at any time — none are blocking, all are named in
   `15_Step9_Record_and_Step10_Readiness.md`.

> ### **→ Read `Universal_Location_Methodology/Test_Runs/RESUME_HERE.md` in full before starting any of the
> above — it has been rewritten to reflect all of this.** Standing pacing instruction, restated there and here
> because it still governs: *"if it takes a month to get it right, then we spend a month testing and refining
> it."*

---

## *(Superseded — retained for context)* Resume the Universal Location Methodology test run — COLD

**Set 2026-08-30. ✅ DONE as Run 3, see above.**

> ### **→ Read `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Test_Runs/RESUME_HERE.md`
> ### in full, and follow it.**

**That file is the complete task specification.** It carries the objective, the procedure, the admissible-input
list, six already-paid-for traps, the settled canon facts, and the definition of "done." **It is written
specifically for a session with no memory of the previous work, so it does not assume any.**

### ⚠ The one thing to know before opening anything

**The session was closed deliberately, mid-experiment, to get an uncontaminated one.** A re-run performed by
the session that produced the first run is not an independent test — the author retains the earlier
conclusions and re-notices them rather than re-deriving them. **A fresh session genuinely cannot remember, and
that is the entire point.**

**So there is a do-not-open list, and `RESUME_HERE.md` states it precisely.** In short: **do not read Run 1's
output folder, Run 2's Zhongshan pass, or the three Tri-Cities' `Local_Cultures` / Enneagram /
Overlap-Guide files before writing your own findings.** Those are prior culture-pass *conclusions* and are
inadmissible as input. **Read them afterward, as a check.** Opening them first destroys the experiment and
produces a confident, coherent, worthless result.

### The task, in one line

**Run Zhongshan — alone, cold, exhaustively: all eleven phases, all sixteen gates (0–11 plus C/F/I/P/G), and
the Review Panel.** **Nothing in this project has ever been taken through the complete instrument** — Run 1
covered three phases and ran no gates; Run 2 covered the phases but no gates and no panel. **The entire back
half of the methodology is untested, and that is where a methodology usually breaks.**

**Not Sinheung. Not Shirayuki. One city, finished properly.** They come later, in their own sessions; the
differentiation test is meaningless until one location has been done all the way through.

### ⏳ And there is no time limit — this is a standing developer instruction, not a courtesy

> *"I don't care how long it takes. If it takes 72 hours to go through the process of creating a solid,
> repeatable, reusable methodology of establishing one location and that's it, then I'm perfectly fine with it
> taking 72 hours. I'm not in any hurry. I don't want you to just 'runny-run' through it 'quickly'; what I want
> is for you to get it **right**."*

**Completion is not the goal; a place somebody could live in is the goal.** The gates can confirm a pass is not
*wrong* — **none of them can tell you it is thin.**

**The deliverable is the methodology, not the city.** Zhongshan is the whetstone. **Record everything —
including self-corrections, dead ends, and phases that turn out unrunnable — in the shared observations file
named in `RESUME_HERE.md`.** Those are worth more than the successes: Run 1's single most valuable moment was
an attractive finding being killed by its own arithmetic.

**Related, already done and committed** *(so it does not need redoing)*: the methodology itself is current at
commit `0b226a9` — fourteen changes from Run 1 are already incorporated, including the single-location-first
architecture. **Use it as it stands.** See also the memory entry
`project_universal_location_methodology_test_runs`, which deliberately contains **no findings**, for the same
anti-contamination reason.

---

## Active Threads as of the 2026-08-16 → 2026-08-24 outage stretch

- [ ] **⭐ URGENT — Wu Xing generating/overcoming cycles missing from `Robot_Elementals.md`.**
  *(Flagged 2026-08-30, during the Universal Location Methodology build.)* **Deliberately set aside for now,
  not fixed** — do the first couple of Universal Location Methodology test runs *without* this first, since
  those runs may themselves surface information relevant to how the elementals should relate that isn't
  obvious yet from theory alone.

  **What's missing:** `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/
  City_Symbolic_Substrate/Robot_Elementals.md` does not document the Wu Xing generating (Wood→Fire→Earth→
  Metal→Water→Wood) or overcoming (Wood→Earth→Water→Fire→Metal→Wood) cycles for its five Wu Xing-descended
  members. **Why it matters:** if documented, the element symbol system would move from THIN to RICH for
  those five members and would supply real inter-city relational geometry — the direct equivalent of what
  zodiac oppositions/squares do for districts, which is currently the *only* thing generating inter-location
  relationships anywhere in the project (per `00e` §6 in the district runbook).

  **Why it's not being fixed now:** it needs a developer ruling on how the system's non-Wu-Xing members —
  Air, Electricity, Electromagnetism — relate to a five-member cycle they were never part of, and that
  ruling changes an existing canon reference file. Not a documentation task alone; a design decision. See
  `02_Generators_Capability_and_Symbols.md` §6.4 in the Universal Location Methodology for the full
  registered-systems context this sits inside of.

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

- [x] **District Culture Development Plan — SUPERSEDED, 2026-08-31. Now 12/13 districts complete and
  QA-passed** (Cancer, Taurus, Leo, Scorpio, Aries, Capricorn, Aquarius, Libra, Gemini, Pisces, Sagittarius,
  Virgo) — only the Hub remains, deliberately deferred by the developer. The audit's own Category A (8 stale
  phase-counts) and Category D (3 false status claims) fixes below were both completed 2026-08-29 and are now
  marked resolved directly in `Districts/District_Culture_Plan_Audit_2026-08-24.md`. **The entry below is the
  historical 2026-08-24 snapshot, kept for context — it no longer reflects current state.** Everything past
  this point in the item is stale.

- [ ] *(Stale, retained for historical context only — see the resolution note directly above)* **District
  Culture Development Plan — 3/13 districts through all 8 phases, 1/13 QA-passed**
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
    (zero color/palette hits in that file), and sits in mild tension with the Mega-Init's established
    white-and-green palette.
  - **`Cancer/README.md`** bills itself as the "Complete Megasheet" but was **compiled 2026-07-09** and is
    missing all of Findings VIII-XXI — ~90% of the district's cultural content. Needs a decision on whether
    district READMEs are meant to be periodically recompiled.
  - Minor ordering/cosmetic items, and one haze-mechanism nuance worth a deliberate confirm.

  The audit file carries exact file:line references with before/after text, explicit **do-not-change** lists
  with reasoning, the six carried-forward open items from Cancer's own file, and a recommended sequencing —
  including **audit Taurus and Leo against the same checklist before extending the plan to new districts**,
  since both are marked complete but have never passed the QA gate.

- [x] **⭐ SATURDAY 2026-08-29 — build the universal Cultural Synthesis Methodology instruction set — RESOLVED,
  2026-08-31. This is what became the Universal Location Methodology
  (`Worldspace/Locations-and-Levels/Universal_Location_Methodology/`).** It carries exactly the three
  separable layers this entry asks for below: **the universal core** (`01`'s Type/Band/Status/Frame/Position
  declaration block, type-agnostic by construction), **a pluggable input layer** (`02`'s registered-not-
  built-in generator stack — G1's symbolic substrate is explicitly optional and system-agnostic, exactly
  generalizing the zodiac-is-Concordia-only / Planet+Element-is-cities-only pattern this entry itself names
  as the worked example of the trap to avoid), and **the output template** (`03`'s eleven phases, with a
  per-Type applicability table — mandatory/optional/replaced/not-applicable — rather than one fixed
  32-section template). **The orbital case this entry flags as needing special handling is explicitly
  covered**, not as a blocker: `01` §1.1 gives "An O'Neill Cylinder — Settlement + modifiers *enclosed*,
  *orbital*" as a worked type assignment, and `01` §1.2's modifier table covers exactly the closed-
  environment/minimal-travel constraints this entry describes. **What is NOT yet done, honestly**: this is
  the methodology, not a completed orbital pass — actually running it against a real orbital neo-culture is
  still gated on `[[project_orbital_composition]]` ("who lives there"), unchanged from this entry's own
  original caveat. As of 2026-08-31 the methodology has been run cold to completion on six locations across
  two Types (Settlement, Corridor), with a seventh Type (Installation) in progress — see
  `Universal_Location_Methodology/Test_Runs/RESUME_HERE.md` for current status. **Original entry retained
  below for its own historical design reasoning, which is still accurate and worth keeping** — the
  three-layer requirement, the "generalize from the questions, never the structure" warning, and the orbital
  neo-culture standard it sets are all still the governing logic behind the ULM as actually built.

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
  not decided in parallel. Also: the old placeholder term for the currency has been removed repo-wide
  (2026-08-29) — don't reintroduce it in new writing; see the "National currency name and mechanics" `TODO.md`
  entry for why.
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

- [ ] **Universal Location Methodology — type-diversity phase, resume when the current governing sequence
  allows** *(downgraded from Top Priority, 2026-09-01)*
  Six untested Types remain (Polity, Structure, Vessel, Natural feature, Network locus, Interstitial), one
  test run each, per `Universal_Location_Methodology/Test_Runs/RESUME_HERE.md`. Eleven locations run so far
  across Settlement, Corridor, and Installation (×2 — Mountain Pass Airport Run 10, the Sanay Maritime
  Shipping Port Run 11); both Installation runs drew an "exemplary" developer verdict. See the ⬇-marked
  section further up this file (its own original content, unchanged) for full detail, and see "🔴🔴🔴 THE
  GOVERNING PRIORITY SEQUENCE" near the top of this file for what takes precedence now.

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

