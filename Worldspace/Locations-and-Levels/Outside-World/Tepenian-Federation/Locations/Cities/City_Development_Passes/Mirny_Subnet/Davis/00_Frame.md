# Davis — Step 0 · THE FRAME

**Frame: Second Interwar (2564–2812)** · written 2026-09-14

> ## ✅ VALID — written on verified unanimous consensus
>
> **The reading discipline, stated because it is the thing being claimed.** All **15** required files were read
> **in full, at their contracted ranges**, by **three independent readers** working from an identical brief, each
> emitting a `PROOF:` block. Those blocks were checked **mechanically against the bytes on disk**; the three
> readers then **cross-checked one another** in a third round. ⛔ **Nothing below rests on a single reader's
> claim to have read something.**
>
> | Round | Result |
> |---|---|
> | **1 — blind, independent** | 3 readers × 15 files. Declaration block agreed on **every line but three** |
> | **2 — mechanical ground truth** | **44 of 45 field-sets byte-exact.** One divergence, diagnosed below — a **brief-convention ambiguity, not a reading failure** |
> | **3 — agent-to-agent cross-check** | All three contested fields resolved **3–0**. **Two readers withdrew their own stated grounds while keeping their verdicts; one reversed its verdict outright** |
>
> **Evidence:** the three Round 1 proof files, the Round 2 verification, and the three Round 3 cross-checks.
> **Governing:** `00_RUNBOOK.md` §"Step 0" **L2416–2479** · `01_Frame_Typology_and_Inheritance.md` **582 lines, in
> full** · `Run_Modes_Warm_and_Cold.md` **177 lines, in full** · the five `Disciplines/` files **in full** ·
> `Robot_Physiology_and_Cultural_Practices.md` **in full**.
>
> **Binding rulings folded in:** `DR-4` *(Census I governs; Band 5 machinery deferred)* · `DR-1` *(Element
> meaning reserved)* · `DR-3` *(currency reserved)* · `DR-6` *(a dispatched reader reads a named file at a named
> range)* · `00.1a` *(vision notes struck corpus-wide)*.

---

# 0 · ⚠ TWO INSTRUMENT DEFECTS FOUND BY RUNNING THE INSTRUMENT

**Recorded first, because Round 2 initially returned `⛔ NOT UNANIMOUS — DO NOT WRITE` and that verdict was
wrong.**

| | Defect | Consequence |
|---|---|---|
| **1** | **`triple_read_verify.py`'s `parse_proof()` line-continuation rule has no terminator.** Once it reaches the LAST proof block's `QUOTE:` field, **every subsequent non-blank line in the file is appended to it** — the `COVERAGE` line, the `MANIFEST` line, and the reader's entire Step 0 output | **Three readers' quotes were parsed at 66,055 · 77,090 · 64,691 characters** and all three failed as *"fabricated."* ⛔ **All three quotes were correct and in range.** The file that failed for all three was simply **the last entry in the reading list** |
| **2** | **The `LLAST` convention is unstated.** The brief said *"the LAST ADMISSIBLE line"* and never said whether a **blank** line counts | Range `L2416–2479` ends on a blank line. **Two readers reported the blank; one reported the last line with content.** ⭐ **An honest reader was failed by an unstated convention** — the same class the script's own docstring records being patched for once already |

> ### ⛔ THE RULE THIS YIELDS — **`M-225`**
> ## ***A 100% FAILURE RATE IS EVIDENCE ABOUT THE CHECKER. VERIFY THE INSTRUMENT BEFORE TRUSTING A FAILURE, EXACTLY AS BEFORE TRUSTING A ZERO.***
> **`00_RUNBOOK.md` Step 7 already says *"verify the instrument before trusting any zero"* and warns that
> a plausible number is more dangerous than a zero.** ⭐ **Neither half covers a plausible-looking FAILURE.**
> ***This is the third measured instance in this project*** *(the retracted "29 of 29" card probe; `M-113`'s
> retracted inventory claim; this)*. **Re-verified count: 44 of 45 clean.**
>
> ⛔ **Neither defect was repaired.** *Finding a defect is not authorization to fix it.* The corrected check was
> run **out-of-tree**; `Tools/triple_read_verify.py` is untouched and **still carries both defects**.

---

# 0.1 · THE FRAME DECLARATION

