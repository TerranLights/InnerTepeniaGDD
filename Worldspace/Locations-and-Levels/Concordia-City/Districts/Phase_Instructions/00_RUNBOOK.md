# RUNBOOK — Running One District, Start to Finish

**Written 2026-08-29, after six districts.** **This is the operational entry point. Start here.**

Everything in this folder is correct, and until now it was organized by **when each rule was learned** rather
than **when you need it** — five rounds of retrospective notes appended to `00_Index.md`. This file reorders all
of it into the sequence you actually work in, with each discipline stated at the point of use and every failure
mode attached to the district it was learned on.

**Reading this in full is mandatory before any district or location culture work** — a new pass, an edit to an
existing `Full_Extrapolation.md`, a single phase, a QA gate, a Review Panel run, or a change to the methodology
itself. That rule is stated bindingly in the project's `CLAUDE.md`. The detail files are the reference; **this
is the procedure.**

**Do not skip it because the task looks small.** Every failure recorded below was found during work that looked
small — a completion claim false for two weeks, a general-population error still live six weeks after the
discipline file was written about it, two districts given the same custom a day apart.

**And keep it current.** A methodology change that does not update this file has not been made — the next pass
will follow the runbook, not the commit message. **Update it in the same commit**, and record what was learned
and on which district.

---

# LAW 0 — DEPTH OVER SPEED. NEVER RUSH TO A FAST RESULT.

**Standing law, stated by the developer 2026-08-29. It governs every step below and overrides any of them that
would be served by hurrying.**

**Worldbuilding is upstream of the entire project.** Every character, questline, faction, companion arc,
personal struggle, daily hardship, pastime and small joy in this universe is **downstream of decisions made
here**. A shallow district does not produce a shallow district — it produces shallow people living in it,
shallow problems for them to have, and shallow reasons for a player to care. **The cost of going fast here is
not paid here.** It is paid later, everywhere, by work that cannot be fixed without coming back and redoing
this.

**Therefore:**

- **Contemplate before writing.** Sit with the material. The first plausible answer is usually the generic one,
  and a generic answer is worse than no answer because it occupies the slot.
- **Do actual web research.** Not recalled from memory, not inferred from the name of a place. **Cancer's
  from-scratch rewrite was forced by exactly this failure**, and every strongest finding since has come from
  research actually run — the ayahuasca aftercare, the Baku flame, the Welsh choirs, the Pullman rents, Oneida's
  mutual criticism.
- **Chase nth-order effects.** *(This is the `Cross_Reference_Synthesis_Technique` applied to place.)* For every
  finding, ask **"and what does that cause?" three times.** First-order is the observation. Second-order is
  usually the interesting one. **Third-order is where the district stops resembling anywhere else.** The Yards'
  housing being an asset on the books is first-order; that it therefore cannot flex in a downturn is second;
  that the request is consequently never made, which the district reads as evidence it isn't needed, is third —
  and the third is the finding.
- **Go deep on the specific, not wide on the general.** One institution understood to its third-order
  consequences beats six sketched.
- **Take the time.** There is no deadline on this and no credit for finishing a district quickly.

## The anti-patterns this law exists to stop

**Named plainly, and I have committed the first three.**

1. **Producing a district because it is the next one**, rather than because it has been thought through.
   Completion is not the goal; **a district somebody could live in is the goal.**
2. **Skipping research picks by declaring them redundant.** The difference-not-tier rule (Step 3.4) is real, but
   it is also *convenient*, and it has been used to research two picks out of eight or nine on several passes.
   **A pick is only redundant once you have actually looked at it.** Redundancy asserted from the title is a
   guess.
3. **Treating "the phase is covered" as "the phase is done."** A finding that answers the template question is
   the floor, not the ceiling.
4. **Accepting the first coherent answer** because it fits and the pass is long.
5. **Letting the QA gates substitute for thinking.** Eleven gates confirm a pass is not *wrong*. **None of them
   can tell you it is not thin.**

## The evidence for this law — a controlled case, recorded because it is the only one available

**Aquarius, 2026-08-29.** The pass researched **two of nine** picks and declared the remaining seven redundant
**from their titles**. Law 0 was written mid-pass, naming that exact anti-pattern, and **four more picks were
then actually researched.** Same district, same author, same day, before and after.

