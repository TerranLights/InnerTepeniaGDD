# Industry Staffing & Productivity — Reference PDFs

**Collected 2026-09-01** during the Division of Industry volume-based requirement work. **These are the
sourced instruments behind the model's two hardest layers: how many people it takes to run an industry, and
how much harder that gets in a hostile place.**

**Consumed by:** `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/
Division_of_Industry/08_Volume_Based_Requirement_Reference.md` §4.1, §6.4b.

> **⚠ Copyright note.** These are author-hosted or association-hosted copies retrieved from public URLs, kept
> here as personal research reference. **The ASCE paper carries "Copyright ASCE. For personal use only; all
> rights reserved."** Do not redistribute or republish; cite the originals.

---

## ⭐ `MCAA_Labor_Productivity_Factors_-_Ibbs_and_Sun_ASCE_2016.pdf` — the important one

**Ibbs & Sun, "Use of Mechanical Contractors Association of America Method in Loss of Productivity Claims,"**
*Journal of Legal Affairs and Dispute Resolution in Engineering and Construction*, Vol. 8, No. 4.

**Why it matters: it reproduces the complete MCAA Labor Productivity Factors table** — 16 impact categories
with minor / average / severe percentage-loss values. **That table is otherwise inside a $495 publication**
*(MCAA, "Change Orders, Productivity, Overtime — A Primer for the Construction Industry," pp. 135–136; free
to MCAA members, $150 to MCAA/SMACNA/NECA members, DRM-secured PDF)*. **Obtaining it here cost nothing.**

**The three categories that map onto Tepenian conditions:**

| Category | Minor | Average | Severe |
|---|--:|--:|--:|
| **Season and weather change** *(very hot or very cold)* | 10 | 20 | **30** |
| **Logistics** *(materials supply / storehouse problems)* | 10 | 25 | **50** |
| **Site access** *(interference with access to work areas)* | 5 | 12 | **30** |

**Two structural facts taken from it:**
- **MCAA applies factors ADDITIVELY** — independently vindicating the additive `1 + Σw(m−1)` difficulty form
  the model had already derived on separate reasoning.
- **Its documented failure mode is over-inflation** — *"if improperly applied… could unrealistically inflate
  the amount of lost staff-hours."* **Summed severe factors exceed 100% loss, so capping is mandatory.**

**⚠ Scope caveat, important:** these measure **disruption to a construction project**, not **steady-state
operation in a permanently hostile place.** A city built for the cold does not run at 30% weather loss
forever. **"Severe" should not be a default.**

---

## `MCAA_Method_In-Depth_Analysis_-_Ibbs_and_Sun.pdf`

Longer companion study — a full critique of the MCAA factor model, with chapters on weather, learning curve,
overtime and crew-size inefficiency, plus analysis of legal cases where the method was applied. **Useful for
the criticisms of the method** *(Harmon & Cole: application is subjective, no description of what constitutes
minor/average/severe, some factors are repetitive)*, which are worth knowing before leaning on it.

---

## `NEIWPCC_Northeast_Water_Wastewater_Plant_Staffing_Guide.pdf`

**"The Northeast Guide for Estimating Staffing at Publicly and Privately Owned Wastewater Treatment Plants"**
(NEIWPCC). Studied 25 New England plants from 0.25 to 56 MGD.

**⚠ Text extraction from this one failed** — the PDF is image-based. **The staffing figures currently used in
the model came from EPA's own estimating manual instead** *(1.0 MGD ≈ 3 staff · 9.5 ≈ 11.7 · 20.0 ≈ 21
well-run · 20.0 ≈ 37 problem plant → `staff ≈ 3 × MGD^0.65`)*. **Kept here because it covers the same
question with a larger sample and may be worth OCR'ing** if the water figures ever need tightening.

---

## Sources located but NOT obtained *(for a future session)*

- **RSMeans City Cost Index / location factors** — paywalled; would give sourced remote-Alaska multipliers.
- **AWWA Utility Benchmarking Survey** — paywalled; has a "Staffing Levels per 1,000 Population Served"
  indicator that would replace the model's estimated water figure with a real one.
- **CRREL** *(US Army Cold Regions Research and Engineering Laboratory)* — McMurdo snow-road and Antarctic
  resupply studies; the authoritative body for cold-regions engineering. Reports exist; specific cost factors
  were not reachable by search.
- **McMurdo's functional staff breakdown** — the ~656 support staff of 995 total, broken down by function.
  **Flagged in the test log as the single highest-value research target remaining**, since it would supply
  sourced rates for a dozen industries at once.
