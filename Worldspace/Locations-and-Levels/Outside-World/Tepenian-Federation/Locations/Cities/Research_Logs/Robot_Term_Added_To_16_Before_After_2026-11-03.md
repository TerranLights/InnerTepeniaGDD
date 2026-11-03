# The robot term added to `16`: before and after (2026-11-03, `DR-96`)

**Status: APPLIED to `16`, `09` (section 3.6 table and range) and `18` (Relung Panen). Nothing committed.** Every number below marked DERIVED is my arithmetic from the census populations (`09` section 2 columns Humans and Residents, Census I) and the formula in `16`. Developer ruling (verbatim, 2026-11-03): *"For the robot term, the omission was probably an accident. Include the robot maintenance sector."*

## What was done

- **Formula (DERIVED, mirrors `09` §3.6):** `baseline = humans × (120.7·f·D + 85.6)/1000 + residents × (64·D + 113.2)/1000 + robots × 15.75/1000`, with robots = residents − humans, 15.75 = B3 maintenance 12.5 + B4 sustenance 3.25 per 1,000 robots. Workforce is unchanged (robots + 0.5 × humans). Edited in place in `16` (no lines added).
- **Held:** each city's mandate **share of the distinctive tier** (as the sections state it), so mandated and free counts fall in proportion to the smaller distinctive tier; itemized mandate rows scale with it and still sum to the mandated total.
- **Scope in `16`:** the tier tables, the distinctive line and the itemized mandate rows of all 35 city sections; a dated note at the end of each section's distinctive paragraph with the old counts; Half B rows (percentage points added = robot term ÷ workforce; Relung Panen and Abowasa set to their recounted values); Abowasa's three-readings table; Princess Elisabeth's f=1.00 and f=0.10 rows; end-of-pass register rows 1 and 4; header note.
- **Abowasa (item 2):** recounted on workforce 351,435 (the counts had been computed on 782,122). **The 10%-of-distinctive mandate stays HELD**, because the hold in the section is the developer's own direction of 2026-09-02 about the rate, not a population issue; the heading text *"HELD AT CURRENT VALUE"* is unchanged because the Santa Luce datasheets quote it.
- **Princess Elisabeth's hypothetical row (item 3):** the old f=0.10 figures (289,915 / 571,118) did not reproduce from the file's own formula on the current population even before the robot term (the formula gives 303,370 baseline without it), so they were stale; recomputed with the robot term: **312,965 baseline (34.8%) / 586,654 distinctive (65.2%)**; the f=1.00 row is 403,193 (44.8%) / 496,426 (55.2%).
- **`09`:** section 2's Required and % WF cells (old B1 = 53 model, refreshed earlier today) are unchanged. Section 3.6's table (§2 + robot term) was recomputed from those cells; the 2026-09 values were up to 0.1 point off. The two files now agree on the robot term and still differ on B1 (53 vs 120.7), so their baselines are not the same quantity.
- **`18` (Relung Panen):** robot term added; food workers 105,535 → 103,535; see the table below.

## Per city: before and after (DERIVED)