**The two strongest findings in the district came from picks four, five and six, and did not exist at two.**

- **Picks 4 and 5** (Akademgorodok, MIT Media Lab) produced the convergence behind **Finding XVII** — two real
  institutions, sixty years and one ideology apart, in which **the objector is the one who leaves.**
- **Pick 6** (Christiania) produced **Finding XVIII**, the pass's best: two long-running utopian communities each
  built a formal mechanism by which one person could act against the collective, **and the district has
  neither** — which is the whole of its capability deficit made institutional.

**Neither finding was reachable from the substrate, from canon, or from the two picks originally researched.**
**The seven "redundant" picks were not redundant. Four of them were the pass.**

> **This is also the argument against the convenient version of Step 3.4.** Difference-not-tier is a real rule,
> and it can be used to justify stopping early. **Redundancy asserted from a title is a guess.**

## The companion failure — research used as decoration

**Doing the research is not the same as letting it change anything.** After each pick, ask plainly: **did this
change a finding, or did it ornament one?** Both answers are honest and they must be recorded differently.

On Aquarius: **Christiania changed the pass** — it produced a finding that did not previously exist.
**Tsukuba did not** — it yielded two useful nuances (relocation was effectively compelled; the district's dark
reputation was factually false) and no finding. **Say which.** A citation attached to a conclusion that would
have been written anyway is decoration, and it makes a thin pass look researched.

## The test

Before closing a district, ask: **could a person live an entire life here, and would that life be unlike a life
in any of the other twelve?** If the honest answer is *"probably, I suppose"*, the pass is not finished
regardless of what the gates say.

---

> **The one rule under all of it** (`../../Cultural_Synthesis_Techniques.md`): **never carry one location's
> answers into another.** If two places produce similar-shaped answers to the same technique, at least one is
> wrong. Every gate below serves that. **Law 0 is what makes it possible to obey** — two places produce
> similar-shaped answers mainly when neither was thought about long enough to become itself.

---

## Step 0 — Before writing anything

**0.1 Read the four cross-phase disciplines.** Not optional, and not once-per-project:
`00b_General_Population_Discipline.md` · `00d_Shadow_Proportion_Discipline.md` ·
`00e_Substrate_Application_Pass.md` · `00f_Review_Panel.md`.

**0.2 Run Gate 0 — reconcile the Plan's claim against the file, *and the file's own open-questions list against
the Deep_Dives folder.*** *(Second half added 2026-08-29 — the Markets' megasheet listed three resolved
mechanisms as open, a month after they were settled.)* *(`00c` Gate 0.)* Open the district's block in
`../District_Culture_Development_Plan.md` and count the phases it claims against the phases the file contains.
**This gate has caught a real defect in three of the six districts checked** — Taurus and Leo over-claiming
("ALL 8 PHASES COMPLETE" while missing Phase 7 entirely), Scorpio **under**-claiming (three finished phases
listed as "needed"). It fails in both directions. Cheapest gate here, highest yield.

**0.3 Determine the mode.** *(`00e` §1.)* **Mode A** — phases already written, substrate applied as a second
pass, mandatory overlap check first. **Mode B** — phases not yet written, substrate folded in as a first-pass
input. **All remaining districts are Mode B.**

**0.4 They do not enter clean.** Every district carries **4-7 pre-Plan findings from 2026-07-09** that predate
the shadow, general-population and research-first disciplines. **Read them before writing over them.**

**0.4b ⚠ Read `../District_Refugee_Diaspora_Composition.md` NOW, not at research time.** *(Moved here from
Step 3.7 on 2026-08-29, because it was skipped on the very first pass after it was written.)* It lived inside
the research step, where it competed with the pick list and lost. **It is a mandatory read, not a research
option.** Five of the first nine districts ignored it; the Markets pass skipped it too and only caught the
omission at Step 8 — reading it then produced a new finding and corrections to three others, including the
discovery that **the district is ~87.7% from a single city and has no idea.** Full evidence at Step 3.7.

