# Completion QA Checklist — the closing gate

**Added 2026-08-16.** A district is **not complete** when its last phase is written. It is complete when it
passes this checklist. Run it as a deliberate final pass, and record the result in the district's own
`Full_Extrapolation.md` before marking it done in the Plan's progress tracker.

**Why this exists.** Cancer cleared all seven original phases and was marked complete while still missing six
template categories entirely, including `siligel` — established national canon — which appeared zero times in
the file. Nothing in the process checked. This gate is that check.

---

> **⚠ Read `00_RUNBOOK.md` first** — these gates are **Step 6** of that procedure, and several of them are
> meant to have been run earlier (Gate 0 at Step 0, Gate 9 at Step 1).

> **⚠ LAW 0 applies here more than anywhere.** *(`00_RUNBOOK.md`.)* **These eleven gates can confirm that a pass
> is not *wrong*. Not one of them can tell you it is not *thin*.** A district can pass every gate below and
> still be shallow — template-complete, internally consistent, correctly scoped, and lifeless. **Passing QA is
> not the same as being finished**, and the closing test in Law 0 is the one that decides: *could a person live
> an entire life here, and would that life be unlike a life in any of the other twelve?*

## The governing test: characteristic consistency

Every gate below serves one underlying question, and it is worth stating plainly before the checklist starts:

> **Is this internally consistent, and characteristically aligned with this specific region and its culture —
> without being constrained to repeat what already exists?**

Two distinct failure modes, and the checklist is guarding against both:

**Failure mode 1 — uncharacteristic.** An element that doesn't belong to *this kind of place*. In a district
full of factories, bars and pubs with live-music nights are entirely reasonable — nobody needs to have written
them down beforehand for them to fit. A giraffe is not. Neither is a guy riding a unicycle. The test is not
"has this been established?" but **"would this be unsurprising *in kind* to someone who knows what sort of
place this is?"**

**Failure mode 2 — over-constrained.** Refusing to produce anything that isn't already in canon. That yields a
sterile district that just re-labels its own existing material — the exact failure that forced Cancer's
from-scratch rewrite. New religions, new factions, new institutions, and whole new categories the 32-section
template has no slot for are all legitimate discoveries. **The template is a floor, not a ceiling.**

The target is the space between: **new, but characteristically inevitable in hindsight.** A reader should meet
a new element and think "of course this is here," not "where did that come from?" and not "I've read this
already."

This test is what makes the methodology produce *personalized* results rather than generic ones — it is
evaluated against each specific place's own established character, so the same technique run on a factory
district and a grief district correctly yields completely different answers.

---

## Gate 0 — Does the completion claim match the file?

**Added 2026-08-29 after Taurus.** Run this before anything else, because it is the cheapest gate and it caught
the largest single error found so far.

Open the Plan's per-district block and **count the phases it lists against the phases the file actually
contains.** Taurus's block read **"ALL 8 PHASES COMPLETE (2026-08-16)"** while listing only ten items, **none of
which was Phase 7** — a phase that had been inserted into the Plan that same day. The claim was false for two
weeks and nothing in the process was looking at it. Leo carried the identical defect.

**The standing rule this implies, which is binding going forward:**

> **When a phase is added to the Plan, every district already marked complete reverts to incomplete for that
> phase.** Adding a phase does not retroactively complete it anywhere. The Plan's per-district blocks and its
> progress tracker must both be corrected in the same commit that adds the phase, and the phase file's own
> per-district status table reset accordingly.

**Track record after five districts: this gate has caught a real defect in three of the four districts that
had a completion claim to check** (Taurus and Leo over-claiming, Scorpio under-claiming; Aries passed clean,
Cancer predates the gate). **It is the cheapest gate here and the highest-yield.** Do not treat it as a
formality because it occasionally passes.

**It fails in both directions — confirmed on Scorpio, 2026-08-29.** Scorpio's block listed Architecture,
Sensory Profile and Export Culture as **"needed"** and the tracker counted Phase 1 at 3/13, while all three were
already written to full depth as Findings V-VII. **The Plan was under-claiming**, which wastes work rather than
hiding gaps but is the same defect. **Treat Gate 0 as a reconciliation step, not an anti-over-claiming one:**
read the file, read the claim, and correct whichever is wrong.