```
## Frame Declaration

**Location:**        Davis — Mirny Arcanet subnet, Tepenian Federation
                     ~68°35′S, 77°58′E · Vestfold Hills, Ingrid Christensen Coast, Prydz Bay

**Type:**            Settlement  +  (NO MODIFIERS ASSIGNED)
                     Primary per `01` §1.1 — people live here as their home, ~1.16M of them.
                     ⭐ ZERO modifiers is a RESULT, not an unfilled slot. All eight checked
                     individually and declined; two were drafted and KILLED (see §0.1a).

**Population band:** 5 — Regional (~1M–50M), approx. 1,158,314
                     RULED by `DR-4`: Census I governs — "the maximum size per city that each
                     city needs to accommodate." NOT re-litigated.
                     ⏸️ `01` §2.2's two MUSTs are DEFERRED BY RULING, NOT MISSED:
                       · threshold 3→4 — mandatory decomposition into sub-locations  → DEFERRED
                       · threshold 4→5 — distributional analysis (spread, modes)     → DEFERRED
                     This pass writes base-level fundamental facts AT a declared Band 5 WITHOUT
                     performing Band 5 distributional analysis. Suspended, not cancelled.
                     ⛔ No finding in this pass may be presented as a distributional result.

**Extent band:**     UNDETERMINED — a BLOCKED CHECK, not an absence. Filed as REQUESTED.
                     `01` §2.1 defines its bands on POPULATION ONLY and supplies no extent scale
                     anywhere; `01` §2 forbids deriving extent from density. The canon extent
                     source is not in this pass's admissible set.
                     ⛔ The DIVERGENCE QUESTION IS THEREFORE OPEN — neither asserted nor denied.
                     If it later resolves as divergent, `01` §2 makes that characterizing and it
                     must be written as a finding then.

**Status:**          LIVING
                     Explicitly NOT `Declining`. `01` §3's 2026-08-31 note governs: the Census I→II
                     fall is MIGRATION TO A DOCUMENTED DESTINATION inside the setting's own future
                     (the orbital tier), not loss. Two independent sources agree — the census's own
                     "nobody was born or died in the transition; they relocated," and the Second
                     Interwar README recording the boundary as pre-war migration to orbit.
                     STATED IN PROSE, as §3 requires: combined 1,158,314 → 781,596 (−376,718);
                     robots 594,715 → 344,173 (−250,542); humans 563,599 → 437,423 (−126,176).

**Temporal frame:**  THE SECOND INTERWAR PERIOD, 2564–2812 (248 years).
                     DECLARED AS THE DEFAULT, EXPLICITLY, per `01` §4.1 rule 4 — an undeclared
                     default is indistinguishable from an accidental one.
                     Prior era: First Interwar (2083–2564), ending at the Falkland Treaty,
                     21 June 2564 — simultaneously this frame's Opening Image. The same event
                     serves as both bookends.
                     Following: the Long Night War, 2812. THIS PASS SITS ENTIRELY BEFORE IT.
                     ACTS: the frame spans BOTH and is MOSTLY ACT 2 (Act 1 ≈ the first 18%).
                     EPISTEMIC HORIZON — the frame's real work: residents know the Arcanet as
                     functioning, Amundsen Tower as completed (~2688) and operating, and orbital
                     migration as a lived event. ⛔ The Long Night War and the Planetary Split
                     Brain have not happened and cannot be imagined by anyone here.
                     POST-WAR FIELDS EXCLUDED BY RULE, THEIR ABSENCE NEVER A GAP:
                     `Status:` · `Current Status / Destruction` · `Connection to Concordia` · `Legacy`.

**Parent:**          The Mirny Arcanet subnet — UNWRITTEN (no ULM pass of its own).
                     Above it: the Tepenian Federation. Six provisional assumptions at §0.6.

**Children:**        NONE — BY DEFERRAL, NOT BY ABSENCE.
                     `01` §2.2's 3→4 threshold says a location this size MUST be decomposed.
                     `DR-4` suspends that. So `01` §5.4 cannot run as written.

**Sibling set:**     EXISTS, and is READ-FORBIDDEN in-run.
                     ONE LOCATION law: the differentiation table is WRITE-ONLY — add Davis's own
                     column, never read another's. Gate 6 moves to Step 7 (`Run_Modes` §4).
                     Substitutes used, per `01` §5.3a — all four declared, with real availability:
                       1. Its own earlier states — AVAILABLE, three-state, all in-frame. PRIMARY.
                       2. Nearest analogous location at another scale — THIN: parent unwritten.
                       3. Real-world comparables (RWBEM) — UNBUILT: no research log. Step 3's job.
                       4. The generator-conflict method (`02` §5) — AVAILABLE, six countable.

**Written:**         ALONE (default). No co-write. `01` §5.3b's permission is narrow, has been
                     over-used once, and the ONE LOCATION law forecloses it here regardless.

**Configuration:**   EXCEPTIONAL — in two specific ways:
                     (a) BAND 5 DECLARED WITH ITS BAND 5 MACHINERY DEFERRED. Every finding this
                         pass produces is produced WITHOUT the decomposition and distribution
                         instruments `01` §2.2 makes mandatory at this band.
                     (b) THE BAND IS RULED BY A SNAPSHOT THE FRAME'S LATER HALF DOES NOT DESCRIBE.
                         `DR-4` fixes Census I on a CAPACITY criterion over Census II's
                         FRAME-DESCRIPTION criterion.
                     FINDINGS THAT DEPEND ON THE EXCEPTIONAL PROPERTY, so a later reader can tell
                     which technique transfers:
                       · anything asserting ONE answer where a distribution is owed;
                       · anything scaled off 1,158,314 rather than off a per-sub-location figure;
                       · anything reading as internally uniform because no sub-locations exist.
                     Recorded, but NOT grounds for the grade:
                       (c) `G1` is PRESENT but LOPSIDED and counts ZERO toward the rule of three.
                       (d) `G3` — what Davis is FOR — rests on ONE line (L143), which a prior pass
                           deleted wholesale without noticing what it cost.

**Provisional assumptions about the parent:**  PA-1 … PA-6, numbered at §0.6.

**Generators available:** G1 lopsided (counts 0) · G2 physical ✅ · G3 function ✅ (one line) ·
                          G4 founding ✅ · G5 network ⚠ (direction yes, volume never stated) ·
                          G6 defining event ⛔ RECORDED NULL — ⚠ see §0.3 · G7 real-world ⚠
                          (designation yes, research unbuilt) · G8 composition ✅ (richest).
                          COUNTABLE: SIX, against a threshold of three.
**Generators selected:**  G2 (physical) · G4 (founding) · G8 (composition) — with G3 (function)
                          carried as a fourth BECAUSE it is the fragile one and must be exercised,
                          not leaned on.
**Reserved decisions this pass must not foreclose:** six, enumerated at §0.5.
```

