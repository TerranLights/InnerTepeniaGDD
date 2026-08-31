# Observations & Methodology Findings — Tri-Cities Test Run

**Test run 1 of the Universal Location Methodology. Started 2026-08-30.**
**Subjects:** Zhongshan · Sinheung · Shirayuki *(the Larsemann Hills cluster, Mirny subnet)*.

> **This file is the point of the exercise.** The three city passes are the *material*; this file is the
> *instrument reading*. Everything here exists so the next run is cleaner, faster, and less wrong — recorded as
> it happened, including the mistakes, because a methodology that only records its successes is the exact
> self-flattering-audit failure this project has measured four times.

**Nothing in this folder is canon. Nothing here has been written to the official city files.** This is a
sandboxed test at the developer's explicit direction.

---

# 0. Why this was a good first test — and why it was nearly a bad one

**The runbook's own pressure-test list recommended starting with the Hub (Interstitial) or a highway
(Corridor)** — cases chosen to break the method. The developer chose the Tri-Cities instead, and **that turned
out to stress a different and arguably more dangerous axis.**

**These three cities are the hardest possible differentiation case in the project:**

- They sit within **8 km** of each other *(Zhongshan and Sinheung a few hundred meters apart)*
- **Identical** climate, identical ice-free-oasis terrain, identical Prydz Bay access
- **One** shared airport, **one** shared highway tri-junction
- **The same founding mechanism** — a single three-way Jeju-do partition
- **The same three national populations**, each Primary in one city and Significant in the other two
- **Identical war status**, resolved together *because* differing fates made no physical sense
- **An identical eventual endpoint** — legal unification into one city

**They are a designed convergence.** The methodology's governing rule is *never carry one location's answers
into another* — and here canon has already carried nearly every input into all three. **If the method can
separate these, the anti-convergence machinery works. If it cannot, the machinery is decorative.**

**The near-miss:** this same property makes the run **maximally vulnerable to circularity** (§1 below), and a
naive pass would have produced a confident, coherent, worthless result.

---

# 1. ⚠ THE CIRCULARITY PROBLEM — the single most important finding so far

**`05` §6.1 says an input must not be derived from the methodology's own output for the same location. That
rule is too narrow, and this run found the gap.**

These three cities already carry **~12,000 lines** of existing canon each-cluster-wide, including:

- full 32-section Cultural Spec Sheets per city
- per-city Enneagram personality reads
- a **`Tri-Cities_Overlap_and_Distinguishing_Guide.md`** — a purpose-built differentiation instrument with
  seven overlaps already analyzed

**None of that is *this methodology's* output — so `05` §6.1 does not technically forbid feeding it in. But
feeding it in would be exactly the same defect.** Reading Zhongshan's completed culture file and then
"deriving" Zhongshan's culture is the district folder's *"planting your own seed and then finding it,"*
one level up.

### The rule this run proposes

> **PROPOSED — generalize the circularity rule from *provenance* to *kind*.**
> An input must not be **a prior culture-pass conclusion about the same location**, regardless of which
> methodology produced it. **Canon supplies inputs; canon does not supply conclusions.**
>
> **The operational split, which turns out to be clean and easy to apply:**
> - **ADMISSIBLE as input** — physical facts · founding mechanism · function/industry · network position ·
>   census and composition · symbol assignment · dated events. *(These are G1–G8. They are attributes.)*
> - **INADMISSIBLE as input** — "the city's character is X" · "its temperament reads as Y" · any prior pass's
>   capability, personality, or culture *conclusion*. **These may be checked against at the END, never
>   consulted at the start.**

### The test protocol this produces — and it is falsifiable

**Because the inadmissible material exists and is extensive, this run has a rare luxury: a control.** The
measure of whether the methodology did anything is not "is the output plausible" but:

> **Did the pass produce findings that the existing ~12,000 lines do not contain?**

**That is checkable by scan, and this file records each check.** A methodology that only reproduces what is
already written has failed even if every sentence is true.

