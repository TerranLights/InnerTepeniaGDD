# Casey and the other recipient cities: recompute of `16` determinations and `09` rows on current populations (for review, 2026-11-03)

**Status: FOR REVIEW. NOTHING IN `16`, `09`, `13`, `04`, `08`, or any spec or datasheet was edited.** This file is the only thing written. Scratch scripts and JSON are in the session scratchpad, not the repo. No web research.

**Labels.** QUOTED = copied from a file (file and line given). DERIVED = my arithmetic on quoted inputs, shown below. Where I infer why an old number is what it is, I say INFERRED.

## 0 · Headlines for Casey

| | Old (in file) | New (current population) | Difference |
|---|--:|--:|--:|
| Census I residents (QUOTED, `Official_Population_Census.md` Section B, Casey row) | 1,495,731 (before `DR-68`) | **1,547,850** | +52,119 |
| Humans / robots | 733,795 / 761,936 | **760,865 / 786,985** | +27,070 / +25,049 |
| Workforce, robots + 0.5 × humans (DERIVED) | 1,128,834 (`16` §21) | **1,167,418** (same as `09` and Half B) | +38,584 |
| `16` §21 baseline (DERIVED, formula in `16` L122–L132) | 436,698 (38.7%) | **452,244 (38.7%)** | +15,546 |
| `16` §21 distinctive tier (DERIVED) | 692,136 (61.3%) | **715,174 (61.3%)** | +23,038 |
| `16` §21 mandated, 30% of distinctive (DERIVED, share held) | 207,641 (18.4%) | **214,552 (18.4%)** | +6,911 |
| `16` §21 FREE (DERIVED) | 484,495 (42.9%) | **500,622 (42.9%)** | +16,127 |
| `09` §2 Required (DERIVED, `09` L26 formula with B1 = 53) | 387,716 | **395,068** | +7,352 |
| `09` §2 % WF | 33.8% (QUOTED) | **33.8%** (395,068 ÷ 1,167,418 = 33.84%) | none |

**The percentages in `16` §21 do not change** (38.7 / 18.4 / 42.9), because the shares are held and everything scales with the workforce. Only the worker counts are stale. Half B's Casey row (workforce 1,167,418; 38.7% / 18.4% / 42.9%) is already correct.

**Resolution of the `09` puzzle (33.8% against 33.2%).** The `% WF` cell (33.8%) is the *right* one: 395,068 ÷ 1,167,418 = 33.84%. The *Required* cell (387,716) is the stale one. INFERRED: 387,716 is the `09` formula applied to the intermediate `DR-68`-only population (745,935 humans / 773,714 robots, 1,519,649 residents): 745,935 × 0.14443 + 1,519,649 × 0.18424 = 107,737 + 279,985 = 387,722, within 6 of the cell. That intermediate workforce is 773,714 + 372,968 = 1,146,682, the same figure `Population_Work_Prep_2026-11-02.md` L80 quotes. So the 2026-10-28 refresh updated Required for `DR-68`, and the later `DR-90` step (+14,930 humans, +13,271 robots; workforce +20,736) updated only Humans, Residents, Workforce and % WF. The earlier tracker comparison (387,716 ÷ 1,167,418 = 33.2%) therefore mixed two populations.

## 1 · How the two files compute a recipient's row

