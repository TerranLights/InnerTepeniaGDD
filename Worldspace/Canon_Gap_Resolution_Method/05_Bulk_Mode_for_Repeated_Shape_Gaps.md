# 05 — BULK MODE: Repeated-Shape Gaps

**Added 2026-09-01, at the developer's direction, as the Governing Priority Sequence's Stage 1 work
("architect the mechanism to procure currently-unavailable, necessary information").**

> **Status: NEW AND UNEXERCISED.** Written before its first run, from a real triggering case (the Division of
> Industry necessary-sector gap, 36 cities × ~18 industries) but not yet validated by it. **Per Step 10's sixth
> check — untested paths are not defects; untested paths described as ready are.** Nothing here has a track
> record. Treat its first run as a test of this file as much as of the gaps it closes.

---

## Why this file exists — the runbook's procedure does not scale, and that is not a criticism of it

**`00_RUNBOOK.md`'s Steps 1–9 are built around individually triaged gaps**: intake a candidate, triage it four
ways, select a cheapest-viable path, acquire, classify, deposit, gate, record. That is exactly right for the
14 LIVE items in `Test_Runs/2026-08-31_Seed_CapeAdare_and_Highway37.md`, where every gap is a genuinely
different question.

**It breaks down completely against a gap that has one shape and hundreds of instances.**

> **The triggering case, 2026-09-01.** The Division of Industry sweep found six necessary industries absent
> from up to 36 of 36 city economies (`../Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/
> Cities/Division_of_Industry_Sweep_2026-08-31.md` §4.4). A full-necessity derivation raises that to roughly 18
> industries. **36 × 18 ≈ 650 cells.** Running the base procedure 650 times is not a method; it is a sentence.

**The failure mode if you try anyway is worse than slowness.** Six hundred and fifty individually-answered
cells, each reasonable on its own, converge — because the cheapest defensible answer to "does this city need
water?" is the same answer every time. **Bulk-answering a necessary-industry question city by city produces
thirty-six identical economies**, which would silently undo differentiation work this project has spent
enormous effort building and guards elsewhere with a dedicated mechanical table
(`Cross_District_Differentiation_Table.md`, and Gate 6b has already failed once without it).

**So bulk mode is not "the normal procedure, faster." It is a different procedure**, with a different unit of
work and a different characteristic failure.

| | Base mode (`00_RUNBOOK.md`) | **Bulk mode (this file)** |
|---|---|---|
| Unit of work | one gap | **one gap *shape*, then its deviations** |
| Triage | per gap | **once, at the shape level** |
| Characteristic failure | closing a gap that should stay open (LAW A) | **closing 650 gaps identically** |
| Success measure | gaps closed vs. correctly protected | **variance produced across instances** |

---

## LAW D — RESOLVE AT THE HIGHEST LEVEL THAT ANSWERS THE QUESTION

**Bulk mode's governing law, and the entire source of its efficiency.**

**Most instances of a repeated-shape gap are not independent questions. They are one question asked N times.**
Answer it once, at the level where it is actually one question, and N−1 instances collapse into short
deviations instead of N from-scratch inventions.

> **The worked case that established this, 2026-09-01.** The sweep reported food production absent from 33 of
> 36 city economies, and flagged the alarming implication that Davis alone might feed ~30 cities — *"a
> significant, currently-unstated national dependency."* **That reading treats 33 cells as 33 gaps.** But
> `Worldspace/City_Logistics.md` already establishes, for Concordia, that *"everything consumed in the city
> must be produced in the city or brought in at significant cost and risk,"* with hydroponics as the primary
> system. **If that generalizes, it is one national ruling — every city runs closed-loop hydroponics as
> baseline load; Davis is the only *export* agriculture — and it closes 33 cells at once.** It also dissolves
> the Davis dependency, which was never canon; it was an inference drawn from absence.

**The escalation order — always try the highest level first, not the lowest:**

1. **Universal / physical law.** Is this true of every instance because of how the world works? *(Water is ice
   everywhere in Tepenia. Nobody landfills in permafrost.)*
