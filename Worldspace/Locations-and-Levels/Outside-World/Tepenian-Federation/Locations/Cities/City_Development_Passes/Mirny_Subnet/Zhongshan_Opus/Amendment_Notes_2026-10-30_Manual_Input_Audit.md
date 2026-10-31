# Zhongshan (Opus folder) — amendment notes, 2026-10-30 (manual input audit)

**What this file is.** Zhongshan's Opus-folder pass was run and closed on 2026-09-11 (Pre-Trip refreshed 2026-10-21). **No pass file is edited by this note, and none was.** Each entry says what has changed in one of Zhongshan's sources since the pass, where the pass rests on the old state, and the live value (recomputed by hand from the live files on 2026-10-30). The old values are kept as "as recorded at the pass (2026-09-11)". The counts of occurrences are from a search of the pass files for the old numbers and may miss a differently worded one.

**Developer decisions of 2026-10-30.** Added after the walk-through (*"all as recommended"*). The Pre-Trip received dated notes beside three stale lines (§E headcount check, §J footprint line, the runbook size and Step 10 range); nothing else in it was changed. Evidence: `Manual_Input_Audit_2026-10-29/Zhongshan_Audit.md` and `FIX_LEDGER.md`. The pass is to be re-analyzed with the current methods (see the Weekly To-Do); this file is the interim record.

---

## ZSO-010 — The census scenario of 2026-10-28 (`DR-68`) rescaled Zhongshan's population

| | As recorded at the pass (2026-09-11) | Live since `DR-68` (census L490 and L610) | Files in the pass that carry the old value |
|---|---|---|---|
| Census I humans | 568,786 | **580,925** | 7 (9 occurrences) |
| Census I robots | 582,703 | **594,481** | 7 (10) |
| Census I combined | 1,151,489 | **1,175,406** | 8 (13) |
| Census II humans | 470,135 | **478,243** | 5 (7) |
| Census II robots | 426,881 | **434,620** | 5 (7) |
| Census II combined | 897,016 | **912,863** | 6 (11) |

## ZSO-011 — Retention figures derived from the old set (recomputed by hand)

| | As recorded at the pass | Live | Where |
|---|---|---|---|
| Combined (912,863 ÷ 1,175,406) | 77.90% | **77.66%** | `00_Frame`, `01_Inherited`, `02_Spine`, `04_Phase_02`, `04_Phase_09` (5 files) |
| Humans (478,243 ÷ 580,925) | 82.66% | **82.32%** | same five files (7 occurrences) |
| Robots (434,620 ÷ 594,481) | 73.26% | **73.11%** | same five files (7) |
| Spread, humans minus robots | 9.40 pp | **9.22 pp** | 7 files, 13 occurrences (incl. `04.9_Close-Out`, `04_Phase_10`) |
| People not here (1,175,406 − 912,863) | 254,473 | **262,543** | `00_Frame` |

## ZSO-012 — Workforce, and which split governs in `16`

The pass uses a workforce of **867,096** (100% of robots plus half of the humans), required workforce 308,838 (35.62%), and the split baseline 356,972 · mandated 133,907 · free 376,217 (`04_Phase_04` ×3, `04_Phase_07` ×4, `08_Review_Panel`, `04_Phase_08`, `04_Phase_10`). Live: workforce **884,944** (594,481 + 580,925 ÷ 2 = 884,943.5; `09_Per_City_Baseline_Run.md` L72: required **315,302**, **35.6%**; `16` L275 also carries 884,944). The counts scale by 884,944 ÷ 867,096 = 1.02058: baseline about **364,320**, mandated about **136,663**, free about **383,961**; the shares of `16` §18 (41.2 / 15.4 / 43.4) do not change. **`16` §18 (L1917, "ZHONGSHAN — DETERMINED") governs; the Half B row (L275: 41.2 / 11.8 / 47.1, source `H`) is superseded for Zhongshan.** §18's own counts (396,635 + 148,786 + 418,019 = 963,440) are on the pre-cut workforce; `16` L1 says the per-city determinations were not recomputed.

## ZSO-013 — Footprint and ice share

| | As recorded at the pass | Live (by hand) | Where |
|---|---|---|---|
| Zhongshan's footprint at 10,000 and 7,000 per km² | 115–164 km² | **118–168 km²** (1,175,406 ÷ 10,000 = 117.5; ÷ 7,000 = 167.9) | `07_QA_Gates` |
| The three Larsemann cities together | 353–504 km² | **325–464 km²** (3,246,137 ÷ 10,000 = 324.6; ÷ 7,000 = 463.7) | `02_Spine` (the range as written) |
| Share of the three cities on ice (the ~40 km² oasis ÷ the footprint) | about 89–92% | **about 88–91%** (40 ÷ 325 = 12.3% rock; 40 ÷ 464 = 8.6%) | 5 files, 9 occurrences |

## ZSO-014 — Retired names in the pass

Bunger Hills City is now **Relung Panen** (`00.1_Step_MINUS-1_Input_Contract`); Princess Elisabeth is now **Utstein** (`04_Phase_06`); Port Lockroy and Juan Carlos are now **Puerto Abrigo** and **Pergamino** (`04_Phase_05`); **Vostok** the city is now **Ariun Nuur** (`10_Readiness_Check` ×3, `04_Phase_08` ×2; where it means the district, the real station or the lake it stays); Sejong is now **Contrapunto** (`04_Phase_10`). See `Cities/City_Renames_Alias_Table_2026-10-03.md`.

## ZSO-015 — Spec sentences the pass could lean on have been rewritten

Since the pass, `Specs/Mirny subnet/Zhongshan.md` was edited so that: the sentence on the name's honorific (L71) now ends "The city kept the name of the station it was built on"; the Significant-tier "founding operator heritage" wording no longer appears; the Settled paragraph (L142) rests on the Founding Register and `DR-21`; and L152 states that the Jeju-do court confirmed Zhongshan's Chinese claim. The pass does not rely on the older sentences. The Founding Register row is **L60** (*"The Sinian Federation's (i.e. China's) immediate geographic and time-zone access to the site"*; founders only from the Register, `DR-19`).

## Pre-Trip notes (former `ZSO-001`, `ZSO-002`, `ZSO-005`)

Dated notes were added beside three lines of `00.0_Pre-Trip_Inspection.md`: §E (the headcount to verify: 568,786 H / 582,703 R as recorded; 580,925 H / 594,481 R live); §J `DRQ-11` (353–504 km² and ~89–92% as recorded; 325–464 km² and about 88–91% live); and the runbook size and Step 10 range (the 3,172-line runbook of 2026-10-21; 3,179 lines on 2026-10-30; Step 10 ends at L3152). The raw block of the Pre-Trip is a dated record and was left.

## Source corrections (developer, 2026-10-30)

- **`ZSO-S01` — left in place.** `Extent_and_Density_Per_City.md` L613 (Zhongshan 1,279,433 · 128 · 183), L655 (the −10% scenario, 127,944) and L593 (the three-city sum 3,527,096) are in the 2026-09-05 snapshot table, a dated scenario and a note. Live: 1,175,406 people need **118 km²** at 10,000 per km² and **168 km²** at 7,000.
- **`ZSO-S02` — left in place.** `16` L275 (Half B) and §18 L1917 ff. (counts on the pre-cut workforce): see `ZSO-012`.

---

*Entries filed 2026-10-30 at the developer's direction ("all as recommended").*
