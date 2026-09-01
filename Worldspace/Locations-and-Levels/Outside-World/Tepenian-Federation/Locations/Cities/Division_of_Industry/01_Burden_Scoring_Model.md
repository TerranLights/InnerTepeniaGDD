# Burden Scoring Model — the instrument

**Built 2026-09-01.** Computes, for all 36 cities, how much of each necessary industry a city actually carries —
so that ~650 cells can be *derived* from already-canon attributes instead of judged 650 times.

> **⚠ INSTANCE, NOT METHOD** (`00_RUNBOOK.md` LAW C). The general procedure is
> `Canon_Gap_Resolution_Method/05_Bulk_Mode_for_Repeated_Shape_Gaps.md`. **Nothing here generalizes** — these
> drivers, weights and anchors are properties of the Tepenian city set.

**Sibling:** `00_Necessary_Industries_Register.md` (what the industries are).
**Research + anchors:** `../Research_Logs/Division_of_Industry_Research_Log.md`.

---

# 0. ⚠ PERIOD SCOPE — READ FIRST

> # Every figure in this model describes the **SECOND INTERWAR PERIOD** (2564–2812).
>
> **These are the cities as they were when the Tepenian Federation was an official, functioning country.** That
> is what §15 Division of Industry describes across the entire corpus, for every city, without exception.

**A `Specs` file's `Status:` line — `Destroyed`, `Damaged; partially operational`, `Survived` — is a
POST-Long-Night-War fact and has NO bearing on this model.** Cape Adare and Casey are both marked `Destroyed`;
both had full working economies of ~1.5 million people during the period this model computes. **Their
destruction is downstream of everything here and does not enter the calculation.**

> **⛔ There is no "war damage" driver, no reconstruction surge, and no post-war adjustment.** A first draft of
> this model included one. **It was wrong and has been removed.** Do not reintroduce it, and do not read a
> `Status:` line as an economic input.

*(Standing project default, not specific to this model: city and location culture work describes the Second
Interwar Period unless a file explicitly says otherwise. See
`../../../../../../../Reference/` timeline material and the interwar-period canon.)*

---

# 1. The core reframe — burden, not presence

**A presence test asks "does this city need healthcare?" The answer is yes, thirty-six times, and you have just
built thirty-six identical economies.**

**Necessary industries do not differentiate cities by their presence. They differentiate by their difficulty.**

Every city needs water. What differs is **what water costs *this* city.** At Vostok — −55 °C annual mean,
3,488 m, deep interior — water is a completely different industry from the one Cape Adare runs at sea level on
an open coast. Same necessity; different economy, different prestige structure, different way to die.

**So the model scores two things per (city, industry) pair, and multiplies them.**

---

# 2. The formula

```
Raw(C,I)  =  W(I)  ×  N(C,I)  ×  B(C,I)

BaselineLoad(C)  =  envelope-mapped sum of Raw(C, ·)          → the headline number
Share(C,I)       =  Raw(C,I) / ΣRaw(C, ·)  ×  BaselineLoad(C)  → the §15 sub-lines

Distinctive(C)   =  100 − BaselineLoad(C)                      → rescale existing §15 entries into this
```

- **W(I)** — the industry's base weight in a reference city. Relative and unitless; normalizes out.
- **N(C,I)** — **necessity**, 0→1. *Does this city need this at all?* Driven by **population composition**.
- **B(C,I)** — **burden**, ~0.7→2.0+. *What does meeting that need cost here?* Driven by **physical situation**.

**Designed to be runnable by hand.** If it needs a spreadsheet to be usable, it is too complex to be worth
having (bulk mode B4).

---

# 3. W — base weights

Relative weights in a reference city *(mid-pack, coastal, connected, mixed human/robot, intact)*. **Folded
industries are carried inside their parent's weight**, per the register's LINE/FOLD split.

| Industry | W | Carries (folded) |
|---|:--:|---|
| A1 Thermal & power | **20** | — |
| A4 Construction & structural maintenance | **16** | A5 emergency services |
| C3 Administration & records | **14** | — |
| A2 Water & sanitation | **12** | — |
| B1 Food production & distribution | **12** | — |
| B2 Human healthcare | **10** | C2 childcare/eldercare, C5 mortuary |
| B3 Robot maintenance & parts | **10** | B4 coolant/siligel, C5 decommissioning |
| C1 Education & training | **10** | — |
| D1 Transport & logistics | **10** | D3 retail/daily distribution |
| A3 Enclosure & atmosphere integrity | **8** | — |
| C4 Materials recovery & recycling | **8** | B5 textiles/survival gear |

