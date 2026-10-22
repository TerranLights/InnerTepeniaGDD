# Phase 7 — Corporation Roster and Model Files — Quick Reference

**Tier U — identical for every city.** Extracted 2026-10-21 from: `TepenianUniverseTimeline/Megacorps/` · `Division_of_Industry/01_Burden_Scoring_Model.md` (311 lines) · `Division_of_Industry/08_Volume_Based_Requirement_Reference.md` (776 lines) · `Reference/Real-World/Industry_Staffing_and_Productivity/` · `Reference/Real-World/jobs_professions_and_fields/`. A quick reference: it copies the sources' words, it adds no finding, and it names no city's answer.

> ⚠⚠ **PRELIMINARY AND RUDIMENTARY — a first draft, at the developer's direction (2026-10-21).** The corporations have not really been worked out yet, so the roster below is only what the folder says today. **This sheet is an index with line numbers and the sources' own header words. It summarizes nothing and decides nothing.** The citation gate on food and industry figures lives in `Division_of_Industry_Reliability_Quick_Reference.md`; read it before citing any figure from the model files.

## A · The corporation roster — what `Megacorps/` holds

| Entry | The folder's own words | Source |
|---|---|---|
| Abramentes | Industrias Abramentes / Primarily based in the Republic of Sonora (La República de Sonora) | `Megacorps/Abramentes/README.md` L1–L3 |
| HyperHedral | HyperHedral Industries / Primarily based in the People's Democratic Republic of Cascadia | `Megacorps/HyperHedral/README.md` L1–L3 |

**The folder's own quick-summary list** (`Megacorps/README.md`): HyperHedral (L9) · Abramentes (L10) · [TBD] (L11).

**What the folder does not say — open, not absent:** the top-level README states the era of these corporations as the First Interwar Period (L3); **it does not say whether either corporation exists in the Second Interwar default frame**, how large or what they make, or which cities they touch; the third roster slot is `[TBD]`. Treat all of that as undeveloped.

## B1 · `01_Burden_Scoring_Model.md` — 311 lines

Built 2026-09-01 (L3). Its own banner (L6–L8) calls it an INSTANCE, not a method: nothing in it generalizes beyond the Tepenian city set. **Section 0 (L15–L36) is the period-scope box — read it first.**

| Line | Heading (as written) |
|---:|---|
| L1 | # Burden Scoring Model — the instrument |
| L15 | # 0. ⚠ PERIOD SCOPE — READ FIRST |
| L37 | # 1. The core reframe — burden, not presence |
| L52 | # 2. The formula |
| L72 | # 3. W — base weights |
| L96 | # 4. N — the necessity multiplier *(population composition)* |
| L118 | # 5. B — the burden multipliers *(physical situation)* |
| L140 | ## Calibration anchors — real, and written down so the numbers mean something |
| L149 | ## 5.1 Labor externalization — added 2026-09-01, and it does something none of the others do |
| L187 | ## The predicted envelope |
| L199 | # 6. Worked example — Ariun Nuur, and why this fixes the sweep's §3 for free |
| L233 | # 7. Output format — the two-tier §15 *(developer ruling, 2026-09-01)* |
| L236 | ## 15. Division of Industry |
| L258 | # 8. Process — and the guards that are not optional |
| L278 | ## The pilot, and its falsification test — declared in advance |
| L303 | # 9. Honest status |

## B2 · `08_Volume_Based_Requirement_Reference.md` — 776 lines

Its own banner (L3–L5) calls it the developer-specified method of 2026-09-01 that supersedes both earlier sizing attempts; L5: basis Census I, period Second Interwar.

