# Results: China's successors (2026-11-01, ~21:50)

**Scratch results, not canon.** Every figure below is computed by `calc_successors.py` from `02_unit_data.csv`;
sources are in `01_Research_Log.md`. Rerun with `python3 calc_successors.py` after any data change. Nothing in the
census, specs, composition file or datasheets has been changed.

**Basis.** Official 2024 year-end provincial populations and 2024 gross regional product (China Statistical
Yearbook 2025, tables 2-5 and 3-9), with the 2020 census as the benchmark. 2024 is the latest year with one complete
official provincial table; eight provinces' 2025 figures (P6) differ from 2024 by under 1% each and are kept in
the CSV as a spot check only. Hong Kong, Macau, Taiwan and Mongolia come from their own statistics offices (Mongolia
through aggregators, flagged).

## Checks

- 31 provinces, 2020 census: 1,409,778,724; plus 2,000,000 servicemen = 1,411,778,724; national total 1,411,778,724 (difference 0)
- 31 provinces, 2024 year-end: 1,406,280,000; national total 1,408,280,000; gap 2,000,000 (servicemen are in the national total only, plus rounding of 31 figures given to the nearest 10,000)
- 31 provinces, 2024 gross regional product: 1,340,312.8 hundred million yuan (provinces are summed as published; the national GDP is a separate account and is not expected to match)

## Raw populations of the successors

| Successor | Present-day units | 2020 census (mainland part) | Share of the 31 provinces, 2020 | 2024 year-end (mainland part) | Share of the 31 provinces, 2024 | Outside China's official figures (latest) | Total, 2024 basis |
|---|---|--:|--:|--:|--:|--:|--:|
| **Sinian Federation** | Beijing, Tianjin, Hebei, Shanxi, Shanghai, Jiangsu, Zhejiang, Anhui, Fujian, Jiangxi, Shandong, Henan, Hubei, Hunan, Guangdong, Guangxi, Hainan, Chongqing, Sichuan, Guizhou, Yunnan, Shaanxi, Gansu, Qinghai, Ningxia, Hong Kong, Macau | 1,257,714,176 | 89.21% | 1,257,460,000 | 89.42% | 8,188,900 | 1,265,648,900 |
| **Manchuria** | Liaoning, Jilin, Heilongjiang | 98,514,948 | 6.99% | 95,010,000 | 6.76% | 0 | 95,010,000 |
| **Mongolia** | Inner Mongolia, Mongolia (present-day country) | 24,049,155 | 1.71% | 23,880,000 | 1.70% | 3,540,000 | 27,420,000 |
| **East Turkestan** | Xinjiang | 25,852,345 | 1.83% | 26,230,000 | 1.87% | 0 | 26,230,000 |
| **Tibet** | Tibet (Xizang) | 3,648,100 | 0.26% | 3,700,000 | 0.26% | 0 | 3,700,000 |
| **Taiwan** | Taiwan | 0 | 0.00% | 0 | 0.00% | 23,400,220 | 23,400,220 |

## GDP per person of each successor's mainland part (DERIVED: summed GRP / summed 2024 year-end population)

| Successor | 2024 GRP, hundred million yuan | Share of the 31 provinces' GRP | GDP per person, yuan |
|---|--:|--:|--:|
| Sinian Federation | 1,227,248.4 | 91.56% | 97,597 |
| Manchuria | 63,450.8 | 4.73% | 66,783 |
| Mongolia | 26,314.6 | 1.96% | 110,195 |
| East Turkestan | 20,534.1 | 1.53% | 78,285 |
| Tibet | 2,764.9 | 0.21% | 74,727 |
| *All 31 provinces* | 1,340,312.8 | 100.00% | 95,309 |

## Splitting China's effective pool of ~210M (mainland parts only)

| Successor | Option A: by headcount | Option B: by economic size (GRP) |
|---|--:|--:|
| Sinian Federation | 187.8M (89.4%) | 192.3M (91.6%) |
| Manchuria | 14.2M (6.8%) | 9.9M (4.7%) |
| Mongolia | 3.6M (1.7%) | 4.1M (2.0%) |
| East Turkestan | 3.9M (1.9%) | 3.2M (1.5%) |
| Tibet | 0.6M (0.3%) | 0.4M (0.2%) |

## What this shows (plain reading of the tables above)

1. **The split by itself barely changes China's weight.** The Sinian Federation keeps **about 89% of China's
   people** (Option A) or **about 92% of its economy** (Option B). Every city's China figure would fall by only
   8–11% of itself. For example, a city at 24% China would land at roughly 21–22% before any rebalancing. **The
   developer's rebalance criteria, not the split, will do most of the work of making the mixes generally
   multicultural.** *(This confirms, with sourced figures, the from-memory estimate given to the developer at
   ~21:39.)*
2. **The breakaway pieces are small pools.** Manchuria is the only sizable one (95 million people, the poorest
   per person of the five). The other three on China's present territory hold between 3.7 and 26 million each.
3. **The two options differ only for the small pieces.** Manchuria is 14.2M by headcount but 9.9M by economic
   size, because its output per person is about two-thirds of the Sinian Federation's. Inner Mongolia goes the
   other way (richer per person than the Federation).
4. **The checks pass exactly.** The 31 provinces plus 2,000,000 servicemen equal the 2020 national census total
   to the person. In 2024 the gap to the national total is exactly 2,000,000, which matches the servicemen.

## Decisions for the developer (nothing assumed)

1. **Option A (headcount) or Option B (economic size)** for splitting China's ~210M effective pool. *Claude's
   recommendation: B. The census already weights nations by GDP per person, and the provinces' GDP per person
   ranges from 52,825 yuan (Gansu) to 228,167 yuan (Beijing).* This choice matters only for the small pieces;
   the Sinian Federation is 188M or 192M either way.
2. **Hong Kong and Macau** (8.2 million together) were never part of China's figures or its 210M, but canon puts
   them in the Sinian Federation. Add them to its pool, and if so, how? Their own income and inequality figures
   have not been gathered yet.
3. **Do the breakaway pieces enter any city as nations of their own,** or do they simply leave China's share?
   Manchuria (UTC+8) would pass the same time-zone test China does. East Turkestan's solar time zone is several
   hours west of Beijing's, so the ±3 window may treat it differently. This is a per-city question for the
   rebalance itself.
4. **Taiwan** (23.4 million) and **Mongolia** (the present-day country, 3.5 million) were never in China's figures.
   Whether either belongs in any city's table is a separate question from the split.
5. **Which era's borders apply.** The census reflects the exile era (2560s onward). The East Asia borders used here
   are Map F (2267 to the present), which keeps Map E's borders, so East Asia is unaffected. For the other countries
   (see `04` once written), the atlas draws each region's "final state," which should be checked against the
   exile era.

## Open threads

- Hong Kong and Macau GDP and inequality figures (for decision 2).
- A primary 2024 year-end figure for Mongolia from its statistics office (1212.mn not reached).
- Full 2025 year-end provincial table (expected in the China Statistical Yearbook 2026; not found online yet).
- Provincial inequality (Gini) figures: not looked for, because the census applies one adjustment per nation.
