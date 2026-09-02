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

Compare Mirny, whose §15 carries an explicit `Communications/Arcanet ~20%` for its own subnet-hub role.
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
FROM WHERE YOU SIT.** Unlike Troll, no canon states national freight moves through PE. **FREE.**

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
| **Sinheung Institute of Cybernetics and Robotic Care** | Sinheung | **Industrial fabrication 45%** |

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
