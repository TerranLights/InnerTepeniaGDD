# Per-City Three-Tier Run — THE CALCULATION SHEET

> **Opened 2026-09-02. Results not yet computed — this file currently holds the INPUT
> REGISTER and the procedure.**
>
> **Supersedes `09_Per_City_Baseline_Run.md`**, which ran the old two-tier model on the
> old (circular) B1 rate.

---

---

# ⭐ SOURCE REGISTER — everything needed to run this, and nothing else

> **⭐ Every path below was resolved and verified on disk, 2026-09-02 — 18 of 18.**

**All paths are relative to THIS FOLDER** — `Worldspace/Locations-and-Levels/
Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/` — **except
`/CLAUDE.md`, which is the repository root.**

## 1. POPULATION AND WORKFORCE — the inputs everything else multiplies

| File | Supplies | Status |
|---|---|---|
| `../Official_Population_Census.md` | **Census I per-city humans / robots / residents.** The 38-city roster | ✅ canon |
| `./06_Census_Basis_Correction.md` | **Why Census I and not Census II** — cities must house their PEAK; "build for peak, then depopulate" | ✅ ruled |
| `./09_Per_City_Baseline_Run.md` §5 | **The workforce formula: `robots + 0.5 × humans`.** A headcount of workers, NOT hours | ✅ resolved |
| `./09_Per_City_Baseline_Run.md` §2 | **The per-city D (difficulty) column** — the only place the 38 assignments are tabulated | ⚠ **table still valid; its `Required` column is SUPERSEDED** |

> **⚠ `09` is superseded as a RESULT and still needed as an INPUT.** Take its
> population, workforce and **D** columns; **discard its `Required` and `% WF` columns**,
> which used the circular B1 rate.

## 2. RATES — the per-1,000 coefficients

| File | Supplies | Status |
|---|---|---|
| `./00_Necessary_Industries_Register.md` | **The 22 necessary industries**, and the human/resident/robot **keying** of each | ✅ canon |
| `./08_Volume_Based_Requirement_Reference.md` §5.1 | **The rate table** — all human-keyed and resident-keyed rates | ✅ **except B1** |
| `./08_...` §8 | **C3 Administration = 65 per 1,000 residents** *(sourced; supersedes the 45 in §5.1's first run)* | ✅ sourced |
| `./08_...` §9 | **Robot-keyed rates** — B3 maintenance 12.5/1,000 robots · B4 sustenance 3.25/1,000 robots · C5-robot **not a standing industry** | ✅ ruled |
| **`./11_Caloric_Rebuild_and_Livestock_Tier.md`** | **⭐ B1 FOOD = 120.7 per 1,000 humans.** **THIS REPLACES the 53 in `08` §5.1** | ✅ **use this** |
| `./08_...` §4.2 | The source register for all 18 original rates *(NFPA, WHO, UNESCO, FAO, OECD, IFMA, EPA, EEA, World Bank, BLS)* | ✅ reference |

> **⛔ C6, C7, C8 and D4 rates are ESTIMATED, not sourced** *(`README` chore 3)*. **Carry
> the uncertainty; do not present them as sourced.**

## 3. DIFFICULTY — and where it does and does not apply

| File | Supplies |
|---|---|
| `./08_...` §6.4b | **The MCAA Labor Productivity Factor table** — weather 10/20/30, logistics 10/25/50, site access 5/12/30, applied **additively**; `multiplier = 1/(1−L)`, capped at 60% |
| `./08_...` §6.1, §6.4 | The three sourced anchors — MCAA, Iqaluit, Halley VI — and the autonomy-duration figures |
| `./08_...` §7.1 | **⭐ SELECTIVE APPLICATION — which industries each factor actually touches.** A factor applied to everything cancels out of composition; this is what makes difficulty *differentiate* rather than merely scale |
| `../Specs/*.md` | Per-city climate blocks *(BAS READER normals)*, elevation, and distance-inland — the physical basis behind each D |

## 4. THE FOOD LAYER — rebuilt, and the largest single change

| File | Supplies | |
|---|---|---|
| **`./10_Validation_Findings_2026-09-01.md`** | **⛔ READ FIRST.** What three independent checkers found; which figures are invalid and why | **required** |
| **`./11_Caloric_Rebuild_and_Livestock_Tier.md`** | **B1 = 120.7/1,000** · the marine-employment finding · the livestock tier · **the fibrous-residue stream (769,849 t/yr)** | **required** |
| `./12_Terraforming_and_the_Outdoor_Tier.md` | **The terraformed belt, RULED at 1,500 km²** across Peninsula / East Antarctic oases / Bunger Hills; the passive-vs-active split | ✅ ruled |
| **`./13_National_Balance_Under_the_Ruling.md`** | **⭐ §12 — no Tepenian crop uses daylight** · **§14 — the three-tier GEOLOGY** · **§15 — all 37 cities classified, and which seven are forced importers** | **required** |
| `./14_Completing_the_Food_Basis.md` | The five-tier basis · **phosphorus as the one unmanufacturable input** · the Upper Earth trade resolution | ✅ |
| **`./15_Open_Items_and_Three_Resolutions.md`** | **⭐⭐ RESOLUTION 4 — THE THREE-TIER SPLIT ITSELF**, which is what this sheet computes. Also fungi sizing, Cape Adare, seed vaults | **required** |

> ## ⛔ **`./01`, `./03`, `./07` are SUPERSEDED** *(the share-first model and its failed
> validation)*. **Kept as the record of why the method changed. DO NOT USE THEIR
> FIGURES.**

## 5. THE MANDATED TIER — national provider roles

| File | Supplies |
|---|---|
| **`./04_Providers_and_National_Balance.md`** §3 | **⭐ THE 22 PROVIDER CITIES with their §15 sector percentages** — the primary input for the mandated tier |
| `./04_...` §4, §6, §7 | The national balance working, the krill/geography research, and the open marine-fraction question |
| `./05_Remaining_Cities_Assessment.md` | The non-provider cities; the Halley-subnet gap and the **commuter-labor mechanism** (5–10% scenarios) |
| `../Specs/*.md` **§15** | **⭐ The canon economic-composition block for each of the 38 cities.** The authority for any sector percentage |
| `./15_...` Resolution 4 | **The mandated/discretionary TEST** — would the nation suffer materially without it? — and the three rulings for Halley, Neumayer and Vostok |

> **⚠ Thirteen cities have NO recorded national role**, because `04` §3 set 22 providers
> aside and left *"15 cities remain to be needs-assessed."* **Assessing them is HALF A of
> this pass** *(`15` §"The Per-City Pass")*, not a missing input.

## 6. OBLIGATIONS AND CAUTIONS — non-optional

| File | Obligation |
|---|---|
| **`/CLAUDE.md`** | **⛔ A city's column in the differentiation table must be filled IN THE SAME COMMIT that completes a category for it.** Also **LAW 0 — depth over speed** |
| **`./02_Cross_City_Industry_Differentiation_Table.md`** | **⛔ STILL EMPTY.** The only mechanical guard against 38 cities converging |
| `../../../../../../Canon_Gap_Resolution_Method/05_Bulk_Mode_for_Repeated_Shape_Gaps.md` | **The method half** — LAWS D–G, the B1–B8 procedure, and **B7a, the two-agent validation protocol** |
| `../../../../../../Canon_Gap_Resolution_Method/Developer_Ruling_Queue.md` | **Open rulings.** ⚠ **DRQ-09 is only PARTLY resolved; DRQ-10 (livestock species/siting) is open** |
| `../Research_Logs/Division_of_Industry_Research_Log.md` | **Per-location research log** — exact search strings and open threads. **Every research pass appends here** |
| `./README.md` | Reading order, the **food-layer carve-out**, and the four standing chores |

## 7. DEPOSIT TARGETS — where results go

| | |
|---|---|
| `../Specs/*.md` §15 | Where the final per-city composition is deposited *(38 files)* |
| `../Local_Cultures/**` | Downstream consumer of the **free tier** |
| **Provenance tag** | `[CGRM <date> · Path 2 · three-tier division-of-industry model]` |

---

---

# ⚠ FOUR THINGS THAT MUST NOT BE RE-DERIVED WRONG

1. **B1 is 120.7 per 1,000 humans, not 53.** The 53 was circular — a supply figure
   inverted into a demand rate *(`10` Finding 1)*.
2. **The food term is 10% of B1 for the seven geologically-forced importers** — Halley,
   Neumayer, Vostok, Byrd, Amundsen Station, Kunlun, Dome Fuji — **and 100% for everyone
   else** *(`13` §15)*.
3. **Kunlun and Dome Fuji have ZERO humans.** Their food term is zero, not small.
4. **⚠ VERIFY UNITS.** Four 1,000×/digit errors occurred and were self-caught in this
   work. **Assert unit conversions before trusting any power or tonnage figure.**

---

# The formula this sheet computes, per city

```
workforce          = robots + 0.5 × humans

baseline           = humans   × (120.7·f·D + 85.6)/1000
                   + residents × (64·D + 113.2)/1000
                     where f = 0.10 for the seven forced importers, else 1.00

distinctive        = workforce − baseline
mandated           = distinctive × Σ(national provider sector shares)
FREE               = distinctive − mandated          ← the character budget
```

**National reference values already computed** *(`15` Resolution 4)*: **baseline 42.0% ·
mandated 11.5% · free 46.5%**, with the free tier running **23.4% (Fort McMurdo) to
72.7% (Dome Fuji)**.

---

# ▶ Results

**Not yet run.** Half A *(assess the thirteen)* precedes Half B *(the 37-city table)* —
see `15_Open_Items_and_Three_Resolutions.md` §"The Per-City Pass".

---

---

# ▶ HALF A — THE THIRTEEN ASSESSED — 2026-09-02

**Every §15 economy block read. The test applied throughout: *would the nation suffer
materially without it?*** **Derived from canon where canon supports it; flagged where it
does not.**

## ✅ Group 1 — canon already names a national role; it only lacked a percentage

| City | Humans | **Mandated role** | Canon basis |
|---|--:|---|---|
| **Princess Elisabeth** | 553,768 | **⭐⭐ ENERGY ENGINEERING** | §15: *"genuine expertise in Antarctic energy systems **that other cities traded for**"* — **an export stated outright.** `04` §3 already listed the role with no figure |
| **Zhongshan** | 631,985 | ~~MARITIME LOGISTICS — the Tri-Cities' port~~ **→ WITHDRAWN 2026-09-02. See §18** | **⚠ This row misquoted §15.** *"Prydz Bay maritime logistics… cluster economy with Sinheung"* **appears nowhere in Zhongshan's §15**, which says *"Prydz Bay **fishing**"* and *"Zhongshan is **not a trade hub**."* The *"cluster economy"* phrase is **Sinheung's** annotation. **Replaced by a technical/scientific mandate — see the determination** |
| **Cape Adare** | 745,967 | **ROSS SEA GATEWAY + ⭐ PHOSPHATE EXTRACTION** | §15 *"Ross Sea gateway — maritime trade, the logistics of arrival and departure"*; phosphate per `15` Resolution 2 |
| **Sejong** | 316,691 | **INTERNATIONAL GATEWAY** | §15: *"the most accessible part of Antarctica, closest to South America… a trade and transit hub."* **Machu Picchu Airport — the nation's international arrival point — is beside it** |
| **Denison** | 522,975 | **STRUCTURAL / WIND ENGINEERING** | §15: *"Denison's defining economic sector — an unusually large share."* ⚠ Its canon `~25%` is an **old-convention** figure *(`README`)* |
| **Scott** | 189,817 | **VOLCANIC MATERIAL EXTRACTION** *(small, specific)* | §15, confirmed 2026-07-07: Erebus material trucked across McMurdo Sound and forwarded into the Janbogo subnet **for further processing** |
| **Concordia** | 504,799 | **THE NATIONAL CROSSROADS** — transit/transshipment | §15 *"inter-district trade and external supply"*; **the only genuine tri-junction in the country** (Hwy 110 × 37 × 183), plus Capricorn's industrial yards |

## ✅ Group 2 — a national role the food model itself supplies

| City | Humans | **Mandated role** | Basis |
|---|--:|---|---|
| **{{Abowasa}}** | 504,237 | **COMMUTER LABOR** + minor research | §15 calls it *"small scale… never a major economic node"* — **but `05`'s commuter mechanism is explicitly "5–10% of Halley + {{Abowasa}} workforce."** **The same answer just ruled for Halley applies here, and canon named {{Abowasa}} in the same breath** |
| **Dome Fuji** | **0** | **⭐ THE NATIONAL SEED ARCHIVE** + ice-core science | `15` Resolution 3. §15: *"one of the best locations on Earth for deep ice core drilling"* — **a city already built around keeping things frozen for hundreds of thousands of years** |

## ⏸️ Group 3 — "nothing national" is the honest answer, and that is a RESULT

**The pass plan explicitly allows this: *a city that is purely itself is a valid and
interesting result, not a failure.***

| City | Humans | Assessment |
|---|--:|---|
| **Dumont d'Urville** | 223,549 | §15: *"the city was small, and its economic significance was **more cultural and historical than industrial**."* **Minor coastal logistics on the Australia corridor; no national mandate.** ⭐ Canon says this plainly — take it at its word |
| **Port Lockroy** | 63,338 | Fourth-smallest city. §15: sheltered harbour + heritage. **⚠ One thread: its post office was *"a genuine, active civic courier institution"*** — a **national courier node** is a small but real mandate. Otherwise: itself |
| **Kunlun** | **0** | §15: *"astronomy, ice core science… the observatory program was Kunlun's primary scientific output."* **⭐ Dome A is the best astronomical site on Earth** — but astronomy is not something the nation would *starve* without. **Discretionary, and its 71.4% free tier is genuine.** ⚠ Its engineering capacity turned Neumayer's Calethina design into a buildable schematic — capability that could be mandated if the developer wants it to be |

## 🔴 Group 4 — LAZAR. The one genuine open question, and canon says so itself

**Lazar is the LARGEST city in the Federation — 1,287,003 humans, 2,620,319 residents —
and its economy is explicitly unresolved in its own spec:**

> *"The city visibly supports genuine megacity-scale commercial density — holographic
> advertisements and multicolored lights throughout — but **what's actually driving an
> economy large enough to justify that presence is explicitly unresolved and flagged as
> needing real development, not just a placeholder gap**."* *(Developer vision session,
> 2026-07-05.)*

**⭐ What this pass can now contribute — three candidates it could not have offered before:**

1. **⭐⭐ WATER.** Lazar sits on **100–180 freshwater lakes** *(Schirmacher Oasis)*. **Every
   other city in Tepenia makes water by melting ice at 128 kWh/tonne** *(`15` List B item
   8)*. **Lazar is the only city in the country that does not pay the melt tax** — and
   water is an input to everything.
2. **⭐ DEEP EXCAVATION.** The developer ruled Lazar builds **upward, outward and downward**
   through Precambrian gneiss. **Every rock-founded city — 29 of 37 — needs that
   capability, and Lazar would have the most of it.**
3. **AVIATION / DROMLAN.** §15 already flags *"Novolazarevskaya's real logistics-hub role
   (part of the real-world DROMLAN air network)."* ⚠ **But Belgrano is already the Halley
   subnet's primary airbase and Troll holds the contested airfield — so this one risks
   convergence.**

> ## ⚠ **NOT RULED. Lazar's economy is a standing developer item, and inventing it inside
> a calculation pass would be exactly the vacuum-filling the anti-convergence rule
> exists to prevent.** **The three candidates above are offered as inputs to that
> decision, not as an answer.**

---

## ⭐ A pattern the thirteen revealed, worth naming

**Six of the thirteen name SCIENTIFIC RESEARCH as an economic activity** — {{Abowasa}},
Princess Elisabeth, Zhongshan, Scott, Kunlun, Dome Fuji — **and Neumayer and Vostok were
just ruled research exporters on the same day.**

> ## **Tepenia has a distributed RESEARCH SECTOR, spread across its small and remote
> cities rather than concentrated in a capital. That is not a coincidence: this is a
> nation assembled out of inherited research stations, and the stations kept doing what
> they were built to do.**

**⚠ Which raises a question for the mandated/discretionary test, and it is a real one:**
**most research is not something a nation dies without in one year — but Neumayer's
growing research is worth 80× the national food power bill, and Vostok's bioinformatics
underpins the Cryptograph Helix.** **Research is mandated when its subject is
load-bearing and discretionary when it is not, and that has to be judged per city rather
than as a class.**

---

---

# ▶ HALF B — THE 37-CITY RUN — 2026-09-02

> **`baseline / mandated / FREE`, sorted by free tier — least free first.**
> **`src`: `C` = canon % from `04` §3 · `D` = derived from the food debt · `H` = Half A
> estimate, MINE, needs ruling · `–` = no national mandate.**

| City | Subnet | D | Workforce | base% | MAND% | **FREE%** | src |
|---|---|--:|--:|--:|--:|--:|:--|
| **Amundsen Station** | Amundsen | 2.50 | 6,296 | 31.8% | **61.4%** | **6.8%** | C |
| **Fort McMurdo** | Janbogo | 1.25 | 334,215 | 41.5% | 35.1% | **23.4%** | C |
| **Marambio** | Palmer | 1.25 | 428,548 | 41.3% | 35.2% | **23.5%** | C |
| **Belgrano** | Halley | 1.43 | 805,928 | 44.3% | 30.7% | **25.1%** | C |
| **Sayowa** | Mawson | 1.43 | 178,698 | 39.3% | 33.4% | 27.3% | C |
| **Sanay** | Halley | 1.43 | 347,881 | 44.5% | 27.8% | 27.8% | C |
| **Byrd** | Byrd | 1.67 | 283,756 | 36.2% | 35.1% | 28.7% | C |
| **Janbogo** | Janbogo | 1.25 | 987,240 | 41.1% | 29.4% | 29.4% | C |
| Sinheung | Mirny | 1.25 | 809,754 | 40.7% | 26.7% | 32.6% | C |
| Denison | Janbogo | **2.00** | 804,656 | **53.2%** | 11.7% | 35.1% | C |
| Esperanza | Palmer | 1.11 | 1,400,618 | 39.7% | 24.1% | 36.2% | C |
| Rothera | Palmer | 1.15 | 240,569 | 39.0% | 24.4% | 36.6% | C |
| Davis | Mirny | 1.25 | 876,514 | 40.7% | 20.7% | 38.5% | C |
| Troll | Halley | 1.43 | 716,590 | 44.4% | 16.7% | 38.9% | C |
| Signy | Palmer | 1.25 | 142,127 | 41.1% | 17.7% | 41.2% | C |
| Princess Elisabeth | Halley | 1.43 | 861,033 | 43.7% | 14.1% | 42.3% | H |
| Juan Carlos | Palmer | 1.15 | 291,821 | 39.3% | 18.2% | 42.5% | C |
| Casey | Mirny | 1.11 | 1,128,834 | 38.7% | 18.4% | 42.9% | C |
| Zukelli | Janbogo | 1.25 | 944,859 | 41.4% | 14.6% | 43.9% | C |
| Cape Adare | Janbogo | 1.25 | 1,126,670 | 41.4% | 14.7% | 44.0% | C |
| **Concordia** | Janbogo | 1.67 | 763,548 | 48.3% | 7.8% | **44.0%** | H |
| Mawson | Mawson | 1.25 | 1,091,868 | 41.0% | 14.8% | 44.3% | C |
| Sejong | Palmer | 1.15 | 486,488 | 39.4% | 15.2% | 45.5% | H |
| Neumayer | Halley | 2.50 | 945,212 | 43.7% | 9.4% | 46.9% | D |
| Halley | Halley | 2.50 | 1,097,470 | 43.6% | 9.4% | 47.0% | D |
| Zhongshan | Mirny | 1.25 | 963,440 | 41.2% | 11.8% | 47.1% | H |
| Mirny | Mirny | 1.25 | 1,018,480 | 41.1% | 11.8% | 47.1% | C |
| Shirayuki | Mirny | 1.25 | 890,078 | 40.9% | 11.8% | 47.3% | C |
| {{Abowasa}} | Halley | 1.54 | 782,122 | 45.5% | 5.4% | 49.0% | H |
| Dumont d'Urville | Janbogo | 1.67 | 341,560 | 48.0% | **0.0%** | 52.0% | – |
| Scott | Janbogo | 1.25 | 291,102 | 41.0% | 2.9% | 56.0% | H |
| Port Lockroy | Palmer | 1.25 | 97,218 | 41.0% | 2.9% | 56.0% | H |
| Vostok | Mirny | 2.50 | 324,452 | 37.4% | 5.8% | 56.8% | D |
| Dome Fuji | Mawson | 2.50 | 55,072 | 27.3% | 14.5% | 58.1% | H |
| **Lazar** | Halley | 1.25 | **1,976,818** | 41.0% | **0.0% ⚠** | **59.0%** | – |
| Palmer City | Palmer | 1.11 | 249,852 | 39.1% | **0.0%** | 60.9% | – |
| **Kunlun** | Mirny | 2.70 | 123,449 | 28.6% | **0.0%** | **71.4%** | – |
| **NATIONAL** | | | **24,214,838** | **42.0%** | **15.2%** | **42.8%** | |

