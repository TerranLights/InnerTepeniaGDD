# QA Gates and the Differentiation Instrument

> **⚠ Read `00_RUNBOOK.md` first.** These are its Step 7.

> **⚠ LAW 0 applies here more than anywhere.** **These gates can confirm that a pass is not *wrong*. Not one of
> them can tell you it is not *thin*.** A location can pass every gate below and still be shallow —
> template-complete, internally consistent, correctly scoped, and lifeless. **Passing QA is not the same as
> being finished.**

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

> ### ⚠ Restated again, 2026-08-31, mid-Run-5 — because it needs to be heard again, not just cited
>
> **Developer instruction, verbatim, given directly during Sinheung's cold pass:**
>
> > *"Refining, fine-tuning, and perfecting this methodology is of absolute top-priority and importance to me.
> > If it takes a month to get it right, then we spend a month testing and refining it."*
>
> **What this adds, beyond what LAW 0 already says above:** it is not only that speed is not rewarded — it is
> that **there is no ceiling on how long this is allowed to take, and no session should treat a long runtime as
> a signal that something has gone wrong or that it should wrap up.** A pass, a phase, or a single finding that
> is still open after extensive work is not evidence of failure; stopping early to manufacture a sense of
> completion is the actual failure. **A future session reading this: you do not need to do this "quickly." You
> need to do it *right*.** If the honest, current state of the work is "still going," that is a legitimate and
> expected state, not a problem to paper over.

*(Copied here in full, verbatim, from `00_RUNBOOK.md`, 2026-09-03 — per developer instruction, after a live
session read this law once at the start of a run and still failed to follow it partway through. Placed at the
top of every ULM instruction file rather than cross-referenced, for the reason the law itself already states.)*

---


**The governing test, before the checklist starts:**

> **Is this internally consistent, and characteristically aligned with this specific place — without being
> constrained to repeat what already exists?**

Two failure modes, and the gates guard both: **uncharacteristic** (an element that does not belong to *this kind
of place*) and **over-constrained** (refusing to produce anything not already in canon, yielding a sterile
place that merely re-labels its own material). **The target is the space between: new, but characteristically
inevitable in hindsight.**

---

# Part I — The carried gates

Gates 0–11 are inherited from `00c_Completion_QA_Checklist.md`, generalized from *district* to *location*. Their
substance is unchanged; only the scope-words move. **They were each earned by a specific recorded failure, and
the reasoning behind them is in that file** — this is the operating version, not a replacement for it.

**Gate 0 — Does the completion claim match the file?** Cheapest gate, highest yield, **fails in both
directions.** Reconcile the tracker's claim against the file *and* the file's own open-questions list against
what has actually been resolved elsewhere. **A file's self-reported status is unreliable in both directions:
check the target, never the claim.** And when a phase is added to this methodology, **every location already
marked complete reverts to incomplete for that phase.**

**Gate 1 — Coverage.** Confirm each applicable phase is *answered*, not gestured at.
> **The instrument-verification discipline is the important half, and it is fully general.** A mechanical scan
> is worthless until you have proved it could have found a hit. Recorded defects, every one found by content
> that existed and scored zero: **whole words that miss their own stems** (`funeral` does not match *funerary*);
> **terms never on the list at all** (`mortuary`); **a register the list did not anticipate** (`mourn` misses
> *grief*, *grieving*, *bereavement*); **a character** (an en dash breaking `human-robot`); and **a strip
> boundary that silently captured the wrong section.**
> **So: before drawing any conclusion from an absence, run the scan against a case you know contains a hit. If
> it does not find that one, it has not found anything.** Prefer stems. Normalize dashes. **And paste the raw
> counts into the QA block — do not summarize them**, because an instruction to read carefully does not survive
> an author grading their own work.

**Three outcomes per term, not two, and a fourth that must not be conflated with the third:**
*pass* · *fail* · **covered in substance, absent in term** *(normal, and usually a sign the location has found
its own register)* · **absent and unexplained** *(a genuine hole)*. **The test is one question: does the pass say
why the thing is missing?** **Never insert a word to make the scan pass.**

**Gate 2 — General population.** Per `00b`, **with the Band-1 inversion from `01` §2.3.** Check **every**
finding, including inherited ones. Highest-risk categories: dress, sensory first-impressions, music, visitor
experience, per-population culture.
> **A recorded failure is not a fixed failure.** When a discipline file cites a location as its example, **open
> that location and confirm the text actually changed.** The origin example is the one most likely to still be
> broken, precisely because writing the discipline felt like having dealt with it.

**Gate 3 — Internal contradiction.** Read the **Ordinary Life** phase last and check every other phase against
it. It is the most reliable statement of who actually lives here and what they actually do, which makes it the
best contradiction detector available.

> **⚠ This gate is the CLOSE POINT for Phase 4's contradiction role — `03` §0.4.** Phase 4 *supplies* the
> instrument; **this gate wields it.** Inside its own slot, Phase 4 checks backward against Phases 1–3 only and
> then **closes complete.** It must never be left open "pending Phases 5–10" — that reads as a phase depending
> on later phases, and it is the recorded symptom of the draft-order/close-order collision.

**Gate 4 — Swap test.** For each finding: would it survive essentially unchanged if swapped onto a comparable
location? **Pick the partner most likely to survive the swap, not a convenient comparable** — the gate is only
informative if it could plausibly fail. **Record which finding was weakest under the swap**, not merely that the
set passed. A gate that only ever reports success is not being run honestly.

**Gate 5 — Cross-location consistency.** Export/import coherence against neighbors; **shared-environment
consequences** (anything vented, emitted, sounded or spilled arrives somewhere); and **new categories are
legitimate discoveries** — the check is not *does this already exist, use that instead*, it is only *is the new
thing named and cross-referenced so it enters canon cleanly?*

**Gate 6 — Duplicate institutions.** ⭐ **IN-RUN: within the location ONLY.** *Does this pass name two
institutions that are the same institution twice?* — **that is a fact about this location and it is fully
runnable.** ⏸️ **The against-siblings half is TERMINAL.**
> ### ✅ RULED 2026-09-06 — **the against-siblings half of Gate 6 leaves the per-location pass entirely**
> > ### **"During the course of the ULM/CST/RWBEM, just follow the data wherever it leads for one single location on its own terms, and we'll worry about differentiation later."** *(Developer.)*
>
> ⭐⭐ **Gate 6 was already the closest of the five comparison instruments to correct — it had deferred itself,
> on its own reasoning, six days earlier.** ⛔ **The ruling completes the move: it does not run at Step 7 of a
> per-location pass either. It runs at the TERMINAL differentiation check, on the finished corpus.**
> ⛔ **Do not "check the most recently written sibling first." Do not state a contrast inline.** *(Both
> instructions are revoked; they were the sharpest form of the thing the law forbids.)*
> ✅ **In-run, run all four Part III.4 substitutes and say in the pass that you did.**

