# QA Gates — Full Text Quick Reference (Step 7, 17 gates)

> ⭐ **Tier U — corpus-wide, identical for every city.** Feeds every city's Step 7. Extracted in full from
> `04_QA_Gates_and_Differentiation.md` Parts I–II (L96–414), read in full 2026-09-15. **Nothing below is
> city-specific — it is the same 17-gate checklist for all 37 cities and does not need re-extraction per city.**
> ⚠ Only the ACTUAL pass/fail verdict for a given city is Tier C — that is Step 7's own future content, not this
> sheet.

**Governing test, before the checklist starts:** *"Is this internally consistent, and characteristically
aligned with this specific place — without being constrained to repeat what already exists?"* Two failure
modes, guarded by the gates together: **uncharacteristic** (an element that doesn't belong to this kind of
place) and **over-constrained** (refusing to produce anything not already in canon). The target is the space
between: new, but characteristically inevitable in hindsight.

**⚠ LAW 0 applies here more than anywhere: these gates can confirm a pass is not *wrong*. Not one of them can
tell you it is not *thin*.** A location can pass every gate below and still be shallow.

## Part I — The carried gates (0–11), from `00c_Completion_QA_Checklist.md`, generalized district→location

**Gate 0 — Does the completion claim match the file?** Cheapest gate, highest yield, fails in both directions.
Reconcile the tracker's claim against the file *and* the file's own open-questions list against what has
actually been resolved elsewhere. Check the target, never the claim. When a phase is added to the methodology,
every location already marked complete reverts to incomplete for that phase.

**Gate 1 — Coverage.** Confirm each applicable phase is answered, not gestured at. A mechanical scan is
worthless until proved it could find a hit — recorded defects: whole words missing their own stems (`funeral`
vs. *funerary*), terms never on the list (`mortuary`), a register the list didn't anticipate (`mourn` misses
*grief/grieving/bereavement*), a broken en dash (`human-robot`), a strip boundary capturing the wrong section.
Before concluding an absence, run the scan against a known hit first. Prefer stems, normalize dashes, paste raw
counts into the QA block — never summarize them. **Four outcomes per term, not two:** pass · fail · covered in
substance, absent in term (normal) · absent and unexplained (a genuine hole). Never insert a word to make the
scan pass.

**Gate 2 — General population.** Per `00b`, with the Band-1 inversion from `01` §2.3. Check every finding,
including inherited ones. Highest-risk categories: dress, sensory first-impressions, music, visitor experience,
per-population culture. When a discipline file cites a location as its own example, open that location and
confirm the text actually changed — the origin example is the one most likely to still be broken.

**Gate 3 — Internal contradiction.** Read the Ordinary Life phase last and check every other phase against it
— the best contradiction detector available. ⚠ This gate is the CLOSE POINT for Phase 4's contradiction role;
Phase 4 supplies the instrument, this gate wields it. Phase 4 itself checks backward against Phases 1–3 only
and then closes complete — never left open "pending Phases 5–10."

**Gate 4 — Swap test.** For each finding: would it survive essentially unchanged if swapped onto a comparable
location? Pick the partner most likely to survive the swap, not a convenient one. Record which finding was
weakest under the swap, not merely that the set passed.

**Gate 5 — Cross-location consistency.** Export/import coherence against neighbors; shared-environment
consequences (anything vented, emitted, sounded or spilled arrives somewhere); new categories are legitimate
discoveries — the check is only whether the new thing is named and cross-referenced so it enters canon cleanly.

**Gate 6 — Duplicate institutions.** ⭐ IN-RUN: within the location ONLY — does this pass name two institutions
that are the same institution twice? ⏸️ The against-siblings half is TERMINAL (ruled 2026-09-06, per the same
"worry about differentiation later" ruling as Step 6 — see `Differentiation_Instrument_Quick_Reference.md`). In
run, run all four Part III.4 substitutes and say so in the pass. Do not check the most recently written sibling
first or state a contrast inline — both revoked. Before recording ANY mismatch found at Step 7 as wrong or
killed, run the both-are-true test (`02` §5.3): *"do not ask which reading is right; ask what single property
would produce both, then check whether the two claims are about different objects or at different scales."*
Candidate scales to check before concluding a kill: (1) public/mainstream vs. private/minority-community,
(2) dominant culture vs. its own counterculture, (3) an earlier generation vs. a later one, (4) a
legal/procedural fact vs. a narrative/emotional one describing the same event. Not every mismatch reconciles —
the test is a required check before declaring a kill, not a guarantee against one.

**Gate 7 — Research accounting.** Every researched pick recorded as changed a finding · ornamented one ·
deliberately withheld · genuinely omitted. Withheld is not unused — record what it would have given and what
it's being held for. Expect roughly 70–80% to change findings; 100% should be suspected of counting ornament as
change; under half means the picks were chosen badly or abandoned before they paid out.

**Gate 8 — Standout recorded.** Name the single strongest thing the pass produced, and why.

**Gate 9 — Asymmetry.** For every finding describing a threshold, gate, conversion, verdict, admission or
status change: the mechanism runs both ways — did the file write both? What happens to someone the mechanism
decides against, is that outcome as durable, and is there any route back? A "no route back" nobody has
perceived as a problem is a textbook shadow. **Runs twice:** on inherited material before writing, and on the
thresholds this pass itself just wrote — a pass reporting Gate 9 firing only on inherited material has
probably not run the second pass. Run it against every membership, promotion or admission mechanism a pass
writes — the favorable path is the one that gets written, which is exactly why the gate exists.

