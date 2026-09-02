# Division of Industry — STATUS: RELIABLE, WITH ONE CARVE-OUT

> ## ⛔ **CARVE-OUT — THE FOOD LAYER (B1) IS NOT RELIABLE. Added 2026-09-01, after independent validation.**
> **Three independent checkers found the national food balance to be circular, double-counted, and stated in
> the wrong units. `10_Validation_Findings_2026-09-01.md` is REQUIRED READING before citing ANY food figure
> from `04`, `05`, `09`, or from this file's own "First results" section below.**
>
> **What is affected:** the B1 rate, every export/deficit figure, the national balance, and the "First results"
> block near the bottom of this file. **What is NOT affected:** population, workforce, the difficulty ladder,
> and the other 21 industries. **The coalition finding and the Weddell Sea third-center finding both survive.**
>
> **✅ DRQ-08 is ANSWERED — see `11_Caloric_Rebuild_and_Livestock_Tier.md`. The B1 rate is rebuilt from human
> caloric need: 53 → 120.7 per 1,000 humans, a 2.28× increase that holds across every plausible input.**
> **⏸️ DRQ-09 (the baseline/distinctive convention) is still open and still blocks every export figure.**

> ## ✅ **MARKED RELIABLE — developer ruling, 2026-09-01.**
> **The findings and figures in this folder are settled working canon.** They may be cited, built on, and used
> as inputs by other work. **They are not "provisional," "draft," or "unvalidated" — that phase is over.**
>
> **What remains is INTEGRATION, not verification:** folding these numbers into the official
> `Specs/` and `Local_Cultures/` files, which is a separate scheduled task.

---

# Read in this order

| File | What it is |
|---|---|
| **`10_Validation_Findings_2026-09-01.md`** | ⛔ **READ FIRST.** What three independent checkers found, and which figures it invalidates |
| **`11_Caloric_Rebuild_and_Livestock_Tier.md`** | ⭐ **The food layer, rebuilt from biology.** The new B1 rate, the marine-employment finding, the livestock tier |
| **`12_Terraforming_and_the_Outdoor_Tier.md`** | ⭐ The terraformed coastal belt, multi-species livestock, and the feed chain. **Candidate answer to what anyone eats after the Tower** |
| **`13_National_Balance_Under_the_Ruling.md`** | ⭐ The three-tier geology, all 37 cities classified, and why the food map is an ECONOMIC question not a geological one. **§12 — Tepenian crops use no daylight** |
| **`14_Completing_the_Food_Basis.md`** | ⭐ The five-tier food system. **Fungi as the fourth tier; phosphorus as the one input that cannot be manufactured** |
| **`15_Open_Items_and_Three_Resolutions.md`** | ⛔ **THE STATUS FILE.** List A = what blocks the per-city pass · List B = open gaps that don't. Fungi sized, Cape Adare's phosphate, seed vaults |
| **`16_Per_City_Three_Tier_Run.md`** | ⭐ **THE CALCULATION SHEET.** Half A (13 assessed cities) + Half B (37-city three-tier table) + open estimates |
| **[`../City_Master_Reference/README.md`](../City_Master_Reference/README.md)** | ⭐⭐ **Everything else about every city** — geography, founding, culture, notable locations — organized by subnet, with a canon-tier legend. Cross-reference this alongside the numbers above |
| **`08_Volume_Based_Requirement_Reference.md`** | ⭐ **The method and the rates.** Start here — **but its B1 rate is superseded by `11`** |
| **`09_Per_City_Baseline_Run.md`** | ⭐ **The answers — all 38 cities.** §3.5 is the freedom-margin finding |
| `00_Necessary_Industries_Register.md` | the 22 industries, and what the SOC cross-check found |
| `04_Providers_and_National_Balance.md` | who supplies whom nationally; the outsourceable split |
| `05_Remaining_Cities_Assessment.md` | the non-provider cities, and the Halley-subnet food gap |
| `06_Census_Basis_Correction.md` | why Census I; the "build for peak, then depopulate" ruling |
| `02_Cross_City_Industry_Differentiation_Table.md` | the anti-convergence guard — **still empty** |
| `01`, `03`, `07` | **SUPERSEDED.** The share-first model and its failed validation. **Kept as the record of why the method changed — do not use their figures** |

---

# What "reliable" does and does not mean here

**✅ Settled and usable:**
- The **22-industry register**, and the human/resident/robot keying.
- The **rates** — sourced against NFPA, WHO, UNESCO, FAO, OECD, IFMA, EPA, EEA, World Bank, BLS/FRED.
- The **difficulty layer**, calibrated against the MCAA Labor Productivity Factors and cross-checked against
  Iqaluit and Halley VI cost data.
- The **per-city baseline figures** for 19 of 22 industries, all 38 cities.
- The **freedom margin** and everything derived from it.

