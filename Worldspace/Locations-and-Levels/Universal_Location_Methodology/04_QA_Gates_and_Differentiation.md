# QA Gates and the Differentiation Instrument

> **⚠ Read `00_RUNBOOK.md` first.** These are its Step 7.

> **⚠ LAW 0 applies here more than anywhere.** **These gates can confirm that a pass is not *wrong*. Not one of
> them can tell you it is not *thin*.** A location can pass every gate below and still be shallow —
> template-complete, internally consistent, correctly scoped, and lifeless. **Passing QA is not the same as
> being finished.**

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

**Gate 6 — Duplicate institutions.** Within the location, and against completed siblings. **Uses the
differentiation instrument in Part III.** **Check the most recently written sibling first** — collisions cluster
there, because whatever was most recently solved is the nearest available shape and it gets reached for. **State
the contrast inline, in the finding itself**, not in a footnote.
> ### ⚠ Gate 6 is UNRUNNABLE in a cold pass, by construction — a scheduling problem, not a failure
> **Added 2026-08-30.** Gate 6 needs the siblings' completed material and the differentiation instrument. **In
> a cold or anti-contamination pass that material is precisely what is withheld.** **The anti-convergence gate
> and the circularity rule are in direct conflict, and one of them must lose.**
>
> **Resolution: Gate 6 runs LATE — at Step 7, when the withheld files are opened — not never.** Until then run
> **all four** Part III.4 substitutes and say in the pass that you did.
>
> **And an encouraging result worth recording, from a real test case.** When Gate 6 finally ran on one cold
> pass it found two collisions with the location's own existing canon — **and Gate 4's swap test had already
> independently flagged one of them as the pass's weakest finding and demoted it, while that canon was still
> invisible.** **The blind instrument caught what the sighted one later confirmed.** **Gate 4 is therefore
> partial cover for a deferred Gate 6 and should be run deliberately as such** — pick the swap partner most
> likely to expose a shared answer. *(The specific collisions are archived in
> `Test_Runs/Zhongshan_Extracted_Worked_Examples.md`.)*
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
> `Test_Runs/Zhongshan_Extracted_Worked_Examples.md`, found the property relocated a demographic-diversity
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
> *(The specific worked case is archived in `Test_Runs/Zhongshan_Extracted_Worked_Examples.md`.)*
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
> copying exactly, because it required no judgement at all:
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
> `Test_Runs/Zhongshan_Extracted_Worked_Examples.md`.)*
>
> > **The transferable rule: before trusting any texture claim, price it against a density figure.** Population
> > over extent is one division, it needs no interpretation, and **it is the only part of this gate that does
> > not run on the same faculty that produced the error.** **Run it every time, early.**
> >
> > *(Note the redundancy that worked: the same pass's own Phase 0 had already caught the same problem, by
> > declaring a divergence between its population band and its extent band. **Two different instruments, two
> > different stages, same catch.** Declaring both bands — `01` §2 — is the cheaper of the two.)*

---

# Part II — The four new gates

These have no district equivalent because the district set had no type, band, frame or parent variation.

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
> judgement.** *(The specific counts and the recurring miss they revealed — a purely local holiday invented
> without ever checking what the location does with a national observance — are archived in
> `Test_Runs/Zhongshan_Extracted_Worked_Examples.md`.)*
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

> **⚠ This entire Part is PEER-REQUIRED — an enhancement, not the core.** Per `00_RUNBOOK.md`, the methodology's
> unit is **one location**, and **most passes will have no sibling set at all.** A pass without one is not
> failing this Part; it is running **III.4**, which is the ordinary path. **Do not treat a missing
> differentiation table as a missing gate.**

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

1. **Before writing a category**, read its row.
2. **If your answer rhymes with any entry, either differentiate it explicitly and inline — in the finding
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
  half of Gate 11 caught nothing, as before. **Prefer a number to a judgement wherever the gate offers a
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