**Gate 10 — The Review Panel.** `00f_Review_Panel.md`, carried unchanged — see
`Corpus_Reference_Sheets/Review_Panel` content already extracted for Step 8. `unmet` should be common and
measures what a location knowingly protects, not how hard the panel was run — a low count usually means the
location's problems are absences it does not know it has. A position that cannot be cast at all is itself a
finding, and a strong one.

**Gate 11 — Plausibility.** The one direction the others cannot look — every other gate checks a relation
between two things already inside the project; this asks: would a person actually do this, at this cost priced
in this location's physical conditions, for this reason, and whose behavior am I actually describing? **The
scale question:** what population, over what span, does my source actually describe — and am I asserting it of
a larger one? Weakest gate on the list; a self-audit runs it with the same faculty that produced the error, so
record what it flagged *and* what it cleared. **The one purely mechanical sub-check that has actually caught
something: divide the population by the area.** A real test case found a scattered-settlement pass whose own
arithmetic implied a density comparable to the densest real cities on Earth — run this division every time,
early, since it needs no judgment at all.

## Part II — The five new gates (`C · F · I · P · G`) — no district equivalent

*(Historical note: this heading read "the four new gates" 2026-08-30→2026-09-07 while five gates sat under it
— the gate SET never changed, only the count sentence was wrong; `M-167`.)*

**Gate C — Canon check, federated.** Was the four-question canon check (`00_RUNBOOK.md` §E) actually run,
against all three tiers? Was every search that produced a NEGATIVE result actually run across all three tiers,
and can you name the search paths? ("Repo-wide" is not exhaustive — the universe repo is a separate repo; a
grep that never left this repo is evidence about one directory, not about canon.) Was project canon checked
against the source, not the last pass that cited it? ⚠ **Shared constants — check at the SOURCE, never at the
neighbors.** A shared constant is invisible to per-file checking by construction: every file agrees with every
other file, so cross-checking between them passes, and agreement among siblings then reads as corroboration —
the error actively defends itself. Does this pass use a figure that also appears in other locations' files (a
duration, era length, generation count, population, distance)? If so, verify against the timeline/spec that
owns it — and if the corrected figure was carrying an argument, rebuild the argument, don't just renumber. Was
any thin-looking canon file checked for being a redirect stub? Rank order respected where sources disagreed,
with the contradiction stated rather than silently resolved? Anything binding beyond this location routed to
RESERVED instead of decided here? Anything genuinely new named, defined and cross-referenced? **Record which
canon files were actually opened** — a pass that reports "checked canon" without naming files has not run this
gate.

**Gate F — Frame integrity.** Does the pass stay inside its own declared frame? Four checks against the Phase 0
declaration block: (1) **Type** — did the pass answer the phases its type actually requires, or default to the
Settlement set? (2) **Band** — is every claim scale-appropriate; a Band 5 pass reading like Band 3 has committed
the scale error, and a Band 1 pass inventing a general population has committed its inverse. (3) **Status** —
does a declining location read as declining, or a healthy one with a sad note attached; does a ruined one
answer the Band 0 substitutions or the ordinary questions? (4) **Temporal frame** — did post-frame facts leak
in? Sweep for the adjacent era's proper nouns specifically.

**Gate I — Inheritance classification.** Is every element correctly classed (`01` §5.1: determined · inflected
· originated · aggregated)? Two opposite failures, both common: inventing a local variant of something the
parent determines (a sub-location does not have its own climate, currency or calendar — wrong, not thin), and
claiming origination for something inherited (how two siblings independently "invent" the same custom — both
actually inflected the same parental form and neither noticed). Walk the pass's named institutions and customs
and assign each a class explicitly; anything classed *originated* goes to Gate 6; anything that cannot be
classed is a flag. **The count is diagnostic:** if Originated outnumbers Inflected by more than ~3:1, stop and
re-run the `01` §5.1 order of attempts (what does the parent determine → what does it supply that this place
inflects → who arrived carrying one → is the place already doing it somewhere → only then invent).

**Gate P — Parent reconciliation.** Runs on a parent's pass, not a child's. When a location is written after
locations it contains: (1) collect every provisional assumption its children registered about it; (2) for each,
does this pass confirm, contradict, or leave it open; (3) where it contradicts one, say so explicitly and name
the child findings that now need revision — do not silently overwrite; (4) where it leaves one open, say that
too. A parent pass that does not run this gate has silently invalidated an unknown amount of its children's
work.

**Gate G — Generator honesty.** Did the spine actually get built the way `02` requires? Were at least three
generators run, and were they independent (three readings descended from the same underlying fact are one
generator wearing three hats — function, founding purpose and the parent's need are frequently the same fact)?
Was each run to a full profile before comparison? Were the conflicts mined or smoothed (a pass whose three
generators agreed on everything either got lucky or flattened them — record the conflicts found and how each
resolved)? Was any generator's null recorded as a null, rather than quietly dropped? Was the deficit researched
*after* the profile named it, not before? Was the Unrecognized Instrument run after the profile rather than
during it?