**⚠ Known-and-stated uncertainties — recorded, not hidden:**
- **Administration ±1.7 points per city** from the uplift multiplier *(base is measured; uplift is a
  worldbuilding judgment)*. **Does not change any city's ranking.**
- **The 2.5× ice-shelf difficulty** is the single number doing the most work in the model.
- **C6, C7, C8, D4 rates are estimated**, not sourced — they were added late, after the SOC cross-check.

**⏸️ Genuinely open, and deliberately so:**
- **The three robot-keyed industries** — B3 maintenance, B4 sustenance, C5-robot decommissioning.
  **This is the remaining substantive topic.**

---

# ⭐ The §15 denominator: RULED, not outstanding

**Earlier files in this folder call the coverage denominator an unresolved gate. It is not.** The developer's
**two-tier §15 ruling** — `Baseline civic load X% + Distinctive economy (100−X)%` — **sums to the whole
economy with baseline explicitly named. That is the denominator.**

**What remains is a MIGRATION, not a decision.** The existing 36 sheets were written under the older
convention where §15 partitioned only the *visible* economy — which is why the 2026-08-31 sweep found
utilities absent from **36 of 36 cities.**

> **⚠ And this explains the Denison anomaly that failed two validation tests.** Its canon `Structural/wind
> engineering: ~25%` is an **old-convention figure** — a share of the visible economy — being compared against
> a **new-convention model** that partitions everything. **The tests were invalid; the model was not wrong.**

---

---

# ⭐ WHAT THIS UNLOCKS — five things that were impossible before and are now straightforward

**Recorded 2026-09-01 at the developer's request, on completion of the model.**

## 1. ⭐ The producer pass — the developer's own deferred item, now computable

> *"We'll go through the producing contributor cities and see how much of other cities' outsourceable
> industries those producer cities are able to reasonably, realistically manage, **without putting an
> unreasonable strain upon their own local populations**."*

**"Unreasonable strain" now has a number.** Spare capacity = workforce × (1 − BaselineLoad):

| Provider | Baseline | **Free for export work** |
|---|--:|--:|
| Esperanza | 35.6% | **64.4%** of 1,400,619 |
| Davis | 36.4% | **63.6%** of 876,515 |
| Sinheung | 36.3% | **63.7%** of 809,755 |
| Signy | 36.7% | **63.3%** of 142,127 |
| Sanay | 39.1% | **60.9%** of 347,881 |

**⭐ And the method that makes it work:** compare a city's §15 sector share against **the model's baseline
requirement for that same industry.** The excess is export capacity. *(Started — see §"First results" below.)*

## 2. ⭐ Every city now has a CHARACTER BUDGET

**Distinctive tier = `100 − BaselineLoad`** — the room available for provider work, LAW G weird industries,
and Local Texture.

> **Casey has 65% to spend on being itself. Neumayer has 49%.**

**A known, per-city budget for character — which the culture work has never had.**

## 3. Absolute headcounts unlock the downstream work

*"Vostok has ~3,240 healthcare workers"* is usable where a percentage never was: **faction and guild sizing,
institution scale, NPC populations, and level design** — what buildings exist in a city and who is inside
them. *(The requirement-first trial's author identified this as the architecture's real advantage; it is now
realized.)*

## 4. Two standing chores became cheap

- **The Cape Adare contradiction** *(`04` §3 and §4 disagree on whether it is a provider)* — now decidable:
  its marine sector either exceeds its own need or it does not.
- **The Belgrano/Sanay Weddell food split** — apportion by their respective spare capacities rather than
  guessing.

## 5. ⭐⭐ The Governing Priority Sequence's Stage 4 is unblocked

Stage 4 — *"populate the city specs with real, lived-in cultures, human and robot both"* — was **deliberately
sequenced last**, because *"writing culture before the gaps are filled would mean building on an incomplete
foundation, exactly what the Canon Gap Resolution Method exists to prevent."*

> **The foundation is filled.** Every city now has a sized economy, a known character budget, a freedom
> margin, and — for the robot half — a leisure history that gives all of it meaning.

## 6. ⭐ A NATIONAL DEPENDENCY MAP — added 2026-09-01

**Every flow now has a source, a destination and a magnitude.** That was never true before; the pieces existed
but none of them were sized.

| Flow | Source → destination |
|---|---|
| **Food** | **Davis** feeds ~⅓ of the country · the **Scotia Sea** feeds the Peninsula · the **polynya** fed Janbogo · **Belgrano + Sanay** feed the Halley subnet, worked by commuters from Halley and {{Abowasa}} |
| **Education** | **Esperanza** and **Shirayuki** export tertiary training; **~21,000 medics + ~3,400 robot-care technicians per year** move outward from three institutes |
| **Chambers** | **Sinheung** and **Byrd** supply the nation. **Mountain Pass** used to |
| **Logistics** | **Casey** *(Hwy 110 × Hwy 2)* · **Marambio** · **Sanay** · **Belgrano** · **Troll** · **Mawson** |
| **Fabrication** | **Sinheung** *(45%, highest in corpus)* · **Rothera** · **Fort McMurdo** · **Byrd** · **Sayowa** |

