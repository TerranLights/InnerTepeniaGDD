# National food balance and slack, refreshed for the new populations (2026-10-28)

> **Status: A REFRESH RECORD. No existing Division of Industry file was rewritten** (only a one-line pointer was added to the title of `13`). Written after the Santa Luce population scenario was applied to the census (`DR-68`, `DR-69`). **Not a new model:** it re-runs the method of `13` §15 on today's Census I populations, and shows the result under the three conventions the folder itself uses for the producers' workforce, because the folder has never settled which is right (`16`, Register item 11: *"the denominator must be settled in the end-of-pass re-run"*). **The standing caution of `13` §15 applies unchanged: do not quote the balance to three significant figures.**

## 0 · What "slack" means (the folder's own term, `13` §15)

**Slack = export capacity − the forced importers.** *Export capacity* is how many people in total the food export sector (Davis, Esperanza, the terraformed belt, the fishery) could feed. The *forced importers* are the people in cities that physically cannot grow their own food (Halley, Neumayer, Vostok, Byrd, Amundsen Station). What is left is the number of people living in cities that **could** grow food but are **not required** to: they can stop growing their own food, specialize in something else, and still eat. After the refresh that is **about 1.14 million people (7.3% of national humans)** under the convention written in `13`. The folder calls it "the Federation's entire economic freedom of maneuver in food": a finite budget the per-city pass spends by deciding which cities specialize away from food. **It is a capacity counted in people who could be fed, not stored food and not actual surplus production.**

## 1 · The method (reproduced from `13`, and checked)

- **Import need** = the humans in the geologically forced importers × 0.1207 × 1.20 (the food rate per human, growing at the mild-coast difficulty). Forced importers: **Halley, Neumayer, Vostok, Byrd, Amundsen Station**; Kunlun and Dome Fuji have no humans. *Check: the old humans (1,640,490) give 237,603, against the file's 237,609.*
- **Supply** = Davis agriculture (35%) + Esperanza agriculture (15%) + the terraformed belt (36,000) + marine capture at its cap (15,600).
- **Export capacity (people fed)** = supply ÷ (0.1207 × 1.20). **Slack** = capacity − the forced importers' humans, shown as a share of the 15,623,523 national humans.
- **What the new populations change.** The forced importers' humans rise from **1,640,490 to 1,689,045** (+48,555), so import need rises from **237,609 to 244,641**. Davis's and Esperanza's workforces each rise by 17,848 (about 2.0% and 1.3%), so supply rises a little. The belt and the fishery are fixed.

## 1b · How the three tiers are computed (from `16`)

1. **Workforce** = robots + 0.5 × humans (each robot counts as one worker, each human as half).
2. **Baseline** (tier one): the jobs a city must staff just to exist, from the folder's 22 necessary industries. **Human-based jobs:** humans × (120.7 × D × f + 85.6) ÷ 1,000, where 120.7 is the food workers needed per 1,000 humans, D is the city's difficulty multiplier (about 1.11 on a mild coast to about 2.7 at the highest and coldest site; it comes from weather, logistics and site access), f is 1.00 for most cities and 0.10 for the seven geologically forced importers (which import about 90% of their food), and 85.6 covers other human-scaled jobs such as childcare and mortuary services. **Everyone-based jobs:** residents (humans and robots) × (64 × D + 113.2) ÷ 1,000.
3. **Distinctive tier** = workforce − baseline: what is left after bare survival.
4. **Mandated** (tier two) = the distinctive tier × the city's national-role percentages (for example Davis's 35% to agriculture).
5. **Free** (tier three) = distinctive − mandated: the "character budget."

*Davis on the old populations:* baseline 40.7% of its workforce, distinctive tier 59.3% (about 519,800), agriculture at 35% of that about 181,800 (counting method B). Some rates in the underlying table (C6, C7, C8, D4) are estimates, not sourced.

## 2 · The refresh, under three conventions for Davis's and Esperanza's agricultural workforce

