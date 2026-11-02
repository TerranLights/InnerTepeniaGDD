# Scenario: China at half to two-thirds of today's population (2026-11-01, ~22:20)

**Scratch, not canon, not a ruling.** No census entry, spec, composition file or datasheet was changed. Figures come
from `calc_china_decline.py`, which only reads the specs and the composition file. Rerun it after any change.

## What was asked

The developer, 2026-11-01 ~22:15, proposing a way to reduce China's dominance in the cities:

> *"So you know how China's population suffered a major hit as a result of their one-child policy. And nowadays, a
> lot of Chinese are just not getting married and not having kids. How would the numbers look if, 500 years from now
> (i.e., at the time of the signing of the Falkland Treaty), China's population was approximately, let's say,
> somewhere around half to two-thirds of the numbers that it is now?"*

And, reconfirming the exemption already in the 2026-10-31 criteria (~22:25):

> *"Also, the two exceptions to this obviously would be Zhongshan and Kunlun, because those two cities are
> fundamentally Chinese in nature."*

### Developer direction on Kunlun (2026-11-01, ~22:30; not yet applied to any file)

Asked whether Kunlun's present table (USA 15.43%, China 15.22%, Russia 11.45%, all three Primary; the 2026-07-06
space-heritage rework) is what "fundamentally Chinese" means, the developer answered:

> *"China should clearly lead in Kunlun, like Zhongshan, due to the fact that Kunlun was set up in part through a
> joint agreement by the Sinian Federation."*

This agrees with the Founding Register (L64: Kunlun's founders are Ariun Nuur's stock, Künnarantaiga and Mongolia,
**plus the Sinian Federation**, `DR-34`, `DR-35`). The reason is the founding agreement, not the real station's
builder.

**Decided (~22:35, confirmed ~22:45): Option A.** *"I would say Option A, yes."* → *"alrighty, so let's go with
Option A."* China alone in the top tier (8 shares); the USA and Russia move to the middle tier (3 shares). Before
any co-founders are added: China ~17.0%, each middle-tier nation ~6.4%, each bottom-tier nation ~2.1% (plain 8/3/1
shares, before de-stacking). **Not yet applied:** Kunlun's spec, the census (Section A), the composition file and
Kunlun's datasheets change in the 2026-11-02 morning population pass, and the ruling goes into the rulings log then.