```
**Run mode:**        WARM
**Other cities:**    CLOSED until Step 6   [warm default]
**Own culture material read at:**  NOT YET READ — opens at Step 5, as a CHECK (Step 0.4 item 6)
**If COLD:** n/a. Declared WARM explicitly, per `§C.5`: "A warm run is honest. A 'semi-cold' run
             is a warm run wearing a cold run's credibility."
```

## 0.1a ⭐ THE THREE CONTESTED FIELDS — how each resolved, because the reasoning is the evidence

**All three came out of Round 1 split 2–1 and closed 3–0 in Round 3. In each case the deciding argument was one
no Round 1 reader had made.**

### 1 · `Resettled` — DECLINED. *(The reader who assigned it reversed itself.)*

**The rule that decided it, read closely:** `01` §1.2 flags `Resettled` as *"Commonly assigned and systematically
under-used — check every location **carrying** it."* ⭐ ***That is an audit instruction for locations that already
have the modifier, not a pull toward assigning it*** — *"commonly assigned"* forecloses under-assignment, so
*"under-used"* must mean its questions go unworked. **With that support removed, NO FORCED FIT's first direction
is unopposed.**

**Three independent grounds, any one sufficient — ⛔ AND THE FIRST HAS SINCE BEEN OVERRULED. See the box below.**
1. ~~**The modifier's obligatory question is *"what did the second population inherit, misread, or fail to notice
   about **the first**?"*** — and the only route to a "first population" here runs through the real station's
   prior occupancy, which **GPS-purposes-only** excludes.~~ ⛔⛔ **STRUCK 2026-09-14 — `DR-7`. THIS GROUND IS NO
   LONGER GOOD LAW.** ***The GPS law does NOT exclude the record a prior lineage left behind***; the test is
   whether the material *"would still be here if the originating nation had left and never returned."*
   ⚠ **The verdict below is unaffected — it survives on grounds 2 and 3, either of which is sufficient — but a
   later reader inheriting this ground would inherit a wrong reason for a right answer.**
2. **`Specs/Davis.md` L127 resolves it in canon:** the documentary inheritance is a **founding-era starting
   point, explicitly superseded** — *"the exiles still built their own practical mastery of the terrain
   independently, over generations of their own."* **A type modifier is a whole-frame property that installs an
   obligatory question into eleven phases; using one for a bounded, canon-superseded Act 1 condition is a scale
   error in the instrument, independent of GPS.**
3. **Nothing is lost by declining.** L127 is seated at **`G4`**, which this pass selects as a primary generator.