2. **National / systemic ruling.** Is there one policy, institution, or standard practice that answers it for
   the whole set? *(How does Tepenia feed itself? What happens to a decommissioned robot?)* **This is where the
   leverage is, and it is the level the base procedure never reaches, because it triages instances.**
3. **Class / archetype.** Does it resolve identically for a defensible subgroup? *(Coastal cities fish; interior
   ones cannot.)* **⚠ Use sparingly and never as the primary tool** — archetype-answering is precisely how
   convergence enters, and a class is not a reason, it is a bucket.
4. **Instance.** Only what genuinely differs at this one location, person, or object.

**The inversion this law forces:** in base mode you work bottom-up from instances. **In bulk mode, reaching
level 4 with real work left to do means levels 1–3 were done properly.** A bulk run whose effort is
concentrated at level 4 has not been made efficient; it has skipped the leverage.

---

## LAW E — THE INSTRUMENT MUST BE DERIVED FROM EXISTING CANON, NOT INVENTED

**A bulk run assigns values to hundreds of cells. If those values come from judgment exercised 650 times, they
are 650 opportunities to be arbitrary, and no reviewer can ever check them.**

**So: build a scoring instrument whose inputs are attributes already written down**, and compute the expected
value of every cell from it. This is `02_Acquisition_Paths.md`'s **Path 2 (derivation)** applied at scale, and
it is what makes a bulk run auditable — anyone can re-run the instrument and get the same numbers, and any
disagreement is a disagreement about a *driver*, which is one argument, not 650.

**The test of a legitimate bulk instrument, and it is strict:** every driver it reads must already exist in
canon for every instance, before the run starts. **A driver you have to invent per-instance is not a driver;
it is the gap wearing a disguise.**

> *Worked case: the industry instrument reads population, human:robot ratio, mean annual temperature, wind
> regime, altitude, coastal access, highway isolation, founding date, polar night length, and labor
> externalization — ten drivers, all already present in every `Specs/` file and the Census. Zero new research
> was required to compute the baseline for all 36 cities.*
>
> **⚠ And one driver that had to be REMOVED, which is the more instructive half.** The first draft included
> **"post-war status,"** read off each `Specs` file's `Status:` line. **That was a period-scope error:** the
> division of industry describes the **Second Interwar Period**, when the Federation was a functioning country
> — a city's destruction in the Long Night War is downstream of the entire model and never enters it. **A
> driver can be perfectly well-sourced and still be measuring the wrong era.** LAW E's requirement is that a
> driver be *already-canon*; it does not by itself guarantee the driver is *in scope*. **Check both.**

---

## LAW F — THE DESIGN WORK IS IN THE DEVIATIONS, AND SO IS THE VALUE

**The instrument's output is not the answer. It is the null hypothesis.**

An instrument gives you the *expected* value for every cell. **Expected values are, by construction, the least
interesting content it is possible to write** — they are what you would have guessed. Deposit them alone and
you have filled 650 cells with the average of the set, which is the homogenization failure arriving on
schedule, wearing a formula for a disguise.

**The generative question is the residual:**

> ## *Where does this instance depart from what the instrument predicts — and what is the reason?*

**And the reason is always the content.** A city whose expected utilities burden is 22% but which actually runs
it at 34% has a *story* in that twelve-point gap: something is wrong with the ice, or someone is being made to
carry it, or a failure in living memory permanently overbuilt the system. **That is culture, and no amount of
correctly-computed baseline produces it.**

**Operationally:** the instrument's job is to tell you *which cells are boring so you can stop looking at them*,
freeing the entire budget for the cells that are not. A bulk run that produces no surprises has not succeeded
quietly. **It has failed, and the instrument is miscalibrated or the drivers are too few.**

---

## LAW G — EVERY INSTANCE GETS A SLOT FOR WHAT ONLY IT COULD HAVE

**Added 2026-09-01, at the developer's direction, immediately after this file's first draft — which did not
have it, and needed it.**