> ### ⚠ THE ORIGINAL 2026-08-30 REASONING, kept because it diagnosed the conflict correctly
> **Gate 6 needs the siblings' completed material and the differentiation instrument. In a cold or
> anti-contamination pass that material is precisely what is withheld.** **The anti-convergence gate
> and the circularity rule are in direct conflict, and one of them must lose.**
> ⭐ **2026-09-06 resolves which: the anti-convergence gate loses — and loses to a SCHEDULE, not to a
> judgment.** *It was never wrong; it was early.*
>
> **And an encouraging result worth recording, from a real test case.** When Gate 6 finally ran on one cold
> pass it found two collisions with the location's own existing canon — **and Gate 4's swap test had already
> independently flagged one of them as the pass's weakest finding and demoted it, while that canon was still
> invisible.** **The blind instrument caught what the sighted one later confirmed.** **Gate 4 is therefore
> partial cover for a deferred Gate 6 and should be run deliberately as such** — pick the swap partner most
> likely to expose a shared answer. *(The specific collisions are archived in
> `Test_Runs/Worked_Examples_Archive/`.)*
>
> ### ⚠⚠ Before recording ANY mismatch found at Step 7 as wrong or killed, run the both-are-true test (`02` §5.3)
> **Added 2026-08-31, at the developer's direct instruction after a first draft got this wrong on a real case.**
> A deferred Gate 6 does not only find duplicates — opening withheld material at Step 7 routinely surfaces
> outright **contradictions** between a cold pass's own findings and established canon. **The reflex is to
> declare the cold finding killed. That reflex is the error, not the contradiction.**
>
> **`02` §5.3's both-are-true test was written for generator-vs-generator conflict, but nothing previously said
> it also governs pass-vs-canon conflict at Step 7 — and it should, for exactly the same reason.** *"Do not ask
> which reading is right. Ask what single property would produce both, then check whether the two claims are
> about different objects or at different scales."* A contradiction between a cold pass's claim and an opened
> culture file is very often not a wrongness but a **scale mismatch** — public vs. private, mainstream vs.
> counterculture, an older generation vs. a newer one, a legal/procedural fact vs. a narrative/emotional one.
> **The candidate scales to check, in order, before concluding a kill:**
> 1. Public-facing / mainstream vs. private / minority-community.
> 2. The dominant culture vs. its own named counterculture.
> 3. An earlier generation vs. a later one (heritage drift, memory loss, or accumulation over time).
> 4. A legal/procedural/structural fact vs. a narrative/emotional/mythic one describing the same event.
>
> **A flat kill discards a finding entirely. Applying the test instead looks for the reconciling property —
> very often already written down in the same source that produced the contradiction — before concluding the
> cold pass's claim was simply wrong.** A real worked case, archived in
> `Test_Runs/Worked_Examples_Archive/`, found the property relocated a demographic-diversity
> finding from a public/general scale (where existing canon contradicted it) to a private/generational scale
> (where it was not contradicted, and became a sharper finding than either the original claim or the killed
> version).
>
> **This does not mean every mismatch reconciles.** Some genuinely are wrong at every scale checked — **the
> test is a required check before declaring a kill, not a guarantee against one.** `00f`'s `refereed`
> disposition is the Review Panel's version of the identical instinct and should be read alongside this note.

**Gate 7 — Research accounting.** Every researched pick recorded as **changed a finding · ornamented one ·
deliberately withheld · genuinely omitted.** *Withheld is not unused* — record what it would have given and what
it is being held for. **Expect roughly 70–80% to change findings**; 100% should be suspected of counting
ornament as change, and under half means the picks were chosen badly or abandoned before they paid out.

**Gate 8 — Standout recorded.** Name the single strongest thing the pass produced, and why.

**Gate 9 — Asymmetry.** For every finding describing a **threshold, gate, conversion, verdict, admission or
status change**: *the mechanism runs both ways — did the file write both?* Ask what happens to someone the
mechanism decides **against**, whether that outcome is as durable, and **whether there is any route back.**
**A "no route back" nobody has perceived as a problem is a textbook shadow.**
> **Runs twice: on inherited material before writing, and on the thresholds this pass itself just wrote.** It
> has an extremely high hit rate against inherited material and has barely been tested against material written
> under a methodology that knows about it. **A pass reporting Gate 9 firing only on inherited material has
> probably not run the second pass.**
>
> ### ⭐ First recorded second-pass fire — 2026-08-30
> **The second pass works, and here is the shape it produced on a real test case, because the shape is
> reusable.** A membership threshold was written entirely from the favorable side, in a pass whose author had
> read this gate that morning. **The gate's question — *what happens to someone it decides against, and is
> there a route back?* — had no answer, and finding one produced the pass's second-strongest finding.**
> *(The specific worked case is archived in `Test_Runs/Worked_Examples_Archive/`.)*
>
> > **The transferable pattern: a membership mechanism with no author has no appeal process either**, and
> > **that is a textbook `00d` shadow — unintended, unnoticed, discoverable, and working with everyone acting
> > in good faith.** **Run Gate 9 against every membership, promotion or admission mechanism a pass writes.**
> > The favorable path is the one that gets written; the gate exists because it is also the only one that
> > feels like it needs writing.

**Gate 10 — The Review Panel.** `00f_Review_Panel.md`, **carried unchanged** — it is explicitly fit for this
methodology and only the casting changes. Six Flat Archetypes, plus the **Passer-Through** and **Neighbor**
(both mandatory), plus the **Lover faculty's question every time** — *is this place alive, and could anyone love
it?* Five dispositions: **accepted · noted · rejected · refereed · unmet.**
> **`unmet` should be common**, and it measures **what a location knowingly protects** rather than how hard the
> panel was run. **A low count is not a soft panel** — it usually means the location's problems are absences it
> does not know it has, and *you cannot refuse to surrender something you do not know you hold.*
> **A position that cannot be cast at all is a finding**, and a strong one.

**Gate 11 — Plausibility.** The one direction the others cannot look. **Every other gate checks a relation
between two things already inside the project.** Take the strongest findings and ask, in order: **would a person
actually do this** · **at this cost, priced in this location's physical conditions** · **for this reason** ·
and **whose behavior am I actually describing?**
> **The scale question, which is three of the seven recorded developer catches in one sentence:**
> **What population, over what span, does my source actually describe — and am I asserting it of a larger one?**
> **This is the weakest gate on the list and it should be reported as such.** A self-audit runs it with the same
> faculty that produced the error. **Record what it flagged *and* what it cleared**, so a later external catch
> can be checked against whether this gate looked at it.
>
> ### ⭐ FIRST RECORDED FIRE — 2026-08-30, on a real test case, and it was found by ARITHMETIC
>
> **This gate had never caught anything before this.** It caught two things at once, and the method is worth
> copying exactly, because it required no judgment at all:
>
> **Divide the population by the area. That is the whole technique.**
>
> A cold pass had spent nine phases describing a scattered, low-density settlement, complete with real-world
> comparanda scaled to a small population — and the arithmetic showed a population an order of magnitude denser
> than the pass's own prose implied, comparable to some of the densest real cities on Earth, with comparanda
> that had been asserted of a population far smaller than the one actually being described: the exact form of
> the scale question above. **Both corrections improved the material** — the pass's own texture findings
> survived the correction and came out sharper for it, not weaker. *(The full worked figures — the actual
> density computed, the real-world comparanda used, and exactly what got corrected — are archived in
> `Test_Runs/Worked_Examples_Archive/`.)*
>
> > **The transferable rule: before trusting any texture claim, price it against a density figure.** Population
> > over extent is one division, it needs no interpretation, and **it is the only part of this gate that does
> > not run on the same faculty that produced the error.** **Run it every time, early.**
> >
> > *(Note the redundancy that worked: the same pass's own Phase 0 had already caught the same problem, by
> > declaring a divergence between its population band and its extent band. **Two different instruments, two
> > different stages, same catch.** Declaring both bands — `01` §2 — is the cheaper of the two.)*