| Line | Heading (as written) |
|---:|---|
| L1 | # Volume-Based Requirement Reference |
| L9 | # 1. Why this replaces what came before |
| L33 | # 2. The procedure |
| L70 | # 3. What this method fixes |
| L83 | # 4. Research findings |
| L112 | ## ⭐ 4.0 — A STRUCTURAL REFINEMENT THE FIRST INDUSTRY FORCED. Applies to all eighteen. |
| L145 | ## 4.1 — A2 WATER & SANITATION ✅ |
| L175 | # 4.2 — ⭐ THE SOURCE REGISTER — canonical references located for all 18 industries |
| L180 | ## ✅ TIER 1 — canonical, free, per-country, both figures obtainable |
| L195 | ## ✅ TIER 2 — good sources, one figure needs more work |
| L206 | ## ⚠ TIER 3 — NO DIRECT REAL-WORLD ANALOG EXISTS. Proxy or invent, and say which. |
| L215 | # 4.3 — ⭐ THREE PATTERNS THAT RECUR ACROSS THE SOURCES |
| L240 | # 4.4 — ⏸️ THE ROBOT DUTY CYCLE IS DEFERRED, AND THE WORK ROUTES AROUND IT |
| L257 | ## ⚠⚠ TWO CORRECTIONS, developer-issued 2026-09-01. Both were my errors. |
| L313 | # 4.5 — EXTRACTED FIGURES, ROUND 2 |
| L350 | # 5 — FIRST RUN OF THE NUMBERS — 2026-09-01 |
| L354 | ## 5.1 The rate table |
| L378 | # 9 — ⭐ THE ROBOT-KEYED RATES — SET 2026-09-01 |
| L383 | ## 9.1 The method: composite parallels, not a single analog |
| L399 | ## 9.2 ✅ **B3 ROBOT MAINTENANCE & CARE = 12.5 per 1,000 robots (1 per 80)** |
| L416 | ## 9.3 ✅ **B4 ROBOT SUSTENANCE (siligel + coolant) = 3.25 per 1,000 robots** |
| L435 | ## 9.4 C5-robot decommissioning — **NOT a standing industry** |
| L446 | # 8 — ⭐ THE ADMINISTRATION RATE, SOURCED — 2026-09-01 |
| L496 | ## 5.2 Results |
| L511 | # ⛔ 5.3 — THE RESULT IS A NEAR-FLAT LINE, AND THAT IS THE FINDING |
| L536 | ## 5.4 Sanity check against the anchor |
| L547 | # 6 — THE DIFFICULTY LAYER: A SOURCED BASIS AT LAST |
| L552 | ## 6.1 The cost ladder — three anchors, all sourced |
| L564 | ## 6.2 ⚠ AND IT REVERSES A JUDGMENT MADE EARLIER IN THIS PASS |
| L585 | ## 6.3 The canonical labor instrument exists, and it is purchasable |
| L598 | ## 6.4 ⭐ And the research handed the autonomy-duration concept real numbers |
| L608 | ## ⭐⭐ 6.4b — THE MCAA FACTOR TABLE, OBTAINED. The difficulty layer now has a sourced basis. |
| L676 | # 7 — SECOND RUN: DEMAND × DIFFICULTY. The flat line breaks. |
| L678 | ## 7.1 Selective application — which industries each factor actually touches |
| L709 | ## 7.2 Results |
| L724 | ## 7.3 ⭐ And the ordering now matches physical intuition, unprompted |
| L737 | ## 7.4 Against the anchor |
| L750 | ## 6.5 What is still missing |
| L764 | # 5. ⚠ Known open questions this method inherits |

## C · The staffing and jobs references

**`Industry_Staffing_and_Productivity/`** — 4 files: `MCAA_Labor_Productivity_Factors_-_Ibbs_and_Sun_ASCE_2016.pdf` · `MCAA_Method_In-Depth_Analysis_-_Ibbs_and_Sun.pdf` · `NEIWPCC_Northeast_Water_Wastewater_Plant_Staffing_Guide.pdf` · `README.md`.

**`jobs_professions_and_fields/`** — 5 files: `SOC_Cross_Category_Commonalities.md` · `SOC_Cross_Category_District_Matching.md` · `SOC_Minor_Group_Summaries.md` · `SOC_Table_of_Contents.md` · `soc_2018_manual.pdf`.

`Industry_Staffing_and_Productivity/README.md` states it was collected 2026-09-01 (L3) and is consumed by `08_Volume_Based_Requirement_Reference.md` §4.1 and §6.4b (L7–L8). SOC tier-marking is additive only: it never replaces a method.

## D · What this sheet is NOT

Not a summary of any model, not a figure for any city, not a list of which corporations a city hosts (no source says), and not a ruling about the corporations. The Phase 7 readers still open the model files in full.