A completion claim is a factual assertion about a file. Verify it against the file, not against memory of
having done the work.

## Gate 1 — Template coverage

Open `District_Culture_Development_Plan.md`'s **Complete template audit** table. For every one of the 32
sections marked **Phase 1-8**, confirm the district's `Full_Extrapolation.md` actually answers it. Not
"gestures at it" — answers it.

Fast mechanical check for the categories most often silently missed. **Run it per-term, and on the findings
only.** Two ways this check has actually failed in practice, both fixed below:

- **An aggregated `grep -c` with alternation cannot tell you which category is missing** — it returns the count
  of lines matching *any* term, so a file strong on `cuisine` and empty on `siligel` scores well. The original
  version of this gate had exactly that defect. Loop per term instead.
- **The QA block contaminates its own re-run.** A QA block that honestly names its gaps makes those very terms
  register as present the next time the check runs. Taurus's re-run showed `funeral`, `humor`, and `slang`
  "passing" for precisely this reason. Cut the QA block before counting.

```
# per-term, findings only — stop before the QA block
sed '/^## QA — Completion Check/,$d' <District>_Full_Extrapolation.md > /tmp/findings.md
for t in siligel cuisine music counterculture holiday human-robot glitch-coolant \
         funeral sport game humor slang death child elder gender; do
  printf "%-16s %s\n" "$t" "$(grep -ci "$t" /tmp/findings.md)"
done
```

Any zero is a fail. **So is a term that appears only inside a sentence declaring it absent** — the word being
present is not the category being covered, and the gate is worthless if it accepts its own excuses.

**But there is a third outcome, and it needs recording as such rather than forced into pass or fail.** A
category can be **covered in substance and absent in term**. Scorpio's `funeral` returned **zero** while
mortuary practice was the single most developed category in its pass — a body-breakers' institution, a
collective-cremation-derived holiday, and a whole doctrine about how death-work is conducted. The district
simply does not use that word; its vocabulary is procedural. Leo's `humor` behaved the same way.

**Record it as "covered in substance, absent in term" and move on.** Do **not** insert the word to make the
grep pass — that is gaming the gate, it degrades the prose, and it destroys the check's value for everyone
after you. The mechanical scan finds candidates; you decide which of the three outcomes each one is.

**This third outcome is normal, not exceptional — three districts in a row now.** Scorpio's `funeral`, Leo's
`humor`, Aries's `funeral` *and* `humor`. And there is a pattern worth knowing: **it is almost always the
emotionally loaded generic words that go missing**, because a well-developed district expresses those things in
its own register instead. The probe list is written in *template* vocabulary; a district that has found its own
is exactly the district that will score zero on it. **A cluster of substance-not-term results is a sign the pass
worked, not that it failed.**

> **⚠ PASTE THE SCAN OUTPUT INTO THE QA BLOCK. Do not summarize it.** *(Rule strengthened 2026-08-29, because
> the weaker version failed twice.)*
>
> The original rule said to *write the open list from the scan output rather than from memory.* **That rule was
> then violated on the very next district, in the same direction.** On Aries I listed `game` as open when it was
> covered and omitted `humor` when it scored zero; on Capricorn I listed `funeral` as absent when it scored 1
> and omitted `death` when it scored zero. **Four errors across two districts, all four flattering the pass.**
>
> An instruction to read carefully does not survive contact with an author grading their own work. **The fix has
> to be mechanical: paste the raw per-term counts into the QA block.** Then the disposition of every term is
> checkable against the data by anyone, including you a week later, and a mis-reading becomes visible instead of
> invisible. Also confirm the sections marked **Covered** genuinely are covered *somewhere* for this
district (they live outside the Full_Extrapolation, in Canon Reference / Mega-Init / diaspora file) — a
district missing its Canon Reference Cultural Texture entry, for instance, has a real hole that this plan was
never going to fill.

## Gate 2 — General-population discipline

Per `00b_General_Population_Discipline.md`. For each Finding — **including every pre-existing one, not only
what this pass wrote** — ask: does this describe the general population, or one profession's / ritual's /
narrow context's version presented as the default?