**Recommendation for `05`:** add this as a standing §6.3, and add "prior culture-pass conclusions about this
same location" to the RESERVED-adjacent list of things a pass reads *last*, not first.

---

# 2. Self-corrections made during the run

**Recorded because the developer asked for them specifically, and because the pattern matters more than the
individual errors.** Every one of these was caught by a mechanism the methodology already mandates.

## 2.1 A false "canon never noticed this" claim — caught by the mandatory verification scan

**What happened.** On finding that Sinheung and Shirayuki share the planet Uranus, I wrote that canon had never
noticed. **Then ran the verification scan the methodology requires, and it was false** —
`Local_Robot_Culture/Mirny_Subnet/Shirayuki.md:271` already records: *"Shirayuki and Sinheung actually share
the same Solar symbol (Uranus), differentiated by Element only,"* dated 2026-08-10.

**Why it matters.** This is the project's documented failure direction — **self-audit error has run toward
flattering the pass on every occasion it has been measured.** I was one unverified sentence from adding a
fifth instance, and the claim would have been *more* attractive than the truth, which is exactly why it needed
checking.

**What survived the correction, and it is sharper than the false version:** the collision **is** recorded — in
one city's robot-culture file — but the **Overlap & Distinguishing Guide contains zero mentions of symbols,
planets, or elements** *(verified: `grep -c` = 0)*. **Canon noticed and never propagated the finding to the
one file whose entire job is keeping these three cities apart.**

> **Methodology lesson — PROPOSED addition to Gate 6 / `04` Part III:**
> **"Noticed somewhere" and "available where it is needed" are different states.** When a differentiation
> instrument exists for a sibling set, check whether findings recorded elsewhere have actually reached it.
> **A finding recorded in a file nobody consults during differentiation is not doing differentiation work.**

## 2.2 Assuming a symbol's meaning instead of reading it — caught by `02` §6.2

**What happened.** I read "Zhongshan = Saturn + Metal" and began building on the *traditional astrological*
Saturn — structure, limit, discipline, time. **The project's Saturn is not that at all:**

> **Saturn — one word: *Mystery*. "Doesn't care to be fully known."** Positive: *beauty built from fragments
> rather than requiring wholeness.* **Negative: *"held together only loosely — a structure with no actual
> cohesion, one disruption away from simply dispersing. Impressive from a distance, insubstantial up close."***

It is derived from **real Saturn facts** — the rings are debris, not solid; it is the least dense planet and
would float. **The entire Zhongshan reading inverted once I actually opened the file.**

> **Methodology lesson — PROPOSED, and it is cheap:** `02` §6 should state explicitly that **a registered
> symbol system's members must be read from the file, never from cultural familiarity with the symbol's
> name.** This project's planetary symbols are derived from *astronomy*, not astrology, and several will
> actively mislead a reader who assumes the traditional meaning. **Saturn is the worked example.**

## 2.3 A silent off-by-one that produced confident wrong numbers — caught only by a spot-check

**What happened.** Parsing the census tables, I indexed `c[3]` as the Humans column. **`c[3]` is the Subnet
column.** The first run therefore reported **robot-only** retention while labelling it "combined." **It did not
error.** It produced 33 plausible rows, a sensible mean, and a sensible spread — all wrong.

**What caught it:** a hand-computed spot-check of one city against the source table, and nothing else. Four
successive attempts to fix it by reasoning about the code failed; **the fix came from dumping the raw line and
printing the actual cells.**

> **Methodology lesson — PROPOSED promotion.** `00_RUNBOOK.md` Step 7 already says *"verify the instrument
> before trusting any zero."* **This run shows the rule is too narrow in two ways:**
> 1. **It is not only about zeros.** A wrong-column parse returns *plausible non-zero numbers*, which is
>    strictly more dangerous than a zero, because a zero prompts suspicion and a plausible number does not.
> 2. **Verification must be a spot-check against the source, not a re-reading of the logic.** I re-read the
>    logic four times and could not see it.
>
> **Proposed wording: "Before trusting any computed figure, verify one row by hand against the source. Do this
> for plausible numbers especially — a wrong result that looks right is the one that survives."**

