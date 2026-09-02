# Division of Industry — STATUS: RELIABLE

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
| **`08_Volume_Based_Requirement_Reference.md`** | ⭐ **The method and the rates.** Start here |
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

# Integration task — scheduled, not started

**Folding these figures into `Specs/` and `Local_Cultures/` requires, per city:**
1. Read the existing §15 for **baseline content already present**, and deconflict *(e.g. Cape Adare's
   "Technical/scientific 20%" explicitly includes medicine — it would double-count against B2)*.
2. Rescale surviving distinctive entries into the `100 − BaselineLoad` envelope, preserving their ratios.
3. Fill the city's column in `02_Cross_City_Industry_Differentiation_Table.md` **in the same commit**.
4. Tag deposits `[CGRM 2026-09-01 · Path 2 · volume-based requirement model]`.

**Two chores to clear first:** the **Cape Adare provider contradiction** *(`04` §3 and §4 disagree)*, and
**sourced rates for C6/C7/C8/D4.**