| City | Workforce | Robot term | Baseline old → new | Mandated old → new | Free old → new | Baseline / mandated / free % of workforce, new |
|---|--:|--:|---|---|---|---|
| Neumayer | 983,798 | 10,448 | 440,945 → 440,945 | 185,655 → 185,655 | 357,198 → 357,198 | 44.8 / 18.9 / 36.3 |
| Belgrano | 844,513 | 8,899 | 296,505 → 296,505 | 356,205 → 356,205 | 191,803 → 191,803 | 35.1 / 42.2 / 22.7 |
| Halley | 1,136,057 | 12,090 | 508,416 → 508,416 | 172,601 → 172,601 | 455,040 → 455,040 | 44.7 / 15.2 / 40.1 |
| Abowasa | 351,435 | 3,734 | 164,480 → 164,480 | 18,696 → 18,696 | 168,259 → 168,259 | 46.8 / 5.3 / 47.9 |
| Sanay | 386,466 | 4,050 | 176,425 → 176,425 | 152,280 → 152,280 | 57,761 → 57,761 | 45.7 / 39.4 / 14.9 |
| Troll | 755,175 | 7,935 | 343,821 → 343,821 | 123,406 → 123,406 | 287,948 → 287,948 | 45.5 / 16.4 / 38.1 |
| Princess Elisabeth | 899,619 | 9,595 | 403,193 → 403,193 | 124,107 → 124,107 | 372,319 → 372,319 | 44.8 / 13.8 / 41.4 |
| Signy | 142,127 | 1,505 | 59,985 → 59,985 | 45,178 → 45,178 | 36,964 → 36,964 | 42.2 / 31.8 / 26.0 |
| Sejong | 486,488 | 5,168 | 196,690 → 196,690 | 72,450 → 72,450 | 217,348 → 217,348 | 40.4 / 14.9 / 44.7 |
| Juan Carlos | 291,821 | 3,102 | 117,915 → 117,915 | 69,562 → 69,562 | 104,344 → 104,344 | 40.4 / 23.8 / 35.8 |
| Esperanza | 894,835 | 9,287 | 364,390 → 364,390 | 225,439 → 225,439 | 305,006 → 305,006 | 40.7 / 25.2 / 34.1 |
| Marambio | 428,548 | 4,518 | 181,720 → 181,720 | 172,780 → 172,780 | 74,048 → 74,048 | 42.4 / 40.3 / 17.3 |
| Palmer City | 249,852 | 2,629 | 100,376 → 100,376 | 62,282 → 62,282 | 87,194 → 87,194 | 40.2 / 24.9 / 34.9 |
| Port Lockroy | 701 | 7 | 295 → 295 | 20 → 20 | 386 → 386 | 42.1 / 2.8 / 55.1 |
| Rothera | 240,569 | 2,578 | 96,382 → 96,382 | 72,094 → 72,094 | 72,093 → 72,093 | 40.0 / 30.0 / 30.0 |
| Shirayuki | 839,655 | 8,926 | 352,970 → 352,970 | 97,337 → 97,337 | 389,348 → 389,348 | 42.0 / 11.6 / 46.4 |
| Sinheung | 767,363 | 8,193 | 321,100 → 321,100 | 211,975 → 211,975 | 234,288 → 234,288 | 41.9 / 27.6 / 30.5 |
| Zhongshan | 905,680 | 9,572 | 383,014 → 383,014 | 137,200 → 137,200 | 385,466 → 385,466 | 42.3 / 15.1 / 42.6 |
| Davis | 915,098 | 9,761 | 383,295 → 383,295 | 252,606 → 252,606 | 279,197 → 279,197 | 41.9 / 27.6 / 30.5 |
| Mirny | 1,057,064 | 11,192 | 446,228 → 446,228 | 244,334 → 244,334 | 366,502 → 366,502 | 42.2 / 23.1 / 34.7 |
| Casey | 1,167,418 | 12,395 | 464,639 → 464,639 | 210,834 → 210,834 | 491,945 → 491,945 | 39.8 / 18.1 / 42.1 |
| Kunlun | 148,497 | 2,339 | 44,809 → 44,809 | 38,883 → 38,883 | 64,805 → 64,805 | 30.2 / 26.2 / 43.6 |
| Vostok | 363,036 | 4,484 | 143,209 → 143,209 | 71,444 → 71,444 | 148,383 → 148,383 | 39.4 / 19.7 / 40.9 |
| Dumont d'Urville | 341,560 | 3,619 | 167,585 → 167,585 | 14,498 → 14,498 | 159,477 → 159,477 | 49.1 / 4.2 / 46.7 |
| Denison | 722,541 | 7,666 | 393,030 → 393,030 | 115,329 → 115,329 | 214,182 → 214,182 | 54.4 / 16.0 / 29.6 |
| Cape Adare | 1,165,257 | 12,265 | 494,873 → 494,873 | 251,394 → 251,394 | 418,990 → 418,990 | 42.5 / 21.6 / 35.9 |
| Zukelli | 983,443 | 10,334 | 418,383 → 418,383 | 56,506 → 56,506 | 508,554 → 508,554 | 42.5 / 5.8 / 51.7 |
| Janbogo | 1,025,824 | 10,852 | 433,404 → 433,404 | 236,968 → 236,968 | 355,452 → 355,452 | 42.2 / 23.1 / 34.7 |
| Fort McMurdo | 334,215 | 3,514 | 142,090 → 142,090 | 115,275 → 115,275 | 76,850 → 76,850 | 42.5 / 34.5 / 23.0 |
| Scott | 291,103 | 3,090 | 122,554 → 122,554 | 42,137 → 42,137 | 126,412 → 126,412 | 42.1 / 14.5 / 43.4 |
| Sayowa | 178,698 | 2,079 | 72,323 → 72,323 | 74,463 → 74,463 | 31,912 → 31,912 | 40.5 / 41.7 / 17.8 |
| Dome Fuji | 80,120 | 1,262 | 23,151 → 23,151 | 11,394 → 11,394 | 45,575 → 45,575 | 28.9 / 14.2 / 56.9 |
| Mawson | 1,130,453 | 12,002 | 475,815 → 475,815 | 229,123 → 229,123 | 425,515 → 425,515 | 42.1 / 20.3 / 37.6 |
| Byrd | 322,340 | 3,397 | 120,375 → 120,375 | 121,179 → 121,179 | 80,786 → 80,786 | 37.3 / 37.6 / 25.1 |
| Amundsen Station | 6,297 | 90 | 2,093 → 2,093 | 3,784 → 3,784 | 420 → 420 | 33.2 / 60.1 / 6.7 |
| Relung Panen | 753,964 | 7,999 | 331,825 → 339,824 | 164,634 → 161,514 | 257,505 → 252,626 | 45.1 / 21.4 / 33.5 |