> *"In each city, I want to make sure to allow space for 'weird' industries. Fields that, upon first glance,
> sound Schizophrenically insane, but then when you consider them within the context of their setting,
> environment, history, culture, and the lives of the people who live there, those 'insane' industries
> actually make perfect sense in context, and that's the sort of thing that really, really gives a place
> character."*

**This law exists because LAWS D–F structurally cannot produce what it asks for, and would never have revealed
that on their own.** A necessity instrument computes what an instance **must** have. This asks for what only
this instance **could** have. **They are inverses**: run the instrument across all 36 cities and it returns
exactly zero weird industries, forever, no matter how well calibrated it is. **So the weird-industry generator
is co-equal to the instrument, not a decoration on it** — a second output from the same drivers, with its own
procedure, its own quota, and its own guard.

### ⛔ WHAT QUALIFIES — the definition, sharpened 2026-09-01 after this file's first draft got it wrong

> *"I don't want to make it 'arts and crafts', because those are not 'weird'; those are hobbies, scaled up to
> subculture-level. What I want is things that (when approached without any context or background), on the
> surface, appear absolutely fucking Schizophrenic, and then when you gain the necessary context and develop a
> sense of perspective, those 'schizophrenic' things suddenly make perfect sense."*

**This file's first draft permitted craft-and-leisure economies as LAW G output. That was the failure it was
written to prevent, arriving one section later.** **A hobby scaled up reads as *charming*; this must read as
*pathological*.** A town full of woodcarvers is a tourist brochure.

#### Gate 1 — the derangement test *(first contact)*

> ## Stated flatly, with no context, would an outsider conclude that something is **wrong** with these people?
>
> **Not "how quaint." Not "how interesting." — "What is wrong with you."**

**This single question disqualifies artisanal, folk-craft, quirky-festival, niche-enthusiast and
hobby-subculture answers *from this slot*.** All of them read as *enthusiasm*, and **enthusiasm is never
deranged.**

