# Completion QA Checklist — the closing gate

**Added 2026-08-16.** A district is **not complete** when its last phase is written. It is complete when it
passes this checklist. Run it as a deliberate final pass, and record the result in the district's own
`Full_Extrapolation.md` before marking it done in the Plan's progress tracker.

**Why this exists.** Cancer cleared all seven original phases and was marked complete while still missing six
template categories entirely, including `siligel` — established national canon — which appeared zero times in
the file. Nothing in the process checked. This gate is that check.

---

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
after you. The mechanical scan finds candidates; you decide which of the three outcomes each one is. Also confirm the sections marked **Covered** genuinely are covered *somewhere* for this
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

## Recording the result

Append a short QA block to the district's `Full_Extrapolation.md`:

```
## QA — Completion Check (District Culture Development Plan)

**Run YYYY-MM-DD.** Gates 0-9 per `Phase_Instructions/00c_Completion_QA_Checklist.md`.
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
```

Only after this block exists may the district be marked complete in the Plan's per-district checklist — and per
Gate 0, the block you write there must list every phase the file actually contains, not a summary claim.