---

# Part II — The five new gates

These have no district equivalent because the district set had no type, band, frame or parent variation.

> ⚠ **This heading read "the four new gates" from 2026-08-30 to 2026-09-07 while five gates — `C · F · I · P · G`
> — sat underneath it.** **It is the ROOT of the project's gate miscount:** *12 carried + "4" = the "sixteen"
> that reached `CLAUDE.md`, the `README`, and several pass records.* **The gate SET never changed; only the
> count sentence was ever wrong.** *Verified 2026-09-07: `Gate G` and this heading entered in the SAME commit
> (`e938061`), so no gate was ever added late, and the first completed city pass ran all seventeen. See
> `M-167`.*

## Gate C — Canon check, federated

**Was the four-question canon check (`00_RUNBOOK.md` §E) actually run, against all three tiers?**

- **⚠ Was every search that produced a NEGATIVE result actually run across all three tiers — and can you name
  the search paths?** *(Strengthened 2026-08-30. The old wording asked only whether the universe repo was
  "opened deliberately," which a pass can answer yes to while every one of its actual sweeps stayed local.)*
  > **The measured case.** A city underwent **six** escalating integrity re-check passes, the sixth recorded as
  > *"genuinely clean, the first fully clean pass in this city's re-check history,"* having tried *"fresh grep
  > angles… **repo-wide**."* **Meanwhile the universe repo still listed the city's retired placeholder name as
  > a current city, and pointed at a directory path that had not existed since the rename.**
  >
  > **"Repo-wide" sounds exhaustive and is not.** The universe repo is not in the repo. **Six genuinely
  > rigorous passes each searched a space that structurally could not contain the remaining bugs, and each
  > returned a clean result that was true of the space searched and false of the world.**
  >
  > **So: a grep that never left this repo is not evidence about canon. It is evidence about one directory.**
  > **Name the paths, or the negative result does not count.**
- **Project canon checked against the source, not against the last pass that cited it?**
- **⚠ SHARED CONSTANTS — check at the SOURCE, never at the neighbors.** *(Added 2026-08-30, from a measured
  case: a wrong era length sat in **20 files across 8 locations**, including the city-culture template itself,
  and had been used as a causal premise in all of them.)*
  > **Does this pass use a figure that also appears in other locations' files — a duration, an era length, a
  > generation count, a population, a distance?** **If so, verify it against the timeline or spec that owns it.**
  >
  > **A shared constant is invisible to per-file checking by construction.** Every file agrees with every other
  > file, so any consistency check *between* them passes — and **agreement among siblings then reads as
  > corroboration**, so the error actively defends itself. **Gate 0 checks a file against its own claims;
  > this gate checks a claim against canon; neither one asks whether twenty files are wrong together.**
  >
  > **And when the corrected figure was carrying an argument, rebuild the argument — do not just renumber.**
  > In the measured case a cuisine finding was justified by *"feeding itself through a six-month polar night"*;
  > the real figure was ~60 days, and swapping the number in would have left a weak claim. **The actual
  > constraint — nothing grows on that continent in any season — was both true and stronger.**
- **Any thin-looking canon file checked for being a redirect stub** before concluding the canon is thin?
- **Rank order respected** where sources disagreed, with the contradiction stated rather than silently resolved?
- **Anything binding beyond this location** routed to RESERVED instead of decided here?
- **Anything genuinely new named, defined and cross-referenced** so it enters canon cleanly?

**Record which canon files were actually opened.** A pass that reports "checked canon" without naming files has
not run this gate.

## Gate F — Frame integrity

**Does the pass stay inside its own declared frame?**

Four checks, each against a line of the Phase 0 declaration block:

1. **Type.** Did the pass answer the phases its type actually requires (`03` §0.1), or did it default to the
   Settlement set? **A Corridor written as a thin Settlement is the predictable failure**, and it shows up as a
   Phase 5 that is shorter than Phase 8.
2. **Band.** Is every claim scale-appropriate? **A Band 5 pass reading like a Band 3 pass has committed the
   scale error**, and a Band 1 pass that invents a general population has committed its inverse.
3. **Status.** Does a *declining* location read as declining, or as a healthy one with a sad note attached?
   Does a *ruined* one answer the Band 0 substitutions or the ordinary questions?
4. **Temporal frame.** Did post-frame facts leak in? **This has already happened in this project** — the city
   symbol assignments were first written partly from post-war facts when the subject was pre-war character, and
   had to be re-derived. **Sweep for the adjacent era's proper nouns specifically.**

## Gate I — Inheritance classification

**Is every element correctly classed?** *(`01` §5.1: determined · inflected · originated · aggregated.)*

Two failures, in opposite directions, and both are common:

- **Inventing a local variant of something the parent determines.** A sub-location does not have its own
  climate, currency or calendar. If the pass produced one, it is wrong — not thin, *wrong*.
- **Claiming origination for something inherited.** This is how two siblings independently "invent" the same
  custom: both actually inflected the same parental form and neither noticed.

**The check:** walk the pass's named institutions and customs and assign each a class explicitly. **Anything
classed *originated* goes to Gate 6.** Anything that cannot be classed is a flag — usually it means the parent's
position on it is genuinely unwritten, which belongs in the provisional-assumptions list rather than being
silently decided here.

> ### ⭐ The count is the diagnostic — and this gate correctly predicted its own failure mode, on a real case
> **Added 2026-08-30.** `01` §5.1 warns that **Inflected is the workhorse and is systematically under-used**,
> and that a pass skipping it *"is working harder for a worse result."*
>
> **A real cold pass produced a lopsided ratio — several Originated elements against exactly one Inflected
> one.** **That ratio is the tell, and it is countable — so make it part of the gate rather than a matter of
> judgment.** *(The specific counts and the recurring miss they revealed — a purely local holiday invented
> without ever checking what the location does with a national observance — are archived in
> `Test_Runs/Worked_Examples_Archive/`.)*
>
> **So: count the classes. If Originated outnumbers Inflected by more than about 3:1, stop and re-run the
> `01` §5.1 order of attempts** — *what does the parent determine → what does it supply that this place
> inflects → who arrived carrying one → is the place already doing it somewhere → only then invent.*

## Gate P — Parent reconciliation

**Runs on a parent's pass, not a child's, and it is the reciprocal obligation created by `01` §5.2.**

When a location is written *after* locations it contains:

1. **Collect every provisional assumption its children registered about it.**
2. **For each: does this pass confirm it, contradict it, or leave it open?**
3. **Where it contradicts one, say so explicitly and name the child findings that now need revision.** Do not
   silently overwrite — the child's pass built on that assumption in good faith and its findings are the record
   of what has to change.