> ## ⚠ DISQUALIFIED FROM THE SLOT ≠ EXCLUDED FROM THE CITY. Two different categories, both required.
>
> **Developer clarification, 2026-09-01, immediately after the gates above were written** — because as first
> drafted they read as banning craft culture from the setting, which is the opposite of the intent:
>
> > *"I do love the idea of including artisanal, folk-craft, quirky-festival, and niche-enthusiasm things. I
> > definitely want all of those to be present in **every** city to at least **some** extent. I'm not saying
> > that they shouldn't be present, because they definitely should. What I'm saying is that those are not
> > 'weird industries'."*
>
> | | **Local Texture** | **LAW G weird industry** |
> |---|---|---|
> | What | artisanal craft, folk practice, festivals, enthusiast scenes | the deranged-then-inevitable thing |
> | Presence | **every city, to some extent — required** | every city reserves a slot; intensity varies |
> | First-contact reading | charming, warm, characterful | **"what is wrong with you"** |
> | Explained by | taste, tradition, availability of time and material | **structure — physics, economics, history** |
> | Economic share | ordinary production inside the Distinctive tier; often what the corpus's undifferentiated "Other: 3–15%" buckets already hold | **0.5–8% per industry**, aggregate uncapped but earned |
>
> **Both, in every city. They are not competitors and they are not the same slot.** A place with texture and no
> strangeness is pleasant and forgettable; a place with strangeness and no texture is a gimmick with nobody
> living in it.
>
> **⭐ They frequently share a cause without sharing a category.** *(Worked case: a rotational-residence city's
> large idle-time blocks produce a genuinely thriving craft scene — **that is Local Texture**. The same city's
> exported productive labor is what leaves room for a high aggregate of weird industry — **that is LAW G**. One
> structural fact, two distinct outputs. **Do not let the first stand in for the second**, which is exactly the
> substitution this file's first draft made.)*

#### Gate 2 — the inevitability test *(on inspection)*

**Context must not merely explain it — it must make it feel forced.** The reader should land on *"of course; it
could not have been otherwise."* **The explanation must be structural** — physics, closed-system economics,
logistics, history. **"They just like it" fails**, which is exactly why scaled-up hobbies can never clear this
bar: their only available explanation is taste. *(The ≤3-step causal chain below enforces Gate 2's rigor.)*

**Both gates, or it is not a LAW G industry.**

#### The six sources of apparent derangement

**The six *moves* below generate a real mechanism. They do not generate the affect.** That needs its own axis:

1. **No visible product** — labor with no object. Walking, listening, counting, waiting.
2. **Grotesque or taboo material** — the dead, bodily remains, decay, the discarded.
   > **⛔ CONTENT BOUNDARY — developer instruction, 2026-09-01: no excreta.** Excretion is **out of scope for
   > this setting's weird industries**, permanently and by preference, not by oversight. **Do not reintroduce
   > it** as a byproduct stream, a waste-recovery detail, or a "realistic closed-loop" argument — the closed
   > system is real and the sanitation sector (A2) still exists, but **it is never mined for character.**
3. **Obsessive precision over the trivial.**
4. **Monetized intimacy** — grief, presence, family, attention: a *social* function with a price on it.
5. **Ritual exceeding function** — ceremonial form bolted onto industrial work.
6. **Inverted valuation** — treasuring refuse, or discarding what everyone else treasures.

> ### 🔓 THIS LIST IS OPEN AND KNOWN TO BE INCOMPLETE — flagged by the developer, 2026-09-01.
>
> **Six is where the list stood on the day it was written, not where it ends.** *"There are some additional
> possible categories for what constitutes 'weird'; I just have some difficulty thinking of what they are, so
> let's mark that for possible future expansion for now."*
>
> **⚠ Do NOT treat a candidate industry as disqualified merely because it maps to none of the six.** The gates
> are Gate 1 and Gate 2. **The sources are a generative aid, not the criteria** — an industry that clearly
> passes both gates and fits no listed source is **evidence of a missing source, not a failed candidate.**
>
> **How the missing ones get found — empirically, not by brainstorming.** Trying to complete this list in the
> abstract is what produced the craft-scene error already. **Instead: when a real industry passes both gates
> and matches nothing above, write it down here as source 7, 8, 9 with the industry that revealed it.** The
> four-city pilot is the first real opportunity, and a run that adds a source has done better work than one
> that only reuses them.
>
> **Sources added since:** *(none yet)*

> **⭐ Two axes, and a qualifying industry needs both: a MOVE supplies the mechanism, a SOURCE supplies the
> derangement.** *Cape Adare's guano scores Move 1 (byproduct→product) and **Source 6 (inverted valuation)** —
> a city whose genuinely non-thematic bulk export is the thing everyone else steps over. **That inversion, not
> the substance, is what makes it work**, and it is why the sweep independently identified it as the model.*
>
> **⚠ Guano is pre-existing canon and stays.** But per the content boundary above, **it is cited here for the
> byproduct-inversion pattern only, and is not a template for finding more material like it.** Future weird
> industries take Source 2 in its other directions — the dead, remains, decay, the discarded — or take one of
> the other five sources entirely.

**Worked, to fix the register:**

- **"The city collects its citizens' breath and sells it back to them as water."** *(Source 1 + 6; Move 1.)*
  **Then:** in a sealed habitat exhaled vapor is a recoverable stream. **It is an air handler with a billing
  department, and it was always going to exist.**
- **"There are people employed to listen to the dome."** *(Source 1 + 5; Move 2.)* **Then:** acoustic
  monitoring for seal failure, where a trained ear beats sensors at anomaly detection. They walk a fixed route,
  daily, listening to a wall.
- **"Paid proxies who live your home life while you are on shift."** *(Source 4; rotation-derived.)* **Then:**
  half the adults are absent half the time and **somebody has to be present in your absence** — school events,
  household, neighbor obligations.

### The generating move

**Every genuine instance of this pattern monetizes something the place treats as a liability, a byproduct, or
an embarrassment.** That is why it reads as absurd for exactly one beat and then stops: the industry is not a
quirk bolted on, it is somebody noticing that the thing everyone complains about has a market.

*(Real-world instances of the pattern, offered as evidence that it is a pattern and not a whim — Siberian
permafrost mammoth-ivory trade; Norilsk reprocessing century-old smelter slag heaps as ore; the Svalbard seed
vault; cold-active enzymes from polar organisms in commercial detergent. **Per the standing rule, these are
sources, not specifications** — see `../Locations-and-Levels/Real-World_Basis_Extrapolation_Method.md`, and
research any of them properly before it becomes canon.)*

**In-corpus, the model already exists and the sweep already identified it**: Cape Adare's **guano extraction**
— *"an ordinary, unglamorous, high-volume byproduct — the city's genuinely non-thematic export,"* which the
sweep called *"the kind of ordinary, unglamorous, specific industry most cities lack."*

### The six moves — ask all six of every instance

1. **Byproduct → product.** The waste stream becomes an export.
2. **Liability → asset.** The condition that makes the place miserable is the one that makes it valuable.
   *(Cold destroys things → cold preserves things. Polar night is punishing → polar night is why the
   instrument works.)*
3. **Extremity → laboratory.** Conditions existing nowhere else make this the only viable site for something.
4. **Isolation → sanctuary.** Nothing can reach it, so site here what must not be reached — archives, vaults,
   quarantine, custody.
5. **Obsolete infrastructure → new tenant.** What was built for a dead purpose is occupied by a live one.
6. **Scarcity → craft.** A thing too expensive to import becomes an entire local trade, with its own training,
   guild structure, and snobbery.

### ⭐ Why this runs off the burden instrument rather than beside it

**Move 2 means an instance's worst burdens are the raw material for its strangest industries.** The instrument
already computes, for every city, exactly which conditions punish it hardest — **so the burden scores are the
generator's own input.** One attribute read, two outputs, pointing at each other: the burden model sizes the
boring tier *and* tells you where to dig for the interesting one.

**This is also what the Distinctive tier is for.** Without LAW G that tier mostly holds purpose-labels —
*"Science 65%"* — which is precisely the flavorless shape the sweep objected to in the first place.

### The honesty gate — three steps or cut it

**The failure mode is quirk for its own sake, which reads as noise rather than character.**

> **State the causal chain from an existing canon attribute to the industry in three steps or fewer.** If you
> cannot, it is not weird-but-inevitable; it is arbitrary. **Cut it.**

*Worked: coastal + biological research already canon → polar fish carry antifreeze proteins → a city
harvesting fish blood for cryoprotectant feedstock, in a nation whose robot population runs on coolant. Three
steps. Sounds unhinged; isn't.*

### Quota, and the calibration that keeps it from becoming a tic

**Reserve the slot in every instance.** **Let the intensity vary.** If all 36 cities have a quirky industry
then quirk is the baseline and stops doing any work — the same convergence trap in fancier dress. **A few
conspicuously plain places make the strange ones land harder**, and for some instances "nothing odd happens
here" is itself the characterization.

> ## The band — developer ruling, 2026-09-01: **0.5% to 8% PER INDUSTRY.**
>
> **The floor is not a rounding error; it is a characterization.** *(Developer's own worked case: Scott — "a
> genuinely decent, quiet place to raise a family," partly inhabited by government workers who commute to
> Fort McMurdo and do not live where they work. **A bedroom city's weirdness budget is 0.5% because a bedroom
> city is where nothing happens, and that is the point.**)*
>
> **8% is a hard ceiling on any SINGLE strange industry.** Past it, that industry stops being the thing that
> gives a place character and becomes the thing the place *is* — the object-colonization failure the Division
> of Industry sweep was originally written to catch, arriving by the front door this time.

### ⚠ The aggregate is a different question — and it is uncapped

**Corrected 2026-09-01, same day, at the developer's direction.** *The band above was first written as a cap on
a city's total weird share. That was wrong, and the case that broke it is instructive.*

> **The developer's counter-case: `{{Abowasa}}`** *(name in braces — provisional, expected to change once its
> origin story is settled; see the standing placeholder-flagging convention).* A city whose residents work
> **multi-day rotations** in Halley or Neumayer — both too distant for a daily commute — living on-site for one
> to three weeks and returning home for one to two. **Its only non-weird industries are the absolutely
> essential ones plus the school.** Proposed aggregate weird share: **25% to 50%+.**

**That is not one industry at 50%. It is eight or ten industries at 3–7% each, none dominant.** **No
colonization occurs.** The per-industry cap was aiming at the right hazard with the wrong instrument.

> ## **Per industry: 8%, hard. In aggregate: uncapped — but it must be EARNED BY A MECHANISM, never chosen.**

**This is a stricter rule than a cap, not a looser one.** A high aggregate cannot be a taste decision; it
requires a stated economic reason why this city's *productive* economy is somewhere other than here. **Absent
such a mechanism, the aggregate stays inside the 0.5–8% band — one strange industry, and that is all.**

### The mechanism that licenses a high aggregate — exported labor

**Where a city's residents earn their living elsewhere, its own economy is left holding only the essential and
the discretionary — and the discretionary, given money and time, becomes strange.** Three real findings, and
the second is what makes it an *industry* rather than a pastime:

1. **The idle-time engine.** Long home rotations concentrate leisure into large, repeating blocks. **Antarctic
   practice already institutionalizes exactly this**: the Australian Antarctic Program provides **"hobby huts"
   — sheds set up for art, craft and woodwork** — plus craft rooms, as standard station amenity. *Craft
   production is treated as necessary infrastructure for mental health, not as recreation.* **The pattern is
   not an analogy to Antarctica; it is how Antarctica already works.**
2. **The money engine.** FIFO home communities gain from **income repatriation** — wages earned at high-paying
   remote sites, spent at home. **Disposable income far exceeds local productive capacity**, which is precisely
   what funds a disproportionate craft economy.
3. **The fracture it creates, free of charge.** The same literature records *"a widening gap between those who
   go away to work and bring back higher than average salaries, and those on lower local salaries."*
   **Essential-services staff cannot rotate** — somebody keeps the heat on — so such a city splits into
   **rotators** (absent, well-paid) and **anchors** (present, ordinary wages).

**⚠ Two guards specific to the high-aggregate case:**

- **Run the differentiation guard INSIDE the city, not only across cities.** Ten weird industries sharing one
  origin ("a hobby that went professional") read as samey to each other — **local monoculture is still
  monoculture.** Seek distinct origins: leisure-derived, material-derived, and **rotation-derived** (outfitting,
  gear storage between shifts, transport brokering — the whole apparatus of arriving and leaving, which is not
  leisure at all).
- **A high-externalization city exposes an undefined term** — see the burden model's note on whether a division
  of industry measures labor performed *in* a place or *by its residents*. For most instances these are the
  same number; here they diverge by half.

**Guard:** weird industries get their own mandatory row in the B6 differentiation table. **Two instances
landing on similar strangeness means at least one is wrong**, and this row is the likeliest in the whole table
to collide, because inventiveness has ruts.

---

## The procedure

**Steps B1–B8. Run `00_RUNBOOK.md` Steps 1–4 first as normal** — bulk mode replaces Steps 5–8 (path selection
through gates), not scoping, intake, or triage.

**B1 — Characterize the shape.** State the repeated question in one sentence, and count the instances. **If you
cannot state it in one sentence, it is more than one shape** — split it and run them separately.

**B2 — Escalate per LAW D.** Work levels 1→4. **Record what resolved at each level**, because the distribution
is the run's main efficiency claim and the only evidence that leverage was actually sought.

> **⚠ LAW A applies with full force here, and bulk mode is unusually good at violating it.** A national-level
> ruling closes hundreds of instances at once — which means **a single wrong ruling is a mass-casualty event
> for canon**, and a ruling that *should* have been the developer's forecloses hundreds of decisions rather
> than one. **Any level-1 or level-2 resolution that is not already canon is RESERVED by default** and goes to
> `Developer_Ruling_Queue.md`. Bulk mode may prepare and present these; it may never settle them.

**B3 — Build the instrument** per LAW E. Name every driver, its source file, its scale, and what it drives.
**Anchor it against real-world or in-canon reference points**, and write the anchors down — an uncalibrated
instrument produces confident numbers with no meaning.

**B4 — Compute the expected value of every cell.** Mechanically. This is the cheap part and it should feel
cheap; if it does not, the instrument is too complex to be worth having.

**B5 — Work the deviations** per LAW F, **and generate the weird slot** per LAW G. **This is where essentially
the entire creative budget goes.** The two are one step deliberately: the deviations tell you which conditions
this instance is unusual in, and those conditions are the weird generator's best input.

**B6 — Run the differentiation guard. Mandatory, not advisory.** Build a table with one row per shape-instance
(the industry, the custom, the attribute) **plus a dedicated row for the LAW G slot**, and one column per
subject, holding **not the computed value but the local form, in one phrase**. **Two cells that read the same
mean at least one is wrong.** This is the direct analog of `Cross_District_Differentiation_Table.md`, and it
exists because the district version's absence already caused a real, recorded failure. **Fill it in the same
commit that completes a row** — the district rule, inherited verbatim, for the same reason.

**B7 — Pilot before committing.** Never run all N. Select a small pilot set:

- **the extremes**, chosen to stress the instrument where it should break;
- **plus at least one deliberately ordinary instance.**

> **⚠ The ordinary one is not optional, and LAW C is the reason.** This project has already shipped *"a
> methodology validated on the least representative configuration in the project."* **An instrument tuned only
> on extremes will be confidently wrong throughout the fat middle where most instances actually live** — and
> the middle is where the homogenization risk is highest, because middling instances have the least to
> distinguish them.

**Declare the falsification test before running the pilot, in writing:** *if the pilot's outputs come out
looking alike, the instrument is broken and the run stops.* A pilot with no stated failure condition is not a
pilot; it is the first batch.

### ⭐ B7a — THE TWO-AGENT VALIDATION PROTOCOL. Added 2026-09-01, at the developer's direction.

> **The observation that produced it, from the developer, after noticing the pattern recur across sessions:**
> *"Over time, across a moderate number of instances, I've noticed you use the term 'self-flattering' (in terms
> of producing, and then checking results). One possible fix… is to run testing via subagents, at a minimum of
> two: one subagent to produce the results, and one subagent to check results."*