**`16` (the current method; its own L26–L31 says to take population, workforce and D from `09` and discard `09`'s Required and % WF).** QUOTED, `16` L122–L132:
`workforce = robots + 0.5 × humans`; `baseline = humans × (120.7·f·D + 85.6)/1000 + residents × (64·D + 113.2)/1000`, f = 0.10 for the forced importers (else 1.00); `distinctive = workforce − baseline`; `mandated = distinctive × Σ(provider shares)`; `FREE = distinctive − mandated`.
Inputs from the census: humans, robots, residents (Section B, Census I). Inputs not from the census: D (`09` §2 / `DR-` rulings), f (seven importers; `16` §N says Belgrano is also a forced importer), and each city's mandate share (a ruling per city; held).

**`09` §2 (superseded as a result).** QUOTED, `09` L26: `Required = Humans × (53·D + 85.6)/1000 + Residents × (64·D + 113.2)/1000`, with the circular B1 = 53 and no importer factor. Relung Panen's row (284,173 = formula, 37.7%) is the precedent that the refresh uses this formula.

**Method I used (the Relung Panen precedent, `18` L1 note).** Counts re-run on the current population; shares, rulings and D held; rounding to whole workers. I did *not* change any share.

## 2 · `16` determinations: old counts against counts on the current population (DERIVED)

Cities whose workforce changed by more than 2 workers since the section was written (23 cities including Casey). "Share held" is mandated ÷ distinctive from the section itself. Dumont d'Urville is shown on the live trimmed population (307,404) as well as noted as computed on the pre-trim 341,560 on purpose (`16` L2432 heading); treat its row as information.

| City (`16` section line) | Workforce old → new (Δ) | Share held | Baseline old → new | Mandated old → new | FREE old → new | Shares (base/mand/free) |
|---|---|--:|---|---|---|---|
| Neumayer (L481) | 945,212 → 983,798 (+38,586) | 34.2% | 413,123 → 430,497 | 181,974 → 189,228 | 350,115 → 364,072 | 43.8 / 19.2 / 37.0% |
| Belgrano (L546) | 805,927 → 844,513 (+38,586) | 65.0% | 274,151 → 287,606 | 345,654 → 361,989 | 186,122 → 194,918 | 34.1 / 42.9 / 23.1% |
| Halley (L600) | 1,097,471 → 1,136,056 (+38,585) | 27.5% | 478,952 → 496,326 | 170,093 → 175,926 | 448,426 → 463,804 | 43.7 / 15.5 / 40.8% |
| Abowasa (L652) | 782,122 → 351,435 (-430,687) | 10.0% | 355,900 → 160,747 | 42,622 → 19,069 | 383,600 → 171,620 | 45.7 / 5.4 / 48.8% |
| Sanay (L707) | 347,881 → 386,466 (+38,585) | 72.5% | 154,715 → 172,375 | 140,045 → 155,216 | 53,121 → 58,875 | 44.6 / 40.2 / 15.2% |
| Troll (L761) | 716,590 → 755,174 (+38,584) | 30.0% | 318,227 → 335,886 | 119,509 → 125,787 | 278,854 → 293,502 | 44.5 / 16.7 / 38.9% |
| Princess Elisabeth (L838) | 861,033 → 899,618 (+38,585) | 25.0% | 375,938 → 393,598 | 121,274 → 126,505 | 363,821 → 379,515 | 43.8 / 14.1 / 42.2% |
| Shirayuki (L1754) | 890,079 → 839,654 (-50,425) | 20.0% | 363,971 → 344,044 | 105,222 → 99,122 | 420,886 → 396,488 | 41.0 / 11.8 / 47.2% |
| Sinheung (L1834) | 809,753 → 767,362 (-42,391) | 47.5% | 329,374 → 312,907 | 228,180 → 215,866 | 252,199 → 238,590 | 40.8 / 28.1 / 31.1% |
| Zhongshan (L1917) | 963,440 → 905,680 (-57,760) | 26.2% | 396,635 → 373,442 | 148,786 → 139,712 | 418,019 → 392,526 | 41.2 / 15.4 / 43.3% |
| Davis (L2006) | 876,515 → 915,098 (+38,583) | 47.5% | 357,063 → 373,534 | 246,740 → 257,243 | 272,712 → 284,321 | 40.8 / 28.1 / 31.1% |
| Mirny (L2110) | 1,018,480 → 1,057,064 (+38,584) | 40.0% | 418,565 → 435,036 | 239,966 → 248,811 | 359,949 → 373,216 | 41.2 / 23.5 / 35.3% |
| Casey (L2181) | 1,128,834 → 1,167,418 (+38,584) | 30.0% | 436,698 → 452,244 | 207,641 → 214,552 | 484,495 → 500,621 | 38.7 / 18.4 / 42.9% |
| Kunlun (L2256) | 123,449 → 148,497 (+25,048) | 37.5% | 35,306 → 42,470 | 33,054 → 39,761 | 55,089 → 66,266 | 28.6 / 26.8 / 44.6% |
| Vostok (L2349) | 324,452 → 363,036 (+38,584) | 32.5% | 121,353 → 138,725 | 66,007 → 72,900 | 137,092 → 151,410 | 38.2 / 20.1 / 41.7% |
| Dumont d'Urville (L2432) | 341,559 → 307,404 (-34,155) | 8.3% | 163,966 → 147,570 | 14,799 → 13,319 | 162,794 → 146,515 | 48.0 / 4.3 / 47.7% |
| Denison (L2580) | 804,656 → 722,541 (-82,115) | 35.0% | 428,167 → 385,364 | 131,771 → 118,012 | 244,718 → 219,165 | 53.3 / 16.3 / 30.3% |
| Cape Adare (L2662) | 1,126,671 → 1,165,256 (+38,585) | 37.5% | 466,136 → 482,608 | 247,701 → 255,994 | 412,834 → 426,655 | 41.4 / 22.0 / 36.6% |
| Zukelli (L2744) | 944,859 → 983,442 (+38,583) | 10.0% | 391,579 → 408,050 | 55,328 → 57,539 | 497,952 → 517,854 | 41.5 / 5.9 / 52.7% |
| Janbogo (L2831) | 987,241 → 1,025,824 (+38,583) | 40.0% | 406,082 → 422,552 | 232,464 → 241,309 | 348,695 → 361,963 | 41.2 / 23.5 / 35.3% |
| Dome Fuji (L3186) | 55,072 → 80,120 (+25,048) | 20.0% | 15,046 → 21,889 | 8,005 → 11,646 | 32,021 → 46,585 | 27.3 / 14.5 / 58.1% |
| Mawson (L3263) | 1,091,868 → 1,130,452 (+38,584) | 35.0% | 447,342 → 463,813 | 225,584 → 233,323 | 418,942 → 433,316 | 41.0 / 20.6 / 38.3% |
| Byrd (L3351) | 283,756 → 322,340 (+38,584) | 60.0% | 102,645 → 116,978 | 108,667 → 123,217 | 72,444 → 82,144 | 36.3 / 38.2 / 25.5% |

Notes on the table:
- **Casey**'s row is the one in section 0. The other 22 follow the same method.
- **Abowasa** is "HELD AT CURRENT VALUE" (`16` L652). Its section was written on a workforce of 782,122; the census now gives 351,435 (Santa Luce scenario, `DR-67`/`DR-68`). The old counts are far off, but the hold stands; this is a different kind of staleness from the others and wants a ruling on whether the hold persists.
- **Kunlun** and **Dome Fuji** changed by +25,048 (robots only), the `DR-68` entry in the census.
- **Neumayer, Halley, Vostok, Byrd, Kunlun, Dome Fuji, Belgrano** use f = 0.10. My recomputed base share matches the section's old base share to within 0.1 point for every row except where noted in section 4 below.
- Shares may differ by ±0.1 point between the old and new rows from rounding of D×rate products; counts are rounded to whole workers and may be off by 1.

### Rows that need no recount (workforce unchanged within ±2 workers)

Signy, Sejong, Juan Carlos, Esperanza, Marambio, Palmer City, Port Lockroy, Rothera, Fort McMurdo, Scott, Sayowa, Amundsen Station.

Of these, Esperanza (`DR-90`, 2026-11-02) and Port Lockroy (`DR-89`, 2026-11-02) were already refreshed in their sections. Their small base differences (Esperanza 355,249 against 355,102 on my formula; Port Lockroy 287 against 288) are rounding. The other rows never changed population.

**Not in the numbered sections, so not recomputed here:** Concordia (deferred by the developer, `16` L2511; Half B shows only a Half A estimate, workforce 802,132; its `09` L58 Required cell is also 8,805 below the formula), Lazar (Half A, Group 4, open question `16` L187; Half B workforce 1,817,722 is current), and Relung Panen (separate file `18`, re-run 2026-11-02; its row reproduces exactly: baseline 331,825 = 44.0%).

## 3 · `09` §2 rows: Required cell against the formula on the current population (DERIVED)

`% WF cell` is the quoted cell; `% WF calc` is Required(calc) ÷ the current workforce. A cell is flagged when Required differs by more than 2 workers. The workforce column was already current in every row except Dumont d'Urville (pre-trim, on purpose, per the row's own note).