4. **Where it leaves one open, say that too**, so the assumption stays visible rather than appearing settled by
   the parent's mere existence.

**A parent pass that does not run this gate has silently invalidated an unknown amount of its children's work.**

## Gate G — Generator honesty

**Did the spine actually get built the way `02` requires?**

- **Were at least three generators run — and were they independent?** Three readings descended from the same
  underlying fact are one generator wearing three hats. *(Function, founding purpose and the parent's need are
  frequently the same fact.)*
- **Was each run to a full profile *before* comparison**, or was the second read written already knowing the
  first?
- **Were the conflicts mined or smoothed?** **A pass whose three generators agreed on everything either got
  lucky or flattened them.** Record the conflicts found and how each resolved.
- **Was any generator's null recorded as a null**, rather than quietly dropped?
- **Was the deficit researched *after* the profile named it**, not before? Researching first produces
  interesting material with nowhere to attach.
- **Was the Unrecognized Instrument run after the profile rather than during it?**

---

# Part III — The differentiation instrument

# ⛔⛔⛔ PART III IS **WRITE-ONLY** DURING A ULM / CST / RWBEM PASS — **RULED 2026-09-06**

> > ### **"In terms of your interpretation of Part III's 'anti-convergence' rule, yes, this is something we'll check for and decide at the very end. During the course of the ULM/CST/RWBEM, just follow the data wherever it leads for one single location on its own terms, and we'll worry about differentiation later."** *(Developer, 2026-09-06.)*

| | During a per-location pass | ⏸️ At the TERMINAL check |
|---|---|---|
| **Adding this location's column** | ✅ **REQUIRED, same commit as the finding** *(Step 9 unchanged)* | — |
| **Reading another location's row** | ⛔⛔ **FORBIDDEN** | ✅ **This is the whole job** |
| **III.2 step 1, "before writing a category, read its row"** | ⛔ **REVOKED in-run** | ✅ **Restored** |
| **III.4 substitutes** | ✅ **The ordinary path, for EVERY location** | — |

> ### ⭐ WHY THE TABLE STILL GETS FILLED — **it is the terminal check's only input**
> ***A write-only table is not a dead table; it is a table under construction.*** **`04` Part III already
> half-said this:** *"the table is FILLED DURING synthesis… it contributes nothing to the first city and
> everything to the thirty-seventh."* ⭐ **The ruling adopts that sentence literally and drops the half that
> contradicted it.** ⛔ **A pass that reads a neighbor's row writes AROUND that neighbor — and
> writing-around-a-neighbor is still a neighbor-shaped decision, which is convergence arriving by the door
> marked anti-convergence.**

> **⚠ And this Part was ALREADY peer-required — an enhancement, not the core.** Per `00_RUNBOOK.md`, the
> methodology's unit is **one location**, and **most passes will have no sibling set at all.** A pass without
> one is not failing this Part; it is running **III.4**, which is the ordinary path. **Do not treat a missing
> differentiation table as a missing gate.** ⭐ **As of the ruling, EVERY pass runs III.4** — the peer-free
> path is no longer the majority case, it is the only case.

> ### ⚠ SCOPE — **`ULM / CST / RWBEM` only. The district instrument is untouched.**
> **`Cross_District_Differentiation_Table.md` and the district runbook keep read-before-write**, on a
> 13-district corpus that is already complete. ⛔ **Do not harmonize the two.**

## III.0 ⚠ "Noticed somewhere" is not "available where it is needed"

**Added 2026-08-30 from a verified instance.** A differentiation instrument only works if the findings that
distinguish its members have actually **reached** it.

**The measured case.** Two cities in one three-city cluster were assigned **the same planetary symbol**. The
collision *was* noticed — recorded in one city's robot-culture file, correctly, months earlier. **But the
cluster's own purpose-built differentiation guide contained zero mentions of symbols, planets, or elements.**
The one file whose entire job was keeping those three cities apart did not know.

> **So, when a differentiation instrument exists, check that it is current:**
> 1. **Has anything been established about these locations since the instrument was last updated?** Symbol
>    assignments, census revisions, founding corrections, and renames are the usual stragglers.
> 2. **A finding recorded in a file nobody consults during differentiation is not doing differentiation work.**
> 3. **Propagation is part of the finding, not a follow-up.** Per Step 9, the column goes in **the same
>    commit** — and so does anything discovered about a *sibling* along the way.

## III.1 What it is

**One file per sibling set**, listing **each completed location's answer per category**, so a new location can
be checked against a single file read instead of re-reading every sibling's full document.

**It exists because the check gets more expensive with every location completed and would otherwise quietly
stop being run** — and because it has already failed once in this project, when two districts were given nearly
the same food custom a day apart.

**Structure:** one section per category most at risk of collision; one row per location; the capability shape
and deficit-address table first, because that is what everything else descends from.

## III.2 How to run it

> ⛔ **STEPS 1–2 ARE TERMINAL-ONLY as of 2026-09-06. Do not run them inside a per-location pass.**
> ✅ **In-run, jump to III.4 and add your own column.**

1. ⏸️ **Before writing a category**, read its row.
2. ⏸️ **If your answer rhymes with any entry, either differentiate it explicitly and inline — in the finding
   itself — or change it.** A prose assurance that "this is different" is not checkable and does not survive the
   next pass; **write the comparison as a table on at least four axes**, and include the **tense** axis — *where
   and when the loss happens* — which is the one most often skipped and the one that most often separates two
   locations that otherwise look identical.
3. **Name the axis the category answers on**, in bold, and confirm no completed sibling already uses it.
   **Different content is not differentiation; a different question is.**
4. **After completing a location, add its column in the same commit.**

## III.3 Sibling sets of different sizes

| Set size | How to run it |
|---|---|
| **Large** (20+) | Full table. **Check the most recently written first** — collisions cluster there, and that comparison will produce most of the work. |
| **Medium** (5–20) | Full table; expect most pairs to eventually be compared directly. |
| **Two** | **Write them together.** Two locations holding one faculty at opposite extremes are each other's exact remedy — and **the remedy is unacceptable**, because taking it means conceding the other's authority over that faculty. Writing them months apart wastes the sharpest contrast available. |
| **One** *(no siblings)* | See below. |

## III.4 The no-sibling case

**The district methodology never faced this. Several location types face it routinely** — a unique station, a
sole polity, a one-off megastructure.

**Four substitutes, in order of strength:**

1. **Its own earlier states.** A location with history is its own sibling set across time: differentiate the
   present frame against the founding frame and the crisis frame. **Usually available, and the strongest.**
2. **The nearest analogous location at another scale.** A unique station against the cities; a unique polity
   against its own sub-units.
3. **Real-world comparables**, with divergence stated explicitly per the source-not-specification rule.
4. **The generator-conflict method** (`02` §5) — which needs no sibling set at all, and is a large part of why
   this methodology runs three generators instead of one.

> **A location with no siblings is at elevated risk of reading like the author's defaults**, because nothing is
> pushing back. **Say so in the pass**, and run substitute 1 without fail.