**The failure this fixes, stated precisely:** this project's files repeatedly *name* self-audit bias — *"self-
audit error in this project has run in one direction, toward flattering the pass, on every occasion it has
been measured"* — and then proceed to have the same party produce and audit the same result.

> ## ⚠ **NAMING A BIAS IS NOT CONTROLLING IT. A warning label is not a mitigation.**
>
> *(Worked case, and the one that prompted this: a Denison model test was predicted to fail, failed, and was
> then supplied — by its own author, in the same breath — with an explanation for why the failure was
> acceptable. The warning about post-hoc rationalization was written directly above the rationalization.)*

**The control: separate the party that produces a result from the party that judges it.**

| Rule | Why |
|---|---|
| **Both agents FRESH. Never a fork.** | A fork inherits the author's full context, including the rationalizations. It reproduces the bias with extra steps |
| **The checker gets the INPUTS and the CRITERION — never the conclusion** | The prompt is the leak. *"Verify that X is acceptable"* has already smuggled the answer in |
| **The checker reads the same SOURCE FILES, not a summary of them** | Whoever selects the evidence selects the finding |
| **Adverse findings are relayed VERBATIM** | The agent's report is not shown to the developer. The relay is the last place the bias can re-enter, and it is a commitment rather than a mechanism |

### The strongest form is not "check my work" — it is INDEPENDENT RE-DERIVATION, then diff