> **⚠ A recorded failure is not a fixed failure. Audit the source, not the lesson.** `00b` names three districts
> as its canonical examples. Checked 2026-08-29: **Cancer was corrected, Leo was corrected, and Scorpio — the
> district the file names first, as the origin case — was still broken**, with Finding VI asserting that a
> resident's face is "routinely covered in public." The lesson had been written down and the source had been
> left alone for six weeks. **The origin example is the one most likely to be uncorrected**, precisely because
> writing the discipline file feels like having dealt with it. Whenever a discipline document cites a district,
> open that district and confirm the text was actually changed.

Note that this gate found its Scorpio instance only because the developer flagged it mid-pass. A Gate 2 run
scoped to new material would have missed it entirely, which is why the scope above is explicit. Highest-risk categories:
**Fashion** (failed three times: Scorpio's masks, Cancer's caregiver vest, Leo's performer dressing), Music,
Sensory Profile's "first impressions," Visitor Experience.

## Gate 3 — Internal contradiction check

Read the district's **Ordinary Daily Life** finding (Phase 5) last, and check every other Finding against it.
It is the most reliable statement of who actually lives in the district and what they actually do, which makes
it the best contradiction detector in the file. Leo's Fashion error was caught exactly this way — performer
dressing as the district default, contradicting its own established majority-support-worker population.

## Gate 4 — Swap Test, every phase (not just Phase 8)

Originally scoped to Robot-Specific Culture only. Extend it: for each Finding, would it survive essentially
unchanged if you swapped in a comparable district? Pick the swap partner deliberately — a district of similar
map position (two small Hub-adjacent wedges) or similar civic register (two care/wound-adjacent districts).
If a Finding survives the swap intact, it hasn't localized; send it back or document honestly that nothing
district-specific emerged (a legitimate outcome — see the Honesty Check in the outer-city robot methodology).

**Choosing the partner — sharpened 2026-08-29.** Pick **the district most likely to survive the swap, not a
convenient comparable.** The gate is only informative if it could plausibly fail. Taurus was swapped against
**the Yards** — its closest structural affinity, sharing both its temperament family and its material,
working-class civic register — which is why the swap result carries weight: the strongest finding failed the
hardest available partner. A swap against a district with nothing in common proves nothing and should not be
recorded as a pass.

**Record which finding was weakest under the swap, not just that the set passed.** Taurus's QA names Finding
XXI(a) as the one that nearly survived and states what it survives on. A gate that only ever reports success is
not being run honestly.

## Gate 5 — Cross-district consistency

Check the district's new material against the districts already completed. Three specific things:

1. **New religions, factions, and whole new categories are legitimate discoveries — do not force them into
   pre-existing constructs.** If analysis produces a belief system, faction, institution, or phenomenon the
   existing roster has no slot for, that is the synthesis working, not a problem to manage. The check here is
   **not** "does this already exist somewhere, use that instead" — it is only: *is the new thing recorded
   properly so it enters canon cleanly?* That means a real name, a clear statement of what it is, and a
   cross-reference from wherever its category normally lives (a new religion should be noted in
   `Worldspace/Factions/Robot_Religions/`, a new faction in `Worldspace/Factions/`, and so on), so the next
   reader finds it. **The 32-section template is a floor, not a ceiling** — a discovery that fits none of the
   32 categories gets its own Finding rather than being crammed into the nearest slot or dropped.
2. **Export/import coherence.** Does anything this district exports conflict with a neighbor's established
   culture? *Worked example:* Cancer exports windbells; Taurus enforces strict quiet hours and is Cancer's
   established migration destination. That's a genuine friction worth naming rather than a contradiction to
   hide.
3. **Shared-environment consequences.** Concordia is enclosed. Anything a district vents, emits, sounds, or
   spills goes into volume shared with its neighbors. *Worked example:* Cancer's Growing Towers vent humid air
   — which has to arrive somewhere.

## Gate 6 — Duplicate-institution check, within the district AND against completed neighbors

**Extended 2026-08-29 after Leo**, which twice came within a sentence of colliding with Taurus.

**(a) Within the district.** New Findings frequently invent something the district already has under another
name. Scan the district's Canon Reference Community Infrastructure list against every new named place/practice.
If two are genuinely close, either merge them or state the relationship explicitly.

> **Use `../Cross_District_Differentiation_Table.md` for this half.** *(Added 2026-08-29.)* It lists each
> completed district's answer per category on one page, so this check costs one file read instead of six.
> **It exists because this gate already failed once** — the Power Core and the Yards were given nearly the same
> food custom a day apart. **Read the relevant row before writing a category, and add the district's column in
> the same commit that completes it.**

**(b) Against districts already completed — the new half, and it gets harder with every district finished.**
Structurally similar institutions will keep arising across districts, because the same categories are being
asked of every one of them. **That is not a failure and they must not be homogenized — but the contrast has to
be stated in the text, or the next reader merges them.** Leo produced two near-collisions with Taurus in a
single pass:

| Both districts have | Taurus | Leo |
|---|---|---|
| A meaning attached to **being fed** | *Admission* — a private threshold nobody explains | *Rank* — a public signal everybody reads |
| A **provenance system for objects** | Documents an object to prove **continuity** | Displays an object to transfer **standing** |

Each was written with an explicit "stated against Taurus deliberately, because these are not the same thing"
sentence. **Do that inline, in the finding, not in a footnote** — a reader meeting Leo's siligel custom without
it will assume it duplicates Taurus's. **The check: for every named institution, ask whether a completed
district has something structurally adjacent, and if so name the difference in the finding itself.** *Worked example:* Cancer's new Long Room vs. its
existing Threshold Waiting Rooms — related but distinct, and the distinction has to be written down or the next
reader will assume it's a duplicate.

## Gate 7 — Unused-research capture

Research always surfaces more than gets used. Before closing the district, record the leftovers in the
district's own research summary — the specific real-world details found but not fused, and why. They are the
first place to look when the district is next expanded. *Cancer's leftovers:* the *balie* (wet nurses who were
sometimes the birth mothers), della Robbia's swaddled-infant medallions, the snakes and dogs sleeping among
patients in the abaton, Eden's Fibonacci-geometry Core.