| Convention | Davis / Esperanza agriculture, before → after | Supply, before → after | Balance, before → after | Export capacity, before → after | **Slack, before → after** |
|---|---|--:|--:|--:|--:|
| **A: as written in `13`** (35% / 15% of the 2026-09-01 "distinctive tier"; scaled by each city's change in distinctive tier) | 208,593 → 212,752 / 143,998 → 145,835 | 404,191 → 410,186 | +166,582 (+70%) → **+165,545 (+68%)** | 2,790,603 (17.9%) → 2,831,997 (18.1%) | 1,150,113 (7.4%) → **1,142,952 (7.3%)** |
| **B: `16`'s current convention** (35% / 15% of the distinctive tier under the three-tier formula) | 181,808 → 185,433 / 126,719 → 128,335 | 360,127 → 365,368 | +122,518 (+52%) → +120,727 (+49%) | 2,486,377 (15.9%) → 2,522,562 (16.1%) | 845,887 (5.4%) → **833,517 (5.3%)** |
| **C: `04` §3** (35% / 15% of the whole workforce) | 306,780 → 313,027 / 210,093 → 212,770 | 568,473 → 577,397 | +330,864 (+139%) → +332,755 (+136%) | 3,924,833 (25.1%) → 3,986,445 (25.5%) | 2,284,343 (14.6%) → **2,297,400 (14.7%)** |

**Reading it.**
- **The population change moves the balance very little:** slack falls by about 0.1 percentage point under A and B and rises by about 0.1 under C. The shift is small because the new people are spread over many cities, and the forced importers and the two producers all gained a few percent.
- **The denominator convention moves it enormously:** the slack is **5.3% to 14.7%** of national humans depending on convention. That spread (about 1.46 million people) is the real uncertainty, and it is the one the folder has flagged since `16` Register item 11.
- **Relung Panen is not in any of these numbers.** Its role is the open question (section 3 below).

## 3 · Relung Panen on its own terms (provisional; nothing derived or recorded as canon)

Census I (current): **477,285 humans, 494,585 robots, 971,870 combined; workforce (robots + 0.5 × humans) = 733,228.** Its baseline needs a difficulty D that has not been derived; three values bracket it:

| D | Baseline | Baseline % of workforce | Distinctive tier | Distinctive % |
|--:|--:|--:|--:|--:|
| 1.11 | 283,858 | 38.7% | 449,369 | 61.3% |
| 1.25 | 300,631 | 41.0% | 432,596 | 59.0% |
| 1.43 | 322,197 | 43.9% | 411,031 | 56.1% |

If its agricultural sector is a given share of the distinctive tier (D = 1.25, convention B, national food rate 0.14484):

| Agricultural share | Agricultural workers | People fed beyond itself | Share of national humans |
|--:|--:|--:|--:|
| 0% (not a food region) | 0 | 0 | 0% |
| 15% | 64,889 | 448,008 | 2.9% |
| 25% | 108,149 | 746,680 | 4.8% |
| 35% (Davis's share) | 151,409 | 1,045,351 | 6.7% |

Added to the refreshed national slack: at 35% the slack becomes about **14.0%** under A or **12.0%** under B.


## 3b · Relung Panen's food role: "Strong" (25%) — RULED 2026-10-28 (`DR-71`); the figures use a placeholder D = 1.25

- **Its own workforce.** Agricultural workers for export: **108,149 (14.7% of its workforce)**. Add the 72,010 who grow its own food (inside the baseline) and about **180,159, or 24.6% of all its workers, work in food**: roughly one in four.
- **What is left for everything else.** The distinctive tier is 432,596 (59.0% of the workforce). After food, **324,447 workers (44.2% of the workforce)** remain for any mandated roles plus the free tier, the room for the city's own character. (At 15% that room would be 50.1%; at 35%, 38.3%.) No other mandate has been assigned yet.
- **What it feeds.** About **746,680 people beyond itself**, 1.56 times its own human population of 477,285.
- **The national budget.** Slack rises from 7.3% (A) or 5.3% (B) to about **12.1% (A) or 10.1% (B)**, a gain of 4.8 points, enough for roughly 750,000 more people to specialize away from food.
- **Supply concentration** (convention B). Today Davis supplies 50.8% of national export supply, and Davis and Esperanza together 85.9%. With Relung Panen at 25% it would supply **22.8%**, Davis falls to **39.2%** and the two to **66.3%**: a second, uncorrelated region, which is what `13` §15 described as the reason to want it.
- **Standing among the producers.** Relung Panen's 108,149 agricultural workers would be below Davis (185,433) and Esperanza (128,335), so Davis keeps its canon identity as the city that "grows more than anyone."
- **Costs and dependencies.** It builds its soil from nothing, and phosphorus is the one input the nation cannot manufacture (`14`), so a food role this size makes Relung Panen a heavy phosphorus consumer and ties it to the import and recycling chain. It also commits a quarter of its workforce to food, which shapes what else it can be.

## 4 · Open items this surfaced

1. **The census row for Relung Panen and its founding note still say Tepenia runs a "26.0% national food deficit" and that Relung Panen "is not optional," sized at about 765,007.** `13` §15 (2026-09-02) superseded that: the balance is a surplus and Relung Panen is "firmly optional." The census wording predates or ignores §15. **Not edited here.**
2. **The Davis/Esperanza denominator** (conventions A, B, C above) is unresolved and swings the slack by about 9 points.
3. **The per-city determinations further down `16`** (Neumayer and others) still carry the old populations; they were not recomputed.
4. **Relung Panen's own row** (D, other mandate roles, free tier) is not derived. **Its food share is now ruled at 25% (`DR-71`)**; the rest waits for D and the differentiation question (`15`, List A item 2).

## 5 · Settled 2026-10-28 (`DR-73`, `DR-72`): convention B, and Relung Panen at D = 1.43

- **Convention B is the national convention** (`DR-73`): mandated-role percentages are shares of the distinctive tier under the three-tier method. Conventions A and C above are retained only as the record of what the other files assumed.
- **Relung Panen's difficulty is 1.43** (`DR-72`), replacing the placeholder 1.25 in sections 3b and 4. At 1.43 its baseline is 322,197 (43.9%), its distinctive tier 411,031 (56.1%), and the Strong 25% food role is **about 102,758 workers (14.0% of the workforce)**, feeding about 709,459 people beyond itself.
- **National figures under B with that role:** export supply 468,126; balance about +91%; slack about **9.9%** of national humans (was 10.1% with the placeholder); Relung Panen supplies 22.0%, Davis 39.6%, Davis and Esperanza together 67.0%.
- **Still open:** the percentages of the new mandated roles (agricultural research, seed breeding, phosphorus and soil recovery; cold-chain logistics pending the port and airport question), the free tier, and the Division of Industry row.