## What the run says

**⚠ The national free tier is 42.8%, not the 46.5% quoted before Half A** — because Half
A added mandates to ten more cities. **The character budget has now fallen twice: 59.4%
→ 46.5% → 42.8%.** *(`09` §3.5's original figure was effectively 62.5%.)*

### ⭐⭐ 1. The subnet ordering INVERTS `09` §3.5

| Subnet | Workforce | base | mand | **FREE** |
|---|--:|--:|--:|--:|
| **Halley** | 7,533,054 | 43.3% | 10.9% | **45.8%** |
| Mirny | 6,135,002 | 40.1% | 15.7% | 44.2% |
| Mawson | 1,325,638 | 40.2% | 17.3% | 42.6% |
| Janbogo | 5,593,850 | 44.4% | 15.6% | 40.0% |
| **Palmer** | 3,337,241 | 39.8% | **21.0%** | **39.1%** |
| Byrd | 283,756 | 36.2% | 35.1% | 28.7% |
| *Amundsen* | *6,296* | *31.8%* | *61.4%* | *6.8%* |

> ## **`09` §3.5 held that the Peninsula was *"simultaneously the easiest place to live
> AND where the food comes from,"* while *"the hardest-working cities have the least to
> show for it."***
>
> ## ⛔ **THE PALMER SUBNET NOW HAS THE LOWEST FREE TIER IN THE COUNTRY — 39.1% — and
> the HALLEY SUBNET THE HIGHEST at 45.8%.** **The resentment engine has reversed
> direction.**

**Why:** Palmer is dense with mandated roles — Esperanza *(food + the Institute)*,
Marambio *(60% logistics)*, Rothera *(40% industrial)*, Signy and Juan Carlos
*(fishing)*, Sejong *(the international gateway)*. **The Peninsula is the mildest place
in Tepenia and the most heavily committed.** *"Easiest to live"* and *"most spoken for"*
turn out to be the same fact seen from two sides.

**⚠ SENSITIVE TO LAZAR.** Lazar is 26% of the Halley subnet and carries a **0% mandate
only because it is unassessed.** **At a 20% mandate the Halley subnet falls to ~42.8%
and the inversion narrows to near-parity.** **Do not build a faction grievance on this
ordering until Lazar is ruled.**

### 2. The least-free cities are the useful ones — confirmed, and sharper

**Fort McMurdo 23.4% · Marambio 23.5% · Belgrano 25.1% · Sayowa 27.3% · Sanay 27.8% ·
Byrd 28.7% · Janbogo 29.4%.** **Every one is a port, an airfield or a factory.**

### 3. Range

**6.8% – 71.4%, a 64.6-point spread.** ⚠ **But three of those are special cases:**
Amundsen Station is *"not a city"* per `04`, and Kunlun and Dome Fuji have **zero
humans.** **Excluding all three, the real-city range is 23.4% (Fort McMurdo) to 60.9%
(Palmer City) — 37.5 points.**

### ⚠ 4. How much of this is canon and how much is mine

| Source | Workers mandated | Cities | Share of mandate |
|---|--:|--:|--:|
| **C — canon % from `04` §3** | **2,790,113** | 20 | **75.6%** |
| D — derived from the food debt | 210,218 | 3 | 5.7% |
| **H — MY Half A estimates** | **688,958** | 10 | **18.7%** |

**The ten H-flagged percentages, which are judgments and not canon:**

| City | My % | Role |
|---|--:|---|
| Denison · Princess Elisabeth · Cape Adare · Sejong | **25%** | wind engineering · energy engineering · Ross Sea gateway + phosphate · international gateway |
| ~~Zhongshan~~ · Dome Fuji | ~~20%~~ · 20% | ~~the Tri-Cities' port~~ **(withdrawn — see §18)** · seed archive + ice-core |
| Concordia | ~~15%~~ **⏸️ DEFERRED — estimate only, do not promote** | the national crossroads *(see the CONCORDIA — DEFERRED block)* |
| {{Abowasa}} | 10% | commuter labor |
| Scott · Port Lockroy | 5% | volcanic extraction · courier node |

> ### ⚠ **These move 688,958 workers — 2.8% of the national workforce. They are the
> single largest soft spot in the table and should be ruled before any city file is
> written from them.**

## ⏸️ Still open after Half B

- **Lazar's mandate** — 0%, and canon flags its economy as needing real development.
- **The ten H percentages above.**
- **Esperanza's education 25%** is counted as fully mandated; **part of it is local
  schooling, which is already in baseline C1a.** ⚠ **A double-count risk worth checking.**
- **`02_Cross_City_Industry_Differentiation_Table.md` is still empty** — and per
  `CLAUDE.md` it must be filled per city, in the same commit as that city's category work.

---

---

# ⚠ PROVENANCE CORRECTION, AND THE SEJONG / MARAMBIO SPLIT — 2026-09-02

## Correction: two of the "ten estimates" were never estimates

**`Denison — structural/wind engineering ~25%` and `Cape Adare — marine 25%` are CANON
§15 figures**, not judgments. `04` §3 states Cape Adare's *"25% explicitly includes
harbor operations and guano"*, and `05` §226–232 treats Denison's 25% as an existing
sector the instrument must be able to reproduce. **Mislabeled in the Half B write-up.**

| Source | Workers | Share of mandate |
|---|--:|--:|
| **Canon `04` §3 + the two reclassified** | **3,049,369** | **82.7%** |
| Derived from the food debt | 210,218 | 5.7% |
| **Genuinely my estimates — EIGHT cities** | **429,702** | **11.6%** *(1.8% of national workforce)* |

**Previously reported as 688,958 / 18.7% across ten cities — overstated.**

## ✅ THE SEJONG / MARAMBIO SPLIT — developer ruling, and it removes the convergence risk

> **Developer: *"Marambio's shipping connects with South America and the Weddell Sea. Its
> airport connects with the rest of Tepenia."*** `[CGRM 2026-09-02 · Path 6]`

**Half B flagged Sejong's 25% as the weakest of the eight, on the grounds that Marambio
already held the South America corridor at 60% and Sejong risked duplicating it.**
**The ruling shows they were never the same function.**

| | **Marambio** *(canon 60%)* | **Sejong** |
|---|---|---|
| **Maritime** | **⭐ South America + the Weddell Sea** — the international shipping corridor and onward distribution across the Weddell | — |
| **Aviation** | **⭐ DOMESTIC** — links Marambio to the rest of Tepenia. *(`Airports.md` already says so: "**Domestic** — links Marambio to other Tepenian cities.")* | **⭐⭐ INTERNATIONAL — Machu Picchu Airport**, *"connects directly to Ushuaia and the… Machu Picchu Border & Customs Authority"*, sited **closest to Sejong** |

> ## ⭐⭐ **They divide by MODE and by DIRECTION, not by territory.**
> **Marambio moves CARGO BY SEA into the country and PEOPLE BY AIR around it.**
> **Sejong is where PEOPLE enter Tepenia, and where the Border & Customs AUTHORITY is seated.**
>
> **⚠ CORRECTED 2026-09-02, during Sejong's own determination.** This line originally read *"Sejong is
> where people and goods ENTER TEPENIA AT ALL"* — **which contradicted the table directly above it**, where
> Marambio *"moves CARGO BY SEA into the country."* **Bulk cargo — phosphate rock above all, which is heavy,
> cheap, and never flies — enters by sea at Marambio; Sanay and Belgrano take the Africa freight. Machu
> Picchu is an AIR gateway.** The resulting structure is better than the error: **Sejong holds the
> institution, the ports hold the inspection points.** *(The mandate survives; the phosphate-inspection
> argument used to upgrade it does not apply as written.)*

### ⭐ And that makes Sejong's mandate stronger, not weaker

**Sejong hosts the national border.** Customs, immigration, quarantine, and the
inspection of everything arriving from Upper Earth — **in a nation that imports its
phosphate existentially from a power it does not trust** *(`14`)*. **A border is
mandated work in the strictest sense the test allows.**

> **25% stands, and is arguably conservative.** *(Compare Marambio at 60% for cargo and
> domestic flights.)*

**⏸️ One question the ruling opens:** `Airports.md` records Machu Picchu Airport as
*"closest to Sejong, but… close enough to Juan Carlos that the developer's own map places
its marker right at Juan Carlos's label — same airport, not a separate one."* **So does
Juan Carlos share the border function, or does Sejong hold it and Juan Carlos merely sit
nearby?** **Juan Carlos already carries fishing 30%; adding a border share would make it
a two-role city.**

## Revised standing of the eight

| Confidence | Cities | Note |
|---|---|---|
| **✅ Solid** | **{{Abowasa}} 10%** · **Scott 5%** · **Port Lockroy 5%** | Straight from canon's own commuter range and its own word *"small"* |
| **✅ Now solid** | **Sejong 25%** | **Upgraded by the ruling above** |
| **Reasonable by analogy** | ~~Zhongshan 20%~~ *(**withdrawn** — built on a misquote, see §18)* · Princess Elisabeth 25% · Concordia 15% | PE could be 15–20% *(consulting is lighter than industry)*; Concordia could be 20–30% *(Casey, a DUAL junction, carries 30%)* |
| **⚠ Weakest — still** | **Dome Fuji 20%** | **An estimate resting on an estimate** — the seed archive is my own proposal, and a *passive* vault needs almost nobody. **10% is probably closer.** Worth only 8,005 workers either way |

---

---

# ▶▶ PER-CITY DETERMINATIONS — the roster pass, one city at a time

> ## ⛔ STANDING RULE FOR THIS SECTION — NO CROSS-CITY COMPARISON
>
> **Developer direction, given at Belgrano and RE-STATED at Mirny, 2026-09-02:** *"Let's not compare between
> cities until after all the city profiles are completed."* · *"Don't make any commentary relative to other
> cities… **All of these numbers are subject to change.** Just report the facts about each city, and we'll
> determine cross-country comparisons later."*
>
> **The line that applies:**
>
> | Allowed | Not allowed |
> |---|---|
> | **Canon's own words**, quoted — including canon's own comparisons | **My comparative judgments** — rankings, "the only city that…", "unlike \<city\>", "least-free" |
> | **Real-world geographic fact** *(e.g. the Vestfold Hills are the largest ice-free coastal oasis in Antarctica)* | Superlatives across the roster drawn from **this pass's own figures** |
> | **Canon supply-chain relationships** *(A ships to B; A is on B's highway)* — these are facts about the city | Evaluative pairings *(who is "paid" vs. "invisible," who got a better deal)* |
>
> **⚠ This rule has been broken twice and swept twice.** Six comparisons were stripped from §§5, 7, 13, 18
> and 19 on 2026-09-02. **The reason it matters: every figure here is provisional until the roster is
> complete, so any ranking built on them is built on sand.**


**Begun 2026-09-02.** Reviewing every city against the full `City_Master_Reference` record plus this
folder's food/mining/shipping findings, and settling its three-tier split. **{{Bunger Hills City}} and
Lazar are excluded** — Bunger Hills deferred by ruling, Lazar's economy explicitly unresolved in canon.

> **⚠ Scope reminder, standing:** everything here describes the **Second Interwar** — Tepenia as a
> functioning country at peace. **`Status:` lines are post-war and are never an input.**

---

## 1. ✅ NEUMAYER — DETERMINED

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=2.50, forced importer → food term at 10%)* | 413,123 | **43.7%** |
| **Mandated** | 181,974 | **19.3%** |
| **FREE — the character budget** | 350,115 | **37.0%** |

**Distinctive tier: 532,089 (56.3%).** Canon §15 maps onto it as: Technical/scientific 35% · Technical/
engineering 20% · Education 15% · Marine 15% · Commercial 10% · Other 5%.

### The mandate, itemized

| Share of distinctive | Workers | Role | Basis |
|--:|--:|---|---|
| **16.7%** | 88,859 | **Scientific research — the EDEN ISS line** | ✅ Ruled floor *(`15` Resolution 4)*, derived from Neumayer's food-import debt |
| **10.0%** | 53,209 | **National design — half of Technical/engineering** | ⭐ **NEW this pass.** See below |
| **7.5%** | 39,907 | **Commuter labor — half of Marine 15%** | ✅ Developer ruling, 2026-09-02 |
| **34.2%** | **181,974** | | |

### ⭐⭐ The finding: `16`'s Half B undercounted this city by ~9.9 points

**Half B recorded Neumayer at mandated 9.4% / free 46.9%.** That figure was **only** the research floor —
and that floor was derived from *what Neumayer owes for imported food*, **not from what it does for the
country.**

> ## **It missed Technical/engineering 20% entirely — the design office that every active fabrication
> chamber in Tepenia builds to.**

Per the city's own canon facts: Neumayer designs the **Cradle Mark IV schematic** Sinheung and Byrd build
from *("nearly every robot fabricated today owes part of her existence to an uncredited Neumayer design
office")*, drafted **Amundsen Tower's schematics**, and re-engineered the **first Rastra**. **It passes the
mandated test without argument: stop it and the nation loses the ability to design the machines that make
robots.**

**Why HALF and not all of it:** on a floating ice shelf, a large share of that engineering sector is
genuinely local — the hydraulic-leg architecture needs continuous adjustment as the shelf moves. That is
local structural work, not national design.

### The marine ruling, and what it buys

**Developer ruling: half of Marine 15% is commuter labor** — the same mechanism ruled for Halley, and the
reading the evidence pointed to: Neumayer has **no docks** (canon), **no airport** (`Airports.md` L25), and
**no main-line highway** (reached only by the unnamed connector off Hwy 7). **Halley's own §15 one entry
away reads *"Marine/resource extraction 20% (indirect — no own docks)"*** — a direct in-subnet precedent for
an ice-shelf city's marine sector being indirect rather than crewed.

> **Ruling half rather than all keeps 39,907 workers in the free tier — +4.2 points — deliberately, so the
> local population is not wholly consumed by the import obligation.**

### ⏸️ Carried, not blocking

- **Possible §15/baseline overlap:** baseline already supplies C1a schooling (15,957), C1b training (5,259)
  and D3 retail (12,521) — up to **33,737 workers, 6.3% of distinctive**, could be double-counted against
  §15's Education 15% and Commercial 10%. **Quantified and small; does not change the determination.**
- Demonym unresolved; two placeholder holidays; whether the centuries-long climate record survived.

### ⭐ Methodological consequence for the rest of the roster

**`04` §3 assigned most cities ONE provider role. Neumayer proves a city can carry two or more nationally
load-bearing sectors in its §15.** **Every remaining city must be checked against its FULL §15**, not just
the single role `04` recorded. **Half B's mandate column is a floor, not a finding.**

---

## 2. ✅ BELGRANO — DETERMINED *(and its geology corrected)*

**Geographic order within the Halley subnet, per developer direction: start at Vahsel Bay and follow the
coast — which is Hwy 7's own route. Belgrano is the western terminus, so it comes first.**

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=1.43, **forced importer** → food term at 10%)* | 274,151 | **34.0%** |
| **Mandated** | 345,654 | **42.9%** |
| **FREE — the character budget** | 186,122 | **23.1%** |

**Distinctive tier: 531,776 (66.0%).** Canon §15: Aviation/logistics ~35% · Maritime/port ~20% ·
Technical/mechanical maintenance ~20% · Industrial ~15% · Other ~10%.

### ⚠ GEOLOGY CORRECTED FIRST — Belgrano is ice-shelf, not rock

**Full correction recorded in `13` §15.** In short: this folder had classified Belgrano rock-founded from
the real-world Bertrab Nunatak; **its own Specs file says *"the ice shelf environment means the coastal
geography shifts over time"* and *"flat coastal ice providing the airstrip infrastructure."*** It is the
Halley subnet's **third** ice-shelf city, making the subnet a 3–3 split.

**Effect: baseline 44.3% → 34.0%**, distinctive up to 66.0%, and Belgrano joins the forced-importer list.
**Its 77,044-worker-year food debt is covered ~3.8× over by aviation + maritime alone** — the obligation is
fully met from sectors it already has. **National balance falls to +89,538, still positive.**

### The mandate, itemized

| Share of distinctive | Workers | Role | Basis |
|--:|--:|---|---|
| **35%** | 186,122 | **Aviation/logistics — the subnet's primary aviation hub** | ✅ Canon §15. *"Paralleling Marambio's role in the Palmer subnet"*; **medevac is an aviation function, and the Belgrano Institute of Medicine sits downstream of the flight line** |
| **20%** | 106,355 | **Maritime/port — one of the two South Africa receiving ports** | ✅ Canon §15 + subnet-level canon *(with Sanay, interchangeable by open passage)* |
| **10%** | 53,178 | **Half of Technical/mechanical maintenance** — the share keeping the airfield and port running | ✅ Developer ruling, 2026-09-02 |
| **65%** | **345,654** | | |

**Industrial 15% stays FREE** — the *"las Arrastradoras"* / first-Rastra work is historical *(Neumayer
re-engineered the design)*, and the paused-Cradle-candidate status is potential, not current output.
**The other half of maintenance is ordinary city upkeep** — developer ruling.

### Notes

- **A heavily mandated city.** 65% of Belgrano's distinctive tier is nationally committed — consistent with
  canon's own framing that **the Airfield itself, not a city hall, was the seat of civic authority.**
- **⚠ The Institute is strategically load-bearing but numerically tiny** — roughly **1,750 teaching staff**
  against a 531,776 distinctive tier. It does not move the percentages; it means a small slice of Belgrano's
  mandate matters far out of proportion to its headcount.

> **⚠ NO CROSS-CITY COMPARISONS ARE DRAWN HERE, DELIBERATELY.** *(Developer direction, 2026-09-02.)* **Every
> figure in this pass is provisional until the whole roster is run** — Neumayer's own mandate moved ~9.9
> points once its full §15 was checked, and Belgrano's baseline moved 10.3 points on a geology correction.
> **Rankings, "least/most free" claims, and pattern statements across cities wait until every city is
> determined.**

---

## 3. ✅ HALLEY — DETERMINED

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=2.50, forced importer → food term at 10%)* | 478,952 | **43.6%** |
| **Mandated** | 170,093 | **15.5%** |
| **FREE — the character budget** | 448,426 | **40.9%** |