> ⛔ **THE FINDING SURVIVES THE MODIFIER'S DEATH, and this file states it so that it cannot quietly vanish:**
> ***a documentary inheritance without a living institution is the sharpest single input this location
> supplies.*** **It is carried at `G4`, and re-seated additionally as a `G2`×`G4` generator conflict.**

### 2 · Extent band — `UNDETERMINED`. *(The reader who declared a value reversed itself.)*

**Declaring `5` is not the conservative act; it is the negative answer to the divergence question.** `01` §2
declares two numbers **so that the second checks the first** — *"when they diverge, the divergence is
characterizing."* **A band declared as "matching" is the first number written twice**, and it pre-answers, in the
negative and permanently, the one question the field exists to ask. **`01` §2's *"they usually match"* is an
observation about two independently determined numbers; used as a derivation rule it makes divergence impossible
by construction and kills the instrument.**

⭐ **And the escape hatch does not reach this case.** It fires when *"a case does not fit a closed set."*
**§2.1's table has no extent column at all — this is a MISSING INSTRUMENT, not a poor fit**, and only the latter
has a sanctioned fallback. ⚠ **`LAW 0-R` is decisive on the rest: *a zero invites suspicion; a plausible number
does not.***

### 3 · Configuration — `EXCEPTIONAL`. *(The reader who wrote `TYPICAL` reversed itself.)*

⭐ **The field's referent is the PASS, not the place** — readable from the current spec without relying on open
docket item `R-4`. `01` §6: the line exists *"so a later reader can tell which technique transfers,"* **and
technique transfers between passes**; §5.3b's only worked instance grades a **co-write**, an authoring fact.
**The baseline is the methodology as written** — `00_RUNBOOK.md` L605–607 names the yardstick in its own
Tri-Cities failure case as findings *"unavailable to a **normal location**."* ⛔ **A self-referential baseline
("all 38 are like this, so this is the new typical") cannot detect a run-wide bias**, and `01` §2.2's MUSTs are
**unamended, merely suspended** — later passes will have the distributional layer.

> ⚠ **The tell, found in cross-check:** the `TYPICAL` cell **already contained a complete EXCEPTIONAL
> declaration** — it named its ruled deviation *"so a later reader can tell which technique transfers"* and then
> ticked the other box. ***Substance right, flag wrong — and the flag is the half `05` §7's pre-flight reads.***

---

# 0.2 · THE DISCIPLINES — what each obliges THIS pass, at Band 5

**Read from `Disciplines/` — the ULM's own copies, not the district originals** *(which are `WITHHELD` and open
at Step 7)*.

| File | The obligation this pass now carries |
|---|---|
| **`00b_General_Population_Discipline.md`** | **A narrow role's version of a category may never stand in for the general population's.** At Band 5 the Band-1 inversion does **not** apply and the rule is in **full force**. ⛔ **The live trap at Davis is occupational:** its function line names *researchers* and *growers*, and both are roles. **"What do people here eat/wear/believe" may not be answered from either.** |
| **`00d_Shadow_Proportion_Discipline.md`** | **Shadow material is written in proportion to its real weight, never as the headline.** ⚠ At Band 5 the shadow is a **distribution**, and this pass may not write distributions — so shadow claims stay **qualitative and explicitly un-sized** until the deferral lifts. |
| **`00f_Review_Panel.md`** | Six Flat Archetypes plus the mandatory **Passer-Through** and **Neighbor**, and **the Lover faculty's question every time.** ⭐ **The `unmet` test in its peer-free form:** *"would satisfying this objection replace something SPECIFIC TO THIS PLACE with something that could be true anywhere?"* **Binds at Step 8; the position-coverage ledger accrues from Phase 2 onward.** |
| **`Cultural_Synthesis_Techniques.md`** | **Never carry one location's answers into another** — binding in BOTH run modes and never relaxed. ⭐ **Technique 13's absence-as-yield applies directly:** no Davis research log exists, which is **maximum yield at Step 3**, not an obstacle. |
| **`Real-World_Basis_Extrapolation_Method.md`** | **`LAW 0-R`: a pick is not exhausted because it has been searched once.** ⛔ **G7's research half is unbuilt** — designation exists, research does not. **Step 3 owes a real log with verbatim search strings, dead ends, and the "changed a finding vs. ornamented one" column.** |
| ⭐⭐ **`Robot_Physiology_and_Cultural_Practices.md`** *(governing, universe-wide)* | **Robots are the majority at Census I — 594,715 of 1,158,314 (51.34%). There is therefore no phase that is not about them.** ⛔ **Robots are human-looking, clothed, gloved, gel-brained, vacuum-capable and NOT altitude-limited — but cold is a real cost.** An environmental hazard is a **preparation problem**, not a hard gate. |