> ### ⚠ Read the *concentration*, not just the entries. It varies by a factor of four and nobody has used it.
> *(Measured across all thirteen districts, 2026-08-29.)*
>
> | District | contributors | top | top-2 | largest |
> |---|---|---|---|---|
> | **10 Pisces** | **2** | **87.7** | **100.0** | Shirayuki |
> | 13 The Hub | 5 | 41.2 | 68.1 | Lazar |
> | 11 Sagittarius | 7 | 39.6 | 57.3 | Denison |
> | **05 Aries** | **3** | 39.0 | **73.9** | Denison |
> | 07 Aquarius | 6 | 36.4 | 56.1 | Halley |
> | 09 Gemini | 7 | 30.0 | 58.7 | Janbogo |
> | 04 Scorpio | 7 | 29.8 | 54.8 | Casey |
> | 02 Taurus | 9 | 26.3 | 41.3 | Lazar |
> | 01 Cancer | 7 | 24.6 | 46.6 | Esperanza |
> | 03 Leo | 9 | 23.9 | 42.7 | Casey |
> | 06 Capricorn | 8 | 22.9 | 42.5 | Neumayer |
> | 08 Libra | 10 | 19.2 | 33.8 | Zhongshan |
> | **12 Virgo** | 8 | **13.3** | **25.6** | Davis |
>
> **Top-2 share runs from 25.6% to 100%.** These are not the same kind of social object and the passes have
> been treating them as if they were. **A district that is nine-tenths one city has a dominant transplanted
> culture that reads as native** — its "local" customs are somebody's imported ones, unrecognized. **A district
> whose largest contributor is 13% has no such thing** and its culture must be synthesis or friction, because
> nothing arrived big enough to set the tone. **Aries is effectively three cities and its file uses *refugee*
> and *transplant* zero times.**
>
> **Directly relevant to the two districts left:** Sagittarius is **concentrated** (57.3% top-2) and Virgo is
> **the most diverse district in Concordia** (25.6%, nothing above 13.3%). **So the Markets and the Undergrid
> are opposites on this axis too** — one city pretending to be a mixture, against a genuine mixture — which is
> a second, independent reason to write them as a pair.

**0.5 Note any reserved decision** and state it at the head of the pass. *(`00e` §5, protocol from Capricorn.)*
Five districts still lack a settled in-fiction name; Capricorn's Narrow Door is reserved outright. **Identify
what would foreclose the choice before you write, not after.**

---

## Step 1 — Gate 9 the pre-Plan findings, first

**Do this before writing new material, not at QA time.** *(`00c` Gate 9.)*

For each existing finding describing a **threshold, gate, conversion, verdict, admission or status change**,
ask: *the mechanism runs both ways — did the file write both?*

**This has fired on 5 of 5 districts, and every time the failure was in the 2026-07-09 material.** Those
findings were written to explain how a district *works*, a framing that documents the favorable path and stops.
Taurus's trust converted a stranger permanently and never said the reverse is equally permanent; Leo's ladder
had only an up direction; Scorpio's legible progress meant legible stalling; Aries wrote the emergency case and
had no register for slow need; Capricorn made drive and pressure indistinguishable and left no way to stop.

**Ask:** what happens to someone the mechanism decides *against*? Is that outcome as durable? Is there a route
back? **A "no route back" nobody has perceived as a problem is a textbook shadow under `00d`.**

---

## Step 2 — The capability reading, before any research

**This is the primary generator and it comes first.** *(`00e` §5; `F_Rulerships.md` §5-6.)* **6 of 6 districts'
strongest structural finding came from here.**

**2.1 Identify the row's *shape*, then ask the matching question. The typology was declared closed at four and
was not** — the Markets exposed a fifth. **Five shapes; the two remaining districts are one of each:**

| Shape | Worked example | The question that unlocks it |
|---|---|---|
| **Complete** (all four terms) | the Power Core, the Yards | *What does the balance cost?* |
| **One absence** | Taurus (no fall) | *What does lacking this faculty entirely mean?* |
| **Double absence** | Leo (no exaltation, no fall) | *What is the one instrument it does have?* |
| **Net-negative** | Scorpio | *Does its civic function require what it lacks?* |
| **Doubled row** *(added 2026-08-29)* | the Markets; **the Undergrid, unwritten** | *Which faculty is doubled, and in which direction?* |

**2.2 Then ask: are the deficits *addressed* or *diffuse*?** Three configurations observed. Both addressed (the
Power Core — concentrated in its own opposite number, so its weakness has a name and a permanent grievance).
Diffuse (Taurus — donor to everyone, no counterparty, no politics). **One of each (the Yards — which is why it
can perceive its care deficit and not its meaning deficit).** *Where a deficit lands determines whether the
district can even see it.*