**Distinctive tier: 618,519 (56.4%).** Canon §15: Technical/scientific 25% · Marine/resource extraction 20%
*(indirect — no own docks)* · Commercial 20% · Technical/Arcanet 15% · Industrial 12% · Other 8%.

### The mandate, itemized

| Share of distinctive | Workers | Role | Basis |
|--:|--:|---|---|
| **20%** | 123,704 | **General commuter labor — the FULL Marine sector** | ✅ Ruled 2026-09-02 *(mines, rigs, ports, yards, krilling among them)*. Canon's own parenthetical calls the sector **"indirect — no own docks"**, which is what a commuter export is. Developer ruling 2026-09-02 set it at the full sector rather than the floor |
| **7.5%** | 46,389 | **Half of Technical/Arcanet — the Hwy 59 cable corridor** | ✅ Developer ruling, 2026-09-02. See below |
| **27.5%** | **170,093** | | |

**Commercial 20%, Industrial 12%, Technical/scientific 25%, Other 8% and the remaining half of Arcanet all
stay FREE.**

### Why the Arcanet split, and what the infrastructure pass contributed

**Halley's food debt is 102,800 worker-years — exactly the 9.4%-of-workforce commuter figure already ruled**,
so the debt and the export were the same number and never in question. **The open item was the separately
named `Technical/Arcanet 15%` sector.**

> **`Highways.md` L20, L62, L181–191: Hwy 59's northern ramp sits between Halley and {{Abowasa}}, and Hwy 59
> *"also carries the Arcanet cable along its full length"* south to Amundsen Station.**

**Halley is the populated city at the northern end of the national Arcanet corridor to the Pole relay.** The
subnet's *nexus* is at Sanay, so Halley's Arcanet sector is not nexus work — **the cable corridor is what it
plausibly is.** **Half mandated** *(a linear asset running hundreds of km south is sustained national work)*,
**half local municipal networking.**

**⚠ Error corrected during this assessment:** the infrastructure pass had recorded Halley as sitting on Hwy 7
*"between Abowasa and Sanay."* **It is between Belgrano and {{Abowasa}}** — the first stop east of Hwy 7's
western terminus. Fixed in `City_Master_Reference/Halley_Subnet_Reference.md`.

### Notes

- **No docks and no airstrip, both deliberate** — canon states fixed infrastructure would simply be carried
  away by the ice. All resupply arrives overland via Belgrano/Sanay onto the Hwy 7 connector.
- **⚠ Halley's mandated work and its survival run through the same two roads.** Canon stresses it has *"no
  maritime fallback"* and is *"genuinely more fragile than a typical coastal city"* — its entire external
  position rests on the Hwy 7 connector and Hwy 59. Does not change the tier arithmetic; worth carrying.
- The city is *"the only city architecturally designed from inception for relocation"* — ski-mounted modules
  with active propulsion tracks, moving deliberately ahead of a shelf drifting 400–700 m/yr.

---

## 4. ⏸️ {{ABOWASA}} — HELD AT CURRENT VALUE, FLAGGED FOR END-OF-PASS REVIEW

> **⚠ PLACEHOLDER NAME.** *"Abowasa"* is a working name folded from Aboa + Wasa (renamed 2026-07-05), not a
> settled one. Re-flagged per standing practice.

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=1.54, **GROWER** — bedrock nunatak, food term 100%)* | 355,900 | **45.5%** |
| **Mandated** *(held — see below)* | 42,622 | **5.4%** |
| **FREE** | 383,600 | **49.0%** |

**Distinctive tier: 426,222 (54.5%).** Canon §15: Technical/scientific 25% · Marine 15% · Commercial 15% ·
Industrial 15% · Education 15% · Other 15%. **Canon flags this itself** as *"genuinely modest, no dominant
sector,"* a *"small-scale economy,"* a city *"never a major economic node."*

### ⚠ Why this one is HELD rather than determined

**{{Abowasa}} grows its own food** — bedrock nunatak, ~130 km inland. **It carries NO food debt**, where a
forced importer of this size would owe 73,034 worker-years.

**That undercuts the rationale behind its current mandate.** The 10%-of-distinctive commuter-labor figure is
**my own Half A estimate**, tagged at the time *"estimate not canon-sourced."* It derives from `05`'s
commuter mechanism — *"5% of Halley + {{Abowasa}} workforce commuting"* — **which was built under the old
model, and applied to both cities for the same reason: paying for food. Halley must. {{Abowasa}} need not.**

**The full-§15 check finds nothing else nationally load-bearing here.** No institute, no fabrication role, no
research elevated anywhere in canon the way Neumayer's design work or Vostok's bioinformatics are.

### ⏸️ Held at current value — developer direction, 2026-09-02

> *"For now, let's keep it at its current value, and flag it for review once all the cities are done, and
> we'll see how cutting the labor affects national numbers."*

**The review should test these three readings against the completed national picture:**

| Reading | Mandated | Free | Note |
|---|--:|--:|---|
| **None — purely itself** | 0.0% | 54.5% | Canon's own "never a major economic node" language leans here |
| Half of Marine 15% | 4.1% | 50.4% | Real participation without obligation |
| **HELD: 10% of distinctive** | **5.4%** | **49.0%** | Current value, carried forward unchanged |
| Full Marine 15% | 8.2% | 46.3% | |

**What the review is actually for:** {{Abowasa}}'s commuter contribution feeds the Halley subnet's marine and
food logistics. **Cutting it changes what the subnet's three forced importers rely on** — so the question can
only be answered once every city's supply and obligation is on the table.

### Carried flags, neither blocking

- **⚠ Founding-nation consistency debt** *(the project's own flag)*: the *"Finnish and Swedish exiles,
  jointly"* premise may not survive the established First Interwar operator-turnover history. Touches the
  city's name, demonym, headline trait and its "Turku Remembrance" holiday.
- **No `Local_Robot_Culture` pass exists** — deliberately deferred pending that fix.

---

## 5. ✅ SANAY — DETERMINED

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=1.43, **GROWER** — bedrock nunatak, food term 100%)* | 154,715 | **44.5%** |
| **Mandated** | 140,045 | **40.3%** |
| **FREE — the character budget** | 53,121 | **15.3%** |

**Distinctive tier: 193,166 (55.5%).** Canon §15 *(rewritten 2026-07-04 per developer vision)*:
Port/shipyard 30% · Trucking/logistics 20% · Warehousing/import-export 15% · Industrial/manufacturing
(repair) 15% · Technical/scientific 10% · Other 10%.

### The mandate, itemized

| Share of distinctive | Workers | Role | Basis |
|--:|--:|---|---|
| **30%** | 57,950 | **Port/shipyard** — one of the two South Africa receiving ports | ✅ Canon §15 + subnet-level canon *(with Belgrano, interchangeable by open passage)* |
| **20%** | 38,633 | **Trucking/logistics** — onward national distribution, and the Sanay Corridor | ✅ Canon §15. *"Keeps a share → trucks the rest onward via Hwy 7, including to Troll for air distribution"* |
| **15%** | 28,975 | **Warehousing/import-export** — ⭐ **NEW this pass** | Same import chain as the two above. See below |
| **7.5%** | 14,487 | **Half of Industrial/manufacturing (repair)** — keeping freighters, trucks and the corridor running | ✅ Developer ruling, 2026-09-02 |
| **72.5%** | **140,045** | | |

**Technical/scientific 10%, Other 10% and the remaining half of repair stay FREE.**

### ⭐ Why warehousing was added

**`16`'s Half B counted port 30% + trucking 20% and stopped.** But goods land at the Port of Sanay, are
**stored and sorted**, then trucked onward. **Port, warehouse and truck are not three functions — they are
three stages of one national import operation.**

> **65% of Sanay's §15 is import-chain work before any judgment call is made at all.**

### ⚠ A structural gap found, not resolved

**Canon states Sanay *"HOSTS THE SUBNET'S ACTUAL ARCANET RELAY NEXUS — semi-distributed across the upper
clifftops."* That is national infrastructure. Its §15 has NO Arcanet sector.**

**Either Sanay's nexus staff sit inside Technical/scientific 10%, or the §15 is missing a line for
infrastructure canon says the city holds.**

**Technical/scientific 10% is left FREE here** rather than assuming it contains the nexus — **assigning it
would be inventing a sector allocation canon does not state.** Added to the review register below.

### Notes

- **The port is geographically disjoint.** Vesleskarvet sits ~200 km inland; the Port of Sanay is a coastal
  facility joined by **the Sanay Corridor** *(Athens/Piraeus model, `[CGRM 2026-09-01 · Path 6]`)*. **A
  substantial share of the mandated trucking sector runs Sanay's own internal corridor**, not only national
  onward distribution.
- Canon: *"Major port/logistics hub, not primarily a city of huge population."*
- `05`'s Halley-subnet commuter mechanism draws on Sanay's spare capacity alongside Belgrano.

---

## 6. ✅ TROLL — DETERMINED *(provisionally — Option A, flagged for review)*

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=1.43, **GROWER** — bedrock nunatak, food term 100%)* | 318,227 | **44.4%** |
| **Mandated** | 119,509 | **16.7%** |
| **FREE — the character budget** | 278,854 | **38.9%** |

**Distinctive tier: 398,363 (55.6%).** Canon §15 *(established 2026-07-04, developer vision session)*:
Commercial/logistics 30% · Technical/scientific 20% · Marine/resource extraction 15% ·
Industrial/manufacturing 15% · Education 12% · Other 8%.

### The mandate: one sector, entire

| Share of distinctive | Workers | Role | Basis |
|--:|--:|---|---|
| **30%** | 119,509 | **Commercial/logistics — the intermodal freight hub** | ✅ Canon §15, annotated *"airfield operations and control, the city's defining function"* |

**Everything else is FREE.**

### ⭐ Why the airport-type ruling settles this

**Developer ruling: every Tepenian airport except Machu Picchu is DOMESTIC** — they connect to each other,
not to the outside world. Applied to Troll, the freight geometry resolves completely:

> **Goods enter Tepenia by SEA. Troll is how they reach the rest of the country.**

Imports land at Sanay/Belgrano from Africa → trucked here on Hwy 7 → **flown out domestically across
Tepenia.** Troll is not an international gateway; it is the **national domestic air-freight distribution
hub for cargo that arrived by ship.** Canon: *"the effective center of a major share of Tepenia's actual
real-economy import/distribution network."*

**Two independent proofs of the mandate test** *("would the nation suffer materially without it?")*:
1. It is how sea imports reach the interior at all.
2. It was **half of the dual-route lifeline that kept Dome Fuji supplied** — from that city's pilgrimage
   resettlement until the Long Night War. *(Two separate direct aviation routes, not a relay; the other ran
   via a Sinheung-area airstrip.)*

### ⭐ No warehousing addition here — and why that is not inconsistent

**Sanay's §15 carries a separate `Warehousing/import-export 15%` line, so it was added to that mandate.
Troll's does not, and none is needed:** §15 annotates the 30% as *"airfield operations and control,"* and
the city's three named operational units — **Runway/Control Tower, Fuel Depot, Trucking Dispatch Yard** —
all sit inside that single sector. **The 30% IS the whole intermodal operation, receipt through dispatch.**

### 🔍 Finding — "Marine / resource extraction" at a city 235 km inland

Troll sits at Jutulsessen, **1,275 m elevation, 235 km from the coast.** Its §15 marine line is
**unannotated** and its label is **compound**.

**Two readings, and canon supports neither over the other:**

| Reading | Fit |
|---|---|
| **Resource extraction** — quarrying the exposed nunatak bedrock; no marine content at all | Strong. Troll is rock-founded with lateral bedrock access *(`13` §14)* |
| **Commuter/indirect marine participation** | The reading held open at {{Abowasa}} — **but weaker here**, since Troll grows its own food and has no import debt to work off |

**Either way it is LOCAL, not mandated** — canon states research and *"whatever the inland nunatak position
otherwise offers"* **round out the rest** of the economy, explicitly marking them as not the national
function. **Logged because the same compound label may appear at other inland cities, and this is the first
time the extraction half has been the more natural read.**

### Notes

- **Technical/scientific 20% is heritage research, not national provider work** — *"descended from the
  founding-era Polar Institute station."* Nothing in canon marks it load-bearing, so it stays free.
- **⚠ Corrected this pass:** the City Master Reference previously stated Troll *"is not on any highway route
  directly."* **False — Troll is on the Hwy 7 main line between Sanay and Lazar**, which is the road half of
  its own freight hub. Fixed in `Halley_Subnet_Reference.md`.
- Troll's freight network is a **confirmed secondary conduit for Cradle chambers passing through** — *"for
  years, nobody at Troll treats this as anything more than ordinary cargo."* Not a sector, but national
  significance moving through the mandated 30%.
- **38.9% free** sits under a city whose entire identity is *"Whoever Holds the Runway."* The runway is the
  mandate; everything Troll is apart from it stays unbought.

---

## 7. ✅ PRINCESS ELISABETH — DETERMINED

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=1.43, **GROWER** — bedrock nunatak, food term 100% — ⚠ see collision below)* | 375,938 | **43.7%** |
| **Mandated** | 121,274 | **14.1%** |
| **FREE — the character budget** | 363,821 | **42.3%** |

**Distinctive tier: 485,095 (56.3%).** Canon §15: Technical/scientific 25% · Industrial/manufacturing 20% ·
Commercial 20% · Marine/resource extraction 15% · Education 12% · Other 8%.

### ⭐⭐ The first city whose export is ASSERTED, not derived

**Specs, verbatim:** *"The zero-emissions design gave Princess Elisabeth genuine expertise in Antarctic
energy systems **that other cities traded for**."* Corroborated by §25 Export Culture: *"Princess
Elisabeth-trained specialists are recognized for genuine skill in sustainable Antarctic infrastructure."*

**Every other mandate in this pass has been derived from sector labels and geography. This one is stated
outright in ✅ CANON.** And it passes the mandate test cleanly — power in Antarctica is not a convenience,
and if PE holds the national competence in it, the nation suffers materially without it. ***"Traded for"
describes the delivery mechanism, not optionality*** — Sanay's port presumably charges too.

### The mandate

| Share of distinctive | Workers | Role | Basis |
|--:|--:|---|---|
| **25%** | 121,274 | **Technical/scientific — renewable energy systems and zero-emissions design expertise, in full** | ✅ Canon Specs + §25. **Developer ruling, 2026-09-02** |

### ⭐ Why FULL 25%, over the analyst recommendation of half

**The analyst recommended B (half, 12.5%)**, reading the sector annotation as naming two things — *"renewable
energy systems"* (PE runs on them; somebody operates them → local) and *"zero-emissions design expertise"*
(what other cities traded for → national).

**Developer ruled A (full 25%), on downstream-design grounds:**

> *"Once the events of the Halley DLC begin, there is a theoretical possibility that maybe, there might be
> some usable application (in either side-content or possibly hypothetically main content) in finding lost
> research records and using it to benefit people somehow. This is not confirmed. It's just a possibility
> that I think is worth considering."*

**⚠ Recorded honestly: this is the first mandate in the pass sized by downstream design potential rather
than by reading the sector.** Everywhere else the three-tier split has been purely descriptive — measuring
what canon already says. Here it is being used **generatively**, to leave room for content that does not
exist yet. **That is a legitimate call and it is the developer's to make, but it is a different kind of move
and should not be mistaken later for a derivation.**

**What the ruling concretely buys** — and this is the substantive gain:

> **PE is DESTROYED. The ruins therefore contain the physical remains of a 121,274-worker energy-research
> establishment**, not a vague sense that "research happened here." **That is a level-design quantity:** how
> many facilities, how much surviving documentation, how deep the archive plausibly runs, how many separate
> sites could hold recoverable records. **Halving it would have halved the ruin.**

### Three sectors that look mandated and are not

**Commercial 20% — the inter-subnet road link.** PE sits on **Hwy 7-ext between Lazar and the Sayowa
Junction — the only road connection between the Halley and Mawson subnets.** But canon frames the sector as
*"trade **leveraging** the city's dual eastern/Atlantic connections"* — **the city profiting from its
position, not conscripted by it. The mandate test asks what the nation needs FROM you, not what you gain
FROM WHERE YOU SIT.** No canon states national freight moves through PE. **FREE.**

**Industrial 20% — *"infrastructure maintenance and repair."*** PE has **zero passive wind shelter**, faces
gales to 300 km/h, and *"survives only through active aerodynamic engineering."* **This is the least
discretionary work in the city and it is still not national work** — a city that cannot stop maintaining or
it dies is performing local survival, not provider service. **FREE**, though the word sits oddly here.

**Marine/resource extraction 15%** — same compound, unannotated label found at Troll, same inland position
*(Utsteinen nunatak, 1,382 m, Sør Rondane Mountains)*. **Second instance of the pattern.** Free either way.

### ⚠ CANON COLLISION — logged, not resolved

**The vignette "What the Wind Can't Grow" states the city *"was never self-sufficient in food/materials, only
energy."*** That directly contradicts PE's GROWER classification.

**Vignettes are not canon, so f = 1.00 stands.** But the sensitivity is large enough to record:

| | Baseline | Distinctive |
|---|--:|--:|
| **f = 1.00 (grower — current)** | 375,938 · **43.7%** | 485,095 · **56.3%** |
| **f = 0.10 (if the vignette were promoted)** | 289,915 · **33.7%** | 571,118 · **66.3%** |

**A possible reconciliation, offered but NOT asserted:** PE's **outdoor tier is genuinely zero** — 300 km/h
winds preclude terraformed fields entirely, and `12`'s 1,500 km² belt does not include it. The vignette may
be describing that, not indoor growing, which bedrock founding permits at will.

### Notes

- **No airport** — highway-only *(Airports.md L25)*. PE is not an air node.
- Retires the earlier note in this file's Half A that *"PE could be 15–20% — consulting is lighter than
  industry."* **That was reasoning by analogy against other cities; reading PE's own sector labels is better
  evidence, and the developer's ruling supersedes both.**

---

# ▓▓ PALMER SUBNET ▓▓

*Halley subnet closed at six determined — Belgrano · Halley · {{Abowasa}} · Sanay · Troll · Princess
Elisabeth — with **Lazar deferred by developer ruling.***

---

## 8. ✅ SIGNY — DETERMINED

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=1.25, **GROWER** — rock-founded island, food term 100%)* | 58,480 | **41.1%** |
| **Mandated** | 46,006 | **32.4%** |
| **FREE — the character budget** | 37,641 | **26.5%** |

**Distinctive tier: 83,647 (58.9%).** Canon §15: Biological/ecological research 30% · Marine/fishing 30% ·
Maritime trade 20% · Technical/maintenance 15% · Other 5%.

### The mandate, itemized *(developer ruling, 2026-09-02)*