> ### ⛔ AND ONE EXPOSURE, DECLARED RATHER THAN CONCEALED
> **`Robot_Physiology_and_Cultural_Practices.md` is MANDATED reading at Step 0.2 and carries conclusion-tier
> material about OTHER cities** — which warm mode closes until Step 6. ***This is leak-register row 1 — required
> reading as a contamination channel — appearing in WARM-RUN clothing, where it has not previously been
> documented.*** ⭐ **It cannot be avoided by care: the file is mandatory and admissibility is a property of
> content, not of filename.** ⛔ **Consequence accepted and recorded: Davis's own position on the topics that
> material covers is left EXPLICITLY OPEN**, and any later convergence with it is **corroboration at best and
> must be tagged**, never an independent finding.

---

# 0.3 · GATE 0 — **PASS**, and it fired in BOTH directions

## ⛔ Direction A — overclaim

| | Finding |
|---|---|
| ⭐⭐ **THE BIG ONE — `G6`'s null rests on a ground that does not establish it** | `REQ-G6` records *"No in-frame defining event for Davis"* on the single stated ground *"`World_History_Reference.md` = 0 matches."* **The filename is given without a path, and there are TWO files with that name.** The GDD's own is a **7-line, 467-byte redirect stub** — a zero out of seven lines is nearly uninformative. **The universe repo's is 346 lines and returns 1.** ⛔ ***This is `M-117` — "a name is not an address" — landing on the evidence for a RECORDED ABSENCE, the claim class nothing downstream re-checks.*** **The matching line was NOT opened** *(outside contract, conclusion-tier risk)*. **The null is not disproved; it is unsupported by the ground given.** ⇒ **Step 1 must re-ground it against the 346-line file before the null stands.** |
| **Contract §3's `G2` Ground cites its own strikes** | `G2` Ground reads `L60; L70–91; L93–114`; §4.2 strikes **L88–89 FULL**, and `88, 89 ∈ [70,91]`. ⭐ **Identical to the defect §2 already self-corrected once** (the Tier 0 parent cell citing struck L9) — **caught at one site, unpatched at another in the same file.** No content harm: the numeric read spec excludes both. **A reader chasing the stated ground by hand would open them.** *(The other seven Ground citations were cross-checked and are clean.)* |
| **A bare line number addressing a different file** | §3.1's *"(L92, column-anchored)"* drops the filename. **Every other bare `Lnn` in the document means `Specs/Davis.md`, whose L92 is blank.** The intended file is `City_Symbol_Assignments.md`. `M-117`'s milder form. |
| **`M-117` recurring inside the file that records it** | `Real-World_Basis_Extrapolation_Method.md` Step D declares *"PATHS ARE RELATIVE TO `Worldspace/Locations-and-Levels/`"* then names tier-1 HARD CANON as two bare filenames. **Neither resolves under the stated convention and they live in different trees.** ⭐ **Directly upstream of the extent band being undeclarable** — the canon source for the mandated second band cannot be addressed from the instruction that names it. **Resolved address: `Universal_Location_Methodology/Extent_and_Density_Per_City.md`.** |
| **A completion claim that does not reconcile against its own table** | §0 claims **11** contaminated lines and enumerates **10**. §4.2's strike table does contain 11 — it adds **`L88`**, folded invisibly into the `L88–89` row. **The number is right; the enumeration is one short.** |
| **An averaging convention left unnamed** | §8's *"mean annual temperature reproduces to 0.03 °C"* holds **unweighted** (−10.0333) and not **day-weighted** (−10.0732). Not wrong — **under-specified.** A later reader recomputing the other way will believe they found an error. |

## ✅ Direction B — understatement and verified-clean