**2.3 Write it as a capability profile, not a diagnosis** — two strong faculties, two weak, then **one
consequence.** If your consequence reads like another district's, it is wrong.

> ⚠ **Sagittarius is the fourth district on the double absence — there are now three existing answers not to
> reuse** (Leo *cannot fail gradually*; the Labs *cannot form a stable intention*; the Circuit *cannot make a
> correction outrank the error*). **And it carries a second hazard the others did not: it is the Circuit's
> opposition, and the Circuit was written first.** The danger there is not contradiction — **it is symmetry.**
> The substrate is explicit that this particular opposition *presents as kinship and stalls there*, which makes
> "write it as the mirror image" the most tempting and most wrong move available. **Its consequence must be
> unrelated to the Circuit's, not inverse to it.**

> ⚠ **The Hub has no capability row, and Step 2 does not work for it.** *(Confirmed 2026-08-29 against
> `F_Rulerships.md` and `13_Ophiuchus_Hub.md`.)* Not "thin", not "two-term" — **explicitly none**: no element,
> no modality, no opposing sign, no ruler, no house. The substrate says so in those words. **So the primary
> generator, credited with the strongest structural finding on every district so far, returns nothing for
> exactly one district**, and that district is the deferred one. **Do not discover this mid-pass.** It also
> makes the Hub the natural falsification test the standing honesty note has been asking for: the prediction
> table's twelve confirmations were all produced where the generator works, and **the Hub is the one place it
> cannot flatter anything.**

> ⚠ **Schedule Virgo and Pisces together, and write neither in ignorance of the other.** They are the two most
> distinctive rows left in the table and they are **structural opposites on the single faculty of
> verification** — Virgo holds it at maximum (the only district whose ruler is also its exalted planet), Pisces
> at minimum (the only district where one faculty holds both detriment and fall). **That is the cleanest
> inter-district conflict the dignity system produces anywhere**, and writing them a month apart without
> reference would waste it. Whichever runs second must read the first's file before Step 2.

