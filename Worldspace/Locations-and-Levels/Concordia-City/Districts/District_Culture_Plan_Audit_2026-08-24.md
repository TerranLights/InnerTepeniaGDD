# District Culture Development Plan — Audit, 2026-08-24

**What this is.** A full verification pass over the 7/8-phase District Culture Development Plan as applied to
**Cancer** — comparing the discarded first-pass results (older formulation & synthesis methodology) against the
2026-08-16 from-scratch rewrite, and checking every load-bearing claim against its cited source. Run at the
developer's request; the question asked was literally *"make sure everything holds up correctly."*

**Why it was written down rather than just reported.** The developer switches from Claude Pro to the **Max5x
plan on Saturday 2026-08-29** (see `[[project_tier_switch_opus_2026_08_29]]`), moving from Sonnet to **Opus** —
a materially better model for worldbuilding and prose, where Sonnet is better suited to automated/mechanical
tasks. A **massive overhaul of the entire country, world, systems, and docs repo** is planned starting then.
This file exists so that overhaul starts from verified ground instead of re-deriving what was already checked,
and so the open items below are not silently lost in the transition.

**Scope note, stated honestly.** This audit covered Cancer specifically, plus the Plan-level and
`Phase_Instructions/` files Cancer depends on. **Taurus and Leo were not audited** — and per the Plan's own
progress tracker they have never been QA'd at all, and predate Phase 7, the research-first rule, and the
general-population discipline. Assume they carry the same classes of problem until checked.

---

## Part 1 — What holds up (verified; do not re-check on Saturday)

### The research is genuine and complete

All **8/8** of Cancer's `District-Inspirational-Influences.md` picks appear in the rewrite's research-basis
paragraph, at the concrete level the method demands — not gestured at from memory:

| Pick | Concrete detail actually used |
|---|---|
| Epidaurus | the abaton's two-part structure; enkoimesis; the *iamata* inscribed cure-stelai; body-part votives |
| Gardens by the Bay | Supertree structure (core / living planting skin / canopy); venting conservatory exhaust; rainwater capture |
| Findhorn Ecovillage | **Attunement** — the pre-task circle; sharing circles; "being over doing"; low-consumption home-made clothing |
| Père Lachaise | conditional-perpetuity concessions; the Aux Morts ossuary; **adoption** of abandoned monuments |
| Ospedale degli Innocenti | the foundling wheel; the *balie*; the *Balie e Bambini* ledgers; **split tokens** |
| Arcosanti | apse-form quarter-domes; the bronze **bell foundry**; rotating work assignments; the five-week newcomer workshop |
| Eden Project | built inside an exhausted 160-year china clay pit; linked geodesic biomes |
| Hundertwasserhaus | the **Window Right**; **tree tenants**; roof forestation; the 1958 Mouldiness Manifesto |

### The rewrite genuinely fixed the diagnosed failure