| Share of distinctive | Workers | Sector | Basis |
|--:|--:|---|---|
| **30%** | 25,094 | **Marine/fishing — FULL** | ✅ `04` §3 lists Signy a national **FOOD (fish) provider** at 30% |
| **15%** | 12,547 | **Biological/ecological research — HALF** | Derived: the fishery is **capped**, and somebody must know where the cap is |
| **10%** | 8,365 | **Maritime trade — HALF** | Derived: **Signy has no highway.** The catch reaches Tepenia only by sea |
| **55%** | **46,006** | | |

### ⚠ Two scope traps deliberately excluded

**The siligel shortage and the "survived, untouched by war damage" status are the two most striking facts in
Signy's file, and BOTH ARE POST-WAR.** Second Interwar is the scope; neither is an input here. **Recorded so
a later reader knows they were set aside on purpose rather than missed.**

### ⭐⭐ The food model resolves a double-count that would otherwise be real

**Signy carries a FULL baseline food term** *(grower, ~22,022 workers feeding its own humans)* **AND a
national fish mandate.** On its face that counts the same labor twice — the city feeds itself *from* the
sector it also exports from.

**It does not, and `14` is why.** Marine capacity is **protein-rich, fat- and carb-poor — the rabbit-
starvation failure mode.** ***Signy cannot eat its way out of needing farms.*** The two labor pools are
genuinely separate: one grows carbohydrate and fat for local consumption, the other harvests protein for the
nation.

> **A constraint built for the national model turned out to do load-bearing work at the single city sitting
> on the richest fishery in the country.** Noted because it is the first time a national finding has resolved
> a per-city accounting problem rather than merely constraining one.

### What the marine 30% actually is — and why the platforms exist

**25,094 workers. `11` established the entire national sustainable catch needs only ~13,000 fishers** — so
this single sector is **1.9× the whole national fisher requirement.** It therefore **cannot be crews.** It is
harvest platforms, processing, and dock work.

**And canon anticipated the crowding from a completely different direction.** Signy Island is **19 km², about
half of it ice-free** *(`13` §13)*, and it holds **both** the work ground and the shipping dock. The ⚠ Vision
Notes' **"floating extension-platforms"** exist *precisely because the island is too small to hold the
operation.* **Two independent lines — a labor calculation and a 2026-07-04 vision session — arrived at the
same physical constraint.**

### The two derived halves, argued

**Maritime trade, half.** Signy is **maritime-access only, the most isolated Palmer subnet city, with no
highway at all.** If it is a national food provider, **the only way that catch physically reaches Tepenia is
by sea** — harvest, process and ship are three stages of one operation, the same structure ruled at Sanay.
**Half, not full**, because the sector also runs Signy's own inbound supply: everything the city consumes
arrives on those same boats.

**Biological/ecological research, half.** The Scotia Sea supplies a material share of national calories and
**cannot be harvested past its limit without collapsing.** A 30% ecological-research sector sitting on that
exact water is plausibly what keeps the national fishery from being fished out. **Half, not full**, because
wildlife work and long-term monitoring are also genuine pure science.

> **⚠ Honest note on the research half: this is DERIVED, not stated.** Canon says only *"Biological/ecological
> research 30%."* The fishery-management reading is inference. **It is a stronger inference than the one
> declined at Troll — the national food model supplies positive evidence rather than analogy — but it is
> still inference, and should be re-examined if Signy's research sector is ever annotated in canon.**

### Notes

- **Technical/maintenance 15% stays FREE** — unannotated as to what it maintains, so per the Troll principle
  it is not assumed to be platform work.
- **⭐ The free budget's shape is unusual and worth recording.** Of 37,641 free workers, **20,912 are the
  untouched halves of the two sectors Signy is already mandated in.** Its genuinely unconscripted work —
  maintenance and Other — is 16,729. **Signy's character budget is mostly the discretionary end of the same
  things it does for the nation, not something separate from them.**
- **The two-island commute is internal**, not labor exported to another city: homes on **Coronation**
  (450 km²), work on **Signy Island** (19 km²), one bridge between *(developer ruling 2026-09-02, the ruling
  that generalized into `13` §14's national bedrock-volume criterion)*. **Not a tier change** — but a real
  share of the free maintenance sector runs the crossing.

---

## 9. ✅ SEJONG — DETERMINED

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=1.15, **GROWER** — rock-founded island, food term 100%)* | 191,522 | **39.4%** |
| **Mandated** | 73,741 | **15.2%** |
| **FREE — the character budget** | 221,224 | **45.5%** |

**Distinctive tier: 294,966 (60.6%).** Canon §15 *(2026-07-04)*: Commercial/trade 25% · Technical/scientific
20% · Diplomatic/inter-community coordination 15% · Marine/resource extraction 15% · Education 15% ·
Other 10%.

### The mandate

| Share of distinctive | Workers | Role | Basis |
|--:|--:|---|---|
| **25%** | 73,741 | **Commercial/trade — the international air gateway** | ✅ Canon §15 *"leveraging King George Island's accessibility"* + the gateway ruling **as corrected above** |

### ⭐ Why the diplomatic sector was NOT added — the sharpest sector call in the pass so far

A port of entry needs immigration and foreign-arrival handling, which **is diplomatic work by nature**, and
Sejong has a 15% sector literally called *Diplomatic*. **It was still declined, and the reason is a
three-step distinction now established across the pass:**

| City | Sector state | Disposition |
|---|---|---|
| **Troll** | **Unannotated** | **Declined** — no positive evidence to split on |
| **Princess Elisabeth** | Annotated, naming **two** things *(one local, one national)* | **Split** — reading the annotation, not assuming past it |
| **Sejong** | Annotated, naming **one** thing, and it **points internally** | **Declined** — taking it would **override a stated annotation** |

**Canon's annotation:** *"inter-community coordination — a genuinely unique sector given the island's
density."* **That is the Korean, Argentine, Brazilian, Chilean, Polish, Russian, Czech and Uruguayan
communities sharing one island** — internal, not international. **Overriding it would be a step beyond
anything ruled so far.**

> **Developer, ruling A, 2026-09-02:** ***"The 'diplomatic' side happens via Machu Picchu Airport."***

### ⚠ The §15 predates the gateway ruling by two months

**Sejong's §15 is from the 2026-07-04 vision session. The international-gateway ruling is 2026-09-02.** The
§15 was therefore written **without the border function in it** — and contains **no customs, immigration, or
border line anywhere.**

**This is the SECOND instance of the Sanay pattern:** a city holding national infrastructure its §15 has no
sector for. Register item 6.

### Notes

- **Technical/scientific 20% — *"inherited KOPRI research tradition."*** Local heritage research, nothing
  marking it load-bearing. **FREE.**
- **Marine/resource extraction 15% — unannotated, but Sejong is COASTAL.** Register item 5's inland-
  extraction pattern **does not apply here**, and `04` §3 names **Juan Carlos** the South Shetlands fishing
  provider, not Sejong. **FREE.**
- **⚠ DATA INTEGRITY — education 15% deliberately excluded from all reasoning.** Sejong's robot-culture file
  carries a **live, only-partially-fixed canon bug**: the invalidated "Korean dilution" premise still stands
  in three files, including an entire Course of Events chain, and the stale material attaches
  Hangul-literacy content to **exactly this sector.** **The determination was built without touching it
  rather than risk reasoning from contaminated content.**
- **⏸️ Still open from the gateway ruling:** whether **Juan Carlos** shares the border function — the
  developer's own map places Machu Picchu's marker at Juan Carlos's label, same airport. **Unaffected by
  this determination**; Sejong's 25% would stand either way, but Juan Carlos's own entry must resolve it.

---

## 10. ✅ JUAN CARLOS — DETERMINED

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=1.15, **GROWER** — rock-founded island, food term 100%)* | 114,813 | **39.3%** |
| **Mandated** | 70,803 | **24.3%** |
| **FREE — the character budget** | 106,205 | **36.4%** |

**Distinctive tier: 177,008 (60.7%).** Canon §15: Maritime/fishing 30% · Commercial/trade 20% ·
Technical/scientific 20% · Cultural/social institutions 15% · Other 15%.

### The mandate *(developer ruling B, 2026-09-02)*

| Share of distinctive | Workers | Role | Basis |
|--:|--:|---|---|
| **30%** | 53,102 | **Maritime/fishing** — national food provider | ✅ `04` §3 + §15 *"leveraging Livingston Island's coastal access"* |
| **10%** | 17,701 | **Half of Commercial/trade — the federal immigration archive and processing** | ✅ Canon national role; **sector inferred** *(see below)* |
| **40%** | **70,803** | | |

### ⭐⭐ The open border question answered itself — and a THREE-CITY SYSTEM fell out

The question carried into this entry was *"does Juan Carlos share Sejong's border function?"* **Canon answers
it, and more precisely than the question was posed.** Juan Carlos is *"Tepenia's first bureaucratic archive —
the original home of Federation immigration/customs records, **directly tied to the Machu Picchu Border &
Customs Authority.** Non-immigrant visitors routed to a separate corridor/sealiner to **Palmer City**."*

> ### **They do not share one function. They hold three stages of one system.**

| City | Stage |
|---|---|
| **Sejong** | The arrival point, and the seat of the Authority |
| **Juan Carlos** | **Immigration processing and the records archive** |
| **Palmer City** | Where **non-immigrant** visitors are routed onward |

**And it explains the destruction.** Upper Earth targeted Juan Carlos *specifically* for records tracking
former Upper Earth officials among the exiles — ***"even after the bulk archive had moved."*** The same
archive is the **direct historical origin of the Amundsen Station archive DLC 1 is built on.**

**⚠ Sector inferred, and the Troll rule is not broken.** Commercial/trade 20% is the only **unannotated**
sector besides Other; Technical/scientific and Cultural/social both carry explicit *local* annotations.
**Troll's refusal was "unannotated AND no positive evidence to split on." Here canon states the national
function exists** — only its sector is open. **Half rather than full: an island city with no highway still
needs ordinary commerce.**

### ⏸️ A timing ambiguity, flagged not decided

Canon says the archive *"later relocated and consolidated into Amundsen Station's"* archive, and that the
strike came *"even after the bulk archive had moved."* **The Second Interwar runs 248 years — the move
happened somewhere inside our own scope window, and no date is given.** Whether this mandate describes the
whole period or only its earlier stretch is **genuinely open.** Register item 10.

---

# ⭐⭐⭐ STRUCTURAL FINDING — WHERE ADMINISTRATION LIVES

**Raised by the developer, 2026-09-02:** *"I'm assuming that Administration/Bureaucracy gets its own
sector?"* **Checked empirically across all 37 cities' §15 blocks — ~85 distinct sector labels.**

## 1. No city has one. Not even the capital.

**There is NO Administration, Government, Bureaucracy, or Civic sector anywhere in the national §15
vocabulary.** The sole exception is **Esperanza — *"Other / administrative (birth registry and related civic
institutions): ~10%"*** — and that is a **sub-label of Other**, not a sector.

> **⚠ `Fort McMurdo` is the NATIONAL CAPITAL. Its §15 reads: Industrial 35% · Marine 25% · Technical 15% ·
> Commercial 10% · Education 8% · Other 7%. The capital of the Tepenian Federation records ZERO governmental
> employment.**

## 2. But the model already handles it — in the BASELINE, not §15.

**`09` §1 puts administration in the resident-keyed baseline term**, and it is the largest component there:

| Difficulty-**immune** component | Rate per 1,000 residents |
|---|--:|
| **C3 Administration** | **65** |
| C8 Finance & allocation | 15 |
| D4 Computing & data | 8 |
| C6 Legal & justice | 5 |
| C7 Community & social | 4 |
| *(remaining: retail, trade training, communications)* | 16.2 |
| **Total = the 113.2 constant** | **113.2** |

**C3 alone is 57% of the entire difficulty-immune baseline term.** **Administration is not missing from the
model. It was never in the §15s because the model put it in baseline** — where it scales with population, as
the administration a city needs *for itself.*

## 3. So the real gap is narrower, and precisely stated

| Scale | Modeled? |
|---|---|
| **Local administration** — what a city needs to run itself | ✅ **Baseline, C3 at 65/1,000 residents** |
| **National administration concentrated in one city** — capital functions, the Border & Customs Authority, the federal archive | ❌ **NOT MODELED. This is the gap.** |

**C3 is a per-capita rate. It cannot represent a function a city performs for the whole country**, because
that work does not scale with the host city's own population.

## 4. ⚠ And adding a generic admin sector to every §15 would be actively harmful

**`09` §1 already warns, in its own words:**

> ***"The affected/immune split has shifted from 50/50 to 36/64. Administration plus four indoor industries
> made the baseline substantially difficulty-immune — which compresses inter-city differentiation. MORE
> ADMINISTRATION MAKES TEPENIAN CITIES LOOK MORE ALIKE."***

**Administration is difficulty-immune, so every unit of it added uniformly flattens the very differentiation
this whole project exists to protect.** *(Compare `CLAUDE.md`'s standing guard against thirteen districts
quietly converging.)*

## 5. Recommendation

**Do NOT add an Administration sector to the §15s.** Instead:

1. **Local administration stays in baseline.** Already correct, already sized, already the largest immune
   component.
2. **National administrative concentration is handled as a MANDATE, city by city** — which is exactly what
   has been done at Sejong *(border authority)* and Juan Carlos *(federal archive)*, and at Sanay *(Arcanet
   nexus)*.
3. **⚠ Fort McMurdo needs one and does not have one.** Its current 35.1% mandate is **entirely industrial**.
   **The seat of national government is, in the model as it stands, a mining and manufacturing town that
   happens to be the capital.** Register item 9 — **to be resolved when its own entry comes up, not now.**

**This reframes the three §15 gaps found so far.** Sanay, Sejong and Juan Carlos are not three separate
oversights: **the §15s describe LOCAL economies, and national functions systematically fell through — because
the vocabulary those breakdowns were written in has no word for them.**

---

# ⭐⭐⭐ ESTABLISHED — THE **ABCC** SECTOR

> ## **Administrative, Bureaucratic, Civic, Clerical** — abbreviated **ABCC** in notes.
> **`[CGRM 2026-09-02 · Path 6 · developer ruling]`** — established directly in response to the structural
> finding above.

**A new sector in the national §15 vocabulary — the first added since the breakdowns were written.** It gives
national administrative work a **named home** instead of leaving it to be inferred into whichever bare sector
happened to sit nearby.

### What it immediately fixes

**Every mandate assigned to administrative work so far has been placed by INFERENCE**, because there was no
sector to put it in:

| City | What was done before ABCC | With ABCC |
|---|---|---|
| **Juan Carlos** | *"Half of Commercial/trade — sector inferred"* | **ABCC**, named |
| **Sejong** | Border Authority folded into Commercial/trade 25% | **ABCC** *(⚠ but see below — a ruling already stands here)* |
| **Esperanza** | Already carries *"Other / **administrative** (birth registry and related civic institutions): ~10%"* | **⭐ The retroactive FIRST INSTANCE — an ABCC line that existed before the sector had a name** |
| **Fort McMurdo** | **Nothing. The capital records zero governmental employment** | **ABCC — register item 9** |
| **Amundsen Station** | Holds the consolidated federal archive; §15 has no line for it | **ABCC candidate** |

**⚠ Sanay is NOT an ABCC case.** Its missing §15 line is the **Arcanet relay nexus** — physical
infrastructure, not administration. **Register item 2 stays open on its own terms.**

**⚠ Sejong already has a standing developer ruling (A, 25%, commercial/trade only).** ABCC does not
automatically reopen it — **flagged, not changed.**

### ⭐⭐ RULED — ABCC IS A **BASELINE** COMPONENT, AND IT **VARIES BY CITY**

> **Developer, 2026-09-02:** ***"The ABCC sector would be part of 'baseline'… Now, exactly, precisely how
> much of baseline, that would depend on the context of the location, but I think you're right to include it
> in baseline."*** **`[CGRM 2026-09-02 · Path 6]`**

**So ABCC is not a §15 sector after all — it is the renaming and RE-SIZING of the baseline's largest
component,** `09` §1's **C3 Administration, 65 per 1,000 residents.**

### ⭐ Why this is the better answer — it dissolves the flattening problem instead of trading against it

`09` §1's own warning was: ***"More administration makes Tepenian cities look more alike."*** **That was
never true of administration as such. It was true of administration held FLAT.**

| | Difficulty-immune? | Uniform across cities? | Flattens? |
|---|---|---|---|
| **C3 as it stands — flat 65/1,000** | Yes | **Yes** | **✅ Yes** |
| **ABCC — variable by city context** | Yes | **NO** | **❌ No** |

**A difficulty-immune component only compresses differentiation if it is the same everywhere.** Making it
context-dependent means **the capital, a subnet hub and a fishing island now differ in their baselines for a
reason that is about governance rather than about weather** — a second, independent axis of differentiation
that the model did not previously have. **`09`'s warning is not overridden here; it is satisfied.**

### What ABCC covers — narrow reading taken, pending any expansion

**ABCC is taken as C3 Administration (65) renamed and made variable.** The adjacent immune components are
**left alone** unless the developer says otherwise, since each has its own separate derivation in `09` §1:

| Component | Rate | Status |
|---|--:|---|
| **C3 Administration** | **65** | **→ becomes ABCC, variable** |
| C8 Finance & allocation | 15 | Unchanged *(own derivation: people, not prices, allocate here)* |
| D4 Computing & data | 8 | Unchanged |
| C6 Legal & justice | 5 | Unchanged |
| C7 Community & social | 4 | Unchanged |
| *(retail, trade training, communications)* | 16.2 | Unchanged |

**⚠ "Clerical" and "Bureaucratic" plausibly reach into C8 and D4.** **Not assumed — flagged for the
developer.** Expanding ABCC to absorb them would raise the variable pool from 65 to 88 per 1,000.

### ⚠ CONSEQUENCE — the ten determinations so far need a baseline re-run

**Every city determined before this ruling used the flat 65.** When per-city ABCC values are set, their
**baselines move, and therefore their distinctive tiers and worker counts move with them.**

> **The re-run is MECHANICAL, not a re-judgment.** Mandates were ruled as **percentages of the distinctive
> tier**, and those percentages do not change — only the worker counts they resolve to. **No developer ruling
> already given is invalidated by this.**

### ⏸️ PER-CITY ABCC VALUES — PARKED, 2026-09-02

**A four-tier structure was proposed *(capital / federal-institution host / ordinary / single-purpose
station)* and SET ASIDE by developer direction.** *"Insofar as the tier structure, I say set this aside for
now, and we'll come back to it later."*

**⚠ WORKING VALUE UNTIL THEN: ABCC stays at the flat 65 per 1,000 residents for ALL cities.** New
determinations continue on the flat value **so that every city re-runs together, consistently, in one pass**
rather than some being converted early.

### ⚠⚠ A CATEGORY ERROR CAUGHT BY THE DEVELOPER — record it, it will recur

**The proposal put *"subnet hub"* cities into the elevated ABCC tier. That is wrong.**

> **Developer, 2026-09-02:** ***"T2 is already way, way, way too high, since that includes Mawson, which is a
> tourism & resort town (which is also a popular honeymoon destination), and therefore the overwhelming
> majority of Mawson's industry would be oriented around some degree of interacting with the public in some
> form."***