Notes: percentages are rounded to 0.1 with the sum forced to 100.0 (largest remainder), so a cell can differ by 0.1 from count ÷ workforce. Esperanza's old baseline in the file (355,249) was 147 above the formula (355,102); the new figure follows the formula. Port Lockroy's mandate is 5% of 406 = 20 (was 21 on 414). Dumont d'Urville stays on the pre-trim workforce 341,560 by design. Relung Panen's mandated total is the sum of its five rows (161,514), not 39% rounded (161,515).

### Relung Panen (`18`) rows (DERIVED)

| Role | Share | Old | New |
|---|--:|--:|--:|
| Food production | 25% | 105,535 | 103,535 |
| Agricultural research | 4% | 16,886 | 16,566 |
| Seed breeding | 3% | 12,664 | 12,424 |
| Phosphorus and soil recovery | 6% | 25,328 | 24,848 |
| Cold-chain logistics | 1% | 4,221 | 4,141 |
| **Mandate total** | **39%** | **164,634** | **161,514** |
| Baseline | | 331,825 (44.0%) | 339,824 (45.1%) |
| Distinctive | | 422,139 | 414,140 |
| **Free** | | 257,505 (34.2%) | **252,626 (33.5%)** |

**Ripple to check:** Relung Panen's food workers are an input to the national food balance (`19`, `17`, and the figures quoted in `18` section 4); at 103,535 instead of 105,535 they are 1.9% lower. Not re-run.

### Half B rows (DERIVED; mandate shares held)