---

# Part IV — The standing honesty problems

**Carried from `00_RUNBOOK.md` and generalized. Recorded here because they are easy to stop seeing.**

- **A zero from a scan is not a result until you have proved the scan could have found a hit.** Four recorded
  instances in this project of a confident wrong answer from a pattern assumption, plus a fifth where a phrase
  wrapped across a line break and a single-line search could not match it. **Prose files are hard-wrapped;
  assume every multi-word pattern is broken somewhere.** Search for the shortest distinctive fragment that fits
  on one line, or normalize whitespace first.
- **Self-audit error does not run in one direction, and that is worse than if it did.** Six consecutive
  mis-readings that flattered the pass produced a rule to re-check in the flattering direction — and then a
  re-scan ran *against* the pass and was also wrong. **The direction was never the real problem; an unverified
  instrument was.** Re-check in both directions and verify the tool before trusting either.
- **~~The gates have never caught a plausibility failure~~ — UPDATED 2026-08-30.** Every gate checks something
  inside the project against something else inside the project, and **the seven errors the developer caught
  were all coherent, sourced, differentiated, and wrong about how people behave.** **Gate 11 has now caught one
  itself**, on a real test case — an order-of-magnitude scale error, found by dividing population by area. **The lesson
  is narrower than "the gate works": the part that fired was the part that was arithmetic.** The interpretive
  half of Gate 11 caught nothing, as before. **Prefer a number to a judgment wherever the gate offers a
  choice.**

- **⭐ A COLD READ IS A CANON-AUDIT INSTRUMENT, and it is the cheapest one available.** *(Added 2026-08-30.)*
  One cold pass surfaced **four live canon errors** that had survived repeated review: a nation wrongly
  credited with causing a war *(in cross-project canon, binding five projects)*; a city name recorded as
  undecided six weeks after it was settled; a polar night stated as **six months** where the location's own
  spec says **~60 days**, used as the premise for four separate cultural findings; and an exile duration of
  **130 years** where the timeline gives **~250**.
  > **Why a cold reader finds these and a continuous one does not: a familiar canon line is *recognized*
  > rather than parsed.** A claim that has quietly hardened from proposal into fact is visible only to someone
  > meeting it for the first time. **None of the four was subtle. All four were in plain text in files that had
  > been read many times.**
  > **So schedule cold reads for canon maintenance, not only for methodology testing.**
- **A perfect prediction record from a self-grader is house style, not evidence.** The predictions were written,
  the locations chosen, the passes run and the results graded by the same person. **The only prediction that
  ever failed did so on a countable fact; every survivor is interpretive.** Two things restore it as a test:
  run a location chosen *because* it looks least likely to conform, or **state in advance what observation would
  falsify each rule.** Prefer the second — it costs nothing and it is the one that has never been done.
- **The Review Panel is not independent review.** Same author writes the location and the objections. Better-
  directed attention, not a second opinion. **And the panel does not check plausibility either, although it
  looks as though it does** — every position on it exists only if the place is already plausible, so no
  panelist has a standpoint from which to doubt it.
- **A recorded failure is not a fixed failure.** When a discipline names an example, open it and confirm the
  text changed.
- **And one specific to this methodology, stated now rather than after it bites:** **none of this has been run
  on anything.** The district gates each descend from a named pass that went wrong. These do not. **The first
  several real runs should be treated as tests of the instrument as much as of the location**, and every gate
  that fires — or conspicuously fails to — should be recorded here with the location it happened on.

---

# Part V — INSTRUMENTS ON TRIAL

> ## ⚠⚠ NOTHING IN THIS PART IS LAW. **It is a proposal with a stated falsification condition, awaiting a second location.**
> **Added 2026-09-11 at the developer's direction:** ***"append it as a test, so that we can see how it flies
> on a different city to see if the same defects still happen."***
>
> ⛔ **Do not cite Part V as binding. Do not enforce it in a review.** A pass that ignores it entirely is not in
> violation of anything. **Its only obligation is on the pass that agrees to run the trial, and that obligation
> is to RECORD, not to comply.**

**Why this Part exists in this form rather than as a new rule:** Part IV, above, says a perfect prediction
record from a self-grader is house style rather than evidence, and names two things that would restore it as a
test — ***"run a location chosen because it looks least likely to conform, or state in advance what observation
would falsify each rule. Prefer the second — it costs nothing and it is the one that has never been done."***

> ### ⭐⭐⭐ **THIS IS THAT, DONE FOR THE FIRST TIME.** **The falsification condition below was written BEFORE the second location ran.**

---

## V.1 — THE DEFECT BEING TRIALED AGAINST

**Found on `Zhongshan_Opus`, Step 7, 2026-09-11, by an audit seeded from a single defect caught by accident
three steps earlier.** **Four quotations in the pass did not match their cited source.**

| | |
|---|---|
| **Class** | ⛔ **Three are tightening ELISIONS with no `…` marker** — words removed. **One ADDS words**: a table's column header welded onto a body cell to manufacture a sentence |
| ✅ **What none of them is** | **A fabrication.** Every one has a real source saying substantially the same thing. **Citation hygiene, not reasoning** — no pass finding changed |
| ⭐⭐ **The locus, which is the whole finding** | ⛔ **ALL FOUR ARE IN TABLE CELLS.** Index rows, register rows, lens rows. ***Not one is in running prose*** |
| ⭐⭐⭐ **The control that proves the container is the variable** | **The same sentence appears TWICE in the same file in the same session** — `04_Phase_09` **L229**, in prose, **quoted in full and correctly**; `04_Phase_09` **L32**, in a cell, **two phrases dropped** |

> ## ⛔ **SO THE MECHANISM IS NOT CARELESSNESS AND NOT MEMORY. IT IS LAYOUT PRESSURE.**
> **A table cell wants a short quotation, and `…` is the cheapest character to drop when the cell is already
> crowded.** ⭐ **Which is why the deletions are not random — each removed exactly the qualifier that was
> costing horizontal space:** *`specifically` · `so` · `of a solution` · `herself`.*

### ⚠ And the reason it went ten phases undetected: the check was named but never written

```
mentions of "quotation audit" across the ULM, 2026-09-11:
  03_The_Phase_Spine.md                              11
  Stepwise_Execution/01_Spine/S06_Step_4...           1
  PRE-TRIP_INSPECTION_RECIPE.md                       1
  00_RUNBOOK.md                                       1
  Test_Runs/OBSERVATIONS_and_Methodology_Findings     1

  files DEFINING how to run it:  0
```

> **Every one of the fifteen is the same `M-169` sentence — *"it passed the spelling sweep, the table check,
> the contradiction gate, THE QUOTATION AUDIT and the swap test."*** ⛔ ***A check that existed only as a name
> in a list of checks that were passed.*** **`M-121` again: registered globally is not registered at the point
> of use.**

---

## V.2 — THE THREE PROPOSALS, in descending order of expected strength

**Ordered by `00_RUNBOOK.md`'s own principle:** ***"Every other fix in this methodology ADDS a control. This
one DELETES THE SURFACE. A control can fail. An absent leak cannot."***