## 2.4 An attractive finding killed by its own arithmetic — the method working correctly

**What happened.** The census split humans from robots, and the three cities showed different human-vs-robot
retention gaps *(Zhongshan +9.4pp, Sinheung +2.5pp, Shirayuki −6.9pp)*. **This looked like a superb Phase 9
finding** — three cities where robots and humans leave at different rates.

**Then I computed it against all 33 cities.** National mean gap is **−1.3pp with sd 13.1**, putting the three
at **z = +0.82, +0.29, −0.42.** **All three are unremarkable.** Sayowa is +30.8pp; Cape Adare and Signy are
−25.6pp. The Tri-Cities differential is noise.

**Recorded as a success, not a failure.** The finding was dropped. **This is the single most valuable thing
that happened in the run so far**, because the finding was interesting, thematically perfect, and false — and
only the comparison against the full population caught it.

> **Methodology lesson — PROPOSED, and this may be the most portable rule the run produces:**
> **Any quantitative differentiator must be scored against the full sibling set before it is used, not just
> against the immediate comparison group.** Three cities differing from *each other* says nothing until you
> know how much cities differ *in general*. **Report the z-score, not the difference.**
> **Without this, any three locations will appear to differ meaningfully on any metric.**

## 2.5 A second over-claim, caught by the same scan discipline — and canon had a better line

**What happened.** Phase 5's Finding R-1 originally claimed as new the observation that Sinheung needs to be
seen while Zhongshan refuses to look. **The verification scan found canon already carries the contrast in three
places**, and one of them is better than what I wrote: Sinheung's own sheet says its people prefer a city that
*"wears its ambition openly **rather than performing quiet superiority the way Zhongshan does next door**."*

**Canon has *Sinheung's reading of Zhongshan* — as superiority.** My draft had Sinheung reading it as
ordinary quiet, which is flatter and less true.

**What survived, revised:** canon states the opposition as **temperament**; the capability frame states it as a
**supply relationship that cannot complete** — and the misattribution of motive *(Sinheung reads structural
preoccupation as contempt)* is the part canon does not have.

> **Pattern worth naming, now that it has happened twice in one run:** **both of my false-novelty claims were
> about the *most interesting* findings.** The pull toward "canon has never noticed this" is strongest exactly
> where the finding is most attractive. **Treat any "this is new" claim about a headline finding as
> presumptively false until scanned.**

## 2.6 Building the whole run on an exceptional configuration — caught by the developer, not by me

**What happened.** The run was structured as a **simultaneous three-location co-write**, and every headline
finding depends on that. **I did not notice this was exceptional** until the developer stated the
architectural rule: *the methodology's fundamental unit is one location, start to finish; multi-location is a
possible extra, never the base structure.*

**Why it was not caught internally.** `01` §5.3 *permits* co-writing a small set, so nothing in the procedure
flagged it. **The methodology has no check that asks whether the configuration being run is representative** —
and the first-ever test was run on the single least representative location set in the project.

> **This is the district folder's recorded failure repeating in a new costume.** The README's own criticism is
> that *"eighteen consecutive prediction confirmations came from a self-grader,"* with the unapplied remedy
> being **to run the case chosen because it looks least likely to conform.** I ran the case most likely to
> conform and was about to report the confirmation.
>
> **PROPOSED — a new pre-flight line, and it is cheap:**
> ***"Is this location's configuration typical, or exceptional? If exceptional, say in what way, and say which
> findings depend on the exceptional property."*** A pass cannot correct for a bias it has not declared.

**Full analysis in `03_Generalizing_Back_to_the_Base_Methodology.md`, which is now the run's primary
deliverable.**

---

# 3. Findings about the METHODOLOGY

## 3.1 What has already earned its keep

**The declaration block caught a real frame error before any content was written** *(`01` §4, §6)*. "Run the
methodology on the three Tri-Cities" is **ambiguous**, and the ambiguity is load-bearing:

