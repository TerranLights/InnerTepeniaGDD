# The Universal Location Methodology

**Working draft, written 2026-08-30. Not final, and expected to change under pressure-testing.**

**What this is.** A procedure for developing **any location of any kind, at any scale** — a district, a city, a
subnet, a nation, an orbital station, a highway, a single structure, a ruin, a natural feature, a stretch of
network. It is the cognate of the eight-phase district methodology in
`../Concordia-City/Districts/Phase_Instructions/`, generalized to the whole space of locations rather than to
Concordia's thirteen districts.

**The name is not invented here.** Two files in the district folder already refer to "the universal location
methodology" as a thing that ought to exist and pre-assign material to it:

- `00f_Review_Panel.md` §9: the Review Panel roster *"is one of the few instruments in this folder already fit
  for the universal location methodology, and it should be carried there rather than rebuilt."*
- `00f_Review_Panel.md` §4d: the Moore & Gillette four-faculty test for whether an invented civilization is
  complete *"should be picked up by the universal location methodology rather than here."*
- `00d_Shadow_Proportion_Discipline.md` opens by declaring itself *"binding for every phase, every district,
  and for any location methodology derived from this one."*

This folder is that methodology. Those three assignments are honored rather than re-derived.

---

## Status, honestly stated

**This is a derivation, not a validated procedure.** The district methodology earned its rules across thirteen
districts and roughly fifteen recorded failures; every discipline in it is attached to a specific pass that went
wrong. **This file has none of that.** It is reasoned from the district methodology's structure, from the
32-section city template, from the existing symbol systems, and from the real range of location types in this
project — but it has not yet been run on anything.

**Expect it to be wrong in ways that will only appear under use.** The plan is to pressure-test it against real
Tepenian locations and revise. Anything below that survives contact should be marked as having survived, with
the location it survived on named; anything that fails should be corrected here in the same commit, per the
same standing rule the district runbook uses.

**What it is *not*:** it is not a replacement for the district methodology. Concordia's thirteen districts have
a working, evidence-backed procedure and should keep using it. This exists for everywhere else, and for the
eventual case where a district pass wants something the district procedure has no slot for.

---

## The four findings that forced the generalization to be more than a rename

Recorded up front because they are the substantive results of the derivation, and because each one is a place
where the universal methodology **must differ** from the district methodology rather than merely restating it.

**1. The eight district phases cover roughly half of the 32-section city template.** They were built to close
*specific measured gaps in Concordia's districts* — categories that scored 0/13 or 2/13 — not to be a complete
location instrument. Sections the district phases never inherited include Founding Story, Climate Character,
Seasonal Rhythms, Social Contract, Who This Place Attracts, Language, Division of Industry, Political Character,
Relationship to Other Cities, Significant Events, and Diaspora Character. **A universal spine has to cover the
whole space, and the eight phases are correctly understood as its culture-depth subset rather than as its
skeleton.**