**Mawson's §15 reads `Subnet-hub logistics / Arcanet coordination: 25%` — and "hub" was read as
administrative weight. It is not.** It is **logistics and communications infrastructure**, and Mawson's
actual economy is **public-facing hospitality** *(its §15 also carries `Hospitality / honeymoon tourism`,
established in the 2026-07-06 vision session)*.

> ## **⭐ STANDING RULE — SUBNET-HUB STATUS IS INFRASTRUCTURE, NOT ADMINISTRATION. It does NOT raise ABCC.**
>
> **This is the same distinction already drawn at Sanay** — whose missing §15 line is the **Arcanet relay
> nexus**, explicitly excluded from ABCC as physical infrastructure — **and then not applied two paragraphs
> later.** **The word "hub" is not evidence of bureaucracy.**
>
> **What DOES raise ABCC:** a city holding a **named governmental body or federal institution** *(the Border
> & Customs Authority, the federal immigration archive, the seat of national government)* — **not a city
> holding cables, roads, or a relay.**

---

## 11. ✅ ESPERANZA — DETERMINED

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=1.11, **GROWER** — mainland Peninsula, food term 100%)* | 555,826 | **39.7%** |
| **Mandated** | 359,037 | **25.6%** |
| **FREE — the character budget** | 485,756 | **34.7%** |

**Distinctive tier: 844,793 (60.3%).** Canon §15: Education/childcare/family ~25% · Maritime/harbor trade
~20% · Commercial ~15% · Technical/scientific ~15% · Agricultural/food production ~15% ·
Other/administrative ~10%.

**⭐ Esperanza carries THREE national roles** — `04` §3 lists it **FOOD · EDUC · MEDICINE**.

### The mandate *(developer ruling, 2026-09-02)*

| Share of distinctive | Workers | Sector | Basis |
|--:|--:|---|---|
| **12.5%** | 105,599 | **Education/childcare/family — HALF** | The Esperanza Institute of Medicine **+ standard schooling**, per the ruling below |
| **15%** | 126,719 | **Agricultural/food production — FULL** | ✅ `04` §3 national FOOD provider |
| **10%** | 84,479 | **Maritime/harbor trade — HALF** | Hwy 1's northern terminus + Halley↔Palmer trans-shipment |
| **5%** | 42,240 | **Other/administrative — HALF (the birth registry)** | ✅ Developer ruling: **national by this era** — see below |
| **42.5%** | **359,037** | | |

### ⭐ The education correction — this file's own Half B flag was right

**`16` counted education 25% as FULLY mandated and flagged its own double-count risk.**
**`National_Medical_and_Care_Institutes.md` had already settled the sizing, in the opposite direction:**

> *"Esperanza at ~12,600 graduates a year on ~3-year programs carries a standing student body of ~37,800 —
> about 2% of a 1.88 M city… **The Institute is one part of a much broader education economy** (local
> schooling, childcare, family services, general tertiary export), **not the whole of it.**"*

**At a 1:12 ratio the Institute is ~3,150 teaching staff — 1.5% of its own host sector.** The national
medical school is a rounding error inside the sector named after it. **Baseline separately already holds
24,839 schooling + 4,777 childcare workers** for Esperanza's own humans.

**Developer ruled HALF rather than the analyst's proposed one-third — and the reasoning changes what the
mandate MEANS:**

> ***"Instead of plus-one-third education, it's plus-half education (since it would account for both standard
> schooling as well as the Institute)."***

> ### **⭐⭐ So standard schooling at Esperanza is NATIONAL work, not local work.**
> **That follows directly from the founding charter** — the city was built *"to care for the children of
> humans who chose exile alongside robots."* **It does not merely educate its own; educating is what the
> city is FOR.** The mandate is therefore not "a medical school plus some local schools" — **it is the
> nation's child-rearing compact, of which the Institute is the smallest visible part.**

### ⭐⭐ NEW CANON — the birth registry's local→national transition

> **Developer, 2026-09-02** `[CGRM 2026-09-02 · Path 6]`:
> ***"During the early period of the country, the birth registry starts out as local (since the peninsula is
> where Tepenia starts out when it was originally founded, following the Falkland Treaty) and then, as the
> country grows and expands, the birth registry proceeds to become national (since now, the statistics are
> nationally relevant)."***

**Two facts established, only one of which is about Esperanza:**

1. **⭐ THE PENINSULA IS WHERE TEPENIA BEGAN**, post-Falkland Treaty. *(Bears on the founding sequence far
   beyond this city — and note the national capital, **Fort McMurdo**, is in the **Janbogo** subnet, so the
   seat of government is NOT where the country started.)*
2. **Esperanza's birth registry began as a local civic record and became a national institution** as the
   country expanded around it — *"the statistics are nationally relevant."*

**Applied to scope:** the Second Interwar is the **mature functioning country**, so **the registry is
NATIONAL here** and its labor is mandated. **Half of the sector**, since §15 names two things — *"birth
registry **and related civic institutions**"* — one national, one local. *(The Princess Elisabeth split
pattern.)*

> **⚠ This also resolves the ABCC tension cleanly.** Per the ABCC ruling, **local** administration lives in
> **baseline** — so the *"related civic institutions"* half correctly stays out of the mandate, while the
> **national** registry is exactly the "national administrative concentration handled as a mandate" case the
> structural finding described. **Esperanza is the first city where that distinction is actually applied.**

### Notes

- **Agricultural 15% stays FULL despite the botany finding.** `13`'s 2026-09-02 research found **Hope Bay has
  the LOWEST moss/lichen diversity of the maritime Antarctic sites studied** — below the South Shetlands —
  and the Peninsula's best growing ground is at Juan Carlos and Sejong instead. **This does not remove the
  role; it changes its nature.** ***Esperanza feeds the Peninsula from ground it does not sit on***, making
  the sector handling and distribution rather than cultivation. *(`13`'s own phrase: "mild, cramped, and
  surrounded by better ground it doesn't sit on" — the Sanay/Port-of-Sanay split in a different key.)*
- **Maritime half** — Hope Bay is **Hwy 1's own northern terminus**, *"the only land route connecting the
  Antarctic Peninsula to the rest of Tepenia,"* and a Halley↔Palmer trans-shipment node. The other half is
  ordinary harbor commerce.
- **Commercial 15% and Technical/scientific 15% stay FREE.**
- **Population note:** Census I *(955,337 H / 922,950 R / 1,878,287)* is used, per Second-Interwar scope.
  Census II shows 1,178,039 — **reduced to 85% by organic emigration to Lazar**, a later-period fact.

### ⭐ RULED — the Institutes do NOT get their own sector

**Developer question, 2026-09-02:** *"Would it be right to list the Institute separately? It's part of
education, yeah?"* — **Yes at Esperanza, and that is exactly why the answer is no.**

| Institute | Host city | Which §15 sector houses it |
|---|---|---|
| **Esperanza Institute of Medicine** | Esperanza | **Education/childcare/family 25%** |
| **Belgrano Institute of Medicine** | Belgrano | **Aviation/logistics 35%** — *"medevac is an aviation function… the school is downstream of the flight line"* |
| **Sinheung Institute of Cybernetics and Robotic Care** | Sinheung | **Education / other 5%** *(⚠ corrected 2026-09-02 during Sinheung's own determination — this row first read "Industrial fabrication 45%," misreading `National_Medical`'s "Why Sinheung" passage. **That passage explains why the CITY hosts the Institute; it does not say which sector employs its staff.** An institute teaching care is staffed by educators. **Why a city hosts something ≠ which sector pays for it** — the three-different-sectors finding is unaffected)* |

**Three institutes, three completely different host sectors. They do not share an industry — they share a
NATIONAL FUNCTION.** A "Medical Institutes" §15 line would have to be carved out of education at one city,
aviation at another, and heavy fabrication at a third.

> **⚠ And it would destroy the best thing about them: each grew out of what its city already did.** Belgrano
> teaches trauma **because it flies the medevacs**; Sinheung teaches robotic care **because it builds bodies
> by the thousand** *(`National_Medical_and_Care_Institutes.md` makes the contrast its point: "an institute
> of care sits inside Tepenia's most heavily industrial city")*. **Give them a shared sector and they become
> three interchangeable medical schools that happen to sit in different places.**

**The MANDATE TIER is already the correct instrument** — it exists precisely to mark *national function
regardless of which sector houses it*, and both determined cities already use it that way.

**Scale confirms it:** Esperanza's Institute is **~3,150 staff — 1.5% of its own sector**, against §15 lines
running 5–45%. A separate line would sit below the resolution of every other entry **and** visually imply the
Institute *is* Esperanza's education mandate — **the exact opposite of the half-education ruling.**

> ### **This is the REVERSE of the ABCC case, and the distinction is worth keeping.**
> **ABCC got a sector because administration was MISSING FROM THE VOCABULARY ENTIRELY.**
> **The Institutes are ALREADY PRESENT and correctly sized — in three different sectors, for three good
> reasons.** ***A new sector is for what the vocabulary cannot say, not for what it says in an unexpected
> place.***

---

## 12. ✅ MARAMBIO — DETERMINED

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=1.25, **GROWER** — Seymour Island, rock-founded, food term 100%)* | 177,203 | **41.3%** |
| **Mandated** | 175,942 | **41.1%** |
| **FREE — the character budget** | 75,404 | **17.6%** |

**Distinctive tier: 251,345 (58.7%).** Canon §15 *(revised 2026-07-16)*: Aviation/logistics 30% ·
Maritime/port operations 30% · Technical/maintenance 20% · Commercial/trade 15% · Other 5%.

### The mandate *(developer ruling B, 2026-09-02)*

| Share of distinctive | Workers | Sector | Basis |
|--:|--:|---|---|
| **30%** | 75,404 | **Maritime/port operations** — the South America + Weddell Sea receiving node | ✅ `04` §3 + §15 *"equally central to the city's defining, dominant identity"* |
| **30%** | 75,404 | **Aviation/logistics** — **DOMESTIC**, distributing onward across Tepenia | ✅ `04` §3 + `Airports.md` L16 |
| **10%** | 25,134 | **Half of Technical/maintenance** | ✅ Developer ruling |
| **70%** | **175,942** | | |

### ⭐ The whole intermodal node sits inside one municipality

**Sea in, air out — both under one city government.** The port receives from **South America and the Weddell
Sea**; the airfield is **domestic-only**, distributing *"to other Tepenian cities."* `04` §3 already lists
the two together as a **single LOGISTICS provider at 60%.**

**And after the Sejong correction, this port carries the country's most load-bearing import.** Bulk cargo —
**phosphate rock above all, which cannot be manufactured and never flies** — enters Tepenia **by sea.**
Marambio is the Palmer subnet's receiving node for it. **That is about as literal as the mandate test gets.**

### Commercial/trade 15% is NOT mandated

§15 annotates it *"leveraging both the airfield's and the port's connectivity"* — **the city profiting from
its position.** *(The Princess Elisabeth distinction: the mandate test asks what the nation needs FROM you,
not what you gain FROM WHERE YOU SIT.)* **The nation needs the port and the runway; it does not need
Marambio's traders to do well out of them.**

### On the half-technical split — precedent, not analogy

**Technical/maintenance 20% is bare and unannotated**, which normally triggers the Troll refusal. **But this
exact split has now been ruled by the developer on two cities of this exact shape** — **Belgrano** *(aviation
hub + port, "Technical/mechanical maintenance ~20%" → half)* and **Sanay** *(port + repair → half)*.
Marambio holds **both an airfield and shipyards**, both mandated, and the work keeping them running is
national by the same reasoning.

> **⚠ The honest counter, recorded:** the shipyards are **already inside the maritime 30%** — §15 names them
> explicitly, *"shipyards, dock loading and unloading."* **So some vessel-maintenance labor is counted there,
> and half of technical on top may be reaching.** **B leaves Marambio 17.6% free**, a narrow character budget
> for a city of 570,269.

### Notes

- **Hwy 1's ONLY inland main-line stop on the Peninsula**, reached by the **Picnic Passage causeway/bridge
  chain** *(Marambio → Snow Hill I. → James Ross I. → Prince Gustav Channel → Trinity Peninsula)*. Port
  Lockroy, Palmer City and Rothera are reached from ramps further along, **not from Marambio directly.**
- **⚠ Post-war, NOT an input — recorded as characterization only:** Marambio was destroyed by *a single
  strike that eliminated the airfield and shipyards together.* **Both halves of the node, one hit** — targeting
  that understood exactly what this city was.
- **⏸️ Still open from the Vision Notes:** the Marambio/Esperanza division of shipping labor *(bulk vs.
  specialty)*, unresolved since 2026-07-04. **Both are now determined and neither determination required it**,
  but it remains open for the city files.

---

## 13. ✅ PALMER CITY — DETERMINED *(⚠ on a self-declared non-canon §15 — see below)*

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=1.11, **GROWER** — Anvers Island, rock-founded, food term 100%)* | 97,747 | **39.1%** |
| **Mandated** | 63,377 | **25.4%** |
| **FREE — the character budget** | 88,728 | **35.5%** |

**Distinctive tier: 152,105 (60.9%).** §15: Entertainment/hospitality 35% · Commercial/trade 20% ·
Cultural institutions/arts 15% · Technical/scientific 10% · Marine/resource extraction 10% · Other 10%.

### The mandate *(developer ruling, 2026-09-02)*

| Share of distinctive | Workers | Sector | Basis |
|--:|--:|---|---|
| **35%** | 53,237 | **Entertainment/hospitality — FULL** | ✅ `04` §3 lists Palmer City a **HOSPITALITY provider at 35%** |
| **6.667%** | 10,140 | **Commercial/trade — ONE THIRD** | The tourism-attached slice: sealiner arrivals, money changing hands |
| **41.667%** | **63,377** | | |

> **This replaces the 0.0% that stood in Half B**, which recorded no mandate for this city at all.

### ⭐⭐ WHY — this city plausibly closes the open half of the Upper Earth trade question

**Two files that were never written together, describing one pipeline from opposite ends:**

| Source | What it says |
|---|---|
| **Palmer City Vision Notes** *(⚠ 2026-07-04)* | *"Economic model resolved: Palmer City runs substantially on **Upper Earth tourism** (casinos, nightlife) — public disdain, private indulgence. **This is a genuine partial answer to the Upper Earth trade justification question.**"* |
| **Juan Carlos canon** ✅ *(read this same pass, §10)* | *"Non-immigrant visitors routed to a separate corridor/sealiner to **Palmer City**."* |

> ### **The three-stage border system found at Juan Carlos is not an immigration system that happens to have a third stage. ITS THIRD STAGE IS AN INDUSTRY.**
> **Machu Picchu (arrival) → Juan Carlos (processing) → Palmer City (where the visitors actually GO, and spend).**

**And `14` resolved only half the trade question.** It established **why Upper Earth SELLS** Tepenia the
phosphate it cannot manufacture — leverage. ***What Tepenia PAYS WITH was left open.*** **Palmer City's
tourism is a direct candidate: it is how the nation earns what buys the phosphorus.** **That is national
provider work in the strictest sense the mandate test allows.**

**⏸️ Flagged, not closed:** this is a strong candidate for the export half, **not a ruling on it.** The
export question stays open until the developer rules on it directly.

### ⚠ FIRST CITY WHOSE §15 DISCLAIMS ITSELF

The source file states outright: *"Palmer City's economic foundations beyond entertainment/hospitality
remain TBD per its own Specs file — **this breakdown is a reasonable working estimate, not confirmed
canon.**"*

**Every other §15 in this pass has been ✅ canon. This one is not.** The 35% is soft in a way no other
city's figures have been — **so Palmer City's determination is provisional on different grounds than
everyone else's**, and should be revisited if the §15 is ever confirmed.

### Why only a THIRD of commercial/trade

**§15 annotates the sector as two things — *"subnet hub role, key Hwy 1 waypoint"* — and neither is a
mandate.** Per the standing rule established by the developer's Mawson correction, **hub status is
infrastructure, not provider work.** *(Palmer City is not even reachable by road: `Highways.md` L74, L79 —
a **ramp off Hwy 1 plus a BOAT CROSSING**, the only Hwy 1-adjacent city that cannot be reached by road
alone.)*

**But the sector must also handle the arriving tourists themselves** — the sealiner traffic, the trade that
exists only because visitors are there. **A third takes the tourism-attached slice without conscripting the
hub role.**

### ⭐ The cultural sector stays FREE — and emphatically so

**Palmer City is Tepenia's CULTURAL CAPITAL, and explicitly NOT its governmental one** *(Fort McMurdo;
Palmer City, Concordia and Lazar are all excluded from capital candidacy)*. Settled **June 21, 2564 — the
day the Falkland Treaty was signed**, the first Tepenian city. Founded by three groups united by
**relationship to robots, not nationality** — the only Tepenian city with no founding-nation-vs-majority
tension. **All 43 master-list nations present.** The jazz collection and the tattered Antarctica flag at
**100 Miles Davis Boulevard**, the first official address in Tepenia.

> **None of that is work the nation conscripts.** ***The free tier is exactly where a cultural capital's
> identity is supposed to live***, and a model that mandated it would be a worse model.

**Free in full:** arts 15% *(22,816)* · technical/scientific 10% *(15,210)* · marine 10% *(15,210)* ·
Other 10% *(15,210)* · **two-thirds of commercial/trade** *(20,281)*. **About 60% of Palmer City's free
budget is work with no relationship to Upper Earth at all.**

### Notes

- **⚠ Post-war, NOT an input:** destroyed, *"among the first and most thoroughly targeted cities of the Long
  Night War."*
- **⚠ The Long Night War's inciting incident happened here** *(⚠ Vision Notes, 2026-07-04)* — an Upper Earth
  diplomat, **in Palmer City for its tourism economy**, assaulted a gynoid who defended herself. **The
  mandated sector above is the reason he was in the city at all.** Her development is **developer-paused,
  flagged as requiring "the utmost care"** — deliberately not built on here.

---

## 14. ✅ PORT LOCKROY — DETERMINED

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=1.25, **GROWER** — Goudier/Wiencke I., rock-founded, food term 100%)* | 39,879 | **41.0%** |
| **Mandated** | 2,867 | **2.9%** |
| **FREE — the character budget** | 54,472 | **56.0%** |

**Distinctive tier: 57,339 (59.0%).** Canon §15: Maritime trade 30% · Heritage/cultural preservation 25% ·
Commercial/small trade 20% · Technical/maintenance 15% · Other 10%.

### The mandate

| Share of distinctive | Workers | Role | Basis |
|--:|--:|---|---|
| **5%** | 2,867 | **The courier node** — the Peninsula corridor's postal/parcel/archive transit point | ⚠ Vision Notes + ✅ Specs L105. **Developer ruling A, 2026-09-02** |

### The courier function is better established than the estimate that priced it

**Half B set 5% and rated it "✅ Solid." The rating was generous — but the FUNCTION is real, confirmed twice
and independently:**

| Source | Evidence |
|---|---|
| ⚠ **Vision Notes** *(developer-approved 250-year arc)* | ***"Rothera moves the materials; Port Lockroy moves the words"*** — correspondence, small parcels and **historical archive shipments** along the Peninsula corridor, *"fully functioning"* by the late Second Interwar |
| ✅ **`Specs/Port_Lockroy.md` L105** *(unmarked background lore, 2026-07-16)* | *"Port Lockroy's own **courier network-node** handled shipping for what became **Calethina**, Concordia's own activation-lab hologram."* **A named companion's components moved through this city.** |