- **Pre-~2688:** three legally separate cities → three Settlement passes, sibling set of 3
- **~2688–2780s:** one continuous urban area, three legal cities
- **Post-~2780s:** **one** city; the three become **sub-districts** → *one* pass, with three children
- **Present (~2822–27):** unified, war-damaged, and — per the census note — **no Census III exists**, so there
  is no authoritative present-day population at all

**Type, band, parent, sibling set, and children all change across that boundary.** A pass that had not filled
the declaration block would have written a hedged document coherent at no point on the timeline — which is
exactly the failure `01` §4 rule 2 names.

**Resolution adopted:** this run writes the **pre-unification frame, three separate cities**, matching the
existing outer-city convention and the developer's stated sequencing *(finish the three individual identities
first)*. **The post-unification pass is a genuinely different document and is logged as a REQUESTED output.**

## 3.2 The pairing-relation typology (`02` §6.3) works, and produced the run's first real finding

**The Planet+Element system is THIN on both sides and only becomes structured through the pairing.** Applied:

| City | Pair | Relation | What falls out |
|---|---|---|---|
| **Zhongshan** | Saturn *(mystery, no cohesion, insubstantial up close)* + Metal *(precision, integrity, refinement, **grief**)* | **IRONIC** | Metal promises an integrated, refined core; **Saturn says the thing that looks refined is fragments with no cohesion.** "Impressive from a distance, insubstantial up close" |
| **Sinheung** | Uranus *(anomaly, outsider)* + Electricity *(animation, the spark, "makes matter conscious")* | **REINFORCING** | Doubled with no counterweight → per §6.3, ask **what it cannot moderate.** Answer: its need to be seen |
| **Shirayuki** | Uranus *(anomaly, outsider)* + Fire *(warmth, charisma, "the courage to be seen")* | **TENSIONED** | Outlier-ness pulls away; warmth pulls toward. **An outlier people are drawn to rather than repelled by** |

**The finding the typology produced that neither symbol alone could, and that canon does not contain:**

> **Sinheung and Shirayuki share Uranus — so both are outliers. Their Elements decide *what kind*.**
> **Sinheung's outlier status must be asserted** (Electricity reinforces the anomaly — louder, more visible,
> never settled). **Shirayuki's outlier status is attractive** (Fire converts difference into draw).
> **The same symbol, at two different stages of the same process:** Uranus's own positive reading is *"an
> identity built after a defining event — reorientation as the new baseline rather than damage waiting to be
> corrected."* **Shirayuki has completed that reorientation. Sinheung is still treating its founding as damage
> to be corrected, and that is why it must keep proving its claim.**

**Canon's own note says the two are *"differentiated by Element only."* The methodology says something stronger
and more useful: they are differentiated by *where each one is in the same process.*** That is a genuine
value-add over the existing material, produced at Step 2, before any research.

## 3.3 The "in its own past" deficit address (`02` §4.1) fired on its first real case

**`02` §4.1 added this address type with an explicit note that the district set *could not* generate it** —
thirteen districts of uniform age and stable institutional history. **Shirayuki produced it immediately**
(see §4.2 below). **The newest and least-tested piece of apparatus in the file worked on the first location
that could exercise it.**

## 3.4 The Tier 3 "optional particulars" pull/push distinction paid off immediately — in a way not anticipated

**The developer added "someone who came" to `05` §2.4 on 2026-08-30, hours before this run**, correcting a
first draft that only asked what drives people out. **Shirayuki was the worked example used to justify it.**

**This run found that the correction is worth more than the argument made for it.** The reasoning at the time
was that attraction is as informative as repulsion. **The stronger fact is that *pull is reversible in a way
push is not*** — and it is measurable *(§4.2)*. **A pass that only asked what attracts people to Shirayuki
would have described its strength and missed that the same property is its largest structural vulnerability.**

> **PROPOSED addition to `05` §2.4's arrival-pair note:** *"Pull and push differ in durability, not only in
> direction. A population assembled by attraction has already demonstrated willingness to relocate, and will
> demonstrate it again when a better attractor appears. Ask of any pull city: **what happens to it when
> somewhere more attractive opens?**"*