**Mongolia and Künnarantaiga.** Developer: *"I think that Mongolia and Künnarantaiga should appear on the
Register."* They are already on the Register as Kunlun's co-founders (L64); what they lack is a row in Kunlun's
population table. **Claude's recommendation (awaiting the developer's word):** add both to Kunlun's middle tier,
marked "founding wave", as Australia is at Mirny, Casey and Davis. Then China is ~15.1%, every middle-tier nation
~5.7% (the two co-founders included), the bottom tier ~1.9%; the lead comes from the USA and Russia dropping, not
from China rising. (Bottom tier instead: China ~16.3%, the co-founders ~2.0%.) **The same gap exists at Ariun
Nuur**, whose founders are the same two and are not in its table either; recommended fix the same way, in the
population pass (which takes Ariun Nuur off the "untouched by the population work" list in the tracker's S.4).

**The prose rewriting** (spec L25, L82, L178 and any other passage built on the 2026-07-06 rework, "no longer
exclusively Sinian") is for 2026-11-02, in hours.

## Real-world context (secondary sources; the UN's own data portal was not opened)

- The UN's 2024 medium projection puts China at **about 633–639 million in 2100**, from about 1.42 billion in 2024:
  roughly **45%** of today, only 75 years out. The 2022 revision had it at just under 800 million, and its low
  variant at 488 million. *(Pew Research, 2025-07-09 and 2022-12-05; populationpyramid.net; SCMP, 2024.)*
- The same 2024 projection has **South Korea** falling from about 52 million to about 22 million (−57%) and
  **Japan** from about 124 million to about 77 million (−38%) by 2100. *(Population Connection; populationpyramid.net.)*
- Search strings: `UN World Population Prospects 2024 China population projection 2100 medium variant` ·
  `World Population Prospects 2024 South Korea Japan population 2100 projection` (2 searches, none refused).

## How the project turns a pool into a city's figures (why there are three readings)

The effective pool (China ~210M, `Upper_Earth_Immigration_Composition.md` L68) does **not** set a city's China
share directly. The composition file ranks a city's nations by pool, places the tier breaks at the largest ratio
gaps (L17, L1107), and then gives **Primary 8 shares, Significant 3, Notable 1** per nation (L1109). The spec
percentages are those shares, then de-stacked within each tier. Halving China's pool therefore changes a city
**only if it changes China's tier.** Reading 1 tests that; readings 2 and 3 cut China's people directly instead.

## Reading 1: the method as written (tiers)

China's pool: today 210M; two-thirds 140M; half 105M. Primary = nations above the largest ratio gap among the top
two boundaries ("typically the top 1–2"); a third boundary is shown where it would change the answer. Shares are
the plain 8/3/1 shares before de-stacking. *The rule reproduces today's Primary tier in all 15 cities ("matches").
Relung Panen's spec table is not a plain 8/3/1 split (its composition is held for the population work), so its
"today" figure here differs from the spec's 21.58%.*

| City | Primary today (rule check) | China today | Two-thirds: Primary | China | Half: Primary | China | Half, if a third place may join |
|---|---|--:|---|--:|---|--:|---|
| Dumont d'Urville | China, USA (matches) | 22.2% | USA, China | 22.2% | USA, China | 22.2% | USA, China, Japan: China 19.5% |
| Mirny | China (matches) | 24.2% | China | 24.2% | China, Japan | 21.1% | same |
| Zukelli | China, USA (matches) | 21.1% | USA, China | 21.1% | USA, China | 21.1% | USA, China, Japan: China 18.6% |
| Relung Panen | China (matches) | 28.6% | China, Japan | 24.2% | China, Japan | 24.2% | same |
| Janbogo | China, USA (matches) | 19.5% | USA, China | 19.5% | USA, China | 19.5% | same |
| Davis | China (matches) | 19.0% | China | 19.0% | China | 19.0% | same |
| Temirötkel | China (matches) | 17.4% | China | 17.4% | China | 17.4% | same |
| Mawson | China (matches) | 17.0% | China | 17.0% | China | 17.0% | same |
| Denison | China, USA (matches) | 24.2% | USA, China | 24.2% | USA, China | 24.2% | USA, China, Japan: China 21.1% |
| Cape Adare | China, USA (matches) | 21.1% | USA, China | 21.1% | USA, China | 21.1% | USA, China, Japan: China 18.6% |
| Scott | China, USA (matches) | 21.1% | USA, China | 21.1% | USA, China | 21.1% | USA, China, Japan: China 18.6% |
| Fort McMurdo | China, USA (matches) | 20.5% | USA, China | 20.5% | USA, China | 20.5% | same |
| Amundsen Station | China, USA (matches) | 21.1% | USA, China | 21.1% | USA, China | 21.1% | same |
| Casey | China, USA (matches) | 20.5% | USA, China | 20.5% | USA, China | 20.5% | USA, China, Japan: China 18.2% |
| Dome Fuji | China, USA (matches) | 10.7% | USA, China | 10.7% | USA, China | 10.7% | same |

**What it shows.** Under the method as it stands, **the idea barely moves anything.** Even at half, China's pool
(105M) is still 1.6 times Japan's (65M), so China stays in the top tier in all 15 cities. At two-thirds, China's
share is unchanged everywhere except Relung Panen. At half, it falls only where **Japan joins the top tier**
(Mirny, Relung Panen, and up to six more if a third place may join). There, Japan jumps from about 5–12% to about
18–24%: the top tier changes who is in it, not how big it is.

## Readings 2 and 3: China's people cut directly

"City shrinks" removes the missing Chinese and leaves every other nation's people as they are. "City keeps size"
fills the gap from the other nations in proportion to their present shares. **China's own figure is the same
however the gap is filled**; who fills it is the rebalance decision (the developer's criteria), and the
proportional fill used for the rank here is only one way to do it. Zhongshan and Kunlun are left as they are
(exempt).

| City | China today (spec) | China rank today | Two-thirds, city shrinks | Two-thirds, city keeps size | Half, city shrinks | Half, city keeps size | Largest other nation today | China's rank at half (shrinks / keeps size) |
|---|--:|--:|--:|--:|--:|--:|---|--:|
| Zhongshan *(exempt)* | 35.83% | 1 of 18 | 35.8% | 35.8% | 35.8% | 35.8% | South Korea 9.70% | 1 / 1 |
| Dumont d'Urville | 24.31% | 1 of 12 | 17.6% | 16.2% | 13.8% | 12.2% | USA 20.13% | 2 / 5 |
| Mirny | 24.24% | 1 of 14 | 17.6% | 16.2% | 13.8% | 12.1% | UK 12.35% | 2 / 4 |
| Zukelli | 22.63% | 1 of 12 | 16.3% | 15.1% | 12.8% | 11.3% | USA 19.47% | 2 / 4 |
| Relung Panen | 21.58% | 1 of 11 | 15.5% | 14.4% | 12.1% | 10.8% | Russia 12.60% | 6 / 6 |
| Janbogo | 20.63% | 1 of 13 | 14.8% | 13.8% | 11.5% | 10.3% | USA 18.39% | 2 / 5 |
| Davis | 19.04% | 1 of 21 | 13.6% | 12.7% | 10.5% | 9.5% | Japan 9.36% | 1 / 4 |
| Temirötkel | 17.39% | 1 of 25 | 12.3% | 11.6% | 9.5% | 8.7% | Indonesia 8.59% | 1 / 5 |
| Mawson | 17.02% | 1 of 26 | 12.0% | 11.3% | 9.3% | 8.5% | UK 8.99% | 2 / 4 |
| Denison | 22.29% | 2 of 11 | 16.1% | 14.9% | 12.5% | 11.1% | USA 26.19% | 3 / 4 |
| Cape Adare | 19.85% | 2 of 12 | 14.2% | 13.2% | 11.0% | 9.9% | USA 22.26% | 4 / 5 |
| Scott | 19.48% | 2 of 12 | 13.9% | 13.0% | 10.8% | 9.7% | USA 22.62% | 4 / 5 |
| Fort McMurdo | 19.34% | 2 of 15 | 13.8% | 12.9% | 10.7% | 9.7% | USA 21.69% | 4 / 5 |
| Amundsen Station | 19.31% | 2 of 12 | 13.8% | 12.9% | 10.7% | 9.7% | USA 22.80% | 4 / 5 |
| Casey | 19.06% | 2 of 13 | 13.6% | 12.7% | 10.5% | 9.5% | USA 21.96% | 4 / 5 |
| Kunlun *(exempt)* | 15.22% | 2 | 15.2% | 15.2% | 15.2% | 15.2% | USA 15.43% | 2 / 2 |
| Dome Fuji | 10.13% | 2 of 43 | 7.0% | 6.8% | 5.3% | 5.1% | USA 11.20% | 4 / 6 |
| Sinheung | 9.74% | 2 of 17 | 6.7% | 6.5% | 5.1% | 4.9% | South Korea 34.62% | 5 / 5 |
| Concordia | 7.70% | 6 of 38 | 5.3% | 5.1% | 4.0% | 3.8% | Japan 9.32% | 8 / 10 |
| Shirayuki | 7.18% | 5 of 17 | 4.9% | 4.8% | 3.7% | 3.6% | Japan 36.27% | 6 / 7 |
| Byrd | 2.95% | 6 of 42 | 2.0% | 2.0% | 1.5% | 1.5% | USA 13.57% | 24 / 24 |
| Palmer City | 0.91% | 23 of 43 | 0.6% | 0.6% | 0.5% | 0.5% | USA 20.29% | 36 / 36 |

*(Kunlun's row count is left out: the parser read 20 rows where the prep file counted 19. Checked ~23:50: the
table has 19 nations plus the Intermarium/Intermaria bloc as its own row, so both counts are right.)*

**Nationally** (Census I humans, summed from the specs):

- Today: **1,660,450 China-origin humans, 10.6%** of Tepenia's 15,623,523. *(The USA is 2,462,596, 15.8%.)*
- Two-thirds: 1,176,348. If cities shrink, Tepenia loses 484,102 humans (−3.1%) and China is **7.8%**; if cities
  keep their size, **7.5%**.
- Half: 934,298. If cities shrink, Tepenia loses 726,152 humans (−4.6%) and China is **6.3%**; if cities keep
  their size, **6.0%**.

*⚠ Corrected ~23:50 (self-correction, logged per the recording law). The first version of this list read
1,654,597 today, 1,172,446 at two-thirds and 931,371 at half, and called the 5,853 gap to the census figure "not
chased." The gap was the script's own error: it read a city's human count only when the table had all four census
columns, and Byrd has no Census II columns, so Byrd's 5,853 China-origin humans were dropped. Fixed in
`calc_china_decline.py`; the percentages above changed by at most 0.1 point.*

**What it shows.** Cut directly, China falls from 17–24% to **11–18% at two-thirds** and **8.5–14% at half** in
the cities it now leads. At half it is no longer first anywhere except Zhongshan, and, if cities shrink, Davis and
Temirötkel, where it stays narrowly ahead. In the China-and-USA cities, the USA leads clearly at half.

## Things that interact with this (no proposal; listed for the developer)

1. **The method question comes first.** The idea works through readings 2 and 3, not through the tier method as
   written (reading 1). Which one is used is a choice about the method itself.
2. **The Sinian split stacks on top.** The Sinian Federation keeps about 89–92% of whatever China's pool is
   (`03_Results.md`), so each China figure above becomes roughly nine-tenths of itself for the Federation, with
   the rest going to Manchuria and the smaller pieces (or leaving, per decision 3 in `03`).
3. **The USA split works the other way.** If the USA's ~22% in a city becomes several successors of at most about
   a third each (`06_Part2_Results.md`), the Sinian Federation at about 9–12% could again be the **largest single
   nation** in many cities, though no longer a dominant one.
4. **The same demographic reasoning reaches other nations.** By the UN's projection, South Korea shrinks faster
   than China and Japan nearly as fast. Applying the decline to China alone is a choice; applying it to every
   low-birth-rate nation would shift other cities too (Sinheung, Shirayuki, and every city where Japan or South
   Korea is large).
5. **Who fills the gap**, if cities keep their size: the developer's criteria (raise nations at about 5% or more
   where that makes the mix generally multicultural; leave those at about 5% or less roughly where they are).