### ⭐ Why 5% is right — the baseline already draws the line

**Baseline carries `D1 Transport & logistics` at 19 per 1,000 residents — every city's OWN local delivery.**
**Port Lockroy's mandate is therefore ONLY the inter-city node**: sorting and moving *between* cities, never
last-mile delivery anywhere. **A node is a small operation even when the network it serves is large.**

**For scale:** a full courier service across the Palmer subnet's **~4.13 M people** *(7 known cities, Rothera
excluded)* would run **4,100–6,200 workers** at real-world rates — **but almost all of that is local delivery
already sitting inside seven cities' baselines.** **2,867 for the node itself is proportionate.**

### What stays FREE, and why

- **Maritime trade 30%** — annotated *"leveraging the harbor's natural shelter."* **The city profiting from
  its geography** *(the Princess Elisabeth distinction)*. Port Lockroy also has **ramp access to Hwy 1**
  *(`Highways.md` L74, L79)* and is **not a food provider**, so nothing forces its shipping to be national
  work the way Signy's roadlessness does.
- **⭐ Heritage/cultural preservation 25%** — *"a genuine civic function inherited from the museum era."*
  **Same call as Palmer City's arts: identity, not provider work.** It is a very large sector for a city of
  128,887 — **and it should be.** Custodianship of **Tepenia's oldest standing structures** *(the 1944
  Operation Tabarin buildings, incorporated into the growing city and never demolished — a genuine
  architectural palimpsest)* **is what this city IS.**

### ⚠ A resolved question still marked TBD in three places — register item 13

**`Specs/Port_Lockroy.md` L112 and L134, and `Local_Cultures/Palmer_Subnet/Port_Lockroy.md` L248, all still
read:** *"whether the city maintained a post office as a functioning institution or a heritage artifact is
**TBD**."*

**It is not TBD.** Both the Vision Notes and the Calethina shipping lore settle it as **a genuine, active
civic institution.** **The resolution never propagated.** *(Not fixed here — culture-file corrections are
deferred until after the division-of-industry pass, consistent with the Sejong handling.)*

---

## 15. ✅ ROTHERA — DETERMINED *(closes the Palmer subnet)*

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=1.15, **GROWER** — Adelaide I., rock-founded, food term 100%)* | 93,804 | **39.0%** |
| **Mandated** | 73,382 | **30.5%** |
| **FREE — the character budget** | 73,382 | **30.5%** |

> **⭐ Mandated and free land EXACTLY equal — the mandate is precisely 50% of the distinctive tier.**

**Distinctive tier: 146,765 (61.0%).** Canon §15: Industrial/manufacturing 40% · Marine/resource extraction
20% · Aviation/logistics 15% · Technical/scientific 10% · Commercial/trade 10% · Other 5%.

### The mandate *(developer ruling, 2026-09-02)*

| Share of distinctive | Workers | Sector | Basis |
|--:|--:|---|---|
| **40%** | 58,706 | **Industrial/manufacturing — FULL** | ✅ `04` §3 **FABRICATION provider at 40%**; §15's *"clearly defining sector"* |
| **5%** | 7,338 | **Marine/resource extraction — ONE QUARTER** | Adelaide Island's terrain as feedstock for the fabrication chain |
| **5%** | 7,338 | **Aviation/logistics — ONE THIRD** | The Bonner airstrip's *"genuinely functional"* half |
| **50%** | **73,382** | | |

### The industrial 40% needs no judgment

§15: *"the city's clearly defining sector, **raw materials into finished infrastructure components**."* Canon:
those components are *"used across the whole subnet, plausibly reaching every subnet city including Palmer
City."* **The Palmer subnet's industrial center, listed as such in `04` §3.**

### ⭐ Why a QUARTER of marine, not the analyst's proposed half

**§15's annotation explains both halves of the sector's own name:** *"Marine / resource extraction: 20% —
Adelaide Island's mountainous terrain **and** maritime trade"* — *resource extraction* ← the terrain;
*marine* ← maritime trade. **The extraction half feeds the mandate**, since Adelaide Island is the subnet's
largest and most mountainous landmass *(~120 km, peaks >2,500 m)* and Rothera turns raw materials into
components.

**The analyst proposed HALF, on the Princess Elisabeth split rule. The developer ruled a QUARTER, which is
better:** **conceding that the island's extraction is *an* input to fabrication is not the same as claiming
the entire terrain half of that sector exists to feed it.** **120 km of mountains produces plenty that is not
feedstock for national infrastructure components.**

**⏸️ The case for the FULL 20%, recorded and not taken:** most of this subnet is islands — Signy, Sejong,
Juan Carlos, Palmer City, Port Lockroy — so **components physically cannot reach them except by ship**,
making maritime the mandate's delivery channel rather than general commerce. **Rejected because the same
argument would mandate the shipping of every coastal city in Tepenia, which would stop distinguishing
anything.**

### ⭐ Why a THIRD of aviation — a correction to the analyst's reading

**§15: *"Aviation/logistics 15% — the Bonner airstrip, secondary to the industrial role BUT GENUINELY
FUNCTIONAL."*** **The analyst read the first half of that annotation and left the sector entirely free.**

**The developer's third takes the second half seriously:** **a deliberately DECENTRALIZED industrial base
spread across 120 km of mountainous island needs internal air movement**, and Rothera holds **one of only ten
airports in the country** *(`Airports.md` L15 — the rare paved Bonner airstrip, 900 m, inherited from BAS)*.

**Two-thirds stay free**, consistent with canon calling it secondary — and with the fact that **heavy
infrastructure components do not fly.** Rothera's fabrication output leaves by the **Hwy 1 ramp** and by sea.

### Notes

- **Technical/scientific 10% — *"inherited BAS research tradition."*** **FREE**, the same call as Troll's
  Polar Institute and Sejong's KOPRI: local heritage research, nothing marking it load-bearing.
- **The Marambio–Rothera ramp is one of only FIVE Hitchhiking-Valid stretches in the national network**
  *(`Highways.md` L287)*.
- **⚠ Post-war, NOT an input:** Rothera survived via **genuine decentralization across Adelaide Island** plus
  **large-scale underground vault sections** — a resilience its concentrated small-island neighbors lacked.
  **The same decentralization is why the aviation third is defensible during peacetime.**
- **⚠ Vision Notes** establish Rothera's bar culture and place it in the **working-class Glitch-Coolant
  category** *(narrower selection, stronger effect)* — now project-wide canon in
  `Robot_Physiology_and_Cultural_Practices.md`. **Sits entirely in the free tier.**

---

# ▓▓ MIRNY SUBNET ▓▓

*Palmer subnet closed **complete, 8 of 8, no deferrals** — Signy · Sejong · Juan Carlos · Esperanza ·
Marambio · Palmer City · Port Lockroy · Rothera.*

---

## 16. ✅ SHIRAYUKI — DETERMINED

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=1.25, **GROWER** — Larsemann Hills, rock-founded, food term 100%)* | 363,971 | **40.9%** |
| **Mandated** | 105,222 | **11.8%** |
| **FREE — the character budget** | 420,886 | **47.3%** |

**Distinctive tier: 526,108 (59.1%).** Canon §15: Scientific/research 25% · Arts, music, fashion/cultural
institutions 25% · Education 20% · Commercial/trade 15% · Other 15%.

### The mandate

| Share of distinctive | Workers | Sector | Basis |
|--:|--:|---|---|
| **20%** | 105,222 | **Education** — the flagship university, drawing nationally | ✅ `04` §3 lists Shirayuki an `ARTS · EDUCATION` provider |

### ⭐⭐ THE ARTS SECTOR IS FREE — and this city is the PROOF CASE for the free tier

**`04` §3 and `16` disagreed about this city.** `04` lists the provider basis as *"arts/music/fashion 25%
(only city with arts as a major economic sector) **+** educ 20%"* — **both sectors.** `16` mandated only
education. **Ruled in `16`'s favor, 2026-09-02.**

**Canon is unusually explicit about why.** Shirayuki was founded by **Upper Earth diplomatic decree** — the
Jeju-do court allocating an empty site to Japan to block a third Chinese claim in the cluster. And:
***"explicitly, canonically NOT founded for art/music — no artistic or musical intention whatsoever."*** The
arts culture developed ***"entirely afterward, organically, over generations."***

> ### **A city grew a defining culture nobody planned, in a place chosen for geopolitics. That can only happen in labor nobody had claimed.**
>
> **The mandate test's own founding example was *"a stevedore is conscripted, a musician is not."*
> Shirayuki is that example at city scale.** Mandating the arts 25% would have the model assert that the
> nation conscripts Shirayuki's musicians — **contradicting the origin story canon is emphatic about.**

**The strongest counter, recorded not buried:** canon calls the music scene *"a genuine pre-war cultural
**EXPORT**"* — the same word that carried Princess Elisabeth's *mandated* energy expertise. **But PE's export
was expertise other cities TRADED FOR to keep the lights on. Shirayuki's is a reputation** — the Larsemann
Hills becoming *"nationally synonymous with Alternative Culture."* **The nation is poorer without it and not
MATERIALLY harmed. That is exactly the line the mandate test draws.**

### ⭐⭐⭐ DEVELOPER OBSERVATION — the free tier is the only tier that can CHANGE OVER TIME

> **2026-09-02:** *"Shirayuki was originally built without any disposition towards arts, but later developed
> the culture organically. So, in the early Second Interwar Period, no arts. Towards the middle- and later
> Second Interwar Period, definitely arts (and rather noticeably so). This isn't really a violation, because
> that can fit in the 'elective' category."*

**Correct, and it identifies something structural about the model that had not been stated anywhere:**

| Tier | Fixed by | Can it change across the 248-year period? |
|---|---|---|
| **Baseline** | Biology and population | **No** — it is what keeping people alive costs |
| **Mandated** | What the nation needs | **No** — not without the national picture itself changing |
| **FREE** | *Nothing* | **⭐ YES. This is where a city's history happens.** |

> **Shirayuki demonstrates it cleanly: SAME baseline, SAME mandate, for 248 years — and the free tier goes
> from "nothing in particular" to the thing the city is known for. No number moves; the CONTENT does.**
>
> **This means the model can hold a city that BECAME something, without needing separate early-period and
> late-period versions of it.** *(General finding — applies to every city, recorded here because Shirayuki is
> where it surfaced.)*

### Notes

- **⚠ The mandate partly exists to feed the un-mandated sector.** Canon: students use the university *"as a
  deliberate stepping stone toward eventually integrating into and becoming part of the local arts and music
  culture."* **Shirayuki's one conscripted sector is, in part, a pipeline into its free one.**
- **Scientific/research 25% stays FREE** — *"genuine institutional depth supported by the calm setting,"*
  nothing marking it nationally load-bearing. *(Contrast within this same subnet: Vostok's Lake Vostok program
  at 65%, Kunlun's astronomy at 60%.)*
- **Commercial/trade 15% is the Tri-Cities cluster economy** with Sinheung and Zhongshan — regional, not
  national. **FREE.**
- **⚠ Hard canon rule observed:** the real-world basis is the Bharati site, **but no Indian or South Asian
  population ever settled in Tepenia.** Founding population is Japanese, by the Jeju-do allocation.
- **⏸️ Open:** whether the region-wide *"Alternative Culture"* reputation belongs to Shirayuki alone or
  genuinely extends to Sinheung and Zhongshan — **deliberately left open pending both cities**, and both are
  still ahead in this subnet.

---

## 17. ✅ SINHEUNG — DETERMINED

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=1.25, **GROWER** — Larsemann Hills, rock-founded, food term 100%)* | 329,374 | **40.7%** |
| **Mandated** | 228,180 | **28.2%** |
| **FREE — the character budget** | 252,199 | **31.2%** |

**Distinctive tier: 480,380 (59.3%).** Canon §15 *(revised 2026-07-06, vision session)*: Industrial
fabrication 45% · Technical/scientific 15% · Commercial/trade 15% · Marine/resource extraction 10% ·
Diplomatic/inter-community 10% · Education/other 5%.

### The mandate *(developer ruling C, 2026-09-02)*

| Share of distinctive | Workers | Sector | Basis |
|--:|--:|---|---|
| **45%** | 216,171 | **Industrial fabrication — FULL** | ✅ `04` §3 **FABRICATION provider**; the corpus's highest single sector |
| **2.5%** | 12,010 | **Half of Education/other — the Institute** | ✅ One of only **three** national medical/care institutes |
| **47.5%** | **228,180** | | |

### ⭐⭐ The fabrication 45% may be the most load-bearing single sector in Tepenia

**216,171 workers — the highest single sector in the entire Division-of-Industry corpus.** What it makes:

> ***"Fabrication-synthesis chambers… the actual apparatus that creates robots"*** — shipped nationwide, so
> that ***"a robot can be 'born' (built) in any Tepenian city regardless of whether that city has its own
> chamber-manufacturing capability."***

**In a country with a robot majority, this is where robots come from.** **Sinheung and Byrd are the only two
cities that make them.** *(Mountain Pass was the historical third, dark since the Tower fell.)* **Mandated
without argument.**

**⭐ And built to a schematic designed elsewhere** — the **Mark IV, designed at Neumayer.** Sinheung's own
canon calls its founding tension *"Claimed, Not Found"*: legitimacy **continuously reproven through output,
never simply settled.** **The city that makes the nation's robots does it to another city's drawing, and
guards the archive of it.**

### ⚠ A CORRECTION to this file's own Institutes ruling, made the same day

**The Institutes ruling *(§ "the Institutes do NOT get their own sector")* placed Sinheung's Institute in
Industrial fabrication 45%. That was imprecise, and the row above is now corrected.**

`National_Medical_and_Care_Institutes.md` says: *"**Why Sinheung.** Its §15 carries the corpus's highest
single sector — Industrial fabrication: 45% — and it manufactures the Cradle chambers."* **That explains why
the CITY hosts the Institute. It does not say which sector employs its staff.** An institute teaching *"the
physical AND emotional care of, and for, robots — **not a repair school**"* is staffed by **educators**, and
§15 has an education line.

> **The distinction to keep: WHY A CITY HOSTS SOMETHING ≠ WHICH SECTOR PAYS FOR IT.**
> **The Institutes ruling itself stands** — three institutes, three different host cities, no shared sector.

### Why HALF of Education/other, not all

**The Institute is the sole source of trained robot-care personnel nationwide** — unambiguously national
provider work, and it was getting **zero** mandate. **But `Education / other` is a combined bucket**, and
mandating all of it would conscript the *"other"* alongside the school.

> **⚠ Honest caveat: the Institute has NO established headcount.** Esperanza's is ~3,150 and Belgrano's
> ~1,750; `National_Medical` says Sinheung's throughput is *"much smaller than the robot share of the
> population suggests — it replaces people who changed their minds, not people who died,"* since robot
> career turnover is **voluntary rather than mortality**. **So 12,010 probably overstates it — but the sector
> granularity does not go finer, and zero understates it worse.**

### What stays FREE — all on established precedent

| Sector | Why free |
|---|---|
| **Diplomatic/inter-community 10%** | *"A genuine sector given the cluster's density"* — **points inward**, exactly like Sejong's |
| **Technical/scientific 15%** | *"Inherited Arctic and Antarctic Research Institute tradition"* — heritage research, as at Troll, Sejong, Rothera |
| **Commercial/trade 15%** | The Tri-Cities cluster economy |
| **Marine/resource extraction 10%** | *"Prydz Bay maritime access."* ⭐ Note Sinheung's raw materials arrive **by truck from Mirny** *(via the Hwy 110/Hwy 4 tri-junction at Zhongshan)*, **not by sea** — so its maritime is not the fabrication chain's input |

### Notes

- **⭐ The Institute is not only a school — it once moved national infrastructure.** The **Mountain Pass**
  outpost *(the historical third chamber site, on Hwy 37 between Vostok and Kunlun)* **began as an act of
  solidarity pushed for by this Institute** `[CGRM 2026-09-01 · Path 6]`. Sinheung supplied the means; Vostok
  and Kunlun staffed it. **The 2.5% mandated above is the descendant of the sector that did that.**
- **⚠ Hard canon:** physical infrastructure from Russia's Progress Station, but **the founding population is
  Korean**, via Jeju-do decree — **Russia was never a founding claimant.**

---

## 18. ✅ ZHONGSHAN — DETERMINED *(replacing a withdrawn estimate)*

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=1.25, **GROWER** — Larsemann Hills ice-free oasis, food term 100%)* | 396,635 | **41.2%** |
| **Mandated** | 148,786 | **15.4%** |
| **FREE — the character budget** | 418,019 | **43.4%** |

**Distinctive tier: 566,805 (58.8%).** Canon §15: Technical/scientific ~35% · Industrial/manufacturing ~25% ·
Marine resource extraction ~15% · Commercial ~15% · Education ~7% · Other ~3%.

### The mandate *(developer ruling, 2026-09-02)*

| Share of distinctive | Workers | Sector | Basis |
|--:|--:|---|---|
| **26.25%** | 148,786 | **Technical/scientific — THREE QUARTERS of the 35% sector** | ✅ §15's own export clause |

> **Developer:** *"Science and Technology is fundamentally Zhongshan's identity, although granted, it is not
> as though everybody in the city is a scientist and/or technician (because cities need other people doing
> other jobs, as well). So, I would say somewhere in that range between 38 to 48% is fine."*
>
> **That 38–48% band is the FREE tier**, and it is exactly the span between the analyst's option B *(half
> technical → 48.5% free)* and option C *(full technical → 38.2% free)*. **Three-quarters lands at 43.4% —
> the midpoint.**

### ⚠⚠ THE WITHDRAWN ESTIMATE — a fabricated quote, and how it got here

**Half B listed Zhongshan as `MARITIME LOGISTICS — the Tri-Cities' port` at 20%, citing §15 as saying:**
*"Prydz Bay maritime logistics… cluster economy with Sinheung."*

> ## **That quote does not exist.**

**Zhongshan's actual §15 says the opposite in two places:**

| Half B claimed | §15 actually says |
|---|---|
| *"Prydz Bay maritime **logistics**"* | *"Marine resource extraction: ~15% — **Prydz Bay FISHING** and related industries"* |
| *"cluster economy with Sinheung"* | **This is SINHEUNG's annotation, not Zhongshan's** |
| A port role at 20% | *"Commercial: ~15% — more modest than a city like Janbogo; **Zhongshan is NOT a trade hub**"* |

**Provenance, per the developer 2026-09-02:** *"That quote… was written by another iteration of Claude using
the Sonnet model (which just interjected it without my say-so, probably based on an assumption from several
different statements I made)."* **It was never developer-approved.** **All three sites where it propagated in
this file are struck above.**

> ### ⭐ **And the distinction it teaches is worth keeping.**
> **At Sanay, Sejong and Juan Carlos, §15 was SILENT about a national function — a gap, which invites
> inference. Here §15 makes a STATEMENT: *"not a trade hub."* Silence invites inference; denial forecloses
> it.** **The estimate did not fill a gap; it overrode a fact.**

**Sinheung's own determination had already contradicted the premise an hour earlier:** its raw materials
arrive *"by truck from Mirny via the Hwy 110/Hwy 4 tri-junction at Zhongshan,"* **not by sea.**

### ⭐⭐ NEW CANON — the chambers do not travel by sea