## 3.5 Where the methodology was slow or clumsy

- **Canon volume defeats Step 0.4 as written.** *"Read everything the location already has, before writing over
  it"* is **~12,000 lines for this cluster**, and that is before the universe repo. The step needs a triage
  order. **Proposed:** specs → symbol assignment → composition/census → differentiation instrument →
  *then* culture files **last** (and per §1, as a check rather than an input).
- **`graphify` performed well here, contrary to the CLAUDE.md warning.** One query returned the amalgamation
  node, both Tri-Cities files, and the correct cluster membership. **The prose-retrieval limitation appears to
  affect large consolidated book-extraction files, not location canon.** Worth narrowing the CLAUDE.md caveat.
- **The four-question canon check is cheap and should be run earlier than Phase 0.** Question 1 *(does canon
  already answer this?)* is the whole of §1's problem and belongs in the pre-flight, not per-phase.

---

# 4. Findings about the CITIES *(carried into the pass files; recorded here as provenance)*

## 4.1 The retention spread — the run's strongest quantitative finding

**Verified by direct computation from `Official_Population_Census.md` Sections II and III, instrument
spot-checked against the source table.** Census I is peak surface population; Census II is the Orbital Era
after Amundsen Tower migration. **Both are explicitly pre-war** — so this is **emigration, not war loss.**

| City | Census I | Census II | Retention | z *(n=33)* | Rank |
|---|---|---|---|---|---|
| **Sinheung** | 1,069,350 | 888,292 | **83.1%** | **+1.41** | 3rd highest of 33 |
| **Zhongshan** | 1,279,433 | 996,684 | **77.9%** | +0.76 | above average |
| **Shirayuki** | 1,178,313 | 728,324 | **61.8%** | **−1.26** | 3rd lowest of 33 |

*(National mean 71.9%, sd 8.0.)*

**A 21.3-point spread across 2.67 standard deviations, between cities 8 km apart** sharing climate,
infrastructure, founding mechanism, war status, and national composition.

**Verified absent from canon:** the Overlap & Distinguishing Guide contains **0** mentions of retention,
census, population loss, or orbital migration. **All three cities' 32-section Cultural Spec Sheets contain 0
mentions of "orbital" or "Amundsen Tower"** — instrument verified on the same files *(`the`=113/74/72,
`Jeju`=3/8/12)*, so these are real absences, not a broken scan.

> **An era in which these cities lost between 17% and 38% of their people does not appear in their cultural
> spec sheets at all.**

## 4.2 What explains it — and it maps onto a typology canon already wrote

**The retention order is the exact inverse of how secure each city's founding claim was.** The Overlap guide's
own founding-relationship typology, which it uses for a completely different purpose:

