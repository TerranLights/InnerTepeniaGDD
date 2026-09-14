# `R-` DOCKET — the city-pass docket registry

> ## ⛔ WHY THIS FILE EXISTS
>
> **The `R-` docket had no registry.** Items were minted inside pass files and cited from other pass files,
> with nothing anywhere recording what an item *was*, whether it was open, or who owned it. Measured
> 2026-09-13: **four items** — `Zhongshan_Opus:R-22`, `:R-23`, `:R-33`, `:R-34` — appeared **exactly once**
> in the entire repository, in the file that created them. Nothing cited them. Nothing tracked them.
>
> ⭐ **The proof case is `Zhongshan_Opus:R-33`.** It read: *"`Sinheung`'s row is wrong in BOTH trackers."*
> It was correct, specific, and **sat unread until the developer independently noticed the symptom two days
> later.** ***The docket found the bug and had no way to deliver it.*** That is a routing failure, not a
> discipline failure — Step 10 did its job perfectly.
>
> **The asymmetry that explains it:** `M-` items have a registry
> (`Test_Runs/OBSERVATIONS_and_Methodology_Findings.md`), which is why `M-157` and `M-215` are cited
> coherently across passes months apart. **`R-` items had none.** Same project, same discipline, opposite
> outcomes — and the only difference was an index.

---

## THE CONVENTION — read before minting or citing an `R-` number

### 1. ⛔ The series is **PER-PASS**, not global.

`R-1` currently means **three different things** — the extent/allocation question in one pass, an abrasive-
particulate finding in another, a distinct blocking item in a third. **A bare `R-n` is local to the pass
whose folder it sits in.**

### 2. ⭐ A cross-pass citation MUST be qualified: `` `Pass:R-n` ``

Write `` `Zhongshan_Opus:R-30` ``, never a bare `` `R-30` ``. **An unqualified cross-pass citation resolves
to the wrong item the moment the citing pass mints that number itself** — silently, with no error.

> ⚠ *Corrected here 2026-09-13: the Davis pass had minted `R-35`…`R-43`, continuing another pass's series,
> and carried three unqualified cross-pass citations. Renumbered to Davis-local `R-1`…`R-9`; the three
> citations qualified. 22 occurrences before, 22 after.*

### 3. A row goes in **the same commit** that mints the item.

The mechanism that already works for the differentiation table. **An item with no row here does not exist.**

### 4. Not every pass uses `R-`.

At least one pass docketed through `M-` numbers and `§C.8c` targets instead. **Both are legitimate; the
registry records whichever was used.**

---

## STATUS VOCABULARY

| | |
|---|---|
| ⛔ **DEVELOPER** | needs a ruling only the developer can give |
| ⛔ **PROPOSED CORRECTION** | a defect in a developer datasheet. ⚠ **Docked, never edited** |
| ⛔ **PROPOSED** | a methodology change, not yet applied |
| ✅ **RESOLVED** | settled, with the resolution recorded |
| ⏸️ **PARKED** | deferred **on purpose** — do not "helpfully" close |
| ⚠ **UNFILLED** | indexed mechanically; description not yet written |

---

# DAVIS — `Mirny_Subnet/Davis` · 12 items

