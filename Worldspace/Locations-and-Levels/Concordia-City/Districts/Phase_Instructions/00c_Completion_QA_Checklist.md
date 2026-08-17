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

## Gate 1 — Template coverage

Open `District_Culture_Development_Plan.md`'s **Complete template audit** table. For every one of the 32
sections marked **Phase 1-8**, confirm the district's `Full_Extrapolation.md` actually answers it. Not
"gestures at it" — answers it.

Fast mechanical check for the categories most often silently missed:

```
grep -ci "siligel\|cuisine\|music\|counterculture\|holiday\|human-robot" <District>_Full_Extrapolation.md
```

Any zero is a fail. Also confirm the sections marked **Covered** genuinely are covered *somewhere* for this
district (they live outside the Full_Extrapolation, in Canon Reference / Mega-Init / diaspora file) — a
district missing its Canon Reference Cultural Texture entry, for instance, has a real hole that this plan was
never going to fill.

## Gate 2 — General-population discipline

Per `00b_General_Population_Discipline.md`. For each Finding, ask: does this describe the general population,
or one profession's / ritual's / narrow context's version presented as the default? Highest-risk categories:
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

## Gate 6 — Duplicate-institution check

New Findings frequently invent something the district already has under another name. Scan the district's
Canon Reference Community Infrastructure list against every new named place/practice. If two are genuinely
close, either merge them or state the relationship explicitly. *Worked example:* Cancer's new Long Room vs. its
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

## Recording the result

Append a short QA block to the district's `Full_Extrapolation.md`:

```
## QA — Completion Check (District Culture Development Plan)

**Run YYYY-MM-DD.** Gates 1-8 per `Phase_Instructions/00c_Completion_QA_Checklist.md`.
- Gate 1 Template coverage: PASS / issues found and fixed: ...
- Gate 2 General-population: ...
- Gate 3 Contradiction check: ...
- Gate 4 Swap Test: swapped against <district>; ...
- Gate 5 Cross-district: ...
- Gate 6 Duplicate institutions: ...
- Gate 7 Unused research: recorded above / at ...
- Gate 8 Standout: recorded in Worth Your Attention.
```

Only after this block exists may the district be marked complete in the Plan's per-district checklist.
