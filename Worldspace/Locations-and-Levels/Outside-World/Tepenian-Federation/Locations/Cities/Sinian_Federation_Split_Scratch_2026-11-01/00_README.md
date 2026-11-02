# Sinian Federation split: scratch files (started 2026-11-01, ~21:40)

**What this is.** Working files for the first population item on the 2026-11-02 list: the real populations of the
countries that today's China becomes in the Interwar timelines, worked out from official figures. **Scratch work,
not canon and not a ruling.** No census entry, spec, composition file or datasheet has been changed. The developer
asked for this to start tonight (2026-11-01, ~21:40): *"create a set of scratching files, and go ahead and get
started on the calculations now."*

## The borders (canon, not researched)

From the Timeline repo (`/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/`):
`Worldspace/Locations/Earth/Upper_Earth/Asia_East/README.md` ("Settled facts"), Map E
(`asia-east-E-unified.png`, 2179–2266), and `Reference/World_History_Reference.md` § The Sinian Federation.

- The Sinian Federation is nine Han states: Zhongyuan, Qin, Bashu, Jin, Wu, Gan, Xiang, Min and Yue. Qinghai is
  part of Qin.
- Mongolia, Manchuria, East Turkestan, Tibet and Taiwan are not members. Inner Mongolia joined Mongolia in 2098
  (Map B).
- Map E's footnote: *"Whole first-order subdivisions only."* So every border follows today's whole provinces.

| Successor | Today's units | Note |
|---|---|---|
| **Sinian Federation** | the other 25 mainland provincial units, plus Hong Kong and Macau | Hong Kong is labeled inside the Federation on Map E. Macau is not labeled there; the author's atlas (`numbering.csv` row 167) places it in the Federation, so this is settled |
| **Manchuria** | Heilongjiang, Jilin, Liaoning | |
| **Mongolia** | Mongolia (today's country) plus Inner Mongolia | |
| **East Turkestan** | Xinjiang | |
| **Tibet** | the Tibet Autonomous Region only | Qinghai stays with Qin; Tibetan-majority prefectures of Sichuan, Yunnan and Gansu stay with their provinces (whole units only) |
| **Taiwan** | Taiwan | Already outside China's official figures today |

Which present-day provinces make up each of the nine Han states is not needed for these sums and is not decided
here.

## What the census uses (why raw headcounts are only the first step)

`Upper_Earth_Immigration_Composition.md` does not place nations by raw population. It uses each nation's
**"Gini-adjusted effective exile population"**: raw population × a GDP-per-person factor × an inequality penalty.
China's is **~210M** (L68). The formula itself is described in prose (§ "Explanatory Summary", Factor 3) but not
written down as numbers, so splitting 210M among the successors needs a choice from the developer (file `03`).

## Files

| File | What it holds |
|---|---|
| `00_README.md` | this file: scope, borders, status |
| `01_Research_Log.md` | every search string verbatim, every page opened, dead ends, conflicts, open threads |
| `02_unit_data.csv` | one row per present-day unit: population (several dated figures), GDP per person, source for each |
| `calc_successors.py` | adds the units up into the successors and computes both split options; reads only the CSV |
| `03_Results.md` | the sums, shares, and the two ways of splitting China's ~210M, with the arithmetic shown |
| `05_part2_unit_data.csv` | Part 2: one row per present-day unit of the USA, Canada, Mexico, Italy, Germany and Argentina |
| `calc_part2.py` | Part 2: adds the units into the successors and splits each country's pool both ways |
| `06_Part2_Results.md` | Part 2 results, plus Russia's existing split (2026-10-29) summarized in millions |
| `calc_china_decline.py` → `07_China_Decline_Scenario.md` | 2026-11-01 ~22:20: the developer's idea of China at half to two-thirds of today's population, three ways (the tier method as written; China's people cut directly with cities shrinking or keeping their size); also the developer's Kunlun direction (Option A) |
| `calc_rebalance.py` → `08_Sinian_Decline_Rebalance.md` + `08_rebalance_city_tables.csv` | Overnight run, 2026-11-01 ~23:00, at the developer's request: China's row → the Sinian Federation's share × a random 55–60%, the gap filled by each city's nations at 5% or more outside its top tier, totals kept; then a verdict on whether each city's adjustment can be justified |
| `calc_rebalance_v2.py` → `09_Rebalance_and_Successor_Splits.md` + `09_city_tables.csv` | Run 2, 2026-11-01 ~23:40, with the developer's settings (proportional fill, 4.5% line, a random 55–65%), plus the USA, Canada, Mexico, Russia and Argentina rows divided among their successor states in all 37 cities (Kunlun left as it is); national table by successor; verdicts |
| `calc_rebalance_v3.py` → `10_Rebalance_Run3.md` + `10_city_tables.csv` | **Run 3, the current one** (2026-11-01 ~23:45), with the developer's answers to run 2: pool-share splits, splits before the decline, founders moved by hand from Japan at Ariun Nuur (Mongolia, Künnarantaiga) and Utstein (the five Nordic nations); Esperanza, Sanay and the Japan/South Korea result left as they are |

**Part 2 was added at the developer's request (~21:45):** *"after the Sinian Federation (and surrounding lands) are
done, see about calculating for Russia, Italy, Germany, Argentina, and the nations of North America."* Its borders come
from the author's world atlas (`/home/kuroskalacs/Documents/Doll-Fi/media/y-files/Map Files/x Full Earth/z-full-world-atlas/`).

## Status

- [x] Mainland provincial populations: 2020 census (benchmark)
- [x] Mainland provincial populations: latest official year-end (2024)
- [x] Hong Kong, Macau, Taiwan, Mongolia: latest official figures (Mongolia through aggregators, flagged)
- [x] GDP per person by unit (2024)
- [x] Sums and shares (file `03`)
- [x] The two split options for China's ~210M (file `03`)
- [x] Questions for the developer listed (file `03`)
- [x] Part 2: USA, Canada, Mexico, Italy, Germany, Argentina computed; Russia summarized from its 2026-10-29 files (file `06`)
- [x] The China-decline scenario (file `07`) and the overnight rebalance run with its verdicts (file `08`), scratch only
- [ ] Developer decisions (files `03`, `06` and the list at the end of `08`'s verdict section), then the city rebalance in the official files (nothing in any city file changed)
- [ ] **Readjust the National Census** (`Official_Population_Census.md`) once the decisions and the rebalance are made

## Next (developer, 2026-11-01, ~22:05)

> *"This is something we'll need to figure out tomorrow. Also, this means that we will eventually need to readjust
> the National Census as well, since the numbers would most assuredly have changed."*

So the order for 2026-11-02 is: the decisions in `03_Results.md` and `06_Part2_Results.md`, then the city
rebalance under the developer's criteria, then the National Census readjustment, then the follow-on files listed in
`../Population_Work_Prep_2026-11-02.md` (spec tables, composition-file sections, datasheet rows, and a sheet-check
rerun).

What the census readjustment will touch, as far as can be told before the decisions: **every per-nation row** that
names China, the USA, Canada, Mexico, Italy, Germany, Argentina or Russia becomes rows for their successors. **The
national totals** change wherever a piece is added (for example Hong Kong, Taiwan, Austria or Chile), a piece is
dropped (for example the Demilitarized Zone, if its people do not count), or the rebalance raises headcounts. If none of
those happen, splitting a pool only divides existing counts and the totals stay the same.