**A1 is the largest single weight and that is deliberate** — heat is the survival precondition in this setting,
and the national currency was energy-backed. **C3's 14 is the research's correction**, not an intuition; see §5.

---

# 4. N — the necessity multiplier *(population composition)*

**Read from the Census. This is the axis that makes a robot-majority city unrecognizable rather than merely
different.**

| Industry | N is driven by | Notes |
|---|---|---|
| B2 human healthcare | **human share** | Kunlun / Dome Fuji: **N ≈ 0** |
| C1 education, C2 childcare | **human share × children present** | Outposts with no family formation: low |
| B1 food | **human share** | ⚠ **Robots do not eat hydroponics.** A 0-human city's food row nearly vanishes |
| B3 robot maintenance, B4 coolant/siligel | **robot share** | Kunlun: **N ≈ 1.0**, and it replaces B1's mass |
| B5 textiles/survival gear | **human share**, partial robot | Different garments, both populations |
| A1–A4, C3, C4, D1 | **≈1.0 universally** | Infrastructure serves whoever is inside it |

> **⭐ The single most important consequence.** Kunlun (0 humans / 123,449 robots) and Dome Fuji (0 / 55,072)
> do not get a *smaller* baseline load — they get a **structurally different** one. Human healthcare, schools,
> childcare and agriculture nearly disappear; robot maintenance and coolant/siligel production expand into the
> space. **Two robot-only cities and thirty-four mixed ones cannot converge, because the model literally cannot
> produce the same row set for them.** That is the variance guarantee doing real work.

---

# 5. B — the burden multipliers *(physical situation)*

**⚠ Every driver below is already canon for every city, in `Specs/` or the Census, before this run starts.**
That is bulk mode LAW E's binding requirement: *a driver you have to invent per-instance is the gap wearing a
disguise.* **Zero new research is needed to compute all 36 baselines.**

| Driver | Source (already exists) | Scale | Primarily multiplies |
|---|---|---|---|
| **Isolation** | `Specs` "Highway access" + subnet + maritime | **1.0** connected → **2.0** road-isolated | **everything** — an isolated city cannot import a service, it must staff it |
| **Cold severity** | `Specs` mean annual temperature | 1.0 @ −10 °C → **2.0** @ −55 °C | A1, A2, A4, B5 |
| **Wind regime** | `Specs` prevailing winds | 1.0 calm → **1.6** katabatic | A3, A4, A5 |
| **Altitude** | `Specs` Geographic Basis | 1.0 sea level → **1.5** >3,000 m | A1, A3, B2 |
| **Enclosure degree** | dome/sealed vs. surface | 1.0 → **1.4** | A3, A5 |
| **Coastal access** | `Specs` Geographic Basis | **0.7** coastal → **1.3** deep interior | B1, D1, C4 |
| **Polar night** | `Specs` polar night days | 1.0 → **1.3** | A1, B1, B2 *(indoor agriculture, mental health)* |
| **Building stock age** | `Specs` Founding date | shifts A4's **character**, not its size | A4 — growth vs. maintenance mix |
| **Population scale** | Census | **sub-linear** — mild economies of scale | C3, B2, C1 |
| **⭐ Labor externalization** | distance to nearest employing city + highway access | **0.0** work-where-you-live → **0.5+** half of resident hours worked elsewhere | **hollows the productive Distinctive tier — see §5.1** |

**Isolation is the highest-variance driver and should be weighted as such.** It alone explains most of the
spread, and it is the axis on which Tepenia's cities genuinely differ most.

## Calibration anchors — real, and written down so the numbers mean something

| Anchor | Figure | What it fixes |
|---|---|---|
| **McMurdo Station** *(closest physical analog)* | **~656 support of 995 total ≈ 66% support / 34% mission** | **The envelope's upper-middle.** An Antarctic research settlement spends **two-thirds** of its labor simply continuing to exist |
| **Nunavut / Iqaluit** | **60% public sector** (35% private, 5% self-employed) | C3's weight of 14 — remote settlements are administration-heavy |
| **Svalbard / Longyearbyen** | **~50% public** vs. 35% mainland Norway | Confirms the above independently, in a *civilian town* rather than a station |
| **Svalbard healthcare** | **<2%** vs. mainland 4% | **⚠ INVERTED for Tepenia** — see register §A. Mechanism transfers, magnitude reverses |