| City (`09` line) | Required cell | Required calc | Difference | % WF cell | % WF calc |
|---|--:|--:|--:|--:|--:|
| Neumayer (L54) | 485,106 | 496,068 | +10,962 | 50.4% | 50.4% |
| Halley (L55) | 560,759 | 571,721 | +10,962 | 50.3% | 50.3% |
| Denison (L56) | 311,847 | 321,510 | +9,663 | 44.4% | 44.5% |
| Vostok (L57) | 143,796 | 154,757 | +10,961 | 42.0% | 42.6% |
| Concordia (L58) | 318,858 | 327,663 | +8,805 | 40.8% | 40.8% |
| Byrd (L59) | 122,756 | 131,561 | +8,805 | 40.7% | 40.8% |
| Dumont d'Urville (L60) | 138,692 | 124,823 | -13,869 | 40.6% | 40.6% |
| Abowasa (L61) | 128,426 | 136,896 | +8,470 | 38.8% | 39.0% |
| Troll (L62) | 279,026 | 287,210 | +8,184 | 38.0% | 38.0% |
| Sanay (L63) | 139,151 | 147,335 | +8,184 | 38.0% | 38.1% |
| Belgrano (L64) | 312,138 | 320,324 | +8,186 | 37.9% | 37.9% |
| Princess Elisabeth (L65) | 329,183 | 337,366 | +8,183 | 37.5% | 37.5% |
| Cape Adare (L66) | 409,472 | 417,189 | +7,717 | 35.8% | 35.8% |
| Zukelli (L67) | 344,935 | 352,650 | +7,715 | 35.8% | 35.9% |
| Janbogo (L70) | 357,832 | 365,548 | +7,716 | 35.6% | 35.6% |
| Mirny (L71) | 368,677 | 376,393 | +7,716 | 35.6% | 35.6% |
| Zhongshan (L72) | 315,302 | 323,017 | +7,715 | 35.6% | 35.7% |
| Lazar (L74) | 637,974 | 645,690 | +7,716 | 35.5% | 35.5% |
| Mawson (L75) | 393,745 | 401,461 | +7,716 | 35.5% | 35.5% |
| Shirayuki (L78) | 290,137 | 297,848 | +7,711 | 35.4% | 35.5% |
| Davis (L79) | 315,832 | 323,548 | +7,716 | 35.3% | 35.4% |
| Sinheung (L80) | 263,357 | 271,073 | +7,716 | 35.3% | 35.3% |
| Esperanza (L81) | 490,159 | 309,238 | -180,921 | 34.6% | 34.6% |
| Casey (L87) | 387,716 | 395,068 | +7,352 | 33.8% | 33.8% |
| Kunlun (L89) | 38,674 | 42,470 | +3,796 | 28.6% | 28.6% |
| Dome Fuji (L90) | 18,264 | 21,889 | +3,625 | 27.3% | 27.3% |