**⭐ It is drawable, and it is the prerequisite for anything about disruption** — severing a line only matters
if you know what was flowing along it and how much.

---

# ⏸️ LOW-PRIORITY / TENTATIVE — what the Long Night War destroyed

**Raised 2026-09-01, and deliberately parked by the developer the same day.**

> *"The extent and nature of it is near-guaranteed to change as more worldbuilding gets accomplished, so let's
> leave that as low-priority tentative for now."*

**The capability is real and worth knowing about:** the model describes the **Second Interwar**, but the game
is set **~2822–27, after the war** — and now that every city's output and every dependency is sized, the cost
of losing a city is computable. Canon marks **Casey** *(the Hwy 110 × Hwy 2 junction)*, **Cape Adare**,
**Zukelli** and **Denison** as destroyed, and **Belgrano** as ruined afterward. **No Census III exists
anywhere in the project**, and this would be the route to its economic half.

> **⚠ But do NOT build on it yet.** The war's extent and nature will move as worldbuilding continues, and
> anything computed now would need redoing. **Revisit once the war itself is more settled.**

---

# First results from the producer pass — 2026-09-01

- **Davis exports 269,442 food producers** *(306,780 total, minus its own 37,338 need)* — enough to feed
  **~5.1 million, roughly a third of Tepenia, from one city.** The breadbasket title is earned; it is simply
  not the whole supply.
- **⭐ Esperanza's education sector is twelve times its own need** *(350,155 vs 29,615)*. **Children cannot
  commute, so this cannot be primary schooling for other cities — it must be tertiary.** **The model
  independently explains why the Esperanza Institute of Medicine is at Esperanza:** it found a city with
  twelve times more teaching capacity than pupils and no way to export a classroom. **Shirayuki is a second
  such city** *(education 20% against a 2.0% need)*.
- **⛔ The Halley subnet is the tightest margin in the country.** 4,907,714 humans need **258,301** food
  producers; Belgrano and Sanay have **248,266** free *after* their existing aviation and port roles.
  **96% self-sufficient, short by ~4%.** **The most food-precarious region in Tepenia is the one holding 31%
  of its people.** ⚠ **The missing 4% turns on whether Lazar's, Troll's and Princess Elisabeth's 15% marine
  sectors are genuine dockside work or indirect** — Halley's is explicitly indirect and Lazar is inland.

---

# Integration task — scheduled, not started

**Folding these figures into `Specs/` and `Local_Cultures/` requires, per city:**
1. Read the existing §15 for **baseline content already present**, and deconflict *(e.g. Cape Adare's
   "Technical/scientific 20%" explicitly includes medicine — it would double-count against B2)*.
2. Rescale surviving distinctive entries into the `100 − BaselineLoad` envelope, preserving their ratios.
3. Fill the city's column in `02_Cross_City_Industry_Differentiation_Table.md` **in the same commit**.
4. Tag deposits `[CGRM 2026-09-01 · Path 2 · volume-based requirement model]`.

**Chores to clear first:**

1. **✅ The Cape Adare provider contradiction — RESOLVED 2026-09-01** by `11`'s marine-employment finding.
   **Cape Adare is NOT a food provider.** Read as fishing crews its 177,732-worker marine sector would land
   13.7× the entire national sustainable catch. **It is a port, shipping and marine-science sector.**
2. **⚠ CONCORDIA'S DIFFICULTY VALUE — flagged 2026-09-01, at the developer's direction. NOT yet corrected.**
   **Concordia is set at `D = 1.67`; Vostok is `2.50`.** But Dome C is **3,233 m, −52.7 °C annual mean, and
   1,100 km from the coast** — as remote and high as any inhabited site in the country.
   **⭐ The offsetting factor is real and must be weighed, not dismissed:** `Specs/Concordia.md` records Dome C
   as unusually **calm** *(3–5 m/s — "dome sites are calmer than slope or coastal stations")*, so the WEATHER
   component of D genuinely is low even where altitude, logistics and site access are extreme.
   **⚠ Consequence if corrected to 2.50: Concordia's own food burden moves from 13.0% to 19.4% of its
   workforce** — which materially changes how precarious the primary game setting is. **See
   `13_National_Balance_Under_the_Ruling.md` §8.**
3. **Sourced rates for C6/C7/C8/D4** — still estimated, not sourced.
4. **⚠ `02_Cross_City_Industry_Differentiation_Table.md` is STILL EMPTY**, and `CLAUDE.md` requires a city's
   column be filled **in the same commit** that completes a category for it.