### ⭐⭐⭐ T1 — DELETE THE SURFACE

**Index, register and summary rows carry a `file:line` pointer plus a 3–5 word tag — never a quoted string.**
**The quotation lives once, in full, in the prose where the argument is built.**

⭐ **This form is already law for a different purpose and needs EXTENDING, not inventing** — `00_RUNBOOK.md`
L247: *"cross-referenced by a **BARE POINTER — never quoted inline**,"* with this very file named as *"the
model to copy."* **It was written for `Test_Runs/` quarantine. The surface it does not currently cover is the
ordinary index table, which is every phase file in the methodology.**

⚠ **SCOPE IT HONESTLY — a blanket ban has a real cost.** **In a Zodiac Lens row the quotation IS the object
under analysis, not a pointer to one; banning it there breaks the instrument.** **Those rows go to `T2`.**

### ⭐⭐ T2 — INVERT THE DEFAULT

**Where a cell legitimately carries a quotation, the COMPRESSED form is the default rendering** —
`"…hard shell built…underneath is soft…"`, leading and trailing ellipsis by convention. **Completeness must be
actively asserted to remove them.**

> ⛔ **Right now the low-effort path is the dishonest one.** ⭐ **This inverts it: the lazy form becomes the
> honest form, and producing the defect requires positive effort rather than merely relaxing.** **It is the
> only one of the three that works WITH the pressure instead of against it, and it is therefore the one most
> likely to survive a tired phase.**

### ⭐ T3 — MECHANIZE, AND AT PHASE CLOSE

✅ **`Tools/quotation_audit.py`** — **written 2026-09-11, validated, and promoted out of a session scratchpad
that would have deleted it.** **Run it at the close of EVERY PHASE, not once at Step 7**, which is where these
four sat undetected across ten phases.

**Its three design properties are the transferable asset — each descends from a recorded failure of the
instrument itself, and they are why the third attempt worked where the first two produced garbage:**

| | Property | The failure it descends from |
|---|---|---|
| **1** | **Normalize hard** — dashes, curly quotes, `*`` ` ``_[]>\|#`, emoji, whitespace, **and case** | ⛔ **Run 1 reported `234/430` missing.** Prose is hard-wrapped; blockquote `>` and table `\|` markers land at different wrap points in source and pass. **`grep -o` returns false negatives SILENTLY** |
| **2** | **Exclude the pass's own folder** | ⛔ *Otherwise a quotation validates against itself and every quote "passes"* |
| **3** | ⭐⭐ **HARD positive controls AND a negative control** | ⛔⛔ ***Run 1's controls passed only because none of them spanned a wrap.*** **An instrument whose positive controls are all easy reports zeroes you cannot trust** — *Part IV's first bullet, met in the wild* |

> ### ⛔ THE PROPOSAL THAT IS **NOT** BEING TRIALED, named so it is not reached for
> **Restating *"always mark elisions with `…`."*** **It is the obvious move and it is worthless here — the rule
> was already known and already binding when all four defects happened.** `00_RUNBOOK.md` L81 has already
> measured this exact shape once: **the rule was written, in the file that stated the rule, and the error
> happened in it anyway.**

---

## V.3 — ⭐⭐⭐ THE FALSIFICATION CONDITION, STATED IN ADVANCE

**The baseline, produced by `Tools/quotation_audit.py` against `Zhongshan_Opus` on 2026-09-11 — the pass the
defect was found on, and therefore the pass that must NOT be corrected:**

```
pass audited : Zhongshan_Opus
corpus mode  : default (own pass excluded)
corpus files : 4685   chars: 34,936,551

  INSTRUMENT VALID: YES
  NEGATIVE CONTROL (must be absent): PASS - absent

fragments tested (single-line, ellipsis-split, >=7 words): 212
NOT FOUND in corpus: 49
  of those, in TABLE CELLS : 32
  of those, in PROSE       : 17

  CONFIRMED AT SOURCE AS REAL DEFECTS: 4   -   ALL FOUR IN CELLS, NONE IN PROSE
```

⚠ **Read the raw numbers honestly: `212/49` here against the `194/41` recorded in the pass's own `07_QA_Gates.md`.**
**The difference is `07_QA_Gates.md` itself**, which did not exist when the first run was made and which quotes
all four defects in order to report them. ⛔ **An audit file inflates its own pass's miss count. Expected, and
recorded rather than tuned away.**

> # ⛔⛔ WHAT WOULD FALSIFY EACH PROPOSAL
>
> | | **Confirmed if the next pass shows…** | ⛔ **FALSIFIED if the next pass shows…** |
> |---|---|---|
> | **T1** | **Confirmed defects in cells fall toward zero while prose stays clean** | ⛔ **Confirmed defects appear in PROSE at a comparable rate.** *Then the container was never the variable, the mechanism is not layout pressure, and the whole diagnosis is wrong* |
> | **T2** | **Cell quotations carry `…` by default and the confirmed-defect count drops** | ⛔ **Writers silently drop the default ellipsis too** — *in which case the honest form was not actually the lazy one and the inversion failed* |
> | **T3** | **The audit fires at a phase close and catches a defect BEFORE Step 7** | ⛔ **The audit is skipped at phase close and only run at Step 7 again** — *then a per-phase obligation does not survive contact with a real pass, exactly as `M-169` found, and it must move into `03`'s per-phase block to have any force* |
>
> ### ⚠⚠ AND THE OUTCOME THAT FALSIFIES THE ENTIRE PART
> ⛔ **The next pass runs a validated audit and finds FOUR-ISH DEFECTS, ALL IN CELLS, WITH `T1`–`T3` APPLIED.**
> ***Then the fix does not work and the mechanism is something none of the three proposals names.*** **Record
> that outcome as loudly as a success. Part IV's whole complaint is that this file has never recorded one.**

---

## V.4 — WHAT THE TRIAL LOCATION MUST DO

> ### ⛔⛔ SUPERSEDED 2026-09-11 — **DEVELOPER RULING: `T1`–`T8` ARE MANDATORY, EVERY STEP, EVERY PHASE, EVERY CITY**
> > ***"Not just on Davis. Every step, every phase, for EVERY CITY. That's why it's IN THE TEMPLATE."***
>
> ⭐ **RECORDING REMAINS REQUIRED** — *the falsification conditions in §9.1/§V.2.4 stand and must still be
> filled in.* ⛔ **But recording is now IN ADDITION to complying, never INSTEAD of it.**

~~**The obligation is to RECORD, not to comply.**~~ *A pass that applies none of `T1`–`T3` but runs the audit and
reports the numbers has fully discharged the trial — and is in fact the more informative result, because it
measures whether the defect recurs unaided.* ⛔ **No longer true. An unapplied instrument is now a defect.**

| | |
|---|---|
| **1** | **Run `Tools/quotation_audit.py <pass_folder>` at the close of every phase.** Paste raw output. **`CLAUDE.md`: never summarize it** |
| **2** | ⛔ **TRIAGE BY HAND. A miss is NOT a defect.** *The pass quoting itself and connective prose captured between two adjacent quotations both appear as misses.* **Confirm each at source** |
| **3** | **Report `confirmed defects` split by `CELL` vs `PROSE`.** ⭐ **That single ratio is the whole experiment** |
| **4** | **Record which of `T1`/`T2`/`T3` were actually applied, and which were skipped and why** — *a skipped proposal is data* |
| **5** | **Append the result to this Part with the location named**, per Part IV's closing bullet |

