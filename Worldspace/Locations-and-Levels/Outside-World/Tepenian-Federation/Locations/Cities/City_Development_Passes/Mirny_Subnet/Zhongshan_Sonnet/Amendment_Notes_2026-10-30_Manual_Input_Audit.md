# Zhongshan (Sonnet folder) — amendment notes, 2026-10-30 (manual input audit)

**What this file is.** Zhongshan's Sonnet-folder partial trial (Step −1 to Phase 3) was run on 2026-09-11 (Pre-Trip refreshed 2026-10-21). **No pass file is edited by this note, and none was.** Each entry says what has changed in one of Zhongshan's sources since the pass, where the pass rests on the old state, and the live value (recomputed by hand from the live files on 2026-10-30). The old values are kept as "as recorded at the pass (2026-09-11)". The counts of occurrences are from a search of the pass files for the old numbers and may miss a differently worded one.

**Developer decisions of 2026-10-30.** Added after the walk-through (*"all as recommended"*). The Pre-Trip received dated notes beside three stale lines (§E headcount check, §J footprint line, the runbook size and Step 10 range); nothing else in it was changed. Evidence: `Manual_Input_Audit_2026-10-29/Zhongshan_Audit.md` and `FIX_LEDGER.md`. The pass is to be re-analyzed with the current methods (see the Weekly To-Do); this file is the interim record.

---

## ZSS-010 — The census scenario of 2026-10-28 (`DR-68`) rescaled Zhongshan's population

| | As recorded at the trial (2026-09-11) | Live since `DR-68` (census L490 and L610) | Files in the trial that carry the old value |
|---|---|---|---|
| Census I humans | 568,786 | **580,925** | 3 |
| Census I robots | 582,703 | **594,481** | 3 |
| Census I combined | 1,151,489 | **1,175,406** | 4 (9 occurrences) |
| Census II humans | 470,135 | **478,243** | 3 |
| Census II robots | 426,881 | **434,620** | 3 |
| Census II combined | 897,016 | **912,863** | 4 (7 occurrences) |

## ZSS-011 — Retention figures derived from the old set (recomputed by hand)

| | As recorded at the trial | Live | Where |
|---|---|---|---|
| Combined (912,863 ÷ 1,175,406) | 77.90% | **77.66%** | `00_Frame`, `01_Inherited`, `02_Spine`, `04_Phase_02` |
| Humans (478,243 ÷ 580,925) | 82.66% | **82.32%** | same four files (5 occurrences) |
| Robots (434,620 ÷ 594,481) | 73.26% | **73.11%** | same four files (5) |
| Spread, humans minus robots | 9.40 pp | **9.22 pp** | same four files, 8 occurrences |
| People not here (1,175,406 − 912,863) | 254,473 | **262,543** | `00_Frame` |

## ZSS-012 — Oasis figures

The trial's "~89–92%" of the three cities on ice (`00_Frame`, `02_Spine` ×2, `04_Phase_03`; 4 occurrences) and the range 353–504 km² (`02_Spine`) are, with the Census I of 2026-10-30, **325–464 km²** and about **88–91%** on ice (3,246,137 ÷ 10,000 = 324.6; ÷ 7,000 = 463.7; the ~40 km² oasis is 12.3% to 8.6% of that).

## ZSS-013 — Retired name

Bunger Hills City (`00.1_Step_MINUS-1_Input_Contract`, once) is now **Relung Panen** (`Cities/City_Renames_Alias_Table_2026-10-03.md`).

## ZSS-014 — Scope of the trial

The trial stops at Phase 3 (nine files: Step −1 to Phase 3). It has no workforce, no `16` figures and no Phase 4–10 files, so the workforce, Half B and §18 entries of the Opus folder's note do not apply here.

## Pre-Trip notes (the same lines as the Opus folder's)

Dated notes were added beside the same three lines of `00.0_Pre-Trip_Inspection.md` (this Pre-Trip is the same text as the Opus one): §E headcount (as recorded 568,786 H / 582,703 R; live 580,925 H / 594,481 R), §J `DRQ-11` (live 325–464 km², about 88–91%) and the runbook size / Step 10 range (as of 2026-10-21; 3,179 lines and Step 10 ending at L3152 on 2026-10-30). The Pre-Trip's verification line (105 of 110 addresses resolve; the five missing are outputs of steps the trial did not reach) was left.

---

*Entries filed 2026-10-30 at the developer's direction ("all as recommended"). The Extent-file lines and `16` entries are recorded in the Opus folder's note.*