> **Developer, 2026-09-02** `[CGRM 2026-09-02 · Path 6]`: ***"There's enough highway access connecting at the
> Tri-Cities (namely Hwy 4, Hwy 22, and Hwy 110, specifically, as well as a nearby airport) that shipping
> robot-synthesis/manufacture chambers via the ocean is not necessary."***

**Fabrication-synthesis chambers move by ROAD and AIR.** Three highways converge at the tri-junction —
**Hwy 4, Hwy 22 and Hwy 110**, with Zhongshan as **Hwy 110's own northwest terminus** — plus **the Tri-Cities
Airport** *(`Airports.md` L13, shared by all three cities)*. **This settles how Sinheung's national output
reaches the country, and it closes the maritime question for the whole cluster.**

### What the national role actually is

**§15's largest sector states it outright:** *"Technical/scientific: ~35% — the research heritage is
continuous from the founding station; **Zhongshan produces engineers and researchers who end up across
Tepenia**."*

**An export clause inside the annotation itself** — the same shape as Princess Elisabeth's *"expertise other
cities traded for."* ***Zhongshan's national contribution is PEOPLE, not cargo.*** **The analyst proposed
half on the Princess Elisabeth split; the developer ruled three-quarters, on the grounds that science and
technology is not one half of this city's character but the whole of its identity — bounded only by the fact
that a city still needs people doing other things.**

### What stays FREE

- **Industrial/manufacturing 25%** — *"precision manufacturing, with the craft ethic applying to industrial
  output as much as to art."* **No stated national reach.**
- **Marine 15%** — **fishing**, and `04` §3 does **not** list Zhongshan among the national fish providers.
- **Commercial 15%** — **denies itself:** *"Zhongshan is not a trade hub."*
- **Education 7% · Other 3%** — local.
- **⚠ The three-highway junction is NOT mandated.** **A crossroads is not automatically an employer** — canon
  already treats the **Sayowa Junction** as separate from Sayowa the city — and §15's *"not a trade hub"* is
  an explicit denial rather than an omission.

---

## 19. ✅ DAVIS — DETERMINED *(⚠ Option B, flagged for post-pass review)*

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=1.25, **GROWER** — Vestfold Hills, the largest ice-free coastal oasis in Antarctica, ~400 km²)* | 357,063 | **40.7%** |
| **Mandated** | 246,740 | **28.2%** |
| **FREE — the character budget** | 272,712 | **31.1%** |

**Distinctive tier: 519,452 (59.3%).** Canon §15 *(developer vision 2026-07-05, revised 2026-07-16)*:
Agricultural/food production ~35% · Technical/scientific ~25% · Maritime ~15% · Commercial ~15% ·
Industrial ~5% · Other ~5%.

### The mandate *(developer ruling B, 2026-09-02 — provisional, see review flag)*

| Share of distinctive | Workers | Sector | Basis |
|--:|--:|---|---|
| **35%** | 181,808 | **Agricultural/food production — FULL** | ✅ `04` §3: *"FOOD — agriculture 35% — 'the breadbasket,' **explicitly national**"* |
| **12.5%** | 64,932 | **Technical/scientific — HALF** | The Signy precedent, applied on land — see below |
| **47.5%** | **246,740** | | |

### ⭐ The research half — the Signy precedent applied on land

**§15: *"Technical/scientific: ~25% — environmental, ecological, and limnological research — the founding
research heritage, now a CO-EQUAL PILLAR ALONGSIDE AGRICULTURE rather than a shrinking minority."***

**Everywhere else in this pass, *"founding research heritage"* has marked a sector FREE** — Troll's Polar
Institute, Sejong's KOPRI, Rothera's BAS, Sinheung's AARI. **This annotation does not stop there.** It names
a **second** thing — *co-equal pillar alongside agriculture* — **explicitly tying the research to the
mandated sector.**

> **The developer already ruled this exact shape at Signy** *(§8)*: half its biological/ecological research
> mandated, because ***the fishery is capped and somebody has to know where the cap is.***
>
> ### **Davis is the same argument on land, and stronger.**
> **This session's entire food rebuild is agricultural science, and Davis is where it would be done:** the
> **1,500 km² terraformed belt** *(`12`)*, **engineering *Deschampsia antarctica*** and the **imported-grass
> comparators the developer ruled on**, the **fungi tier**, the **livestock tier** *(`11`)*. **The Breadbasket
> is not only where the food grows — it is where the growing is figured out.**

**HALF, not full**, because the annotation genuinely names both a local heritage and a national pillar — the
**Princess Elisabeth split**, applied to a sector where **both halves are real.**

### What stays FREE

- **Maritime 15%** *(Prydz Bay, fjord access)* — **considered for the mandate and rejected.** Davis's produce
  must reach the country, but **Davis sits on the `Hwy 110` (Coastal Cut Highway) main line** between
  Zhongshan and Mirny *(`Highways.md` L195, L197)*, so **it is not dependent on its own
  shipping** — and the cluster's output moves **by road and air** per the 2026-09-02 ruling at Zhongshan.
- **Commercial 15%** — *"bars, eateries, social establishments."* Local amenity. **⭐ Worth pairing with the
  robot-culture finding that Davis has NO drinking-culture institution at all** — *"a genuine muted absence…
  consistent with the 'let the work speak' ethos."* **The bars exist; the culture around them does not.**
- **Industrial 5%** *(non-mining, general)* — **the mining/quarrying role was reassigned to Mirny, 2026-07-16**,
  to resolve a direct conflict with the breadbasket identity.
- **Other 5%**, including *"a small but genuine arts/music community."*

### ⚠⚠ REGISTER ITEM 11 IS LIVE IN THIS CITY'S OWN PUBLISHED NUMBERS

**`04` §3 states: *"Davis alone: 306,780 producers ÷ 15,623,523 = 1 per 51."*** That is **35% of the WHOLE
WORKFORCE.** **`16`'s convention gives 181,808** — 35% of *distinctive*.

> **Same sector, same city, 124,972 workers apart — and `04` built a memorable national ratio on the larger
> figure.** **The clearest instance yet of why the denominator must be settled in the end-of-pass re-run.**

### Notes

- **⭐⭐ Geology is the whole story here.** The **Vestfold Hills are the largest ice-free coastal oasis in
  Antarctica (~400 km²)** — Davis *"can grow, and grows more than anyone."*
- **Named for John King Davis, a ship's captain** — *"a navigator and enabler, not a flag-planter."*
  **Explicitly NOT a Tepenian Saint** *(Saints are pre-2083 explorers, not supporting mariners)*.
- **⭐ Kinship is collective research credit, not teaching lineage** — a founding-era decision to decline solo
  credit set the norm. **A robot's "family" is whoever she shares discovery-credit with.** *(Sits directly on
  top of the half-mandated research sector.)*
- **Human-majority reversal** — 437,423 H / 344,173 R at Census II, rare in this corpus.

---

## 20. ✅ MIRNY — DETERMINED

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=1.25, **GROWER** — four rock outcrops at Mabus Point, food term 100%)* | 418,565 | **41.1%** |
| **Mandated** | 239,966 | **23.6%** |
| **FREE — the character budget** | 359,949 | **35.3%** |

**Distinctive tier: 599,914 (58.9%).** Canon §15: Communications/Arcanet ~20% · Technical/scientific ~20% ·
Industrial/manufacturing ~20% · Maritime ~15% · Commercial ~15% · Other ~10%.

### The mandate *(developer ruling C, 2026-09-02 — "there's not even a question about it")*

| Share of distinctive | Workers | Sector | Basis |
|--:|--:|---|---|
| **20%** | 119,983 | **Communications/Arcanet infrastructure — FULL** | ✅ §15: *"an unusually large sector, reflecting Mirny's unique subnet-hub role"* |
| **20%** | 119,983 | **Industrial/manufacturing — FULL** | ✅ §15's own vision note — see below |
| **40%** | **239,966** | | |

### ⭐⭐ Canon ruled the industrial sector in its own words

**Half B mandated only the Arcanet 20%. The §15's own developer-vision note ends by stating its conclusion
outright:**

> ***"Two distinct quarrying-to-manufacturing chains running through the same industrial core, giving Mirny's
> ~20% Industrial/manufacturing sector share genuine claim to 'top-tier industrial hub' status AT THE
> NATIONAL SCALE, NOT JUST THE SUBNET SCALE."***

**This was not an inference to be drawn. It was a conclusion already written down and not yet applied.**

### The two chains

| Chain | Route | Established |
|---|---|---|
| **1** | **Quarries south toward the continental interior → Mirny's industrial yards → SINHEUNG**, where the material is fabricated into **robot-synthesis chambers**. Canon: ***"near-exclusive"*** | **Reassigned 2026-07-16**, resolving the Davis mining/breadbasket tension — *"previously misattributed to Davis"* |
| **2** | Same quarries → the yards → **construction materials for the eastern highways** *(toward Casey and, via Hwy 110's spur, Concordia)* **+ the machinery that builds and maintains the subnet's infrastructure** | Developer vision, **2026-07-05** — *"the subnet's construction engine"* |

**Both named uses are provider work. Nothing in the sector is described as discretionary.** Canon's own
framing: *"Mirny didn't just administer the subnet's communications hub — **it built the subnet's own roads
and the equipment that maintains them.**"*

### The Arcanet 20%

**Already mandated in Half B, and it stands.** §15 calls it *"an unusually large sector, reflecting Mirny's
unique subnet-hub role"* — **routing Zhongshan, Casey, Davis, Vostok and Kunlun to each other** *(and
explicitly **not** to Concordia, a different subnet, severed by the Split Brain)*.

### What stays FREE

- **Technical/scientific 20%** — *"inherited Soviet/Russian institutional research capacity."* Heritage
  research, on the standing precedent for that annotation.
- **Maritime 15%** — **in neither chain.** The quarries are **inland to the south**, the material arrives by
  truck, and the output moves by road. *(Chambers travel by road and air per the 2026-09-02 ruling.)*
- **Commercial 15% · Other 10%** — local.

### Notes

- **⭐ "The Threshold."** Mirny sits within seconds of arc of the **exact Antarctic Circle** — minimal polar
  night AND minimal midnight sun, ~4–5 days each, the sun grazing the horizon without fully rising or
  setting. **Canon calls this the city's central symbolic and civic fact.**
- **Among the windiest coastal stations in Antarctica** *(sustained events >40 m/s)*. **The city is
  architecturally built as its own windbreak** — concentric rings, dense, **residential woven into the
  industrial core rather than separated.** *(The mandated sector is physically inside where people live.)*
- **⭐ Robot kinship is the shared everyday condition of living inside the windbreak ring** — home and shelter
  barely distinguishable — **not a founding incident.**
- **⚠ Flagged for an eventual rename**, unresolved: the national composition *(China Primary 24.24%; Russia
  only Significant 7.22%)* no longer matches the Russian ship and station the name and founding legend are
  built around.

---

## 21. ✅ CASEY — DETERMINED

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=1.11, **GROWER** — Bailey Peninsula-adjacent, Wilkes Land coast)* | 436,698 | **38.7%** |
| **Mandated** | 207,641 | **18.4%** |
| **FREE — the character budget** | 484,495 | **42.9%** |

**Distinctive tier: 692,136 (61.3%).** Canon §15: Transit/logistics/resupply ~30% · Commercial ~20% ·
Technical/scientific ~15% · Maritime ~15% · Industrial/manufacturing ~10% · Other ~10%.

### The mandate *(developer ruling A, 2026-09-02)*

| Share of distinctive | Workers | Sector | Basis |
|--:|--:|---|---|
| **30%** | 207,641 | **Transit/logistics/resupply — the junction economy** | ✅ `04` §3 **LOGISTICS provider**; §15's *"the dominant sector, reflecting the junction economy directly"* |

### ⭐ This city clears the crossroads test on its own §15's terms

**A standing principle established earlier in this pass: *a crossroads is not automatically an employer*** —
geography that goods pass through does not necessarily buy labor.

**Casey clears it because its §15 ASSERTS the sector rather than leaving it to inference:**
`Transit / logistics / resupply: ~30%`, annotated ***"reflecting the junction economy directly."***

**And the geography is unusually load-bearing.** Casey is **where Hwy 2 BEGINS** *(its western end is
literally "junction with Hwy 110")*, and **Hwy 110 runs THROUGH the city, not past it**
*(`Highways.md` L56, L89, L197)*.

> **The proof is in what happened when it stopped:** *"Casey's destruction **severed Hwy 2/DCH at the
> source** — the route runs directly through the city; **Dumont d'Urville's overland connection survives only
> via a much longer, more dangerous Hwy 183 detour.**"*
>
> **A junction whose loss re-routes another city's entire land access was doing national work.**

### ⭐⭐ Why commercial 20% stays FREE — the city's defining fact lives there

**The mandated sector's own name already contains *RESUPPLY*** — the work of servicing what moves through is
**counted there.** **Commercial 20% is the city earning from its position**, the distinction that has kept
commercial sectors free throughout this pass.

**And Casey's identity is in that sector.** It holds **Splinters** — canon's own words: *"Tepenia's largest,
most famous bar, a full city block, Classic Rock/Jazz/Blues/Acoustic Folk, famous along the whole Dumont
d'Urville Sea coast"* — revived from **real pre-exile historical records of the actual Casey Station's own
social bar.**

**The Enneagram read was flagged as sitting *"in real tension with the 'quiet, function-first' framing"*
dominant elsewhere in Casey's own sheet — and resolved in favor of the LOUD SPLINTERS REGISTER as Casey's
actual defining fact, rather than smoothed over.**

> **Mandating that sector would put the city's defining fact in the conscripted column.**

### What else stays FREE

- **Technical/scientific 15%** — *"inherited Australian Antarctic Division capacity."* Heritage research.
- **Maritime 15% · Industrial 10% · Other 10%** — nothing marks them national.

### Notes

- **⭐ A threshold city:** sits **just north of the Antarctic Circle** — the sun never fully sets, but winter
  days shrink to **~5 hours.**
- **⭐ Robot kinship is the shared, ongoing condition of *being the last stop*** — a repeating daily rhythm
  rather than a converging settled community. **Glitch-Coolant here fits neither canon category: its variety
  is TRANSIENCE-DRIVEN**, tracking whichever traveler population is passing through in concentration.
  **Both sit in the free tier.**
- **⭐ The founding creed is explicitly anti-mythologizing** — from the Wilkes-excavation-abandonment
  incident: ***"buried things are curiosities, not destinations."*** **Post-war, Casey is now exactly that
  kind of thing.** Canon flags the irony as questline material; **it sits entirely in the free tier.**
- **⚠ Post-war, NOT an input:** destroyed in the Long Night War. **Timing within the war — early strategic
  target or late survivor — remains unresolved.**
- **Wilkes Station ruins** *(a genuine pre-exile American research site, never Tepenian)* sit nearby as a
  curiosity.

---

## 22. ✅ KUNLUN — DETERMINED *(⚠ flagged for post-pass review — register item 15)*

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=2.70 — highest in the roster — **but 0 humans**, so the human-keyed term is zero)* | 35,306 | **28.6%** |
| **Mandated** | 33,054 | **26.8%** |
| **FREE — the character budget** | 55,089 | **44.6%** |

**Distinctive tier: 88,143 (71.4%).** Canon §15: Astronomy 60% · Ice core science 15% · Religious
practice/pilgrimage infrastructure 15% · Altitude-legacy medical infrastructure/facility maintenance 10%.

### The mandate *(developer ruling, 2026-09-02 — provisional)*

| Share of distinctive | Workers | Sector | |
|--:|--:|---|---|
| **30%** | 26,443 | **Astronomy — HALF** | ½ of 60% |
| **7.5%** | 6,611 | **Ice core science — HALF** | ½ of 15% |
| **37.5%** | **33,054** | | |

> **Both of Kunlun's scientific sectors split down the middle — half of each doing work the country needs,
> half doing work the city does because that is what it is.**

### ⭐ A structural note: highest difficulty, lowest baseline share

**Kunlun carries D = 2.70, the highest in the roster, and a baseline of only 28.6%, the lowest.** **Not a
contradiction.** With **zero humans**, the entire human-keyed term *(food, health, schooling, childcare,
mortuary — `120.7·f·D + 85.6` per 1,000 humans)* **is multiplied by zero.** ***Difficulty only scales costs
there is nobody to spend on.*** **The free tier is 71.4% of distinctive because robots do not eat.**

### Why astronomy is half, not zero — revisiting Half A

**Half A ruled astronomy discretionary** — *"genuinely world-class, but not something the nation would starve
without."* **The §15 itself records a developer follow-up that changes the reading:**

> *"**Follow-up, 2026-07-06:** the developer isn't certain of an exact research focus, but leans toward
> Kunlun's observatory work concentrating more on **near-Earth objects of interest — Mars, the Moon, and
> similar** — than on distant star systems."*

**Tepenia has millions of people in orbit, and during the Second Interwar they are still arriving via
Amundsen Tower.** A nation with a large and growing orbital population **needs someone watching near-Earth
space.** Kunlun is *"potentially the best ground-based observatory site in Tepenia,"* and its robot-culture
file notes it is **the one city capable of reaching orbital structures directly.**

> **Cataloguing distant stars is discretionary. Tracking near-Earth space for an orbital population is not.**

**⚠ That focus is explicitly TENTATIVE** — *"the developer isn't certain… Tentative, not firmly settled."*
**Half rather than full is partly a hedge against building on an unsettled premise.**

### Why ice core is half, not zero

**Under-argued by the analyst as "pure science," and corrected.** ***Tepenia is a nation that lives on and
inside ice.*** Concordia sits on 3+ km of it, Halley is built to move across a floating shelf, Byrd was
founded underground in it, and `13` §14 split all 37 cities on exactly that question. **Dome A holds some of
the oldest ice on Earth — Kunlun is where the ice sheet's own behavior is read.** **The half-split keeps the
paleoclimate-for-its-own-sake portion free.**

### What stays FREE

- **Religious practice / pilgrimage 15%** — **Kunlun is Ice Cold Buddhism's holiest site in Tepenia**, above
  even Dome Fuji, on the combination of highest elevation, coldest sustained environment, calmest winds and
  atmospheric purity. **Devotional practice is character, not conscription.**
- **Altitude-legacy medical / facility maintenance 10%** — local survival at 4,093 m.
- **The un-mandated halves of both science sectors** — 26,443 + 6,611.

### ⭐⭐ The reason the free tier is deliberately kept large

> **Developer, 2026-09-02:** *"Having a 44% free budget would allow for other scientific research that I may
> not have thought of."*

**This is the free tier used as DESIGN HEADROOM rather than as a residue** — the same property recorded at
Shirayuki *(the free tier is the only tier that can change over the period)*, applied forward instead of
backward. **A science city whose science is fully conscripted has no room to discover anything the design has
not already specified.**

### Notes

- **⭐⭐ The strongest cross-reference finding of the entire 8-city robot-culture run sits in the free tier:**
  robots' own sensory apparatus gives them something closer to **direct physical access to the stillness Ice
  Cold Buddhism venerates** than a human devotee could ever have — *"the first finding in the whole
  methodology where robot embodiment itself is the load-bearing mechanism of a devotional experience, not an
  inflection on a human-originated one."*
- **⭐ A ready-made irony, canon's own:** Kunlun's symbolic Element is **Air** *(breath, communication)* — yet
  it is **the single most Arcanet-disconnected city in Tepenia** and simultaneously **the one city capable of
  reaching orbital structures directly.**
