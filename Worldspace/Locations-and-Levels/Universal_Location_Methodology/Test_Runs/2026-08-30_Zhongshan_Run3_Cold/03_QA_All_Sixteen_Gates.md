# Zhongshan — Run 3 (cold) — QA: all sixteen gates

**Gates 0–11 plus C · F · I · P · G.** **No gate in this methodology had ever been run on anything before this
document.** Every gate below is therefore a test of the gate as much as of the location, and is reported that
way.

**Raw scan output is pasted, never summarized** *(`00_RUNBOOK.md` Step 7)*.
**Five gates fired. Four produced corrections that are applied in `04_Corrections_Applied.md`.**

---

## Gate 0 — Does the completion claim match the file? *(fails in both directions)*

**Outward direction:** no tracker yet claims this pass complete. Nothing to reconcile.

**⚠ Inward direction — and it fired twice, externally, during the run.** Gate 0 also requires checking *"the
file's own open-questions list against what has actually been resolved elsewhere."* **Two standing claims were
false and had been for weeks or months:**

1. **`RESUME_HERE.md` §5 listed Sinheung's name as RESERVED.** It was made official **2026-07-14** — six weeks
   earlier. The stale claim had propagated into Run 1's observations and Run 2's protocol.
2. **The universe repo asserted the Sinian Federation "drove the war."** Retracted on developer ruling.

> **Neither was caught by the gate. Both were caught by a human reading the pass's own quotations.** **Gate 0's
> inward direction is the gate this methodology is worst at running on itself**, because the check requires
> knowing what has been settled *elsewhere*, and a pass only ever reads what it opens. **Recorded as a real
> limit.**

**VERDICT: PASS outward · FAILED inward, twice, corrected.**

---

## Gate 1 — Coverage

### Instrument verification, run before any conclusion was drawn from an absence

```
=== INSTRUMENT VERIFICATION (Gate 1): prove the scan can find a hit before trusting a zero ===
  probe 'round'              count=35    expected_hit=True  -> OK
  probe 'lake'               count=22    expected_hit=True  -> OK
  probe 'zzzznotpresent'     count=0     expected_hit=False  -> OK
  (whitespace normalized; dashes normalized; stems used, not whole words)
```

**Whitespace was normalized before scanning** — `04` Part IV records a prior defect where a phrase wrapped
across a line break and a single-line search could not match it. **Dashes normalized** — a prior defect where an
en dash broke `human-robot`. **Stems used, not whole words** — a prior defect where `funeral` missed *funerary*.

### Raw counts, pasted

```
=== GATE 1 — RAW COVERAGE COUNTS (pasted, not summarized) ===
Phase 2 composition    composition=5  arrival=10  born here=1  who is not here=1  retention=7
Phase 3 texture        sensory=1  sight=1  sound=1  smell=5  feel=2  seam=4  architect=5
Phase 4 ordinary       ordinary=8  routine=1  mundane=1  struggle=2  escap=1  downtime=2  leisure=1
Phase 5 relation       peer=4  parent=12  edge=5  crossing=3  depend=17  membership=1
Phase 6 meaning        belief=1  sacred=3  compact=3  death=4  dead=6  mourn=1  observ=6  holiday=0
Phase 7 order          work=22  econom=3  export=4  governance=1  transmission=3  apprentic=0
                       countercult=2  sanction=2  prohibit=0
Phase 8 making         cuisine=1  food=4  music=2  dress=11  cloth=0  language=4  slang=0  play=5  craft=1
Phase 9 populations    robot=15  human=7  population=28  inherit=3  emergent=1  swap test=1
Phase 10 catalog       landmark=0  named place=2  role=7  archetype=2  setting=1  event=20
Disciplines            general population=1  shadow=2  null=3  reserved=10  proposed=4  z ==1  z==0
```

### The five zeros, each classified into one of the four outcomes