Verified by diffing the current file against the discarded first pass (commit **`3f0b5b8`**, "Complete all 7
District Culture Development Plan phases for Cancer"):

- **Old Finding VIII** was literally titled *"Architecture — formalizing what's already established, not
  inventing from scratch."* That is the re-labeling failure stated as an intention. The new VIII generates the
  apse vernacular, **the Window Reach**, the Growing Towers, and root tenants.
- **Old Finding IX** described itself as *"built from material already established … rather than invented
  fresh."* New IX adds **windbells** and the constant arm's-height foliage contact.
- **Old Finding X** asserted Cancer exports *"people and practice, not goods."* New X overturns this with cast
  windbells and rooted stock — and **explicitly announces the overturn** ("Research on Arcosanti and Gardens by
  the Bay overturns that") rather than silently rewriting canon. **This is the correct pattern and should be the
  house standard for the Saturday overhaul: when new work contradicts old work, say so in the text.**

### Gate 1's own mechanical check passes

Ran the checklist's grep verbatim against `Cancer_Full_Extrapolation.md` — any zero is a fail:

```
siligel 6 · cuisine 4 · music 13 · counterculture 5 · holiday 4 · human-robot 4
```

### Citations verified accurate

- **Diaspora arithmetic** — "Esperanza, Zukelli, and Cape Adare … together make up over half the district's
  outer diaspora": ~25% + ~16.7% + ~13% ≈ **55%**. All three confirmed destroyed in the source file. ✓
- **Fragmentation Matrix** — Cancer high-Grief with Taurus: `Fragmentation_Matrix.md:127` confirms they are the
  *only two* high-Grief districts. ✓
- **Armor set** — Sanctuary Warden Vest / Caretaker's Embrace Plating: confirmed in
  `District_Armor_Augmentations_and_Protection.md:64`. ✓
- **`Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Symbolic_Substrate/City_Symbol_Assignments.md` "contains no district entries"**: confirmed, zero matches. ✓
- **"Scorpio and Gemini, both confirmed Stage 2 Override destinations"**: confirmed — they are Override 1 and
  Override 2 in `City_Refugee_District_Affinities.md`. ✓
- **Middle-ring map position**: confirmed, Plan line 188. ✓
- **Cancer→Taurus 250-year pipeline**: confirmed across Deep Dive, Cross-Reference Synthesis, and History
  Enhancement files. ✓
- **Cancer/Scorpio sibling-district basis for the Swap Test**: confirmed, `01_Cancer_Deep_Dive.md:58`. ✓
- **Deep Dive "revised Finding B" (rare, not systemic)**: confirmed. ✓
- **Named institutions** — Threshold Waiting Rooms, Quiet Register, Paired Creches, Second Chair Workshops,
  Mother's Circuit, Communal Warm-Soak Houses, broth kitchens, Overcrowding Decision, Rationing of Grief: all
  grounded in `District_Canon_Reference.md` / `Cancer_Mega_Init.md`. ✓
- **Timeline** — Overcrowding Decision at c. 2813 sits correctly after the 2812 Long Night War, and the
  Mega-Init's "250 years in Cancer's future" from the 2564 founding lands in the same window. ✓
- **Demonym** — "Cancrian (proposed)" is consistent across all four Cancer files, and still openly undecided
  against "Cancerian." No contradiction; a standing open item, correctly flagged as such. ✓
- **Output-shape decision** — no `Local_District_Robot_Culture/` folder exists; the outer-city
  `Local_Robot_Culture/` precedent folder does. Finding XVII describes this accurately as still open. ✓

### Old Findings I–VII integrate cleanly with the new VIII–XXI

No contradictions found. The Green Ledger (I) is load-bearing across five new Findings; the Circuit House (VI)
is formalized in XVI; the Zhongshan-descended caregiver (V) recurs in XIV and XIX as the established
counter-case; the founding logic (III) drives XIV and XIX.

### The Plan's progress tracker matches reality

Phase 7 at 1/13 (Cancer), QA Completion Check at 1/13 (Cancer), Phase 8 at 3/13 first-pass-only — all
consistent with what is actually in the files.

---

## Part 2 — Issues found (open; these are the Saturday work items)

### Issue 1 & 2 — the Plan file and `Phase_Instructions/` carry stale phase-counts and stale status claims

> **✅ RESOLVED 2026-08-29 — verified 2026-08-31.** Both **Category A** (the 8 stale "7-phase" totals) and
> **Category D** (the 3 false status claims, D1-D3) were fixed on 2026-08-29, per an inline note now sitting
> in `Phase_Instructions/08_Phase_8_Robot_Specific_Culture.md`'s own §8: *"Corrected 2026-08-29; this section
> previously read 'None yet,' which was already false when written."* A fresh repo-wide sweep on 2026-08-31
> (`grep -rn -i "7[- ]phase\|seven[- ]phase\|all 7\|7 phases\|phases 1-7\|phase 1-7"` across this Plan and
> every `Phase_Instructions/` file) found **zero** remaining Category A instances, and every surviving
> "Phases 1-7" hit is a legitimate Category B/C prerequisite range or historical reference — including C1,
> which now carries exactly the inline guard comment this audit's own Part 4 recommended *("the count is
> correct here... do not 'correct' it to 8")*. **This audit's own record was simply never updated to say so
> — recorded here purely as a housekeeping correction, no further action needed on Category A or D.** The
> project has also moved substantially further than this audit's own snapshot: as of 2026-08-31, **12 of 13
> districts are complete and QA-passed** (Cancer, Taurus, Leo, Scorpio, Aries, Capricorn, Aquarius, Libra,
> Gemini, Pisces, Sagittarius, Virgo) — only the Hub remains, deliberately deferred by the developer. The
> Weekly To-Do's own tracking entry for this Plan was corrected to match in the same pass that added this
> note. **Categories E, and Issues 3-6 below, were NOT re-verified in this pass and may also be stale or
> already resolved — check before assuming they are still open.**

> **Original developer instruction, 2026-08-24, preserved for context: "do not fix these yet — flagged for a
> closer look together on Saturday."** That Saturday session is what resolved them, above.
> This section is written to be self-contained so that review needs no re-derivation. A full sweep was run
> (`grep -rn -i "7[- ]phase\|seven[- ]phase\|all 7\|7 phases\|phases 1-7\|phase 1-7"` across
> `District_Culture_Development_Plan.md` and `Phase_Instructions/`) and **every** hit is classified below. The
> sweep found more instances than the initial read did — including two in the Phase 8 instruction file that are
> a genuinely separate and arguably worse bug, and several that are **correct and must not be touched.**

#### Root cause — what actually happened

The plan originally had **seven** phases, with Robot-Specific Culture as Phase 7. On **2026-08-16** a full
re-audit against all 32 template sections found that the original tiering accounted for only 16 of them, and
that Cancer had cleared every phase while still having no Cuisine, no Music, no Arts, no Counterculture, no
Municipal Holidays, no district-level Human-Robot Relations, and zero occurrences of `siligel`. A new **Phase 7
— Native Culture** was inserted to close those, and **Robot-Specific Culture was renumbered 7 → 8.**

The Plan documents that renumbering correctly and explicitly at its own **lines 302-303**. What did not happen
is a sweep of everything downstream that had already hard-coded "7." The structural sections (Execution order,
Progress tracking, the follow-on heading) were updated; the **per-district checklist headers, two
`Phase_Instructions/` files, and the Phase 8 file's own status sections were not.**

This is an ordinary post-renumber cleanup miss, not a design problem. The danger is only that it misinforms —
which it already has: it propagated into commit messages ("Rewrite Cancer's **7-phase** culture pass from
scratch"), into the Weekly To-Do entry, and into how the plan gets referred to in conversation.

#### Category A — stale phase-count, safe to change (8 instances)

Each of these means *"all of the phases"* and is now numerically wrong.

| # | File | Line | Current text | Proposed |
|---|---|---|---|---|
| A1 | `District_Culture_Development_Plan.md` | 336 | `### 01 — Cancer — **ALL 7 PHASES COMPLETE — REWRITTEN FROM SCRATCH 2026-08-16**` | `ALL 8 PHASES COMPLETE` |
| A2 | `District_Culture_Development_Plan.md` | 352 | `### 02 — Taurus — **ALL 7 PHASES COMPLETE (2026-08-16)**` | `ALL 8 PHASES COMPLETE` |
| A3 | `District_Culture_Development_Plan.md` | 363 | `- Second district to complete the full 7-phase process.` | `full 8-phase process` |
| A4 | `District_Culture_Development_Plan.md` | 365 | `### 03 — Leo — **ALL 7 PHASES COMPLETE (2026-08-16)**` | `ALL 8 PHASES COMPLETE` |
| A5 | `District_Culture_Development_Plan.md` | 376 | `- Third district to complete the full 7-phase process.` | `full 8-phase process` |
| A6 | `District_Culture_Development_Plan.md` | 538 | `…explicitly gated on every district finishing all 7 phases first.` | `all 8 phases first` |
| A7 | `Phase_Instructions/00_Index.md` | 9 | `…the *what* and *in what order*: the 7-phase structure, the per-district checklist…` | `the 8-phase structure` |
| A8 | `Phase_Instructions/00b_General_Population_Discipline.md` | 3 | `This applies across all 7 phases, not just one…` | `across all 8 phases` |

**A6 is the sharpest single instance.** Its own section heading, three lines above at line 536, reads *"Planned
follow-on (after all 13 districts clear all **8** phases)"* — and the paragraph directly beneath it says *"all
**7** phases."* A reader cannot tell which is authoritative without going to the Execution order section.

**A7 matters disproportionately** because `00_Index.md` is the designated front door to the whole instruction
set, and its very first orienting statement about the Plan gives the wrong count.

#### Category B — **CORRECT AS WRITTEN. DO NOT CHANGE.** (6 instances)

These say *"Phases 1-7"* meaning **the seven phases that are prerequisites for Phase 8** — Phase 8 being the
capstone that draws on all of them. The number 7 here is not a stale total; it is a correct range. A
find-and-replace sweep would silently corrupt every one of these into nonsense ("Phases 1-8 must be complete
before starting Phase 8").

| # | File | Line | Text | Why it's right |
|---|---|---|---|---|
| B1 | `District_Culture_Development_Plan.md` | 547 | `…every district has a full Phase 1-7 foundation…` | Phase 8 is what's being triaged; 1-7 are its foundation |
| B2 | `Phase_Instructions/08_Phase_8_...md` | 8 | `Do not start this phase for a district until Phases 1-7 are done` | correct prerequisite range |
| B3 | `Phase_Instructions/08_Phase_8_...md` | 37 | `**Hard prerequisite: Phases 1-7 complete for the target district.**` | correct prerequisite range |
| B4 | `Phase_Instructions/08_Phase_8_...md` | 105 | `…Phases 1-7 are checked complete in …progress tracker.` | correct prerequisite range |
| B5 | `Phase_Instructions/08_Phase_8_...md` | 115 | `…does it fold into each district's own Full_Extrapolation.md like Phases 1-7?` | correct — contrasts Phase 8 against 1-7 |
| B6 | `Phase_Instructions/08_Phase_8_...md` | 123 | `Don't start this phase for a district whose Phases 1-7 aren't done.` | correct prerequisite range |

#### Category C — historically accurate. **DO NOT CHANGE.** (1 instance)

| # | File | Line | Text |
|---|---|---|---|
| C1 | `District_Culture_Development_Plan.md` | 14 | `Caught immediately after Cancer's full 7-phase pass: Cancer cleared every phase and **still had no Cuisine, no Music, no Arts…**` |

This sits inside the `⚠ RE-AUDIT, 2026-08-16` block. It is describing **the state of the world before Phase 7
existed** — when the plan genuinely did have seven phases and Cancer genuinely had cleared all seven while
still missing six template categories. **This sentence is the explanation for why the eighth phase exists at
all.** "Correcting" it to 8 would falsify the record and destroy the causal account of the renumber.

#### Category D — stale *status claims*, a separate and arguably worse bug (3 instances)

These are not counting errors. They are **factual assertions about project state that are now false**, in files
specifically written to orient a future session. This is the same class of problem as Issue 2's original
finding, and the sweep shows it is not confined to `00_Index.md`.

| # | File | Line(s) | Current claim | Reality |
|---|---|---|---|---|
| D1 | `Phase_Instructions/00_Index.md` | 62-66 | *"Phase 1 has one completed worked example (Cancer — Findings VIII-X)… **No other district/phase combination has been executed yet as of this writing.**"* | Cancer has all 8 phases **and** a passed QA gate; Taurus and Leo have all 8 phases each (un-QA'd). |
| D2 | `Phase_Instructions/08_Phase_8_...md` | 104 | *"**All 13 districts: blocked pending Phases 1-7.** Do not attempt Phase 8 for any district…"* | Cancer, Taurus, and Leo have **all completed Phase 8.** Not blocked. |
| D3 | `Phase_Instructions/08_Phase_8_...md` | 137 | Section titled **"8. Worked example"** — *"**None yet** — this phase is gated behind Phases 1-7 for every district, and **no district has cleared that gate** as of 2026-08-16."* | Cancer's Finding XVII **is** a completed Phase 8 worked example, and it passed the QA gate. Two more exist (Taurus XIV, Leo XIV). |

**D3 is the most actively harmful item in this entire audit.** A section explicitly headed "Worked example"
tells the reader none exists, when a QA-passed reference example is sitting one folder away in
`Cancer_Full_Extrapolation.md`. A Saturday session opening the Phase 8 instructions to start work on a new
district would conclude it was pioneering the phase from nothing — and would lose the benefit of the Swap Test
framing, the Inheritance/Iceberg tagging convention, and the honest-scope-note pattern that Cancer's pass
already established.

**D2 has a real operational consequence too:** it is phrased as a hard instruction ("Do not attempt Phase 8 for
any district"), so read literally it forbids exactly the work that has already been done three times.

#### Category E — minor pointer drift, needs a judgment call (1 instance)

| # | File | Line | Issue |
|---|---|---|---|
| E1 | `Phase_Instructions/01_Phase_1_Lived-in_Texture.md` | 27 | Points the reader to *"the head of its **Phase 1-7 block** in `Cancer_Full_Extrapolation.md`"* as the research-summary format to follow. The actual heading in Cancer's file reads **`## District Culture Development Plan — Phases 1-8`**. The named block does not exist under that name. |

Ambiguous: it may mean "the block covering Phases 1-7" (stale) or be a loose reference to the whole block
(should read 1-8). Low stakes; decide alongside A7/A8 since it's the same family of pointer.

#### Why this is worth doing carefully rather than with a bulk replace

**19 items are classified above: 18 of them are grep hits** for "7-phase"-family strings across these files,
plus **D1**, which the grep does *not* catch (its Status text contains no phase-count string at all — it was
found by reading the section). Of the 19: **8 must change (A)**, **7 must not (B1-B6, C1)**, **3 are a different
bug entirely (D)**, and **1 needs a decision (E)**.

A naive find-and-replace would break the Phase 8 prerequisite logic in six places and falsify the historical
re-audit note — while still missing D1 entirely, since that one contains no number to match on. **The Category
B and C entries are the reason this is a review item rather than a one-line sed command; D1 is the reason a
grep alone was not sufficient to find the problem.**

#### Suggested handling on Saturday

1. Apply **A1-A8** — mechanical, no judgment needed.
2. Rewrite **D1, D2, D3** to reflect real state. D3 should point at Cancer's Finding XVII as the worked example
   and note the QA pass; D2 should list Cancer/Taurus/Leo as done and the remaining 10 as blocked.
3. Decide **E1**.
4. Leave **B1-B6 and C1 untouched**, and consider adding a short inline comment at C1 noting it deliberately
   refers to the pre-renumber state, so a future reader doesn't "fix" it.
5. **Consider a standing convention** to prevent recurrence: phrase prerequisite ranges as "all prior phases"
   rather than a hard-coded range, and keep per-district completion headers free of a phase count entirely
   (they already list each phase individually, so the count is redundant and only creates drift).

### Issue 3 — Finding XII's palette citation is unsupported · **needs a judgment call**

`Cancer_Full_Extrapolation.md` lines 283-284:

> **Palette.** Warm, soft, low-saturation — greens, unbleached naturals, and the warm tones Mawson-descended
> households favour district-wide (`District_Refugee_Diaspora_Composition.md`).

`District_Refugee_Diaspora_Composition.md` contains **zero** colour/palette/warm-tone content anywhere — grep
for `warm tone|palette|colour|color` returns nothing. The Mawson→Cancer entry covers the First Walk, the
Welcome Plaza and Welcome Feast, and the Unbroken Watch; nothing aesthetic. The claim also sits in mild tension
with the Mega-Init's established **"white-and-green palette"** (`Cancer_Mega_Init.md:36`).

**Two clean resolutions, pick one:** (a) drop the false citation and keep the palette as an honest new
proposal, reconciled explicitly against the established white-and-green; or (b) actually ground a Mawson colour
preference in the diaspora file first, then cite it.

### Issue 4 — `Cancer/README.md` is a stale compilation · **needs a decision**

Its own header: *"Cancer — Complete Megasheet. The full, concatenated Cancer reference — synthesis, then
extrapolation, then cross-reference … **Compiled 2026-07-09**."*

It contains Findings I–VII and **none** of Findings VIII–XXI. Grep for `window reach|windbell|perpetual
pot|attunement|keeping` → **0 hits**. The file that advertises itself as the complete reference is missing
roughly 90% of the district's cultural content.

**Decision needed:** are these `README.md` files meant to be periodically recompiled from their three source
files, or were they one-time snapshots? If the former, all 13 need regenerating after their phase passes — a
natural batch job for the overhaul. If the latter, the header wording should stop claiming completeness.

### Issue 5 — Minor structural / cosmetic

- **Non-monotonic Finding order.** Finding XVII is Phase 8; Findings XVIII–XX are Phase 7. Phase 8 physically
  precedes Phase 7 because Phase 7 was written later and appended. Consistent with the Plan's stated
  append-don't-reorder convention, but it reads oddly, and the Plan's own checklist lists them out of order to
  match. Leave as-is or reorder deliberately — but decide, don't drift.
- **Stray double `---`** at `Cancer_Full_Extrapolation.md` lines 536-537.

### Issue 6 — Worth a deliberate confirm, not an error

Finding II and `Cancer_Mega_Init.md:36` both hold that the ambient haze is *"not a deliberate engineering
choice, just an ambient, unremarked quality of the air itself."* Finding VIII now sources it to the Growing
Towers' venting — engineered infrastructure. **These reconcile** (nobody engineered *the haze*; it is a
byproduct of towers built for hydroponics and air handling), and Finding VIII is honest that it is supplying a
mechanism rather than overwriting Finding II. But it does move the haze from unexplained ambience to
infrastructure exhaust. Confirm that shift is wanted rather than assuming it is seamless.

---

## Part 3 — Carried-forward open items already flagged inside Cancer's own file

Not defects — genuine open questions the pass correctly declined to resolve. Listed here so they are not lost:

1. **The Rationing of Grief question** (Finding X) — whether Libra capping Cancer's bereavement-care timelines
   was partly a reaction to Cancer's care model becoming influential *outside* its borders. Explicitly deferred
   to Libra's own Phase 1 pass.
2. **Demonym** — Cancrian vs Cancerian, still undecided across all four files.
3. **The Ofrenda's eventual owner** (Finding XI) — flagged as a strong candidate for a Phase 6 role-placeholder
   or for whichever doll becomes Cancer's anchor companion. **Cancer has no confirmed anchor doll** (per
   `District_Source_Index.md`).
4. **Robot Elementals / solar symbols** (Finding XVII) — whether Concordia's districts participate in that
   system at all is unconfirmed; `city-symbol-pairs.md` has no district entries. Deliberately unresolved,
   flagged for whoever owns that system.
5. **Phase 8 output shape** (Finding XVII) — folded into `Full_Extrapolation.md` vs a dedicated
   `Local_District_Robot_Culture/` folder, as the outer cities did. Flagged as needing settling **before Phase
   8 scales past the early worked examples** — i.e. this should be decided early in the overhaul, not late.
6. **The full Robot Universals triage** — gated on all 13 districts clearing all 8 phases; Cancer's Phase 8 was
   run without loading the complete reference text and says so honestly.

---

## Part 4 — Recommended sequencing for the Saturday overhaul

1. **Work Issue 1&2's Category D first — before anything else.** D1/D2/D3 are false statements about project
   state sitting in the files a new session opens to orient itself. D3 in particular tells a reader that no
   Phase 8 worked example exists when a QA-passed one does. Everything else in this list is easier once the
   instruction set stops misdescribing reality.
2. **Then Category A (A1-A8)** — mechanical phase-count corrections, no judgment needed. **Do this by hand, not
   with a bulk replace** — Categories B and C contain seven correct "Phases 1-7" strings that a sweep would
   corrupt. See that section's own warning.
3. **Decide Categories E, plus Issues 3 and 4** — four small judgment calls: the Phase-1 pointer wording, the
   unsupported palette citation, whether district `README.md` files are meant to be recompiled, and the
   cosmetic items in Issue 5.
4. **Settle the Phase 8 output-shape question** (Part 3, item 5) — folded into `Full_Extrapolation.md` vs a
   dedicated `Local_District_Robot_Culture/` folder. Finding XVII explicitly warns this should be settled
   **before Phase 8 scales past the early worked examples**, and there are already three.
5. **Audit Taurus and Leo against this same checklist before extending the plan to new districts.** Both are
   marked complete but have never passed the QA gate, and both predate Phase 7, the research-first rule, and
   the general-population discipline. The Plan itself already says so at line 527; this audit is the template
   for what checking them actually looks like.
6. **Only then** run Phase 1 across the remaining 10 districts.

**Standard worth carrying into the overhaul generally:** the single best thing the Cancer rewrite does is
Finding X's explicit announcement that it overturns prior canon. New work that contradicts old work should say
so in the text, with the reason. That habit is what made this audit possible at all.

---

## Part 5 — This file's other job: input to the universal methodology build

**Added 2026-08-24, per developer instruction.** A second, larger Saturday deliverable is planned alongside the
fixes above: **generalizing the cultural synthesis methodology into a universal, repeatable instruction set**
usable for any Concordia district, any of the 35 outer cities, DLC locations, and possibly
orbital-infrastructure settlements. Full brief in `Dev-Road-Map/Weekly_To-Do_-_Current.md`.

**Why this audit matters to that build.** Cancer is the intended source example to generalize *from* — so the
generalization is only as sound as Cancer actually is. That is what Part 1 establishes: the research is real
(8/8 picks), the citations check out, the Findings are internally consistent, and the rewrite genuinely fixed
the failure it diagnosed. **Cancer is safe to treat as the reference standard.**

**Three things this audit surfaced that should feed the general instruction set directly:**

1. **The re-labeling failure mode, and its tell.** The discarded first pass announced itself in its own section
   title — *"formalizing what's already established, not inventing from scratch."* That phrasing is a reliable
   warning sign, and the general methodology should name it explicitly as a checkable failure mode: if a pass
   describes itself as consolidating, formalizing, or naming what already exists, it has probably not generated
   anything.
2. **Overturn-announcement as a house rule.** Finding X explicitly states that new research overturned a prior
   assumption, and why. Without that sentence this audit could not have distinguished a deliberate canon change
   from a contradiction. Make it a required element wherever a pass contradicts earlier material.
3. **Post-renumber / post-restructure sweeps are their own failure mode.** Issue 1&2 above is not a content
   problem at all — it is what happens when a structure changes and the downstream references are not swept.
   Any methodology that has phases, numbered stages, or per-location checklists will hit this. Worth building
   an explicit "structure changed → sweep downstream references, and classify each hit before changing it"
   step into the general instruction set, with the Category A/B/C/D breakdown above as the worked example of
   why blind replacement is unsafe.