| | Finding |
|---|---|
| ⭐⭐ **`REQ-G6` is UNDERSTATED as well as under-grounded** | The null is **independently corroborated** — Davis is named **zero times** in the 562-line Second Interwar `Timeline.md`. ⭐ **But the era README supplies the legal substitute the contract missed:** the ~2688 cluster is *"national context, true everywhere — therefore never a differentiator,"* and ***"what differentiates is how hard a given place used that exit."*** **Davis has a measured answer in its own arithmetic, needing no second city.** ⇒ **Re-grade from *"runs thinner"* to *"runs thinner ON THE EVENT AXIS, and the era file routes the substitute question straight into `G8`, this location's richest generator."*** |
| **`R-7` is diagnosed, not merely confirmed** | L84 *falls ~73 mm* · L85 *lands ~28 mm (~45% retention)* · L86 *lost ~45 mm*. `28 ÷ 72.8 = 38.46%`, and `73 − 45 = 28`. ⇒ ***the millimeter figure for what is LOST has been reused as the retention PERCENT.*** The mm mass balance is sound, which isolates the error. ⇒ **recommend re-grading `R-7` from "unresolvable in-pass" to "diagnosed; correction proposed."** |
| **`R-3` is bigger than its grading conveys** | L74's endpoints read off **two different columns**: min Avg-Low **−20.8** (Aug); max Avg-High **+3.2** (Jan); max Mean **+0.9** (Jan). ⭐ **The warm endpoint is +3.2 °C, and two months carry non-negative Means.** **For a city whose only function line is cultivation, how many months sit at or above freezing is a primary input, not a footnote.** |
| **Verified exactly** | Read spec expands to **137 distinct lines**, set-equal to `bound(142) − {4,9,88,89,121}` · all four per-nation columns sum exactly; shares **100.0000%** · retention **67.4770 / 77.6125 / 57.8719**, spread **19.7405 pp** · precipitation sums to exactly **72.8 mm** · band straddle reproduces (1,158,314→5; 781,596→4) · six countable generators reconciles · `Davis_Research_Log.md` verified **ABSENT**. |

> ### ⭐⭐ A BLIND SPOT IN THE ONE-SENTENCE TEST — found twice, and the fix is offered rather than applied
> §4.2 flags **L117** (*"unusual in Tepenia"*) as *"the only strike whose violation is an implicit normal naming
> no city — the one-sentence test cannot see it."* ⭐ **The same shape was found a second time at `L120`
> (*"the largest oasis environment in Tepenia"*) — a corpus superlative naming no city.** **Delete every other
> city's name and both sentences stand, and both are still comparisons.**
>
> ### ✅ THE SECOND TEST THAT CATCHES THEM
> > ## ***"Does this claim require knowing anything about any other place in order to be true?"***
> **`L117` and `L120` both fail it. Davis's own figures — 400 km², −10.0 °C, 67.48% retained — all pass it.**
> ⏸️ **Recommended for the ONE LOCATION law alongside the one-sentence test. NOT applied unilaterally.**

---

# 0.4 · THE MANDATED READ ORDER — `Run_Modes` §2, at the point of use

> ⛔ **In a warm run this order is the whole discipline, because nothing physically prevents opening the last
> item early.** *"This is the single point where a warm run can silently destroy its own value."*

| # | Item | Status |
|--:|---|---|
| **1** | Specs / physical facts | ✅ **READ** — complete for the admissible set (137 lines) |
| **2** | Symbol assignment | ⚠ **READ AT STEP −1, partially admissible.** `Earth / Earth`, column-anchored; the `Why` column **permanently REFUSED**; the **Element half's meaning is `RESERVED` under `DR-1`** |
| **3** | Composition, census, population change across snapshots | ✅ **READ, complete — and the richest.** All arithmetic independently reproduced |
| **4** | Founding and events | ✅ **READ** — `G4` present at L127/L129; **`G6` a null now under challenge** *(§0.3)* |
| **5** | The sibling set's differentiation instrument | ⛔ **EXISTS. NOT READ. MUST NOT BE READ IN-RUN.** Write-only; Davis's own column is added at Step 9 |
| **6** | ⛔ **This location's own culture material** | ⛔ **NOT YET READ. Opens at Step 5, as a CHECK.** `Local_Cultures/Mirny_Subnet/Davis.md` and `Local_Robot_Culture/Mirny_Subnet/Davis.md` — **existence confirmed by filename only; neither opened by any reader** |

✅ **`06_Worked_Example_Provenance.md` checked for this subject BEFORE Step 0.2, as `Run_Modes` §2 requires:
ZERO Davis hits.** ⚠ **The file was absent from the readers' own list; all three correctly recorded it as an
unmet requirement rather than assuming it clean. It was discharged by the pass owner instead.**

---

# 0.5 · RESERVED — the methodology must not decide these