Rows not listed (Marambio, Fort McMurdo, Signy, Port Lockroy, Scott, Sayowa, Sejong, Juan Carlos, Palmer City, Rothera, Amundsen Station, Relung Panen) already agree with the formula to within 1 worker.

**Observations (DERIVED):**
- In 24 of the 26 flagged rows the cell is lower than the formula by 3,600 to 11,000 workers (the other two are Dumont d'Urville and Esperanza, below), the signature of a Required column left on a smaller population (for Casey, the intermediate `DR-68` population; INFERRED). Lazar, Zhongshan, Shirayuki, Sinheung, Denison and Dumont d'Urville carry other population steps (the −10% and −15% rulings of 2026-09-05); their cells may be on yet other stages, which I did not trace.
- **Esperanza (L81)**: Required 490,159 is on the old 1,878,287-person city; on the current 1,200,000 it is 309,238. This is a large visible error; its % WF (34.6%) is already right.
- **Dumont d'Urville (L60)**: the Required cell (138,692) is the formula on the *pre-trim* pop (223,549 humans / 453,334 residents), consistent with its pre-trim workforce note. On the live population (201,194 humans, 408,001 residents) the formula gives 124,823 and the live workforce is 307,404.
- Several % WF cells differ from the calc by 0.1 point (Denison, Byrd, Abowasa, Sanay, Zukelli, Zhongshan, Shirayuki, Davis) and Vostok by 0.6 point (cell 42.0%, calc 42.6%); small rounding or old-D differences.
- The `09` header (L1) already says the Required and % WF columns "remain the superseded old-B1 model". Recomputing them refreshes a column `16` tells readers to discard.

## 4 · Differences between `09` and `16` as baselines (for Casey, and generally)

| | `09` §2 | `16` Half B and §21 |
|---|---|---|
| Food rate (B1) | 53 per 1,000 humans (circular: a supply figure turned into a demand rate; `10` Finding 1, per `16` L111) | 120.7 per 1,000 humans (`11`), 10% of it for the forced importers |
| Casey baseline on 1,547,850 residents | 395,068 workers = 33.8% of the workforce | 452,244 workers = 38.7% of the workforce |
| Status | superseded as a result (`16` L26–L31) | current |
| Robot-keyed industries (B3 maintenance 12.5 and B4 sustenance 3.25 per 1,000 robots) | added in `09` §3.6 ("COMPLETE", +15.75 per 1,000 robots; Casey 33.8% → 34.9%) | **not in `16`'s formula** (L122–L132 lists no robot term; the source register L41 mentions the rates) |

**Which looks right (not a ruling).** For the baseline, `16`'s B1 = 120.7 looks right: `16` and `10`/`11` say the 53 was circular and instruct readers to use 120.7, and Half B and `18` both run on it. The open point is the robot term. `09` §3.6 declares the model complete only with B3 and B4, and `16`'s formula has no such term. If the robot term were added, Casey's baseline would rise by 786,985 × 15.75 ÷ 1,000 = 12,395 workers (DERIVED) before the distinctive tier is split. I found no sentence in `16` saying the term was dropped deliberately. This applies to every city, not Casey alone, and is a method question for the developer.

**Other disagreements found while checking (outside the task, reported only):**
- **Belgrano**: its `16` section treats it as a forced importer (food term 10%; base 34.0%); Half B and `09` treat it as a grower (base 44.3% in Half B). My recomputed base on the section's treatment is 34.1% of the new workforce; Half B's 44.3% is on the other treatment.
- **Vostok**: Half B base 37.8% against 38.2% by the formula on the current population.
- **Half B MAND% and FREE% are not the determinations'.** For 25 cities Half B's mandated share differs from the section's by more than 0.5 point (examples: Neumayer 9.4% against 19.3%; Mirny 11.8% against 23.6%; Vostok 5.8% against 20.3%; Scott 2.9% against 14.7%; Zukelli 14.6% against 5.9%). Half B's own banner says its figures are Half A estimates; the DR-68 refresh held those. Casey's Half B equals its determination, so Casey is unaffected.

## 5 · Downstream lines that quote the old figures (DERIVED by text search for the old counts; nothing edited)

Search: every old count in section 2 (baseline, mandated, FREE, distinctive, workforce) and the `09` Required cell, formatted with commas, across all `.md` files under `Worldspace/` except `graphify-out/`. A hit is a line containing the number; a few may be coincidences (the same number used for something else), so each needs reading before it is changed.

### Casey (all hits, 48)

| File (under `Cities/` unless noted) | Line | Old figure | What it is |
|---|--:|---|---|
| `Population_Work_Prep_2026-11-02.md` | 80 | workforce 1,128,834 | record: ledger item CASEY-S05 (records the open item) |
| `Research_Logs/TEPENIA_Research_Tracker_and_Handoff.md` | 320 | baseline 436,698; mandated 207,641; free 484,495; workforce 1,128,834; 09 Required 387,716 | record: tracker S.0y Casey check |
| `Division_of_Industry/09_Per_City_Baseline_Run.md` | 87 | 09 Required 387,716 | the `09` row (Required cell) |
| `Division_of_Industry/16_Per_City_Three_Tier_Run.md` | 2185 | baseline 436,698 | §21 tier table |
| `Division_of_Industry/16_Per_City_Three_Tier_Run.md` | 2186 | mandated 207,641 | §21 tier table |
| `Division_of_Industry/16_Per_City_Three_Tier_Run.md` | 2187 | free 484,495 | §21 tier table |
| `Division_of_Industry/16_Per_City_Three_Tier_Run.md` | 2189 | distinctive 692,136 | §21 distinctive tier line |
| `Division_of_Industry/16_Per_City_Three_Tier_Run.md` | 2196 | mandated 207,641 | §21 mandate table |
| `Division_of_Industry/04_Providers_and_National_Balance.md` | 27 | workforce 1,128,834 | national balance input table (old humans 733,795 and workforce) |
| `Division_of_Industry/04_Providers_and_National_Balance.md` | 204 | workforce 1,128,834 | national balance table (workforce) |
| `Division_of_Industry/08_Volume_Based_Requirement_Reference.md` | 501 | workforce 1,128,834 | rate-table worked example, old population |
| `Division_of_Industry/13_National_Balance_Under_the_Ruling.md` | 373 | baseline 436,698; workforce 1,128,834 | national food-balance table row (workforce, baseline) |
| `City_Development_Passes/Mirny_Subnet/Casey/Datasheets/Phase_7.md` | 55 | baseline 436,698; mandated 207,641; free 484,495; distinctive 692,136 | Casey datasheet row quoting §21 |
| `City_Development_Passes/Mirny_Subnet/Casey/Datasheets/Phase_7.md` | 56 | baseline 436,698; mandated 207,641; free 484,495; workforce 1,128,834 | Casey datasheet row; already notes the counts predate DR-68 |
| `City_Development_Passes/Mirny_Subnet/Casey/Datasheets/Phase_4.md` | 21 | 09 Required 387,716 | Casey datasheet row quoting `09`; already notes only Humans, Residents, Workforce were refreshed (and per section 0 the Required cell is on the intermediate `DR-68` population) |
| `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Casey_Audit.md` | 62 | baseline 436,698; mandated 207,641; free 484,495; workforce 1,128,834 | record of the 2026-10-29 Manual Input Audit |
| `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Casey_Audit.md` | 82 | 09 Required 387,716 | record of the 2026-10-29 Manual Input Audit |
| `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Casey_Audit.md` | 96 | workforce 1,128,834 | record of the 2026-10-29 Manual Input Audit |
| `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Casey_Audit.md` | 107 | workforce 1,128,834 | record of the 2026-10-29 Manual Input Audit |
| `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/FIX_LEDGER.md` | 109 | workforce 1,128,834 | record of the 2026-10-29 Manual Input Audit |
| `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/FIX_LEDGER.md` | 119 | workforce 1,128,834 | record of the 2026-10-29 Manual Input Audit |
| `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/FIX_LEDGER.md` | 144 | workforce 1,128,834 | record of the 2026-10-29 Manual Input Audit |
| `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Sweep_Reports/CHECK_Casey_Independent.md` | 45 | baseline 436,698; mandated 207,641; free 484,495; distinctive 692,136; workforce 1,128,834 | record of the 2026-10-29 Manual Input Audit |
| `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Sweep_Reports/Casey_Sweep.md` | 34 | workforce 1,128,834 | record of the 2026-10-29 Manual Input Audit |
| `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Sweep_Reports/Casey_Sweep.md` | 44 | workforce 1,128,834 | record of the 2026-10-29 Manual Input Audit |
| `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Sweep_Reports/Casey_Sweep.md` | 52 | baseline 436,698; mandated 207,641; free 484,495; distinctive 692,136; workforce 1,128,834 | record of the 2026-10-29 Manual Input Audit |

Not hit but relevant: Casey's `00.0_Pre-Trip_Inspection.md` and the spec carry no old §21 counts (no hit). The Casey sheets that quote `16` and `09` (Phase_4 L21, Phase_7 L55–L56) already flag their own staleness, so they would need the new counts and, for Phase_4 L21, the corrected Required cell and the DR-90 note, not a new warning. The Manual Input Audit files are records of what was true on 2026-10-29 and are normally left alone.

### The other 22 cities (counts of lines holding an old figure, by kind of file)

| City | `16` sections | `09` row | other Division_of_Industry files | city datasheets | City_Master_Reference | records and scratch | other |
|---|--:|--:|--:|--:|--:|--:|--:|
| Neumayer | 5 | 1 | 3 | 16 | 0 | 9 | 0 |
| Belgrano | 7 | 1 | 0 | 16 | 0 | 5 | 0 |
| Halley | 5 | 1 | 2 | 13 | 0 | 10 | 0 |
| Abowasa | 4 | 1 | 2 | 13 | 0 | 9 | 0 |
| Sanay | 5 | 1 | 1 | 13 | 0 | 7 | 0 |
| Troll | 5 | 1 | 0 | 13 | 0 | 8 | 0 |
| Princess Elisabeth | 8 | 1 | 2 | 13 | 0 | 9 | 0 |
| Shirayuki | 5 | 1 | 0 | 0 | 0 | 17 | 10 |
| Sinheung | 5 | 1 | 0 | 0 | 0 | 16 | 0 |
| Zhongshan | 5 | 1 | 0 | 0 | 0 | 23 | 7 |
| Davis | 5 | 1 | 4 | 2 | 0 | 14 | 9 |
| Mirny | 5 | 1 | 0 | 6 | 2 | 316 | 60 |
| Kunlun | 6 | 1 | 8 | 17 | 3 | 25 | 18 |
| Vostok | 5 | 1 | 3 | 16 | 2 | 14 | 0 |
| Dumont d'Urville | 5 | 1 | 1 | 7 | 0 | 19 | 0 |
| Denison | 5 | 1 | 3 | 9 | 2 | 16 | 0 |
| Cape Adare | 5 | 1 | 2 | 14 | 2 | 21 | 0 |
| Zukelli | 5 | 1 | 1 | 11 | 2 | 27 | 0 |
| Janbogo | 5 | 1 | 1 | 16 | 2 | 20 | 1 |
| Dome Fuji | 4 | 1 | 4 | 12 | 3 | 22 | 21 |
| Mawson | 5 | 1 | 0 | 16 | 1 | 23 | 0 |
| Byrd | 7 | 1 | 1 | 16 | 1 | 21 | 1 |

Per-city line lists are reproducible with the scratch script (`recompute.py` and the search step in the session scratchpad). I did not list them line by line here, because the large counts for Mirny (390, mostly T8 reader scratch files) and Kunlun and Dome Fuji (many are the same small round numbers used in unrelated places) would bury the real follow-ups. **Likely coincidence hits to read before trusting:** Kunlun and Dome Fuji (low-count figures), Mirny (T8 scratch). The files that clearly need to follow, for every one of the 22 other cities, are `16` (own section), `09` (own row), and the city's `Datasheets/Phase_4.md`, `Phase_7.md` and `Step_1_and_2.md` where they hit; for Abowasa the hits are in the Santa Luce folder and for Princess Elisabeth in the Utstein folder.

## 6 · Open questions for the developer (no ruling made here)

1. Apply the recount to all 23 cities (Casey and the 22 others) `16` sections with the method above (counts only; shares, D, rulings held), or only to Casey now?
2. For `09` §2: refresh the Required column on the formula (B1 = 53) as done for Relung Panen, or mark the column "superseded, not maintained" since `16` tells readers to discard it?
3. Abowasa's hold: keep the old counts (they are on a workforce more than twice the current one), or recount it like the others?
4. The robot-keyed term (B3 + B4, 15.75 per 1,000 robots) that `09` §3.6 added and `16` does not carry: deliberate or dropped?
5. Belgrano: grower or forced importer in Half B (the section says importer).
6. Casey's national-balance lines in `04` L27 and L204, `13` L373 and `08` L501 sit on the old population; they belong to the national balance refresh (`19`), not to this recompute.