| City | base% old → new | MAND% old → new | FREE% old → new |
|---|---|---|---|
| Amundsen Station | 31.8 → 33.2 | 61.4 → 60.1 | 6.8 → 6.7 |
| Fort McMurdo | 41.5 → 42.6 | 35.1 → 34.4 | 23.4 → 23.0 |
| Marambio | 41.3 → 42.4 | 35.2 → 34.5 | 23.5 → 23.1 |
| Belgrano | 44.3 → 45.4 | 30.6 → 30.0 | 25.1 → 24.6 |
| Sayowa | 39.3 → 40.5 | 33.4 → 32.7 | 27.3 → 26.8 |
| Sanay | 44.5 → 45.5 | 27.8 → 27.3 | 27.8 → 27.2 |
| Byrd | 36.2 → 37.3 | 35.1 → 34.5 | 28.7 → 28.2 |
| Janbogo | 41.1 → 42.2 | 29.4 → 28.9 | 29.4 → 28.9 |
| Sinheung | 40.7 → 41.8 | 26.7 → 26.2 | 32.6 → 32.0 |
| Relung Panen | 44.0 → 45.1 | 21.8 → 21.4 | 34.2 → 33.5 |
| Denison | 53.2 → 54.3 | 11.7 → 11.4 | 35.1 → 34.3 |
| Esperanza | 39.7 → 40.7 | 24.1 → 23.7 | 36.2 → 35.6 |
| Rothera | 39.0 → 40.1 | 24.4 → 24.0 | 36.6 → 35.9 |
| Davis | 40.8 → 41.9 | 20.7 → 20.3 | 38.5 → 37.8 |
| Troll | 44.4 → 45.5 | 16.7 → 16.4 | 38.9 → 38.1 |
| Signy | 41.1 → 42.2 | 17.7 → 17.4 | 41.2 → 40.4 |
| Princess Elisabeth | 43.7 → 44.8 | 14.1 → 13.8 | 42.2 → 41.4 |
| Juan Carlos | 39.3 → 40.4 | 18.2 → 17.9 | 42.5 → 41.7 |
| Casey | 38.7 → 39.8 | 18.4 → 18.1 | 42.9 → 42.1 |
| Zukelli | 41.5 → 42.6 | 14.6 → 14.3 | 43.9 → 43.1 |
| Cape Adare | 41.4 → 42.5 | 14.7 → 14.4 | 44.0 → 43.1 |
| Concordia | 48.3 → 49.4 | 7.8 → 7.6 | 44.0 → 43.0 |
| Mawson | 41.0 → 42.1 | 14.8 → 14.5 | 44.3 → 43.4 |
| Sejong | 39.4 → 40.5 | 15.2 → 14.9 | 45.5 → 44.6 |
| Neumayer | 43.7 → 44.8 | 9.4 → 9.2 | 46.9 → 46.0 |
| Halley | 43.7 → 44.8 | 9.4 → 9.2 | 47.0 → 46.0 |
| Zhongshan | 41.2 → 42.3 | 11.8 → 11.6 | 47.1 → 46.1 |
| Mirny | 41.1 → 42.2 | 11.8 → 11.6 | 47.1 → 46.2 |
| Shirayuki | 40.9 → 42.0 | 11.8 → 11.6 | 47.3 → 46.4 |
| Abowasa | 45.6 → 46.8 | 5.4 → 5.3 | 49.0 → 47.9 |
| Dumont d'Urville | 48.0 → 49.1 | 0.0 → 0.0 | 52.0 → 50.9 |
| Scott | 41.0 → 42.1 | 2.9 → 2.8 | 56.0 → 55.1 |
| Port Lockroy | 41.0 → 42.1 | 2.9 → 2.8 | 56.0 → 55.1 |
| Vostok | 37.8 → 39.0 | 5.8 → 5.7 | 56.5 → 55.3 |
| Dome Fuji | 27.3 → 28.9 | 14.5 → 14.2 | 58.1 → 56.9 |
| Lazar | 41.0 → 42.1 | 0.0 → 0.0 | 59.0 → 57.9 |
| Palmer City | 39.1 → 40.2 | 0.0 → 0.0 | 60.9 → 59.8 |
| Kunlun | 28.6 → 30.2 | 0.0 → 0.0 | 71.4 → 69.8 |

The NATIONAL row and the subnet table in `16` were not recomputed (they did not reproduce from the rows before this change). Workforce-weighted from the rows: before 42.0 / 15.6 / 42.4 (base / mand / free), after 43.1 / 15.3 / 41.5.