| | Reserved | What would foreclose it |
|---|---|---|
| **1** | **Proper names of people** *(permanent)* | Naming any individual. ⚠ **Second route:** naming a **practice, method, tool or institution** after a person smuggles a name in and is harder to reverse than a character. ⛔ **Third, specific to Davis:** the spec names a real historical person as the city's namesake (L64, L131) — **that is site provenance under `G7`.** Building any in-world figure, honorific, holiday or founding story on it would **invent a person AND violate GPS in the same sentence** |
| **2** | **The demonym** | Any adjectival form, even once, even hedged — a coined demonym is copied forward as canon. ⚠ **Specific pull:** the Robot Physiology file uses demonyms for other places, which establishes the form and makes the gap at Davis feel fillable. **It is not.** Write *"residents of Davis," "people here," "the city's growers"* |
| **3** | **Which DLC covers the Mirny subnet** | Anything presuming a player's arrival, a hub, a quest structure, a gate, a companion sited here. ⭐ **`Repo_Scope.md` sharpens this:** *this repo holds what happened and why; never what a player does about it* |
| **4** | ⚠ **Disposal of the dead** — **highest risk of the six** | Three pressures converge: `01` §1.2's sealed-location pull; the Robot Physiology file's **vivid, recently-ruled ossuary doctrine whose human-side arrival-rate problem is expressly DEFERRED**; and a Davis physical fact that points straight at it. **See the reserved finding below** |
| **5** | **`G1`'s Element meaning** *(`DR-1`)* | Reading meaning off the bare word *"Earth."* ⛔ **Unusually live here:** Davis's strongest physical facts — exposed rock, soil, agriculture, a breadbasket, groundedness — are **precisely what a reader would intuitively call "Earth."** **Any sentence connecting Davis's agriculture or its ground to the Element forecloses a reserved decision** |
| **6** | **Early-Federation currency** *(`DR-3`)* | Any sentence that prices something, names a unit, or describes a wage, harbor fee, tariff or freight rate. ✅ **What Davis VALUES and TRADES is recordable and should be** — it is the input the future currency pass will need |

> ### ⏸️ RESERVED FINDING **A-1** — found, stated, and explicitly NOT adopted
> **Davis holds ~400 km² of exposed ice-free rock, in a nation where burial is impossible because of
> permafrost** — that is the substrate any non-ice interment or ossuary construction would physically require.
> **And L143's 2026-07-16 reassignment moves mining and quarrying AWAY from Davis.**
> **What it would decide:** where a mortuary practice could physically sit at Davis, and on what material it
> would draw. ⛔ **Not adopted.** *Stating the constraint is legal; converting it into a practice is foreclosure.*
> **Handed forward.**

---

# 0.6 · PROVISIONAL ASSUMPTIONS ABOUT THE UNWRITTEN PARENT

**Parent: the Mirny Arcanet subnet. No ULM pass of its own.** `01` §5.2 is explicit that this is **the normal
case, not the exception** — *"a methodology that assumes top-down order will never run."*

| | Assumption | Revision cost · preferred local constraint |
|---|---|---|
| **PA-1** | The subnet supplies Arcanet connectivity as a **working, ambient utility** for the frame | **CHEAP.** ⚠ Era timeline dates national buildout to *"beginning around 2614"* with an **unreconciled** earlier local-hub date ⇒ safe as *"for most of the frame,"* **unsafe as "from 2564."** ✅ **Prefer L127's documentary-inheritance founding**, which needs no subnet at all |
| **PA-2** | Davis is **not** the subnet's administrative hub | **CHEAP.** ⭐ Consequence: `01` §5.1's **Determined** class is **wider** for Davis than for a hub ⇒ ⛔ **local variants of subnet-standardized things must not be invented** |
| **PA-3** | The food obligation runs **OUTWARD**; the subnet does not relieve Davis of its own production | ⚠⚠ **MODERATE-TO-EXPENSIVE — the assumption with the most hanging on it.** `G3`'s tension reading depends on it. ✅ **Mitigation:** both halves of that tension sit in **one ratified line (L143) as Davis's own self-description**, so it survives as a fact about how Davis describes itself. **Tag every finding using the outward direction `PA-3`** |
| **PA-4** | Hwy 110 runs both directions through Davis; Prydz Bay harbor is a working maritime entry | **CHEAP for existence and direction.** ⛔ **UNSAFE FOR MAGNITUDE** — `02` `G5` demands direction **and volume**, and **no throughput figure exists** (`REQ-G5v`). **No finding may be scaled off assumed throughput** |
| **PA-5** | The subnet supplies **no** defining in-frame event | ⚠ **An assumption about an ABSENCE — cheapest to revise, most dangerous to build on.** ⭐ **Deliberately NOT BUILT ON.** `G6` is a recorded null, not evidence nothing happened. If the subnet's pass later supplies an event, **nothing here unwinds** |
| **PA-6** | ⛔ **GUARD, not an inheritance:** nothing about the subnet is admissible as a source of Davis's culture | **The subnet is unwritten, so there is no subnet culture to inherit** — and the failure `01` §5.2 exists to prevent is **inventing one and then "inheriting" it.** ⛔ With the parent unwritten, *"what the parent determines"* returns **UNKNOWN, which is not NOTHING**, and must never be written as if it were |