- **Human presence is FORBIDDEN by settled protective policy**, not attrition — altitude and cold would be
  fatal to humans, harmless to robots *(ruled 2026-07-05)*.
- **Population is NOT single-nation Chinese** *(re-resolved 2026-07-06)* — a **deliberately curated 19-nation
  astronomy/comms-heritage population**, tiered by real-world space-program credentials.
- **⏸️ Open, and flagged in canon as a REQUIRED DLC story deliverable:** the observatory's **five centuries of
  findings** — not yet designed.

---

## 23. ✅ VOSTOK — DETERMINED *(closes the Mirny subnet)*

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=2.50, **ICE-SHEET FORCED IMPORTER** — bedrock ~4 km down under Lake Vostok, food term at 10%)* | 121,353 | **37.4%** |
| **Mandated** | 66,007 | **20.3%** |
| **FREE — the character budget** | 137,092 | **42.3%** |

**Distinctive tier: 203,100 (62.6%).** Canon §15: Science *(Lake Vostok research program)* 65% ·
Self-sufficiency/survival infrastructure 25% · Other 10%.

### The mandate *(developer ruling B, 2026-09-02)*

| Share of distinctive | Workers | Sector | |
|--:|--:|---|---|
| **32.5%** | 66,007 | **Science — HALF of the 65% sector** | The Kunlun treatment: a dominant science sector at an extreme site, split down the middle |

### ⭐ The previous 9.2% was a FLOOR, not an assessment

**Half B's mandate came from the reciprocal-obligation work:** Vostok owes **18,774 food-worker-years** as a
geologically forced importer, and its ruled export — **scientific research, the bioinformatics /
Cryptograph Helix basis** — was set at ***"minimum 9.2% of distinctive tier."***

> **That figure was sized to match the DEBT, not to measure the SECTOR'S NATIONAL ROLE.** **It was a floor,
> and it was never revisited.**

### ⭐⭐ The national argument, beyond the debt

**Tepenia is a CLOSED POPULATION** — one-way exile, no meaningful inflow, sustained across ~250 years by
**artificial wombs**. ***Accumulated mutation and genetic drift in a closed gene pool of ~15 million is a
real biological problem*** — and Vostok's research sits exactly there. Canon gives it **DNA computing /
bioinformatics** as the ruled export, and **Charlene (XT-17)**'s *"reduced-mutation-rate breakthrough tied to
Lake Vostok biology."*

> **Cataloguing a sealed lake is discretionary. Understanding mutation rates in a closed human population is
> not.**

**⚠ Scope caution, recorded:** **Charlene's breakthrough is DLC-present.** During the Second Interwar the
**PROGRAM** exists; the **RESULT** may not have landed yet. ***The mandate rests on the program, not on the
discovery.***

### Self-sufficiency / survival 25% stays FREE

*"Required simply to remain viable at the single most extreme location in Tepenia."* **Local survival, not
provider work** — the same disposition given to Princess Elisabeth's wind engineering, **and the same
oddity: it is the least discretionary work in the city and still not national.**

### ⭐ What the ruling does to Vostok's standing

**At the 9.2% floor, Vostok's export exactly matched what it owed** — a city that barely paid its way. **At
half science, the mandate covers the food debt roughly 3.5× over.**

> **Vostok becomes a net contributor rather than a break-even one** — which fits a place whose research
> archive canon describes as ***"too vast for any single mind, human or robot, to hold."***

### Notes

- **⭐ Holds the coldest naturally-recorded surface temperature on Earth** *(−89.2 °C, 1983)*, and sits above
  **Lake Vostok — sealed 15–25 million years, 4 km down.**
- **⭐⭐ The founding-legend mismatch is DELIBERATELY UNRESOLVED:** the founding population was Russian; the
  current population *(USA/Japan Primary, **zero Russian representation at any tier**)* has **no documented
  connection** to them, and **no migration event explains it** — *"ambient, settled fact"* per its own §5a.
  **Russian survives only as a *"liturgical language of science"* — fixed technical identifiers, spoken by
  nobody, understood by all serious researchers.** *(All in the free tier.)*
- **⭐ Robot kinship is archive-domain inheritance across researchers who may never overlap in time** — canon
  calls it *"the most purely condition-based kinship finding"* in the whole run. **The public/private divide
  is organized by TIME, not space** — *"Window Courtesy."*
- **⏸️ Charlene (XT-17)** — robot geneticist, **confirmed recruitable companion, DLC 7 central character.**
  **Vostok is the mandatory launch point for Kunlun's DLC content** *(her discovery needs Kunlun's comms
  relay)*.
- **Not a roadside node:** Vostok sits on **Hwy 37** between Mountain Pass and Concordia, but **the highway's
  only stopping place on that stretch is Mountain Pass** — canon calls this **the single hardest route in
  Tepenia to hitchhike.**

---

# ▓▓ JANBOGO SUBNET ▓▓

*Mirny subnet closed **complete, 8 of 8, no deferrals** — Shirayuki · Sinheung · Zhongshan · Davis · Mirny ·
Casey · Kunlun · Vostok.*

---

## 24. ✅ DUMONT D'URVILLE — DETERMINED

| Tier | Workers | Share |
|---|--:|--:|
| **Baseline** *(D=1.67, **GROWER** — Petrel Island, Géologie Archipelago)* | 163,966 | **48.0%** |
| **Mandated** | 14,799 | **4.3%** |
| **FREE — the character budget** | 162,794 | **47.7%** |

**Distinctive tier: 177,593 (52.0%).** Canon §15: Marine/resource extraction 25% · Technical/scientific 25% ·
Commercial 20% · Industrial/manufacturing 15% · Education 8% · Other 7%.

### The mandate *(developer ruling B, 2026-09-02)*

| Share of distinctive | Workers | Role | Basis |
|--:|--:|---|---|
| **8.33%** *(⅓ of marine 25%)* | 14,799 | **The food share of the marine sector** | ✅ `04`'s national food supply tally already counts it |

> **This replaces the 0.0% that stood in Half B.**

### ⭐ Why 0% was honestly reached — and why it still had to change

**Half B set 0.0% by taking the city's own Spec at its word:** *"its economic significance was **more cultural
and historical than industrial**."* **That was the right instinct — not every city has to have a national
role, and inventing one would have been worse.** **But two canon facts sit against a clean zero:**

**1. `04`'s national food tally ALREADY COUNTS this city.** Its supply table lists *"Dumont d'Urville ·
marine 25%, ~⅓ food · **28,463**"* — and that figure sits **inside the ~835,000 total** that produces the
model's headline ***"1 food producer per ~19 people."***

> **Remove it and the ratio becomes 1 per 19.4.** **Not fatal — but the national balance was leaning on food
> this city was not being credited with producing.** ***Leaving it unmandated was an internal inconsistency,
> not a judgment call.***

**⚠ And `04` contradicts itself:** **Dumont d'Urville appears in the food TALLY but NOT in `04` §3's provider
LIST.**

**2. §15 names an international trade role** — *"Commercial: 20% — port and shipping logistics **(Australian
freighter trade)**."* This coast is the **Australia-facing** side of Tepenia's Upper Earth shipping.

### ⏸️ Why the commercial share was NOT taken

**Held deliberately.** The Australian-freighter line is **a single mention in one file** — `Specs/
Dumont_dUrville.md` does not mention it — and **this coast has several receiving points rather than one
chokepoint.** **Banked as an option** *(C = ⅓ marine + half commercial → mandate 9.5% / free 42.5%;
D = + full commercial → 14.7% / 37.3%)* **rather than assumed.**

### ⭐ The marine sector's other half — counted deliberately, not overlooked

**§15: *"Marine / resource extraction: 25% — coastal and channel resources, PENGUIN COLONY MANAGEMENT."***
The Adélie colonies are *"a defining daily-life feature — **food supplement + coexistence**."*

> **Management, not harvest.** **Only the ⅓ that `04` treats as food is mandated; the coexistence work stays
> free.**

### What stays FREE

- **Technical/scientific 25%** — *"wind engineering, structural maintenance against ongoing wind damage."*
  **Local survival** among **the windiest regions on Earth** *(Adélie katabatics; George V Land nearby holds
  real-world highest-sustained-wind records)*. **The Princess Elisabeth disposition: least discretionary work
  in the city, still not national.**
- **Industrial 15%** — explicitly *"repair and maintenance-focused rather than large-scale production."*
- **Commercial 20% · Education 8% · Other 7%.**

### Notes

- **⭐ DOUBLE MAIN-LINE TERMINUS** — **Hwy 2's own eastern end AND Hwy 183's own northern end converge here
  directly** *(`Highways.md` L56, L65, L87–96, L224–231, L264)*. **Not mandated:** per the standing crossroads
  principle, **a terminus is not automatically an employer**, and §15 has no highway-logistics sector — its
  commercial line is a *port*, not a road hub.
- **Named for St. Jules** *(Jules Dumont d'Urville, landed 21 Jan 1840)* — **the most distinctively
  francophone-speaking city in Tepenia.** Symbolic read: *"New Orleans at 1/20th scale."*
- **⏸️ Genuinely open in canon:** **permanent bridge to the mainland vs. seasonal crossing** — extensively
  brainstormed in Specs *(flutter risk, pack-ice pier loads, maintenance access)* and **explicitly not
  resolved.**
- **Pink Lucy's origin city**; she relocated to Janbogo pre-war *(resolved 2026-07-12)*. Whether she then
  reached Concordia is open.

---

# ⏸️⏸️ CONCORDIA — DEFERRED BY DEVELOPER DIRECTION, 2026-09-02

> ***"I'd like to hold off on Concordia until we've been able to develop every one of the districts to a very
> well-defined degree, since that will determine the municipal division-of-industry character, which will
> then determine what sort of post-war condition the city will end up in, which will then determine the
> setting of the actual game."***

### ⭐⭐ Why this is not just another deferral — the dependency runs BACKWARDS here

**For all 36 other cities, this pass runs TOP-DOWN:** the city's §15 and national role are read first, and
the determination then informs the city's character.

> ### **Concordia runs BOTTOM-UP. Its thirteen districts determine the city, not the reverse.**

**The chain the developer stated, in order:**

| | Step | Determines |
|---|---|---|
| **1** | **All 13 districts developed to a well-defined degree** | → |
| **2** | **The municipal division-of-industry character** | → |
| **3** | **What post-war condition the city ends up in** | → |
| **4** | ***THE SETTING OF THE ACTUAL GAME*** | |

**Running Concordia now would mean deriving step 2 without step 1, and every step downstream inherits the
error.** **Step 4 is the game itself** — ***this is the single costliest place in the whole roster to guess.***

### What this means for the pass

- **Concordia is NOT determined**, and its Half A/B estimate *(15%, rated "reasonable by analogy")* **stands
  as an estimate only — do not promote it.**
- **The Janbogo subnet will close INCOMPLETE**, alongside Halley *(Lazar)*.
- **The national re-run** *(ABCC values + the §15 denominator, register items 11 and 15's companions)*
  **must treat Concordia as an open cell**, not a filled one.
- **Prerequisite:** the district culture work — the 13-district development plan and its runbook — **is
  upstream of this determination**, not parallel to it.

---

## 📋 END-OF-PASS REVIEW REGISTER

**Items deliberately held during the roster pass, to be revisited once all cities are determined.**

| # | City | Held item | What the review tests |
|---|---|---|---|
| 1 | **{{Abowasa}}** | Commuter-labor mandate held at 10% of distinctive *(5.4% of workforce)* | Whether a city with **no food debt** should carry a commuter export at all — and what cutting it does to the Halley subnet's supply picture and the national balance |
| 2 | **Sanay** | **Its §15 has no Arcanet sector, yet canon says it hosts the subnet's Arcanet relay nexus** | Whether the nexus staff sit inside Technical/scientific 10% *(currently left FREE)*, or whether Sanay's §15 needs an Arcanet line added. Compare Mirny's explicit `Communications/Arcanet ~20%` |
| 3 | **Troll** | **Set to Option A — logistics 30% only. Mandate 16.7%, free 38.9%** | Rerun as **Option B (+ half of Industrial/manufacturing = 37.5% of distinctive → mandate 20.8%, free 34.7%)** and see what it does to the national numbers. **A was chosen because Troll's §15 says only "Industrial / manufacturing," unannotated** — unlike Sanay's, which literally reads `Industrial/manufacturing (repair)`. Taking half would assume a sector's content to match precedent rather than read it. **The case for B:** air freight is maintenance-hungry and a 3,000 m blue-ice runway needs constant grooming — though that work more likely already sits inside the 30% canon calls *"airfield operations and control"* |
| 4 | **Princess Elisabeth** | **A vignette says the city *"was never self-sufficient in food/materials, only energy"* — contradicting its GROWER classification** | Vignettes are not canon, so f=1.00 stands. But if ever promoted, baseline drops **43.7% → 33.7%** and distinctive rises to **66.3%** — a 10-point swing. Possible reconciliation *(not asserted)*: PE's **outdoor** tier is genuinely zero *(300 km/h winds)*, which the vignette may be describing rather than indoor growing |
| 5 | **Method — inland "Marine / resource extraction"** | **Second instance** *(Troll, Princess Elisabeth)* of an unannotated compound marine label at a city far inland and high up | Whether the **extraction** half is the intended read at inland nunatak cities generally. Watch for further instances as the pass continues; if the pattern holds across subnets it is worth one consolidated ruling rather than per-city judgment |
| 6 | **Sejong** | **Its §15 has no customs/immigration/border line, yet it hosts the Machu Picchu Border & Customs Authority** | **Second instance of the Sanay pattern** *(national infrastructure with no §15 sector)*. Here the cause is datable: **the §15 is from 2026-07-04, the gateway ruling from 2026-09-02.** Whether Sejong's §15 needs a border line added, or the function is considered folded into Commercial/trade 25%. **Mandate held at 25% either way** |
| 7 | **National — deferred by developer** | **Where a neutral zone of international diplomacy would be situated** | ⏸️ **Parked deliberately, 2026-09-02: *"I actually hadn't previously thought about where a 'neutral zone' of international diplomacy could be situated, but that's a problem for the future."*** Raised by Sejong's border role. **NOT to be closed opportunistically** — it is a real open design question, not an oversight |
| 8 | **Sejong — canon bug, deferred** | **The Hangul-literacy / Korean-dilution premise: the 2026-08-02 fix was incomplete, 3 files still stale, 17 more unaudited** | ⏸️ **Deferred by developer 2026-09-02 until per-city DoI is finished** — *"that's really more relevant to the per-city culture than anything else."* **Not a DoI input; Sejong's determination was built without touching the education sector where the stale material attaches.** Full detail and the 3 file paths now recorded in `TODO.md`'s existing Sejong section — **⚠ read for the premise, do not grep-and-delete "Hangul," which is still valid canon** |
| 9 | **⭐ Fort McMurdo — THE CAPITAL** | **Its §15 records zero governmental employment; its 35.1% mandate is entirely industrial** | **The seat of national government is modeled as a mining town that happens to be the capital.** Per the structural finding above, national administrative concentration must be a **mandate**, not a §15 sector — so Fort McMurdo needs one. **Resolve at its own entry, not before** |
| 10 | **Juan Carlos** | **When did the federal archive relocate to Amundsen Station?** | Canon says it moved *"later,"* and that the strike came *"even after the bulk archive had moved"* — **but the Second Interwar runs 248 years and no date is given.** Whether the 10% archive mandate describes the whole period or only its earlier stretch |
| 11 | **⚠⚠ METHOD — ALL CITIES** | **The DoI files disagree on what §15 percentages are a percentage OF** | **`16` applies them to the DISTINCTIVE tier; `04` and `National_Medical_and_Care_Institutes.md` apply them to the WHOLE WORKFORCE.** Esperanza education 25%: **211,198 vs 350,155** — 139,000 workers apart. `04` does it too *(Signy "fishing 30% → 42,638" is 30% of whole workforce)*. **NOT resolved mid-pass by deliberate choice** — re-picking the denominator now would invalidate every determination **and** the national balance. **Resolve together with the ABCC re-run; both are mechanical re-runs of the same table.** All determinations continue on `16`'s convention so they stay mutually consistent |
| 12 | **Belgrano — deferred by developer** | **The Belgrano Institute of Medicine's classification** | ⏸️ **Parked 2026-09-02: *"I'm sure there's a better way to classify the Belgrano Institute of Medicine."*** Currently absorbed into the **Aviation/logistics 35%** mandate on the grounds that medevac is an aviation function and the school is downstream of the flight line. **Revisit AFTER the full-country run**, not before — and note the ruling above stands: it is not a case for a separate §15 sector |
| 13 | **Port Lockroy — stale TBD** | **Its post office is recorded as an open question in 3 files, but the question is resolved** | `Specs/Port_Lockroy.md` **L112, L134** and `Local_Cultures/Palmer_Subnet/Port_Lockroy.md` **L248** all say *"functioning institution or heritage artifact — TBD."* **Both the Vision Notes and the Calethina courier lore (Specs L105) settle it as a genuine, active civic institution.** A resolution that never propagated. **Deferred with the other culture-file corrections until after this pass** |
| 14 | **Davis** | **Set to Option B — agriculture 35% + HALF technical/scientific 12.5%. Mandate 28.2%, free 31.1%** | ⏸️ **Marked for review after all cities are determined**, per developer direction — *"just in case we need to figure on adjusting stats in some cities."* **Alternatives precomputed:** **A** *(agriculture only)* mandate 20.7% / free 38.5% · **C** *(+ full technical)* mandate 35.6% / free 23.7% · **D** *(B + half maritime)* mandate 32.6% / free 26.7%. **The half-technical rests on the Signy precedent** — a capped national resource needs someone who knows its limits — **applied on land to the Breadbasket** |
| 15 | **Kunlun** | **Set to HALF astronomy + HALF ice core. Mandate 26.8%, free 44.6%** | ⏸️ **Marked for review by the developer, who is weighing TWO-THIRDS of each instead** — precomputed: **mandate 44,072 (35.7%) / free 44,072 (35.7%)**, exactly equal. **The developer's own reason for holding at half:** *"having a 44% free budget would allow for other scientific research that I may not have thought of."* **Also depends on an unsettled premise** — the near-Earth observatory focus is explicitly *"tentative, not firmly settled"* (2026-07-06) |
| 16 | **`04` — internal inconsistency** | **Dumont d'Urville appears in `04`'s national FOOD TALLY (28,463 producers) but NOT in `04` §3's provider LIST** | Found during DdU's determination. **The tally figure is load-bearing** — it sits inside the ~835,000 total behind the headline *"1 food producer per ~19 people"*; without it the ratio is 1 per 19.4. **Whether `04` §3's provider list should gain Dumont d'Urville, or the tally should lose it.** *(The mandate has been set on the tally's side.)* |
| 17 | **⏸️ CONCORDIA — DEFERRED** | **Not determined, and deliberately so.** Its 13 districts must be well-defined FIRST, because they determine the municipal DoI character → the post-war condition → **the setting of the actual game** | **The dependency runs backwards here: bottom-up, where every other city is top-down.** Its 15% Half A/B estimate **stands as an estimate only — do not promote it.** **District culture work is UPSTREAM of this, not parallel.** The national re-run must treat Concordia as an **open cell** |
