# Davis — `T8` ROUNDS, STEP 3 · RAW

**The evidence `03_Research.md` rests on.** *Written 2026-09-15.*

> ## ⛔ WHERE THE SEARCH RECORDS LIVE — they are NOT in this file
> **Every verbatim search string, rejected source, dead end and open thread is in
> `…/Cities/Research_Logs/Davis_Research_Log.md`** *(1,943 lines)*, **per the standing convention that a
> location's research log is a separate, durable, append-only artifact.**
> ⭐ **This file carries the three researchers' FINDINGS, their proof blocks, and the three rounds.**

---

# THE THREE ROUNDS

| Round | What it does | Result |
|---|---|---|
| **1** | Three researchers, identical briefs, dispatched in parallel, no knowledge of each other | **A:** 78 queries + ~35 fetches · **B:** 57 index queries + 42 retrievals + 2 local computations · **C:** 39 searches + 64 fetches. ⭐ **~310 retrieval operations** |
| **2** | `Tools/triple_read_verify.py` — mechanical ground truth against the bytes on disk | ✅ **`UNANIMOUS — CLEARED TO WRITE`. 15 of 15 field-sets byte-exact** (3 × 5 files) |
| **3** | Peer cross-check — same three agents continued, context intact, **plus an explicit per-pick EXHAUSTION TEST** | ✅ **All 6 cross-verdicts `CONSISTENT`** · **3 substantive corrections, one against the pass owner** |

> ## ⭐⭐ ROUND 3 HAS A DIFFERENT JOB AT A RESEARCH STEP, AND THE TEMPLATE SAYS SO
> **`PRE-TRIP_INSPECTION_RECIPE_TRIAL.md`, Step 3's own `T8` line:** *"`LAW 0-R` binds here: a source is not
> exhausted because it was searched once — **the cross-check in Round 3 is where that gets tested, not Round
> 2.**"*
> ⭐ **So each researcher was required to answer SPENT / NOT SPENT for every pick, and to name the single
> specific document, query or question that would change the answer.** ⛔ *"More research would help" was
> explicitly disallowed.*

## ⭐ WHAT ROUND 3 CAUGHT

| # | Correction | Held by | Caught by |
|--:|---|---|---|
| **1** | ⭐⭐ **"Salt, NOT freeze–thaw"** — the source establishes salt's presence and pattern; it **does not compare against frost and does not exclude it** | **A**, then ⚠ **propagated into a repo file by the PASS OWNER** | **C** flagged it independently; **A conceded against itself**; **B supplied the settling mechanism** |
| **2** | ⛔ **The generalist-obligation reframe carried to settlement scale** — *every* supporting case is **tens** of people; Davis is **1,158,314** | **A** | **C** |
| **3** | ⛔ **Generalizing the refusal finding** — **n=1** on primary-source evidence; a codified colonial instrument is not an organic assembly | **A** *(3 mixed-quality cases)* | ⚠ **B, against its own strongest result**; **C** concurred |
| **4** | **A support ratio stated as a point value** *(7:1 vs 4:1)* | A / B | **Adjudicated as a SCOPE DIFFERENCE — recorded as a range, `4:1 – 7:1`** |

> ### ⭐⭐⭐ CORRECTION 1 IS THE ONE WORTH READING TWICE — **`M-158` at four levels**
> **The book qualified itself** *("best seen in WET climates")* **and the extraction correctly refused to infer
> past it** → **a researcher over-read its source as excluding frost** → ⚠ **the pass owner accepted that
> receipt on trust and wrote it into the repo as settled** → **a peer caught it, the author conceded, and a
> third supplied the mechanism.**
> ⛔ ***Only the peer cross-check caught the middle two. No QA gate would have.***
> ### ***`T8` Round 2 proves a reader opened a file. It proves nothing whatever about a research claim.***

---

# ⛔ ROUND 2 — MECHANICAL GROUND TRUTH, RAW OUTPUT

```
python3 Tools/triple_read_verify.py \
  Davis/.t8_required_step3.txt \
  Davis/.t8_step3_readerA.md  Davis/.t8_step3_readerB.md  Davis/.t8_step3_readerC.md
```

```
required files: 5
agents: agent1, agent2, agent3

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md  [range 2526-2620] ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/Real-World_Basis_Extrapolation_Method.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Stepwise_Execution/01_Spine/S05_Step_3_Research_aimed_at_what_Step_2_named.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/README.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Davis/02_Spine.md ===
  agent1   ✅ all fields match ground truth
  agent2   ✅ all fields match ground truth
  agent3   ✅ all fields match ground truth

=== VERDICT ===
UNANIMOUS - CLEARED TO WRITE
```

---

# ⭐⭐ ROUND 3 — PEER CROSS-CHECK, RAW

**Design: the lightweight form — the SAME three Round-1 agents continued by `SendMessage`, context intact.**

## ROUND 3 · READER A

# ROUND 3 ADDENDUM — appended 2026-09-15, after peer cross-check

**Appended after the PROOF blocks so the verified Round-2 body is untouched.**

## R3.1 — The salt-line claim, NARROWED on my own source

**Source:** Gore & Leishman, *Bunger Hills palaeowinds*, Antarctic Science (Macquarie PDF), publisher line
numbers **258–262** and **710–723**. Two verbatim claims: **"At Vestfold Hills and Bunger Hills, tafoni were
only found in areas of the most salt-weathered bedrock, suggesting a causal linkage between the intensity of
physical weathering and the occurrence of tafoni"**; and the salt line **"divides an area to the east that is
rich in vegetation and with relatively unweathered bedrock and an area to the west where physical weathering of
the metamorphic basement creates abundant sand."**

⛔ **CORRECTION TO PART A §4.4.** The source establishes salt crystallization as the **operative agent of the
cavernous forms and of the spatial pattern**. **It never runs a comparison against freeze–thaw and never
excludes it.** My phrase *"not freeze–thaw"* overstates the source. **`M-158` applies to me here: the source's
silence is not a negative.** The 60 annual zero-crossing days remain live, and the quantity that would settle it
is the **count of crossings of the −3 to −8 °C segregation window**, which no reader has.

## R3.2 — Dead-end taxonomy: adopting **TOOL-DEATH**

**One name, one definition:** ***TOOL-DEATH — the query never reached a source index, because the instrument
refused: a session cap or quota, HTTP 403/429, a CAPTCHA, a size limit, or an engine that discarded the query
terms.*** It is **a fact about the toolchain, not about the world**; it is **re-runnable verbatim**, which is why
the string must be logged. My *engine-death* and *infrastructure* rows and Reader C's *budget-death* are
subclasses and are hereby folded in. **Bias confirmed:** after the 200/200 cap my mix shifted to encyclopedic and
peer-reviewed sources — which **helped Pick 4 and hurt Picks 1 and 3**, whose material is ethnography, statistics
and grey literature.

## R3.3 — Pick 1 re-read on Reader B's primary texts

My §1.11 recorded "no case found of a community with no refusal instrument of any kind." **B's reading of the
Tristan ordinances narrows that correctly: the instrument exists and is not communal.** It converges with my own
§1.6 (a governor may reject the incomeless; a site operator demobilizes). ⇒ ***In all three documented cases the
power over a person's presence sits with an external or administrative office, while the community's own body
governs work, land, stock and amenities.*** **The absence of a COMMUNAL instrument of refusal is a common
structural feature of isolated communities, not a peculiarity.** ⛔ What follows for Davis is not this step's.

## R3.4 — Pick 3 reframe, scope stated

