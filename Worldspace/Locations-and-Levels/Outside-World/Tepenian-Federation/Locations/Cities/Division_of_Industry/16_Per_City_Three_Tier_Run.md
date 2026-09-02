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
| **Zhongshan** | 631,985 | **MARITIME LOGISTICS — the Tri-Cities' port** | §15: *"Prydz Bay maritime logistics… cluster economy with Sinheung."* **Sinheung builds the nation's Cradle chambers; they have to leave by sea, and Zhongshan is how** |
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
| Zhongshan · Dome Fuji | **20%** | the Tri-Cities' port · seed archive + ice-core |
| Concordia | 15% | the national crossroads |
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
> **Sejong is where people and goods ENTER TEPENIA AT ALL.**

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
| **Reasonable by analogy** | Zhongshan 20% · Princess Elisabeth 25% · Concordia 15% | PE could be 15–20% *(consulting is lighter than industry)*; Concordia could be 20–30% *(Casey, a DUAL junction, carries 30%)* |
| **⚠ Weakest — still** | **Dome Fuji 20%** | **An estimate resting on an estimate** — the seed archive is my own proposal, and a *passive* vault needs almost nobody. **10% is probably closer.** Worth only 8,005 workers either way |

---

---

# ▶▶ PER-CITY DETERMINATIONS — the roster pass, one city at a time

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