## Left stale on purpose (inside `16`)
- Prose that quotes percentages from the old counts (Half B discussion, ranges such as 6.8%–71.4%, the C/D/H table, Troll and Davis and Kunlun options in the end-of-pass register, and sensitivity tables inside sections other than Abowasa and Princess Elisabeth).
- Half B MAND%/FREE% for the 25 cities whose Half A estimates differ from their later section determinations (unchanged policy).

## OTHER files that quote the old numbers (file : line : number : city and quantity)

These were not edited. Counts below are exact-number matches of the old baseline, mandated, free and distinctive figures (and Relung Panen's old role counts) outside `16`, `09` and `18`.

- `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/Datasheets/Phase_5.md`: L24 4,221 (Relung Panen cold chain 1%)
- `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Relung_Panen/Datasheets/Phase_7.md`: L20 331,825 (Relung Panen baseline); L20 422,139 (Relung Panen distinctive); L21 105,535 (Relung Panen food workers); L21 16,886 (Relung Panen agri research/4% cold chain); L21 12,664 (Relung Panen seed); L21 25,328 (Relung Panen phosphorus); L21 4,221 (Relung Panen cold chain 1%); L22 164,634 (Relung Panen mandated); L23 331,825 (Relung Panen baseline); L23 164,634 (Relung Panen mandated); L23 257,505 (Relung Panen free); L24 4,221 (Relung Panen cold chain 1%) …
- `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Division_of_Industry/19_National_Balance_Refresh_2026-11-02.md`: L13 422,139 (Relung Panen distinctive); L13 105,535 (Relung Panen food workers)
- `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Relung_Panen/ULM_Input_Status.md`: L279 105,535 (Relung Panen food workers)
- `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Casey_and_Recipients_Recompute_For_Review_2026-11-03.md`: L78 331,825 (Relung Panen baseline)
- `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Relung_Panen_Ethnic_Origin_EO1_East_Asia_2026-10-29.md`: L222 4,221 (Relung Panen cold chain 1%)
- `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Relung_Panen_Held_Edits_Diffs_For_Review_2026-11-03.md`: L11 16,886 (Relung Panen agri research/4% cold chain); L11 4,221 (Relung Panen cold chain 1%); L38 4,221 (Relung Panen cold chain 1%); L134 4,221 (Relung Panen cold chain 1%); L160 331,825 (Relung Panen baseline); L160 422,139 (Relung Panen distinctive); L164 422,139 (Relung Panen distinctive); L164 4,221 (Relung Panen cold chain 1%); L165 164,634 (Relung Panen mandated); L165 422,139 (Relung Panen distinctive); L165 4,221 (Relung Panen cold chain 1%); L167 164,634 (Relung Panen mandated) …
- `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Relung_Panen_Open_Items_Proposals_For_Approval_2026-11-02.md`: L129 16,886 (Relung Panen agri research/4% cold chain); L129 4,221 (Relung Panen cold chain 1%)
- `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/Relung_Panen_Round2_Findings_and_Amendments_For_Approval_2026-11-02.md`: L15 16,886 (Relung Panen agri research/4% cold chain); L76 105,535 (Relung Panen food workers); L118 16,886 (Relung Panen agri research/4% cold chain); L120 12,664 (Relung Panen seed); L120 4,221 (Relung Panen cold chain 1%)
- `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/TEPENIA_Research_Tracker_and_Handoff.md`: L303 105,535 (Relung Panen food workers); L338 4,221 (Relung Panen cold chain 1%)
- `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Relung_Panen.md`: L263 4,221 (Relung Panen cold chain 1%)
- `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Specs/Mirny subnet/Sinheung.md`: L101 14,498 (Dumont d'Urville mandated)
- `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Infrastructure/Airports.md`: L22 4,221 (Relung Panen cold chain 1%)
- `Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md`: L1623 16,886 (Relung Panen agri research/4% cold chain); L1633 16,886 (Relung Panen agri research/4% cold chain); L1633 4,221 (Relung Panen cold chain 1%)
- `Worldspace/Locations-and-Levels/Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/Contrapunto_Audit.md`: L16 234,288 (Sinheung free)