Single secondary source: [Cool Antarctica, *Find a job in Antarctica*](https://www.coolantarctica.com/Community/find_a_job_in_antarctica.php),
wording **"On many bases there is the expectation and requirement that all staff will fulfill generalist roles."**
**Scope: an aggregator's generalization across programs — "many bases," not one published policy.** Already
flagged at open thread 15; **it needs one primary corroboration before anything downstream leans on it.**
⚠ **Not a contradiction with Reader B's "roughly four support staff per scientist" vs my "roughly seven to one":
different sources, different scopes. Record as a RANGE (~4:1 to ~7:1), not as a conflict.**

## ROUND 3 · READER B

## ROUND 3 — PEER CROSS-CHECK (Reader B)

**Verdicts: Reader A — `CONSISTENT`. Reader C — `CONSISTENT`.** *Same material at the overlaps (Fogbank's
impurity, Polanyi, Lave & Wenger, Mau Piailug, Hirschman, ostracism, blackball, `murahachibu`, Hutterite lots,
Longyearbyen, Vestfold extent variance, sublimation-dominated ablation, the −3 to −8 °C frost window). No claim
contradicts mine. Each holds sources I could not have produced — A: **Gore & Leishman**, the guild masterpiece,
the Ise 20-year rebuild, **Liberty-ship knowledge decay at 3–6%/month**, the 7:1 support ratio; C: a
laser-reconstruction controlled case, Norilsk. All are addressed and findable.*

### 1 · The salt line — ⭐ **CONFIRMED BY MECHANISM from my own retrievals, with two caveats I own**

**Confirmed.** My frost source: ice segregation dominates, window **−3 to −8 °C**, and **"unavailable moisture
limits damage regardless of temperature."** My Europe PMC source: these soils are **hyperarid**. My lake data:
salinity **4–235 g/L**, one body at **~270 g/L**, six marine basins plus seven seasonally isolated ones.
⭐ ***The frost reagent is scarce here and the salt reagent is superabundant.*** A's site-specific paper supplies
what I could only infer. **I withdraw my §4.5 framing of the two as merely "co-located": on reagent
availability, salt is the dominant term, and A is right.**

**What freeze–thaw is doing with 60 zero-crossing days:** ⛔ **crossing 0 °C is not the damage window.** The
window is −3 to −8 °C **with liquid water present** — so the 60 days are an upper bound on *occasions*, not a
count of *damaging cycles*, and most crossings happen in the thawed, drained warm months when water drains
rather than segregates. **Both processes are real; they are not competing for one slot.**

**Two caveats, raised not resolved:** *(a)* Gore & Leishman's transport mechanism is **winds >10 m/s** —
roughly double this site's canon mean of **~5.6 m/s** *(`02` §2.1)*. **Mean is not peak, so this is not a
refutation** — but the gust distribution is unstated and `M-158` forbids inferring it. *(b)* The paper's primary
subject is **a different oasis**; the Vestfold statement is a comparative aside. **A SCOPE, not a contrast.**

### 2 · The dead-end taxonomy — ⭐ one name, one definition

> ## **`TOOL-DEATH`** — *the retrieval never reached an index or a document because the CHANNEL refused.*
> **Causes, tagged not separated: `quota` · `host` · `capability`.** *(Subsumes C's budget-death, A's
> engine-death and infrastructure-blocks as causes of one class.)*
> ⭐ **The diagnostic that separates it from the other two: re-run the identical query on a different channel.
> If it returns, the death was the tool.** ⛔ **Query-death and source-death are both claims about the world;
> tool-death is a claim about nothing** — the query may be perfect and the source present, and **you have
> learned neither.**

**And the bias statement, precisely, because it is worse than missing coverage:**

> ⛔⛔ **The cap did not sample my sources at random — it TRUNCATED THEM IN TIME, and the surviving channels were
> not a random subset.** **My first 31 retrievals ran on a general web index. Every one of the ~60 after the cap
> ran on Wikipedia's search API, Europe PMC, or a known document URL** — because those were the only channels
> that answered. ⭐ ***So the corpus is systematically weighted toward encyclopedic and peer-reviewed material
> and away from trade, journalistic, ethnographic and practitioner sources — and the weighting correlates with
> PICK ORDER, because picks are worked in order.*** **Picks 1–2 were researched under one source regime and
> Picks 3–5 under another.** ⚠ **A reader comparing pick depth across this log is partly measuring the cap.**
> ⭐ **Recorded as a confound in the instrument, not a gap in the coverage.**

### 3 · The limit of the Tristan result

**(a) ⛔ I have NO grounds to generalize. `n = 1`.** Every structural feature I found has an equally good
particular explanation: it is a **British Overseas Territory**, so an appointed Administrator and a reserved
Governor are constitutional furniture, not a discovery about isolation. **My one attempt at a second case
(Pitcairn) failed at both routes** *(403, 404)*. ⭐ **Until a second corpus is read, the honest statement is:
*one community's written law places person-power outside the community* — not *isolated communities do.***
⚠ **And A independently found the same shape at a modern isolated settlement** — *"people without a source of
income can be rejected by the governor"* — **which is suggestive and still is not a pattern.**

**(b) ⭐⭐⭐ YES — and I think it matters more than the documented absence.** **A third mode is documented here:**

> ### **AUTHORITY BY PRACTICE — a body exercising a real, consequential, merits-based refusal over named persons that NO instrument confers on it.**
> **Not communal authority** *(the Council's twenty-one statutory heads do not reach a person)*. **Not external
> authority** *(the Administrator holds that, and this is not him)*. ⭐ **A third thing: an unwritten power that
> is nonetheless published, procedural and routinely used** — police certificates, merits evaluation, a stated
> public-interest test, a £500 fee.
> ⭐⭐ **Its properties are the finding:** *it has a procedure but no jurisdiction; it can be described but not
> cited; it cannot be appealed because there is nothing to appeal against; and **it cannot be abolished,
> because there is no instrument to repeal.*** ⛔ **Whether a later ordinance confers it is my one honest
> unknown, and this reading is falsifiable by that document.**

### 4 · Reader A's Pick-3 reframe — ⭐ **SUPPORTED, by two things I retrieved independently**

A's *"all staff will fulfill generalist roles"* is **corroborated twice in my own material.** *(i)* The settlement
inventories: a school with **two teachers**, a bank with **one banker**, a hospital with **one doctor and one
nurse** — ⭐ **at ones and twos, a "class" of general workers is arithmetically impossible; the work has to be
an obligation on people who also do something else.** *(ii)* Schedule 3 head **(l): "the performing of public
work"** — a by-law power over **a duty**, not over an occupation.

⚠ **But it does not replace the majority finding, and A's own numbers say so:** **7:1** support-to-science, a
named trade list, **>85 buildings**, a power plant, a water plant, a waste plant. **A settlement runs both: a
staffed specialist support majority AND a general obligation laid on everyone.** ⭐ **The reframe is that the
steer's phrase *"the non-specialist majority"* presumes one structure where the sources document two.**
⛔ **Which a place has is not this step's to decide.**

### 5 · ⭐⭐ THE EXHAUSTION TEST

| Pick | Verdict | ⛔ The single thing that would most change the answer |
|---|:--:|---|
| **1** | ⚠ **NOT SPENT** | **The instrument conferring the Tristan Council's visitor-refusal power — or proof that none exists.** *Everything in §3(b) turns on it, and it is one document.* |
| **2** | ⛔ **NOT SPENT, and least spent of the five** | **Rothamsted's long-experiment protocols and `e-RA` documentation.** *All three of us found the loss side; **nobody found a case of unwritten practice successfully transmitted across generations of staff who never met** — and A's OpenAlex query on that exact question returned **zero works**. That null is now confirmed twice and is the pick's real hole.* |
| **3** | ⚠ **NOT SPENT** | **One remote settlement's actual occupational census.** *Statistics Norway's Svalbard employment series. Three readers produced ratios, rosters and inventories; **none produced a breakdown**, and A's reframe cannot be tested without one.* |
| **4** | ✅ **SPENT on light and lakes** *(computed 38/49-day conventions, 55-day midnight sun, no day without civil twilight; heliothermal confirmed in the peer-reviewed literature)* · ⚠ **NOT SPENT on rock** | **Adamson & Pickard 1986 and Gore et al. 1996** — cited for the salt line by A's own source, **read by nobody.** *They hold whether the line moves, how sharp it is, and whether east/west generalizes.* ⭐ **C names the complementary quantity: the freeze–thaw CYCLE COUNT in the −3 to −8 °C window — which three of us lacked and which is computable.** |
| **5** | ⚠ **NOT SPENT on institutions** *(greenhouse fully quantified; limnology joined to Pick 4)* | **Jon Gertner, *The Idea Factory*.** *The registered topic is the history of multi-disciplinary institutions, and **all three of us hit source-death on how such a place is actually organized.** The encyclopedic layer is exhausted; the book layer is untouched.* |

> ⭐⭐ **Three of five picks are NOT SPENT for the same reason, and it is not laziness: their answers are in
> BOOKS AND PRIMARY DOCUMENTS, not on an index.** *The one pick I did spend is the one where I stopped querying
> and fetched the statute.* ⛔ **`LAW 0-R` says a pick is not exhausted because it was searched. This round says
> something narrower and sharper: several of these picks were never searchable.**

---
---


## ROUND 3 · READER C

# APPENDIX C-1 — ROUND 3 PEER CROSS-CHECK (Reader C)

*Appended 2026-09-15 after Round 2 cleared 15/15 byte-exact. Nothing above this line was altered. The PROOF
blocks were written to be last in the file; they are now followed by this appendix, which was added at the
coordinator's instruction after those blocks were verified.*

## §C1.1 — Per-agent verdicts

**Reader A — `CONSISTENT`.** Same material covered on Picks 1, 2, 4, 5; A went deeper than me on the scientific
literature (OpenAlex/Crossref) and shallower on the refusal ethnography. **Claims I could not have produced and
cannot independently verify:** the Gore & Leishman salt-line quotation and the Fogbank impurity detail — both are
direct quotations with locatable citations, both are *consistent with* my own sources (my Tafoni source states
"most workers have advocated salt weathering as the primary explanation"; my MacKenzie & Spinardi source states the
uninvention thesis Fogbank instantiates). **Accepted as plausible, marked unverified by me.**
**Tensions, not contradictions:**
- A reports a **fourth** ice-free area figure — **200 km²** (AntarcticGlaciers.org) — against my 400/420/512. The
  spread is therefore **200–512 km², a factor of ~2.5**, worse than I recorded. ⭐ **Adopt A's wider range.**
- A gives **Deep Lake at ~270 g/L** and winter water **as low as −20 °C**; the Vestfold Hills envelope I used caps
  at **235 g/L / −14 °C**. ⚠ Most likely the envelope is the **meromictic-subset** range and Deep Lake's figures
  are whole-lake. **Not reconciled. Do not average.**
- A cites **winds >10 m/s** as the salt-transport mechanism; `02_Spine.md` §2.1 gives a mean of **~5.6 m/s**. A mean
  does not preclude events above 10 m/s — ⛔ **but nothing either of us read establishes their frequency at this
  site.** `M-158`: the unstated half must not be inferred.

**Reader B — `CONSISTENT`.** B reached primary legal instruments I did not attempt. **Claim I could not have
produced:** the verbatim Schedule 3 enumeration and the Entry Control Ordinance sections. **Accepted**; the
structure it describes independently matches A's §1.6 (an administrator holds the person-power) and my A1.5
(refusal relocated to the gate), which is three-way convergence from three different evidence types.

## §C1.2 — ⭐⭐⭐ QUESTION 1 — A'S SALT LINE AND MY SALINITY ENVELOPE ARE **ONE PHENOMENON**

**They connect, and the connection is causal, not analogical.**

| Step | Fact | Source |
|---|---|---|
| 1 | Lakes here are **"generally saline or hypersaline near the coast, and fresh… near the Antarctic Plateau"** | A, §4.2 (*J. Glaciology*) |
| 2 | Winds **>10 m/s** "create salty spray **from the marine inlets and saline lakes** and transport salt aerosols" | A, §4.4 (Gore & Leishman) |
| 3 | Tafoni occur **"only… in areas of the most salt-weathered bedrock"**; the **salt line** divides east (vegetated, **relatively unweathered bedrock**) from west (sand-generating, lichen-inhibiting) | A, §4.4 |
| 4 | **Varves form only in fresh or brackish water** — "salt water causes clay particles to coagulate uniformly year-round, preventing distinguishable annual separation" — and require **anoxia / no bioturbation** | C, A4.3 (*Varve*) |

> ### ⭐⭐⭐ THE JOINT FINDING NEITHER OF US COULD REACH ALONE
> **The saline basins are the SOURCE of the airborne salt that destroys the rock — and they are the same basins
> that cannot keep an annual ledger.** The fresh basins, which *can*, sit on the side of the ground whose bedrock
> is sound and whose lichen survives.
> ### ***One gradient does both jobs: it decides which water can hold a dated record, and which ground is being eaten.***
> **The archive-keeping half of the lake system and the rock-preserving half of the land are the same half.**

⛔ **THE STRICT CAVEAT, AND IT IS LOAD-BEARING.** The two axes are stated on **different bases**: the salinity
gradient runs **coast → plateau**; the salt line runs **west | east**. **No source either of us read states that
these are the same axis.** They are *plausibly* the same (the coast lies west of the plateau at this site) — and
plausibility is exactly what `LAW 0-R` warns about. **A's own open thread 4 flags it: whether "east/west" is a
general rule of the site or a local observation is unread.** ⇒ ✅ **The convergence is recorded as a HYPOTHESIS
WITH A NAMED TEST**, not as a finding. **The test is Adamson & Pickard 1986 and Gore et al. 1996** — cited by Gore
& Leishman, read by neither of us. **Those two papers are now the highest-value unread documents in this step.**

## §C1.3 — QUESTION 2 — THE DEAD-END CLASS: ONE NAME, ONE DEFINITION

My framing has priority, but **"budget-death" names only the cap and does not cover A's rate-limits, CAPTCHAs and
403s from search engines, which are the same failure.** Coverage should beat priority, so I propose the wider word
and cede mine as a sub-kind:

> ## **CHANNEL-DEATH** *(sub-kinds: budget · rate-limit · CAPTCHA · block)*
> **Definition:** *the query was never put to any index and no source was ever consulted, because the retrieval
> channel itself refused.*
> **The diagnostic that separates it from the existing two:** ⭐ **query-death teaches you something about your
> framing; source-death teaches you something about the world; CHANNEL-DEATH teaches you nothing about either,
> and is cured by a different session, a different tool, or waiting.**
> ⛔ **Why the convention must gain it:** a capped query filed under "query-death" tells the next session the
> framing was wrong when it was fine, and a capped query filed under "source-death" tells it the material does not
> exist. **Both are false in the same direction — toward treating an unrun pick as spent.** That is `LAW 0-R`'s
> exact failure mode arriving through the log's own vocabulary.

*(Reader B's "tool-death" and Reader A's "engine-death" are the same class; all three of us hit the identical
200/200 cap. Three independent discoveries of one missing category.)*

## §C1.4 — QUESTION 3 — DOES B'S TRISTAN FINDING CONVERT MY UNASSERTED NEGATIVE? **PARTLY. BE STRICT.**

**What I claimed (A1.8):** the St Kilda parliament is *not recorded as* deciding about persons. **That was an
argument from silence in a single secondary source, and I flagged it as such.**

**What B produced is a different and stronger kind of evidence:** not a silence but **an exhaustive enumeration.**
Schedule 3 of the Island Council Ordinance lists **21 heads** of by-law power — and **not one reaches a person's
admission, residence, membership, exclusion, expulsion or removal.** An exhaustive list that omits a power is a
**positive** absence. Meanwhile the person-power demonstrably exists and is held elsewhere: *"no person may remain
in Tristan da Cunha for a period exceeding 3 days unless the person is in possession of a valid permit signed by
**the Administrator**"*, revocable *"at any time… as he or she thinks fit."*

⛔ **So, strictly:**
1. **It does NOT license the generalization** *"communities of this type do not adjudicate persons."* Two cases is
   two cases, and the second is a codified colonial-era instrument, not an organic assembly — a **different object**
   from a morning street meeting.
2. ✅ **It DOES convert the underlying structural claim**, which was the one that mattered: **allocation and
   adjudication are separable, and the separation is not an accident of what got recorded — in at least one case it
   is written into law, head by head.** My A1.8 rested on that separability. **It now stands on an enumeration
   rather than on a silence.**
3. ⭐⭐ **And it changes the shape of the answer, which is more valuable than confirming it.** B's case is not
   *"nobody decides about persons."* It is ***"somebody does, and it is not the people who live there."*** That is
   A's §1.6 (a governor may reject; removal is demobilization by the operator) and my A1.5 (refusal relocated to
   the gate, impersonal) arriving from a third direction — **statute.**
4. ⛔ **AND IT IS THEREFORE A QUESTION THIS PASS MAY NOT CLOSE.** In every real case the person-power sits with the
   parent. **`02_Spine.md` §5.3 / `PA-6` hold that Davis's parent is UNWRITTEN — *"what the parent determines
   returns UNKNOWN, which is not NOTHING."*** ⇒ **The three-way convergence names precisely the thing the pass has
   ruled it cannot know.** Handed forward as a live question, not as a filled slot. `NO FORCED FIT`.

**My open thread 12 therefore survives, narrowed:** the remaining test is the St Kilda primary accounts
(Martin Martin 1698; Macaulay 1764), because an *organic* assembly with the same separation would be the case B's
statutory one cannot supply.

## §C1.5 — QUESTION 4 — A'S GENERALIST REFRAME: **SUPPORTED AT ONE SCALE, UNDERCUT AT ANOTHER**

A's source: *"On many bases there is the expectation and requirement that all staff will fulfill generalist roles
such as unloading ships, washing-dishes, night-watch, cleaning the base, dealing with the trash."*

**My material supports it from an unexpected side, and undercuts it on scale.**

| | Evidence | Direction |
|---|---|---|
| **Supports** | My coal-town layer: work that "was never an occupation at all — neither paid nor recorded," whose largest component was **moving and heating water** (A3.5). **General work done by people with no job title for it** is the same phenomenon A names, in a settlement rather than a crew | ✅ |
| **Supports** | Benedictine ch. 24: the disciplined monk is excluded from table and oratory but **"shall be alone at the work assigned him"** — the obligation is not transferable to a class | ✅ |
| **Undercuts** | My USAP evidence is organized **by department and by contract** — waste, cargo, lodging/food/recreation/retail/post, IT, infrastructure, medical, construction — **which is a class structure, explicitly procured as one** (A3.2) | ⛔ |
| **Undercuts** | Economic base theory's **~1:1 basic/non-basic ratio** is a *class* model and is the only quantitative handle either of us has on the 40% (A3.1) | ⛔ |

> ### ⭐⭐ THE RESOLUTION, AND IT IS A SCALE RULE
> **Every generalist-obligation case in the combined corpus is a CREW — tens of people** (A's "many bases"; the
> 13-person and 9-person winter crews; a 56-person base including 10 families). **Every class-structure case is a
> SETTLEMENT — thousands** (the ~3,000-person program procured by department; the ~2,817-person Arctic town with
> three kindergartens and 45 teachers; the 2,256-person mining town; the 176,735-person industrial city with 80
> education institutions).
> ⛔ **A generalist obligation is documented at crew scale. It is documented NOWHERE at settlement scale.**
> ⇒ **A's reframe is real and must be carried — but as a fact about small closed crews, not as a template that
> survives multiplication.** ⭐ **The honest statement is that the corpus contains no case of the generalist
> obligation persisting past the point where a settlement can afford a class**, and neither of us searched for the
> transition. **That transition is the unasked question of Pick 3.**

## §C1.6 — QUESTION 5 — THE EXHAUSTION TEST

| Pick | Verdict | **The single specific thing that would most change the answer** |
|---|:--:|---|
| **1 — refusal** | ⛔ **NOT SPENT** | **Martin Martin, *A Late Voyage to St Kilda* (1698), and Macaulay (1764)** — the primary accounts. The question they settle: **did that assembly ever rule on a person, or only on work?** B's ordinance answers the statutory case; only these answer the *organic* one, and my A1.8 rests on it |
| **2 — tacit competence** | ⛔ **NOT SPENT** *(but the target has MOVED)* | ⭐ A's OpenAlex `count: 0` converts my refused handover query from an open thread into a **genuine source-death** — that sub-part is now closed as an absence. **What replaces it: the IAEA knowledge-management series on nuclear workforce knowledge loss** (my refused query #2, unrun by all three of us). It is the one body of work that has written *procedures* for the problem `D3b` names |
| **3 — the general population** | ⛔ **NOT SPENT** | ***The Polar Journal*, "The diversity of overwintering groups in Antarctica and the limitations of psychological studies" (HTTP 403).** It very likely carries the occupational composition of winter crews **and** a critique of studies that over-sample scientists — which is simultaneously Pick 3's missing number and the test of §C1.5's scale rule |
| **4 — the physical site** | ⛔ **NOT SPENT — and it is the least spent of the five** | ⭐⭐⭐ **Adamson & Pickard 1986 and Gore et al. 1996**, the two papers Gore & Leishman cite for the salt line. **They decide whether §C1.2's convergence is one phenomenon or two**, by stating the salt line's axis, geometry and stability. **Highest-value unread document in the whole step** |
| **5a — greenhouse** | ⛔ **NOT SPENT** | **The DLR/EDEN ISS operational reports** — specifically **crew-hours per week to run a polar greenhouse.** The only number in the corpus that would let anyone size a grower workforce against the 60/40 split |
| **5b — limnology** | ✅ **SPENT for this step** | Three angles run (paleolimnology · varves · meromixis), the convergence found, and A independently reached the primary Antarctic Science paper and a 650-year diatom-salinity evaporation record. Further depth belongs to a later phase, not to Step 3 |
| **5c — multi-disciplinary institutions** | ✅ **SPENT** | Two models obtained (seasonal multi-institution; no-teaching institute) plus Feynman's objection naming the lost correction loop. ⛔ **`NO FORCED FIT`: the pick's remaining yield is thin, and saying so is the result** |

**Overall: 5 of 7 sub-picks NOT SPENT.** ⛔ **No pick should be logged as covered on the strength of this round.**

---

# ROUND 1 — THE THREE RAW FINDING SETS

> ⚠ **As written, BEFORE Round 3 corrected them — they therefore contain the four corrections listed at the top of this file.** **`03_Research.md` is the corrected synthesis.** ⛔ **Do not cite a claim from this section without checking it there first.**


## ROUND 1 · READER A — findings, raw

---

# Davis — Step 3 · RESEARCH · Reader A

**Date:** 2026-09-15 · **Frame:** Second Interwar (default) · **Point in procedure:** `00_RUNBOOK.md` Step 3, run
after Step 2 named the deficit. **Governing:** `LAW 0-R` (research fully; no time limit, no search budget) ·
`LAW 0` (depth over speed) · the GPS law · ONE LOCATION, ON ITS OWN TERMS · NO FORCED FIT · rules 3.1–3.5.

**What this file is:** Part A records what the real world actually says, organized by pick. Part B is the
research log in the `Research_Logs/README.md` convention. **Neither part states a conclusion about Davis.**
No institution, practice, custom, festival, person, demonym or price is invented anywhere below.

> ### ⚠ SESSION CONSTRAINT, RECORDED BECAUSE IT SHAPED THE METHOD
> **The `WebSearch` tool hit a hard session cap (200 of 200 calls) partway through Pick 3.** Research continued
> by fetching search engines and scholarly APIs directly. **Brave Search worked, then rate-limited (HTTP 429)
> and stayed limited; DuckDuckGo served a CAPTCHA; Mojeek and Ecosia returned 403; Bing returned results
> unrelated to the query terms; Semantic Scholar returned 429.** **OpenAlex and Crossref worked throughout and
> carried the scientific picks.** Every blocked attempt is logged in Part B §3 with its exact query string, so
> the next session knows which door is shut and which is open.

---
---

# PART A — RESEARCH FINDINGS

Each finding carries its source and is marked **`[CHANGED]`** *(it moved what this pick yields)* or
**`[ORNAMENT]`** *(it decorates something the pick already had)*. "Aimed at" names the deficit the research was
run against; it is not a claim about what Davis does with it.

---

## ⭐⭐ PICK 1 — THE ABSENT INSTRUMENT OF REFUSAL

*Rule 3.1: the profile says what the place cannot do; find a real culture that has it, and the contrast writes
the finding.* **Aimed at: `D2` — no social instrument of refusal or subtraction, no body that decides about a
person at all (`02_Spine.md` §2.3, §3.2, §5.2, §7.2).**

### 1.1 The decision rule is the variable, not the existence of the instrument

Real communities that hold a refusal power differ far less in *whether* they have one than in **what threshold
it takes to fire and who is allowed to pull it.** The measured spread is wide:

| Mechanism | Who may refuse | Threshold | Source |
|---|---|---|---|
| **Blackball** (gentlemen's clubs, Masonic lodges, fraternities; recorded from the late 18th c., ballot-by-ball practice far older) | any single member, anonymously | **one black ball rejects; acceptance must be unanimous** — "the candidate would never know who had 'blackballed' him" | [Blackballing, Wikipedia](https://en.wikipedia.org/wiki/Blackballing); [Oxford Reference](https://www.oxfordreference.com/display/10.1093/oi/authority.20110803095509469) |
| **Amish `Bann`/`Meidung`** | the congregation; the bishop may raise the question | **unanimous vote of the congregation**, after private approaches fail; excommunication is "a step of last resort" | [Amish Studies, Elizabethtown College](https://groups.etown.edu/amishstudies/religion/church-discipline/); [Amish America](https://amishamerica.com/why-do-the-amish-practice-shunning/) |
| **Romani `kris`** | a tribunal of male elders chosen for experience, impartiality and knowledge of custom | **a majority of judges suffices** (explicitly not unanimity); the chairman alone must stay impartial; `marime` may be temporary or permanent | [Kris (Romani court), Wikipedia](https://en.wikipedia.org/wiki/Kris_(Romani_court)); [Marime, Wikipedia](https://en.wikipedia.org/wiki/Marime) |
| **Athenian ostracism** | the whole assembly | **quorum of 6,000; the man with most votes leaves for ten years — no charge, no accusation, no defense, property and civil rights retained** | [Ostracism, Wikipedia](https://en.wikipedia.org/wiki/Ostracism); [Livius](https://www.livius.org/articles/concept/ostracism/); [History & Policy](https://historyandpolicy.org/policy-papers/papers/ostracism-selection-and-de-selection-in-ancient-greece/) |
| **Swiss communal naturalization by assembly** | the assembled residents of the commune, in public | simple vote; documented rejections "for reasons such as people mowing the lawn on Sundays or wearing tracksuit bottoms in public" | [France 24](https://www.france24.com/en/20190518-citizenship-cases-swiss-direct-democracy-shows-its-cracks); [Bürgergemeinde, Wikipedia](https://en.wikipedia.org/wiki/B%C3%BCrgergemeinde) |
| **`Liberum veto`** (Polish–Lithuanian Commonwealth) | **any single member of the Sejm**, by shouting *"Nie pozwalam!"* | one voice ends the session **and nullifies legislation already passed** | [Liberum veto, Wikipedia](https://en.wikipedia.org/wiki/Liberum_veto) |
| **Sociocratic consent** | every circle member | **"Consent is defined as 'no objections'"**, and an objection must be "based on the ability of the objector to work productively toward the goals of the organization" | [Sociocracy, Wikipedia](https://en.wikipedia.org/wiki/Sociocracy) |
| **Formal consensus** (activist/cooperative tradition) | every participant | **block vs. stand aside**: a block "expresses a fundamental objection" and "must be based on a generally recognized principle, not personal preference"; a stand-aside is recorded with the proposal and **"in essence, becomes a part of the decision"** | [Seeds for Change](https://www.seedsforchange.org.uk/shortconsensus); [Butler & Rothstein, *On Conflict and Consensus*](https://theanarchistlibrary.org/library/c-t-butler-and-amy-rothstein-on-conflict-and-consensus-a-handbook-on-formal-consensus-decisionm) |
| **Quaker discernment** | any Friend, on conscience | **no votes are taken**; the clerk minutes "the sense of the meeting"; a Friend may "stand in the way" of unity; where unity is absent, "no decision can be made nor action taken" | [Third Haven Friends Meeting](https://www.thirdhaven.org/decision_making.php); [Philadelphia Yearly Meeting](https://www.pym.org/faith-and-practice/faith-reflected-practice-daily-life/discernment-clearness-and-decision-making/) |

**`[CHANGED]`.** The pick was framed as an absence of *a* thing. The research says the thing is not one thing:
**a refusal instrument is a triple — who may fire it, what threshold, and what the refused person keeps.** Three
of the nine leave the refused person materially intact (ostracism keeps property and civil rights; a stand-aside
keeps the objection in the record; `marime` may be time-limited). That triple is the usable structure, and it is
not visible from the word "refusal."

### 1.2 The sharpest single contrast: consent is not consensus

> **"By consensus, I must convince you that I'm right; by consent, you ask whether you can live with the decision."**
> — [Sociocracy, Wikipedia](https://en.wikipedia.org/wiki/Sociocracy)

The companion test sociocracy applies to a proposal is **"good enough for now, safe enough to try"**; if it is
not, that is an objection. **`[CHANGED]`.** This supplies the missing half of the pick: a refusal instrument
needs a *standard of validity* for refusals, or it is only a preference. Sociocracy's standard is functional
(can I still work toward the aim?); formal consensus's is principled (a generally recognized principle, not
personal preference); the blackball's is nothing at all.

### 1.3 A refusal power held by everyone is measurable, and it was measured

From 1573 to 1763 the Polish–Lithuanian Commonwealth held **about 150 sejms, of which 53 passed no legislation
and 32 were disrupted by the `liberum veto`.** In the reign of Augustus III (1734–1763) **only one session was
able to pass legislation at all.** [Liberum veto, Wikipedia](https://en.wikipedia.org/wiki/Liberum_veto)

**`[CHANGED]`.** This is the only hard arithmetic available on what a universal individual veto does over time,
and it runs against the intuition that a refusal instrument is simply a good a polity either has or lacks.
⚠ **Stated as the source states it and no further** — the source attributes deterioration to the device;
that attribution is contested historiography and is not carried as fact.

### 1.4 The substitute institutions — rule 3.2's target, and the richest return in this pick

Cultures that **lack** a coercive refusal organ do not simply go without. Three distinct workarounds are
documented, and they are not variants of each other:

1. **FISSION — the group divides instead of expelling.** In band societies "membership is fluid enough to allow
   fission... to mitigate conflicts," and "the threat of fission does much to keep ambitious leaders in check";
   mobility is the enforcement. [Band society, Grokipedia](https://grokipedia.com/page/Band_society); [Egalitarian Societies, LibreTexts](https://socialsci.libretexts.org/Courses/HACC_Central_Pennsylvania's_Community_College/ANTH_205:_Cultures_of_the_World_-_Perspectives_on_Culture_(Scheib)/08:_Political_Organization/8.02:_Egalitarian_Societies)
2. **SCHEDULED FISSION — division as routine maintenance, not as crisis.** Hutterite colonies branch at roughly
   **30 families or about 150 people**; membership of the daughter colony is settled either by volunteers going
   *freiwillig* or by **casting lots**, with assets valued and split in two. [Hutterites.org, Daughter Colony](https://hutterites.org/day-to-day/structure/daughter-colony/); [Colony branching among the Schmiedeleut Hutterites (ResearchGate)](https://www.researchgate.net/publication/352222436_Colony_branching_among_the_Schmiedeleut_Hutterites_Colony_branching_among_the_Schmiedeleut_Hutterites_of_Manitoba)
3. **GRADUATED WITHDRAWAL — the community subtracts itself instead of the person.** Japanese `murahachibu`
   withdraws **eight of the ten common activities of village life** and keeps two — **funerals and
   firefighting** — because both are so time-sensitive that "even the ostracized were conscripted." The eight
   withdrawn are coming-of-age, weddings, births, care of the ill, construction, repair of water damage, death
   anniversaries, and travel. [Murahachibu, Wikipedia](https://en.wikipedia.org/wiki/Murahachibu_ostracism); [Unseen Japan](https://unseen-japan.com/murahachibu-the-shizuoka-village-ostracism-incident/)

**`[CHANGED]`, and this is the strongest structural return of the entire pick.** `Murahachibu` is a refusal
instrument that **never removes the person and never touches the two functions on which survival depends.** It
is graduated, it is enumerated, and its exceptions are chosen on a *physical* criterion (time-sensitivity), not
a moral one.

### 1.5 Adjudication without enforcement is a documented, stable form

Medieval Iceland's Althing **"had no executive power; it could make and adjudicate law but could not enforce
it."** Outlawry came in two grades — lesser (`fjörbaugsgarðr`, three years) and full (`skóggangur`, for life,
with the outlaw lawfully killable after three months) — and **enforcement "was up to the individual, with the
help of his friends, family, and Chieftain."** [Hurstwic](https://www.hurstwic.org/history/articles/society/text/laws.htm); [Friedman, *Private Creation and Enforcement of Law*](http://www.daviddfriedman.com/Academic/Iceland/Iceland.html); [Understanding Outlawry in Medieval Iceland (Academia.edu)](https://www.academia.edu/9928046/Understanding_Outlawry_in_Medieval_Iceland)

**`[CHANGED]`.** A culture can possess a fully developed *verdict* and no organ to carry it out. The verdict
still does work — it reassigns who is permitted to act, rather than acting.

### 1.6 Where the refusal power actually sits in isolated work settlements — and it is not the community

Two real cases put the refusal instrument in an **administrator's** hands, not a neighbor's:

- **Svalbard.** Anyone may live there visa-free, but **"people without a source of income can be rejected by the
  governor"**; there are **no welfare payments and no care or nursing services**; and voting for the community
  council requires three prior years' residence on the mainland.
  [Longyearbyen, Wikipedia](https://en.wikipedia.org/wiki/Longyearbyen); [Nordic co-operation](https://www.norden.org/en/info-norden/moving-or-travelling-svalbard); [Life in Norway](https://www.lifeinnorway.net/living-on-svalbard/)
- **Remote resource sites.** Removal is *demobilization* by the site operator (the sources spell it
  *demobilisation*): a labor-hire worker "was dismissed when [the employer] complied with [the client's]
  direction to remove him from their site," and a 2025 case turned on whether demobilization from a fly-in
  fly-out site was itself a dismissal.
  [HRD Australia — HSS case](https://www.hcamag.com/au/specialisation/employment-law/hss-defeats-dismissal-claim-over-labour-hire-site-removal/579859); [Fair Work Commission — labour hire workers](https://www.fwc.gov.au/labour-hire-workers)

**`[CHANGED]`.** In the modern isolated-settlement cases, **residence is conditioned on an economic test
administered by an office**, and the community that lives with the person has no part in the decision. This is a
different animal from every mechanism in §1.1, and it is the one that occurs in settlements resembling the
physical type under study.

### 1.7 Communities that hold the entry gate collectively

- **Tristan da Cunha:** "No 'outsiders' are allowed to buy land or settle"; the only outsiders are essential
  workers on fixed-term contracts. **All land is communally owned and stock numbers are strictly controlled "to
  conserve pasture and to prevent better-off families accumulating wealth."**
  [Freedom News](https://freedomnews.org.uk/2023/02/08/tristan-da-cunha-the-utopia-that-worked/); [tristandc.com](https://www.tristandc.com/patches.php)
- **Kibbutz:** the general assembly "approves new members," with a rigorous candidacy process and probationary
  periods of one to two years; a `Va'adat Kabala` (acceptance committee) vets prospective residents.
  [Jewish Virtual Library](https://jewishvirtuallibrary.org/history-and-overview-of-the-kibbutz-movement); [RNC](https://www.rnc.co.il/kibbutz-real-estate/)

**`[ORNAMENT]`** for the refusal question itself — both are entry gates rather than subtraction instruments —
but **`[CHANGED]`** for a distinction the pick did not contain: **refusing entry and subtracting a member are
different powers, held by different bodies, at different moments,** and a community can have one and not the
other. The Tristan stock cap is a third thing again: a standing limit that refuses an *accumulation* rather than
a person.

### 1.8 A body that removes a person it also appointed

Among the Haudenosaunee, clan mothers "represented the interests of their clan by selecting a chief to speak on
their behalf at the Confederacy council," and **"had the authority to oust a chief if he led insufficiently,"**
with warnings preceding removal. [Haudenosaunee Clan Mother, Wikipedia](https://en.wikipedia.org/wiki/Haudenosaunee_Clan_Mother)
**`[ORNAMENT]`.** ⚠ The detailed removal procedure (the "dehorning" sequence, number of warnings) **could not be
sourced** — see Part B dead ends. What survives is only the bare structure: appointment and removal held by the
same body.

### 1.9 What being refused actually does, over time

The only study located that follows ostracism outside the laboratory tracks **"cumulative ostracism"** across 25
biographical narratives over seven months, finding a consistent sequence of **an immediate stage, a coping
stage, and a resignation stage**, with recovery occurring "through encounter with a new religious group."
[Loss of Close Relationships and Loss of Religious Belonging as Cumulative Ostracism, *Behavioral Sciences* 2020](https://doi.org/10.3390/bs10060099)
**`[ORNAMENT]`.** Useful as texture on the receiving end; it studies exit *from* a group into another, which is
not the configuration the pick is about.

### 1.10 The theory that connects refusal to departure

Hirschman's `exit / voice / loyalty`: **"exit often undercuts voice"**, and the seesaw is explicit — *the more
easily available the exit option, the lower the likelihood of voice*; studies "confirm Hirschman's assertion
that greater exit and entry costs heighten the likelihood of voice." The worked case is a system where exit by
"the very people that would make effective voice possible" locks in decline.
[Exit, Voice, and Loyalty, Wikipedia](https://en.wikipedia.org/wiki/Exit,_Voice,_and_Loyalty); [Harvard University Press](https://www.hup.harvard.edu/books/9780674276604); [LSE blog](https://blogs.lse.ac.uk/internationaldevelopment/2014/05/21/reflections-on-the-classics-exit-voice-and-loyalty/)

**`[CHANGED]`.** This is a named, published, empirically tested mechanism for the shape Step 2 reached
independently at §5.2. It is recorded here **as an available real-world instrument, not as an endorsement** —
`02_Spine.md` reached its version from Davis's own arithmetic, and the two must not be fused without a decision
that is not this step's to make.

### 1.11 What Pick 1 did NOT return

- **No case was found of a settled human community with no refusal instrument of any kind.** Every society
  examined has at least one of: expulsion, graduated withdrawal, fission, an entry gate, or an administrative
  removal power. ⛔ **Recorded as a null, not resolved.** Whether this reflects the world or reflects what gets
  written about is unknown from here.
- Gossip, ridicule, shaming and avoidance recur everywhere as the informal layer beneath the formal one (Inuit
  ethnography names "gossip, shaming or embarrassing, ridicule, and social ostracism" as the effective
  measures). [Public Safety Canada review](https://www.publicsafety.gc.ca/cnt/rsrcs/pblctns/rvw-plc-prctcs-pauk/index-en.aspx); [Inuit Justice (inuitq.ca, PDF)](http://www.inuitq.ca/learningresources/powerpoints/CCO_Justice%20_english.pdf)

---

## ⭐ PICK 2 — COMPETENCE REBUILT BUT NEVER WRITTEN DOWN

**Aimed at: `D3a`/`D3b` — the living institution did not survive the handoff; the competence the exiles rebuilt
was never written down, and is therefore "unspeakable" (`02_Spine.md` §2.2, §5, check B).**

### 2.1 The base claim is a named, published position

Polanyi: **"we can know more than we can tell."** Polanyi's paradox is the phenomenon that "there exist many
tasks which human beings understand intuitively how to perform but cannot verbalize their rules or procedures";
tacit knowledge "resid[es] — often subconsciously — in bodily actions and cultural norms."
[Polanyi's paradox, Wikipedia](https://en.wikipedia.org/wiki/Polanyi's_paradox); [The Tacit Dimension, U. Chicago Press](https://press.uchicago.edu/ucp/books/book/chicago/T/bo6035368.html); [infed.org](https://infed.org/dir/welcome/michael-polanyi-and-tacit-knowledge/)
**`[ORNAMENT]`** — it names the thing the pick already assumed.

### 2.2 Unwritten is not always inexpressible — sometimes it is policy

Historians of craft find that **"concrete craft knowledge about how the respective products were manufactured
was not recorded in guild books"**; transmission was "oral and practical," apprentice education "almost entirely
practical and oral, with no textbooks or formal classrooms," and guilds bound members with **oaths of secrecy.**
[Apprenticeship, Guilds, and Craft Knowledge (Springer)](https://link.springer.com/rwe/10.1007/978-3-319-20791-9_247-1); [University of Florence, Medium](https://universityofflorence.medium.com/transmission-of-useful-knowledge-in-texts-written-by-craftsmen-7bee8afcd6b6)

**`[CHANGED]`.** The pick assumed "never written down" is a *failure state*. The historical record says it is at
least as often a **deliberate policy with an enforcement mechanism attached.** Those are different absences and
they behave differently under stress.

### 2.3 The instrument that makes unwritten competence checkable

The guild **masterpiece**: "a work of a very high standard produced by an apprentice to obtain full membership,
as a 'master'." The requirement could be exactly specified — Nuremberg goldsmiths (1531–1572) had to produce
**columbine cups, dies for a steel seal, and gold rings set with precious stones**; London goldsmiths made the
piece under supervision at a workhouse in Goldsmiths' Hall. In some guilds **"apprentices were not allowed to
marry until they had obtained full membership."** Apprenticeship contracts "varied widely from two to seven or
more years," beginning at ten to fifteen years of age, with the master providing "food, lodging and formal
training in the craft."
[Masterpiece, Wikipedia](https://en.wikipedia.org/wiki/Masterpiece); [Apprenticeship, Wikipedia](https://en.wikipedia.org/wiki/Apprenticeship)

**`[CHANGED]`, and this is the highest-value return of Pick 2.** It is the direct structural answer to the
pick's own difficulty: **a craft that refuses documentation can still be verified — by requiring an object, made
under observation, that only the competence could produce.** The verdict is public, the standard is an artifact,
and nothing about the skill has to be written down for it to work.

### 2.4 Transmission as a scheduled obligation, not an intention

Ise Jingu's `shikinen sengu`: the shrines "have been re-constructed at adjacent alternate sites every twenty
years without a break for the last 1,300 years," and **"because every architectural detail, piece of clothing
and sacred artifact must be completely remade every 20 years, traditional techniques are never forgotten."**
[Japan for Sustainability](https://www.japanfs.org/en/news/archives/news_id034293.html); [Smithsonian](https://www.smithsonianmag.com/smart-news/this-japanese-shrine-has-been-torn-down-and-rebuilt-every-20-years-for-the-past-millennium-575558/)

Compare the personal-lineage form: the temple carpenter (`miyadaiku`) Tsunekazu Nishioka (1908–1995), whose
grandfather and father were both master carpenters at the same temple, received his knowledge "through oral
traditions and written texts in a family tradition"; `miyadaiku` training "lasts a minimum of ten years, often
twenty." [Tsunekazu Nishioka, Wikipedia](https://en.wikipedia.org/wiki/Tsunekazu_Nishioka); [Japan Woodcraft Association](https://japanwoodcraftassociation.com/masters/tsunekazu-nishioka/)

**`[CHANGED]`.** A twenty-year rebuild cycle is a **transmission interval deliberately set shorter than a working
life**, so that every generation must perform the whole operation once. It converts an intention ("teach the
young") into a dated obligation with a physical deliverable — the same move as the masterpiece, at the scale of
a society rather than a person.

### 2.5 Unwritten competence decays on a measurable clock

- **Organizational forgetting.** Liberty ship production: Argote, Beckman and Epple found knowledge decayed at
  **about 15% to 25% a month**; Thompson, controlling for other factors, revised this to **3–6% a month**,
  implying **"a shipyard that stops producing ships would lose half its knowledge in about a year."** The same
  source states that where capabilities "are embedded in people, they decay faster than if they are embedded in
  technology." [King Canute, *Learning Curves*](https://kingcnut.substack.com/p/learning-curves)
- **Individual skill decay (meta-analysis).** With lack of use, **half of initial skill-acquisition performance
  gains were lost after approximately 6.5 months for accuracy, 13 months for speed, and 11 months for mixed
  performance**; decay grows at 0.08/month (accuracy) and 0.06/month (speed and mixed); **procedural skills
  decline faster than continuous and automated psychomotor skills**, and intermittent performance opportunities
  moderate the rate.
  [*Procedural Skill Retention and Decay: A Meta-Analytic Review*, Psychological Bulletin](https://psycnet.apa.org/manuscript/2026-23054-001.pdf); [Ovid listing](https://www.ovid.com/journals/plbul/pdf/10.1037/bul0000481~procedural-skill-retention-and-decay-a-meta-analytic-review)
- **Production breaks.** Forgetting "is a function of the amount of learning prior to the interruption and the
  elapsed time of the interruption," and relearning rate is a function of the original learning rate.
  [Production breaks and the learning curve (ScienceDirect PDF)](https://www.sciencedirect.com/science/article/pii/0307904X9500157F/pdf)

**`[CHANGED]`, strongly.** The pick's phrasing ("never written down") implies a binary — the knowledge is either
held or lost. **The measured reality is a rate**, it differs by skill type, and **the controlling variable is the
gap between performances**, not the passage of time as such.

### 2.6 What a near-total loss looks like from inside, and what recovery cost

**Fogbank.** The production process was lost by 2000; "NNSA had lost virtually all of its institutional
knowledge base regarding Fogbank," the facility was shuttered, documentation "either lost or incomplete," and
the original staff gone. Re-derivation took **five years and $92 million** — and the decisive discovery was that
**modern cleaning processes made the product too pure**: an *impurity* present in the 1980s process had to be
deliberately reintroduced. [Fogbank, Wikipedia](https://en.wikipedia.org/wiki/Fogbank); [The War Zone](https://www.twz.com/32867/fogbank-is-mysterious-material-used-in-nukes-thats-so-secret-nobody-can-say-what-it-is); [Scitales](https://scitales.com/fogbank-how-the-united-states-forgot-how-to-make-its-nuclear-weapons/)

**`[CHANGED]`, and it is the sharpest single fact in this pick.** The lost ingredient was **something nobody knew
they were doing.** A written record made by the original practitioners would not have contained it, because it
was not a step — it was a property of the conditions they worked in. **This is the specific failure mode of
"write it down" as a remedy, demonstrated rather than asserted.**

### 2.7 Transmission that survives only through an unbroken chain of persons

- **Learning by accompaniment.** Inuit sea-ice knowledge moves "through the quiet acts of travelling on the
  land"; observation is central; "whatever people learn comes from elders, and these skills aren't taught in
  school at all." Interruption of that accompaniment produced "loss of experiential mentorship, language, and
  communication between Elders and youth."
  [NSIDC](https://nsidc.org/news-analyses/news-stories/those-who-work-weather-inuit-and-visiting-scientists-collaborate-better); [Arctic Focus](https://www.arcticfocus.org/stories/inuit-childhood-and-subsistence-hunt/); [Frontiers in Climate](https://www.frontiersin.org/journals/climate/articles/10.3389/fclim.2021.715105/full)
- **Recovery through a single surviving holder.** Polynesian wayfinding: Mau Piailug of Satawal, "believed to be
  the last human keeper of wayfinding knowledge," was **persuaded to break with custom and teach an outsider**;
  in 1980 Nainoa Thompson became the first Polynesian in centuries to navigate a long-distance voyage without
  instruments, and from 1992 began training further navigators.
  [Hōkūle'a](https://hokulea.com/polynesian-wayfinding/); [Mau Piailug, Wikipedia](https://en.wikipedia.org/wiki/Mau_Piailug); [PBS Wayfinders](https://www.pbs.org/wayfinders/wayfinding.html)
- **Learning without teaching, formalized.** Lave and Wenger's *legitimate peripheral participation*: newcomers
  "learn from old-timers by being allowed to participate in certain tasks," moving from peripheral to full
  participation; grounded in Liberian tailors, Mayan midwives, US Navy quartermasters, and supermarket meat
  cutters; "learning is ubiquitous in ongoing activity, though often unrecognized as such."
  [infed.org](https://infed.org/dir/welcome/jean-lave-etienne-wenger-and-communities-of-practice/); [Situated Learning (Google Books)](https://books.google.com/books/about/Situated_Learning.html?id=CAVIOrW3vYAC)

**`[ORNAMENT]`** for the mechanism (the pick already had it); **`[CHANGED]`** for one detail: **recovery ran
through a single person who had to violate his own tradition's rules to make it possible.** Transmission failure
is recoverable, and the recovery path documented here is not institutional.

### 2.8 The sub-part that returned an honest null

⛔ **"How isolated stations hand over practice across personnel rotations" has no located literature.** An
OpenAlex query built precisely on those terms returned **`"count": 0`** — zero works — while a broader query on
the same concepts returned 588 works, none on point. What exists instead is generic shift-handover practice
(shadowing, phased overlap: shadowing → co-development → independent delivery, with an overlap period for
escalations) from maintenance, cybersecurity and software sources.
[Anti Entropy — staff handover](https://resourceportal.antientropy.org/docs/staff-handover-process); [Dovient](https://dovient.com/learning/knowledge-transfer-during-shift-handover); [*Passing the Baton*, arXiv](https://arxiv.org/html/2601.07788v1)

**Recorded as an absence, per NO FORCED FIT.** It is a genuine source-death, not a query-death — see Part B.

---

## ⭐⭐ PICK 3 — THE GENERAL POPULATION

**Aimed at: Step 2's explicit steer — "The deficit is now known, and it is the GENERAL POPULATION... Research
picks must target the 40%, not the 60%" (`02_Spine.md` §11).**

### 3.1 The support majority is real, and the ratio is documented

- **"Depending on the season, support staff — the janitors, cooks, trash sorters and other people who keep the
  stations functioning — outnumber researchers in Antarctica roughly seven to one."**
  [Scientific American](https://www.scientificamerican.com/article/i-worked-in-antarctica-for-three-years-my-sexual-harasser-was-never-caught/)
- Composition of one small wintering crew: **13 people — 5 scientists, 8 technical staff, a doctor and a chef**
  (the arithmetic in the source overlaps categories; reported as printed).
  [Poseidon Expeditions](https://poseidonexpeditions.com/about/articles/antarctica-population/)
- Continental scale: roughly **1,000 people year-round, up to 5,000 in summer**, with about half of ~70 stations
  staying open through winter. [Poseidon Expeditions](https://poseidonexpeditions.com/about/articles/antarctica-population/); [Aurora Expeditions](https://www.aurora-expeditions.com/eu/blog/do-people-live-in-antarctica)

**`[CHANGED]`.** The pick supposed a non-specialist majority whose work is invisible in the records. The real
ratio is not merely a majority — in the closest physical analogue it is **about seven to one**, and the
occupations named first in every source are **janitor, cook, and waste handler.**

### 3.2 The roles, itemized

A trades-and-support inventory from a non-operator source: **cook, electrician, carpenter, boat handler,
mechanic, plumber, radio operator, doctor, diving officer, fire fighters**; at larger bases, "attorneys, judges,
pharmacists, and PhD's working as mechanics, janitors, galley slaves, housing department and shuttle drivers."
[Cool Antarctica](https://www.coolantarctica.com/Community/find_a_job_in_antarctica.php)

A physical-plant inventory from one station: **more than 85 buildings**, including dormitories, a galley,
stores, a chapel, a science center, **a power plant, a water distillation plant and a waste treatment facility**,
a firehouse, a harbor, a heliport and landing strips, repair facilities, warehouses; about **60 super-duty
trucks** plus hundreds of other vehicles; population **1,000 in summer and 153 in winter** (capacity 1,200).
[McMurdo Station, Wikipedia](https://en.wikipedia.org/wiki/McMurdo_Station)

**`[CHANGED]`.** This is the concrete inventory the pick asked for, and it is dominated by **utilities, repair
and movement** — power, water, waste, fire, vehicles, warehouses — none of which appear in an occupational
record that lists only what a place produces.

### 3.3 ⭐ The finding that reframes the pick: the general work may not belong to a general class

> **"On many bases there is the expectation and requirement that all staff will fulfill generalist roles such as
> unloading ships, washing-dishes, night-watch, cleaning the base, dealing with the trash."**
> — [Cool Antarctica](https://www.coolantarctica.com/Community/find_a_job_in_antarctica.php)

**`[CHANGED]`, and it is the most important return in Pick 3.** The pick was framed as *"what does the
non-specialist majority do?"* — which presumes a non-specialist majority exists as a class. In small isolated
settlements the documented arrangement is frequently the opposite: **the general work is an obligation
distributed across everyone, specialists included, on top of the specialty.** ⛔ Recorded as an available real
structure and nothing more; which arrangement any given place has is not this step's to decide.

### 3.4 A civilian settlement's demographic and service profile

Longyearbyen, as a documented case of a permanent Arctic town rather than a work camp:

| | |
|---|---|
| **Population** | ~2,817 (2026); 2,354 registered at the 2020 census |
| **Composition** | 64.5% Norwegian; largest minority groups Thai 9%, Swedish 7%, Filipino 7%; **60% male** (2012); about half aged 20–44; **approximately 400 children and few elderly** |
| **Turnover** | in 2008, **427 people (23%) moved away in one year**; as of 2022, **43% of residents had stayed less than two years and 64% less than five** |
| **Services** | one grocery store; library, cinema, youth club, gallery, church; sports center with multi-sport hall, shooting range, climbing wall and a 25 m pool; hospital — but **"no care or nursing services and welfare payments are available"** |
| **Schooling** | school covering ages 6–18, about **270 pupils and 45 teachers**; **three kindergartens** for ages 1–6 |
| **Vehicles** | 1,481 registered road vehicles (49% of households own a car); **2,672 registered snowmobiles — 69% of households own at least one** |
| **Constraints on ordinary life** | monthly limits on how much alcohol an individual may purchase; **no options for burial**; import of most live mammals and birds prohibited; a standing recommendation to carry a rifle outside the settlement |
| **Employment** | tourism and related services **more than 60% of employment (2024)**; university center with 350 students, 40 permanent faculty, 120 guest lecturers |

[Longyearbyen, Wikipedia](https://en.wikipedia.org/wiki/Longyearbyen); [Longyearbyen lokalstyre](https://www.lokalstyre.no/en/longyearbyen-local-council/services/school/primary-school-education); [Statistics Norway — population of Svalbard](https://www.ssb.no/en/befolkning/folketall/statistikk/befolkningen-pa-svalbard)

**`[CHANGED]`.** The pick asked what the majority does. This case answers with a **demography**: a young,
male-skewed, child-bearing but not child-raising-to-adulthood population with **no elderly tier at all**, and a
service layer sized to that shape (three kindergartens, one shop, no nursing). The rationed alcohol and the
absence of burial are ordinary-life constraints of a kind no occupational record would ever contain.

### 3.5 The invisible labor layer in single-industry settlements

- Company towns: the firm "provided its employees with goods and services, hired police, collected garbage,
  dispensed justice, and answered (or failed to answer) complaints from residents"; **"community services that
  today are provided by municipal governments were provided by the profit-maximizing firm."** Housing tenure
  followed employment — leases "allowed for a quick termination, usually five days."
  [EH.net — The Company Town](https://eh.net/encyclopedia/the-company-town/)
- The staffed layer companies paid for: hospitals, hotels, recreation halls, schools and stores, plus **medical
  personnel and teachers**; the commissary "served as the town's social center and housed the U.S. Post Office."
  [Social Welfare History Project](https://socialwelfare.library.vcu.edu/programs/housing/company-towns-1890s-to-1935/); [Coal town, Wikipedia](https://en.wikipedia.org/wiki/Coal_town)
- The **unpaid** layer: "women contributed to the camp by washing laundry, cooking hot meals, and keeping
  boarding houses"; in the absence of a bath house, "miners' wives or the women at the boardinghouse... had to
  supply the hot water for the bath," and **"well into the 1930s, women in many coal mining towns carried all
  their own water for laundering."**
  [WV Culture — Strategies for Survival](https://archive.wvculture.org/history/journal_wvh/wvh49-4.html); [IUP — A Woman's Day](https://www.iup.edu/library/departments/archives/coal/people-lives-stories/a-womans-day-work-and-worry.html); [JSTOR Daily](https://daily.jstor.org/the-women-written-out-of-mining-history/)

**`[CHANGED]`.** The non-specialist majority of a single-industry settlement includes **a large body of labor
that was never an occupation at all** — it was neither paid nor recorded, and in the documented cases its
largest single component was **moving and heating water.**

### 3.6 Non-working time, documented

- Clubs, bands, classes, trivia nights, book clubs, movie marathons and inter-station visiting; gyms, saunas,
  billiards, table tennis, volleyball, board games, darts; bicycles and cross-country skis and a small ski loop;
  libraries, cinemas; **communal band and stage equipment (drum kit, bass, electric guitars, keyboard)** with
  regular performances; midwinter events including a runway jog and a mini-Olympics.
  [Swoop Antarctica](https://www.swoop-antarctica.com/blog/whats-it-like-to-spend-a-winter-in-antarctica/); [IceCube — Daily Life](https://icecube.wisc.edu/pole/daily-life/); [CNN](https://www.cnn.com/travel/what-its-really-like-to-live-in-antarctica-intl-hnk); [Midwinter Day, Wikipedia](https://en.wikipedia.org/wiki/Midwinter_Day)
- A second-settlement pattern: on Tristan da Cunha, the Potato Patches carry **camping huts equipped with "beds,
  stoves, chairs and tables for a weekend away from the Settlement,"** and "all help to plant, tend and harvest
  crops." [tristandc.com](https://www.tristandc.com/patches.php)
- What remote-site workers themselves report needing: **"maintaining closest contacts; warm rest time; proper
  varied meals; additional onsite enjoyment assistance; transportation organization; community living promotion;
  and professional-personal life balance."**
  [Literature review, wellness in the Australian mining sector (OpenAlex record)](https://api.openalex.org/works?search=fly-in%20fly-out%20camp%20workers%20daily%20routine%20leisure%20social%20life%20accommodation%20village)

**`[ORNAMENT]`** for the activity list — it is largely what one would expect — **`[CHANGED]`** for the Tristan
pattern: **a worked landscape at a distance from the settlement generates a second, weekend dwelling place**,
which is a structural fact about how such a population uses time, not a list of pastimes.

### 3.7 A caution the sources themselves supply

Fly-in fly-out research repeatedly models the arrangement as **"simultaneous fracturing and blending of personal
and work lives."** [*Fly-in-fly-out work: a review*, 2022](https://doi.org/10.1177/20413866221134938)
⚠ **Marked as NOT DIRECTLY TRANSFERABLE**: rotational camp labor and a permanently resident population are
different objects, and the FIFO literature's findings are about the commute structure. Recorded so the next
session does not mistake its abundance for relevance.

---

## PICK 4 — THE PHYSICAL SITE

**Site as given: Vestfold Hills, Ingrid Christensen Coast, Prydz Bay (~68°35′S, 77°58′E).**
⛔ **GPS discipline applied throughout: physical facts only.** Sources published by the site's station operator
were located and **not read** — see Part B §4b.

### 4.1 The ice-free ground — and the sources disagree on how much of it there is

| Figure | Source |
|---|---|
| **512 km²** "in extent," rounded rocky coastal hills "subdivided by three west-trending peninsulas bounded by narrow fjords" | [Vestfold Hills, Wikipedia](https://en.wikipedia.org/wiki/Vestfold_Hills) |
| **~420 km²**, listed as an Antarctic oasis | [Antarctic oasis, Wikipedia](https://en.wikipedia.org/wiki/Antarctic_oasis) |
| **200 km²**, "the third largest ice-free area in Antarctica after the Dry Valleys" | [AntarcticGlaciers.org](https://www.antarcticglaciers.org/glacial-geology/glacial-landforms/periglaciation/antarctic-periglacial-environments/) |

**`[CHANGED]`.** ⚠ **The ice-free area of this site is not a settled number in the literature — published values
span 200 to 512 km², a factor of about 2.5.** This is an input-data fact and is recorded as such. It bears on
`02_Spine.md` §6's warning that the administrative extent and the ice-free area are two different objects; **it
does not resolve that warning, and nothing here should be read as resolving it.** ⭐ The source superlative
("third largest ice-free area") is quoted as the source's own statement about the real site and is **not
transferable** to any claim about the city.

**Relief:** "Most of the hills range between 30 and 90 metres in height, with the highest summit reaching nearly
160 metres." **Geology:** three mapped rock types — **Chelnok Paragneiss, Crooked Hill Gneiss and Mossel
Gneiss**. [Vestfold Hills, Wikipedia](https://en.wikipedia.org/wiki/Vestfold_Hills); [data.gov.au — simplified geology dataset](https://data.gov.au/data/dataset/aad-vestfold-geology-map-inset-gis)

**Why an oasis is an oasis:** "sufficient solar energy is absorbed by the ground to melt what little snow does
fall, or else it is scoured or sublimated by katabatic winds, leaving the underlying rock exposed," with "very
low humidity and precipitation." [Antarctic oasis, Wikipedia](https://en.wikipedia.org/wiki/Antarctic_oasis)
**Climate at the site:** "a cool periglacial climate with a mean annual temperature of -10.2°C. Rainfall is very
rare, and precipitation is light, making this a semi-arid environment," with snow and ice melting **December to
February**, "resulting in limited surface water being available." [AntarcticGlaciers.org](https://www.antarcticglaciers.org/glacial-geology/glacial-landforms/periglaciation/antarctic-periglacial-environments/)
**`[ORNAMENT]`** — consistent with what the pass already holds; recorded for corroboration only.

### 4.2 ⭐⭐ The lake system, and it is the site's defining physical fact

**Over 300 lakes and ponds**, including "what is possibly the largest concentration of meromictic (stratified)
lakes in the world": **37 permanently stratified water bodies, including six marine basins and seven seasonally
isolated marine basins (SIMBs).** Their measured ranges:

| Property | Range |
|---|---|
| **Salinity** | **4 g/L to 235 g/L** |
| **Temperature** | **−14 °C to 24 °C** |
| **Depth** | **5 m to 110 m** |
| **Area** | **3.6 ha to 146 ha** |
| **Surface level** | **30 m below to 29 m above sea level** |

[Vestfold Hills, Wikipedia](https://en.wikipedia.org/wiki/Vestfold_Hills); [*The meromictic lakes and stratified marine basins of the Vestfold Hills, East Antarctica*, Antarctic Science](https://www.cambridge.org/core/journals/antarctic-science/article/abs/meromictic-lakes-and-stratified-marine-basins-of-the-vestfold-hills-east-antarctica/42C014367EFFDAED6D5050348BBD0003)

The typology also runs spatially: lakes "are generally saline or hypersaline near the coast, and fresh... near
the Antarctic Plateau." [*Modeling present and future ice covers in two Antarctic lakes*, J. Glaciology](https://www.cambridge.org/core/journals/journal-of-glaciology/article/modeling-present-and-future-ice-covers-in-two-antarctic-lakes/9306439ADD5492BC05F3BAF0E076B1C3)

**Two endpoints, both real, both at this site:**

- **Deep Lake** — salinity **~270 g/L**, maximum depth **36 m**, surface temperatures averaging **−16 to 12 °C**
  with winter water temperatures falling **as low as −20 °C**, and a water column that **"remain[s] free of ice
  year-around due to the high salinity."** The archaeon *Halorubrum lacusprofundi* isolated from it in the 1980s
  was "the first archaea domain member to be isolated from a cold environment."
  [Deep Lake (Vestfold Hills, Antarctica), Wikipedia](https://en.wikipedia.org/wiki/Deep_Lake_(Vestfold_Hills,_Antarctica))
- **Ekho Lake** — hypersaline and **heliothermal** (solar-heated): "the temperature of the lower layers... remains
  at about +13 °C in winter. During austral summer, intermediate strata reached +19 °C," with an aerobic zone
  from 0–24 m.
  [*Antarctobacter heliothermus*, IJSEM](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-48-4-1363); [*Nesterenkonia lacusekhoensis* (ResearchGate)](https://www.researchgate.net/publication/11233369_Nesterenkonia_lacusekhoensis_sp_nov_isolated_from_hypersaline_Ekho_Lake_East_Antarctica_and_emended_description_of_the_genus_Nesterenkonia)
- **Ace Lake** — a 9 m deep saltwater lake, surface elevation 8.8 m, on the Langnes peninsula.
  [Ace Lake, Wikipedia](https://en.wikipedia.org/wiki/Ace_Lake)

**`[CHANGED]`, decisively.** Pick 4 asked for "the lake system and its typology." **The typology is not a list of
kinds — it is a continuum with a factor-of-sixty salinity range and a 38-degree temperature range inside a
single small area, in which one water body is liquid at −20 °C and another is +19 °C in mid-layer.** Adjacent
basins at this site are not variants of one thing.

### 4.3 How the landlocked marine basins came to be landlocked

Relative sea level here **"rose to a maximum ~9 m above present sea-level 6200 yr ago"** from ~7.5 m 8,000 years
ago, and has fallen since — the mechanism by which marine inlets become isolated basins.
[*Holocene sea-level change and ice-sheet history in the Vestfold Hills*, EPSL](https://www.sciencedirect.com/science/article/abs/pii/S0012821X97002045)
A core documenting one such detachment is dated at **5050 ± 98 yr BP at 18–19 cm and 5560 ± 96 yr BP at 28–29
cm** — roughly **10 cm of sediment per 500 years.**
[*A Testimony of Detachment of an Inland Lake from Marine Influence during the Mid-Holocene*, MDPI](https://www.mdpi.com/2300-7575/13/4/209) ⚠ *abstract via search snippet; the full paper returned HTTP 403 — see Part B.*

**`[CHANGED]`.** The site's water bodies have **individual dates of separation from the sea**, and the record of
that separation accumulates at about **a centimeter per fifty years.**

### 4.4 ⭐⭐ The damage regime is salt, not frost — and it draws a line across the ground

- **Frost weathering** requires water in pore spaces; the classic volumetric mechanism needs rock "water-saturated
  and frozen quickly from all sides," conditions "considered unusual," with ice segregation the better-supported
  model; it operates "between −3 and −8 °C... if water is present."
  [Frost weathering, Wikipedia](https://en.wikipedia.org/wiki/Frost_weathering)
- **Salt weathering** operates wherever "salts are concentrated by evaporation... most common in arid climates
  where strong heating causes strong evaporation and along coasts"; sodium and magnesium salts are the most
  effective; it is "likely important in the formation of tafoni."
  [Salt weathering, Wikipedia](https://en.wikipedia.org/wiki/Salt_weathering)
- **At this site specifically:** **"At Vestfold Hills and Bunger Hills, tafoni were only found in areas of the
  most salt-weathered bedrock."** Strong winds (>10 m/s) are the transport mechanism — they "are strong enough
  to create salty spray from the marine inlets and saline lakes and transport salt aerosols." "As brine dries on
  rock surfaces, the growing salt crystals exert pressure on the rock surface, loosening mineral grains and
  leading to intense physical weathering of rock and glacial debris."
  [Gore & Leishman, *Bunger Hills palaeowinds*, Antarctic Science (Macquarie University PDF)](https://research-management.mq.edu.au/ws/portalfiles/portal/114710811/108593368_AV.pdf)

> #### ⭐⭐⭐ THE SALT LINE — a real, named, visible boundary on this ground
> **"...the line delineating the salt-enriched area is known as the 'salt line' (Adamson & Pickard 1986, Gore et
> al. 1996), which divides an area to the east that is rich in vegetation and with relatively unweathered
> bedrock and an area to the west where physical weathering of the metamorphic basement creates abundant sand
> and inhibits the growth of lichen and moss vegetation."**
> — Gore & Leishman, as above, lines 715–723 of the published typescript.

**`[CHANGED]`, and this is the single strongest physical return of the whole pass.** Pick 4 asked about
**freeze–thaw damage regimes**. At this site the dominant physical weathering agent is **salt delivered by wind
off the inlets and saline lakes**, and its effect is **spatially divided by a named line** that separates
vegetated, sound bedrock from sand-generating, lichen-hostile ground. It is concrete, nameable, load-bearing,
and entirely a fact about the land.

**Ground-ice behavior, same site:** melt-out and sublimation tills form as debris consolidates; "when deposit
thickness reaches or exceeds summer thaw depth, ice cores remain unmelted, forming semi-permanent features," and
the primary control is "climate at the glacier terminus area."
[*Ice-marginal Depositional Processes In A Polar Maritime Environment, Vestfold Hills*, J. Glaciology (1990)](https://doi.org/10.3189/002214390793701255)
**Biology of the rock itself:** the site contains "excellent examples of terrestrial sublithic, epilithic,
chasmoendolithic algal communities" — life under, on, and inside the stone.
[*Antarctic terrestrial ecosystems: The Vestfold Hills in context*, Springer](https://link.springer.com/article/10.1007/BF00025586)

### 4.5 Sublimation-dominated water budgets

- At a perennially ice-covered Antarctic lake, **"ice-cover dynamics are controlled by sublimation rather than
  melt — the dominating ablation process — meaning negligible surface melt occurs during austral summer."**
  [*Source Environments of the Microbiome in Perennially Ice-Covered Lake Untersee*, Front. Microbiol. 2019](https://doi.org/10.3389/fmicb.2019.01019)
- In the cold-desert case, lakes exist through "a climate-induced balance between the maintenance of a thick,
  permanent ice cover due to low temperatures, **the loss of ice to sublimation**, and the replacement of water
  into the lakes themselves from seasonal glacial meltwater inflow"; katabatic wind "evaporates the snow rapidly
  and little melts into the soil," and melt streams run "for several weeks in the summer" into lakes with **no
  outflow to the sea**. Precipitation there averages "around 100 millimetres per year over a century of records,
  almost exclusively in the form of snow."
  [McMurdo Dry Valleys, Wikipedia](https://en.wikipedia.org/wiki/McMurdo_Dry_Valleys)
- Mixing timescales under permanent ice cover: CFC profiles give **vertical mixing times of 20–30 years** in one
  such lake. [*Evidence of deep circulation in two perennially ice-covered Antarctic lakes*, L&O 1998](https://doi.org/10.4319/lo.1998.43.4.0625)
- Salt as a hydrological tracer: in cold-desert soils "halite is ubiquitous; sodium comprises 70–90% of cations
  and chloride exceeds 50% of anions in nearly all samples," and the salts serve "as tracers for paleolake
  levels." [*Patterns and Processes of Salt Efflorescences in the McMurdo region*, AAAR 2015](https://doi.org/10.1657/aaar0014-024)

**`[CHANGED]`.** The pick's phrase "sublimation-dominated water budget" is confirmed as a real regime with a
named dominant term, **and it carries a consequence the phrase does not: in a closed basin under permanent ice,
the water column itself turns over on a 20-to-30-year clock.**

⛔ **A specific sublimation rate in mm/yr for the lakes of this site was not obtained.** Four differently framed
attempts failed (Part B). Recorded as an open hole, not filled by inference — `M-158` applies.

### 4.6 Closed-loop water recovery, with numbers and with a rule about bodies

| Fact | Source |
|---|---|
| Station water use "can roughly be estimated anywhere between **40 to 100 litres per person per day**" | [ESA](https://www.esa.int/ESA_Multimedia/Images/2018/08/Cool_water); [Phys.org](https://phys.org/news/2018-08-image-concordia-station-recycling-facility.html) |
| One inland station **"reclaim[s] about 85% of its wastewater"** via nanofiltration and reverse osmosis; the system derives from a space-agency regenerative life-support program | [Fluence](https://www.fluencecorp.com/wastewater-treatment-in-antarctica/) |
| Another **"recycles up to 75% of its wastewater"**, with an anaerobic bioreactor for black water and an aerobic one for grey water, plus nanofiltration, carbon filtration, UV and chlorine | [Fluence](https://www.fluencecorp.com/wastewater-treatment-in-antarctica/) |
| ⭐ That station **"requires people on antibiotics to use a separate toilet to prevent antibiotics from killing the microorganisms"** | [Fluence](https://www.fluencecorp.com/wastewater-treatment-in-antarctica/) |
| One station's treatment plant handles "highly variable flows" across a population swing from **150 in winter to 1,000 in summer** | [Fluence](https://www.fluencecorp.com/wastewater-treatment-in-antarctica/) |
| A reverse-osmosis plant producing "about 8 000 litres per day" | [Alfa Laval](https://www.alfalaval.com/media/stories/fresh-water/running-water-in-the-antarctic/) |
| Regulation: the 1991 Madrid Protocol requires that wastewater and solids which cannot be discharged or reused **be shipped off the continent** | [Fluence](https://www.fluencecorp.com/wastewater-treatment-in-antarctica/) |

**`[CHANGED]`, on one item above all.** The antibiotics rule is the pick's best return: **a closed-loop water
system generates a binding rule about what individual people may put into it, enforced by biology rather than by
anyone's authority.** It is a real, sourced instance of infrastructure legislating conduct.

### 4.7 Cultivation under a polar night — real plants, real numbers

| Fact | Source |
|---|---|
| A container greenhouse at an Antarctic station produced **268 kg of food in 12.5 m² over 9.5 months**; **646 kg** of edible biomass across the 2018–2019 experiment phase; **1,014 kg** over four growing campaigns | [EDEN ISS](https://eden-iss.net/index.php/2019/08/26/vegetable-cultivation-in-the-antarctic-for-the-moon-and-mars); [DLR](https://www.dlr.de/en/latest/news/2023/03/eden-iss-greenhouse-returns-to-bremen-and-has-a-new-destination) |
| First-campaign breakdown: **117 kg lettuce, 67 kg cucumbers, 46 kg tomatoes, 19 kg kohlrabi, 15 kg herbs, 8 kg radishes** | [Polar Journal](https://polarjournal.net/eden-iss-the-greenhouse-in-antarctica) |
| Energy: **~205 kWh of electricity per kilogram of food produced (2018)**; a different polar growth chamber used **~22.8 kWh/kg** | [*Energy and Power Demand of Food Production in Space* (ResearchGate)](https://www.researchgate.net/publication/361677353_Energy_and_Power_Demand_of_Food_Production_in_Space_based_on_Results_of_the_EDEN_ISS_Antarctic_Greenhouse) |
| ⭐ Labor: **694.5 crew-member hours, i.e. 6.31 CM-h per kilogram**; on-site crew requirements were about **four times** remote-only operation; maintenance and planning carried the highest perceived workload | [*Crew time and workload in the EDEN ISS greenhouse in Antarctica*, LSSR 2021](https://doi.org/10.1016/j.lssr.2021.06.003) |
| ⭐ Agronomy: **multiple harvests raised lettuce production by approximately 400% versus single harvesting**; lettuce and red mustard responded 35–90% to increased light (200–600 μmol m⁻² s⁻¹, 21–25 °C); tomato and cucumber biomass rose 8–15% at 300 μmol m⁻² s⁻¹ | [*Growing fresh food on future space missions*, Scientia Horticulturae 2018](https://doi.org/10.1016/j.scienta.2018.03.002) |
| At a very high, very cold inland site, five growing seasons of 13 varieties across 9 leaf-vegetable types showed **statistically significant annual yield decreases of 16–61% per m²**, possibly from genotype–environment interaction under different barometric pressure and partial oxygen | [*Growth and Development of Leaf Vegetable Crops... in Antarctica*, Agronomy 2023](https://doi.org/10.3390/agronomy13123038) |
| History and scale: plants have been carried to Antarctic field sites **since 1902**; **over 46 distinct plant production facilities** have operated there; **nine hydroponic systems** currently operate; motivation is partly "expeditioners' desire to associate themselves with plants" | [*Review of Antarctic greenhouses and plant production facilities* (2015)](https://api.openalex.org/works?search=South%20Pole%20Food%20Growth%20Chamber%20hydroponic%20greenhouse%20crew%20psychological%20benefit%20fresh%20vegetables%20Antarctic) |
| High-latitude horticulture generally: **"Supplementary lighting is essential to maintain year-round production in Iceland due [to] the extremely low natural light level in winter"**; LEDs proved more energy-efficient than high-pressure sodium at equal photon flux, and switching lamp type beat raising temperature | [*Winter Strawberry Production Under LEDs in Iceland*, 2023](https://doi.org/10.1080/09064710.2023.2251498) |

**`[CHANGED]`, twice over.** First: **sheltered cultivation in the dark has a labor price as well as an energy
price — about 6.3 person-hours per kilogram** — and the heaviest part of it is *maintenance and planning*, not
harvesting. Second: **harvest strategy is worth a factor of four**; whether a crop is taken all at once or
progressively changes the yield more than most environmental variables in the same study.

### 4.8 Ski-only aviation and the seasonal window

- A sea-ice runway "usually operated from October to December, after which time the sea ice would break up";
  ice "over 2 meters... thick" is required to land a heavy transport; replacement fields were built on compacted
  snow and the ice shelf to extend the season.
  [Ice Runway, Wikipedia](https://en.wikipedia.org/wiki/Ice_Runway); [*A snow runway for supporting wheeled aircraft: Phoenix Airfield*, CRREL 2019](https://doi.org/10.21079/11681/32731)
- **"Antarctica is [the] last continent where aviation still depends almost entirely on expeditionary airfields
  and 'bush flying'."** [*Notes on Antarctic aviation*, CRREL Report 93-14 (1993)](https://rosap.ntl.bts.gov/view/dot/33846/dot_33846_DS1.pdf) ⚠ *record via OpenAlex; the PDF itself exceeded the fetch size limit.*
- Snow roads are "the critical link between [a] Station and its snow ice airfields," and deteriorate under use.
  [*Snow Roads at McMurdo Station* (2010), via OpenAlex](https://api.openalex.org/works?search=ski-equipped%20aircraft%20snow%20runway%20skiway%20Antarctic%20operations%20bearing%20capacity%20season)
- Ski-equipped transports can land "on some including ungroomed or poorly groomed snow / ice surfaces."
  [Aviation Stack Exchange](https://aviation.stackexchange.com/questions/16735/what-kind-of-aircraft-may-land-on-iced-areas-like-antarctica)

**`[CHANGED]`, modestly.** The pick asked about ski-only access and its seasonal availability. The literature's
emphasis is elsewhere and is more useful: **the constraint is the surface, and the surface is a maintained
artifact** — runways are built, groomed, monitored and lost, and **the road to the runway is itself a work item
that degrades.** ⛔ A ski-specific operating window (temperature and snow-strength limits for ski takeoff) was
not obtained; the authoritative technical report was unreadable at size. Open thread.

---

## PICK 5 — THE REGISTERED TOPICS

*Rule 3.3: prioritizing is not skipping. Each was looked at far enough to know what it would have given.*

### 5.1 Greenhouse agriculture in extreme climates

Covered in §4.7 above, which is where its material landed. **What it would have given on its own:** the
energy-per-kilogram and labor-per-kilogram figures, the four-fold harvest-strategy effect, and the historical
scale (46 facilities since 1902, nine now operating). **`[CHANGED]`** — see §4.7. One additional structural
note: designers of such facilities report that **environmental regulation, logistics, waste management and
energy use "heavily influence subsystem selection and operational paradigms"** — that is, the growing system's
shape is set by the disposal and power constraints, not by the crop.
[*Early trade-offs and top-level design drivers for Antarctic greenhouses* (2016), via OpenAlex](https://api.openalex.org/works?search=South%20Pole%20Food%20Growth%20Chamber%20hydroponic%20greenhouse%20crew%20psychological%20benefit%20fresh%20vegetables%20Antarctic)

### 5.2 Limnology and lake-sediment paleoclimate reconstruction

- **"Polar lakes respond quickly to climate-induced environmental changes."** A study of **127 lakes and ponds
  from eight ice-free regions**, comparing repeat measurements from 1987–2009 and 1997–2008, found inter-annual
  and inter-decadal variability "relatively large, particularly in non-dilute lakes with low depth-to-surface-area
  ratios," and concluded such measurements **"should thus be part of long-term biological monitoring
  programmes."** [*Chemical limnology in coastal East Antarctic lakes*, Antarctic Science 2011](https://doi.org/10.1017/s0954102011000642)
- A **650-year high-resolution record of evaporation** was derived from a diatom-salinity signal in a single
  sediment core at this site. [*Late-Holocene East Antarctic climate trends from ice-core and lake-sediment proxies*](https://journals.sagepub.com/doi/10.1191/095968301677143452)
- Palaeohydrological modeling of the same lake: "water level and lakewater salinity then stabilize in the last
  ~200 years BP... there is no significant change in evaporation for the last ~700 years but... a lower
  evaporation period is evident at ~150–200 years BP."
  [*Palaeohydrological modelling of Ace Lake*, The Holocene](https://journals.sagepub.com/doi/abs/10.1191/095968399672424476)
- The transfer-function method that makes this work is generic and documented: diatom assemblages calibrated
  against conductivity across >100 lakes, tested by jackknifing, then applied down a dated core.
  [*Development and evaluation of a diatom-conductivity model from lakes in West Greenland*, Freshwater Biology 2002](https://doi.org/10.1046/j.1365-2427.2002.00832.x)

**`[CHANGED]`.** The pick named a discipline; what it actually yields is a **method with a stated grain**: a
salinity proxy read down a core produces **evaporation history at century-to-decade resolution**, and the
instrument is a population of microscopic shells rather than any written measurement. The lakes here are an
archive that was accumulating before anyone read it.

### 5.3 The history of genuinely multi-disciplinary research institutions

Two traditions were examined, and they answer different halves of the topic.

**(a) The institution where production and study are the same enterprise — the agricultural experiment
station.** First at Pechelbronn, Alsace, **1836**; Rothamsted **1843**; Möckern, near Leipzig, created **28
September 1850** with the stated objective of **"cooperation between practical farmers and scientific
professionals"**; Connecticut on a permanent footing from an 1875 appropriation. Station scientists work with
**extension agents** who carry findings to growers; in one national system there are "more than 600 main
experiment stations and branch stations, run by about 13,000 scientists."
[Agricultural experiment station, Wikipedia](https://en.wikipedia.org/wiki/Agricultural_experiment_station)

**(b) The very long series.** The Broadbalk experiment has been "planted annually with winter wheat since
**1843**"; the Park Grass Experiment was "initiated in **1856** and has been continually monitored ever since."
Park Grass keeps **"an archive of soil and hay samples that have been used to track the history of atmospheric
pollution, including nuclear fallout,"** and it demonstrated that "conventional field trials probably
underestimate threats to plant biodiversity from long term changes, such as soil acidification."
[Rothamsted Research, Wikipedia](https://en.wikipedia.org/wiki/Rothamsted_Research); [Park Grass Experiment, Wikipedia](https://en.wikipedia.org/wiki/Park_Grass_Experiment)

**(c) The method that binds instruments to landscape.** Humboldtian science: "the accurate, measured study of
widespread but interconnected real phenomena in order to find a definite law and a dynamical cause," pursued
with chronometers, sextants, thermometers, hygrometers, barometers and more — **"multiple versions of each
instrument to compare errors"** — and applied "not to isolated science in laboratories, but to greatly variable
real phenomena." [Humboldtian science, Wikipedia](https://en.wikipedia.org/wiki/Humboldtian_science)

**`[CHANGED]`, on (b) in particular.** A long series' greatest payoff was **unforeseeable at its start**: hay and
soil archived from 1856 onward became an atmospheric-pollution and fallout record for questions nobody had in
1856. That is a real, documented property of serial observation — the value arrives later, to someone else, for
a reason the observer could not have known. ⛔ Recorded as a real-world property. **What, if anything, follows
for Davis is not this step's to say.**

---

## ⛔ WHAT PART A DOES NOT CLAIM

- **No finding here is a decision about Davis.** No institution, custom, practice, festival, name, demonym or
  price is proposed, and no roster is filled.
- **No comparison to any other city, real or fictional, is made or implied.** Real-world comparables are used as
  rule 3.1 directs; the superlatives quoted belong to their sources and to real places.
- **Nothing here resolves the `410 km²` / `~400 km²` question** raised at `02_Spine.md` §6. It adds two further
  published figures and records that the literature disagrees.
- **Three picks returned explicit nulls** — a community with no refusal instrument of any kind (§1.11), the
  station-handover literature (§2.8), and a site-specific sublimation rate (§4.5). **None was filled by
  inference.**

---
---


### A — PROOF BLOCKS

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md
LRANGE: 2526-2620
LINES: 95
L1: # Step 3 — Research, aimed at what Step 2 named
LMID:
LLAST:
QUOTE: > ## ⛔ ONE SEARCH AGAINST A PICK ESTABLISHES THAT THE PICK EXISTS. **IT DOES NOT ESTABLISH WHAT IT HOLDS.**

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/Real-World_Basis_Extrapolation_Method.md
LRANGE: FULL
LINES: 463
L1: # ⭐⭐⭐ LAW 0-R — RESEARCH FULLY. **A PICK IS NOT EXHAUSTED BECAUSE IT HAS BEEN SEARCHED.**
LMID: ### ⭐ IT IS A SEQUENCING RULE, NOT A REPEAL — **the prohibition above is UNCHANGED**
LLAST: 3. **A real detail beats an invented one every time.**
QUOTE: 3. ⭐ **A pick with a sub-part is at least TWO picks.** *A district is not its city; a station is not its site.*

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Stepwise_Execution/01_Spine/S05_Step_3_Research_aimed_at_what_Step_2_named.md
LRANGE: FULL
LINES: 152
L1: # Step 3 — Research, aimed at what Step 2 named
LMID: **3.2 Research can supply a substitute institution**, not only texture — a real culture that lacked the same
LLAST: > ☐ **Did I modify any file?** → **`graphify update .`** *(`CLAUDE.md`.)*
QUOTE: **3.1 Research the deficit.** The single most reliable move available: the profile says what the place cannot do; it does not say what the missing thing looks like. **Find a real culture that has it, and the contrast writes the finding.**

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/README.md
LRANGE: FULL
LINES: 123
L1: # Research Logs — one per location
LMID: > for each particular location that keeps a record of exactly what it was that was researched in order to find
LLAST: | **Janbogo** | `Janbogo_Research_Log.md` | 2026-08-31 — Run 9 cold pass. 2 search queries + 3 fetches (1 failed, HTTP 402); Jang Bogo Station's real staffing/scale and its historical namesake. **5 open threads recorded**, incl. an unfused downfall-by-overreach parallel deliberately deferred to a later filter test |
QUOTE: | ⭐ **DEAD ENDS, and whether each died at the QUERY or at the SOURCES** | *(query-death is recoverable by re-framing; source-death is a real absence)* |

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Davis/02_Spine.md
LRANGE: FULL
LINES: 585
L1: # Davis — Step 2 · BUILD THE SPINE
LMID: | **For `DIFFUSE`** | ⭐ **The admitted set names no supplier**, so *"above Davis"* ≠ *"in the parent."* **And `PA-6` is explicit that the parent is UNWRITTEN — *"what the parent determines returns UNKNOWN, which is not NOTHING."*** Addressing a remedy TO the parent asserts the parent holds it, which this pass cannot know |
LLAST: ⛔ **Step 3 — RESEARCH, aimed at what Step 2 named — opens next.**
QUOTE: **The deficit is now known, and it is the GENERAL POPULATION.**

---
---


## ROUND 1 · READER B — findings, raw

---

# Davis — Step 3 · RESEARCH · Reader B

**Frame:** Second Interwar (default) · **Run date:** 2026-09-15 · **Governing:** `LAW 0` · `LAW 0-R` ·
`00_RUNBOOK.md` L2526–2620 · `Disciplines/Real-World_Basis_Extrapolation_Method.md` · `Research_Logs/README.md`
· `02_Spine.md` §11 (the hand-forward).

> ## ⛔ WHAT THIS FILE IS AND IS NOT
> **It is real-world input data and a provenance record.** ⛔ **It contains no conclusion about Davis.** No
> institution, practice, custom, festival, person, demonym or price is proposed here. Nothing below says what
> Davis does. Where a real mechanism is described, it is described as the real culture's, and the reason it
> **cannot be transcribed** is stated instead of a fusion.
>
> ⛔ **GPS LAW OBSERVED THROUGHOUT.** The Vestfold Hills are admissible as a coordinate and a set of physical
> facts. **A real research station operates at this site; its operating nation, operators, funding body,
> institutional lineage, history, personnel and fate are forbidden input and were excluded on contact.**
> Three sources surfaced that material and the exclusions are itemized in Part B §6.
>
> ⛔ **ONE LOCATION, ON ITS OWN TERMS.** No other city — real or fictional — is used as a ranking, control or
> implicit normal. Real-world **comparables** are used, which `3.1` requires and the law expressly permits.

---
---

# PART A — RESEARCH FINDINGS

---

# ⭐⭐ PICK 1 — THE ABSENT INSTRUMENT OF REFUSAL

**The deficit researched against:** `02_Spine.md` §2.3 (`G8` DEFICIT) — *"No social instrument of refusal or
subtraction"*; §3.2 — *"All four generators are silent on any mechanism by which a decision about a person is
made, reviewed, or appealed"*; §5.2 — *"Nobody at Davis has ever stood in front of a person who could have said
no and did."*

**Method used:** `3.1` — find real cultures that **have** the instrument, and let the contrast write the
finding; and `3.2` — find real cultures that **lacked** it and evolved a workaround.

---

## 1.1 · The instruments that exist, sorted by WHAT THEY ACTUALLY REFUSE

Fifteen real refusal instruments were retrieved. They do not form one category. They sort into **six
structurally different objects**, and the sorting is itself the finding, because the spine's phrasing —
*"no veto, no refusal, no subtraction, no appeal, and no body that decides about people at all"* — collapses
six different absences into one clause.

| # | What is refused | Real instrument | The mechanical detail that makes it specific |
|---|---|---|---|
| **A** | **A PROPOSAL** | **Quaker "sense of the meeting"**; blocking / "standing in the way"; *standing aside* | The refusal is **recorded without a name**: a Friend who stands aside has the concern minuted as part of the sense of the meeting, but **"their name is not recorded in the minutes."** And the unity principle expressly **"does not give an individual Friend the authority to veto."** The clerk's fallback is not a vote — it is **"laying aside the matter indefinitely."** |
| **A′** | **A PROPOSAL, absolutely** | **`liberum veto`** (Sejm, first used **1652**) | One deputy shouting **`Nie pozwalam!`** (*"I do not allow"*) ended the session **and voided every act already passed in it.** The refusal is retroactive, not prospective. |
| **A″** | **A PROPOSAL, with a cost attached to refusing** | **Modern consensus practice**: *"consensus minus one"*, legitimate-block criteria | The instrument that actually fails is the one with **no criteria for what counts as a block**. Earthaven's remedy: blocker + advocates hold **up to three solution-oriented meetings** to co-create a replacement proposal; failing that it returns under consensus-minus-one, which means **"it takes two blocks, not one."** |
| **B** | **A PERSON, at the door** | **Blackballing** (17th c. onward); **kibbutz admission** | Physical, anonymous and unanswerable: each voter **"audibly casts a single ball into the ballot box under cover of the box… so that observers can see who votes but not how they are voting."** One black ball defeats the candidacy. In the kibbutz form, **"admission and expulsion of members must always go to a broad ballot"** and expulsion needs **two-thirds.** |
| **C** | **A PERSON, already inside — by the whole body** | **Amish `Bann`/`Meidung`**; **Athenian ostracism**; **Icelandic outlawry** | The Amish ladder ends in a **unanimous congregational vote**, after the offender is **publicly warned, given an opportunity to confess, and urged once more** — excommunication first (`Bann`), avoidance second (`Meidung`). Athens went the other way: **no charge, no defense, no trial, no appeal**, quorum **6,000 votes**, ten years' exile, **property retained and citizenship retained.** Iceland graded it: `fjörbaugsgarðr` = three years out, with **three named places of sanctuary and the roads between them, immunity holding only if he asks passage of at least three ships each summer**; `skóggangr` = **no fire, shelter or food from any inhabitant, and he may be killed by anyone without penalty.** |
| **D** | **A PERSON, by nobody in particular** | **`Murahachibu`**; **`charivari`/skimmington** | The sanction with **no office behind it at all.** Charivari was performed by **"young men temporarily bestowed with the power of rule over the everyday affairs of the community,"** **"carefully planned and often staged at times of traditional festivity,"** running **three to seven consecutive nights**, escalating through public ridicule → an impersonator paraded in the target's place → an effigy burned. There is no charge, no verdict, no appeal and **no author.** |
| **E** | **A LEADER** | **Haudenosaunee "dehorning"** | The refusal runs **upward**, and it is procedural: the Clan Mother must issue **three warnings** before symbolically removing the antlers. Grounds are named — **cowardice, dishonesty, drunkenness, or ignoring the will of the clan.** |
| **F** | **A TASK** | **Stop Work Authority / right to refuse unsafe work** | The only instrument in the set where **one person refuses the group** and is protected for it. Protection is conditional on **good faith**, a **reasonable apprehension of death or serious injury**, and having **asked first**. In most programs **"anyone on the job site can stop unsafe work, including employees, contractors, and even visitors."** |

> ### ⭐⭐ WHAT THE SORTING SHOWS — **changed a finding**
> **The spine's D2 names one absence. The real-world corpus shows that "an instrument of refusal" is not one
> thing but at least six**, and they are **independently present or absent** in real communities: a place can
> have (F) and lack (B); can have (D) and lack every one of (A)–(C); can have (C) and have no (E) whatsoever.
> ⛔ **This does not say which Davis has or lacks — that is not this step's to write.** ⭐ **What it changes is
> the shape of the question Step 4 inherits:** *the spine's single clause is a bundle of six separable
> questions, and answering it as one would be answering five of them by accident.*

---

## 1.2 · The instrument that decides about a person while removing the decider — **changed a finding**

**Three real mechanisms produce a decision about persons with no person as its author.** This is `3.2`'s
"workaround no design process would have invented," and it is the single highest-yield return of the pick.

1. **Hutterite colony branching.** At roughly **130–150 adult members** a colony splits. Leaders reorganize
   families by skills, ages and preferences into two workable halves — **and then the decision of which half
   goes is made by casting lots on moving day**, because the Hutterites hold that this **places the decision in
   God's hands.** ⭐ *The human judgment is spent entirely on making both outcomes survivable; none of it is
   spent on who receives which.* The stated reason for splitting is structural, not moral: **"when colonies are
   too small they become clannish and dominated by a single family, and when too large they do not provide
   enough employment for the members."**
2. **The Icelandic Commonwealth's procedural rule.** Cases at the Quarter Courts could be decided **"on the
   correctness of the legal procedure being followed. If one side followed the correct procedure and the other
   did not, the first side won the case, regardless of the facts of the matter."** The verdict is authored by
   the procedure, not by the judges. (Thirty-six judges per Quarter Court; **six dissenters deadlocked it**,
   which is why a Fifth Court taking simple majorities had to be added.)
3. **The Azande poison oracle (`benge`).** ⚠ **PARTIALLY REFUTED IN-RUN, RETAINED AT REDUCED WEIGHT.** I went
   looking for "a decision about a person routed through a non-person in a society with no central authority."
   The returned sources say the opposite in the part that matters: the oracle's answers **"carry the force of
   law, if it is so ordered by a prince,"** i.e. **enforcement is supplied by an authority, not by the
   oracle.** *Retained only as: the deliberative content can be delegated to a non-person; the binding force
   cannot be.* **Flagged as needing Evans-Pritchard's primary text before any use** — see open threads.

---

## 1.3 · What a community does when it has no instrument at all — **changed a finding**

**Four independent literatures converge on the same answer, and it is not "nothing happens."**

- **Sanctions appear anyway, ungraded and unaccountable.** Boehm's egalitarian bands run a **"reverse dominance
  hierarchy"**: the ladder is **criticism → ridicule → disobedience → shunning → ostracism → banishment → (rarely)
  capital punishment.** The mechanism is a **subordinate coalition**, not an office.
- **They target character, not conduct.** The Ju/'hoansi practice of **"insulting the meat"** is explicitly
  aimed at a disposition rather than an act: *"when a young man kills much meat he comes to think of himself as
  a chief… We refuse one who boasts, for someday his pride will make him kill somebody. So we always speak of
  his meat as worthless. **This way we cool his heart and make him gentle.**"* And the verbal shaming **scales
  with the size of the kill** — the better you did, the harder you are levelled.
- **The informal structure becomes an elite that cannot be removed.** Jo Freeman, *The Tyranny of
  Structurelessness*: a lack of formal structure **"disguised an informal, unacknowledged, and unaccountable
  leadership, and in this way ensured its malefaction by denying its existence."** Her precise mechanical
  claim: informal structures **"have no obligation to be responsible to the group at large; their power was not
  given to them and cannot be taken away; their influence is not based on what they do for the group, therefore
  they cannot be directly influenced by the group."**
- **A modern community that discovered the gap built the instrument from scratch.** The **Contributor
  Covenant** (released **2014**; on GitHub from **2016**; claimed adoption by **over 100,000 projects**) exists
  because open-source projects had no way to refuse a contributor. Its Enforcement Guidelines are a **four-rung
  ladder with each rung specifying a "Community Impact" and a "Consequence"**: **Correction** (private written
  warning, public apology may be requested) → **Warning** (no contact with the parties involved for a specified
  time) → **Temporary Ban** (from interaction and public communication) → **Permanent Ban** (**"a permanent ban
  from any sort of public interaction within the community"**). ⭐ *What is notable for a research input is the
  design choice: the ladder is defined by impact and consequence, and never by the offender's character.*

---

## 1.4 · Hirschman, and why an easy exit destroys the complaint — **changed a finding. Strongest single return of the pick.**

**Albert Hirschman, *Exit, Voice, and Loyalty*.** Exit is withdrawal; **voice is "attempt to repair or improve
the relationship through communication of the complaint, grievance or proposal for change,"** and voice **"can
be graduated, all the way from faint grumbling to violent protest."** The governing proposition:

> **"The greater the availability of exit, the less likely voice will be used."**

And the mechanism that matters most here — **the quality-conscious exodus.** In Hirschman's school case, the
members **most sensitive to decline leave first**, which removes precisely the constituency that would have
complained; the remaining members are **"unable or unwilling to voice,"** and the institution is **"locked into
that state,"** having lost **both** the exit signal and the feedback. He goes as far as calling one exit
channel **"a conspiracy in restraint of voice."**

Hirschman's own stated exceptions are equally usable and were deliberately retrieved: **loyalty suppresses
exit and therefore raises voice**; and he later conceded a case (the GDR, 1989) where **"exit triggered voice,
and both worked in tandem."** ⛔ **So this is not a one-way law and must not be imported as one.**

> ### Why this is a research finding and not a conclusion
> **It supplies a named, documented, third-party mechanism for a shape the spine reached independently** at
> §5.2 — *"a remedy-by-departure removes the demand for the remedy."* ⭐ **It also supplies what the spine did
> not have: the conditions under which the mechanism does NOT fire** (loyalty; high exit cost; exit-triggers-
> voice). **A source that only confirmed would have ornamented. This one supplies the falsifier.**

---

## 1.5 · Where the "no" actually lives in a real isolated settlement — **changed a finding**

**This is the sub-part of Pick 1 that had to be searched separately** (`LAW 0-R`: *a pick with a sub-part is at
least two picks*), and it returned the sharpest material in the section.

| Real mechanism | The detail |
|---|---|
| ⭐⭐ **The refusal happens BEFORE arrival, and a specialist administers it** | Polar winter-over screening is expressly **"a 'select out' rather than 'select in' methodology"** — criteria exist **"to eliminate those individuals who are most at-risk of psychological maladjustment and clinical decompensation,"** not to identify good candidates. It is run by designated physicians and clinical psychologists, on questionnaires plus interview plus general medical examination. **Nuance retrieved and kept:** *"the discovery or pre-existence of a pathology is not a direct reason for exclusion. Certain pathologies, which are controlled, may be allowed, while those that require regular follow-up or ongoing treatment are excluded."* |
| ⭐⭐⭐ **Where refusal is impossible, the BODY is altered instead** | At one civilian Antarctic settlement, **as of 2018 all residents, including children, are required to have their appendixes removed before coming**, as a safety precaution given limited healthcare access. ⭐ *A precondition is not a judgment. Nobody decides about the person; the person is made admissible in advance.* |
| **And the community's own "no" comes from outside it** | Home-brewing had been practiced at one Antarctic station from the 1990s until **2021, when the operating authority banned the practice.** *The refusal that finally lands on a station community is issued by a distant administration, not generated inside.* ⚠ *Operator identity stripped; retained as structure only.* |
| ⚠ **What actually happens when a wintering group cannot expel anyone** | A 2026 PNAS study of a **12-person, 10-month** Antarctic winter crew, using wearable proximity sensors plus repeated psychological assessment at months 1, 3, 6 and 9: **cohesion declined (F = 7.41, p < 0.001); conflict intensified (F = 4.82, p = 0.01); individual performance decreased (F = 3.56, p = 0.03); loneliness rose significantly (p = 0.01); ideas of reference rose 18.50 → 22.42 between months 3 and 6 (p = 0.03).** ⭐⭐ **And the counter-intuitive result:** higher proximity-based interaction strength correlated **positively** with conflict and paranoid ideation and **negatively** with cohesion and performance — **"more frequent contact did not equate to social support."** Sub-groups formed and hardened along **language and nationality lines**, **"especially pronounced toward the end of the mission in Month 9."** The station is described as **"completely cut off from the outside world, with no possibility of external assistance"** in winter. |

> ⛔ **THE N=12, ONE-CREW, ONE-WINTER CAVEAT IS RECORDED AS PART OF THE FINDING, NOT AS A FOOTNOTE.**
> *The study is a single crew in a single winter. Its effect directions are usable as a real, measured shape;
> its magnitudes are not a population statistic, and the sub-group axis it found (language/nationality) is a
> property of that crew's composition, not a law.*

---

## 1.6 · Two instruments retrieved that refuse NOTHING, and are here because they bound the category

- **The Nuer leopard-skin chief.** A mediator in homicide disputes who **"lacks any kind of political
  authority,"** **"had no power to coerce anyone or enforce their judgments,"** and whose role is
  reconciliation rather than punishment. ⭐ *An office can exist, be universally recognized, be the standard
  route for the hardest class of dispute — and still have no refusal power whatsoever.* **"Has an office" and
  "has an instrument of refusal" are independent variables.**
- **The ombudsman.** Created in **Sweden in 1809** (with a 1713 predecessor), to give **independent oversight
  from outside the offending institution.** Its limit is the point: **"Ombudsmen in most countries do not have
  the power to initiate legal proceedings or prosecution on the grounds of a complaint"** — it resolves
  **"usually through recommendations (binding or not) or mediation,"** or publishes a report.

---

## 1.7 · NOT FORCED — what Pick 1 did **not** return

⛔ **I did not find a documented real community that has no refusal instrument of any of the six kinds and is
described as stable in that condition.** Every case retrieved either (a) has a formal instrument, (b) has an
informal one (charivari, leveling, reverse dominance), or (c) has exit standing in for one (band fission —
which the sources say works **only** where **"land and resource territoriality must be absent or minimal, and
ease of mobility is necessary"**). **That is a result, not a gap, and it is left explicitly open.** It does not
license inventing one for Davis, and it does not license asserting that none is possible.

---
---

# ⭐ PICK 2 — COMPETENCE REBUILT BUT NEVER WRITTEN DOWN

**The deficit researched against:** `02_Spine.md` §2.2 (`G4`) — *"No living institution, and no correction
loop… Learning from a written record isn't the same as being taught by a living institution"* (L127); §5
**D3b** — *"The rebuilt competence was never written down"*, address **DIFFUSE**, consequence **Unspeakable**.

---

## 2.1 · The theory, stated by its author — **ornamented a finding**

**Michael Polanyi, *The Tacit Dimension*: "we know more than we can tell."** Tacit knowledge is **"personal and
cannot be represented or entirely encoded,"** is **"difficult to formalise and to communicate,"** and its
transmission **"relies heavily on direct interaction with a teacher and mentor."** The named failure mode is the
**expert blind spot**: as experience accumulates, step-by-step reasoning compresses into automatic pattern
recognition, the expert **"knows the answer at a glance,"** and **"many micro-reasoning steps have sunk below
the threshold of consciousness."**

⭐ **The operative consequence for a rebuilt-but-unwritten competence:** *the person most able to do the thing
is, by the same mechanism, the person least able to state it.* **Ornamented, because the spine already reached
D3b's shape; Polanyi supplies the name and the mechanism, not a change of direction.**

## 2.2 · The transmission form that refuses to explain — **changed a finding**

**Japanese craft apprenticeship: `minarai` / `minarau` ("learning by watching") and `gijutsu wo nusumu` /
`nusumu no gei` ("stealing the technique/art").** The master **demonstrates but does not teach.** Masters
**"do not nurture their apprentices, but rather make them work for their knowledge."** The stated rationale is
explicit and is not mysticism: **"people will place greater value on something they had to make an effort to
learn."** **"The emphasis of an apprenticeship is not on teaching, but on learning — observing and imitating,
rather than being shown how."**

> ⭐⭐ **Why this CHANGED rather than ornamented.** The spine's D3b treats "never written down" as a deficit
> with an unspeakable consequence. **This source is a real, durable, high-competence tradition in which the
> refusal to articulate is the METHOD, deliberately chosen, with a stated reason.** *It does not make D3b
> false. It removes the assumption that non-documentation must be read as a failure state.* ⛔ **It also does
> not say Davis does this** — and the divergence is stated below at §2.7.

## 2.3 · The structure of learning that has no teacher at its center — **ornamented a finding**

**Lave & Wenger, *Situated Learning*: legitimate peripheral participation.** Grounded in ethnography of
**Liberian tailors, Mayan midwives, US Navy quartermasters, non-drinking alcoholics, and US supermarket meat
cutters.** Newcomers **"begin to participate in a group by helping out with tasks that are easy and low-risk
but still valuable and important,"** and **"move from peripheral to full participation"** over time. Learning is
**"situated activity"** — a property of the community's practice, not of an instructor.

## 2.4 · The measured cost of losing it — **changed a finding. Sharpest single item in the pick.**

**FOGBANK.** A material for warhead refurbishment. The producing facility ran **1975–1989** and was
decommissioned by **1993**. By **2000**, when it was needed again, **"few records of its manufacturing process
had been retained"** and **"nearly all staff members who had expertise in its production had either retired or
left the agency."** Reproduction took until **2008** and cost **$92 million** (**$23M** seeking alternatives,
then **$69M** to actually reproduce it).

⭐⭐⭐ **And the cause of the failure is the finding:**

> **"A root cause investigation determined that this structural change had been implicitly relied upon in a
> downstream process, even though it had never been explicitly documented, tested, or controlled."**

**The new team's IMPROVED purification broke the product**, because it removed an impurity that the original
process had silently depended on. Once identified, the impurity was **added back in a separate production step
and monitored explicitly.**

> ### ⭐ THE TRANSFERABLE PROPOSITION, STATED AS A SOURCE FACT
> ***What a written record omits is not the hard part. It is the part nobody knew was load-bearing.***
> **And competence can therefore be lost by people who are doing everything better.** *This is a measured,
> attributed, dated instance — not a maxim.*

## 2.5 · The gap that exists even when the record is complete — **changed a finding**

**Work-as-Imagined vs Work-as-Done** (resilience engineering; Hollnagel and others; the distinction originates
in French ergonomics — *tâche* vs *activité*). **"Differences between Work-As-Imagined and Work-As-Done are
always present in complex systems, due to daily variability,"** arising from **contextual constraints and
technological limitations.** Safety practitioners study **"the adaptations in the gap between work as imagined
and work as done"** precisely because that gap is where both resilience and brittleness live.

⭐ *Combined with §2.4: the un-written part is not a residue left over after documentation; **it is generated
continuously by the difference between the written task and the performed activity**, and it re-accumulates
after every documentation effort.*

## 2.6 · What handover across a rotation actually achieves — **changed a finding**

Two independent measurements, retrieved separately:

- **Remote-station handover is short and is done body-to-body.** New winter personnel **"spend a week training
  with outgoing personnel before relieving them of their duties"** at one station type; at another, **"the old
  teams usually depart within one to two weeks of the new crew's arrival."** Long-term summer contract staff
  **become the winter crew**, so the handover is layered into an existing season rather than performed cold.
- ⭐⭐ **Even with the outgoing person physically present, structured handover is measurably necessary.**
  In clinical handover — the one field that has engineered and measured this — a structured electronic model
  cut the **handover error rate from 17.97% to 6.84% (P < .01)**, with nursing adverse events falling
  **11.17% → 4.72% (P = .015)**; an ED study cut **total errors from 102 to 25 (P < 0.0001)**; I-PASS
  implementations raised adherence **57.4% → 94%**. Across settings, reductions cluster around **60–75%**.

> ⭐ **The inference this permits, stated as a source fact:** *a handover conducted face-to-face, by the person
> who did the work, to the person about to do it, with the artifacts in the room, still carried an error in
> roughly one case in six before it was engineered.* **That is the ceiling of the best case. The written-record
> case is not on the same scale, and no source retrieved puts a number on it.**

## 2.7 · Reconstructing practice from a record alone — the named discipline — **ornamented a finding**

**Experimental archaeology** is the real-world discipline that does exactly what `02_Spine.md` §2.2 describes
the founders doing: recovering practice when only the record and the artifacts survive. It exists **because
artifacts and written sources alone do not illuminate past practice**; practitioners **"learned much through
the hands-on approach of actually making."** **Butser Ancient Farm** and **Lejre Land of Legends** are named
long-running reconstruction sites; **Janet Stephens** rebutted a standing theory about Roman hairpins by
reconstructing the hairstyles with a hairdresser's hands.

**And the loss case where a single lineage nearly ended:** Carolinian wayfinding was **"acquired through rote
learning passed down through teachings in the oral tradition."** By **1970 there were six *pwo* (master)
navigators left**, all on two islands, **several already too old to go to sea**; Mau Piailug had been the last
on his island recognized as *pwo*, in **1951**. Transmission resumed only because he **broke the tradition that
held the knowledge inside the navigator's family lineage** and taught outsiders.

> ### ⛔ WHY THIS SOURCE IS NOT A SPECIFICATION — divergence stated
> **Experimental archaeology and the wayfinding revival both run with a surviving corpus of comparative
> practice to check against** — other sites, other reconstructions, a living master in the wayfinding case.
> **`02_Spine.md` §5.1 records that Davis's case has no prior state anywhere to compare against.** *These
> sources therefore supply the method and its difficulty; they do not supply an analogue of the situation, and
> claiming one would be transcription.*

## 2.8 · NOT USED — and why

⚠ **"80% of the most important knowledge is unconscious and only 20% can be found in memos or books."**
Returned in the nuclear-knowledge-management material. ⛔ **NOT USED.** It is a round, quotable,
confident-sounding split with **no traceable primary measurement in the returned source**. This is exactly the
shape `LAW 0-R` names: ***a zero invites suspicion; a plausible number does not.*** The **qualitative** claim
around it is retained — retiring experts take **"tacit knowledge never before extracted from them,"** and
knowledge loss is managed as an **explicit operational risk class**, with the IAEA publishing a methodology for
**knowledge-loss risk management** keyed to **employee attrition**.

---
---

# ⭐⭐ PICK 3 — THE GENERAL POPULATION

**The steer:** `02_Spine.md` §11 — ***"The deficit is now known, and it is the GENERAL POPULATION… Research
picks must target the 40%, not the 60%."***

⛔ **DISCIPLINE OBSERVED:** nothing below is derived from the two known occupations. Every item is a real-world
attribute of an isolated, single-industry or single-purpose settlement, retrieved from a source about that
settlement's **non-specialist** population.

---

## 3.1 · The majority is not the named vocation, and the ratio is measured — **changed a finding**

| Measure | Figure |
|---|---|
| **Support staff per scientist at Antarctic stations** | ⭐ **"For every scientist, there are roughly four support staff members involved."** |
| **One national program's annual deployment** | **~3,000 participants; ~700 of them scientists** (≈ **23%**) |
| **Named support trades, from the hiring side** | electrician · plumber · carpenter · sheet-metal worker · welder · power-plant mechanic · fuel systems technician · boiler operator · maintenance engineer · field staff · chef · sous chef · baker · steward · **hairstylist** · comms/IT · medical · pilots |
| **The stated proportion, in plain words** | **"Research scientists only make up a small fraction of any station's staffing: most people in Antarctica are mechanics, cooks, plumbers, and other support staff."** |
| **Seasonal population swing** | **~4,400–5,000 in austral summer → ~1,000 in winter**, ≈ **5:1** |
| **Tour lengths** | summer personnel **3–6 months** (Oct–Mar); year-round staff **12–14 months** including the winter |

⭐⭐ **Why this CHANGED a finding.** *The 4:1 support-to-science ratio is not a texture detail. It is a
structural statement that in a settlement organized around a named purpose, **the named purpose is a minority
occupation**, and the settlement's actual working day is trades, maintenance, feeding, power, fuel and
logistics.* ⛔ **Stated as a real-world attribute. Not applied to Davis's own numbers, which are canon and not
this step's to touch.**

## 3.2 · The full service inventory a settlement of 56–150 people actually carries — **changed a finding**

Two civilian Antarctic settlements with resident families were retrieved. ⚠ **Operator nations and named
national institutions are stripped; only the structural inventory and the staffing counts are used.**

**Settlement A — 150 summer / 80 winter; families and children present:**
- A **1st–8th grade primary school, two teachers**, run **33 years** until it closed in 2018; over its life it
  educated **300+ children**.
- A **bank branch open year round, staffed by a sole banker.**
- A **post office** that receives mail and redistributes it to other installations in the area.
- A **hospital: one doctor, one nurse, two beds**, with **X-ray, laboratory, surgery, pharmacy and a dental
  clinic.**
- A **chapel** that draws people from beyond the settlement.
- ⭐ A **sports center described as "the main community hub"** — tennis, basketball, volleyball, exercise
  machines, ping-pong, **sauna**.
- A **small shop.**
- **Fourteen houses of 90 m² each.**
- ⛔ **The prophylactic-appendectomy rule** (see §1.5): a **precondition on the body**, applied to children too.

**Settlement B — 116 summer / 56 winter, of whom the winter complement includes 10 families and 2 school
teachers:**
- A **provincial school**, founded 1978, independent status 1997; it hosts a **Scout troop.**
- ⭐ A **civil register office where births and weddings are recorded** — the first birth in 1978, with **at
  least ten more children born there** by 2010.
- A **radio station**, broadcasting since 1979 on **shortwave and FM.**
- A **cemetery** with a memorial stele.
- **~1,100 tourists a year.**

> ### ⭐⭐⭐ THE STRUCTURAL PROPOSITION — **stated as a real-world attribute, not as a claim about Davis**
> ***The moment a settlement contains families rather than personnel, it acquires an administrative apparatus
> for the events of a life — birth, marriage, schooling, death — and the people who run that apparatus are
> counted in neither of the settlement's named occupations.*** **The registrar, the two teachers, the sole
> banker, the one nurse and the sports-hall are not support functions for the vocation. They are the
> settlement's own civil life, and they are staffed by ones and twos.**

## 3.3 · A settlement whose industry ended, and who is left — **changed a finding**

One Arctic single-industry settlement, post-industry:

- **~2,817 residents.** Mining ceased **2017**; the last mine ran to **30 June 2025.**
- ⭐⭐ **The population is transient by structure:** **43% of residents stayed less than two years; 64% stayed
  less than five.**
- ⭐ **70% of households are single-person**, against **41%** for the mainland — **a settlement of people whose
  families are elsewhere.**
- Employment now: **tourism and hospitality; research** (a university center with **350 students and a
  permanent faculty of 40**); **government services.** Tourism alone: **89,000 guest-nights** in one year,
  producing **200 man-years** of work.
- The service and civic inventory: a **school for ages 6–18**; a **hospital**; **one grocery store**; a
  **25 m swimming pool** in a sports hall; a **cinema, a youth club, a library and a gallery** run by the
  community council; a **church**; a **weekly newspaper.**
- ⚠ **No burial option exists** — a 1950 finding that bodies did not decompose in permafrost, raising concern
  about preserved pathogens. *(Not illegal to die there; there is simply nowhere to be buried.)*
- Residents are advised to **carry a rifle outside the settlement** against a specific local hazard.

## 3.4 · Non-working time, documented — **ornamented a finding, except where marked**

- ⭐ **One observance carries the whole calendar.** **Midwinter Day** (20/21 June) is **"the continent's primary
  cultural holiday,"** begun in **1902** as a deliberate imitation of Christmas and later established as its
  own holiday; it became continent-wide **after WWII, once year-round stations existed.** Content: multi-course
  feasts from ingredients **reserved for months** and shipped in the previous summer for exactly this purpose
  (**"alcohol and expensive foods such as lobster and ribeye steak are included in the annual summer food
  shipment for such occasions"**); **formal clothing**; galleys decorated with flags; **greetings exchanged
  between stations and from national leaders**; **music, dance and theater performances**; themed parties;
  **cold-water plunges or naked runs**; **breakfast in bed** at some stations; **card and gift exchanges**; and
  the tradition of **watching horror films about being trapped in the snow.**
- ⭐⭐ **A stated tradition of watching, back-to-back, the three film versions of the same trapped-in-the-ice
  story — after the last flight leaves for the winter.** *An annual, self-selected, self-mocking marker of the
  moment the settlement closes.* **Changed a finding**: it is a concrete, documented instance of a remote
  community **ritualizing the date it becomes unreachable**, using material about itself.
- **Alcohol is rationed and the ration is specific**: at one station, weekly, **"either a bottle of hard
  liquor, three bottles of wine, or a whole lot of weak beer."** **Home-brewing persisted for ~25 years until
  banned by the operating authority.**
- ⭐ **Plants are documented recreation, not only food.** Crop-growing tasks were rated **"enjoyable, engaging,
  meaningful, and stimulating"**; perceived **sensory-stimulation enjoyment increased over time**; the
  literature describes cultivation as a **"resilience countermeasure in austere environments"**, and plant
  interaction as able to **"alleviate cognitive fatigue, reduce monotony, and strengthen team cohesion."**
- **Food is an intermittent, weather-dependent event.** Fresh delivery is inconsistent; **"freshies"** is the
  standing term for what arrives and then stops. At one station the greenhouse **"is the only source of fresh
  fruit and vegetables during the winter."** Frozen stores are deep enough that one account reports finding
  supplies with **expiration dates as old as 2001**, still safe at storage temperature.

## 3.5 · NOT FOUND — recorded as a result

⛔ **No occupational census of a remote single-industry settlement was obtained.** I wanted an actual
breakdown — what percentage of a real remote settlement's workforce is service, maintenance, logistics,
domestic and childcare. **What I got instead was: a 4:1 support-to-science ratio, a 23% scientist share of one
program's deployment, and settlement-by-settlement service inventories staffed in ones and twos.** *That is
real and usable, and it is not the same thing as a census.* **The slot is left explicitly open**; the sources
that would close it are named in the open threads. ⛔ **No figure was estimated to fill it.**

---
---

# PICK 4 — THE PHYSICAL SITE

**Site:** Vestfold Hills, Ingrid Christensen Coast, Prydz Bay, Antarctica (**~68°35′S, 77°58′E**).
⛔ **Physical facts only.**

---

## 4.1 · The ice-free extent — **changed a finding, and it is a CORRECTION-CLASS result**

**Four different figures for "the Vestfold Hills' area" are in circulation, and they are not all the same
object.** I am recording what each source says and resolving nothing.

| Figure | What the source says it is |
|---|---|
| **512 km²** | the area the hills **"cover"** — the geographic feature |
| ⭐ **420 km²** | the **ice-free area**, in a list of Antarctic oases beside **McMurdo Dry Valleys ~4,900 km²**, **Bunger Hills 950 km²**, **Schirmacher Oasis 34 km²** |
| **~400 km²** | the figure carried in this pass's admitted set as the ice-free area *(L60, L120)* |
| **410 km²** | the pass's administrative extent `[COR]`, which `02_Spine.md` §6 already rules is **a different object** |

> ⛔ **NOT RESOLVED, AND DELIBERATELY SO.** `02_Spine.md` §6 already struck one conflation of two of these and
> recorded that **"the admitted set nowhere states they are the same object."** ⭐ **What Step 3 adds is that
> there are FOUR figures in play, not two, and that at least one published source distinguishes "the area the
> hills cover" from "the ice-free area" explicitly.** *Handed forward as a source-variance note.*

## 4.2 · Why the ground is bare — **ornamented a finding**

An Antarctic oasis is **"a large area naturally free of snow and ice."** The mechanism: **"very low humidity
and precipitation. Although these areas are very cold, sufficient solar energy is absorbed by the ground to
melt what little snow does fall, or else it is scoured or sublimated by katabatic winds, leaving the underlying
rock exposed."** Vegetation that survives is **bryophytes and lichens.** The Vestfold soils are characterized
in the microbiological literature as **hyperarid.**

⚠ **Read against `02_Spine.md` §2.1, which records this site's wind at ~5.6 m/s and expressly out of the
katabatic regime**, the general oasis mechanism is a class description and **the katabatic half of it is not
automatically this site's.** *Recorded as a scope, not a contrast — `M-158`.* The **low-humidity / low-
precipitation / solar-absorption** half is not wind-dependent and stands.

## 4.3 · The lake system, and its typology — **changed a finding**

| Attribute | Figure, as stated |
|---|---|
| **Lakes and ponds** | **over 300** |
| **Permanently stratified water bodies** | **37** |
| **Marine basins** | **six**, plus **seven seasonally isolated marine basins** |
| ⭐ **Salinity range across the stratified bodies** | **4 g/L to 235 g/L** |
| ⭐⭐ **Temperature range across the stratified bodies** | **−14 °C to 24 °C** |
| **Depth range** | **5 m to 110 m** |
| ⭐ **Surface elevation range** | **30 m BELOW sea level to 29 m ABOVE it** |
| **Concentration of meromictic lakes** | described as **"possibly the largest concentration of meromictic (stratified) lakes in the world"** |
| ⭐⭐ **Origin and AGE** | the lakes **"evolved from a marine origin only 3000–7000 years ago"**; one is **"a marine-derived, stratified lake… with an upper oxic and lower anoxic zone"**; another **"separated from Antarctic seawater thousands of years ago"** and shows **"steep gradients of salinity and temperature in the upper layer of the water column"** |
| **One hypersaline body, measured** | **~270 g/L**, max depth **36 m**, surface **−16 to 12 °C** with winter lows to **−20 °C**; only the top few meters exceed freezing in summer; **the salt keeps it liquid year-round** |

**Meromixis, as a mechanism:** a **mixolimnion** over a **chemocline** over a **monimolimnion**; the bottom is
**"hypoxic and more saline,"** circulates little, and **"the layers of water can remain unmixed for years,
decades, or centuries."** Dissolved oxygen can fall **below 1 mg/L** at depth against **10 mg/L or more** at
the surface, so **"very few organisms can live in such an oxygen-poor environment."**

> ### ⭐⭐⭐ THE HELIOTHERMAL RESULT — **changed a finding**
> **The peer-reviewed literature describes one of this site's lakes in exactly these words: "hypersaline,
> heliothermal and meromictic."** *Heliothermal = the deep layer is warmed by sunlight and cannot shed the
> heat, because the density gradient forbids convection.*
>
> **The mechanism, confirmed at another Antarctic oasis where it is measured:** under **3.5–4 m of transparent
> ice**, a three-layer lake runs **4–6 °C at the top, 7 °C in the middle, and 23 °C at the bottom**, with the
> deep water **"more than ten times"** the salinity of seawater. **The engineered version of the same physics —
> a salinity-gradient solar pond — holds ~30 °C over the gradient and ~90 °C in the storage zone**, because
> the halocline means **"convection occurs separately in the bottom and top layers, with only mild mixing."**
>
> ⭐ **So: on this site's own reported range, a body of standing water holds ~+24 °C, permanently, under an
> Antarctic sky, with no energy input but the sun and no machinery at all.** **It is not drinkable, it is not
> reachable without going through the cold layer, and it is not a resource in the ordinary sense — it is a
> physical fact about the ground.**

## 4.4 · Water budget — **changed a finding**

⭐ **Sublimation, not melt, dominates.** Stated directly in the Antarctic lake literature: **"the ice-cover
dynamics are controlled by sublimation — not melt — as the dominating ablation process and therefore surface
melt during austral summer does not provide significant amounts of water for recharge compared to subsurface
melt."** The continent averages the equivalent of **~150 mm of water per year** in precipitation.

⚠ **Scope note, `M-158`:** *that finding is measured at a different Antarctic lake system.* **It establishes
that sublimation-dominated ablation is a real, documented regime in Antarctic ice-free settings. It is not a
measurement of this site**, and this pass's own `G2` profile already carries this site's own precipitation and
retention figures, which are canon and untouched here.

**Closed-loop recovery, as engineered:** the ISS urine processor was **designed for 85% recovery** and had to
be **re-rated to 70%** because of **calcium sulfate precipitation** — the calcium coming from **the crew's own
bone loss in microgravity**. Recovered water feeds electrolysis for oxygen (operational **12 July 2007**);
throughput is **~9 kg/day for a six-person crew**.

> ⭐⭐ **The transferable proposition, as a source fact:** ***in a closed loop, the inhabitants' own bodies are
> an input to the chemistry, and the loop's rated performance is a function of who is living in it.*** *A
> measured, dated instance — not a maxim.*

## 4.5 · Freeze–thaw and salt weathering — **changed a finding**

**The dominant mechanism is not the one usually named.** Since the 1980s the **volumetric-expansion / 9%**
account has been demoted: those conditions — water-saturated rock, frozen rapidly from all sides, no
compressible air space — are **"considered unusual."** **Ice segregation** is the modern consensus: water
migrates by capillary action toward the freezing front and grows **ice lenses** that progressively weaken the
rock.

⭐⭐ **And the operative constraint is the window, not the cold.** **Frost weathering operates between −3 °C and
−8 °C**, and **requires water to be present** — *"unavailable moisture limits damage regardless of
temperature."*

**Salt weathering runs on the same physics** — brine seeps in, evaporates, crystallizes, draws in more salt by
capillarity, and forms **"salt lenses that exert high pressure on the surrounding rock."** **Sodium and
magnesium salts are the most effective.** It **"is most common in arid climates where strong heating causes
strong evaporation and along coasts,"** and it produces **tafoni** (cavernous weathering). It attacks
**"buildings made of any stone, brick or concrete."**

> ### ⭐⭐⭐ THE CO-LOCATION RESULT — **changed a finding**
> **The source expressly separates the two regimes by climate:** frost weathering dominates **"subarctic or
> alpine environments"**, salt weathering characterizes **"coastal and arid regions"** — **"distinct climatic
> niches with different triggering mechanisms."**
> ⭐ **A cold, hyperarid, coastal, hypersaline, ice-free site satisfies BOTH descriptions at once.** *This is a
> real and specific physical consequence of the site's combination of attributes, and it is the sort of thing
> that does not appear in either literature because each is written for the niche where the other is absent.*
> **Stated as a physical inference from two sourced regime descriptions, and labeled as such.**

## 4.6 · The light year at 68°35′S — **changed a finding. COMPUTED AND REPRODUCIBLE.**

⚠ **`M-141` is on record in this project: 22 cities carried wrong polar-night spans.** Rather than recall or
accept a figure, I computed the solar geometry at **φ = −68.5833°** using the NOAA fractional-year declination
series, evaluated at local solar noon for every day of a year. **The script is reproducible and is quoted in
Part B §3.**

| Result | Value |
|---|---|
| ⭐ **Polar night — standard convention** *(upper limb + refraction: sun's center below −0.833°)* | **38 days, ~3 June → ~10 July** |
| **Polar night — geometric-center convention** *(center below 0°)* | **49 days, ~29 May → ~16 July** |
| ⭐⭐ **Midnight sun** *(upper limb never sets)* | **55 days, ~25 November → ~18 January** |
| **Lowest solar-noon altitude of the sun's center, all year** | **−2.04°**, at the June solstice |
| ⭐⭐⭐ **Days in the year with NO civil twilight at all** | **ZERO** |
| **Civil twilight on the darkest day** | **≈ 4.99 h** |
| **Nautical twilight on the darkest day** | **≈ 8.13 h** |
| **Astronomical twilight on the darkest day** | **≈ 10.59 h** |

> ### ⭐⭐⭐ WHAT THIS CHANGES
> **1. The canon `~37-day` polar night is CORROBORATED** — my computation returns **38 days** on the standard
> convention, within rounding and within the sensitivity of the declination approximation and the assumed
> horizon. ✅ **The figure is not one of `M-141`'s casualties.**
> **2. The figure is CONVENTION-DEPENDENT by 11 days.** *A later phase reaching for "the dark period" without
> saying which convention it means will be off by nearly a third.*
> **3. ⭐⭐ THE UNSTATED HALF, which `M-158` forbids inferring and which Step 3 was supposed to be asked for:
> the polar night at this latitude is never dark at midday.** **At the solstice the sun's center sits only
> ~2° below the horizon at noon and there are ~5 hours of civil twilight.** *There is not one day in the year
> without it.*
> **4. ⭐ The year is ASYMMETRIC: 55 days of midnight sun against 38 days of polar night**, because refraction
> and the sun's semidiameter extend the one and shorten the other. **The bright half is the longer half.**

## 4.7 · Ski-only aviation — **ornamented a finding**

**Continental inventory:** ~20 airports; **15 runways** (gravel, sea-ice, blue-ice or compacted snow) and
**15 snow skiways limited to ski-equipped aircraft.** Four skiways exceed 3 km. Aircraft named: C-130 Hercules,
C-17, Twin Otter.

⭐ **Winter availability, stated plainly:** **"Flights to the continent in the permanent darkness of the winter
are normally only undertaken in an emergency, with burning barrels of fuel to outline a runway."** A 2008
development using **night-vision goggles** created a limited winter capability. At one interior station the
personnel **"are isolated between mid-February and late October"** — **roughly eight months with no flights** —
against **"several flights per week"** between October and February. The same station **lacks an MRI or CT
scanner**, so serious conditions cannot be fully evaluated during the isolation.

⭐ **Two-tier consequence worth carrying forward as an attribute:** *the aviation constraint and the medical
constraint are the same constraint.* **A settlement is not "hard to reach" in winter; it is a place where a
diagnosis cannot be completed** — which is the same structure as the prophylactic-appendectomy rule at §3.2,
retrieved independently from a different source.

---
---

# PICK 5 — THE REGISTERED TOPICS

⚠ **Ranked below 1–3 per `3.3`, and looked at far enough to know what each would have given.**

---

## 5.1 · Greenhouse agriculture in extreme climates — **changed a finding**

**A fully instrumented Antarctic greenhouse, 2018 campaign, measured:**

| Parameter | Value |
|---|---|
| **Growing area** | **12.5 m²** |
| **Total edible biomass** | **>268 kg** over **9 months** |
| ⭐ **Yield** | **27.4 kg/m²/year** = **0.075 kg/m²/day** |
| **Crops** | **26 different crops**; cucumbers **67 kg**, lettuce **56 kg**, leafy greens **49 kg**, tomatoes **50 kg** |
| **Light** | LED, **330–600 µmol/m²/s**; photoperiod **17 h/day** |
| **Air** | **21 °C**, **~65% RH**, **CO₂ 1,000 ppm** |
| ⭐ **Monitoring** | **32 HD color cameras plus spectral imagers**, automatic image analysis for anomaly detection, stress detection and **harvest-timing prediction** |
| ⭐⭐ **A husbandry result, not an engineering one** | **spread harvesting yielded ~400% more than single harvesting** |
| **Light response** | lettuce and red mustard **+35–90%** from 200→600 µmol/m²/s; tomato and cucumber fruit biomass **+8–15%** from 300→600 |

> ⭐⭐ **The `+400%` spread-harvest result is the finding.** *Identical hardware, identical light, identical
> crop — and a fourfold difference produced entirely by **when the hand goes in**. It is a tacit-practice
> result hiding inside an engineering trial,* and it is the point where Pick 5 and Pick 2 touch.

**Context figure, retrieved separately:** at one interior station the greenhouse is **"the only source of fresh
fruit and vegetables during the winter,"** growing **eggplant to jalapeños**, hydroponically, **no soil**.

## 5.2 · Limnology and lake-sediment paleoclimate — **ornamented a finding, with one change**

**Varves** are annual couplets: a **light lamina of silica and calcium carbonate** from summer microorganisms
over a **dark lamina of organic matter and fine sediment** carried in by spring freshets. **Two conditions are
required and both are absences:** varves **"commonly form under anoxic conditions,"** and **"varve formation
requires the absence of bioturbation."** Chronologies reach **13,200 varve years** (a chronology built from
thousands of sites) and, by cross-matching overlapping cores, **52,800 years** in one lake sequence.

**Paleolimnology's proxies:** **pollen** (vegetation history around the lake), **diatoms** (silica frustules
preserved in extractable quantity), **chironomid head capsules** (paleotemperature), and **organic matter with
carbon and nitrogen isotopes** (productivity and nutrient cycling). Resolution runs **annual to decadal**
depending on sedimentation rate.

> ⭐ **THE CHANGE:** **the two literatures join.** *A meromictic lake is precisely the body that satisfies both
> varve-preservation conditions — its monimolimnion is anoxic, and almost nothing lives there to stir it.*
> **The lake system at §4.3 is therefore, by its own physics, a recording medium**, and the record is legible
> because nothing is alive enough to disturb it. ⛔ **Stated as a property of the lakes. Not a claim about what
> anyone does with them.**

## 5.3 · Multi-disciplinary research institutions — **changed a finding for one case, source-death for another**

**What the registered topic actually returned was the wrong kind of institution, twice, and the right kind
once.**

- ⛔ **Bell Labs: SOURCE-DEATH.** The encyclopedic source **"focuses primarily on *what* Bell Labs invented
  rather than *how* it was organized to enable multidisciplinary collaboration."** No building layout, no
  corridor design, no management philosophy, no statement about mixing theorists with craftsmen. **Nothing
  usable was retrieved.** *Named secondary sources exist and are logged as an open thread.*
- ⭐ **The agricultural experiment station is the structurally relevant form, and it was not on the pick list.**
  Its founding statute (**1887**) mandates **"original research, investigation, and experiments which
  contribute to the establishment and maintenance of the agricultural industry."** The first permanent state
  station opened **1877**, in **two rooms on the lower floor of a university hall.** The modern system runs
  **600+ main and branch stations with ~13,000 scientists**, and scientists there **work with the producers
  directly** — farmers, ranchers, suppliers, processors — on **"biological, economic, and social problems of
  food and agriculture"**, paired with extension agents whose job is dissemination. ⭐⭐ ***This is the real
  institutional form in which the research subject IS the production: not two tribes and not two buildings.***
- ⭐⭐ **The long-experiment institution is the sharper find.** One research institution, founded **1843**, runs
  **seven Long-term Experiments**, including a wheat trial planted annually **since 1843** and a grassland
  study **"started in 1856 and… continuously monitored ever since,"** covering **28,000 m²**. It houses
  entomology, meteorology, botany, chemistry, biochemistry, **statistics**, genetics, nematology, soil science,
  virology and pedology under one roof — **~300 scientists, 100 administrative staff, 40 PhD students.**
  ⭐ **And its distinctive asset is an archive of physical soil and hay samples** used to reconstruct histories
  nobody was collecting for — **atmospheric pollution and nuclear fallout** among them.
  ⚠ **But: the source says nothing about how methodological continuity is maintained across generations of
  staff.** *That is the single question this pick was aimed at, and it is SOURCE-DEATH.* **Open thread.**
- **What the long experiment yields that nothing else can:** it showed that **conventional trials underestimate
  long-term biodiversity threats from soil acidification**, and produced **"one of the first demonstrations of
  local evolutionary change under different selection pressures."** ⭐ *Both are results that only exist because
  nobody stopped.*
- ⭐ **The teaching-and-research fusion, stated by a founder:** a marine laboratory's first director set as its
  organizing principle that **"other things being equal, the investigator is always the best instructor,"** and
  built the institution to **"combine research and education"** rather than separate them. It runs on a
  **summer course model** — a **six-week** introductory course from the 1890s; by 2024, **550 students from
  273 institutions and 58 countries** alongside **500+ visiting scientists and summer staff.** Supporting
  apparatus: a supply of organisms and **running sea water**, a **library from 1889**, and a **journal from
  1899 still edited in-house.**

---
---

# PART A — CLOSING NOTES

## What was WITHHELD (real, usable, deliberately held back)

| Item | Held for |
|---|---|
| The **six-way sort of refusal instruments** (§1.1) | **Step 4 / Phase 7 (Order)** — it is a question-shaping result and belongs where an institution is actually written, not here |
| The **Hirschman exception set** (loyalty; high exit cost; exit-triggers-voice) | **Step 4** — `02_Spine.md` §7.3's wording rule makes the *conditions* more useful than the rule |
| **Charivari's three-to-seven-night escalation ladder and its anonymity structure** (§1.1 D) | **Phase 6 / Phase 7** — it is the most concrete authorless-sanction mechanism retrieved and will be misused if it lands early |
| The **heliothermal lake** (§4.3) | **Phase 3 (Surface and Texture)** and **Phase 5 (Relation and Geometry)** |
| The **co-located frost + salt weathering regime** (§4.5) | **Phase 3** and **Phase 8 (Making)** — it is a materials constraint before it is scenery |
| The **+400% spread-harvest result** (§5.1) | **Phase 8 (Making)** — a tacit-practice result inside an engineering dataset |
| The **civil-twilight structure of the dark half** (§4.6) | **Phase 4 (Ordinary Life)** |

## What was OMITTED (genuinely did not fit — with the reason)

- **Every operator nationality, national institution and station history** encountered at or near the site.
  ⛔ **GPS law.** Itemized in Part B §6.
- **The `liberum veto`'s political-decline narrative** (bribery of deputies, paralysis, foreign leverage).
  *A polity-scale historical judgment about a specific real state; the mechanical detail — one voice voiding a
  session retroactively — is what was needed and is all that was kept.*
- **`Murahachibu`'s "eight-tenths / two exceptions" reading.** The source states plainly that **"there is
  little historical evidence to support this"** and that the word may be a corruption of *hajiku*, "to shun."
  ⛔ **The vivid detail is exactly the kind `3.5` warns about — kept only as a recorded folk etymology, never
  as a fact.**
- **The Contributor Covenant adoption controversy.** Off-target; the pick needed the enforcement ladder.
- **`skóggangr`'s kill-without-penalty clause** as anything other than a data point about how far real
  outlawry went. *Importing it anywhere would be `3.5`'s second failure mode exactly.*
- **The Azande oracle's ritual detail.** Retained only at reduced weight (§1.2), pending the primary
  ethnography.

## Divergences from source — **stated, per "divergence stated is stronger than resemblance implied"**

1. **Every consensus-and-veto tradition retrieved (Quaker, kibbutz, Amish, consensus-minus-one) presupposes a
   MEMBERSHIP with a boundary** — you can be admitted, so you can be refused. **The sources do not describe a
   community that decides about people without first having decided who is inside.** *Any use of them has to
   supply that, and this step does not.*
2. **Band fission works only under stated conditions** — **"land and resource territoriality must be absent or
   minimal, and ease of mobility is necessary."** ⛔ *A settlement whose habitable ground is a bounded ice-free
   oasis does not satisfy the first, whatever it does about the second.* **The mechanism is retrieved; its
   precondition is retrieved with it, and they travel together.**
3. **Both the reconstruction disciplines (§2.7) run against a comparative corpus.** *Neither is an analogue of
   a case with no prior state anywhere.*
4. **The oasis mechanism at §4.2 is stated with katabatic scouring as a component**, and this site's wind is on
   record as out of that regime. *The class description is a SCOPE, not this site's mechanism.*
5. **The sublimation result at §4.4 is measured at a different lake system.** *It establishes the regime as
   real and documented; it is not a measurement here.*

---
---
---


### B — PROOF BLOCKS

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md
LRANGE: 2526-2620
LINES: 95
L1: # Step 3 — Research, aimed at what Step 2 named
LMID:
LLAST:
QUOTE: > ## ⛔ ONE SEARCH AGAINST A PICK ESTABLISHES THAT THE PICK EXISTS. **IT DOES NOT ESTABLISH WHAT IT HOLDS.**

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/Real-World_Basis_Extrapolation_Method.md
LRANGE: FULL
LINES: 463
L1: # ⭐⭐⭐ LAW 0-R — RESEARCH FULLY. **A PICK IS NOT EXHAUSTED BECAUSE IT HAS BEEN SEARCHED.**
LMID: ### ⭐ IT IS A SEQUENCING RULE, NOT A REPEAL — **the prohibition above is UNCHANGED**
LLAST: 3. **A real detail beats an invented one every time.**
QUOTE: > ## ***THE LAW EXISTS SO A PLACE IS CHARACTERIZED BY WHO LIVES THERE, NOT BY WHOSE SITE IT OCCUPIES.***

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Stepwise_Execution/01_Spine/S05_Step_3_Research_aimed_at_what_Step_2_named.md
LRANGE: FULL
LINES: 152
L1: # Step 3 — Research, aimed at what Step 2 named
LMID: **3.2 Research can supply a substitute institution**, not only texture — a real culture that lacked the same
LLAST: > ☐ **Did I modify any file?** → **`graphify update .`** *(`CLAUDE.md`.)*
QUOTE: the one least like the others. **Look at each pick at least far enough to know what it would have given.**

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/README.md
LRANGE: FULL
LINES: 123
L1: # Research Logs — one per location
LMID: > for each particular location that keeps a record of exactly what it was that was researched in order to find
LLAST: | **Janbogo** | `Janbogo_Research_Log.md` | 2026-08-31 — Run 9 cold pass. 2 search queries + 3 fetches (1 failed, HTTP 402); Jang Bogo Station's real staffing/scale and its historical namesake. **5 open threads recorded**, incl. an unfused downfall-by-overreach parallel deliberately deferred to a later filter test |
QUOTE: | ⭐ **DEAD ENDS, and whether each died at the QUERY or at the SOURCES** | *(query-death is recoverable by re-framing; source-death is a real absence)* |

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Davis/02_Spine.md
LRANGE: FULL
LINES: 585
L1: # Davis — Step 2 · BUILD THE SPINE
LMID: | **For `DIFFUSE`** | ⭐ **The admitted set names no supplier**, so *"above Davis"* ≠ *"in the parent."* **And `PA-6` is explicit that the parent is UNWRITTEN — *"what the parent determines returns UNKNOWN, which is not NOTHING."*** Addressing a remedy TO the parent asserts the parent holds it, which this pass cannot know |
LLAST: ⛔ **Step 3 — RESEARCH, aimed at what Step 2 named — opens next.**
QUOTE: | ⭐⭐ **Step 3 — research** | **The deficit is now known, and it is the GENERAL POPULATION.** The admitted set describes only two roles and `00b` forbids answering from either. ⇒ ***Research picks must target the 40%, not the 60%.*** **Create `Davis_Research_Log.md`** *(verified absent)*; `LAW 0-R` binds |

## ROUND 1 · READER C — findings, raw

---

# Davis — Step 3 · RESEARCH — READER C

**Frame:** Second Interwar (default) · **Run date:** 2026-09-15 · **Reader:** C, working blind
**Governing:** `00_RUNBOOK.md` L2526–2620 · `Disciplines/Real-World_Basis_Extrapolation_Method.md` ·
`Stepwise_Execution/01_Spine/S05_Step_3...md` · `Cities/Research_Logs/README.md` · this pass's `02_Spine.md`
**Binding laws honored:** `LAW 0` · `LAW 0-R` · GPS law (site = coordinate + physics only) · ONE LOCATION ON ITS
OWN TERMS · NO FORCED FIT · source ≠ specification · the two failure modes (transcription; the vivid detail that
does not follow).

> ## ⛔ WHAT THIS FILE DOES NOT DO
> **It does not write Davis's culture.** No institution, practice, custom, festival, office, ritual, name, demonym
> or price is invented or proposed here. Every entry below is **a real-world attribute plus the structural
> contrast it draws against something Step 2 named as absent.** Where the contrast would require a decision about
> what Davis does, the decision is left open and marked.

> ## ⚠ A HARD BLOCKAGE HIT MID-RUN — RECORDED, NOT ROUTED AROUND (`S05` rule 5)
> **The session-wide web-search budget was exhausted at 200/200 calls part-way through Pick 2.** Four already-drafted
> queries were refused outright and are listed verbatim in Part B §4c. **`LAW 0-R` says there is no search budget;
> the tooling imposed one anyway.** The run continued on **direct URL fetches**, which were not capped — 64 of them —
> so the remaining picks were researched, but **by a weaker instrument**: a fetch requires guessing an address, so it
> cannot discover a source it does not already suspect exists. **Three of the four refused queries are now logged as
> open threads, not as covered ground** (Part B §7, threads 1–3).

---
---

# PART A — RESEARCH FINDINGS

*Each finding: what the source actually says · the source · and whether it **CHANGED** something this step hands
forward, or **ORNAMENTED** something already established.*

---

## ⭐⭐ PICK 1 — THE ABSENT INSTRUMENT OF REFUSAL

**The deficit, restated from `02_Spine.md` §2.3, §3.2, §5.2, §7.2:** no veto, no refusal, no subtraction, no appeal,
**and no body that decides about a person at all.** Rule 3.1 frame: find real cultures that HAVE one; the contrast
writes the finding.

**Twenty-two distinct instruments were examined.** They sort into six structural families, and the sorting is itself
the finding.

### A1.1 — THE FAMILY THAT CANNOT TRANSFER, AND WHY: expulsion presupposes an elsewhere and a carrier

Every classical instrument in the corpus — Icelandic *skóggangr* and *fjörbaugsgarðr*, Amish *Meidung*, Jehovah's
Witness removal, Jewish *ḥerem*, Romani *marime*, Athenian ostracism, Japanese *murahachibu* — **subtracts a person
by relocating them, socially or physically, into a space that is not the community.** Two preconditions are common
to all of them:

- **Somewhere to be subtracted TO.** Greater outlawry placed the convicted *outside the protection of all law*: after
  three months the outlaw could lawfully be killed by anyone, and anyone who sheltered, fed or assisted him became an
  accomplice ([Hurstwic](https://www.hurstwic.org/history/articles/society/text/laws.htm),
  [skjalden.com](https://skjalden.com/outlawry/)). Lesser outlawry excluded the person *from their home district for
  three years* while permitting travel to named foreign destinations — i.e. the sanction is a geography.
- **A population willing to carry it.** Viking-age societies had *no police*; "it was up to the community to uphold
  the law" ([OTHRAVAR](https://othravar.com/viking/norse-law)). *Ḥerem* required the whole community to cut off all
  ties — Amsterdam's ban forbade communicating with the man "not even in writing… nor [coming] within four cubits in
  his vicinity" ([Wikipedia, Herem](https://en.wikipedia.org/wiki/Herem_(censure)),
  [NEH](https://www.neh.gov/article/why-spinoza-was-excommunicated)). *Marime* is "a sentence of social death," and
  "not just the member, but his whole family will often be subject to a Marime verdict"
  ([Wikipedia, Kris](https://en.wikipedia.org/wiki/Kris_(Romani_court)),
  [Leeson](https://www.peterleeson.com/gypsies.pdf)).

**⇒ CHANGED a finding.** The profile records a *missing instrument*. The corpus shows the standard instrument is not
one thing but **a pair**: a verdict and an outside. A settlement that is the only settlement on its ground, whose
people cannot be handed to a neighbor and whose sanction cannot be enforced by anyone but themselves, **has not
lost a refusal instrument — the ordinary form of one was never available to it.** That is a different kind of
absence from the one the profile's wording implies, and it is a structural fact about ANY such site, not a
temperament.

### A1.2 — ⭐⭐⭐ THE ONE FORM THAT WORKS WHERE REMOVAL IS IMPOSSIBLE: separation without departure

The Rule of St Benedict, ch. 23–25, is the only instrument in the corpus that **subtracts a person while they remain
physically present, still working, still fed.** It is graduated and precisely specified:

- **Lighter faults:** "barred from the common table," and he "will not lead a psalm or an antiphon in the oratory,
  nor recite a reading by heart until he has made satisfaction." He eats *later* than the others — "if the brothers
  eat at noon, he will eat in mid-afternoon."
- **Weightier faults:** "excluded both from the table and from the oratory, and none of the brethren may join him
  either for company or for conversation. **He shall be alone at the work assigned him**… and let him take his meals
  alone in the measure and at the hour which the Abbot shall consider suitable."
  ([Christ in the Desert](https://christdesert.org/rule-of-st-benedict/chapter-24-degrees-of-excommunication/),
  [OSB text](https://archive.osb.org/rb/text/rbemjo1.html))

**Two properties make it the load-bearing item in this pick.** (1) The unit of subtraction is **the shared meal and
the shared assembly**, not the territory. (2) **The work continues** — the person is not relieved of the obligation,
only of the company.

**⇒ CHANGED a finding.** This is the mechanism-shaped answer Rule 3.2 asks research to supply: a real culture that
lacked the capacity to expel and evolved a workaround. ⛔ **Whether Davis has any version of this is not decided
here and must not be assumed** — the finding is that the shape exists and is documented, not that it fits.

### A1.3 — THE DECISION THAT IS A WRITTEN ENTRY

Three sources, independently, make the refusal's operative act **an inscription**, not a speech:

- **Quaker business meeting:** "Friends have not completed their action until they have approved the minute." The
  minute is composed by the clerk, **read aloud**, and confirmed before it becomes action. Where unity is not
  reached the meeting produces a **"minute of exercise," which "states the various perceptions in the meeting on a
  given matter" without forcing consensus** — and it "record[s] concerns without naming individuals." A Friend who
  stands aside is likewise not named: "the name of an individual standing aside is not recorded."
  ([New England Yearly Meeting](https://neym.org/faith-and-practice/decision-making))
- **Spinoza's ḥerem** was "entered in the *Livro dos Acordos da Naçao e Ascamot*, the community's record book," and
  read before the congregation ([NEH](https://www.neh.gov/article/why-spinoza-was-excommunicated)).
- **Reinstatement among Jehovah's Witnesses** is likewise an announcement with fixed wording: "It should simply
  state: '[Name of person] is reinstated as one of Jehovah's Witnesses.'"
  ([Wikipedia](https://en.wikipedia.org/wiki/Jehovah's_Witnesses_congregational_discipline))

**⇒ CHANGED a finding.** §3.1 of the spine establishes that at Davis "the legitimacy is in the log" and the
characteristic form of authority is "a dated observation rather than a person." **The corpus shows that a record can
be the operative act of a refusal and not merely its evidence** — and, in the Quaker case, that a record can
formally hold *an unresolved disagreement with no verdict and no names attached*. That is an instrument the pass did
not know existed. ⛔ Not assigned to Davis here.

### A1.4 — A BODY THAT DECIDES ABOUT A PERSON WITHOUT DECIDING FOR THEM

The **clearness committee** is convened for an individual and addresses exactly three classes of question:
personal concerns, **membership applications**, and marriage under the meeting's care. It is "appointed by one of
the standing committees of a Monthly Meeting" and "can be requested by anyone for any reason," and its stated
discipline is to aid "the person seeking clearness in **finding the answer within, rather than offering outside
advice or guidance**" ([Wikipedia](https://en.wikipedia.org/wiki/Clearness_committee),
[PYM](https://www.pym.org/faith-and-practice/faith-reflected-practice-daily-life/discernment-clearness-and-decision-making/)).

**⇒ CHANGED a finding.** §3.2's "shared silence" is stated as: no mechanism by which *a decision about a person is
made, reviewed, or appealed.* The clearness committee is a real counter-example that **is a body, does decide about
persons, and holds no authority over them** — it is the minimum viable form of the missing organ. ⚠ Its duration and
formal output are **not documented** in the source read (recorded as a source-death, Part B §4b).

### A1.5 — REFUSAL RELOCATED TO THE GATE, BECAUSE THE EXIT IS SHUT

Where removal is physically impossible for most of the year, the documented practice is to **move the entire refusal
forward, to admission**:

- Antarctic winter-over candidates undergo psychological evaluation whose explicit logic is **select-OUT**: "current
  crew selection does not seek to identify people with the most adaptable profiles. Instead, aptitude criteria are
  used to eliminate those individuals who are most at-risk of psychological maladjustment and clinical
  decompensation" ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13519399/),
  [45 CFR 675](https://www.ecfr.gov/current/title-45/subtitle-B/chapter-VI/part-675)).
- At one civilian Antarctic settlement the admission criterion is **surgical**: "all residents, **including children**,
  are required to have their appendixes removed" before arrival, because the on-site hospital cannot cover the case
  ([Wikipedia, Villa Las Estrellas](https://en.wikipedia.org/wiki/Villa_Las_Estrellas)).
- The window in which removal is possible at all is narrow and physical: winter personnel are "almost totally
  isolated" **mid-February to late October** at one station
  ([Wikipedia, Amundsen–Scott](https://en.wikipedia.org/wiki/Amundsen–Scott_South_Pole_Station)); another is
  "isolated from the outside world, having no transportation… for **9 months**"
  ([Wikipedia, Concordia Station](https://en.wikipedia.org/wiki/Concordia_Station)).

**⇒ CHANGED a finding.** §7.2 refuses to name the exit's gate in either direction, correctly. This supplies a
different, unasked-for fact: **in real communities with a closed exit, the refusal that exists is an ENTRY
criterion, and it is impersonal — medical, psychometric, procedural.** ⚠ The pass records that `G2` "already
performs the refusing — impersonally, absolutely, and adequately" (§5.2). The real-world pattern is the same shape
arrived at independently, which strengthens §5.2 rather than adding to it. ⛔ No entry criterion is proposed for
Davis.

### A1.6 — THE MEASURED COST OF HAVING NO INSTRUMENT, IN A CLOSED GROUP

A 10-month instrumented winter study of a 12-person crew (wearable proximity sensors at 10-second resolution, plus
UCLA loneliness, GPTS paranoia, cohesion, conflict and performance scales at months 1, 3, 6, 9):

| Measure | Result |
|---|---|
| Loneliness | significant positive slope, *estimate* = 2.42, *P* = 0.01; reached "moderate social isolation" |
| "Ideas of reference" (belief that others observe/gossip about one) | rose from *M* = 18.50 (month 3) to *M* = 22.42 (month 6), *P* = 0.03 |
| Team cohesion | declined, *F* = 7.41, *P* < 0.001 |
| Conflict | rose, *F* = 4.82, *P* = 0.01 |
| Individual performance | fell, *F* = 3.56, *P* = 0.03 |
| Total contact duration | fell significantly month 1 → 9 (K–S *P* = 10⁻⁴) |
| Subgroup structure | strong "assortativity with respect to nationality," intensifying by month 9 |

⭐ **The paradox the authors flag:** proximity *centrality* correlated **positively** with conflict and paranoid
ideation and **negatively** with cohesion and performance — "higher levels of proximity-based interaction were
positively correlated with conflict and paranoid ideation." Their conclusion: "it is not isolation per se, but
rather prolonged close physical confinement that may serve as a key precipitating factor in psychosocial strain."
([PNAS / PMC13229265](https://pmc.ncbi.nlm.nih.gov/articles/PMC13229265/))

A first-hand account from a 13-person crew adds the mechanism from inside: **thin walls prevent privacy and
residents cannot escape difficult relationships**, so the crew "confronts tensions deliberately, understanding that
escalation would be unwise" ([ESA Concordia blog](https://blogs.esa.int/concordia/2018/10/12/the-winter-over-syndrome/)).

**⇒ ORNAMENTED, with one CHANGED corner.** Mostly it supplies texture for a condition the spine already states. The
**changed** corner is the withdrawal direction: contact *duration falls* while conflict *rises*. In a group with no
instrument of refusal, the observed adaptation is **not confrontation and not expulsion — it is measurable
avoidance**, and avoidance is silent. That is the same failure shape §4.1 names as **LAPSE**, arriving from an
entirely independent direction (physiology and proximity sensors rather than obligation structure).

### A1.7 — THE THREE REAL SUBSTITUTES FOR A DECIDING BODY

Where no organ exists, three documented workarounds appear, and they are not variants of each other:

1. **Fission — split rather than subtract.** Hutterite colonies branch at 120–130 persons: "they buy land for the
   new colony, develop the new infrastructure, divide into two equal groups, and **choose by lot** which group stays
   and which moves." The article's own framing: "the branching system appears to be an alternative to expelling
   members," reinforced by the doctrinal point that leaving the colony carries eternal consequences, so "the
   colonies normally do not force their members out."
   ([Peaceful Societies](https://peacefulsocieties.uncg.edu/societies/hutterites/),
   [ResearchGate](https://www.researchgate.net/publication/352222436))
2. **Exhaustion — talk until nobody has anything left.** The Semai *bcaraa'*: a public assembly at the headman's
   house whose "purpose… is to settle the dispute **rather than to determine guilt or innocence**." Parties speak
   "for many hours, until no one has anything additional to say and everyone is exhausted"; the headman lectures on
   solidarity and interdependence, may levy a small fine — **and the fine is usually returned** to the guilty party
   as part of reintegration ([Peaceful Societies](https://peacefulsocieties.uncg.edu/societies/semai/),
   [Robarchek](https://peacefulsocieties.uncg.edu/wp-content/uploads/2015/11/Robar97.pdf)).
3. **Contest with a lay verdict.** The Inuit song duel: "the Inuit court system where disputes were settled by the
   verdict of the audience after the disputing parties had sung and danced their songs against each other." A party
   "so angry at the audience's laughter that he was unable to complete the duel… would automatically lose." Its
   stated purpose was "to cleanse the air between them while maintaining set guidelines for accepted behavior."
   Most Greenlandic courtrooms now hang a drum as the symbol of dispute settlement
   ([Trap Greenland](https://trap.gl/en/kultur/drum-dance-and-drum-song/),
   [TWoA](https://teenworldarts.com/magazine/conflict-resolution-greenland-style)).

**⇒ CHANGED a finding.** Three real mechanisms, none requiring a standing authority, none requiring an outside to
expel to. All three **produce an outcome without producing a judgment about a person's character** — which is the
precise inverse of the shadow §8.1 records. ⛔ None is assigned.

### A1.8 — ⭐⭐ THE ONE INSTRUMENT THAT DECIDES ABOUT WORK AND NOT ABOUT PEOPLE

The St Kilda "parliament": a meeting held in the street every morning after prayers, attended by all adult males.
**"No one led the meeting, and all men had the right to speak." "There were no set rules, no chairman and the
'members' arrived in their own time."** What it did: it "considered the work to be done that day **according to each
family's abilities** and divided up the resources **according to their needs**." And: "discussion frequently spread
discord, but **never in recorded history were feuds so bitter as to bring about a permanent division in the
community**" ([Thomas Tallis School](https://www.thomastallisschool.com/mrs-roberts-writes-archive/st-kildas-parliament),
[Wikipedia](https://en.wikipedia.org/wiki/St_Kilda,_Scotland)).

**⇒ CHANGED a finding — and it is the single closest structural match in the whole corpus.** It is a daily, universal,
chairman-less, rule-less assembly of an isolated community that **allocates labor and resources and is not recorded
as deciding about persons at all.** §3.2's "shared silence" describes a community with exactly this profile, and
this shows such a body is not a contradiction: **allocation and adjudication are separable, and a real community
separated them for centuries.** ⚠ **Whether the St Kilda parliament ever ruled on a PERSON is not established by the
sources read** — logged as open thread 12, and it is the one I most want answered.

### A1.9 — TWO WARNINGS ABOUT WHAT AN ABSENT ORGAN ACTUALLY PRODUCES

- **Freeman:** informal structure "forms the basis for elites"; an elite is "a small group of people who have power
  over a larger group of which they are part, usually without direct responsibility to that larger group, and often
  without their knowledge or consent." Combined with a myth of structurelessness, "there can be no attempt to put
  limits on the use of power. **It becomes capricious.** This lack of structure disguises an informal,
  unacknowledged, and unaccountable leadership, and in this way ensures its malefaction by denying its existence"
  ([libcom](https://libcom.org/article/tyranny-structurelessness-jo-freeman)).
- **Boehm:** an egalitarian order is **actively enforced**, on a ladder — teasing, ridicule, shunning ("the band acts
  as if the offending person doesn't exist"), banishment, and at the extreme assassination, which "an entire
  community can do… readily in the absence of 'bodyguards' or a loyal 'police force'"
  ([P2P Foundation](https://wiki.p2pfoundation.net/Reverse_Dominance_Hierarchy), Boehm 1993/1999). The Ju/'hoansi
  state the reason in their own words, via Tomazo to Richard Lee: *"when a young man kills much meat he comes to
  think of himself as a chief… We can't accept this. We refuse one who boasts, for someday his pride will make him
  kill somebody. So we always speak of his meat as worthless. This way we cool his heart and make him gentle."*
  ([Wikipedia, Leveling mechanism](https://en.wikipedia.org/wiki/Leveling_mechanism))

**⇒ CHANGED a finding.** These cut in opposite directions and both bear on §8.1. Boehm shows that **"no formal
instrument" does not mean "no enforcement"** — the enforcement simply becomes informal, graduated, and unwritten.
Freeman shows that the unwritten form is **not neutral**: it is *capricious*, and it is invisible precisely because
it is denied. §8.1 records Davis converting structural charges into character judgements "authorlessly… and invisibly
from inside." **Freeman is the real-world literature that says that outcome is what structurelessness reliably
produces** — which upgrades §8.1 from an inference about this place to an instance of a documented pattern. ⚠ **It
also raises a hazard for later phases:** Freeman's remedy is formal structure, and §8.2 notes Davis holds two
instruments already. Connecting them is *not* this step's call.

### A1.10 — EXIT AS THE SUBSTITUTE FOR VOICE

Hirschman's mechanism, stated by the source: "**Exit often undercuts voice** while being unable to counteract
decline, with loyalty serving to retard exit and permit voice to play its proper role"; the tested corollary is that
"increasing the number of exit options reduces voice," and conversely "greater exit and entry costs heighten the
likelihood of voice"
([Wikipedia](https://en.wikipedia.org/wiki/Exit,_Voice,_and_Loyalty),
[IPMJ test](https://www.tandfonline.com/doi/full/10.1080/10967494.2021.1878314)).

**⇒ ORNAMENTED, deliberately not more.** §5.2 already reaches this independently: "a remedy-by-departure removes the
demand for the remedy." Hirschman names the mechanism and supplies the empirical literature, but changes nothing —
recorded as ornament rather than dressed up as a discovery, per `LAW 0`'s companion test. ⛔ **And a guard:** the
§7.3 wording rule forbids characterizing the remaining population as self-selected. Hirschman's *loyalty* term is
exactly the concept that would smuggle that back in. **Do not import "loyalty."**

### A1.11 — NOT USED, WITH REASONS (see also Part B §5)

| Instrument | Why not used |
|---|---|
| **Athenian ostracism** — "no charge and no defense could be mounted"; quorum of 6,000; ten years; property retained; recallable | Requires a citizen assembly voting in body — precisely the organ named absent. Retained only as the **limiting case of subtraction without accusation** |
| **Liberum veto** — any deputy could end the session by shouting *Sisto activitatem!*; ~⅓ of ~150 sejms 1573–1763 passed nothing | An individual refusal so strong it consumed the body holding it. Retained only as a **failure case**, not a model |
| **Blackballing** — one black ball defeats a candidacy, anonymously; larger clubs require two | An admission-refusal held anonymously by every member. **Not used:** presupposes a membership institution |
| **Kris romani / marime** | Requires a standing authority — "only the head of the kris decides guilt and punishment" — plus a pollution ontology. No admissible analog |
| **Haudenosaunee "dehorning"** — a clan mother removes a sachem after warnings, for "cowardice, dishonesty, drunkenness, or for ignoring the will of the clan" | Removes an **office-holder**, not an ordinary person. Retained as the "removal by the body that appointed" pattern only |
| **Pitcairn / Tristan da Cunha councils** | Both sit under an external Governor or Administrator, so the refusal power is **delegated from outside the community** — a different object from an indigenous instrument |
| **Sociocracy's "paramount objection"** — "opposition must always be supported with an argument"; objections valid only if the proposal harms the group or obstructs its aim | A modern designed procedure, not an evolved one. Retained for **one distinction only**: objection-with-argument vs. veto-without |
| **Murahachibu** — the eight excluded categories (births, coming of age, weddings, sickness, memorial services, travel, floods, building/repairs); the two retained are **fire and funerals** | ⭐ Retained for the *shape* — a sanction that keeps two exceptions, both catastrophic — but **not used**: the folk etymology is explicitly flagged as having "little historical evidence" to support it. **A vivid detail that does not follow.** Cut per rule 3.5 |

---

## ⭐ PICK 2 — COMPETENCE REBUILT BUT NEVER WRITTEN DOWN

**The deficit, from `02_Spine.md` §2.2 and §5 (D3a/D3b):** the founders inherited a written record of the terrain
and no living institution to teach from; they rebuilt practical mastery "over generations of their own" (L127) and
**never wrote the rebuilt competence down** — address `DIFFUSE`, consequence **unspeakable**.

### A2.1 — ⭐⭐⭐ THE CONTROLLED EXPERIMENT ALREADY EXISTS, AND IT WAS RUN ON A LASER

Collins's TEA-laser study is the cleanest documented instance of a competence that survives only person-to-person:
**"no scientist succeeded in building a laser by using only information found in published or other written
sources. Every scientist who managed to copy the laser obtained a crucial component of the requisite knowledge from
personal contact and discussion."** And a second, sharper result: **"no scientist succeeded in building a TEA-laser
where the informant was a 'middle man' who had not built a device himself."** Collins's illustration of what the
gap actually is: if you had visited a working lab you built a metal framework to hold the capacitor close to the
top electrode; working from the circuit diagram alone you laid it on the bench with leads too long and the
inductance too high, and the laser did not work
([Physics Today Q&A](https://physicstoday.aip.org/news/q-a-harry-collins-on-acquiring-and-using-scientific-knowledge),
[Collins & Harrison 1975](https://journals.sagepub.com/doi/10.1177/030631277500500404)).

**⇒ CHANGED a finding.** D3b's consequence is recorded as *unspeakable*. The TEA-laser result says something
stronger and testable: **the failure is not that the knowledge is unspoken, it is that a speaker who has not done
the thing cannot transmit it either.** The middle-man result means a written record *plus* a person who has read the
record is still insufficient. ⭐ That is a direct, documented constraint on any transmission chain — and it is the
mechanism by which a competence can be genuinely alive, genuinely practiced, and still one generation from gone.

### A2.2 — THE INVERSE CASE: THE RECORD SURVIVED AND THE PRACTICE DID NOT

The F-1 engine. **"Every design document ever created for the Apollo program is still available"** in archives,
physical and digital. What is gone is the making: the engine "was largely handcrafted using methods that are no
longer common," with "complex welding techniques… [that] took skilled welders an entire day to complete a single
complex weld," by welders "some of whom originated from WWII production lines." And the diagnosis: **"many of the
tricks they used to get things to work and go together were kept in their heads or scribbled down on scraps of paper
long since lost"** ([Apollo11Space](https://apollo11space.com/why-cant-we-remake-the-rocketdyne-f1-engine/)).

Bessemer is the same shape in commercial form: he "patented an advanced steelmaking process but could not convey
its practical execution to purchasers, ultimately requiring him to establish his own steel company. Patent holders
possessed explicit information but lacked the embodied knowledge essential for implementation"
([Wikipedia, Tacit knowledge](https://en.wikipedia.org/wiki/Tacit_knowledge)).

**⇒ CHANGED a finding.** Davis's `G4` profile is **the exact mirror of the F-1 case**: there, the documents survived
the practice; here, per L127, a documentary inheritance survived and the teaching institution did not, and the
practice was rebuilt underneath it. ⭐ **The transferable point is that the two halves are independently mortal.** A
place can hold a complete written record of a subject and hold no ability to act on it, and the record gives no
signal that this has happened — which is the same silence §4.1 names.

### A2.3 — UNINVENTION: WHAT A GENERATIONAL GAP ACTUALLY COSTS

MacKenzie & Spinardi's argument, from the paper itself: tacit knowledge is "embodied in people rather than words,
equations, or diagrams"; **"if design ceases and if there is no new generation of designers to whom that tacit
knowledge can be passed, then in an important (though qualified) sense nuclear weapons will have been uninvented,"**
and their renewed development "would have some characteristics of **reinvention** rather than simply copying."
Designers "often cannot explain *why* certain design choices work — only that they do based on accumulated
experience." ⭐ And the paper's structural point: **testing is the correction loop.** "Without active testing
programs and prototyping cycles, designers lose the experiential basis for their intuitions"; knowledge may be lost
"not only through complete disarmament but also through measures such as a nuclear test ban."
([MacKenzie & Spinardi 1995, AJS 101(1):44–99](https://gwern.net/doc/radiance/1995-mackenzie.pdf))

**⇒ CHANGED a finding, and it is the strongest single item in this pick.** `G4`'s deficit is stated as *"No living
institution, and **no correction loop**."* MacKenzie & Spinardi supply the missing causal link between those two
clauses that the pass asserts side by side: **the correction loop is not a separate amenity — it is what keeps the
tacit half alive.** Remove the loop and the competence degrades even while the documents and the personnel remain.
⭐ And **"reinvention rather than copying"** is the precise term for what L127 records the exiles as having done.

### A2.4 — HOW THE TRANSMISSION IS ACTUALLY DONE, WHEN IT IS DONE

| Tradition | Mechanism, as documented |
|---|---|
| **Japanese craft apprenticeship** | *Minarai* = "apprenticeship, probation, and **learning by observation**." The governing phrase is *gijutsu wo nusumu* — "**stealing knowledge**"; *nusumu no gei*, "stealing the art." Masters "do not spoonfeed the apprentices with easy explanations, but rather make them work for their knowledge." The emphasis "is not on teaching, but on learning — observing and imitating, rather than being shown how" ([Japan Intercultural](https://japanintercultural.com/free-resources/articles/gijutsu-wo-nusumu-japanese-workers-stealing-knowledge-to-get-ahead/)) |
| **Journeyman years (*Walz*)** | "at least three years and one day"; must be "unmarried, childless and debt-free"; may not come "within a perimeter of **50 km** of his home town" except for an imminent death in the family; starts with a fixed token sum (historically five marks, now five euros) and must **return with the identical sum**; carries only trade tools and a log book. Each town stamps the **Wanderbuch**, which "qualifies as a record of his travels and also replaces the residence registration." Its documented systemic effect: "transmission of artistic style around Europe." ~800 active as of 2023 ([Wikipedia](https://en.wikipedia.org/wiki/Journeyman_years)) |
| **Oceanic wayfinding** | Carolinian navigation was "acquired through **rote learning** passed down through teachings in the oral tradition." By the 1970s Mau Piailug "was among the last people on Earth who had received complete traditional training… from childhood." The 2007 *pwo* ceremony on Satawal — **the first in 56 years** — initiated five Hawaiians and eleven Micronesians as *palu* ([Wikipedia](https://en.wikipedia.org/wiki/Mau_Piailug)) |
| **Situated learning** | Lave & Wenger: learning as legitimate peripheral participation; newcomers move from peripheral observation toward full participation. Explicitly **not** pedagogy — situated learning "is not an educational form, much less a pedagogical strategy" ([Wikipedia](https://en.wikipedia.org/wiki/Situated_learning)) |
| **Organizational transfer** | Szulanski's "**stickiness**": transfer is inhibited by factors other than lack of incentive — the nature of the knowledge, its source, its recipient, and the context. Named practices: mentorship, work shadowing, paired work, communities of practice, narrative transfer, after-action reviews. The governing caution: "information should not be confused with knowledge, nor is it, strictly speaking, possible to 'transfer' experiential knowledge to other people" ([Wikipedia, Knowledge transfer](https://en.wikipedia.org/wiki/Knowledge_transfer)) |

**⇒ ORNAMENT, with one CHANGED item.** Most of this is texture for a mechanism Step 2 already names. **The changed
item is the *Wanderbuch*:** a craft tradition whose transmission is deliberately undocumentable **still issues its
traveler a stamped book** — and the book records *where he was*, not *what he learned*. ⭐ **A record of movement in
place of a record of competence** is a real, documented solution to the exact problem D3b names, and it is not one a
design process would invent. ⛔ Not assigned to Davis.

### A2.5 — WHAT FAILURE LOOKS LIKE AT THE SEAM

Piper Alpha's inquiry found **"there was no written procedure for handovers."** On the night of 6 July "the handover
did not discuss the fact that a pressure relief valve had been removed and not yet replaced, and handovers did not
discuss active or suspended permits." Communication between departments, shifts and crews "was personal, informal
and tailored to the job," and "minimum standards were not set or met." The practice had drifted so that "maintenance
would sign off the permit and leave it in the control room or safety office" because operations were doing their own
handovers at the same time. The inquiry identified shift handover as **"the most vulnerable point in a permit's
lifecycle"** ([The Chemical Engineer](https://www.thechemicalengineer.com/features/piper-alpha-the-disaster-in-detail/),
[Human Factors 101](https://humanfactors101.com/incidents/piper-alpha/)).

**⇒ CHANGED a finding.** This is the *loud* failure of an undocumented handover — and it is the counter-case that
sharpens §4.1's bimodal split. The seam between two shifts, unlike a serial observation run, **has a moment at which
it fails and a system that announces it.** ⭐ The finding is the contrast: an undocumented handover in a system with
a failure signal produces a disaster and an inquiry; **an undocumented handover in a system with no failure signal
produces nothing at all** — which is why the second kind is not in the safety literature.

⚠ **Pick 2 is NOT exhausted.** The one sub-part that goes directly to D3b — *how isolated stations actually hand over
practice across personnel rotations* — was refused by the search cap (Part B §4c, open thread 1).

---

## ⭐⭐ PICK 3 — THE GENERAL POPULATION

**The deficit, verbatim from `02_Spine.md` §11:** *"The deficit is now known, and it is the GENERAL POPULATION. The
admitted set describes only two roles and `00b` forbids answering from either. ⇒ Research picks must target the 40%,
not the 60%."*

### A3.1 — ⭐⭐ THE RATIO IS A MEASURED THING, NOT A GUESS

Economic base theory splits employment into **basic** (exporting, bringing wealth in) and **non-basic** (local-serving).
The stated empirical regularity: **"Typically the basic/nonbasic employment ratio is about 1:1,"** i.e. a multiplier
of roughly 2 — each basic job supports about one local-serving job. The theory's own predictive use: if 5,000 basic
jobs are removed, "approximately 5,000 additional non-basic positions could be lost." Its stated limitation: it
"assumes export growth drives all regional economic development, largely ignoring investment, government spending,
and household consumption effects"
([Wikipedia, Economic base analysis](https://en.wikipedia.org/wiki/Economic_base_analysis)).

**⇒ CHANGED a finding.** This is the first **quantitative** handle on the 40% that does not derive from either known
occupation. It is a real-world comparable, stated flatly and without reference to any other city: **the ordinary
structure of a settlement built around an export function is roughly half export work and half local-serving work.**
⚠ Two guards, both binding: (1) this is a *comparable*, not a specification — it neither confirms nor overrides the
pass's own 35/25/5 tier data; (2) the theory's stated limitation means it **understates** the local-serving share
wherever consumption and public provision are large.

### A3.2 — ⭐⭐ THE NAMED TRADES, FROM AN ACTUAL HIRING ROSTER

The support workforce of a polar research program, as advertised by function
([USAP jobs](https://www.usap.gov/jobsandopportunities/)):

- **Skilled trades:** carpenters · electricians · pipefitters · welders · heavy equipment operators · mechanics ·
  firefighters · aviation mechanics · fixed-wing and helicopter pilots
- **Operations and logistics:** transportation and logistics staff · airfield management · waste management ·
  science project managers
- **Food and hospitality:** bakers · food service workers · lodging coordination · retail
- **Technical support:** information technology · telecommunications · communications
- **Medical:** physicians and medical support staff
- **Administration:** travel coordinators · **technical writers** · research support personnel

Structurally, the support function is subcontracted by **department**: science planning and program management ·
waste management · cargo · **lodging, food/beverage, recreation, retail, post office** (one contract) · IT and
communications · infrastructure, operations, transportation, logistics · regional operations · medical · design and
construction ([Wikipedia, USAP](https://en.wikipedia.org/wiki/United_States_Antarctic_Program)).

Scale: **~3,000 people at seasonal maximum**, overwhelmingly October–February; ~90% pass through one station;
station populations winter/summer roughly **150–200 / 800–1,000**, **~45 / ~150**, and **20+ / ~44** at three
stations respectively.

**⇒ CHANGED a finding.** This is the pick's core answer and it is an inventory, not an inference: **the
non-specialist majority of an isolated single-function settlement is trades, logistics, food, waste, medicine,
communications and administration** — and the one grouping that recurs as a single unit is *lodging, food,
recreation, retail and post*, i.e. **the business of living is organized together, separately from the business of
working.** ⚠ The precise scientist-to-support ratio is **not stated** in either source (source-death, Part B §4b) —
recorded as a hole, **not** filled by inference, per `M-158`.

### A3.3 — WHAT AN ISOLATED SETTLEMENT'S DOMESTIC AND CARE LAYER ACTUALLY CONTAINS

Three real settlements, read for their non-work infrastructure:

| | Facts |
|---|---|
| **An Arctic company town** | Pop. ~2,817 (2026), down from a mining peak. **43% of residents stayed less than two years; 64% less than five.** **70% of households are single-person, against 41% on the mainland**, because workers leave families behind. Three kindergartens plus a **13-grade school** for ages 6–18; families commonly relocate away when children reach 16–17. A hospital — but **"no care or nursing services and welfare payments are available."** One grocery store. Cinema, youth club, library, gallery, two museums, a church. A sports hall with a multi-sport floor, shooting range, climbing wall and 25 m pool. Residents are more educated than the national average (54% vs 43% upper secondary; 30% vs 26% tertiary) ([Wikipedia, Longyearbyen](https://en.wikipedia.org/wiki/Longyearbyen)) |
| **A civilian Antarctic settlement** | 150 summer / 80 winter, in **fourteen 90 m² homes**. A school operating 33 years, **two teachers**, grades 1–8, six pupils as of 2014, 300+ children over its life. A hospital with **one doctor and one nurse**, X-ray, lab, surgery, two beds, dental. A **bank branch open year-round, staffed by a single banker.** A chapel drawing people from across the island. A souvenir shop run by local women. ⭐ **"The sports center… functioning as the 'main community hub'"** — tennis, basketball, volleyball, ping pong, sauna ([Wikipedia, Villa Las Estrellas](https://en.wikipedia.org/wiki/Villa_Las_Estrellas)) |
| **A family Antarctic base** | **"56 inhabitants in winter, including 10 families and 2 school teachers"**; ~116 in summer; 43 buildings, 3,744 m². A provincial school, independent since 1997, with the southernmost Scout troop. **A civil register office where births and weddings are recorded.** A shortwave/FM radio station since 1979. At least eleven children born there ([Wikipedia, Esperanza Base](https://en.wikipedia.org/wiki/Esperanza_Base)) |

**⇒ CHANGED a finding, twice over.**
1. **The care layer is the one that is missing, not the service layer.** The Arctic town has a hospital and no nursing
   or welfare provision; the settlement with families has two teachers and one nurse. **Teaching and nursing are
   present at minimum viable count — one or two people — in every case.** That is the shape of the domestic/care
   fraction in a small isolated settlement: not a sector, a handful of named individuals.
2. ⭐ **The recurring civic center is the sports hall, not the meeting hall.** In three separate settlements the named
   "main community hub" or largest civic building is athletic. ⛔ **Not assigned to Davis, and explicitly flagged as
   the kind of detail rule 3.5 warns about** — but it recurs across three independent cases, which is what
   distinguishes a pattern from an interesting fact.

### A3.4 — NON-WORKING TIME, AS DOCUMENTED

- **Ritual, not merely recreation:** a midwinter dinner as the winter's morale anchor; an annual back-to-back viewing
  of three films of one title after the last flight of the season departs; "The 300 Club"
  ([Wikipedia, Amundsen–Scott](https://en.wikipedia.org/wiki/Amundsen–Scott_South_Pole_Station)).
- **Facilities:** indoor gymnasium, music room, library and recreation center (ibid.); a hydroponic greenhouse that is
  "the only source of fresh fruit and vegetables during the winter," growing crops as specific as eggplant and
  jalapeños, with "no soil" (ibid.).
- **Media made locally:** a station AM and shortwave radio service; a television station operating from 1973; a store,
  a barber and a bowling alley co-located with the radio station in the 1960s
  ([Wikipedia, McMurdo](https://en.wikipedia.org/wiki/McMurdo_Station)).
- **A large industrial cold city:** a polar drama theatre founded 1941; a museum, cultural center, cinemas, music
  schools; **80 general education institutions** (38 pre-school, 29 secondary, 6 preparatory, 1 lyceum, 6
  extracurricular centers); futsal and ice hockey clubs, curling, a sports palace, three district pools, a water
  park; polar night ~45 days ([Wikipedia, Norilsk](https://en.wikipedia.org/wiki/Norilsk)).

**⇒ ORNAMENT, with a CHANGED corner.** The inventory is texture. **The changed corner is that the leisure
infrastructure of isolated settlements is disproportionately about MAKING things that are consumed internally** —
a local radio station, a local theatre, a local greenhouse producing food nobody exports, rituals with no audience
outside. ⭐ That is a category of activity the 35/25/5 tier data cannot see, because none of it is production.

### A3.5 — ⭐⭐ THE BUILDING THAT IS THE SETTLEMENT

A subarctic mining town whose civic answer to the climate is a **single 1.3 km long, 15 m high structure** — "The
Wall" — containing apartments, retail, educational facilities, a hotel, bars, restaurants, a supermarket and a
swimming pool, and sheltering the smaller residential buildings on its leeward side. Its purpose is explicit: to
let residents "conduct daily activities without venturing outside during the brutal seven-month winter season," and
specifically to "enable **non-mining residents** to remain indoors throughout winter months." ~2,256 residents
(2021); ~1,600 employees at the mine; mining generates over 80% of municipal revenue
([Wikipedia, Fermont](https://en.wikipedia.org/wiki/Fermont)).

**⇒ CHANGED a finding.** This is the answer to the question "what does the physical settlement look like when it is
designed around the **non-producing** population rather than the producing one." The mine did not need a wall; the
schoolchildren and the shopkeepers did. ⛔ **Not proposed for Davis.** It is recorded because it is the only case in
the corpus where the settlement's largest single artifact exists **for the 40%.**

### A3.6 — THE COUNTER-CASE: THE MODEL THAT EXISTS SO THAT NO GENERAL POPULATION FORMS

Fly-in fly-out: rosters of "a fortnight on and one week off," or month-on/month-off for more isolated sites, at
12–18 hour shifts. One operator estimated residential employment would cost an additional **"$100,000 per person per
year"**; converting 330 employees from residential to FIFO in one town would save **"$33 million a year."** The
documented effects: "economic leakage," housing distortion, and towns hollowing out — one settlement of 9,000 in
1938 reduced to 300 with "almost all employees of the local mines on fly-in fly-out rosters." Social findings: 30%
of surveyed employees reported families not in favor of the lifestyle; 25% reported family relationships "earnestly
disadvantaged"; children "suffer emotionally from the parent's absence"; and a federal inquiry linked the model to
increases in substance abuse and mental illness. Also a hard operational number: **"eight consecutive work days of
twelve-hour shifts is the maximum which employees are able to perform well at before fatigue begins to affect work
adversely"** ([Wikipedia, FIFO](https://en.wikipedia.org/wiki/Fly-in_fly-out)).

Monotowns are the opposite pole: 319 officially listed places, **~14 million people**, where all employment outside
"essential services (schools, shops)" comes from one employer — and where privatization caused private owners to
refuse housing, childcare and social services as "economically inefficient," producing "a radical decrease in
quality of life" ([Wikipedia, Monotown](https://en.wikipedia.org/wiki/Monotown)).

**⇒ CHANGED a finding.** Between them these bracket the pick: **FIFO is the case where the 40% is deliberately never
allowed to exist, and the monotown is the case where it exists and is owned.** A settlement that has a permanent
general population and no owner to provide for it sits between the two and is described by neither. ⭐ **That gap is
itself the result** — and per the NO FORCED FIT law it is left open rather than filled from either bracket.

### A3.7 — WHAT THE COMPANY-TOWN LITERATURE GIVES AND WHAT IT WITHHOLDS

Company towns supplied "stores, schools, churches, markets, and recreation facilities" alongside housing, and the
implied support workforce is "shopkeepers, teachers, clergy, doctors, and maintenance staff." Their characteristic
pathologies: shops "usually owned by the company… resulting in a monopoly"; workers "had no say in local affairs,
and therefore felt dictated to"; eviction as a strike weapon
([Wikipedia, Company town](https://en.wikipedia.org/wiki/Company_town)).

**⇒ DIVERGENCE STATED (rule 3.4).** The **service inventory transfers; the causal engine does not.** Every mechanism
in the company-town literature — the monopoly store, paternalism, eviction — **requires an owner who can refuse.**
That is exactly the instrument Pick 1 records as absent. ⭐ **So the company town is a source for what a settlement
must contain and an anti-source for how it is governed**, and stating that divergence is worth more than the
resemblance would have been. ⚠ The source also gave **no occupational breakdown** (source-death, Part B §4b).

---

## PICK 4 — THE PHYSICAL SITE

**Site as a coordinate and a set of physical facts only:** Vestfold Hills, Ingrid Christensen Coast, Prydz Bay,
~68°35′S 77°58′E. ⛔ **Everything about any station's operator, nation, lineage, personnel, funding or history that
surfaced during these fetches is WITHHELD** — see Part B §6.

### A4.1 — THE GROUND

Rounded, rocky coastal hills on the north side of a glacier, **subdivided by three west-trending peninsulas bounded
by narrow fjords.** Most hills stand **30–90 m**, the highest summit **~160 m**. Proterozoic crystalline basement
(the Vestfold Hills Block). Largely snow- and ice-free — classified as an **Antarctic oasis**
([Wikipedia, Vestfold Hills](https://en.wikipedia.org/wiki/Vestfold_Hills)).

⚠ **THE AREA FIGURE DOES NOT AGREE ACROSS SOURCES AND IS LEFT UNRESOLVED.**

| Source | Figure |
|---|---|
| This pass's admitted set (`02_Spine.md` §6) | **~400 km²**, ice-free area, ratified |
| [Wikipedia, Antarctic oasis](https://en.wikipedia.org/wiki/Antarctic_oasis) (list of oases) | **~420 km²** |
| [Wikipedia, Vestfold Hills](https://en.wikipedia.org/wiki/Vestfold_Hills) | **512 km² (198 sq mi)** |

**⇒ CHANGED a finding — negatively, which is the point.** A 28% spread between the highest and lowest published
figure for "how big the ice-free ground is." The likeliest cause is definitional (ice-free land vs. the whole block
including lakes, fjord water and islands), but **no source read states its definition**, so the reconciliation is
not available and is not guessed. ⭐ This is exactly `LAW 0-R`'s "a plausible number does not invite suspicion":
any one of the three would have been accepted alone. ⛔ **Nothing downstream should rest on the ice-free area being
a single known quantity**, and §6's existing warning that the 410 km² administrative extent and the ~400 km²
physical measurement are **two different objects** is reinforced, not weakened, by this.

### A4.2 — ⭐⭐⭐ THE LAKE SYSTEM IS A TYPOLOGY, AND THE TYPOLOGY IS A TIME SERIES

**Over 300 lakes and ponds**, with "possibly the **largest concentration of meromictic (stratified) lakes in the
world**" — **37 permanently stratified water bodies**, comprising **six marine basins and seven seasonally isolated
marine basins (SIMBs)**. The measured envelope across them
([Wikipedia, Vestfold Hills](https://en.wikipedia.org/wiki/Vestfold_Hills)):

| Property | Range within one ~400–500 km² area |
|---|---|
| **Salinity** | **4 g/L → 235 g/L** |
| **Temperature** | **−14 °C → +24 °C** |
| **Depth** | **5 m → 110 m** |
| **Surface elevation** | **30 m BELOW sea level → 29 m ABOVE** |

The formation mechanism is **isolation by uplift**: post-glacial rebound raises the land, and former marine
embayments are cut off one by one and thereafter evolve independently — the general mechanism is documented, with
typical present-day uplift "of the order of 1 cm/year or less," peak measured rates ~11 mm/yr in one rebounding
region, total uplift "several hundred metres near the centre of rebound," and a relaxation tail of "at least another
10,000 years" ([Wikipedia, Post-glacial rebound](https://en.wikipedia.org/wiki/Post-glacial_rebound)). One named
Vestfold basin is dated: it "was formed **6,000 years ago** when sea levels were higher" and remains isolated
([Wikipedia, Organic Lake](https://en.wikipedia.org/wiki/Organic_Lake)).

**⇒ CHANGED a finding.** The lakes are not a scenic inventory. **They are one physical process — isolation — caught
at different stages, and the stage each basin is at is legible from its chemistry.** A basin still connected, a
basin seasonally connected, a basin isolated 6,000 years: the same system, read at three points in time. ⭐ **And the
liquid-water envelope from −14 °C to +24 °C within a single small area is an unguessable physical fact** that no
recalled description of "Antarctic lakes" would produce.

⚠ **A second unresolved source disagreement:** the Vestfold Hills article gives **37** permanently stratified water
bodies; the meromictic-lake article gives "**21 lakes in Vestfold Hills**"
([Wikipedia, Meromictic lake](https://en.wikipedia.org/wiki/Meromictic_lake)). Not reconciled; likely different
inclusion criteria; **not averaged, not chosen between.**

### A4.3 — ⭐⭐⭐ WHICH BASINS CAN KEEP A LEDGER, AND WHICH PHYSICALLY CANNOT

Three sources, queried separately, converge on a constraint that none of them states alone:

1. **Meromixis preserves.** Bottom sediments of a meromictic lake "remain relatively undisturbed because there is
   little physical mixing and few living organisms to agitate them," which makes their cores valuable "for tracing
   past changes in climate." Stratification persists "for years, decades, or centuries"; the monimolimnion is
   hypoxic and more saline than the rest
   ([Wikipedia, Meromictic lake](https://en.wikipedia.org/wiki/Meromictic_lake)).
2. **Annual layering requires anoxia AND the absence of burrowers.** Varve formation "demands the absence of
   bioturbation," so "varves commonly form under anoxic conditions." Long chronologies are possible — a 13,200-varve
   national chronology; one lake sequence extending to 52,800 years
   ([Wikipedia, Varve](https://en.wikipedia.org/wiki/Varve)).
3. ⛔ **AND SALT DESTROYS THE ANNUAL SIGNAL.** "Varves form only in **fresh or brackish water**; salt water causes
   clay particles to coagulate uniformly year-round, **preventing distinguishable annual separation**" (ibid.).

**⇒ CHANGED a finding — and this is my single strongest result.** Put against A4.2's salinity envelope of 4–235 g/L,
the consequence is physical and unavoidable: **within this one small area, some basins keep a dated, year-by-year
record of everything that happened to them, and others — the most extreme, most distinctive, most striking ones —
physically cannot.** The distinction is not a matter of who observed what or how carefully. It is set by the water.

⭐ **The third-order chain, and it is an exact structural rhyme with `02_Spine.md` §4.1's bimodal split:** the pass
records Davis as "cost-dominant in the things that can report, and cost-ABSENT in the things that cannot," with
"the reliability of the loud half… offered as the evidence for the quiet half." **The ground under the city has the
same division, in its own substance, for reasons that have nothing to do with anyone living on it.** §4.1 was derived
from obligation structure; this is derived from chemistry; they agree. ⛔ **What Davis makes of that is not this
step's to write** — but the co-location of a readable archive and an unreadable one, a few kilometers apart, is now
a researched physical fact rather than a metaphor.

⚠ **Honest limit:** the varve constraint is stated for varves specifically. **Whether the hypersaline Vestfold basins
hold a non-annual sediment record of some other kind is NOT established by any source read** — one paper set on
Vestfold sediment cores was cited but unread (open thread 7). *Per `M-158`, no inference is written for the unstated
half.*

### A4.4 — THE EXTREMES ARE REAL AND THEY ARE LOCAL

- A hypersaline Antarctic pond at **45.8% salinity** — "200 to 474 g/L, dominated by **calcium chloride**," "30%
  greater salinity than the Dead Sea" — which "remain[s] liquid even at temperatures as low as **−50 °C**" and is
  "the only Antarctic hypersaline lake that almost never freezes." Dimensions: 300 m × 100 m, 0.03 km², mean depth
  ~0.76 m, max 2.1 m, ~3,000 m³. **It is also shrinking** — ~10 cm deep in January 1997; "almost dry everywhere
  except for an area of a few tens of square metres" by December 1998
  ([Wikipedia, Don Juan Pond](https://en.wikipedia.org/wiki/Don_Juan_Pond)).
- A Vestfold basin holding "**the highest recorded concentration of dimethyl sulfide in any natural body of water**,"
  meromictic, mean depth 7.5 m, a few hundred meters across
  ([Wikipedia, Organic Lake](https://en.wikipedia.org/wiki/Organic_Lake)).
- Hypersaline lakes generally: formed in endorheic basins where evaporation exceeds inflow, or by isolation of
  trapped seawater; some halotolerant bacteria in crystallized salt "survive for over 250 million years"
  ([Wikipedia, Hypersaline lake](https://en.wikipedia.org/wiki/Hypersaline_lake)).

**⇒ ORNAMENT, with one CHANGED item.** Mostly texture. **The changed item is volatility:** a hypersaline pond that
lost nearly its entire visible water body between two summers. ⭐ **The lakes are not a fixed inventory.** §3.1 of
the spine rests on the environment being **STATIONARY** — "the five-century-old record survived usefully because its
subject did not change." That claim is sound for bedrock, relief and climate normals. **It is measurably NOT sound
for the smallest, saltiest, shallowest basins**, which move between one season and the next. ⚠ This is a real,
sourced qualification on a load-bearing spine clause, and it is handed forward as such rather than smoothed over.

### A4.5 — THE WATER BUDGET, AND A DIVERGENCE THAT MUST BE STATED

An Antarctic oasis stays ice-free by three mechanisms: very low humidity and precipitation; "sufficient solar energy
is absorbed by the ground to melt what little snow does fall"; and snow "scoured or sublimated by katabatic winds,
leaving the underlying rock exposed" ([Wikipedia, Antarctic oasis](https://en.wikipedia.org/wiki/Antarctic_oasis)).
In the largest such oasis the wind mechanism dominates outright: a mountain snow-shadow plus katabatic winds where
"the dry wind evaporates the snow rapidly and little melts into the soil. During the summer, this process can take
only hours." That oasis receives ~100 mm/yr, almost all as snow, holds over 6,000 lakes and ponds, and has valley
floor mean annual temperatures of −14.7 °C to −29.6 °C with extremes +12.0 °C to −65.7 °C
([Wikipedia, McMurdo Dry Valleys](https://en.wikipedia.org/wiki/McMurdo_Dry_Valleys)).

⛔ **DIVERGENCE STATED (rule 3.4).** `02_Spine.md` §2.1 records this site's wind as **~5.6 m/s, out of the katabatic
regime, "so there is no event generator here."** **Therefore the katabatic scour mechanism — the dominant one in the
best-documented Antarctic oasis — DOES NOT TRANSFER.** The ice-free condition here has to be carried by the other
two legs: low precipitation and humidity, and solar absorption by dark exposed rock. ⭐ **This is the most important
negative result in Pick 4**, because "Antarctic cold desert" imagery is overwhelmingly katabatic, and importing it
would have been transcription of the worst kind — a vivid mechanism that does not follow.

⚠ **AND A HOLE, LABELED AND LEFT OPEN.** I could not obtain a **quantitative** sublimation-versus-melt share for a
low-wind coastal oasis. The generic sources give the mechanism but no numbers: sublimation is listed among ablation
components, with the note that solar radiation dominates "if air temperatures are low under clear skies," and
temperate ablation rates of ~2 mm/h — **"no specific percentages for sublimation's share in cold environments"**
([Wikipedia, Ablation](https://en.wikipedia.org/wiki/Ablation); see also
[Wikipedia, Sublimation](https://en.wikipedia.org/wiki/Sublimation_(phase_transition))). ⛔ **Per `M-158`, no
inference is written for the unstated half.** The pass's own 72.8 mm / ~28 mm / 38.5% retention figures stand on
their own admitted footing; **this research neither corroborates nor refutes them**, and must not be cited as if it
did.

### A4.6 — ⭐⭐ THE DAMAGE REGIME: THE WARM MONTHS ARE THE DESTRUCTIVE ONES

Frost weathering, as documented:
- Water expands 9% on freezing, generating up to **207 MPa at −22 °C** — but volumetric expansion requires
  water-saturated rock frozen rapidly from all sides with little compressible air, conditions the source calls
  "**unusual**."
- The dominant modern mechanism is **ice segregation**: water migrates by capillary action to a freezing front and
  grows ice lenses that weaken the rock cumulatively.
- ⭐ **The damage window is narrow: "anywhere at sub-freezing temperatures (between −3 and −8 °C) if water is
  present."**
- ⭐⭐ **"Damage results from repeated cycles rather than sustained cold"** — the *frequency* of freeze–thaw events
  matters more than absolute severity — and **"Dry, extremely cold environments lack the necessary moisture for
  either mechanism to operate effectively."**
([Wikipedia, Frost weathering](https://en.wikipedia.org/wiki/Frost_weathering))

Salt weathering is the competing process: saline solutions seep into cracks and evaporate, salt lenses grow by
capillary draw and "exert high pressure on the surrounding rock"; sodium and magnesium salts are most effective;
crystallization "is thus most common in arid climates where strong heating causes strong evaporation and along
coasts" ([Wikipedia, Salt weathering](https://en.wikipedia.org/wiki/Salt_weathering)). Its signature landform,
**tafoni** — cavities from under 1 cm to over 1 m with "smooth concave walls, and often round rims and openings" —
occurs in "the Arctic regions and Antarctica," with the unifying condition "high salt concentrations and frequent or
occasional desiccating conditions," and since the 1970s "most workers have advocated salt weathering as the primary
explanation" ([Wikipedia, Tafoni](https://en.wikipedia.org/wiki/Tafoni)).

**⇒ CHANGED a finding, and it corroborates a spine clause by an independent physical route.** `02_Spine.md` §8.3
closes on "ground whose **most dangerous season is its warmest**." The physics says exactly why, and it is not
rhetoric: **freeze–thaw damage requires liquid water and repeated zero-crossings, so it can only happen in the months
that cross zero.** §2.1 records **sixty days crossing zero daily** (Jan +3.2/−1.2; Dec +2.4/−2.2). ⭐ **The whole
annual weathering budget of this ground is spent in its summer.** The deep cold is inert; the warm endpoint —
`R-3`'s correction, flagged in §11 as "bigger than its grading" — is what breaks rock.

⭐ **Second-order, and it changes the pick's own framing:** the brief names "freeze–thaw damage regimes" as the
target. The literature says that in a **cold-arid, saline, coastal** setting, **salt weathering is the process most
workers now credit**, not frost. Both operate here in principle: the ground is coastal, the basins reach 235 g/L,
and the summer crosses zero daily. ⛔ **Which dominates at this specific site is NOT established by anything read**
— no rates were available from either source (two source-deaths, Part B §4b). Left open.

### A4.7 — ⭐⭐ THE LIGHT: THE POLAR NIGHT HERE IS NOT DARKNESS

The polar-night duration gradient, as tabulated: **68° → ~24 days · 70° → ~52 days · 78° → ~107 days · pole → ~179
days** ([Wikipedia, Polar night](https://en.wikipedia.org/wiki/Polar_night)). Interpolating between the 68° and 70°
rows brackets a ~37-day span at 68°35′ comfortably — **the brief's ~37-day figure is independently plausible and is
not contradicted.**

⭐ **The stronger result is the KIND of polar night.** The same source defines **civil polar twilight as the band
67°24′ – 72°34′**, where "the sun remains below the horizon but no more than 6° at solar noon," and states plainly:
**"During civil polar twilight, there is still enough light for most normal outdoor activities at midday because of
light scattering by the upper atmosphere and refraction."** The sky shows characteristic blue tones; "the middle of
the day will typically be the brightest time." **68°35′ falls inside that band.**

*Derivation, labeled as such and not as a source claim:* at midwinter, solar altitude at local noon ≈ 90° − (68.58°
+ 23.44°) ≈ **−2.0°** — two degrees below the horizon, well inside the 0° to −6° civil range. This is arithmetic
from the site latitude plus the axial tilt, offered as a check on the cited band, not as a substitute for it.

**⇒ CHANGED a finding, and it is a correction of an image rather than of a claim.** Nothing in `02_Spine.md` asserts
that the polar night is dark — §8.3 says "a four-month blaze of light and work followed by **an eight-month
carry**," which is about work and replenishment, not illumination. ⛔ **But the phrase "the dark half" (§2.1
GRUDGING TOLERANCE, §3 table, §8.3) is one short step from an inference that would be wrong.** The ~37-day polar
night at this latitude is **blue twilight bright enough to work outdoors at midday.** The long interval is defined by
low sun angle, cold, and the absence of a growing season — **not by blackness.** ⚠ Flagged for every later phase:
*going out in the dark half* is a real cost and is **not** a cost of not being able to see at noon.

### A4.8 — AVIATION: THE ACCESS WINDOW AND THE WORK WINDOW ARE THE SAME FOUR MONTHS

A compacted-snow skiway: "a groomed snow surface that can support **ski-equipped aircraft landings only**," roughly
8 m of compacted snow over 8–10 ft of ice, floating over 550 m of water; wheeled gear would break through into the
softer layers beneath. **"The skiway is typically in operation from November through the end of February."** The
surface is not static — the ice shelf it sits on is "on a continuous slow slide towards the sea," forcing three
relocations ([Wikipedia, Williams Field](https://en.wikipedia.org/wiki/Williams_Field)).

**⇒ CHANGED a finding.** `02_Spine.md` §2.1 gives the light-and-work block as **Nov–Feb** (13% of annual
precipitation across it). The skiway season is **the identical four months**, for entirely independent physical
reasons. ⭐ **Access and productivity are not merely correlated at this kind of site — they are the same window**,
which means everything that must arrive and everything that must be done compete for one interval. ⚠ **And a
correction to my own source handling:** the fetched summary described Nov–end-Feb as "a six-month window." **The
dates are four months.** The arithmetic in the summary is wrong; **the dated statement is the fact.** Logged in
Part B §4d as a caught error, because an unlogged one would have propagated.

⚠ **NOT ESTABLISHED:** the failure mode and seasonal degradation numbers for **sea-ice** runways specifically
(source gave the season, not the decay). Open thread 18.

---

## PICK 5 — THE REGISTERED TOPICS

*Ranked below 1–3 as the brief directs, but looked at far enough to know what each would have given (rule 3.3).*

### A5.1 — Greenhouse agriculture in extreme climates — **PARTIAL. The operational numbers were not obtainable.**

What was obtained: CEA controls temperature (air, nutrient solution, root-zone, leaf), relative humidity, CO₂, and
light (intensity, spectrum, duration, intervals), plus water quality, nutrient concentration, pH, cropping duration
and density. Yields "up to 20 times as much high-end, pesticide-free produce as a similar-size plot of soil."
**Electricity is the binding cost** — "high capital investment and energy operating costs — particularly the price
of electricity"; only **51%** of indoor farming operations surveyed in 2018 were profitable. **Labor was reported at
$2.35 per pound** for container farms. Economic crops are narrow: "tomatoes, leafy greens and herbs"
([Wikipedia, Controlled-environment agriculture](https://en.wikipedia.org/wiki/Controlled-environment_agriculture)).
A polar station greenhouse is "the only source of fresh fruit and vegetables during the winter," using "water and
nutrients and no soil," and producing crops as specific as eggplant and jalapeños
([Wikipedia, Amundsen–Scott](https://en.wikipedia.org/wiki/Amundsen–Scott_South_Pole_Station)).

**⇒ ORNAMENT.** It confirms what the pass already implies and adds one usable constraint — **the economics of
sheltered cultivation are set by energy, and the viable crop list is short.** ⛔ **What I wanted and did not get:
crew-hours per week to run a polar greenhouse, and mass yields.** That figure is the one that would size a grower
workforce, i.e. the one number in this pick that bears on the 60/40 split. **Four fetch attempts failed** (Part B
§4b/§4a); it is open thread 6.

### A5.2 — Limnology and lake-sediment paleoclimate — **strong, and it fed Pick 4.**

Proxies and what each records: **pollen** (terrestrial vegetation, disturbance, clearance); **diatoms**, "particularly
suited to paleolimnology" because frustules preserve and species track pH, nutrients and salinity; **chironomids**,
"bottom dwellers… very responsive to any fluctuation," whose head capsules record temperature, oxygen, salinity and
productivity; **organic geochemistry** (C and N isotopes, lignin and lipid biomarkers, C:N ratios) distinguishing
aquatic from terrestrial sources. Cores "can be dated quite accurately," and reconstructions run to thousands of
years across the Holocene ([Wikipedia, Paleolimnology](https://en.wikipedia.org/wiki/Paleolimnology)).

**⇒ CHANGED a finding — by feeding A4.3.** On its own this is discipline description. Queried a **third** time,
against varves and then against meromixis, it produced the salt/anoxia constraint that is this reader's strongest
result. ⭐ **That is `LAW 0-R`'s own claim reproduced in miniature: the convergence was invisible at one query and at
two, and appeared at three.**

### A5.3 — Multi-disciplinary research institutions — **thin at the sources, but one item earns its place.**

- **A seasonal, multi-institution model:** founded 1888, ~250 year-round employees (half scientists and support
  staff), expanding each summer to "more than 500 visiting scientists, summer staff, and research associates from
  hundreds of institutions," plus, in 2024, 550 students from 273 institutions in 58 countries. Founding principle:
  "other things being equal, **the investigator is always the best instructor**." Research and advanced training are
  deliberately fused across physiology, embryology, neurobiology, microbiology, imaging and computation; a shared
  library serves biology, biomedicine, ecology and oceanography
  ([Wikipedia, Marine Biological Laboratory](https://en.wikipedia.org/wiki/Marine_Biological_Laboratory)).
- ⭐⭐ **A research institution built without a teaching function — and the documented objection to it.** Founded on
  "the usefulness of useless knowledge": no students, no tuition, no classes; "Research is never contracted or
  directed. It is left to each individual researcher to pursue their own goals." 28 permanent faculty; ~190 visiting
  members a year from 100+ institutions. **Feynman's criticism, verbatim: "there's not enough real activity and
  challenge: You're not in contact with the experimental guys. You don't have to think how to answer questions from
  the students."** ([Wikipedia, Institute for Advanced Study](https://en.wikipedia.org/wiki/Institute_for_Advanced_Study))

**⇒ Feynman's objection CHANGED a finding; the rest is ORNAMENT.** `G4`'s deficit is "no living institution, and no
correction loop," and §3.1's synthesis is that "verification replaces authority." Feynman names **two distinct
correction loops that a purely contemplative research institution loses**: contact with people who run experiments,
and **having to answer a student's question.** ⭐ The second is the one worth carrying: **being asked to explain is
itself a correction mechanism, and a place with no teaching institution does not have it.** That connects D3a
(no living institution) to D3b (the rebuilt competence was never written down) by a route neither deficit states —
*you write a thing down, or articulate it at all, largely because somebody asks.* ⛔ Not written into Davis here.

⚠ **Bell Labs returned nothing usable** — the source carries the history and not the organizational philosophy.
Source-death, Part B §4b.

---

## A6 — CONVERGENCES ACROSS PICKS (recorded, not resolved)

| # | The convergence | Picks | Status |
|---|---|---|---|
| **C1** | **Both halves of §4.1's bimodal split have a physical twin in the ground.** Basins that can hold an annual ledger and basins that chemically cannot, a few km apart | 4 ← 5 | ⭐⭐⭐ Strongest result. **Not written into the city** |
| **C2** | **The correction loop is what keeps tacit competence alive** (MacKenzie & Spinardi: testing) — and **being asked to explain is a correction loop** (Feynman). Both bear on `G4`'s two clauses | 2 + 5 | ⭐⭐ Supplies the causal link the pass asserts without one |
| **C3** | **Access window = work window = Nov–Feb**, from skiway physics and from the light/precipitation record, independently | 4 | ⭐ Corroboration by a second route |
| **C4** | **Where the exit is shut, the real refusal instrument sits at the ENTRY and is impersonal** (medical, psychometric) — which is the same shape as §5.2's *"`G2` already performs the refusing — impersonally, absolutely, and adequately"* | 1 | ⭐ Independent arrival at a conclusion the pass reached from generators |
| **C5** | **Allocation and adjudication are separable**, and a real isolated community separated them for centuries (St Kilda) | 1 + 3 | ⭐⭐ Directly addresses §3.2's shared silence without filling it |
| **C6** | **The 40% is the half that needs the building.** The only settlement in the corpus whose largest artifact exists for the non-producing population built it for schoolchildren and shopkeepers, not for the mine | 3 | ⭐ Handed forward |

---

## A7 — ⛔ EMPTY SLOTS. **NOT FILLED. `NO FORCED FIT` APPLIED.**

1. **No real-world instrument in this corpus is a fit for Davis as a whole.** Twenty-two were examined; the closest
   structural matches (Benedictine separation-without-departure; the St Kilda parliament) match on *one property
   each*. ✅ **"None fits" is the result.** Nothing is nominated.
2. **The scientist-to-support ratio at a real polar program is not stated by either source read.** Not inferred from
   headcounts. **Hole, left open.**
3. **Whether salt weathering or frost weathering dominates at this specific site is not established.** Both operate
   in principle. No rates available. **Left open.**
4. **The sublimation share of the water budget for a LOW-WIND coastal oasis is not established.** The katabatic
   mechanism is explicitly ruled out as non-transferable; nothing replaces its numbers. **Left open.**
5. **Whether the hypersaline basins hold any non-annual sediment record is not established.** **Left open.**
6. **The ice-free area of the site is not a single agreed number.** Three published figures spanning 28%. **Left
   unreconciled.**
7. **What isolated stations actually transfer at a personnel handover is not established** — the query was refused
   by the tooling, not answered. **Left open, and it is the hole nearest to D3b.**

---
---


### C — PROOF BLOCKS

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/00_RUNBOOK.md
LRANGE: 2526-2620
LINES: 95
L1: # Step 3 — Research, aimed at what Step 2 named
LMID:
LLAST:
QUOTE: > ## ⛔⛔ THERE IS NO TIME LIMIT AND NO SEARCH BUDGET.

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Disciplines/Real-World_Basis_Extrapolation_Method.md
LRANGE: FULL
LINES: 463
L1: # ⭐⭐⭐ LAW 0-R — RESEARCH FULLY. **A PICK IS NOT EXHAUSTED BECAUSE IT HAS BEEN SEARCHED.**
LMID: ### ⭐ IT IS A SEQUENCING RULE, NOT A REPEAL — **the prohibition above is UNCHANGED**
LLAST: 3. **A real detail beats an invented one every time.**
QUOTE: > ## ***THE LAW EXISTS SO A PLACE IS CHARACTERIZED BY WHO LIVES THERE, NOT BY WHOSE SITE IT OCCUPIES.***

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Stepwise_Execution/01_Spine/S05_Step_3_Research_aimed_at_what_Step_2_named.md
LRANGE: FULL
LINES: 152
L1: # Step 3 — Research, aimed at what Step 2 named
LMID: **3.2 Research can supply a substitute institution**, not only texture — a real culture that lacked the same
LLAST: > ☐ **Did I modify any file?** → **`graphify update .`** *(`CLAUDE.md`.)*
QUOTE:    ✅ ***"None is sited here" must never read as "none is possible here."***

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/README.md
LRANGE: FULL
LINES: 123
L1: # Research Logs — one per location
LMID: > for each particular location that keeps a record of exactly what it was that was researched in order to find
LLAST: | **Janbogo** | `Janbogo_Research_Log.md` | 2026-08-31 — Run 9 cold pass. 2 search queries + 3 fetches (1 failed, HTTP 402); Jang Bogo Station's real staffing/scale and its historical namesake. **5 open threads recorded**, incl. an unfused downfall-by-overreach parallel deliberately deferred to a later filter test |
QUOTE: | ⭐ **DEAD ENDS, and whether each died at the QUERY or at the SOURCES** | *(query-death is recoverable by re-framing; source-death is a real absence)* |

### PROOF: /home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Davis/02_Spine.md
LRANGE: FULL
LINES: 585
L1: # Davis — Step 2 · BUILD THE SPINE
LMID: | **For `DIFFUSE`** | ⭐ **The admitted set names no supplier**, so *"above Davis"* ≠ *"in the parent."* **And `PA-6` is explicit that the parent is UNWRITTEN — *"what the parent determines returns UNKNOWN, which is not NOTHING."*** Addressing a remedy TO the parent asserts the parent holds it, which this pass cannot know |
LLAST: ⛔ **Step 3 — RESEARCH, aimed at what Step 2 named — opens next.**
QUOTE: | ⭐⭐ **Step 3 — research** | **The deficit is now known, and it is the GENERAL POPULATION.** The admitted set describes only two roles and `00b` forbids answering from either. ⇒ ***Research picks must target the 40%, not the 60%.*** **Create `Davis_Research_Log.md`** *(verified absent)*; `LAW 0-R` binds |

---
---