> ## ✅ `01` §5.2 RULE 4 — SATISFIED BY CONSTRUCTION, NOT BY VIGILANCE
> *"Do not build the location's single strongest finding on a provisional assumption about an unwritten parent."*
>
> **The strongest finding available at Step 0 is the retention-and-inversion reading:** Davis retained **67.48%**
> of its Census I population across the orbital opening — **humans 77.61%, robots 57.87%, a 19.74 pp spread** —
> and **the city enters the transition robot-majority and leaves it human-majority.** ⭐ **That is not a
> population change; it is a change in what kind of place this is.**
> ⭐ ***It rests on census arithmetic and on nothing about Mirny whatsoever.***
>
> **The question it hands the pass needs no second city to ask or to answer:**
> ### ***When leaving became possible, robots left at substantially higher rates than humans. What about this place made that so?***

> ## ⚠ `01` §5.2 RULE 5 — **NOT DONE, and recorded as an outstanding obligation**
> *"Register the assumption where the parent's eventual pass will see it."* **No Mirny-subnet registry exists to
> write into.** ⇒ **An obligation the pass owner must discharge, not a satisfied requirement.** **Gate P
> reconciles against it later**, and the reciprocal duty is real: when Mirny is written, **its pass must
> reconcile against these six and name the Davis findings needing revision.**

---

# 0.7 · HANDED FORWARD

| To | Item |
|---|---|
| ⛔ **Step 1** | **RE-GROUND `G6`.** The null must be re-tested against the universe repo's **346-line** `World_History_Reference.md`, not the GDD's 7-line stub |
| **Step 1** | **`R-7` and `R-3` re-grades** — both diagnosed; corrections proposed, not applied |
| **Step 2** | `G3`'s tension — *residents understand themselves as researchers while the polity above requires calories* — tagged `PA-3` |
| **Step 2** | ⭐ The `G2`×`G4` conflict: **a documentary inheritance without a living institution, against ~400 km² of exposed rock and a −10.0 °C mean** |
| **Step 3** | **Create `Davis_Research_Log.md`** — verified absent; `G7`'s research half is unbuilt. `LAW 0-R` binds |
| **Step 5** | **First opening** of `Local_Cultures/` and `Local_Robot_Culture/`, as a CHECK |
| ⚠ **Developer — PARTLY RULED** | `01` §1.2 — does `Resettled` require a prior resident **POPULATION** or merely prior **OCCUPANCY**? *(Settles most of the 38-city run — nearly all sit on real station sites)* ⭐ **`DR-7` (2026-09-14) removes the GPS OBSTACLE to answering it** — inherited material is admissible — **but does not itself answer the §1.2 question.** ⛔ **Still open, and now open on its own terms rather than as a GPS question** |
| ⏸️ **Developer** | `01` §1.1's *"expect this doubling"* (`Settlement + Installation`) **collides head-on with the GPS law for every Tepenian city founded on a real station.** Twice-evidenced, methodology-level |
| ⏸️ **Developer** | **RWBEM Step D still commands reading `City_Vision_Notes/` as "PRIMARY AND UPSTREAM"** after `00.1a` struck that root corpus-wide. **A pass following the method opens a struck root** |
| ⏸️ **Developer** | The **second one-sentence test** *(§0.3)*, and the two `triple_read_verify.py` defects *(§0)* |

---

# 0.8 · VERDICT

> # ✅ **FRAME DECLARED — PROCEED TO STEP 1**

**Unanimous across three readers in three rounds** — blind in Round 1, mechanically verified in Round 2, and
cross-checked in Round 3, where **every contested field closed 3–0 on an argument no Round 1 reader had made.**

**Strongest reason:** the declaration rests on **ratified ground and reproduced arithmetic** — every census column
sums exactly, retention reproduces to four decimal places, precipitation sums exactly to its stated annual, and
the band straddle reproduces from `01` §2.1's own table. **Six countable generators against a threshold of three.**

**Biggest doubt, carried forward:** ⭐ **`G6`'s null is under challenge.** A generator was recorded ABSENT on a
zero-match search of a **7-line redirect stub**, when a 346-line file of the same name returns a match. ⛔ **The
null may well survive — it is independently corroborated by the era timeline — but it is not currently
established by the ground the contract gives for it.**

**Conditions, both discharged:** `01` §2.2's Band 5 machinery is **deferred by ruling and said to be so**; and
this location's own culture material **remains unopened**, per the one rule that does not relax in either mode.

⛔ **Step 1 — AUDIT WHAT IS INHERITED — opens next.**