**Asking a checker to audit a result anchors it on that result.** Instead: **give it the same inputs and the
same spec, have it compute the answer itself, and compare the two.** Disagreement then localizes to a specific
driver, weight or reading — **one concrete argument, rather than a debate about whether a conclusion feels
acceptable.** Combined with the pre-registered falsification criterion above, the protocol is: **criterion
written down first · two independent derivations · diff.**

**Instruct the adversarial checker to build the strongest case AGAINST its own conclusion, and to state what
evidence would change its mind and whether that evidence exists.** A checker that only reports a verdict has
done half the job.

### ⚠ The honest limit — this buys PROCEDURAL independence, not EPISTEMIC independence

**Both agents are the same model with the same priors.** **It kills motivated reasoning** — the *"I already
committed to this, let me defend it"* failure. **It does nothing for a shared blind spot:** a weight any
instance would choose, or a canon file any instance would misread, fails identically in both and comes back
looking like agreement. **Two confident agreeing agents are not corroboration.**

**The existing guard against *that* is different and remains mandatory: paste raw output, never summarize it**
— put the unprocessed thing in front of the developer. **The two controls cover different failures and neither
substitutes for the other.**

### When to use it

**Use:** model validation runs · QA gates · readiness checks · any point where the author would otherwise be
auditing their own output · **any hypothesis whose survival is convenient for the person testing it.**