| id | Target | Status | What |
|---|---|---|---|
| **`R-1`** | `Cities/City_Vision_Notes/` — the **9 reconstructed** files | ⏸️ **DEVELOPER** | They are a pass artifact reporting on a conversation, not a developer statement. A **separate** decision from root ratification: even if the root were enumerated, these 9 warrant their own call. |
| **`R-2`** | `Specs/Davis.md` **L135–181** | ✅ **RESOLVED** — Round 3 | A blanket heading-level cut, which `05` §6.1a forbids. Adjudicated line by line, unanimous. **Cost of the original cut: `G3` — a generator — sat inside the refused range, on one line.** ⭐ **And the principle turned on the range that was *cleared*:** `L4`, `L89`, `L117`, `L120`, `L121` carry post-war and cross-corpus material **inside L1–134**. *"The range is a bound on where to look, never a clearance for what is found there."* |
| **`R-3`** | `Specs/Davis.md` **L74** | ⛔ **PROPOSED CORRECTION** | Temperature-range endpoints sit on **two different columns**. Cold `−21` = Avg Low (Aug −20.8) ✅; warm `0` matches no Avg High — it is **December's Mean**, and December is not the warmest month. Under L111's basis the warm end is **+3.2**. Confirmed 3/3. Matters for growing season. |
| **`R-4`** | `05` §7 + `01` §6 — the `Configuration:` field | ⛔ **PROPOSED** | `TYPICAL / EXCEPTIONAL` describes the **authoring configuration of the pass**, not the typicality of the place — but the bare label invites the locational reading, which ONE LOCATION forbids. Rename → **`Pass configuration: DEFAULT / NON-DEFAULT`**. All three readers converged. |
| **`R-5`** | `05` §6.3 rules 5 + 6 — ratification by banner | ⛔ **DEVELOPER — BLOCKING `G1`'s grade** | Does a file's **self-declared** *"official reference framework"* status ratify it **outside an enumerated root**? Rule 6's body demotes *silence* only; its heading says **"BY ROOT, NOT BY BANNER"**; its table reserves extension to the developer. Rule 5 (*never ratify by use*) also bites. **A and B both refused to rule.** |
| **`R-6`** | Frame — which side of the orbital migration | ✅ **RESOLVED by `DR-4`** *(2026-09-13; row corrected 2026-09-14)* | Census I **1,158,314 → Band 5**; Census II **781,596 → Band 4**; both in-frame. Readers converged on **Band 4 on Census II** — ⛔ **the developer ruled the other way: CENSUS I GOVERNS, BAND 5**, *"because that's the maximum size per city that each city needs to accommodate."* **`DR-4` explicitly overrides the unanimous T8 recommendation**, and `01` §2.2's two "MUST"s *(3→4 decomposition, 4→5 distributional analysis)* are **DEFERRED**, not skipped. ⚠ **This row read `BLOCKING Step 0` for a day after the ruling that settled it** — the pass's own `00.1` §2.1 had already recorded it as decided. ***Gate 0's understating direction, inside the docket whose job is to track exactly this*** *(`M-221`)*. |
| **`R-7`** | `Specs/Davis.md` **L85** | ⛔ **DEVELOPER — cannot be resolved in-pass** | Retention stated `~45%`; computed **38.5%** (`28 ÷ 72.8`). The `45` is **L86's millimeter figure reused as a percent**. The mm mass balance is sound, which isolates the error. ⛔ L91's source is a 37-city comparison — **barred in-run by ONE LOCATION** — so the pass cannot adjudicate it. |
| **`R-8`** | `Specs/Davis.md` **L111** | ⛔ **PROPOSED CORRECTION** | The provenance block **names a superseded column set** — none of its four column names (*Avg Temp, Temp Range, Avg Precip, Precip Probability*) match the actual L93 header. Consequence: *"Avg Daylight"* mislabels **mid-month point samples** as a mean. |
| **`R-9`** | `Stepwise_Execution/01_Spine/S01_…md` **L4** | ⛔ **PROPOSED CORRECTION** | Origin pointer says `00_RUNBOOK.md` **L2350–2375**; actual is **L2390–2414** — stale by 40 lines, *despite a note reading "mechanically re-verified 2026-09-07."* Body verified byte-identical. Confirmed 3/3. |
| **`R-10`** | `Stepwise_Execution/` — the **step/gate card set**'s declared origin ranges | ⛔ **PROPOSED CORRECTION** — ⭐ **pointer half now FULLY MEASURED, 2026-09-14** | ⭐ **`R-9` generalizes, but NOT as far as expected — and the measurement NARROWS the defect rather than widening it.** **All 29 cards swept 2026-09-14; probe verified two independent ways before trusting it.** ⛔ **SPINE: 12 of 12 STALE** — ten at **0% overlap** with the section they claim, `S05` at 27%, `S02` at 5%. *(`S02` — Step 0's own card — declares `L2376–2417`; Step 0 is at **`L2416–2479`**, so its claimed range is almost entirely Step −1's text.)* ✅ **GATES: 17 of 17 CORRECT** — every claimed start line matches the real heading exactly (`Gate 0`→`102`, `Gate C`→`294`, `Gate G`→`399`, …). ⭐⭐ **THE MECHANISM, and it explains both halves:** *the Spine cards point at `00_RUNBOOK.md`, which took insertions **above** its Step sections; the Gate cards point at `04_QA_Gates_and_Differentiation.md`, which grew **568 → 922 lines by APPENDING past line 567**, so nothing above them shifted.* ***Drift is caused by where a file grows, not by how much.*** ⛔ **This also refutes the retracted "29 of 29 content-missing" probe in the opposite direction for 17 cards** — *a 100% failure rate was evidence about the checker; the true rate is 41%, and it is structured.* ⚠ **STILL OPEN: the DRIFT question proper** — *do the Spine cards still TEACH what the runbook now says?* **Only the POINTERS have been measured.** ✅ **Scope of any fix is now bounded: re-extract 12 Spine cards; leave all 17 Gate cards alone.** |
| **`R-11`** | `00.0_Pre-Trip_Inspection.md` §C — the **Step 1** `T8` block | ⛔ **PROPOSED CORRECTION** *(found 2026-09-14, while building Step 1's dispatch)* | The block instructs reading `Specs/Davis.md` **"in full."** ⛔ **That contradicts the ratified Step −1 admissibility contract**, which admits **137 of 181 lines** and excludes `L135–142, L144–147, L149–152, L157–175, L180–181` **entirely** (`00.1` §4.3), plus five struck lines inside the bound. ⭐ **Cause is ordinary drift, not carelessness:** the Pre-Trip was generated **2026-09-11**; the contract was finalized **2026-09-13**, *widening* the range from `L1–134 ∪ {143}` to the current spec after `R-2`'s line-by-line adjudication. **The Pre-Trip was never re-synced.** ⚠ **Severity is real:** a reader obeying §C would open struck and excluded material — including `L121`, which the contract rates the worst line in the file. ✅ **Dispatched against the contract's read spec instead; no breach occurred.** ⛔ **THE GENERAL SHAPE — check every other step's `T8` block for the same drift:** *a pass's address book is written BEFORE its input contract exists, so any range it states is a **prediction**, and the contract is the **ruling**.* **Where the two disagree, the contract wins.** |
| **`R-12`** | `00.0_Pre-Trip_Inspection.md` §C — the **Step 2** `T8` block | ⛔ **PROPOSED CORRECTION** *(found 2026-09-14)* | ⭐⭐ **`R-11`'s PREDICTED SHAPE, CONFIRMED ON THE VERY NEXT STEP.** `R-11` closed by saying *"check every other step's `T8` block for the same drift."* **It was checked, and Step 2's block is wrong in a different way — an OFF-BY-ONE in the step→phase mapping.** ⛔ **The block sends Step 2 to the "§D **Phase-2** row-set."** ✅ **The runbook is explicit: Step 2 is *"**Phase 1**, and the whole of `02`"*, and *"Phases **2–10**"* belong to Step 4.** ⚠ **Consequence is material, not cosmetic:** a pass obeying §C would open Phase 2's canon *(No National Stereotypes, Falkland Treaty, Census)* and **miss Phase 1's entirely** — ⛔ *the **Climate READER** (`G2`'s authoritative monthly-mean source) and **`16` Half B** (`G3`'s figures)* — **at the one step the runbook calls "the step everything else hangs on," building a spine on `G2` and `G3`.** ✅ **Dispatched against the Phase 1 row-set; no miss occurred.** ⭐ **THE GENERAL RULE, now twice-evidenced: `Step N ≠ Phase N`. The mapping is Step 0→Phase 0, Step 2→Phase 1, Step 4→Phases 2–10 — and any address book that assumes the identity is wrong from Step 2 onward.** ⚠ **Steps 3 and 5–10 still unchecked against this.** |

**Cross-pass citations carried by this pass:** `Zhongshan_Opus:R-13`, `Zhongshan_Opus:R-14`
*(`Highways.md` staleness)* · `Zhongshan_Opus:R-30` *(`Division_of_Industry/05` §3 density benchmark,
self-flagged unreconciled)*. ⚠ **Cited for the shared instrument they concern, never for that pass's
findings about its own city.**

---

# OTHER PASSES — index only

> ⛔ **Descriptions are deliberately blank.** This registry was built while the Davis pass was mid-run, and
> **the LAW OF ONE LOCATION forbids reading another location's pass findings during a live pass.** The rows
> below were extracted **mechanically — tokens and file paths only.** No line content was read, by the
> script or by its operator.
>
> ⭐ **To fill them in: do it from a session that is NOT running a city pass.** Filling a description
> requires opening the item, and opening the item is the thing the law prohibits mid-pass. **The empty cell
> is the discipline working, not an oversight.**

## `Mirny_Subnet/Shirayuki` · 6 items

| id | Appears in | × | What |
|---|---|---|---|
| `R-1` | `03_Research.md` · `09.5_Log.md` | 10 | ⚠ **UNFILLED** |
| `R-2` | `03_Research.md` · `04_Phase_09_Populations.md` | 4 | ⚠ **UNFILLED** |
| `R-3` | `09.5_Log.md` | 4 | ⚠ **UNFILLED** |
| `R-4` | `09.5_Log.md` | 1 | ⚠ **UNFILLED** |
| `R-5` | `09.5_Log.md` | 3 | ⚠ **UNFILLED** |
| `R-6` | `09.5_Log.md` | 4 | ⚠ **UNFILLED** |

## `Mirny_Subnet/Zhongshan_Opus` · 34 items

| id | Appears in | × | What |
|---|---|---|---|
| `R-1` | `00.1_Step_MINUS-1_Input_Contract.md` · `00_Frame.md` · `01_Inherited.md` · `02_Spine.md` · `04_Phase_10_Catalog.md` | 14 | ⚠ **UNFILLED** |
| `R-2` | `00.1_Step_MINUS-1_Input_Contract.md` · `00_Frame.md` · `01_Inherited.md` · `02_Spine.md` · `04_Phase_10_Catalog.md` | 5 | ⚠ **UNFILLED** |
| `R-3` | `00.1_Step_MINUS-1_Input_Contract.md` · `00_Frame.md` | 2 | ⚠ **UNFILLED** |
| `R-4` | `00.1_Step_MINUS-1_Input_Contract.md` · `00_Frame.md` | 2 | ⚠ **UNFILLED** |
| `R-5` | `00.1_Step_MINUS-1_Input_Contract.md` · `00_Frame.md` · `04_Phase_06_Meaning.md` · `09.5_Log.md` · `10_Readiness_Check.md` | 7 | ⚠ **UNFILLED** |
| `R-6` | `00.1_Step_MINUS-1_Input_Contract.md` · `00_Frame.md` | 2 | ⚠ **UNFILLED** |
| `R-7` | `00.1_Step_MINUS-1_Input_Contract.md` · `00_Frame.md` · `04_Phase_04_Ordinary_Life.md` | 4 | ⚠ **UNFILLED** |
| `R-8` | `00_Frame.md` · `02_Spine.md` | 2 | ⚠ **UNFILLED** |
| `R-9` | `00_Frame.md` | 3 | ⚠ **UNFILLED** |
| `R-10` | `00_Frame.md` · `01_Inherited.md` · `02_Spine.md` | 4 | ⚠ **UNFILLED** |
| `R-11` | `02_Spine.md` · `04_Phase_03_Surface_and_Texture.md` · `04_Phase_07_Order.md` · `04_Phase_08_Making.md` · `04_Phase_09_Populations.md` · `04_Phase_10_Catalog.md` · `06_Differentiation.md` · `07_QA_Gates.md` · `08_Review_Panel.md` · `10_Readiness_Check.md` | 13 | ⚠ **UNFILLED** |
| `R-12` | `04_Phase_07_Order.md` · `04_Phase_08_Making.md` · `04_Phase_09_Populations.md` · `04_Phase_10_Catalog.md` | 4 | ⚠ **UNFILLED** |
| `R-13` | `04_Phase_07_Order.md` · `04_Phase_08_Making.md` · `04_Phase_09_Populations.md` · `04_Phase_10_Catalog.md` · `09_Record.md` · `10_Readiness_Check.md` | 6 | ⚠ **UNFILLED** |
| `R-14` | `04_Phase_07_Order.md` · `04_Phase_08_Making.md` · `04_Phase_09_Populations.md` · `04_Phase_10_Catalog.md` · `09_Record.md` · `10_Readiness_Check.md` | 6 | ⚠ **UNFILLED** |
| `R-15` | `04.9_Step_4_Close-Out_Check.md` · `04_Phase_08_Making.md` · `04_Phase_09_Populations.md` · `04_Phase_10_Catalog.md` · `05_Reconciliation.md` · `09.5_Log.md` | 10 | ⚠ **UNFILLED** |
| `R-16` | `04_Phase_08_Making.md` · `04_Phase_09_Populations.md` · `04_Phase_10_Catalog.md` | 3 | ⚠ **UNFILLED** |
| `R-17` | `04_Phase_08_Making.md` · `04_Phase_09_Populations.md` · `04_Phase_10_Catalog.md` | 3 | ⚠ **UNFILLED** |
| `R-18` | `04_Phase_09_Populations.md` · `04_Phase_10_Catalog.md` | 2 | ⚠ **UNFILLED** |
| `R-19` | `04_Phase_10_Catalog.md` | 2 | ⚠ **UNFILLED** |
| `R-20` | `04_Phase_10_Catalog.md` · `05_Reconciliation.md` | 3 | ⚠ **UNFILLED** |
| `R-21` | `04.9_Step_4_Close-Out_Check.md` · `09.5_Log.md` | 5 | ⚠ **UNFILLED** |
| `R-22` | `05_Reconciliation.md` | 1 | ⚠ **UNFILLED** |
| `R-23` | `05_Reconciliation.md` | 1 | ⚠ **UNFILLED** |
| `R-24` | `04_Phase_02_Composition_and_Arrival.md` · `05_Reconciliation.md` · `06_Differentiation.md` · `07_QA_Gates.md` · `08_Review_Panel.md` · `09.5_Log.md` · `10_Readiness_Check.md` | 12 | ⚠ **UNFILLED** |
| `R-25` | `05_Reconciliation.md` · `06_Differentiation.md` · `07_QA_Gates.md` · `09.5_Log.md` · `09_Record.md` | 11 | ⚠ **UNFILLED** |
| `R-26` | `06_Differentiation.md` | 2 | ⚠ **UNFILLED** |
| `R-27` | `06_Differentiation.md` · `07_QA_Gates.md` | 4 | ⚠ **UNFILLED** |
| `R-28` | `07_QA_Gates.md` · `09.5_Log.md` · `10_Readiness_Check.md` | 5 | ⚠ **UNFILLED** |
| `R-29` | `07_QA_Gates.md` | 2 | ⚠ **UNFILLED** |
| `R-30` | `07_QA_Gates.md` · `08_Review_Panel.md` · `09.5_Log.md` · `09_Record.md` · `10_Readiness_Check.md` | 6 | ⚠ **UNFILLED** |
| `R-31` | `08_Review_Panel.md` · `09.5_Log.md` · `10_Readiness_Check.md` | 6 | ⚠ **UNFILLED** |
| `R-32` | `08_Review_Panel.md` · `09.5_Log.md` · `10_Readiness_Check.md` | 4 | ⚠ **UNFILLED** |
| `R-33` | `10_Readiness_Check.md` | 1 | ⚠ **UNFILLED** |
| `R-34` | `10_Readiness_Check.md` | 1 | ⚠ **UNFILLED** |

## `Mirny_Subnet/Zhongshan_Sonnet` · 11 items

| id | Appears in | × | What |
|---|---|---|---|
| `R-1` | `00.1_Step_MINUS-1_Input_Contract.md` · `00_Frame.md` · `01_Inherited.md` · `02_Spine.md` | 13 | ⚠ **UNFILLED** |
| `R-2` | `00.1_Step_MINUS-1_Input_Contract.md` · `00_Frame.md` · `01_Inherited.md` · `02_Spine.md` | 4 | ⚠ **UNFILLED** |
| `R-3` | `00.1_Step_MINUS-1_Input_Contract.md` · `00_Frame.md` | 2 | ⚠ **UNFILLED** |
| `R-4` | `00.1_Step_MINUS-1_Input_Contract.md` · `00_Frame.md` | 2 | ⚠ **UNFILLED** |
| `R-5` | `00.1_Step_MINUS-1_Input_Contract.md` · `00_Frame.md` | 2 | ⚠ **UNFILLED** |
| `R-6` | `00.1_Step_MINUS-1_Input_Contract.md` · `00_Frame.md` | 2 | ⚠ **UNFILLED** |
| `R-7` | `00.1_Step_MINUS-1_Input_Contract.md` · `00_Frame.md` | 3 | ⚠ **UNFILLED** |
| `R-8` | `00_Frame.md` · `02_Spine.md` | 2 | ⚠ **UNFILLED** |
| `R-9` | `00_Frame.md` | 3 | ⚠ **UNFILLED** |
| `R-10` | `00_Frame.md` · `01_Inherited.md` · `02_Spine.md` | 4 | ⚠ **UNFILLED** |
| `R-11` | `02_Spine.md` · `04_Phase_03_Surface_and_Texture.md` | 3 | ⚠ **UNFILLED** |

---

*Generated 2026-09-13. Index extracted mechanically; Davis rows written by hand.*