### ⛔⛔ GUARDS ON THE TRIAL

- ⛔ **DO NOT retrofit `T1`–`T3` to `Zhongshan_Opus`, and do not correct its four defects.** ***It is the
  baseline.*** **Correcting it destroys the only number the trial has to compare against.** *They are docketed
  at `R-29` and stay docketed.*
- ⛔ **DO NOT run the trial on `Zhongshan_Sonnet`.** *It is the held control half of a deliberate model
  divergence fork sitting at Phase 3. Introducing a new instrument into one arm of a two-arm comparison
  destroys that experiment to serve this one.*
- ✅ **Run it on the NEXT CITY to open a pass**, whichever that is.
- ⚠ **THIS IS NOT A COMPARISON OF CITIES AND DOES NOT TOUCH THE ONE LOCATION LAW.** *It compares the behavior
  of an INSTRUMENT across two runs. No content, finding, axis or figure from one city is read into the other —
  the only quantity crossing between them is a defect count for a tool.*

### 📌 RESULTS LOG — *append one row per location, and record failures at full volume*

| Location | Date | Fragments | Misses | Confirmed defects | **CELL** | **PROSE** | T1/T2/T3 applied | Verdict |
|---|---|---|---|---|---|---|---|---|
| **`Zhongshan_Opus`** | **2026-09-11** | `212` | `49` | **`4`** | **`4`** | **`0`** | ⛔ **none — baseline** | ⚠ **BASELINE. Not a test of the fix** |
| *(next city)* | | | | | | | | |

---

# Part V.2 — THE HANDOFF LEDGER, AND WHAT AN AXIS SHEDS

> ## ⚠⚠ ALSO ON TRIAL. **Same terms as Part V: a proposal with a falsification condition, awaiting a second location.**
> **Added 2026-09-11 at the developer's direction:** ***"append them to Part V as an additional test trial so we
> can see how effective they are."***
>
> ⛔⛔ ~~Not law. Not enforceable in a review. A pass that ignores it is not in violation.~~
**SUPERSEDED 2026-09-11 — developer ruling.** ***"Not just on Davis. Every step, every phase, for EVERY CITY.
That's why it's IN THE TEMPLATE."*** ⛔ **`T1`–`T8` are LAW, are enforceable, and a pass that ignores them IS
in violation.** ⭐ **The falsification conditions below remain in force — they measure an instrument that now
runs unconditionally.**

---

## V.2.1 — THE DEFECT

**Found on `Zhongshan_Opus` at Step 8.** **`Phase 8` skipped the `§H` inbound handoff sweep. Five handoffs were
dropped, including a canon tradition handed to it THREE separate times.** ⭐ **Caught only because a LATER
phase's unrelated required reading happened to surface the same canon entry.**

### ⛔⛔ But the Review Panel found the part that matters, and it is not the dropped rows

**The `Lover faculty` — *is this place alive, and could anyone love it?* — is the one instrument in the
methodology that asks after beauty, pleasure and joy.** **It passed. It passed ONLY because of the repair.**

| What the amendment restored | |
|---|---|
| **The city's classical tradition** | *the wind as its only continuo* |
| **Its cuisine model** | *fusion by necessity* |
| **Its craft standard** | *two building stocks, two definitions of a good repair* |
| **Its seasonal trade** | *four months building, eight not* |
| **The wind reframed as a PROVIDER** | *`95%` of power — written three times as hazard, noise and schedule, never once as supply* |

> ## ⭐⭐⭐ **THAT IS THE ENTIRE INVENTORY OF WHAT MAKES A PLACE LOVABLE, AND ALL OF IT WAS IN THE DROPPED ROWS.**
> **Without the repair the pass had a structure and no pleasures — and would have passed every one of the
> seventeen gates.**

### ⭐⭐⭐⭐ THE MECHANISM, AND IT GENERALIZES TO EVERY POSITION

> # ***A SKIPPED SWEEP DOES NOT DROP MATERIAL AT RANDOM. THE AXIS PROTECTS WHAT SERVES IT AND SHEDS THE REST.***

**`Phase 8`'s axis was structural, so what it shed was sensory, human-scale and pleasurable.** ⛔ **A phase with
an economic axis will shed the intimate; one with a governance axis will shed the child.** ⭐⭐ **And each panel
position is the sole instrument that asks after one of those categories — so the loss is invisible until that
position is voiced, ONCE, at the very end, when it can only be patched.**

---

## V.2.2 — ⛔⛔ AND THE BASELINE IS WORSE THAN THE DEFECT REPORT SAID

**`Tools/handoff_audit.py`, written and validated 2026-09-11, run against the pass that found the defect:**

```
pass audited : Zhongshan_Opus          phase files : 9

=== CONTROLS ===
  POSITIVE (detector must find a formal block): phases 7, 8, 9
  NEGATIVE (detector must find nothing)       : phases 2, 3, 4, 5, 6
  INSTRUMENT VALID: YES - both classes present, detector discriminates

  phase | outbound | sweep    | rows | verdict
  ------+----------+----------+------+---------
      2 |        0 | NONE     |    0 | n/a - nothing addressed to it
      3 |        1 | NONE     |    0 | *** NONE - 1 ROWS UNACCOUNTED ***
      4 |        1 | NONE     |    0 | *** NONE - 1 ROWS UNACCOUNTED ***
      5 |        1 | NONE     |    0 | *** NONE - 1 ROWS UNACCOUNTED ***
      6 |        2 | NONE     |    0 | *** NONE - 2 ROWS UNACCOUNTED ***
      7 |        4 | FORMAL   |   23 | reconcile 23 enumerated against 4 outbound
      8 |        5 | FORMAL   |    7 | reconcile 7 enumerated against 5 outbound
      9 |        3 | FORMAL   |    7 | reconcile 7 enumerated against 3 outbound
     10 |        5 | informal |    0 | informal only - 5 rows never enumerated

TOTAL outbound handoff rows: 22
PHASES WITH ROWS ADDRESSED TO THEM AND NO ENUMERATION: 5
```

> ## ⛔⛔⛔ **`PHASE 8` WAS NOT AN ANOMALY. IT WAS THE CASE WHERE THE SAME OMISSION HAD VISIBLE CONSEQUENCES.**
> **`Phases 3, 4, 5, 6` enumerated NOTHING. `Phase 10` ran the sweep and never wrote it down.** ⭐ **Of eight
> eligible phases the sweep was formally enumerated in THREE — and one of those three is `Phase 8`'s own
> repair.** ***At the time of writing it was two of eight.***
>
> ⭐⭐ **The pass's own amendment said *"this pass ran it at Phase 7, Phase 9 and Phase 10."* That was
> generous.** **Recorded at full volume per Part IV, because a self-report that flatters the pass is the
> failure this file exists to measure.**