**Do not use:** routine writing, research, or edits. **There is no bias to control there, and the cost is
real.** Two agents on every file edit is waste, not rigor.

**B8 — Deposit** per `03_Deposit_Discipline.md`. **One shared provenance tag identifying the bulk run**, plus
each instance's own marker. **Kind-classification does not get to be bulk**: derived values are conclusion-tier
and must carry conclusion-tier markers wherever they land in an otherwise-attribute file, per LAW B. **The
volume is exactly why this matters** — a bulk deposit of unmarked conclusions is the Cape Adare contamination
chain, multiplied by N.

---

## The output block

Extends `00_RUNBOOK.md` Step 9's block. **The LAW D, F and G lines are the ones that make a bulk run
reviewable, and all three are easy to omit precisely because they are the ones that would show a run coasted.**

```
## Bulk Gap Resolution Run — <shape> — <date>

**Shape:** <the one-sentence repeated question>     **Instances:** n
**Resolved by level (LAW D):** universal n · national n · class n · instance n
**Instrument:** <drivers, and where each is already-canon>   **Anchors:** <calibration references>

**RULINGS ROUTED (n):** <level-1/2 resolutions sent to the developer — NOT settled here>
**DEVIATIONS WORKED (n):** <instance — expected vs. actual, and the reason, which is the content>
**WEIRD SLOTS FILLED (n):** <instance — the industry, and its ≤3-step causal chain (LAW G)>
**FLAT CELLS (n):**       <computed, unremarkable, deposited without further work — state the count honestly>
**PROTECTED (n):**        <instances deliberately left open, and why>

**Differentiation guard:** <rows filled; any collisions found; how each was resolved — including the LAW G row>
**Pilot:** <set, falsification test as declared in advance, and whether it passed>
**Variance check:** <spread of the headline value across instances — the anti-convergence evidence>
```

**A bulk run reporting a high CLOSED count and a low DEVIATIONS count has not done the work.** It has
filled cells. Per LAW F, the deviations are the deliverable; the flat cells are the byproduct.

---

## When NOT to use bulk mode

- **Fewer than ~15 instances.** The instrument costs more than it saves; run base mode.
- **The instances only look alike.** If the shared shape is superficial and each case turns on genuinely
  different reasoning, bulk mode will flatten real distinctions into a formula. **Test: can you name the
  drivers before you look at the instances?** If not, they are not one shape.
- **The gap is RESERVED at the shape level.** If the whole question is the developer's call, bulk mode's only
  legitimate output is a well-prepared ruling request.
- **The instances are people.** *(`00_RUNBOOK.md` Step 1: person-scope skews heavily RESERVED and SCAFFOLD.)*
  **Characters are not cells**, and a scoring instrument applied across a cast is a machine for producing
  interchangeable ones. Bulk mode is for attributes of places and systems.