| Term | Outcome | Reason |
|---|---|---|
| `holiday=0` | **covered in substance, absent in term** | Phase 6E delivers an observance (*The Turn of the Round*); `observ=6`. The location's own register is "the day the order resets," not "holiday" |
| `apprentic=0` | **covered in substance, absent in term** | Phase 7c answers transmission — trades pass *by proximity* — which is a real mechanism and deliberately not an apprenticeship |
| `cloth=0` · `slang=0` · `landmark=0` | **covered in substance, absent in term** | `dress=11`; the speech marker is directional-by-water; Phase 10 heads its section *Named places* |
| **`prohibit=0`** | ⚠ **absent, and only half-explained** | `03` Phase 7b states *"Prohibitions live here."* The pass argues Zhongshan has **no sanction** because it has **no leverage** (four cheap exits, mild climate) — which explains the absence of *penalties* but never explicitly says the city therefore has few *prohibitions*. **Corrected.** |

**Never inserted a word to make a scan pass.** *(`04` Gate 1's binding rule.)*

**VERDICT: PASS, with one under-explained null corrected.**

---

## Gate 2 — General population *(with the Band-1 inversion — N/A here, this is Band 4)*

```
=== GATE 2 — general-population risk scan ===
  'everyone'           3      'every resident'     0      'all residents'      0
  'residents '         5      'a resident'         1      'the whole city'     0      'universal'          3
```

**Every finding checked against `00b`'s highest-risk categories.**

| Category | Verdict |
|---|---|
| Dress | **PASS.** Re-soled footwear derives from a requirement *every* resident meets — walking on rock and ice in the same trip. Not a trade's uniform |
| Sensory first-impressions | **PASS.** Sight/sound/smell/feel are site properties, not one institution's interior |
| Visitor experience (5d) | **PASS** |
| Per-population culture (Ph 9) | **PASS.** The arrival-order axis is explicitly cross-cutting, not a subgroup's view |
| **Music** | ⚠ **FAILS** |

> ### ⚠ GATE 2 FIRES — Music
>
> **`00b` is explicit: *"a place's professional performers are not its musical culture,"* and names music among
> the worst offenders.** The Phase 8 music finding describes **performers waiting on the ice and playing
> non-metrically against thermal cracking.** **That is a performance practice, and the pass offered it as
> Zhongshan's music.**
>
> **This is the exact failure `00b` was written about**, reproduced in a pass whose author had read `00b` the
> same day. **Recorded as evidence that reading the discipline does not discharge it.**
>
> **Corrected** in `04_Corrections_Applied.md` — a genuine general-population answer is written, with the
> performance practice retained as an explicitly-scoped narrow case on top of it.

**VERDICT: FAILED on one category, corrected.**

---

## Gate 3 — Internal contradiction *(read Ordinary Life last, check everything against it)*

**Phase 4 read last, as required.** Every other phase checked against it.

| Checked | Result |
|---|---|
| Ph 3 *"no single date on which spring arrives"* vs Ph 4 *"days organized around thaw state"* | **Consistent** — the second is the lived form of the first |
| Ph 7c *skill distribution is geographic* vs Ph 4 *archipelago commute* | **Consistent** |
| Ph 8 *footwear/re-soling* vs Ph 4 *rock-and-ice walking* | **Consistent** |
| **Ph 6 compact — *"you will be here when it is your turn"*** vs **Ph 4 — *"nothing here tells you that you are falling behind"*** | ⚠ **APPARENT CONTRADICTION** |

> **Gate 3 fires, and resolves — which is the gate working, not failing.**
> A compact requiring presence on a schedule *is* a deadline, and Phase 4 claims the city has none.
>
> **Resolution, and it sharpens both:** The Round's interval is long, and **a missed leg is visible only to the
> next walker, not to the person who missed it.** The compact is real and it is enforced by nobody, late, and
> to one other person. **So both stand: there is a deadline, and it is the only one, and it is exactly as weak
> as the spine predicts.** The reconciliation is written into the corrected text rather than left implicit.

**VERDICT: PASS after one resolution.**

---

## Gate 4 — Swap test

**Partner chosen to make the gate *able* to fail** *(`04` Gate 4: pick the one most likely to survive the swap,
not a convenient comparable)*. **Chosen: Casey** — same subnet, coastal, mean −9.3 °C against Zhongshan's
−9.9 °C *(the closest climate match in the country)*, comparable size, Census II 1,042,031.

| Finding | Survives swap onto Casey? |
|---|---|
| **I** — joined, not founded | **No.** Requires the continuous-habitation exception, which is Zhongshan's and Byrd's alone |
| **VI** — architectural monoculture | **No.** The mechanism is a 3.69:1 plurality ratio. **Casey's is 1.15:1** (USA 21.96% / 19.06%). The finding is arithmetically unavailable there |
| **VII** — The Round | **No.** Requires ~150 unconnected lakes |
| **XIV** — arrival-order outranks kind | **No.** Requires a pre-exile resident population |
| **IV** — no Peninsula nations present | **No** — Casey's top nation *is* the USA |
| **Ph 8 — "route-argument as pastime"** | ⚠ **YES, largely** |

> **Weakest finding under the swap, recorded as `04` Gate 4 requires:** **the route-argument pastime.** Any
> city on complex terrain could hold trivial opinions about which way round. **It survives only on the
> archipelago justification, which is thin support for a named custom.** Kept, but downgraded in the corrected
> text from a named pastime to a texture note.

**VERDICT: PASS. One weak finding identified and demoted.**

---

## Gate 5 — Cross-location consistency

- **Import coherence.** Zhongshan cannot feed itself and imports from **Davis** — canon-consistent; Davis is the
  established breadbasket, 2nd stop down Hwy 110. ✓
- **Export coherence.** Dressed stone from orthogneiss/pegmatite/granite. **No canon conflict found**; no other
  city claims to supply Mirny-subnet stone. ✓
- ⚠ **Shared-environment consequence — a real one, and it must be flagged rather than resolved here.**
  The eastern lakes are brackish because **the Dålk glacier calves into that corner of the oasis.** **The oasis
  is shared with Sinheung and Shirayuki.** A glacier surge is not a Zhongshan-only event. **This binds beyond
  this location** → per §E question 3, **routed to RESERVED / REQUESTED rather than decided.** See the input
  requests.
- **New categories are legitimate discoveries** — the check is only whether they are named and cross-referenced.
  **The Round**, **The Standing Objection**, and **The Turn** are new. **Cross-referencing is a Step 9 action
  and is listed there.**

**VERDICT: PASS, with one cross-location consequence escalated.**

---

## Gate 6 — Duplicate institutions

> ### ⚠ **UNRUNNABLE IN THE COLD PHASE — BY CONSTRUCTION, AND THIS IS A METHODOLOGY FINDING**
>
> Gate 6 checks against **completed siblings** using **the differentiation instrument** (`04` Part III).
> **Zhongshan's siblings are Sinheung and Shirayuki, and their material — including the cluster's purpose-built
> `Tri-Cities_Overlap_and_Distinguishing_Guide.md` — is exactly what the cold protocol withholds.**
>
> **So the anti-convergence gate and the anti-contamination rule are in direct conflict, and one must lose.**
> **A cold run cannot run Gate 6 at the time Gate 6 is meant to run.**

**What was run instead — `04` Part III.4's four substitutes, all of them:**

1. **Its own earlier states** — ✓ Phase 5b, the three-era set. **Produced a sharper result than a sibling set
   would have** (see the note there).
2. **Nearest analogous location at another scale** — ✓ Casey, at Gate 4.
3. **Real-world comparables with divergence stated** — ✓ three picks plus two comparanda, divergences in §3.4.
4. **The generator-conflict method** — ✓ Phase 1C, four generators, conflict resolved both-are-true.

**VERDICT: DEFERRED to Step 7, where the withheld files are opened. This is the correct sequencing and it means
Gate 6 runs late rather than not at all.**

---

## Gate 7 — Research accounting

**Run in full at `02_Research_and_Phases_2-10.md` §3.5.** **6 of 8 sources changed a finding = 75%**, inside
Gate 7's expected 70–80% band. **One withheld with its purpose recorded** (Vilnius's hidden courtyards, held for
an interior pass); **one honestly omitted** (Yekaterinburg's 1723 industrial founding). **Not 100%**, which
Gate 7 says to be suspicious of.

**VERDICT: PASS.**

---

## Gate 8 — Standout recorded

> **The single strongest thing this pass produced: Finding I — *Zhongshan was not founded; it was joined.***

**Why it, and not The Round** *(which is more usable)*: Finding I is the only finding that **reconciles two
ranks of canon against each other** *(rank-1 `No_National_Stereotypes.md` vs rank-2 `Specs/Zhongshan.md`)*,
it comes from **reading a binding cross-project rule literally rather than from invention**, and it **produces
a second finding downstream** — XIV, the arrival-order axis — that is genuinely emergent and that no other
Tepenian city can have.

*(Per `00f` §8 the panel may change this; if it does, the change is recorded rather than the original erased.)*

---

## Gate 9 — Asymmetry *(runs twice — inherited, then this pass's own)*

**Pass 1, on inherited material.** Limited by design: the inherited *conclusions* are quarantined. Run against
what was admissible — the founding mechanism. **The Jeju-do court confirmed Zhongshan's claim. What happened to
a party it decided against?** Canon says neither Japan nor Korea pressed a competing claim, so **no party was
decided against.** **A genuine negative result, and it is characterizing:** Zhongshan's founding contains no
loser.

**Pass 2, on this pass's own thresholds — and `04` warns that a pass reporting only inherited fires has
probably not run this half.**

| This pass's threshold | Both directions written? |
|---|---|
| Ph 7c — *learn the trade nearest you* | ✓ **Yes** — the against-direction is written: those who cannot must physically move, which in a city with four cheap exits often means leaving |
| Ph 5d — **membership: you are local once a leg is yours** | ⚠ **NO** |

> ### ⚠ GATE 9 FIRES ON THIS PASS'S OWN MATERIAL
>
> **The membership mechanism was written entirely from the favorable side** — how someone becomes a local.
> **The question `04` Gate 9 forces: what happens to someone the mechanism decides against, is that outcome as
> durable, and is there a route back?**
>
> **Answer, and it is a textbook shadow.** Legs are not granted; they are *picked up*. So a person becomes local
> by being **near a lapse at the right moment**. Someone who never happens to be — because their part of the
> city is well-covered, because they arrived when nothing had lapsed — **is never handed anything, has no way to
> ask, and there is no route in.** **Nobody excludes them. There is simply no application.**
>
> **`00d`-compliant on all three tests:** unintended · unnoticed in-world · discoverable rather than announced.
> **And it works with everyone acting in good faith**, which is the non-malice discipline's requirement.
>
> **This is the pass's second-strongest finding and it exists only because Gate 9's second pass was run.**
> **Written up as Finding XV** in the corrections file.

**VERDICT: FIRED, productively. One new finding.**

---

## Gate 10 — The Review Panel

**Run separately: `05_Review_Panel.md`.**

---

## Gate 11 — Plausibility *(the weakest gate, and it is reported as such)*

**The scale question, run first because `00b` calls it three of the seven recorded developer catches in one
sentence: *what population, over what span, does my source actually describe — and am I asserting it of a
larger one?***

```
Census II population      : 996,684
Larsemann Hills ice-free  : 40.0 km^2   (researched figure)
=> density                : 24,917 people per km^2
   comparison             : Manila ~46,000 · Manhattan ~28,000 · Paris ~20,000
people per lake           : 6,645
```

> ### ⚠⚠ GATE 11 FIRES — AND IT IS THE FIRST TIME THIS GATE HAS EVER CAUGHT ANYTHING IN THIS PROJECT
>
> `04` Part IV records: *"The gates have never caught a plausibility failure, and the developer has caught
> seven."* **This one caught its own.**
>
> **Two source-scale violations, both mine:**
>
> 1. **The forcing-function comparanda are parish-scale and shrine-scale.** Beating the bounds serves a parish
>    — hundreds of people. Ise Jingū is one shrine. **The pass asserted the same structure of a city of
>    996,684.** A single walked circuit cannot serve a million people, and the pass wrote *"someone walks it"*
>    and *"the walk takes days"* as though one person did.
> 2. **The whole texture was written as a scattered lakeside settlement.** At **24,917 people per km²**
>    Zhongshan is denser than Paris. **The lakes are not out in a landscape people stroll to. They are inside a
>    dense city, hemmed by it.**
>
> **Both corrected.** The Round becomes **a distributed rota of several hundred walkers holding subdivided
> legs** — the parish model scaled the way parishes actually scale, by multiplying, not by lengthening the
> walk. And Phase 3's texture is rewritten dense. **The finding survives; it was the scale that was wrong.**
>
> **The correction improves it.** A lake with 6,645 people living around it is a *public square that happens to
> be water*, which is more playable than a remote pond.

**Other Gate 11 checks:** *would a person actually do this* — yes, once distributed · *at this cost, priced in
this location's conditions* — yes; mild climate, ice-free rock, short distances · *for this reason* — yes, the
water genuinely varies and genuinely must be checked · *whose behavior am I describing* — **now correctly the
general population, after the Gate 2 fix.**

**VERDICT: FAILED on scale, twice. Corrected. Gate 11 is no longer a gate that has never caught anything.**

---

## Gate C — Canon check, federated

**Universe repo opened deliberately?** ✓ **Yes** — and it produced the pass's standout finding.
**Files actually opened, named as the gate requires:**

| Tier | Files opened |
|---|---|
| **Universe repo** | `Reference/Repo_Scope.md` · `Reference/No_National_Stereotypes.md` · `Reference/World_History_Reference.md` · `Timeline Eras/1 The First Interwar Period/Timeline.md` · `Reference/Falkland_Treaty/{Scaffold,Draft_v1,Real_World_Influences}.md` · `Worldspace/Locations/README.md` · `Reference/Amundsen_Station_Archive_and_Trucking_Network.md` |
| **Project** | `Specs/Zhongshan.md` · `Specs/Sinheung.md` (climate only) · `Official_Population_Census.md` · `City_Symbolic_Substrate/{Planetary_Symbols,Robot_Elementals,City_Symbol_Assignments}.md` · `Infrastructure/{Highways,Airports}.md` · `Inspirational-Influences.md` · all 35 `Specs/*.md` (composition parse only) |
| **Deliberately NOT opened** | every conclusions file on the quarantine list |

- **Checked against the source, not the last pass that cited it?** ✓ — and **M-3 records a case where a project
  file's claim had been migrated upstream and was wrong.**
- **Thin-file redirect check?** ✓ N/A — no thin file was mistaken for thin canon.
- **Rank order respected where sources disagreed?** ✓ **Finding I states the rank-1/rank-2 contradiction and its
  reconciliation in the text**, rather than silently picking a side.
- **Anything binding beyond this location routed to RESERVED?** ✓ — the Dålk glacier's cross-city effect; the
  mortuary mechanism; the "Alternative Culture" question.
- **Anything new named and cross-referenced?** ⚠ **Named yes, cross-referenced NOT YET** — Step 9 action.

**VERDICT: PASS, with one Step 9 obligation outstanding.**

---

## Gate F — Frame integrity

**1. Type.** Settlement; the Settlement phase set was answered. **Phase 5 is not shorter than Phase 8** *(the
predicted failure signature)*. ✓

**2. Band.** Band 4. ⚠ **Partial fire.** `01` §5.4 requires a Band 4+ pass to answer **patterned**, not
**uniform** — and *"a Band 4+ pass that answers everything as Uniform has not been written at its own scale."*
**The pass makes several uniform claims** — *"the universal item is footwear,"* one city-wide compact, one
observance. **Corrected**: the internal variation is written, and the pattern of variation named.
*(This is the same defect Gate 11 caught from the other side — both are scale errors.)*

**3. Status.** *Living, shrinking without declining.* **Reads correctly** — the pass never treats the 22.1% loss
as decline, and states explicitly that Zhongshan **rose** from 9th to 7th largest while losing it. ✓

**4. Temporal frame — post-frame leakage sweep, raw output:**

```
  'long night war' -> 3   (all three inside frame declarations, marked "has NOT happened")
  'post-war'       -> 0
  'ruin'           -> 0
  'destroyed'      -> 0
  'damaged'        -> 0
  '2812'           -> 2   (both in frame declarations)
  '2822'           -> 0
  'dlc'            -> 0
  'present day'    -> 0     'present-day' -> 0
```

**Zero leakage into claims.** Notable, because `Specs/Zhongshan.md` — the pass's own primary input — is written
**post-war** and repeatedly describes the city as *"damaged but partially operational."* **The pass took its
facts from a post-war document and stayed inside a pre-war frame.** ✓

**VERDICT: PASS on 1, 3, 4. Partial fire on Band. Corrected.**

---

## Gate I — Inheritance classification

**Every named institution walked and classed** *(`01` §5.1)*.

| Element | Class |
|---|---|
| The Round · The Turn · The Standing Objection · The Quarter of One Trade · the food-by-water axis · the compact · the directional speech marker | **Originated** → all go to Gate 6 |
| Climate · currency · calendar · robot legal personhood · the Falkland-Treaty order | **Determined** by the parent — and **the pass invented no local variant of any of them** *(the gate's first failure mode, avoided; climate uses real READER data)* |
| The hitchhiking norm on Hwy 4 and Hwy 110 | **Inflected** |
| The plurality-default decision habit | **Aggregated** *(a property of the composition, not a chosen institution)* |

> ### ⚠ GATE I FIRES — the Inflected class is under-used, exactly as `01` §5.1 predicts
>
> **`01` §5.1: *"The Inflected class is the workhorse and is systematically under-used,"* and a pass that skips
> it in favour of wholly-invented material *"is working harder for a worse result."***
>
> **This pass produced seven Originated elements and exactly one Inflected one.** That ratio is the diagnostic.
> **The specific miss: `National_Holidays.md` establishes Federation-wide observances, and the pass wrote a
> purely local observance (The Turn) without ever asking what Zhongshan does with a national one.**
>
> **Corrected** — an inflected observance is written in `04_Corrections_Applied.md`. **And the gate's prediction
> was accurate to the letter, which is worth recording: this is a gate with no prior track record correctly
> forecasting its own failure mode.**

**VERDICT: FIRED. Corrected.**

---

## Gate P — Parent reconciliation

**Correctly NOT APPLICABLE. `04` is explicit: Gate P *"runs on a parent's pass, not a child's."*** Zhongshan is
a child of the Mirny subnet and of the Federation, both unwritten.

**The reciprocal obligation was discharged in the other direction** — **four provisional assumptions are
registered** where the parent's eventual pass will see them (`01` §5.2 rule 5), **and assumption 4 is written
with its consequence attached**: *if the Mirny subnet does adjudicate between member cities, the deficit's
address moves from `diffuse` to `in the parent` and this is a substantially different city.*

**VERDICT: N/A, discharged from the child side.**

---

## Gate G — Generator honesty

| Check | Result |
|---|---|
| **≥3 generators, and independent?** | **4 run** — G2, G4, G5, G8. ⚠ **Independence declared honestly rather than claimed:** G2 and G5 are **partially correlated** (an ice-free deepwater site is *why* roads converge here), and G4 and G8 are **partially correlated** (the founding shapes the composition). **Neither pair is identical, and the correlation is stated rather than hidden.** G3 was **excluded specifically for non-independence** — function here restates G5 and G2, and would have been "one generator in three hats" |
| **Each run to a full profile before comparison?** | ✓ Yes — four separate four-quadrant profiles precede the comparison table |
| **Conflicts mined or smoothed?** | ✓ **Mined.** One real conflict — four different deficits from four generators — resolved both-are-true into a single property at four scales. **Not smoothed into agreement** |
| **Nulls recorded as nulls?** | ✓ **G6 recorded as a null with its reason** (pre-war frame). G3's exclusion recorded. Phase 5c's near-null recorded and classified |
| **Deficit researched AFTER the profile named it?** | ✓ Yes, and the ordering is stated at the head of Step 3 |
| **Unrecognized Instrument run AFTER the profile?** | ✓ **Yes — and it produced the pass's central finding.** ⚠ **But it was never labelled as such at the time**, which is a reporting failure rather than a procedural one. See below |

> ### The Unrecognized Instrument, recognized late
>
> **`02` §4.2: the location is already doing the thing it cannot do, somewhere, for an unrelated reason, and has
> never noticed the method generalizes.** **That is exactly what The Round is** — Zhongshan cannot detect lapse,
> and is detecting lapse, in one process, filed as water-quality monitoring.
>
> **The technique was run and the label was not applied.** Correcting the label matters because §4.2's payoff
> depends on it: *found first it softens the deficit; found second it sharpens it.* **Finding X — the city's
> refusal to extend The Round beyond the water — is the sharpening, and it only reads as such once the
> instrument is named.**
>
> **A second instance was then found by asking deliberately for one rather than stopping at the first:**
> **the Standing Objection's minute-books.** The city has no mechanism for recording what was decided; a parody
> body keeps scrupulous minutes; **the joke archive is the only decision record the city has**, and nobody has
> noticed it generalizes either.

> ### ⚠ And a generator was selected and then not used — caught by the translation sweep
>
> ```
>   'saturn' -> 1 hit   (inside the generator-selection table only)
>   'metal'  -> 1 hit   (same table)
>   'uranus' -> 0   'zodiac' -> 0   'planet' -> 0   'mystery' -> 0   'wu xing' -> 0
> ```
>
> **Translation discipline: PASS, absolutely** — the symbol vocabulary appears nowhere in any claim about the
> city. **But the same scan shows G1 contributed nothing at all.** It was declared "supporting" and then never
> cashed.
>
> **What it would have contributed, recorded now rather than pretended earlier:** this project's **Saturn** is
> *"beauty built from fragments rather than requiring wholeness"* and *"held together only loosely — a structure
> with no actual cohesion."* **That is an independent description of a 40 km² site made of ~130 islands and
> ~150 unconnected lakes, and of a city with no forcing function.** **`02` §5.2: all agree → build hard on it.**
>
> ⚠ **Tagged `[SELF-ORIGINATED]`** — the symbol assignment derives from the withheld Enneagram reads (M-1b), so
> **this is corroboration, not independent derivation**, and it is recorded as such rather than presented as a
> fourth agreeing generator.

**VERDICT: PASS on procedure. One labelling failure and one unused generator, both recorded.**

---

# Summary — what the instrument actually did

| Gate | Result |
|---|---|
| **0** | **Failed inward, twice** — both caught by a human, not by the gate |
| **1** | Pass; one under-explained null corrected |
| **2** | **FIRED** — Music written as performers' practice. Corrected |
| **3** | Pass after one genuine resolution |
| **4** | Pass; weakest finding identified and demoted |
| **5** | Pass; one cross-location consequence escalated to RESERVED |
| **6** | **UNRUNNABLE in the cold phase, by construction.** Substitutes run; deferred to Step 7 |
| **7** | Pass — 75%, in band |
| **8** | Standout recorded |
| **9** | **FIRED on this pass's own material** → produced Finding XV |
| **10** | Review Panel — separate document |
| **11** | **FIRED, twice, on scale.** First time this gate has caught anything in this project |
| **C** | Pass; one Step 9 obligation outstanding |
| **F** | Pass on type/status/frame; **partial fire on Band** |
| **I** | **FIRED** — Inflected under-used, exactly as predicted |
| **P** | N/A — correctly; discharged from the child side |
| **G** | Pass on procedure; one labelling failure, one unused generator |

**Five gates fired. Two of them — 9 and 11 — produced material the pass would not otherwise contain.**
**One gate (6) could not be run at all.** **One gate (0) failed in the direction it is specifically warned about
and was caught externally.**