**When a shape repeats, the procedure is three steps and only the first is shared.** *(Method recovered from
Aquarius, which shares Leo's shape exactly and produced an unrelated finding.)*

1. **The shape gives you the question** — here, *what is the one instrument?* This part is identical across
   every district with the same row, and is the only part that is.
2. **The ruler gives you the instrument.** Leo's is **recognition**. The Labs' is **the collective.** Nothing
   about the shape predicts which; you have to read the row.
3. **The instrument gives you the consequence, and this is where the districts separate entirely.** Leo, running
   on recognition with no fallback → **cannot fail gradually.** The Labs, running on the collective while
   holding two irreconcilable accounts of what serving it means → **cannot form a stable intention.** *Same
   shape, same question, opposite results.*

**If your step-3 consequence resembles the earlier district's, you have stopped at step 1 and assumed the rest.**

---

## Step 3 — Research, aimed at what Step 2 named

**3.1 Actually run it.** The picks in `../District-Inspirational-Influences.md` are almost always **identity-level
only** — never mined concretely. That condition forced Cancer's from-scratch rewrite.

**3.2 Research the deficit.** *(`00e` §5. 2 for 2, and it produced the top finding both times.)* The capability
reading says what a district **cannot** do; it does not say what the missing thing looks like. **Find a real
culture that has it, and the contrast writes the finding.** Scorpio's row said *nowhere to convalesce* →
researching Iquitos ayahuasca practice showed real transformative practice devotes as much structure to the
aftermath as the event → **Scorpio has the ceremony and not the aftercare.** Capricorn's said *no care, no
meaning* → guild practice bundled craft standard + mutual aid + devotional meaning → **the Yards is a guild with
the burial fund and the patron's day missing.**

**3.3 Research can supply a substitute *institution*, not just texture.** Welsh coalfield choirs — founded after
named disasters, for rehabilitation *and fundraising* — gave Aries both the archive it lacks and the
compensation mechanism it cannot build.

**3.4 Prioritize by difference, not by tier — but prioritizing is not the same as skipping.** *(Tightened under
Law 0.)* Most pick-lists contain a redundant cluster, and **the most valuable pick is the one least like the
others**, whatever its PRIMARY/SECONDARY/SUPPORTING label. **But redundancy has to be established, not
assumed.** Several passes have researched two picks out of eight or nine and declared the rest redundant **from
their titles** — which is a guess wearing the costume of a method. **Look at each pick at least far enough to
know what it would have given**, and record that in Gate 7 rather than the assumption.

**3.5 The inspiration is a source, not a specification.** *(Developer instruction, 2026-08-29 — and this is as
important as the instruction to do the research at all.)*

**A pick is an *inspiration*. It is not a template to be transcribed, and the location is under no obligation to
match it.** Three outcomes are all legitimate:

- The location ends up closely resembling its inspiration **with a new paint job** — fine.
- It takes **one mechanism** and diverges everywhere else — fine, and commonest.
- It goes somewhere **the inspiration never went** — fine, and often the best result.

**The two tests that actually bind are internal, not external:**

1. **Is it characteristically consistent with *itself*?** Does this follow from what this place already is?
2. **Is it consistent in-world, within the Tepenian universe as a whole?**

**Nothing requires fidelity to the real-world case.** The research exists to supply ideas, mechanisms, and
consequences a designer would not have reached alone — **not to be reproduced.**

**Two failure modes to watch, both easy:**

- **Transcription.** Mapping a real place onto a district feature-for-feature produces a **costumed version of
  somewhere real**, not a place. The test above catches it: ask whether each imported element follows from the
  district's own character, or only from the source's.
- **Importing a vivid detail that does not follow.** A striking real fact is not automatically a district fact.
  *(This is the standing `feedback_realworld_fact_vs_fiction_driver` rule applied to place: a striking fact is
  not automatically a culture driver.)* **If the only argument for a detail is that it is interesting, cut it or
  earn it.**

**Preferred shape when writing a fusion:** state what the real case did, then state what **this** place does —
and let them differ where the district's own character says they should. **Divergence stated is stronger than
resemblance implied**, because it shows the reasoning.

**3.6 Record what you skipped and why**, in Gate 7. Name the genuine omission separately from the redundant
ones. **Three outcomes now, not two — *changed*, *ornamented*, *withheld*** (`00c` Gate 7). Expect roughly
70-80% of picks to change findings.

**3.7 ⚠ Read `../District_Refugee_Diaspora_Composition.md`. Five of the nine completed districts did not, and
it is the largest unexploited source in the folder.** *(Measured 2026-08-29 across all nine
`Full_Extrapolation.md` files, findings only.)*

```
                diaspora  transplant  refugee
01 Cancer          7          3          6
02 Taurus          3          2          2
03 Leo             6          4          0
04 Scorpio         0          0          0     ← a Stage 2 Override district
05 Aries           1          0          0
06 Capricorn       0          0          0
07 Aquarius        0          0          0
08 Libra           0          0          1
09 Gemini          1          3          5
```

**Scorpio is the indictment.** It is one of the four **Stage 2 Override** districts — four destroyed cities
were routed into it specifically — and its file uses the word *refugee* **zero times.** Capricorn, Aquarius and
Libra are the same story without the aggravating factor.

**The file is per-district, already written, weighted, and specific**, down to named transplanted institutions
and social-cohesion mechanisms per contributing city. **The Circuit's two best culture findings came out of it
and out of nothing else** — the Zukelli food-and-music venues (Finding XVII) and the Memory Circles as the
district's first funerary institution (Finding XXII). Neither was reachable from the substrate, from canon, or
from any research pick.

**This is the same failure as the Aquarius research case, in a different costume:** a rich, specific, already-
written source declared unnecessary without being opened.

---

## Step 4 — Write the phases

**Mode B: fold the substrate in as you write; do not bolt on a separate section.**

- **Conflict geometry goes into Phase 4** (`00e` §11b). **No phase covers inter-district relationships** — this
  is a real hole in the Plan, and the measured consequence is that districts do not mention each other. Taurus's
  file mentioned its own opposite district **zero** times; Leo's mentioned one of its two hardest frictions
  zero times; Aries and Virgo mention no neighbours at all.
- **Phase 7 counterculture:** **check for an existing one in canon first** (Capricorn had the Recalibration
  Underground). Then derive from **Step C** — what does this district require of everyone, and who will not give
  it? **The Phase 5 seed technique is Mode A only.** **Do not default to a refusal:** a counterculture can
  refuse, can *add* what the district cannot do (the Tally), or can **demand the district's own rule be applied
  more literally than the mainstream does** (the Recalibration Underground).
- **Phase 7 has an eighth category the template omits: Death and the Dead** (`07_Phase_7` §1b, added
  2026-08-29). **The 32-section template has no mortuary slot at all**, and measured across nine districts with
  a verified strip and five terms, death practice appears only where some other finding dragged it in — **two
  districts score zero on every term.** **The question is obligatory; a section is not** — write one only where
  the answer is distinctive, and **use the `funerar` stem**, which has now caught two sections that `funeral`
  scored at zero.
- **Phase 2 religion: use the Naming technique before inventing.** *(6 for 6.)* Search canon for religious
  register attached to non-religious objects. **It does not always return a religion** — a district that already
  has one yields a *stake*, a *compact*, or a *creed* instead.
- **When a category comes up empty, ask who *brought* one before inventing one.** *(New technique, 2026-08-29,
  from the Circuit — see `../../Cultural_Synthesis_Techniques.md`, **Borrowed Form**.)* A district that lacks a
  form very often has an incoming population that already had one, and **an institution the district borrowed
  is a better answer than one it invented**, because it explains something already in canon and it carries a
  built-in relationship: the host uses it, values it, and cannot quite say what it is receiving.
- **Check `../Cross_District_Differentiation_Table.md` before writing each category.** See Step 6.
- **General-population discipline throughout** (`00b`). Highest-risk categories: Fashion, Music, Sensory
  first-impressions, Visitor Experience.

---

## Step 5 — Substrate findings and contradictions

**Expect the contradiction to resolve both-are-true.** *(7 for 7.)* The recurring shape: **one disposition
producing two opposite effects on two different objects or at two different scales.** Don't ask which is true —
ask *what single trait would produce both*, then check whether the two claims are about different objects.

**Mine the substrate's §15 Source Gaps.** *(`00e` §2.)* It looks like a caveats list and is one of the highest-
yield generators in the folder. **Where the sources have a hole, ask whether the hole is the district's
mechanism.** Two of Scorpio's best structural findings came from nowhere else.

**Translation discipline** (`00e` §8): no zodiac vocabulary outside a bracketed citation or a header. **Sweep
with word boundaries on every alternative** — a bare `mars` matches inside `grammars`. This has caught genuine
leaks on every district; expect 3-7.

---

## Step 6 — QA, Gates 0-10

Full detail in `00c_Completion_QA_Checklist.md`. The three that need emphasis:

**Gate 1 — paste the raw per-term counts into the QA block. Do not summarize them.** *(Rule strengthened after
it failed twice.)* Four mis-readings across Aries and Capricorn, **all four flattering the pass.** An
instruction to read carefully does not survive an author grading their own work. Three outcomes per term: **pass
· fail · covered in substance, absent in term** — the third is normal, and **never insert a word to make the
grep pass.**

> ⚠ **And the counts are only as good as the strip. Verify it before you record anything.** *(Added
> 2026-08-29, round 9.)* The same scan was run three times over nine districts and returned **three different
> answers** — the terms never changed, only the boundary did. **The QA header must be exactly
> `## QA — Completion Check` (eight districts use it; the Circuit's pass wrote something else and the strip
> silently matched nothing, counting the whole QA block as findings).** Use **stems, not whole words** —
> `funeral` does not match `funerary`, and `mortuary` was never on the list at all. **A 0 must be re-run
> against its stem before it is recorded as anything.** Full procedure and the correct verification command —
> the obvious one is wrong — in `00c` Gate 1.

> ⚠ **Gate 9 runs twice now.** Inherited material at Step 1, **and the thresholds this pass itself just
> wrote**, before the QA block. Gate 9 is eight for eight and **every firing was against the same inherited
> defect class** — it has never been tested against a finding written under this methodology. See `00c`.

**Gate 4 — swap against the partner most likely to survive**, not a convenient comparable. **Record which
finding was weakest**, not just that the set passed.

**Gate 6(b) — check against completed districts using
`../Cross_District_Differentiation_Table.md`.** One file read instead of six. **This gate has already failed
once**: the Power Core and the Yards were given nearly the same food custom a day apart. **Differentiate inline
in the district's own finding, not only in the table**, and **add the district's column in the same commit.**

---

## Step 7 — The Review Panel *(Gate 10)*

`00f_Review_Panel.md`. Cast the six Flat Archetypes, add the **Passer-Through** and **Neighbor** (both
mandatory), and always run the **Lover faculty** — *is this place alive, and could anyone love it?* — the one
question no other gate asks.

**Three rules:** a position with nothing to say says nothing · reviewers need not be fair or right · **a position
is not guaranteed to get what it wants.**

**Five dispositions:** `accepted` · `noted` · `rejected` · `refereed` (two positions both right and both
excessive — state the settlement) · **`unmet`** (the want is genuine and the place characteristically would not
and should not satisfy it — **write the refusal as characterization, not as a gap**).

> **The test that keeps this from homogenizing thirteen districts:** *would satisfying this objection make the
> district more like the other twelve?* If yes, it is `unmet`. **`unmet` should be common; a panel that never
> produces it is being run wrong.**

**Apply Truby's four-corner check to the panel itself.** If three positions raised the same objection in
different clothes, the panel collapsed to one lens. **Convergence from genuinely opposed corners is the
strongest signal available** — Capricorn's Child, Lover and Lover-faculty independently found the same absence.

**Record Life Arc silences.** The Mage arc returning nothing from the Yards *was* a finding.

---

## Step 8 — Record

1. **Append the QA block and the Review Panel block** to the district's `Full_Extrapolation.md`.
2. **Update `../District_Culture_Development_Plan.md`** — the district's own block *and* the progress tracker.
3. **Update `07_Phase_7_Native_Culture.md`**'s status table.
4. **Add the district's column to `../Cross_District_Differentiation_Table.md`.** Same commit.
5. **Update `00_Index.md`**'s status section.

---

## The standing honesty problems

**Recorded here because they are easy to stop seeing.**

- **Self-audit error was thought to run in one direction. Round 9 found it does not, and that is worse.**
  Across six districts every mis-reading of my own QA output flattered the pass, and the rule was to re-check
  in the flattering direction. **Then a round-9 re-scan ran *against* the pass — and was also wrong.** Three
  runs of one scan gave three answers because the strip boundary was never specified or verified. **The
  direction was never the real problem; an unverified instrument was.** A scan whose boundary is undefined
  returns whatever the last edit happened to make it return, and the author will believe it either way.
  **Re-check in both directions, and verify the tool before trusting either.**
- **The prediction table is at twelve straight confirmations and should be read as house style, not evidence.**
  The predictions were written, the districts chosen, the passes run and the results graded by the same person.
  **The only prediction that ever failed did so on a countable fact; every survivor is interpretive.** Two
  things would restore it as a test — run a district chosen *because* it looks least likely to conform (the Hub
  was identified for this and is deferred), or state in advance what would **falsify** each rule. Neither has
  been done.
- **The Review Panel is not independent review.** Same author writes the district and the objections. It is
  better-directed attention, not a second opinion.
- **A recorded failure is not a fixed failure.** `00b` names three districts as its canonical general-population
  examples; **two were corrected and Scorpio — the origin case — was still broken six weeks later.** When a
  discipline file cites a district, open that district and confirm the text actually changed.

---

## Where everything lives

| File | What it is |
|---|---|
| **`00_RUNBOOK.md`** | **this file — the procedure** |
| `00_Index.md` | file index, per-district status, and the **historical record** of how each rule was learned (five rounds) |
| `00b_…Discipline.md` | general population, not narrow context |
| `00c_Completion_QA_Checklist.md` | Gates 0-10 |
| `00d_…Discipline.md` | the shadow is a byproduct, never the operating principle |
| `00e_Substrate_Application_Pass.md` | modes, capability reading, contradictions, translation discipline, predictions |
| `00f_Review_Panel.md` | the archetype panel, Gate 10 |
| `01`-`08` | the eight phases |
| `../Cross_District_Differentiation_Table.md` | **check before writing each category; update on completion** |
| `../District_Culture_Development_Plan.md` | the what and in what order; progress tracker |
| `../../Cultural_Synthesis_Techniques.md` | the generative toolkit — where new culture actually comes from |
| `../Zodiac_Personality_Substrate/` | per-district substrate; `99_Application_to_Districts.md` is the bridge |