### ⚠ AND THE INSTRUMENT'S OWN LIMIT, NAMED BEFORE ANYONE TRUSTS IT

**It detects a FORM, not an act.** ⛔ **`Phase 10` genuinely ran the sweep and reads as `informal`.** ⭐⭐ **That
false positive is itself the finding:** ***a step with no required form cannot be audited at all*** — **which
is why `C2` below is not a reminder but the precondition for every other check here.**

---

## V.2.3 — THE FIVE CHECKS, in descending order of expected strength

| | Check | Attacks |
|---|---|---|
| ⭐⭐⭐ **C1** | **HANDOFFS BECOME AN ACCOUNTING IDENTITY.** *Every outbound row is discharged BY NAME in its target phase — written, or refused with a reason.* **Then `outbound N` vs `discharged N` is arithmetic.** ✅ **The outbound half already parses for free** | *silent skipping* |
| ⭐⭐⭐ **C2** | **THE `§H` SWEEP GETS A RECEIPT, IN THE `M-171` CLOSE BLOCK.** *A phase does not close without pasting its inbound enumeration.* ⭐ **Adds no machinery — routes a missing check into the Step 4 close-out check, which already reads receipts and already caught the `G6` omission** | *silent skipping · and it is what makes `C1` auditable at all* |
| ⭐⭐ **C3** | **A POSITION-COVERAGE LEDGER.** *Nine rows — six Flat Archetypes, Passer-Through, Neighbor, Lover faculty — one column per phase. At each close, one mark: did this phase produce anything this position could stand on?* ⭐ **The BLANKS are the instrument.** ⛔ **Bookkeeping, NOT generation — it records what the phase produced anyway** | *the shed category · the end-loaded panel* |
| ⭐⭐⭐ **C4** | **ONE QUESTION AT EVERY PHASE CLOSE: *"What did this phase's axis have no use for?"*** **One line, answered at the moment of shedding.** ⭐ *For `Phase 8` the honest answer was "everything sensory — the axis is structural," which is the whole finding, free, at the time* | ⭐ *the deepest cause* |
| ⭐ **C5** | **RUN THE `Lover faculty` EARLY, AS A SMOKE TEST** — once after `Phase 6`, again at Step 8. ⚠ **The one proposal with a contamination risk**, stated plainly: it edges a review instrument toward generation. *Its defense is that "is this place alive?" says something is missing without saying what to write* | *the end-loaded panel* |

> ### ⛔ THE CHECK THAT IS **NOT** BEING TRIALED, named so it is not reached for
> **"Run the `§H` sweep, really."** ⛔ **The rule existed, was binding, was read, and was skipped in six of
> eight phases anyway.** *Identical in shape to Part V's rejected fix.*
>
> ### ⛔⛔ AND A HARD BOUND ON ALL FIVE
> **`00f` §7: the panel is *"a review mechanism, not a generation mechanism."*** ⛔ **None of `C1`–`C5` may
> become a list of positions to write toward.** ***A pass written to satisfy eight positions produces eight
> accommodations, and `00f` Rule 3 already measured where that ends.***

---

## V.2.4 — ⭐⭐⭐ THE FALSIFICATION CONDITIONS, STATED IN ADVANCE

> | | **Confirmed if the next pass shows…** | ⛔ **FALSIFIED if the next pass shows…** |
> |---|---|---|
> | **C1** | **A mismatch is caught at a phase close, before the target phase is written** | ⛔ **Mismatches are reconciled cosmetically** — *rows marked discharged that were not. Then the identity measures compliance with itself and nothing else* |
> | **C2** | **Every phase closes with an enumerated receipt; the close-out check reads them** | ⛔ **Receipts appear and are empty, or the sweep is written AFTER the phase.** *A receipt for an act that already happened is a record, not a check* |
> | **C3** | **A position's row is visibly blank before Step 8, and that blank is acted on** | ⛔⛔ **The ledger is filled in retroactively at Step 8**, *which makes it a summary of the panel rather than a warning about it* — **or phases start writing toward blank rows, which is the contamination `00f` forbids** |
> | **C4** | **At least one phase names a shed category that a later position would have missed** | ⛔ **Every phase answers "nothing" —** *then the question is decorative, and the axis is not actually shedding anything, which on this evidence is not credible* |
> | **C5** | **The early run says "not yet" and the late run says "yes"** | ⛔ **The early run changes what the middle phases write.** *Then it is generative and must be withdrawn* |
>
> ### ⚠⚠ THE OUTCOME THAT FALSIFIES THE WHOLE PART
> ⛔ **The next pass applies `C1`–`C5`, and its `Lover faculty` still passes only on material added after the
> fact.** ***Then the shed category is not recoverable by bookkeeping, and the fix has to be structural — the
> panel moved earlier, or the phase spine rebalanced.*** **Record that as loudly as a success.**

---

## V.2.5 — WHAT THE TRIAL LOCATION MUST DO

> ⛔⛔ **SUPERSEDED 2026-09-11 — mandatory on every step, phase and city.** *See §V.4's ruling block.*

~~**The obligation is to RECORD, not to comply.**~~ ⛔ **Comply AND record.**

| | |
|---|---|
| **1** | **Run `Tools/handoff_audit.py <pass_folder>` at every phase close.** **Paste raw output.** ⛔ *`CLAUDE.md`: never summarize it* |
| **2** | ⛔ **Check the CONTROLS line first.** *If the detector never discriminated, every verdict below it is meaningless* |
| **3** | **Report `PHASES WITH ROWS ADDRESSED TO THEM AND NO ENUMERATION`.** ⭐ *That single number is `C1`+`C2`'s whole experiment* |
| **4** | **Report the `Lover faculty`'s verdict AND whether it rested on material added after the phase that should have carried it.** ⭐ *That is `C3`–`C5`'s whole experiment* |
| **5** | **Record which checks were skipped and why** — *a skipped check is data* |

### ⛔⛔ GUARDS

- ⛔ **DO NOT retrofit `C1`–`C5` to `Zhongshan_Opus`, and do not add the missing sweep blocks to Phases 3–6
  and 10.** ***It is the baseline.*** *The `2-of-8` figure is the only number the trial has to beat.*
- ⛔ **DO NOT run this on `Zhongshan_Sonnet`** — *held control, Phase 3, divergence fork.*
- ✅ **Run it on the NEXT CITY to open a pass.**
- ⚠ **This compares INSTRUMENTS across runs, not cities.** *No content crosses. `THE LAW OF ONE LOCATION`
  is untouched.*

### 📌 RESULTS LOG — *append one row per location; record failures at full volume*

| Location | Date | Outbound rows | Phases w/ rows and NO enumeration | Formal / informal / none | Lover faculty | Rested on a late repair? | C1–C5 applied | Verdict |
|---|---|---|---|---|---|---|---|---|
| **`Zhongshan_Opus`** | **2026-09-11** | `22` | ⛔ **`5` of `8` eligible** | `3 / 1 / 5` *(and one of the 3 is a repair)* | ✅ **PASS** | ⛔⛔ **YES — entirely** | ⛔ **none — baseline** | ⚠ **BASELINE. Not a test of the fix** |
| *(next city)* | | | | | | | | |