## 5.1 Labor externalization — added 2026-09-01, and it does something none of the others do

**Every other driver scales a cost. This one relocates an entire economy.**

Where residents earn their living in another city, that labor appears in **that** city's division of industry,
never in this one's. **The effect is asymmetric and that is the whole point:**

- **Baseline civic load is barely reduced.** The city still heats itself, melts its water, maintains its
  structures and runs its school for children **who do not rotate.**
- **The productive half of the Distinctive tier is hollowed out**, because the production happens elsewhere.
- **What remains is discretionary** — and discretionary labor, given repatriated income and large repeating
  blocks of idle time, **professionalizes into strange micro-industries.**

**So this driver is what licenses a high aggregate LAW G share** (`05_Bulk_Mode` §LAW G, "the aggregate is
uncapped but must be earned"). **Weirdness is not chosen here; it is what is left over.**

| City | Externalization | Why |
|---|---|---|
| **Scott** | moderate | Adjacent to Fort McMurdo, shares a municipal border — **daily commute**, residents sleep at home |
| **`{{Abowasa}}`** | **high** | Halley and Neumayer both far in either direction — **forces multi-day rotation**, 1–3 weeks away, 1–2 weeks home |

> **⭐ Already visible in the corpus, un-noticed.** The sweep's matrix records `{{Abowasa}}` as
> **`Health . · Constr . · Food . · Educ Y · Admin . · Utils .`** — **five of six absent, and the one present
> is the school.** That is exactly the predicted signature of a rotational-residence city, sitting in canon
> before anyone proposed the mechanism. **Children do not rotate**, so education's share of *in-city* labor is
> structurally inflated while every productive sector thins out.

### ⚠ The undefined term this exposes

**§15 has never specified whether it measures labor performed *in* a city or labor performed *by its
residents*.** For 35 of 36 cities those are the same number, so nothing ever forced the question. **At a
rotational city they diverge by roughly half.**

**Resolution used here — an externalization header line, so cross-city comparability survives:** baseline and
distinctive still sum to 100% *of in-city labor* at every city, and externalization is stated separately as an
additional characterizing fact rather than folded into the denominator. **Routed to the ruling queue as a
format decision, not settled by this model.**

## The predicted envelope

> ### **BaselineLoad ranges ~40% → ~75%.**
> **~40–45%** — mild, coastal, connected, mature, intact. *(Cape Adare, Esperanza, Port Lockroy.)*
> **~55–65%** — the fat middle where most of the 36 live.
> **~70–75%** — extreme, isolated, high-altitude, sealed. *(Vostok, Kunlun, Dome Fuji.)*

**That single number is itself the differentiator.** "Vostok 73% / Cape Adare 42%" tells a reader everything
about both cities before reading a word of prose — **the cost of existing there, stated as a number.**

---

# 6. Worked example — Vostok, and why this fixes the sweep's §3 for free

**Vostok's drivers:** isolation ~1.9 · cold 2.0 (−55 °C, the harshest in the corpus) · altitude 1.5 (3,488 m) ·
interior 1.3 · enclosure 1.4 · polar night 1.3 · wind ~1.1 *(plateau interior, not katabatic-coastal)*.
**Near the ceiling on nearly every axis. BaselineLoad ≈ 72–75%.**

| | Current §15 | **Modeled** |
|---|---|---|
| Science (Lake Vostok program) | **65%** | **~22–25%** |
| Self-sufficiency / survival | 25% *(un-itemized)* | **→ becomes the 72–75% baseline, itemized** |
| Other | 10% | folded |

**Sanity check against the anchor:** McMurdo — coastal, sea level, −17 °C — really runs ~34% mission. **Vostok
is far harsher than McMurdo on every axis.** A *lower* mission share than McMurdo's is therefore exactly the
expected result, not a diminishment.

> ## ⭐ This dissolves the sweep's §3 without a separate pass.
>
> The sweep flagged four "purpose-dominant" cities (Vostok 65% science, Kunlun 60% astronomy, Dome Fuji 75% in
> two sectors, Scott) as *"plausible, but leaves almost nothing for ordinary life,"* and treated it as a
> distinct problem from §4's missing sectors. **They are the same problem.** Vostok cannot be 65% science
> *precisely because* an isolated −55 °C plateau outpost spends three-quarters of its labor on continuing to
> exist. **The missing necessary sectors are exactly what the thematic sectors crowded out.** Compute burden
> honestly and §3 resolves itself.
>
> **And Vostok's identity survives intact**: at ~24% science is still, overwhelmingly, its dominant distinctive
> sector. **It stops being the whole city and becomes the point of it.**

**Vostok's §15 already contains the seed of all of this** — `Self-sufficiency / survival infrastructure: 25%`.
**One city already invented this concept; the model generalizes and itemizes it.** This is derivation from
existing canon, not imposition on it.

---

# 7. Output format — the two-tier §15 *(developer ruling, 2026-09-01)*

```markdown
## 15. Division of Industry

**Baseline civic load: 73%** — what Vostok spends simply remaining habitable
 - Thermal & power: 19%
 - Water & sanitation (ice-melt, closed-loop): 11%
 - Enclosure & atmosphere integrity: 9%
 - Construction & structural maintenance: 12%
 - Food (closed-loop hydroponics): 7%
 - Human healthcare + robot maintenance: 8%
 - Administration & records: 4%
 - Materials recovery: 3%

**Distinctive economy: 27%**
 - Science (Lake Vostok research program): 24%
 - ⟨LAW G slot⟩: 3%
```

**The existing §15 entries are rescaled into the Distinctive tier, preserving their ratios to one another.** A
city's established identity is not rewritten — it is given an honest denominator.

---

# 8. Process — and the guards that are not optional

**Work industry-major, not city-major.** One industry across all 36, then the next.

> **Why, and this is the opposite of the obvious approach:** holding *water and waste* in mind while looking at
> 36 variants is where differentiation actually comes from — **you can see the sameness and push against it in
> the moment.** City-by-city means re-deriving "what is healthcare" 36 times and never noticing that city 31's
> answer duplicates city 4's.

**Mandatory guards** *(bulk mode B6/B7)*:

- **`02_Cross_City_Industry_Differentiation_Table.md`** — one row per industry **plus a dedicated LAW G row**,
  one column per city, holding **the local form in one phrase, not the number**. **Two cells that read the same
  mean at least one is wrong.** Filled in the **same commit** that completes a row, per the district rule.
- **Every derived value is conclusion-tier** and carries a `[CGRM 2026-09-01 · Path 2 · burden model]` marker
  wherever it lands. **Bulk volume is exactly why** — an unmarked bulk deposit is the Cape Adare contamination
  chain multiplied by 36.
- **Quarantine check before touching any city with a pending cold ULM run**, and **no graphify on Path 3
  subjects** (`00_RUNBOOK.md` tooling note).

## The pilot, and its falsification test — declared in advance

**Four cities, not 36:**

| City | Stresses |
|---|---|
| **Vostok** | the burden ceiling |
| **Kunlun** | the necessity function — 0 humans should produce a structurally different row set, not a smaller one |
| **Cape Adare** *(or Esperanza)* | the burden floor; already best-covered at 2/6 |
| **Casey** *(or Neumayer)* | **the ordinary middle — not optional** |

**The fourth is mandatory and LAW C is why:** this project has already shipped *"a methodology validated on the
least representative configuration in the project."* An instrument tuned only on extremes will be confidently
wrong across the fat middle where 30 of the 36 actually live.

> ## ⛔ FALSIFICATION TEST — declared before running, per bulk mode B7
>
> **If the four pilot §15s come out looking alike — similar baseline loads, similar row sets, interchangeable
> local forms — the instrument is broken and the run STOPS.** It is not tuned and re-run to a nicer answer.
>
> **Expected spread if it is working: ≥25 percentage points between the highest and lowest BaselineLoad, and
> Kunlun's row *set* visibly different from the other three's rather than merely smaller.**

---

# 9. Honest status

**Unexercised.** No city has been run through this. The weights in §3 are reasoned from the register and
anchored in §5's research, **but not one of them has been checked against a real city's data.** The Vostok
figures in §6 are a hand-worked illustration of the method, **not a proposed edit to Vostok's file.**

**Nothing in this model may be deposited into any city file until the pilot has passed its own falsification
test.**