## Gate 8 — Standout recorded

The district's **Worth Your Attention** section names the single strongest thing the pass produced and why.
This is a standing project rule (`City_Megasheet_Compilation_Guide.md`), and it's also what feeds the
cross-district standout digest.

---

## Gate 9 — Asymmetry check: was only the favorable half written?

**Added 2026-08-29 after Taurus, where this caught a real hole in existing canon.**

For every Finding describing a **threshold, gate, conversion, verdict, admission, or status change**, ask: *the
mechanism runs both ways — did the file write both?*

Taurus's Finding II established that earned trust converts a stranger into someone whose door is answered warmly
"the first time, every time after." It wrote only the favorable case. **The mechanism is symmetrical: a verdict
that goes the other way is equally permanent, equally unspoken, and equally never revisited** — and because it
is never written down, the district's own belief system leaves nothing to appeal. That is the district's most
characteristic injustice, and its warmth and its injustice turned out to be *the same institution seen from two
sides*, with nobody acting in bad faith at any point.

This is cheap to run and high-yield, because the omission is almost never deliberate — a pass writing about how
a district welcomes people simply does not think to ask what happens to the people it doesn't.

**Run it on the district's *earliest* findings first.** Both instances found so far were in pre-Plan material
written 2026-07-09 — Taurus's Finding II and Leo's Finding III — and this is not a coincidence. Those findings
predate `00d_Shadow_Proportion_Discipline.md` entirely and were written to explain how a district *works*, which
is a framing that naturally documents the favorable path and stops. **Every district still carries four to seven
of these early findings** *(verified 2026-08-29 across the ten unstarted districts)*, so expect this gate to
fire on them and check them before checking anything written later.