| City | Founding relationship *(canon's own words)* | Retention |
|---|---|---|
| **Sinheung** | **"Inherited, not found"** — a claim that has to keep proving itself | **83.1%** |
| **Zhongshan** | **"Confirmed"** — validation of something already theirs | 77.9% |
| **Shirayuki** | **"Allocated to emptiness"** — a place decided for you | **61.8%** |

> **Proposed reading: a claim still being proved cannot be abandoned, because leaving forfeits it. A claim
> already secure does not need defending. A claim that was simply handed over costs nothing to give up.**

**Third order — and this is where Shirayuki stops resembling anywhere else:** **being easy to love is not the
same as being hard to leave.** Every attachment Shirayuki offers — art, schools, ease of friendship, an
outdoor gallery — is a *low-switching-cost* attachment. Sinheung's are all high-cost: a trade, a plant, a
claim, and a city where *"people know each other's business."* **Shirayuki optimized for arrival and never
built anything that costs something to give up.**

**Fourth order:** Shirayuki still draws students nationwide **on a reputation built by a population that has
already left.** New arrivals come for a scene at 62% of the strength that made it famous. **Its remedy lives
in its own past** — `02` §4.1's "in its own past" address, producing *"a characteristic nostalgia that is
factually correct."*

---

## 4.3 A rule this run broke, self-caught and recorded rather than quietly tolerated

**`01` §5.2 rule 4: *do not build the location's single strongest finding on a provisional assumption.***

**Phase 5's Finding R-4 — that Sinheung is replaceable, because the Federation needs the chambers rather than
Sinheung, and the design belongs to Neumayer — is the run's strongest single finding.** It rests on **what the
Federation needs**, and **the Federation has no pass**: it is a Band-6 polity that has never been written.
**The finding therefore rests on exactly the kind of provisional parental assumption the rule forbids
building on.**

**Not withdrawn** — the Neumayer design-authority fact is canon and load-bearing on its own — **but flagged**,
and the flag is the point. The alternative was to notice and say nothing.

> **Observation about the rule itself:** it is easy to obey while writing a weak finding and hard to obey when
> the strong one arrives, **because you do not know which finding is strongest until the pass is nearly done.**
> **PROPOSED: move this check from `01` §5.2 (where it reads as advice at declaration time) into Step 5
> Reconciliation, as a retrospective question — *"which finding is strongest, and what does it rest on?"***

---

# 5. Running list of PROPOSED methodology changes

> **⚠ Superseded and expanded.** The consolidated, confidence-ordered list of **fourteen** proposals now lives
> in **`03_Generalizing_Back_to_the_Base_Methodology.md` §7**, restructured around the developer's
> single-location-first correction. **The table below is the original nine, kept as a record of what was
> visible before that correction reframed the run.**

| # | File | Change | Confidence |
|---|---|---|---|
| **1** | `05` §6.1 | Generalize circularity from *provenance* to *kind*: prior culture-pass **conclusions** about the same location are inadmissible as input regardless of source | **High** — the run's central finding |
| **2** | `04` Part III / Gate 6 | "Noticed somewhere" ≠ "available where needed." Check whether findings have reached the sibling set's differentiation instrument | **High** — verified instance |
| **3** | `02` §6 | Registered symbols must be **read from file, never assumed from the name.** Saturn is the worked example | **High** — caused a full inversion |
| **4** | `00_RUNBOOK` Step 7 | Broaden "verify the instrument": spot-check **one row by hand against the source** for *plausible* numbers, not only zeros | **High** — silent wrong output |
| **5** | *new, cross-file* | **Score any quantitative differentiator against the full sibling set (z-score), never against the local comparison group alone** | **High** — killed a false finding |
| **6** | `05` §2.4 | Pull vs push differ in **durability**: ask what happens to a pull city when a better attractor opens | **High** — measurable here |
| **7** | `00_RUNBOOK` Step 0.4 | Add a triage order for high-canon locations; culture files read **last** | Medium |
| **8** | `00_RUNBOOK` Step −1 | Move canon-check question 1 into the pre-flight | Medium |
| **9** | `CLAUDE.md` | Narrow the graphify caveat — it underperforms on consolidated book files, not on location canon | Low — one data point |

---

# 6. REQUESTED — inputs this run needs and canon does not have

*(Per `05` §5: what is missing · which phase is blocked · what the pass did instead · what changes if the
answer differs.)*

1. **A post-unification pass frame.** *Missing:* whether the unified city is written as one location with three
   sub-districts. *Blocks:* nothing here — this run declares pre-unification. *Instead:* declared and flagged.
   *Sensitivity:* **high** — it changes type, band, parent, and sibling set, and the present day (~2822) is on
   the far side of it.
2. **Census III.** *Missing:* any present-day population figure; the census file states outright that none
   exists. *Blocks:* any present-frame pass. *Instead:* pre-war baseline used throughout. *Sensitivity:* high
   for a present-day pass, nil for this one.
3. **Whether "Alternative Culture" belongs to Shirayuki alone or all three.** Canon flags this as deliberately
   open pending Zhongshan's and Sinheung's megasheets. *Instead:* **not decided here** — treated as RESERVED.
4. **Sinheung's final in-universe name** and **the unified city's name** — both explicitly RESERVED. Working
   designations used; nothing named.

---

**Status: run in progress.** Sections update as the three passes proceed.