> **Verified, not asserted — 2026-08-30**, per this methodology's own Gate 1 discipline. Scanned all eight
> district phase files for ten of the claimed-absent section names. **Proof-of-hit run first** (`architect`
> returns three files, so the scan works). **Eight of ten score zero.** The two non-zero results were inspected
> individually rather than trusted: **`climate`** returns one hit, and it is a line stating that Concordia's
> climate is *uniform across districts* — which confirms the claim rather than contradicting it;
> **`language`** returns three, and **all three mean *wording*** (*"Vision Notes language,"* *"religious-register
> language"*), not language as a cultural category. **Count of genuine coverage: 0/10.** Full section tally:
> ~18 of 32 covered, 14 absent.



**2. The relational hole is inherited from a deletion, not an oversight.** `00e` §6 records that no district
phase covers inter-district relationships, with measured consequences (Taurus's file mentions its own opposite
district zero times). **The city template it was translated from has that section — §23, "Relationship to Other
Cities."** It was present at city scale and dropped at district scale. So the fix is not to invent a relational
phase; it is to **restore one that already existed**, and to place it early enough that it cannot be dropped
again. It is Phase 5 here, in the middle of the spine, for exactly that reason.

**3. The primary generator is not portable, and its replacement is stronger than a fallback.** The district
capability reading depends on the zodiac dignity row — a rich, externally-given, four-term structure with
meaningful absences and built-in cross-relations. **Almost no other location in this project has one.** The
35 outer cities have a Planet + Element pair that is *thin* by comparison (dual-valence, no absences, no
documented cross-relations). Highways, orbital stations and ruins have none at all.
**But physical and environmental constraint is a first-class generator in its own right, and in one respect a
better one:** the zodiac is non-negotiable by convention, while an ice sheet is non-negotiable in fact.
`02_Generators_Capability_and_Symbols.md` treats generator selection as a real step with a ranked stack, and
requires **three independent generators run in parallel** so that the conflicts between them can be mined —
which the single-generator district procedure structurally cannot do.

**4. The capability frame needs two quadrants the zodiac never supplied.** The dignity row is two poles at two
grades — what a place is good at, what it is bad at. **It never asks what a place must keep paying to continue
existing, or what it permits but punishes.** In a setting where every location is a hostile-environment
settlement, "what does this place have to do continuously or stop being a place" is not a minor addition. The
universal frame is four quadrants — **Strength, Deficit, Standing Cost, Grudging Tolerance** — and the two new
ones are where a great deal of this setting's character actually lives.

---

## Contents

| File | What it is |
|---|---|
| **`00_RUNBOOK.md`** | **the procedure — start here** |
| `01_Frame_Typology_and_Inheritance.md` | location types, scale bands, inhabitation status, temporal frame, and the nesting/inheritance protocol |
| `02_Generators_Capability_and_Symbols.md` | the generator stack, the four-quadrant capability frame and its shapes, and the open symbol-binding protocol |
| `03_The_Phase_Spine.md` | the eleven phases, in detail |
| `04_QA_Gates_and_Differentiation.md` | the generalized gates and the sibling-differentiation instrument |
| `05_The_Input_Contract.md` | **what must be supplied vs. what the method produces** — all eight generators are inputs |

## What this folder deliberately does not duplicate

These already exist, are already general, and are referenced rather than rebuilt:

| File | Why it is not duplicated here |
|---|---|
| `../Cultural_Synthesis_Techniques.md` | Already explicitly general-scope — *"Concordia districts, the 35 outer Tepenian cities, DLC locations, or a location in any future project."* It supplies the **operations**; this folder supplies the **procedure**. Sixteen techniques, each with a divergence table. |
| `../Real-World_Basis_Extrapolation_Method.md` | The research method. Already cross-scale. |
| `../Concordia-City/Districts/Phase_Instructions/00f_Review_Panel.md` | Explicitly stated to carry unchanged to *"a surface city, a nation, an orbital settlement, a station, or a ship — and in a novel or a film as readily as in a game."* Only the casting changes. |
| `.../00d_Shadow_Proportion_Discipline.md` | Explicitly binding on any derived methodology. |
| `.../00b_General_Population_Discipline.md` | Universal in substance — but see `01`, because it **inverts below roughly thirty people** and that limit was never stated. |

## Pressure-testing — pick the cases that would break it, not the ones that would confirm it

**The district folder's sharpest self-criticism is that eighteen consecutive prediction confirmations came from
a self-grader**, and that the two available remedies — run the case chosen *because* it looks least likely to
conform, and **state in advance what would falsify each rule** — had been flagged for three rounds without
either being applied.

**So this methodology should not be first tested on a mid-sized settlement, which is the case it was designed
around and cannot fail.** Ranked by how hard each would stress a *different* load-bearing assumption:

| Test candidate | What it would falsify |
|---|---|
| **A highway** *(e.g. Hwy 37, or the Marambio–Rothera segment)* | **Corridor type, Band 0 population against Band 5 extent.** If the phase spine produces a thin result here, the type-variance matrix in `03` §0.1 is decorative rather than functional. |
| **Amundsen Tower** | **Structure + ruined.** Tests the Band 0 substitutions and whether The Surviving Witness genuinely carries a pass on its own. Also the only case where "in its own past" is unambiguously where the remedy lives. |
| **A single orbital station** | **The enclosed/orbital modifiers, and a location with no siblings** — so all four no-sibling substitutes get exercised at once. |
| **Concordia's Hub (Axis Mundi)** | **The Interstitial procedure** (`01` §1.3). The district methodology returns *nothing* here — no capability row at all — so if `01` §1.3 also returns nothing, the type is a label rather than a procedure. **This is the single best falsification case available**, and the district folder independently identified the Hub as its own designated falsifier. |
| **The Tepenian Federation** | **Band 6.** Tests whether the delegate/distribution machinery works or whether the pass silently reverts to writing a very large town. |
| **A 12-person research station** | **Band 1 and the general-population inversion.** If the pass invents a general population anyway, `01` §2.3 has not actually changed behavior. |

**And state the falsification condition before each run, not after.** For each of the four new gates and the
four-quadrant frame: *what observation would show this does not work?* That question has never been asked in
this project's methodology work, and asking it once is worth more than another six confirmations.

## The rule that governs everything here

Carried unchanged from `../Cultural_Synthesis_Techniques.md`, because it is the reason any of this exists:

> **Never carry one location's answers into another. If two places produce similar-shaped answers to the same
> technique, at least one of them is wrong.**

And **LAW 0 — depth over speed** applies here exactly as it does in the district runbook, and is restated in
full at the head of `00_RUNBOOK.md` rather than cross-referenced, because a procedure that cites its governing
law instead of stating it will be run without it.
