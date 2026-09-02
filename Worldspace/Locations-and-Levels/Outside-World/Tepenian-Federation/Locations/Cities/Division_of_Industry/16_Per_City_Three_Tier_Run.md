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
| `./05_Remaining_Cities_Assessment.md` | The non-provider cities; the Halley-subnet gap and the **commuter-labour mechanism** (5–10% scenarios) |
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