**Ask of each such Finding:**
1. What happens to someone the mechanism decides *against*?
2. Is that outcome as durable as the favorable one? (Usually yes, and usually unwritten.)
3. Is there any route back? (Usually none, and usually nobody has noticed there isn't.)

A "no route back" that nobody in the district has ever perceived as a problem is a textbook shadow finding under
`00d` — unintended, unnoticed, and discoverable only by a player who goes looking.

## Gate 10 — The Review Panel

**Added 2026-08-29, at the developer's direction.** Full mechanism and roster:
**`00f_Review_Panel.md`.** Run it **after Gates 0-9 and before finalizing the standout**, because it frequently
changes what the standout should be.

**Why it exists:** every other gate in this file is a check the author runs against their own reasoning. Gates
0-9 catch omissions, contradictions and over-generalizations; **they cannot catch what a person standing in the
district would notice and the author would not.**

**The panel is built on K.M. Weiland's archetypes and John Truby's character web**, both already mined into this
project's character methodology. The standing panel is **Weiland's six Flat Archetypes — Child, Lover, Parent,
Ruler, Elder, Mentor** — the *resting* life-stages, which is exactly what a reviewer should be: someone settled
in a position rather than mid-crisis. Behind them sit the **six Life Arcs** (can this passage even happen here?)
and the **twelve Shadows** (what does this place enable in someone already gone wrong), pulled in as needed.
**Truby's four-corner opposition is the check on the panel itself** — if three positions raised the same
objection in different clothes, the panel has collapsed to one lens.

**A fourth panel, added the same day, comes from Moore & Gillette's *King, Warrior, Magician, Lover*:** four
**faculties** a functioning place needs — order/blessing, disciplined action, knowledge, and aliveness — each
with an active and a passive shadow (Tyrant/Weakling, Sadist/Masochist, Manipulator/Denying Innocent,
Addict/Impotent Lover). Where Weiland's archetypes are *who is looking*, these are *what is being examined*, so
they compose rather than compete. **Run the Lover faculty's question on every district without exception** —
*is this place alive, and could anyone love it?* — because it is the one question no other gate in this file
asks, and it is the likeliest omission in any district written from structure outward.

**These are positions in a human life, not roles in a society or a studio**, which is why the roster carries
unchanged to cities, nations, orbital settlements — and to novels and films as readily as to this game.

**Three rules, all load-bearing:** a position with nothing to say **says nothing** (manufacturing objections to
fill slots is the failure mode); reviewers are **not required to be fair or right** — the Neighbor From Across
the Line is biased by design, and the Shadows are hostile by definition; and **a position is not guaranteed to
get what it wants.**

**That third rule is the one most likely to be violated, and the most damaging when it is.** Before accepting
any objection, ask whether satisfying it would make this district **more like the other twelve** — because
accepting every reasonable want across eleven positions and thirteen districts retrofits each of them with a
children's space, a courtship venue, an eldercare route and a festival, and produces thirteen districts that
read the same. **A want the location characteristically would not satisfy is a finding about the location**, and
is recorded with the **`unmet`** disposition rather than treated as a gap to close. Record the objection, then decide it: **accepted**, **noted**, or **rejected**, each with a reason.

**Honest scope:** this reduces single-lens bias; it does not make the review independent, since the same author
writes both the district and the panel. Do not report its output as a second opinion.

## Recording the result

Append a short QA block to the district's `Full_Extrapolation.md`:

```
## QA — Completion Check (District Culture Development Plan)

**Run YYYY-MM-DD.** Gates 0-10 per `Phase_Instructions/00c_Completion_QA_Checklist.md`.
- Gate 0 Completion claim vs. file: ...
- Gate 1 Template coverage: PASS / issues found and fixed: ...
- Gate 2 General-population: ...
- Gate 3 Contradiction check: ...
- Gate 4 Swap Test: swapped against <district>; ...
- Gate 5 Cross-district: ...
- Gate 6 Duplicate institutions: ...
- Gate 7 Unused research: recorded above / at ...
- Gate 8 Standout: recorded in Worth Your Attention.
- Gate 9 Asymmetry: findings checked for unwritten reverse cases; ...
- Gate 10 Review Panel: run; see the panel block below.
```

Only after this block exists may the district be marked complete in the Plan's per-district checklist — and per
Gate 0, the block you write there must list every phase the file actually contains, not a summary claim.
