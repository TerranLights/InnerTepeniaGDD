# Relung Panen: Division of Industry determination (2026-10-29)

> **Status: a new file. Nothing existing in this folder was rewritten.** `09` §2 still carries the old placeholder row for this city and `16` Half B still excludes it; both are left as written and are pointed at from here. Written at the developer's rulings `DR-71` (food role), `DR-72` (difficulty and first mandated roles), `DR-73` (shares are taken of the distinctive tier) and `DR-75` (the shares below). **Cold-chain logistics is not included and is explicitly pending** (section 5). **Not a ULM pass:** this city's pass has not run, so nothing here is a ULM finding.

## 1 · Inputs

| | |
|---|---|
| Census I | 477,285 humans, 494,585 robots, 971,870 combined (`Official_Population_Census.md`, as of `DR-68`) |
| Workforce | robots + 0.5 × humans = **733,228** (`16`'s convention) |
| Difficulty D | **1.43** (`DR-72`): weather 15 + site access 5 + logistics minor 10 = 30% productivity loss; 1 ÷ 0.70. Factor table: `08` §6.4b |
| Food-rate factor f | 1.0 (not one of the seven geologically forced importers) |
| Convention | role shares are shares of the **distinctive tier** (`DR-73`, convention B) |

**A check recorded against the weather factor.** D used the White Smoke Lake station (−11.2 °C annual mean, 4.6 m/s mean wind). The other record, the Soviet Oasis station of 1956–58, reads −9.0 °C, a 6.8 m/s mean wind, 122 days a year at 15 m/s or more, and a peak of 56 m/s (`Research_Logs/Relung_Panen_Soil_Research_2026-10-25_E_Oasis_Ground_Water_and_Light.md`, key figures). The two sit in different spots and years: the AWS stood on an ice-covered lake against a glacier, which the Russian arctic institute says is almost 2 °C colder, and the Oasis station ran two years, which its own author calls too short to characterize the climate. The wind is two-sided: two-thirds of readings are 5 m/s or less and calms are 39% of observations, yet one day in three has wind above 15 m/s, April averages 10 m/s, and blizzards fall on 53 days. The main katabatic flow misses the oasis, and winter mean wind there is 2 to 3 times lower than at nearby ice-sheet stations. Read on the ladder (`08` §6.4b), that is a cold, intermittently stormy site with a lower mean wind than the windswept stations, which supports weather at 15 and does not support 20 (the ladder's 20 is a site with a 22 m/s mean). Weather 10 is arguable on the mean alone. D = 1.43 stands as ruled.

## 2 · The tiers

`baseline = humans × (120.7 × f × D + 85.6) ÷ 1,000 + residents × (64 × D + 113.2) ÷ 1,000`

| Tier | Workers | Share of workforce |
|---|--:|--:|
| Baseline | 322,197 | 43.9% |
| Distinctive (workforce − baseline) | 411,031 | 56.1% |

## 3 · The mandate

| Role | Share of distinctive | Workers | Ruling | Basis |
|---|--:|--:|---|---|
| Food production (the second, uncorrelated agricultural region) | 25% | 102,758 | `DR-71` | National balance is a surplus, so the city is optional; a second region is wanted for supply. The outdoor belt sited at Bunger Hills (about 400 km², `12` siting table) serves Relung Panen, Mirny and Casey. |
| Agricultural research | 4% | 16,441 | `DR-75` | A partner's stake in the joint research project with Davis, Ariun Nuur and Zhongshan. Davis holds the national research half; this site adds a different one (shelf-sealed oasis, thaw season, permafrost table 82 to 106 cm, made ground). |
| Seed breeding | 3% | 12,331 | `DR-75` | Supplies seed to other cities (developer, `DR-75`). A second, uncorrelated seed stock is insurance against a crop disease in one region. |
| Phosphorus and soil recovery | 6% | 24,662 | `DR-75` | A national role (developer, `DR-75`), also serving other cities' waste streams. The country cannot manufacture phosphorus and must find it or recycle nearly all of it (`14`); recovery is described there as infrastructure. |
| **Mandate total** | **38%** | **156,192** | | 21.3% of the workforce |

How the joint research project is counted: each city counts its own workers in its own sector. Relung Panen's 16,441 are Relung Panen's staff; the other three cities' staff stay in their own rows. Nothing is split or double-counted.

## 4 · The result

| Tier | Workers | Share of workforce |
|---|--:|--:|
| Baseline | 322,197 | 43.9% |
| Mandated | 156,192 | 21.3% |
| **Free (the character budget), before cold-chain logistics** | **254,839** | **34.8%** |

Each additional point of the distinctive tier given to a role is about 4,110 workers (0.56% of the workforce) taken out of the free tier.

**National figures with the food role at D = 1.43, convention B** (`17` section 5): export supply 468,126; balance about +91%; slack about 9.9% of national humans; Relung Panen 22.0% of export supply, Davis 39.6%, Davis and Esperanza together 67.0%.

## 5 · Open items

1. **Cold-chain logistics.** Yes in principle (developer, `DR-72`); to be registered once the port and airport question is settled. Needs a share.
2. **Sourced staffing ratios** for seed breeding and nutrient recovery would sharpen the 3% and 6%; none were found. The shares are judgment calls, recorded as such.
3. **Edits not made, awaiting the developer's OK:** `09` §2 (the placeholder row currently reads D 1.43 with TBD values, which now has values) and `16` Half B (add the row). Both are existing files.
4. **The differentiation table column** is drafted in `02_Cross_City_Industry_Differentiation_Table.md` as a separate subsection, from this determination and not from a ULM pass.
5. **Power remains the binding constraint** for the stacked hydroponics (the spec says: no geothermal, no measured wind resource, off-grid). That is an input to the food role that the determination does not resolve.
