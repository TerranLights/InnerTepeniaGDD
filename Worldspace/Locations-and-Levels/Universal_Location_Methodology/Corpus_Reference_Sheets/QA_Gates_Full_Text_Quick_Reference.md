# QA Gates — Full Text Quick Reference (Step 7, 17 gates)

> ⭐ **Tier U — corpus-wide, identical for every city.** Feeds every city's Step 7. Copied word for word from
> `04_QA_Gates_and_Differentiation.md`: the LAW 0 line (L5–L8), the governing test (L84–L92), and Parts I–II
> (**L96–L419**; Part I at L96, Part II at L288, Part III begins at L423), as of 2026-11-18. **Nothing below is
> city-specific — it is the same 17-gate checklist for all 38 cities and does not need re-extraction per city.**
> ⚠ Only the ACTUAL pass/fail verdict for a given city is Tier C — that is Step 7's own future content, not this
> sheet.
> *(Re-copied 2026-11-18: the earlier version, read 2026-09-15 and citing L96–419, was condensed under an "Extracted in full" title and lacked the 2026-10-01 and 2026-11-04 additions to Gates 0, 4, 5, C and 10. Two sheet notes, marked as such, follow the copy: the Gate 10 pointer and `00_RUNBOOK.md` Step 7's own rules.)* *(Re-copied in part 2026-11-18, `DR-142` item 2: `04` L167 amended in place, re-copied word for word at sheet L101; no line moved.)* *(Re-copied in part 2026-11-18, `DR-142` item 2 as corrected 2026-11-18 (substitutes 3 and 4 only): `04` L167 amended again in place, re-copied word for word at sheet L101; no line moved.)*

---

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

**Gate 0 outward also reads a tracker's scope words (*unattended*, *in the developer's absence*, *complete*) and its forward references (*Step N to confirm*) against the files, not only its completion marks.** *(Added 2026-11-04, `M-287`.)*

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
informative if it could plausibly fail. ⛔ **In a ULM / CST / RWBEM pass the partner is never another Tepenian
city** (`00_RUNBOOK.md`, THE LAW OF ONE LOCATION): swap onto a real-world comparable or a generic location of the
same type, and ask the peer-free question, *would this be true anywhere?* **Record which finding was weakest under the swap**, not merely that the
set passed. A gate that only ever reports success is not being run honestly.

**Gate 5 — Cross-location consistency.** Export/import coherence against neighbors *(RELATION: what flows and
where it lands, read from canon such as the Division of Industry, never from another location's culture pass)*; **shared-environment
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
> ✅ **In-run, run Part III.4 substitutes 3 and 4 only (real-world comparables; the generator-conflict method) and say in the pass that you did; record substitute 1 (its own earlier states) as deferred to after the pass; do not run substitute 2 (the nearest analogous location at another scale), which reads another location and belongs to the terminal differentiation check** (`DR-142` item 2, as corrected 2026-11-18; `Run_Modes_Warm_and_Cold.md` L127; a pass captures a place at its height, `DR-136` item 6, `DR-137` item 10). *(Was: ~~"run all four Part III.4 substitutes and say in the pass that you did"~~; then, earlier on 2026-11-18, ~~"run Part III.4 substitutes 2 to 4"~~.)*

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
it?* Six dispositions: **accepted · noted · rejected · refereed · unmet · declined.**
> **Refusals — `unmet` and `declined` together — should be common.** `unmet` measures **what a location knowingly
> protects** rather than how hard the panel was run, so **a low `unmet` count is not a soft panel** — it usually means the location's problems are absences it
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
- **When a ruling changes a fact, check its "applied" list against every file that states the fact, at once.** A ruling applied to some sources and not others is recorded as a Gate C failure, with the files that lag. *(Added 2026-11-04, `M-312`/OBS-9.)*
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

## Sheet notes (not `04` text)

**Gate 10's full text lives in** `Corpus_Reference_Sheets/Review_Panel_Full_Text_Quick_Reference.md` *(corrected 2026-11-18: the earlier version of this sheet cited "`Corpus_Reference_Sheets/Review_Panel` content", a name no file has; folder listing)*.

**`00_RUNBOOK.md` Step 7's own rules, copied word for word from L2941–L2944 as of 2026-11-18** *(added 2026-11-18: this sheet feeds Step 7 and carried neither; the runbook added both on 2026-11-04)*:

**Paste raw scan output, whole; or, where it is long, save the whole output to a file beside the record and head the pasted part *raw output, excerpted (N lines omitted, reason)*.** A block with no such heading is read as complete. Cutting another location's lines under the law of one location is a labeled excerpt, not a summary. *(Added 2026-11-04, `M-285`; Mirny Phases 5–10.)* **Verify the instrument before trusting any zero. Report what Gate 11 cleared as well as
what it flagged.**

**The station-builder scan looks for denials as well as assertions.** A sentence saying the builder does *not* explain a form is the same violation as one saying it does (`DR-19`; `No_National_Stereotypes.md`; `Corpus_Reference_Sheets/No_National_Stereotypes_Quick_Reference.md` L76–78). Read every hit in context. *(Added 2026-11-04, `M-279`; Mirny Step 7.)*
