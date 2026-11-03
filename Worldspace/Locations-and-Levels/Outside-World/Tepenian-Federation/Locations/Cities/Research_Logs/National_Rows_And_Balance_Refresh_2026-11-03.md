# National rows and national food balance, after the robot term (2026-11-03, `DR-97`)

All numbers DERIVED (my arithmetic on the rows already in `16` Half B and on file `19`'s inputs). Scratch scripts: `natl.py`, `bal.py` in the session scratchpad. Nothing committed.

## 1 · `16` NATIONAL row and subnet table (workforce-weighted averages of the 38 Half B rows)

Method: for each subnet, Σ(workforce × percent) ÷ Σ(workforce), for base, mandated and free. Second way: Σ round(workforce × percent) as counts, ÷ Σ workforce. Both agree (national 43.13 / 15.34 / 41.53 and 43.13 / 15.34 / 41.53). The old NATIONAL row (42.0 / 15.2 / 42.8 on 24,214,838) and the old subnet table did not reproduce from the old rows either (the previous fork noted this), so the table is rebuilt from the current rows, with Dumont d'Urville at its pre-trim 341,560 as the row prints it.

| | Old | New |
|---|---|---|
| NATIONAL | 24,214,838; 42.0 / 15.2 / 42.8 | 24,211,482; 43.1 / 15.3 / 41.5 (sums 99.9, rounding) |
| Halley | 7,533,054; 43.3 / 10.9 / 45.8 | 7,174,785; 44.4 / 11.4 / 44.2 |
| Mirny | 6,135,002; 40.1 / 15.7 / 44.2 | 6,917,775; 41.6 / 16.0 / 42.4 |
| Mawson | 1,325,638; 40.2 / 17.3 / 42.6 | 1,389,271; 41.1 / 16.8 / 42.0 (99.9) |
| Janbogo | 5,593,850; 44.4 / 15.6 / 40.0 | 5,666,074; 45.3 / 15.4 / 39.3 |
| Palmer | 3,337,241; 39.8 / 21.0 / 39.1 | 2,734,941; 40.9 / 20.7 / 38.4 |
| Byrd | 283,756; 36.2 / 35.1 / 28.7 | 322,340; 37.3 / 34.5 / 28.2 |
| Amundsen | 6,296; 31.8 / 61.4 / 6.8 | 6,296; 33.2 / 60.1 / 6.7 |

Lazar sensitivity: Lazar is 1,817,722 of 7,174,785 (25.3%) of the Halley subnet; a 20% mandate of its distinctive tier (57.9% × 0.2 = 11.6 points of its workforce) lowers the subnet free tier by 25.3% × 11.6 = 2.9 points, 44.2% to about 41.2%.

## 2 · Prose fixed in `16` (line count unchanged, 3,580)

Half B discussion (the Half A free-tier history sentence, the subnet headline, the Lazar sensitivity, the least-free list, the range sentences), Fort McMurdo (illustration table and two free-tier statements), Kunlun (baseline and free statements, the register line), Amundsen Station (6.8% to 6.7%), and a note on the Half A worker-count table that its counts are the 2026-09-02 figures. Left as history: `16` L137 (Half A reference values from `15`), the mandated and free counts in the C/D/H table, Kunlun's two-thirds precompute (marked not recomputed). Coincidences skipped: `09` L205, `16` L605, L659, L1925-type section figures (all 35 city sections' distinctive tiers checked against workforce − new baseline: all match).

## 3 · `19` national food balance: inputs changed, so re-run (`19` section 5)

The food role is a share of the distinctive tier, and the robot term raises every baseline, so the farm workers of Davis (189,548 to 186,131), Esperanza (80,960 to 79,567) and Relung Panen (105,535 to 103,535) all fall; populations and the import need (253,292) did not change. The method reproduces the old figures (427,643 against 427,642). Result: export supply 420,833 (was 427,642), balance +167,541 (+66%, was +69%), slack 7.4% (was 7.7%); without Relung Panen supply 317,298, balance +64,006 (+25%), slack 2.8% (was 3.0%). Shares: Davis 44.2%, Esperanza 18.9%, Relung Panen 24.6%. Pointers updated in `04`, `13`, `17`, `18`.

## 4 · Not done
Conventions A and C of `17` (retained records); the C/D/H mandate-share table recount; Kunlun's two-thirds precompute; `09` needed no prose change.
