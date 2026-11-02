# Run 3: the developer's answers applied (2026-11-01, ~23:45 onward)

**Scratch, not canon. No official file was changed.** Figures come from `calc_rebalance_v3.py` (it reuses runs 1
and 2's functions); every row of every city in every census column is in `10_city_tables.csv`; the script's whole
output is the appendix. Runs 1 and 2 (`08_*`, `09_*`) are kept as they were.

## The developer's answers to run 2 (~23:40, verbatim)

> *"1.) in proportion to its share of the old country. It's a numerical method that works perfectly fine, and I
> personally can't think of any reason to change it*
> *2.)*
> *- subtract two randomly-generated values from Japan's "25%" count, that are anywhere between 3.5% to 5% and
> redistribute them to Künnarantaiga and Mongolia, with the higher of the two values going to Mongolia. So, let's
> say one value is 4%, and the other is 4.5%, Mongolia gets 4.5%, Künnarantaiga gets 4%, and Japan comes down to
> 15.5%. We'll take a look and see how the numbers turn up*
> *- do the same thing distributing to all of the Scandinavian countries from Japan's "17%" count. A
> randomly-generated value between 0.5% and 1% to Iceland, and a randomly-generated value between 1.5% to 3.5% to
> Norway, Sweden, Finland, and Denmark, in the same fashion that Künnarantaiga and Mongolia get from Japan*
> *- that's probably fine*
> *3.) This might actually work to the advantage of the synthesis of the Tepenian language. Down at its
> foundational level core, it's fundamentally a Pidgin between English and Japanese at its core, with several
> languages stacked on top of it, and then a bunch more languages stacked on top of that.*
> *4.) that should be fine*
> *5.) that works"*

**What each answer settles (to go into the rulings log when applied for real):**
1. **Split by pool share,** every successor in proportion to its share of the old country, in every city. This is
   the "pool split" side of the open Russia ruling, now for every split country.
2. **Ariun Nuur and Utstein** get their founders by hand from Japan's share (below). **Esperanza** stays as run 2
   left it (Brazil 18.9%).
3. **Japan and South Korea as large communities are fine.** The developer's language remark agrees with the Modern
   Hawaiian note on file (`Worldspace/Modern_Hawaiian_Language.md`; memory: a pidgin of English, Japanese and
   Tagalog at its core, with Korean and Spanish supplementary). Language work lives in its own repo; nothing was
   written there.
4. **Sanay** stays as it is.
5. **Order: the splits first, then the decline.**

*Arithmetic note on the example in answer 2: 25% − 4.5% − 4% is 16.5%, not 15.5%. The script subtracts exactly
what it gives away. For any pair of draws in 3.5–5%, Japan at Ariun Nuur lands between 14.97% and 17.97%.*

## What was done

1. **Every city except Kunlun:** the USA, Canada, Mexico, Russia and Argentina rows divided among their successors
   (run 2's shares, Option B).
2. **The 20 cities with Chinese presence except Zhongshan and Kunlun:** China's row → the Sinian Federation ×
   run 2's draw (0.55–0.65 per city; same seed); the gap filled **in proportion to size** by rows at **4.5% or
   more** outside the top tier, **successor rows included** (so the CSA, Cascadia and others can receive it).
3. **The founder moves,** in points of the city's population, in every census column:
   - **Ariun Nuur:** two draws in 3.5–5.0 from Japan, the higher to Mongolia.
   - **Utstein:** from Japan, Iceland 0.5–1.0; Norway, Sweden, Finland and Denmark 1.5–3.5 each, added to Norway's
     and Finland's existing rows; Sweden, Denmark and Iceland are new rows.

   Seeds: Utstein 2026110123; Ariun Nuur 202611012343 (its redraw, below).

**Checks:** every city keeps its exact total in every census column, and no count goes negative (the script checks
both).

### The founder draws

| City | Row | Points from Japan |
|---|---|--:|
| Ariun Nuur | Mongolia | 4.1932 |
| Ariun Nuur | Künnarantaiga | 3.7316 |
| | *Japan, total* | *7.9248* |
| Utstein | Iceland | 0.5541 |
| Utstein | Norway | 2.4137 |
| Utstein | Sweden | 2.6476 |
| Utstein | Finland | 2.7699 |
| Utstein | Denmark | 3.0688 |
| | *Japan, total* | *11.4542* |

**Ariun Nuur's draw history.** The first draw (seed 2026110123, ~23:40) gave Mongolia 3.5114 and Künnarantaiga
3.5107: both at the very bottom of the range, so the two were equal in effect, and Japan stayed at 17.95% (lead
1.32). It was a genuine draw (the seed's first two numbers are 0.0076 and 0.0071 on a 0-to-1 scale, checked) and was
kept until the developer asked for a redraw (~23:43): *"redraw Ariun Nuur with a new seed, because it only makes
sense that Mongolia would have a higher share than Künnarantaiga."* **The redraw** uses its own seed, 202611012343,
fixed before the result was seen, and gave **Mongolia 4.1932, Künnarantaiga 3.7316**. Utstein's draws are unchanged
(its stream still skips the two numbers the first Ariun Nuur draw used).

## Results

### Every city

| City | China → Sinian Fed. | Leader before | Leader after | Lead after (1st ÷ 2nd) | Top five after (%) |
|---|---|---|---|--:|---|
| Amundsen Station | 19.31 → 11.33 | USA 22.80 | UK 12.17 | 1.05 | UK 12.2, Germany 11.6, Sinian Federation 11.3, Japan 11.0, CSA 7.6 |
| Byrd | 2.95 → 1.67 | USA 13.57 | Australia 7.07 | 1.04 | Australia 7.1, Japan 6.8, Demilitarized Zone 4.2, Cascadia 4.1, CSA 3.9 |
| Belgrano | — | USA 28.57 | Brazil 13.73 | 1.02 | Brazil 13.7, Germany 13.4, CSA 8.3, Appalachia 5.6, New England 5.6 |
| Halley | — | USA 23.53 | Brazil 11.69 | 1.11 | Brazil 11.7, UK 10.6, France 7.3, CSA 6.8, Cascadia 5.7 |
| Lazar | — | USA 19.05 | UK 10.08 | 1.06 | UK 10.1, Germany 9.5, Brazil 9.1, CSA 5.5, Appalachia 3.7 |
| Neumayer | — | USA 19.51 | France 10.03 | 1.07 | France 10.0, Germany 9.4, CSA 5.6, UK 5.2, Brazil 4.6 |
| Sanay | — | Germany 25.00 | Germany 25.00 | 2.16 | Germany 25.0, Brazil 11.6, UK 7.2, Estonia 4.6, Serbia 4.5 |
| Santa Luce | — | USA 17.02 | Brazil 8.93 | 1.14 | Brazil 8.9, UK 7.8, Magna Lombardia 6.4, CSA 4.9, Russia (core state) 3.8 |
| Troll | — | USA 18.60 | UK 8.44 | 1.01 | UK 8.4, Brazil 8.4, France 5.5, CSA 5.4, Russia (core state) 4.1 |
| **Utstein** | — | Japan 16.94 | **Brazil 8.18** | **1.06** | Brazil 8.2, France 7.7, Australia 7.2, Japan 5.5, Finland 5.3 |
| Cape Adare | 19.85 → 11.51 | USA 22.26 | Australia 12.48 | 1.03 | Australia 12.5, Japan 12.2, Sinian Federation 11.5, Indonesia 10.8, CSA 7.5 |
| Concordia | 7.70 → 4.23 | Japan 9.32 | Japan 10.27 | 1.00 | Japan 10.3, South Korea 10.3, Australia 8.6, Indonesia 8.5, Vietnam 4.2 |
| Denison | 22.29 → 13.19 | USA 26.19 | South Korea 14.21 | 1.08 | South Korea 14.2, Sinian Federation 13.2, Indonesia 12.4, CSA 8.7, Japan 8.6 |
| Dumont d'Urville | 24.31 → 13.88 | China 24.31 | France 14.47 | 1.01 | France 14.5, Japan 14.4, Sinian Federation 13.9, Australia 13.6, CSA 7.1 |
| Fort McMurdo | 19.34 → 9.90 | USA 21.69 | Germany 12.94 | 1.08 | Germany 12.9, France 12.0, Japan 11.2, Sinian Federation 9.9, CSA 7.7 |
| Janbogo | 20.63 → 10.48 | China 20.63 | South Korea 12.38 | 1.02 | South Korea 12.4, Australia 12.1, Italy 11.1, Indonesia 10.7, Sinian Federation 10.5 |
| Scott | 19.48 → 11.30 | USA 22.62 | Japan 12.46 | 1.00 | Japan 12.5, UK 12.4, Sinian Federation 11.3, Australia 10.9, CSA 7.5 |
| Zukelli | 22.63 → 12.21 | China 22.63 | South Korea 13.51 | 1.11 | South Korea 13.5, Sinian Federation 12.2, Australia 11.6, Italy 7.6, Indonesia 7.2 |
| Dome Fuji | 10.13 → 5.13 | USA 11.20 | Indonesia 6.60 | 1.07 | Indonesia 6.6, Australia 6.2, France 6.0, Germany 5.8, South Korea 5.7 |
| Mawson | 17.02 → 8.79 | China 17.02 | UK 10.72 | 1.08 | UK 10.7, Australia 9.9, Indonesia 9.4, Japan 8.9, Sinian Federation 8.8 |
| Temirötkel | 17.39 → 9.28 | China 17.39 | Indonesia 10.21 | 1.04 | Indonesia 10.2, Australia 9.8, Germany 9.8, UK 9.5, Sinian Federation 9.3 |
| **Ariun Nuur** | — | USA 28.36 | **Japan 17.05** | **1.26** | Japan 17.0, Indonesia 13.6, CSA 8.2, Cascadia 7.0, Australia 6.5 |
| Casey | 19.06 → 9.60 | USA 21.96 | South Korea 12.59 | 1.04 | South Korea 12.6, France 12.1, Australia 11.1, Sinian Federation 9.6, CSA 7.6 |
| Davis | 19.04 → 9.97 | China 19.04 | Japan 11.27 | 1.02 | Japan 11.3, Germany 11.0, UK 10.4, Sinian Federation 10.0, South Korea 8.6 |
| Mirny | 24.24 → 12.46 | China 24.24 | UK 15.16 | 1.06 | UK 15.2, South Korea 14.3, Indonesia 13.5, Sinian Federation 12.5, Japan 8.0 |
| Relung Panen | 21.58 → 12.24 | China 21.58 | Indonesia 14.08 | 1.02 | Indonesia 14.1, Japan 13.8, South Korea 12.9, Australia 12.7, Sinian Federation 12.2 |
| Shirayuki | 7.18 → 4.23 | Japan 36.27 | Japan 36.27 | 3.64 | Japan 36.3, Australia 10.0, South Korea 9.0, Germany 5.6, Sinian Federation 4.2 |
| Sinheung | 9.74 → 5.25 | South Korea 34.62 | South Korea 34.62 | 3.15 | South Korea 34.6, Germany 11.0, Japan 9.9, Sinian Federation 5.3, Indonesia 4.4 |
| Zhongshan | 35.83 → 35.83 | China 35.83 | China 35.83 | 3.69 | China 35.8, South Korea 9.7, Germany 8.5, Japan 7.3, Australia 3.7 |
| Contrapunto | — | USA 21.65 | France 11.62 | 1.03 | France 11.6, UK 11.3, Germany 10.7, México 9.0, Brazil 6.7 |
| Esperanza | — | USA 36.36 | Brazil 18.92 | 1.36 | Brazil 18.9, México 13.9, CSA 10.5, UK 9.8, Argentina (without Patagonia) 7.5 |
| Marambio | — | USA 27.59 | Spain 14.19 | 1.05 | Spain 14.2, UK 13.5, México 11.2, CSA 8.0, Germany 6.6 |
| Palmer City | 0.91 → 0.53 | USA 20.29 | Brazil 9.75 | 1.01 | Brazil 9.8, France 9.6, Germany 9.6, CSA 5.9, UK 5.6 |
| Pergamino | — | USA 29.63 | Italy 14.24 | 1.01 | Italy 14.2, Spain 14.1, UK 13.7, CSA 8.6, France 8.5 |
| Puerto Abrigo | — | USA 32.00 | France 16.71 | 1.13 | France 16.7, Germany 14.8, UK 14.3, Brazil 9.7, CSA 9.3 |
| Rothera | — | USA 28.57 | Germany 14.31 | 1.02 | Germany 14.3, Brazil 14.0, CSA 8.3, France 7.4, Cascadia 7.4 |
| Signy | — | USA 33.33 | France 17.19 | 1.01 | France 17.2, UK 17.0, CSA 9.6, Brazil 8.0, Germany 7.8 |

**Reading it (DERIVED):**
- **31 of 37 cities now have their leading nation at most 1.14 times the next** (Utstein joins them). The six
  exceptions are all ruled or intended: the three founding allocations (Zhongshan, Shirayuki, Sinheung), Sanay and
  Esperanza (left as they are), and Ariun Nuur.
- **Ariun Nuur (redrawn):** Japan falls from 24.97% to 17.05% and still leads (1.26 times Indonesia's 13.55%).
  Mongolia 4.19%, Künnarantaiga 3.73% (5,944 and 5,290 humans). For any draw Japan lands between 14.97% and
  17.97%.
- **Utstein:** Japan falls from 16.94% to 5.49%. **The five Nordic founders together are 16.78%,** the city's
  largest bloc (Finland 5.34%, Norway 5.17%, Denmark 3.07%, Sweden 2.65%, Iceland 0.55%); no single nation leads
  (Brazil 8.18%, 1.06 times France). For any draw Japan would land between 1.94% and 10.44%.

### Nationally (Census I humans, 15,612,333 in the specs)

| Rank | Nation or successor | Humans | Share | Before |
|--:|---|--:|--:|---|
| 1 | South Korea | 1,007,710 | 6.45% | 892,502 |
| 2 | Sinian Federation | 992,151 | 6.35% | China 1,660,450 |
| 3 | Japan | 979,879 | 6.28% | 953,710 |
| 4 | UK | 907,615 | 5.81% | 855,222 |
| 5 | Australia | 840,752 | 5.39% | 727,081 |
| 6 | Germany | 774,542 | 4.96% | 735,406 |
| 7 | CSA | 757,865 | 4.85% | part of the USA (2,462,596) |
| 8 | Indonesia | 706,082 | 4.52% | 606,976 |
| 9 | Brazil | 705,086 | 4.52% | 704,963 |
| 10 | France | 524,494 | 3.36% | 490,468 |

*The full national table (72 rows) is in the appendix.* **The founders' national figures:** Norway 134,882 (was
121,223), Finland 119,032 (was 103,357), Sweden 54,640 (was 39,657), Künnarantaiga 46,016, Denmark 17,367 (new),
Mongolia 5,944 (new), Iceland 3,136 (new).

**Against run 2:** doing the splits first moves part of the fill to the American successors (the CSA rises from
4.56% to 4.85% nationally), and the founder moves take Japan from 6.76% to 6.28%, so **South Korea is now first
nationally**, the Sinian Federation second and Japan third, all within 0.2 points of each other.

## Things to know before this is applied for real

1. **Three new nations enter Tepenia's tables: Mongolia, Denmark and Iceland.** None has a row in the composition
   file's pool table. Mongolia's would come from Inner Mongolia's part of China's pool plus today's Mongolia
   (`03`); Denmark and Iceland are not in the master list at all. As founder rows set by hand, like Zhongshan's
   adjustments, they do not need pools; the composition file would just need to say so.
2. **The tier labels** (Primary, Significant, Notable) no longer follow from the numbers in most cities, and the
   new founder rows are labeled "Founder (new row)" here. Relabeling is a separate, mechanical step.
3. **Founders, after the splits:** Mirny's founder Idelsk-Uralia now has a row (1.69%, from Russia's split).
   **Lazar's founder, Russia's core state, drops from 4.81% (as "Russia") to 2.01%**, because the pool split gives
   the core state 41.83% of Russia's row. Still without rows: Kazakhstan (Temirötkel, Mawson) and Russia's core
   state at Mawson. Under the line: New Zealand at Scott (3.52%), Malaysia at Relung Panen (3.30%).
4. **Still open from before:** Option A or B (B used throughout); Canada's Demilitarized Zone (its own row here,
   up to 5.2% of a city); rows for the pieces that left China; Hong Kong, Macau and Taiwan; Sardinia; Austria,
   Chile and Petén; which era's borders; Kunlun's co-founders; and the four cities recommended to wait (Concordia,
   Dome Fuji, Relung Panen, Amundsen Station), which are computed here for completeness.

---

## Appendix: the script's full output

*Pasted from `python3 calc_rebalance_v3.py`, unedited apart from heading levels (regenerated after the Ariun Nuur redraw).*

### The founder draws (seeds: Ariun Nuur 202611012343, Utstein 2026110123)

| City | Row | Points moved from Japan |
|---|---|--:|
| Ariun Nuur | Mongolia | 4.19 |
| Ariun Nuur | Künnarantaiga | 3.73 |
| Ariun Nuur | **Japan, total moved** | **7.92** |
| Utstein | Iceland | 0.55 |
| Utstein | Norway | 2.41 |
| Utstein | Sweden | 2.65 |
| Utstein | Finland | 2.77 |
| Utstein | Denmark | 3.07 |
| Utstein | **Japan, total moved** | **11.45** |

*Every city keeps its exact total in every census column, and no count is negative: yes.*

### Every city, after all three steps

| City | China → Sinian Fed. | Leader before | Leader after | Lead after (1st ÷ 2nd) | Top five after (%) |
|---|---|---|---|--:|---|
| Amundsen Station | 19.31 → 11.33 | USA 22.80 | UK 12.17 | 1.05 | UK 12.2, Germany 11.6, Sinian Federation 11.3, Japan 11.0, CSA 7.6 |
| Byrd | 2.95 → 1.67 | USA 13.57 | Australia 7.07 | 1.04 | Australia 7.1, Japan 6.8, Demilitarized Zone 4.2, Cascadia 4.1, CSA 3.9 |
| Belgrano | — | USA 28.57 | Brazil 13.73 | 1.02 | Brazil 13.7, Germany 13.4, CSA 8.3, Appalachia 5.6, New England 5.6 |
| Halley | — | USA 23.53 | Brazil 11.69 | 1.11 | Brazil 11.7, UK 10.6, France 7.3, CSA 6.8, Cascadia 5.7 |
| Lazar | — | USA 19.05 | UK 10.08 | 1.06 | UK 10.1, Germany 9.5, Brazil 9.1, CSA 5.5, Appalachia 3.7 |
| Neumayer | — | USA 19.51 | France 10.03 | 1.07 | France 10.0, Germany 9.4, CSA 5.6, UK 5.2, Brazil 4.6 |
| Sanay | — | Germany 25.00 | Germany 25.00 | 2.16 | Germany 25.0, Brazil 11.6, UK 7.2, Estonia 4.6, Serbia 4.5 |
| Santa Luce | — | USA 17.02 | Brazil 8.93 | 1.14 | Brazil 8.9, UK 7.8, Magna Lombardia 6.4, CSA 4.9, Russia (core state) 3.8 |
| Troll | — | USA 18.60 | UK 8.44 | 1.01 | UK 8.4, Brazil 8.4, France 5.5, CSA 5.4, Russia (core state) 4.1 |
| Utstein | — | Japan 16.94 | Brazil 8.18 | 1.06 | Brazil 8.2, France 7.7, Australia 7.2, Japan 5.5, Finland 5.3 |
| Cape Adare | 19.85 → 11.51 | USA 22.26 | Australia 12.48 | 1.03 | Australia 12.5, Japan 12.2, Sinian Federation 11.5, Indonesia 10.8, CSA 7.5 |
| Concordia | 7.70 → 4.23 | Japan 9.32 | Japan 10.27 | 1.00 | Japan 10.3, South Korea 10.3, Australia 8.6, Indonesia 8.5, Vietnam 4.2 |
| Denison | 22.29 → 13.19 | USA 26.19 | South Korea 14.21 | 1.08 | South Korea 14.2, Sinian Federation 13.2, Indonesia 12.4, CSA 8.7, Japan 8.6 |
| Dumont d'Urville | 24.31 → 13.88 | China 24.31 | France 14.47 | 1.01 | France 14.5, Japan 14.4, Sinian Federation 13.9, Australia 13.6, CSA 7.1 |
| Fort McMurdo | 19.34 → 9.90 | USA 21.69 | Germany 12.94 | 1.08 | Germany 12.9, France 12.0, Japan 11.2, Sinian Federation 9.9, CSA 7.7 |
| Janbogo | 20.63 → 10.48 | China 20.63 | South Korea 12.38 | 1.02 | South Korea 12.4, Australia 12.1, Italy 11.1, Indonesia 10.7, Sinian Federation 10.5 |
| Scott | 19.48 → 11.30 | USA 22.62 | Japan 12.46 | 1.00 | Japan 12.5, UK 12.4, Sinian Federation 11.3, Australia 10.9, CSA 7.5 |
| Zukelli | 22.63 → 12.21 | China 22.63 | South Korea 13.51 | 1.11 | South Korea 13.5, Sinian Federation 12.2, Australia 11.6, Italy 7.6, Indonesia 7.2 |
| Dome Fuji | 10.13 → 5.13 | USA 11.20 | Indonesia 6.60 | 1.07 | Indonesia 6.6, Australia 6.2, France 6.0, Germany 5.8, South Korea 5.7 |
| Mawson | 17.02 → 8.79 | China 17.02 | UK 10.72 | 1.08 | UK 10.7, Australia 9.9, Indonesia 9.4, Japan 8.9, Sinian Federation 8.8 |
| Temirötkel | 17.39 → 9.28 | China 17.39 | Indonesia 10.21 | 1.04 | Indonesia 10.2, Australia 9.8, Germany 9.8, UK 9.5, Sinian Federation 9.3 |
| Ariun Nuur | — | USA 28.36 | Japan 17.05 | 1.26 | Japan 17.0, Indonesia 13.6, CSA 8.2, Cascadia 7.0, Australia 6.5 |
| Casey | 19.06 → 9.60 | USA 21.96 | South Korea 12.59 | 1.04 | South Korea 12.6, France 12.1, Australia 11.1, Sinian Federation 9.6, CSA 7.6 |
| Davis | 19.04 → 9.97 | China 19.04 | Japan 11.27 | 1.02 | Japan 11.3, Germany 11.0, UK 10.4, Sinian Federation 10.0, South Korea 8.6 |
| Mirny | 24.24 → 12.46 | China 24.24 | UK 15.16 | 1.06 | UK 15.2, South Korea 14.3, Indonesia 13.5, Sinian Federation 12.5, Japan 8.0 |
| Relung Panen | 21.58 → 12.24 | China 21.58 | Indonesia 14.08 | 1.02 | Indonesia 14.1, Japan 13.8, South Korea 12.9, Australia 12.7, Sinian Federation 12.2 |
| Shirayuki | 7.18 → 4.23 | Japan 36.27 | Japan 36.27 | 3.64 | Japan 36.3, Australia 10.0, South Korea 9.0, Germany 5.6, Sinian Federation 4.2 |
| Sinheung | 9.74 → 5.25 | South Korea 34.62 | South Korea 34.62 | 3.15 | South Korea 34.6, Germany 11.0, Japan 9.9, Sinian Federation 5.3, Indonesia 4.4 |
| Zhongshan | 35.83 → 35.83 | China 35.83 | China 35.83 | 3.69 | China 35.8, South Korea 9.7, Germany 8.5, Japan 7.3, Australia 3.7 |
| Contrapunto | — | USA 21.65 | France 11.62 | 1.03 | France 11.6, UK 11.3, Germany 10.7, México 9.0, Brazil 6.7 |
| Esperanza | — | USA 36.36 | Brazil 18.92 | 1.36 | Brazil 18.9, México 13.9, CSA 10.5, UK 9.8, Argentina (without Patagonia) 7.5 |
| Marambio | — | USA 27.59 | Spain 14.19 | 1.05 | Spain 14.2, UK 13.5, México 11.2, CSA 8.0, Germany 6.6 |
| Palmer City | 0.91 → 0.53 | USA 20.29 | Brazil 9.75 | 1.01 | Brazil 9.8, France 9.6, Germany 9.6, CSA 5.9, UK 5.6 |
| Pergamino | — | USA 29.63 | Italy 14.24 | 1.01 | Italy 14.2, Spain 14.1, UK 13.7, CSA 8.6, France 8.5 |
| Puerto Abrigo | — | USA 32.00 | France 16.71 | 1.13 | France 16.7, Germany 14.8, UK 14.3, Brazil 9.7, CSA 9.3 |
| Rothera | — | USA 28.57 | Germany 14.31 | 1.02 | Germany 14.3, Brazil 14.0, CSA 8.3, France 7.4, Cascadia 7.4 |
| Signy | — | USA 33.33 | France 17.19 | 1.01 | France 17.2, UK 17.0, CSA 9.6, Brazil 8.0, Germany 7.8 |

### Nationally (Census I humans, 15,612,333 in the specs)

| Rank | Nation or successor | Humans after | Share | Before (as listed today) |
|--:|---|--:|--:|---|
| 1 | South Korea | 1,007,710 | 6.45% | 892,502 |
| 2 | Sinian Federation | 992,151 | 6.35% | China 1,660,450 |
| 3 | Japan | 979,879 | 6.28% | 953,710 |
| 4 | UK | 907,615 | 5.81% | 855,222 |
| 5 | Australia | 840,752 | 5.39% | 727,081 |
| 6 | Germany | 774,542 | 4.96% | 735,406 |
| 7 | CSA | 757,865 | 4.85% | part of USA |
| 8 | Indonesia | 706,082 | 4.52% | 606,976 |
| 9 | Brazil | 705,086 | 4.52% | 704,963 |
| 10 | France | 524,494 | 3.36% | 490,468 |
| 11 | Cascadia | 517,623 | 3.32% | part of USA, Canada, Mexico |
| 12 | Appalachia | 487,366 | 3.12% | part of USA |
| 13 | New England | 484,021 | 3.10% | part of USA |
| 14 | Chile | 229,408 | 1.47% | 229,408 |
| 15 | New Zealand | 226,668 | 1.45% | 226,668 |
| 16 | México | 222,079 | 1.42% | part of Mexico |
| 17 | Argentina (without Patagonia) | 215,331 | 1.38% | part of Argentina |
| 18 | Russia (core state) | 210,539 | 1.35% | part of Russia |
| 19 | Philippines | 203,480 | 1.30% | 196,541 |
| 20 | Vietnam | 201,016 | 1.29% | 197,574 |
| 21 | Malaysia | 198,508 | 1.27% | 198,508 |
| 22 | Italy | 188,700 | 1.21% | 164,828 |
| 23 | Thailand | 176,905 | 1.13% | 173,181 |
| 24 | Hungary | 166,778 | 1.07% | 166,778 |
| 25 | Estonia | 165,919 | 1.06% | 165,919 |
| 26 | South Africa | 162,098 | 1.04% | 162,098 |
| 27 | Romania | 157,022 | 1.01% | 157,022 |
| 28 | Midwest Republic | 151,247 | 0.97% | part of USA |
| 29 | Poland | 150,296 | 0.96% | 150,296 |
| 30 | Slovenia | 150,283 | 0.96% | 150,283 |
| 31 | Serbia | 148,201 | 0.95% | 148,201 |
| 32 | Czech Republic | 143,563 | 0.92% | 143,563 |
| 33 | Slovakia | 140,484 | 0.90% | 140,484 |
| 34 | Lithuania | 136,473 | 0.87% | 136,473 |
| 35 | Bulgaria | 136,049 | 0.87% | 136,049 |
| 36 | Norway | 134,882 | 0.86% | 121,223 |
| 37 | Ukraine | 130,844 | 0.84% | 130,844 |
| 38 | Croatia | 129,454 | 0.83% | 129,454 |
| 39 | Belarus | 122,235 | 0.78% | 122,235 |
| 40 | Demilitarized Zone (s. Ontario; not a nation) | 119,833 | 0.77% | part of Canada |
| 41 | Finland | 119,032 | 0.76% | 103,357 |
| 42 | Uruguay | 119,026 | 0.76% | 119,026 |
| 43 | Latvia | 117,792 | 0.75% | 117,792 |
| 44 | Netherlands | 117,470 | 0.75% | 117,470 |
| 45 | Colorado | 116,898 | 0.75% | part of USA |
| 46 | Idelsk-Uralia | 115,695 | 0.74% | part of Russia |
| 47 | Siberia | 83,520 | 0.53% | part of Russia |
| 48 | Quebec | 82,760 | 0.53% | part of Canada |
| 49 | Sonora | 79,695 | 0.51% | part of USA, Mexico |
| 50 | Prairie Federation | 78,731 | 0.50% | part of Canada |
| 51 | Spain | 77,165 | 0.49% | 77,165 |
| 52 | Sweden | 54,640 | 0.35% | 39,657 |
| 53 | Künnarantaiga | 46,016 | 0.29% | part of Russia |
| 54 | Belgium | 42,545 | 0.27% | 42,545 |
| 55 | Donska-Kubania | 35,188 | 0.23% | part of Russia |
| 56 | Yucatán | 24,790 | 0.16% | part of Mexico |
| 57 | Araucanía-Patagonia | 24,081 | 0.15% | part of Argentina |
| 58 | Denmark | 17,367 | 0.11% | new row |
| 59 | Magna Lombardia | 13,649 | 0.09% | 13,649 |
| 60 | Hawaii | 10,029 | 0.06% | part of USA |
| 61 | Alaska | 6,781 | 0.04% | part of USA, Canada |
| 62 | Mongolia | 5,944 | 0.04% | new row |
| 63 | Karelia | 4,792 | 0.03% | part of Russia |
| 64 | Meridia | 4,550 | 0.03% | 4,550 |
| 65 | Iceland | 3,136 | 0.02% | new row |
| 66 | Dagestan | 3,014 | 0.02% | part of Russia |
| 67 | Chechnya | 1,434 | 0.01% | part of Russia |
| 68 | Kabardino-Balkaria | 987 | 0.01% | part of Russia |
| 69 | North Ossetia-Alania | 940 | 0.01% | part of Russia |
| 70 | Karachay-Cherkessia | 493 | 0.00% | part of Russia |
| 71 | Tuva | 396 | 0.00% | part of Russia |
| 72 | Ingushetia | 296 | 0.00% | part of Russia |

### City by city (rows under 0.10% added together by source country; every row is in the CSV)

#### Amundsen Station

*Sinian draw 0.6410; fill to: CSA, Cascadia, UK, Germany, Japan, South Korea, Australia*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | UK |  | 10.57% | 12.17% | 136 |
| Significant | Germany |  | 10.09% | 11.62% | 130 |
| Primary | Sinian Federation | China | 19.31% | 11.33% | 127 |
| Significant | Japan |  | 9.59% | 11.04% | 123 |
| Primary | CSA | USA | — | 7.59% | 85 |
| Significant | South Korea |  | 5.70% | 6.56% | 74 |
| Significant | Australia |  | 5.22% | 6.01% | 68 |
| Primary | Cascadia | USA + Canada | — | 5.70% | 64 |
| Primary | Appalachia | USA | — | 4.48% | 50 |
| Primary | New England | USA | — | 4.45% | 50 |
| Notable | New Zealand |  | 3.59% | 3.59% | 40 |
| Notable | Argentina (without Patagonia) | Argentina | — | 3.23% | 36 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 2.27% | 25 |
| Notable | Norway |  | 1.67% | 1.67% | 19 |
| Notable | Chile |  | 1.67% | 1.67% | 19 |
| Significant | Quebec | Canada | — | 1.56% | 18 |
| Significant | Prairie Federation | Canada | — | 1.49% | 17 |
| Primary | Midwest Republic | USA | — | 1.40% | 16 |
| Primary | Colorado | USA | — | 1.08% | 12 |
| Primary | Sonora | USA | — | 0.56% | 6 |
| Notable | Araucanía-Patagonia | Argentina | — | 0.36% | 4 |
| | *1 smaller USA successor* | USA | — | 0.09% | 1 |
| | *1 smaller USA + Canada successor* | USA + Canada | — | 0.08% | 1 |

#### Byrd

*Sinian draw 0.6184; fill to: Australia, Japan*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Australia |  | 6.42% | 7.07% | 14,030 |
| Significant | Japan |  | 6.19% | 6.82% | 13,527 |
| Primary | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 4.18% | 8,286 |
| Primary | Cascadia | USA + Canada + Mexico | — | 4.06% | 8,055 |
| Primary | CSA | USA | — | 3.92% | 7,784 |
| Significant | South Korea |  | 3.19% | 3.19% | 6,329 |
| Primary | Quebec | Canada | — | 2.88% | 5,722 |
| Primary | Prairie Federation | Canada | — | 2.74% | 5,444 |
| Primary | Appalachia | USA | — | 2.67% | 5,289 |
| Primary | New England | USA | — | 2.65% | 5,252 |
| Notable | Lithuania |  | 2.27% | 2.27% | 4,504 |
| Notable | Philippines |  | 2.23% | 2.23% | 4,425 |
| Notable | Thailand |  | 2.22% | 2.22% | 4,404 |
| Notable | Indonesia |  | 2.21% | 2.21% | 4,385 |
| Notable | Malaysia |  | 2.20% | 2.20% | 4,365 |
| Notable | Brazil |  | 2.20% | 2.20% | 4,365 |
| Notable | Croatia |  | 2.16% | 2.16% | 4,285 |
| Notable | Latvia |  | 2.15% | 2.15% | 4,266 |
| Notable | Netherlands |  | 2.10% | 2.10% | 4,167 |
| Notable | Slovakia |  | 2.06% | 2.06% | 4,087 |
| Notable | South Africa |  | 2.02% | 2.02% | 4,008 |
| Notable | Czech Republic |  | 1.96% | 1.96% | 3,889 |
| Notable | Uruguay |  | 1.96% | 1.96% | 3,889 |
| Notable | Vietnam |  | 1.94% | 1.94% | 3,850 |
| Notable | UK |  | 1.93% | 1.93% | 3,829 |
| Notable | Finland |  | 1.90% | 1.90% | 3,770 |
| Notable | New Zealand |  | 1.90% | 1.90% | 3,770 |
| Notable | Romania |  | 1.90% | 1.90% | 3,770 |
| Significant | Sinian Federation | China | 2.95% | 1.67% | 3,314 |
| Notable | Norway |  | 1.23% | 1.23% | 2,440 |
| Notable | Hungary |  | 1.23% | 1.23% | 2,440 |
| Notable | Ukraine |  | 1.22% | 1.22% | 2,420 |
| Notable | Germany |  | 1.19% | 1.19% | 2,361 |
| Notable | Belarus |  | 1.17% | 1.17% | 2,321 |
| Notable | Poland |  | 1.16% | 1.16% | 2,302 |
| Notable | France |  | 1.11% | 1.11% | 2,203 |
| Notable | Bulgaria |  | 1.06% | 1.06% | 2,103 |
| Notable | Chile |  | 1.02% | 1.02% | 2,024 |
| Notable | Italy |  | 0.92% | 0.92% | 1,826 |
| Notable | Slovenia |  | 0.92% | 0.92% | 1,826 |
| Notable | Spain |  | 0.91% | 0.91% | 1,805 |
| Notable | Belgium |  | 0.91% | 0.91% | 1,805 |
| Notable | Sweden |  | 0.90% | 0.90% | 1,785 |
| Notable | Argentina (without Patagonia) | Argentina | — | 0.88% | 1,748 |
| Notable | Serbia |  | 0.86% | 0.86% | 1,706 |
| Primary | Midwest Republic | USA | — | 0.83% | 1,654 |
| Notable | México | Mexico | — | 0.77% | 1,518 |
| Primary | Colorado | USA | — | 0.64% | 1,278 |
| Notable | Russia (core state) | Russia | — | 0.50% | 988 |
| Primary | Sonora | USA + Mexico | — | 0.40% | 793 |
| Notable | Idelsk-Uralia | Russia | — | 0.28% | 553 |
| Notable | Siberia | Russia | — | 0.20% | 399 |
| | *1 smaller Argentina successor* | Argentina | — | 0.10% | 196 |
| | *10 smaller Russia successors* | Russia | — | 0.21% | 421 |
| | *1 smaller Mexico successor* | Mexico | — | 0.09% | 170 |
| | *1 smaller USA + Canada successor* | USA + Canada | — | 0.08% | 151 |
| | *1 smaller USA successor* | USA | — | 0.06% | 110 |

#### Belgrano

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Brazil |  | 13.73% | 13.73% | 74,683 |
| Significant | Germany |  | 13.44% | 13.44% | 73,128 |
| Primary | CSA | USA | — | 8.26% | 44,943 |
| Primary | Appalachia | USA | — | 5.61% | 30,535 |
| Primary | New England | USA | — | 5.57% | 30,325 |
| Notable | Hungary |  | 5.32% | 5.32% | 28,952 |
| Notable | Poland |  | 5.18% | 5.18% | 28,201 |
| Primary | Cascadia | USA | — | 5.13% | 27,924 |
| Significant | UK |  | 4.97% | 4.97% | 27,066 |
| Notable | Uruguay |  | 4.91% | 4.91% | 26,741 |
| Notable | Slovakia |  | 4.66% | 4.66% | 25,378 |
| Notable | Chile |  | 4.34% | 4.34% | 23,635 |
| Notable | Argentina (without Patagonia) | Argentina | — | 3.96% | 21,528 |
| Notable | Czech Republic |  | 2.80% | 2.80% | 15,226 |
| Notable | Slovenia |  | 2.74% | 2.74% | 14,926 |
| Notable | South Africa |  | 2.48% | 2.48% | 13,484 |
| Notable | Serbia |  | 1.82% | 1.82% | 9,910 |
| Primary | Midwest Republic | USA | — | 1.75% | 9,547 |
| Primary | Colorado | USA | — | 1.36% | 7,379 |
| Primary | Sonora | USA | — | 0.70% | 3,816 |
| Notable | Croatia |  | 0.62% | 0.62% | 3,351 |
| Notable | Araucanía-Patagonia | Argentina | — | 0.44% | 2,408 |
| Primary | Hawaii | USA | — | 0.12% | 633 |
| | *1 smaller USA successor* | USA | — | 0.06% | 345 |

#### Halley

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Brazil |  | 11.69% | 11.69% | 84,380 |
| Significant | UK |  | 10.57% | 10.57% | 76,332 |
| Significant | France |  | 7.31% | 7.31% | 52,779 |
| Primary | CSA | USA | — | 6.80% | 49,109 |
| Primary | Cascadia | USA + Canada | — | 5.66% | 40,823 |
| Primary | Appalachia | USA | — | 4.62% | 33,365 |
| Primary | New England | USA | — | 4.59% | 33,137 |
| Notable | Netherlands |  | 4.30% | 4.30% | 31,063 |
| Significant | Germany |  | 4.21% | 4.21% | 30,377 |
| Notable | Croatia |  | 4.16% | 4.16% | 29,998 |
| Notable | Serbia |  | 4.10% | 4.10% | 29,616 |
| Notable | Slovenia |  | 4.08% | 4.08% | 29,443 |
| Notable | Chile |  | 3.82% | 3.82% | 27,575 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 3.78% | 27,263 |
| Notable | Poland |  | 3.56% | 3.56% | 25,699 |
| Significant | Quebec | Canada | — | 2.61% | 18,828 |
| Significant | Prairie Federation | Canada | — | 2.48% | 17,912 |
| Notable | Argentina (without Patagonia) | Argentina | — | 2.09% | 15,079 |
| Notable | South Africa |  | 1.80% | 1.80% | 13,021 |
| Notable | Czech Republic |  | 1.78% | 1.78% | 12,848 |
| Notable | Hungary |  | 1.58% | 1.58% | 11,401 |
| Primary | Midwest Republic | USA | — | 1.45% | 10,432 |
| Primary | Colorado | USA | — | 1.12% | 8,063 |
| Notable | Slovakia |  | 0.85% | 0.85% | 6,123 |
| Primary | Sonora | USA | — | 0.58% | 4,169 |
| Notable | Araucanía-Patagonia | Argentina | — | 0.23% | 1,686 |
| | *1 smaller USA successor* | USA | — | 0.10% | 692 |
| | *1 smaller USA + Canada successor* | USA + Canada | — | 0.09% | 676 |

#### Lazar

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | UK |  | 10.08% | 10.08% | 117,927 |
| Significant | Germany |  | 9.48% | 9.48% | 110,946 |
| Significant | Brazil |  | 9.05% | 9.05% | 105,932 |
| Primary | CSA | USA | — | 5.51% | 64,457 |
| Primary | Appalachia | USA | — | 3.74% | 43,793 |
| Primary | New England | USA | — | 3.72% | 43,493 |
| Primary | Cascadia | USA | — | 3.42% | 40,048 |
| Notable | Norway |  | 3.42% | 3.42% | 40,028 |
| Notable | Finland |  | 3.34% | 3.34% | 39,040 |
| Notable | Czech Republic |  | 3.30% | 3.30% | 38,655 |
| Notable | Estonia |  | 3.29% | 3.29% | 38,517 |
| Notable | Poland |  | 3.21% | 3.21% | 37,604 |
| Notable | Hungary |  | 3.08% | 3.08% | 36,021 |
| Notable | Slovenia |  | 3.07% | 3.07% | 35,881 |
| Notable | Slovakia |  | 3.00% | 3.00% | 35,117 |
| Notable | Serbia |  | 2.95% | 2.95% | 34,503 |
| Notable | Romania |  | 2.87% | 2.87% | 33,600 |
| Significant | France |  | 2.30% | 2.30% | 26,951 |
| Significant | Russia (core state) | Russia | — | 2.01% | 23,534 |
| Notable | Belarus |  | 1.81% | 1.81% | 21,232 |
| Notable | Lithuania |  | 1.76% | 1.76% | 20,619 |
| Notable | Ukraine |  | 1.70% | 1.70% | 19,854 |
| Notable | South Africa |  | 1.55% | 1.55% | 18,131 |
| Notable | Croatia |  | 1.47% | 1.47% | 17,219 |
| Notable | Latvia |  | 1.43% | 1.43% | 16,695 |
| Notable | Bulgaria |  | 1.34% | 1.34% | 15,708 |
| Notable | Argentina (without Patagonia) | Argentina | — | 1.31% | 15,362 |
| Notable | Netherlands |  | 1.19% | 1.19% | 13,981 |
| Primary | Midwest Republic | USA | — | 1.17% | 13,692 |
| Significant | Idelsk-Uralia | Russia | — | 1.13% | 13,171 |
| Primary | Colorado | USA | — | 0.90% | 10,583 |
| Significant | Siberia | Russia | — | 0.81% | 9,508 |
| Primary | Sonora | USA | — | 0.47% | 5,472 |
| Significant | Künnarantaiga | Russia | — | 0.40% | 4,636 |
| Significant | Donska-Kubania | Russia | — | 0.34% | 4,006 |
| Notable | Araucanía-Patagonia | Argentina | — | 0.15% | 1,718 |
| | *2 smaller USA successors* | USA | — | 0.12% | 1,403 |
| | *8 smaller Russia successors* | Russia | — | 0.12% | 1,406 |

#### Neumayer

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | France |  | 10.03% | 10.03% | 62,801 |
| Significant | Germany |  | 9.39% | 9.39% | 58,766 |
| Primary | CSA | USA | — | 5.64% | 35,308 |
| Significant | UK |  | 5.24% | 5.24% | 32,826 |
| Significant | Brazil |  | 4.60% | 4.60% | 28,790 |
| Primary | Appalachia | USA | — | 3.83% | 23,989 |
| Primary | New England | USA | — | 3.81% | 23,824 |
| Notable | Sweden |  | 3.65% | 3.65% | 22,846 |
| Notable | Lithuania |  | 3.60% | 3.60% | 22,558 |
| Notable | Hungary |  | 3.53% | 3.53% | 22,123 |
| Primary | Cascadia | USA | — | 3.50% | 21,937 |
| Notable | Slovakia |  | 3.32% | 3.32% | 20,795 |
| Notable | Bulgaria |  | 3.10% | 3.10% | 19,400 |
| Notable | Ukraine |  | 3.05% | 3.05% | 19,115 |
| Notable | Finland |  | 3.01% | 3.01% | 18,820 |
| Notable | Croatia |  | 3.01% | 3.01% | 18,813 |
| Notable | Romania |  | 2.99% | 2.99% | 18,735 |
| Notable | Chile |  | 2.99% | 2.99% | 18,700 |
| Notable | Argentina (without Patagonia) | Argentina | — | 2.84% | 17,770 |
| Notable | Belgium |  | 1.89% | 1.89% | 11,830 |
| Notable | Latvia |  | 1.87% | 1.87% | 11,717 |
| Notable | Estonia |  | 1.87% | 1.87% | 11,711 |
| Notable | Serbia |  | 1.82% | 1.82% | 11,416 |
| Notable | Norway |  | 1.78% | 1.78% | 11,130 |
| Notable | Netherlands |  | 1.56% | 1.56% | 9,735 |
| Notable | Czech Republic |  | 1.34% | 1.34% | 8,407 |
| Notable | Slovenia |  | 1.27% | 1.27% | 7,974 |
| Notable | Poland |  | 1.23% | 1.23% | 7,684 |
| Primary | Midwest Republic | USA | — | 1.20% | 7,500 |
| Notable | South Africa |  | 1.17% | 1.17% | 7,304 |
| Primary | Colorado | USA | — | 0.93% | 5,797 |
| Primary | Sonora | USA | — | 0.48% | 2,998 |
| Notable | Araucanía-Patagonia | Argentina | — | 0.32% | 1,987 |
| | *2 smaller USA successors* | USA | — | 0.12% | 768 |

#### Sanay

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Primary | Germany |  | 25.00% | 25.00% | 60,929 |
| Significant | Brazil |  | 11.57% | 11.57% | 28,204 |
| Significant | UK |  | 7.18% | 7.18% | 17,492 |
| Notable | Estonia |  | 4.58% | 4.58% | 11,151 |
| Notable | Serbia |  | 4.53% | 4.53% | 11,041 |
| Notable | South Africa |  | 4.48% | 4.48% | 10,923 |
| Notable | Ukraine |  | 4.21% | 4.21% | 10,253 |
| Notable | Slovenia |  | 4.11% | 4.11% | 10,018 |
| Notable | Hungary |  | 4.10% | 4.10% | 10,002 |
| Notable | Bulgaria |  | 3.95% | 3.95% | 9,636 |
| Notable | Norway |  | 3.87% | 3.87% | 9,421 |
| Notable | Argentina (without Patagonia) | Argentina | — | 3.80% | 9,250 |
| Notable | Czech Republic |  | 2.38% | 2.38% | 5,811 |
| Notable | Romania |  | 2.30% | 2.30% | 5,596 |
| Notable | Croatia |  | 2.15% | 2.15% | 5,230 |
| Notable | Latvia |  | 2.14% | 2.14% | 5,214 |
| Notable | Slovakia |  | 2.04% | 2.04% | 4,980 |
| Notable | Poland |  | 2.03% | 2.03% | 4,947 |
| Notable | Lithuania |  | 1.77% | 1.77% | 4,310 |
| Notable | Belarus |  | 1.72% | 1.72% | 4,191 |
| Notable | Chile |  | 1.67% | 1.67% | 4,081 |
| Notable | Araucanía-Patagonia | Argentina | — | 0.42% | 1,034 |

#### Santa Luce

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Brazil |  | 8.93% | 8.93% | 19,097 |
| Significant | UK |  | 7.81% | 7.81% | 16,704 |
| Significant | Magna Lombardia |  | 6.38% | 6.38% | 13,649 |
| Primary | CSA | USA | — | 4.92% | 10,523 |
| Significant | Russia (core state) | Russia | — | 3.78% | 8,086 |
| Significant | France |  | 3.72% | 3.72% | 7,968 |
| Primary | Appalachia | USA | — | 3.34% | 7,150 |
| Primary | New England | USA | — | 3.32% | 7,101 |
| Primary | Cascadia | USA | — | 3.06% | 6,538 |
| Notable | Latvia |  | 3.04% | 3.04% | 6,488 |
| Notable | Netherlands |  | 2.91% | 2.91% | 6,229 |
| Notable | Croatia |  | 2.84% | 2.84% | 6,073 |
| Notable | Estonia |  | 2.84% | 2.84% | 6,058 |
| Notable | Ukraine |  | 2.84% | 2.84% | 6,073 |
| Notable | Serbia |  | 2.79% | 2.79% | 5,976 |
| Notable | Argentina (without Patagonia) | Argentina | — | 2.75% | 5,902 |
| Notable | Czech Republic |  | 2.71% | 2.71% | 5,795 |
| Notable | Hungary |  | 2.68% | 2.68% | 5,727 |
| Notable | Romania |  | 2.62% | 2.62% | 5,591 |
| Significant | Germany |  | 2.41% | 2.41% | 5,146 |
| Notable | Meridia |  | 2.13% | 2.13% | 4,550 |
| Significant | Idelsk-Uralia | Russia | — | 2.12% | 4,525 |
| Notable | Sweden |  | 1.64% | 1.64% | 3,509 |
| Notable | Lithuania |  | 1.57% | 1.57% | 3,372 |
| Notable | Belgium |  | 1.55% | 1.55% | 3,304 |
| Significant | Siberia | Russia | — | 1.53% | 3,267 |
| Notable | Bulgaria |  | 1.46% | 1.46% | 3,123 |
| Notable | Norway |  | 1.42% | 1.42% | 3,026 |
| Notable | Slovakia |  | 1.42% | 1.42% | 3,041 |
| Notable | South Africa |  | 1.42% | 1.42% | 3,026 |
| Notable | Finland |  | 1.34% | 1.34% | 2,870 |
| Notable | Slovenia |  | 1.22% | 1.22% | 2,612 |
| Notable | Poland |  | 1.19% | 1.19% | 2,538 |
| Primary | Midwest Republic | USA | — | 1.05% | 2,235 |
| Primary | Colorado | USA | — | 0.81% | 1,728 |
| Significant | Künnarantaiga | Russia | — | 0.74% | 1,593 |
| Significant | Donska-Kubania | Russia | — | 0.64% | 1,376 |
| Primary | Sonora | USA | — | 0.42% | 893 |
| Notable | Araucanía-Patagonia | Argentina | — | 0.31% | 660 |
| | *8 smaller Russia successors* | Russia | — | 0.23% | 483 |
| | *2 smaller USA successors* | USA | — | 0.11% | 229 |

#### Troll

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | UK |  | 8.44% | 8.44% | 41,157 |
| Significant | Brazil |  | 8.38% | 8.38% | 40,900 |
| Significant | France |  | 5.52% | 5.52% | 26,917 |
| Primary | CSA | USA | — | 5.38% | 26,242 |
| Significant | Russia (core state) | Russia | — | 4.13% | 20,169 |
| Primary | Appalachia | USA | — | 3.65% | 17,829 |
| Primary | New England | USA | — | 3.63% | 17,707 |
| Notable | Czech Republic |  | 3.39% | 3.39% | 16,549 |
| Notable | Slovakia |  | 3.39% | 3.39% | 16,558 |
| Notable | Finland |  | 3.38% | 3.38% | 16,474 |
| Primary | Cascadia | USA | — | 3.34% | 16,304 |
| Notable | Croatia |  | 3.31% | 3.31% | 16,159 |
| Notable | Netherlands |  | 3.28% | 3.28% | 15,996 |
| Notable | Slovenia |  | 3.24% | 3.24% | 15,814 |
| Notable | Serbia |  | 3.23% | 3.23% | 15,774 |
| Notable | Bulgaria |  | 3.10% | 3.10% | 15,109 |
| Notable | Argentina (without Patagonia) | Argentina | — | 3.08% | 15,029 |
| Notable | Latvia |  | 3.08% | 3.08% | 15,029 |
| Significant | Germany |  | 2.66% | 2.66% | 12,995 |
| Significant | Idelsk-Uralia | Russia | — | 2.31% | 11,287 |
| Significant | Siberia | Russia | — | 1.67% | 8,148 |
| Notable | Ukraine |  | 1.57% | 1.57% | 7,662 |
| Notable | Poland |  | 1.55% | 1.55% | 7,583 |
| Notable | Hungary |  | 1.42% | 1.42% | 6,916 |
| Notable | Sweden |  | 1.41% | 1.41% | 6,876 |
| Notable | Lithuania |  | 1.37% | 1.37% | 6,696 |
| Notable | Belarus |  | 1.34% | 1.34% | 6,531 |
| Notable | Estonia |  | 1.27% | 1.27% | 6,217 |
| Notable | Norway |  | 1.26% | 1.26% | 6,132 |
| Notable | South Africa |  | 1.26% | 1.26% | 6,143 |
| Notable | Romania |  | 1.23% | 1.23% | 5,982 |
| Primary | Midwest Republic | USA | — | 1.14% | 5,575 |
| Primary | Colorado | USA | — | 0.88% | 4,308 |
| Significant | Künnarantaiga | Russia | — | 0.81% | 3,973 |
| Significant | Donska-Kubania | Russia | — | 0.70% | 3,433 |
| Primary | Sonora | USA | — | 0.46% | 2,228 |
| Notable | Araucanía-Patagonia | Argentina | — | 0.35% | 1,681 |
| | *8 smaller Russia successors* | Russia | — | 0.25% | 1,206 |
| | *2 smaller USA successors* | USA | — | 0.12% | 571 |

#### Utstein

*from Japan: Iceland 0.55, Norway 2.41, Sweden 2.65, Finland 2.77, Denmark 3.07*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Brazil |  | 8.18% | 8.18% | 46,290 |
| Significant | France |  | 7.73% | 7.73% | 43,730 |
| Significant | Australia |  | 7.19% | 7.19% | 40,664 |
| Primary | Japan |  | 16.94% | 5.49% | 31,043 |
| Notable | Finland |  | 2.57% | 5.34% | 30,239 |
| Notable | Norway |  | 2.76% | 5.17% | 29,297 |
| Significant | Germany |  | 4.58% | 4.58% | 25,913 |
| Primary | CSA | USA | — | 4.17% | 23,614 |
| Founder (new row) | Denmark |  | — | 3.07% | 17,367 |
| Primary | Appalachia | USA | — | 2.83% | 16,044 |
| Primary | New England | USA | — | 2.82% | 15,934 |
| Notable | Belgium |  | 2.78% | 2.78% | 15,758 |
| Notable | Poland |  | 2.73% | 2.73% | 15,443 |
| Notable | Ukraine |  | 2.71% | 2.71% | 15,325 |
| Notable | Serbia |  | 2.67% | 2.67% | 15,091 |
| Founder (new row) | Sweden |  | — | 2.65% | 14,983 |
| Primary | Cascadia | USA | — | 2.59% | 14,672 |
| Notable | Bulgaria |  | 2.57% | 2.57% | 14,542 |
| Notable | Romania |  | 2.52% | 2.52% | 14,246 |
| Notable | Czech Republic |  | 2.51% | 2.51% | 14,180 |
| Notable | Latvia |  | 2.51% | 2.51% | 14,222 |
| Significant | UK |  | 1.74% | 1.74% | 9,846 |
| Notable | Netherlands |  | 1.42% | 1.42% | 8,013 |
| Notable | Hungary |  | 1.41% | 1.41% | 7,970 |
| Notable | Belarus |  | 1.40% | 1.40% | 7,948 |
| Notable | Croatia |  | 1.35% | 1.35% | 7,650 |
| Notable | Lithuania |  | 1.35% | 1.35% | 7,628 |
| Notable | Slovakia |  | 1.26% | 1.26% | 7,102 |
| Notable | Estonia |  | 1.21% | 1.21% | 6,868 |
| Notable | South Africa |  | 1.16% | 1.16% | 6,554 |
| Notable | Slovenia |  | 1.14% | 1.14% | 6,434 |
| Notable | Argentina (without Patagonia) | Argentina | — | 1.07% | 6,070 |
| Primary | Midwest Republic | USA | — | 0.89% | 5,016 |
| Primary | Colorado | USA | — | 0.68% | 3,877 |
| Founder (new row) | Iceland |  | — | 0.55% | 3,136 |
| Primary | Sonora | USA | — | 0.35% | 2,005 |
| Notable | Araucanía-Patagonia | Argentina | — | 0.12% | 679 |
| | *2 smaller USA successors* | USA | — | 0.09% | 514 |

#### Cape Adare

*Sinian draw 0.6333; fill to: CSA, Cascadia, Australia, Japan, Indonesia, South Korea, UK*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Australia |  | 10.76% | 12.48% | 94,588 |
| Significant | Japan |  | 10.49% | 12.17% | 92,274 |
| Primary | Sinian Federation | China | 19.85% | 11.51% | 87,249 |
| Significant | Indonesia |  | 9.28% | 10.76% | 81,582 |
| Primary | CSA | USA | — | 7.46% | 56,581 |
| Significant | South Korea |  | 5.29% | 6.14% | 46,552 |
| Significant | UK |  | 5.03% | 5.83% | 44,238 |
| Primary | Cascadia | USA + Canada | — | 5.68% | 43,065 |
| Primary | Appalachia | USA | — | 4.37% | 33,146 |
| Primary | New England | USA | — | 4.34% | 32,918 |
| Notable | Chile |  | 3.74% | 3.74% | 28,375 |
| Notable | New Zealand |  | 3.19% | 3.19% | 24,155 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 2.38% | 18,034 |
| Notable | Philippines |  | 2.08% | 2.08% | 15,745 |
| Significant | Quebec | Canada | — | 1.64% | 12,455 |
| Significant | Prairie Federation | Canada | — | 1.56% | 11,849 |
| Notable | Malaysia |  | 1.52% | 1.52% | 11,526 |
| Primary | Midwest Republic | USA | — | 1.37% | 10,364 |
| Primary | Colorado | USA | — | 1.06% | 8,010 |
| Primary | Sonora | USA | — | 0.55% | 4,142 |
| | *1 smaller USA successor* | USA | — | 0.09% | 687 |
| | *1 smaller USA + Canada successor* | USA + Canada | — | 0.08% | 572 |

#### Concordia

*Sinian draw 0.5996; fill to: Japan, South Korea, Australia, Indonesia*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Primary | Japan |  | 9.32% | 10.27% | 53,099 |
| Primary | South Korea |  | 9.31% | 10.26% | 52,995 |
| Primary | Australia |  | 7.82% | 8.61% | 44,523 |
| Primary | Indonesia |  | 7.72% | 8.50% | 43,934 |
| Significant | Vietnam |  | 4.23% | 4.23% | 21,846 |
| Primary | Sinian Federation | China | 7.70% | 4.23% | 21,844 |
| Primary | Russia (core state) | Russia | — | 3.85% | 19,899 |
| Significant | Belarus |  | 3.77% | 3.77% | 19,477 |
| Significant | New Zealand |  | 3.76% | 3.76% | 19,461 |
| Significant | Philippines |  | 2.62% | 2.62% | 13,518 |
| Primary | Idelsk-Uralia | Russia | — | 2.15% | 11,137 |
| Significant | Malaysia |  | 1.95% | 1.95% | 10,079 |
| Notable | Serbia |  | 1.59% | 1.59% | 8,227 |
| Significant | Thailand |  | 1.58% | 1.58% | 8,187 |
| Primary | Siberia | Russia | — | 1.55% | 8,040 |
| Notable | Estonia |  | 1.55% | 1.55% | 8,022 |
| Notable | Belgium |  | 1.54% | 1.54% | 7,956 |
| Notable | France |  | 1.51% | 1.51% | 7,820 |
| Notable | Spain |  | 1.47% | 1.47% | 7,591 |
| Notable | Croatia |  | 1.44% | 1.44% | 7,440 |
| Notable | Hungary |  | 1.43% | 1.43% | 7,418 |
| Notable | Finland |  | 1.41% | 1.41% | 7,280 |
| Notable | Czech Republic |  | 1.38% | 1.38% | 7,143 |
| Notable | Norway |  | 1.38% | 1.38% | 7,120 |
| Notable | UK |  | 1.32% | 1.32% | 6,822 |
| Notable | Poland |  | 1.32% | 1.32% | 6,812 |
| Significant | CSA | USA | — | 1.28% | 6,626 |
| Notable | México | Mexico | — | 1.03% | 5,303 |
| Significant | Cascadia | USA + Mexico + Canada | — | 0.94% | 4,854 |
| Significant | Appalachia | USA | — | 0.87% | 4,502 |
| Significant | New England | USA | — | 0.86% | 4,471 |
| Notable | Lithuania |  | 0.84% | 0.84% | 4,345 |
| Notable | Latvia |  | 0.81% | 0.81% | 4,176 |
| Primary | Künnarantaiga | Russia | — | 0.76% | 3,920 |
| Notable | Italy |  | 0.75% | 0.75% | 3,856 |
| Notable | Sweden |  | 0.75% | 0.75% | 3,879 |
| Notable | Bulgaria |  | 0.72% | 0.72% | 3,719 |
| Notable | Ukraine |  | 0.69% | 0.69% | 3,581 |
| Notable | Romania |  | 0.69% | 0.69% | 3,559 |
| Notable | Slovakia |  | 0.66% | 0.66% | 3,408 |
| Primary | Donska-Kubania | Russia | — | 0.66% | 3,387 |
| Notable | Netherlands |  | 0.59% | 0.59% | 3,042 |
| Notable | Germany |  | 0.58% | 0.58% | 2,977 |
| Notable | Slovenia |  | 0.28% | 0.28% | 1,459 |
| Significant | Midwest Republic | USA | — | 0.27% | 1,408 |
| Notable | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 0.22% | 1,162 |
| Significant | Colorado | USA | — | 0.21% | 1,088 |
| Significant | Sonora | USA + Mexico | — | 0.20% | 1,022 |
| Notable | Quebec | Canada | — | 0.15% | 802 |
| Notable | Prairie Federation | Canada | — | 0.15% | 763 |
| Notable | Yucatán | Mexico | — | 0.11% | 592 |
| | *8 smaller Russia successors* | Russia | — | 0.23% | 1,189 |
| | *1 smaller USA successor* | USA | — | 0.02% | 93 |
| | *1 smaller USA + Canada successor* | USA + Canada | — | 0.01% | 64 |

#### Denison

*Sinian draw 0.6464; fill to: CSA, Appalachia, New England, Cascadia, South Korea, Indonesia, Japan, Australia*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | South Korea |  | 12.31% | 14.21% | 64,914 |
| Primary | Sinian Federation | China | 22.29% | 13.19% | 60,263 |
| Significant | Indonesia |  | 10.77% | 12.43% | 56,807 |
| Primary | CSA | USA | — | 8.74% | 39,922 |
| Significant | Japan |  | 7.41% | 8.55% | 39,050 |
| Significant | Australia |  | 5.87% | 6.78% | 30,944 |
| Primary | Appalachia | USA | — | 5.94% | 27,123 |
| Primary | New England | USA | — | 5.90% | 26,937 |
| Primary | Cascadia | USA | — | 5.43% | 24,804 |
| Notable | New Zealand |  | 3.92% | 3.92% | 17,910 |
| Notable | Vietnam |  | 3.72% | 3.72% | 16,974 |
| Notable | Philippines |  | 3.64% | 3.64% | 16,643 |
| Notable | Malaysia |  | 2.42% | 2.42% | 11,034 |
| Primary | Midwest Republic | USA | — | 1.61% | 7,346 |
| Notable | Thailand |  | 1.45% | 1.45% | 6,631 |
| Primary | Colorado | USA | — | 1.24% | 5,678 |
| Primary | Sonora | USA | — | 0.64% | 2,936 |
| Primary | Hawaii | USA | — | 0.11% | 487 |
| | *1 smaller USA successor* | USA | — | 0.06% | 265 |

#### Dumont d'Urville

*Sinian draw 0.6236; fill to: CSA, France, Japan, Australia, Indonesia*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | France |  | 11.80% | 14.47% | 29,115 |
| Significant | Japan |  | 11.72% | 14.38% | 28,931 |
| Primary | Sinian Federation | China | 24.31% | 13.88% | 27,934 |
| Significant | Australia |  | 11.08% | 13.59% | 27,337 |
| Primary | CSA | USA | — | 7.14% | 14,364 |
| Significant | Indonesia |  | 5.59% | 6.86% | 13,797 |
| Notable | New Zealand |  | 4.16% | 4.16% | 8,361 |
| Notable | Vietnam |  | 4.04% | 4.04% | 8,128 |
| Primary | Appalachia | USA | — | 3.95% | 7,956 |
| Primary | New England | USA | — | 3.93% | 7,901 |
| Primary | Cascadia | USA | — | 3.62% | 7,275 |
| Notable | Philippines |  | 3.40% | 3.40% | 6,839 |
| Notable | Malaysia |  | 2.16% | 2.16% | 4,339 |
| Significant | South Korea |  | 1.48% | 1.48% | 2,980 |
| Primary | Midwest Republic | USA | — | 1.24% | 2,487 |
| Primary | Colorado | USA | — | 0.96% | 1,923 |
| Primary | Sonora | USA | — | 0.49% | 994 |
| Notable | Thailand |  | 0.14% | 0.14% | 278 |
| | *2 smaller USA successors* | USA | — | 0.13% | 255 |

#### Fort McMurdo

*Sinian draw 0.5591; fill to: CSA, Germany, France, Japan, Italy*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Germany |  | 10.49% | 12.94% | 28,734 |
| Significant | France |  | 9.73% | 12.00% | 26,648 |
| Significant | Japan |  | 9.08% | 11.20% | 24,895 |
| Primary | Sinian Federation | China | 19.34% | 9.90% | 21,998 |
| Primary | CSA | USA | — | 7.73% | 17,180 |
| Significant | Italy |  | 4.90% | 6.04% | 13,423 |
| Primary | Cascadia | USA + Canada | — | 4.38% | 9,728 |
| Significant | UK |  | 4.27% | 4.27% | 9,481 |
| Primary | Appalachia | USA | — | 4.26% | 9,465 |
| Primary | New England | USA | — | 4.23% | 9,400 |
| Notable | Chile |  | 3.54% | 3.54% | 7,869 |
| Notable | Malaysia |  | 3.31% | 3.31% | 7,355 |
| Notable | New Zealand |  | 3.20% | 3.20% | 7,118 |
| Notable | Australia |  | 1.92% | 1.92% | 4,276 |
| Notable | Indonesia |  | 1.82% | 1.82% | 4,040 |
| Notable | South Korea |  | 1.64% | 1.64% | 3,637 |
| Notable | Philippines |  | 1.59% | 1.59% | 3,525 |
| Primary | Midwest Republic | USA | — | 1.33% | 2,960 |
| Notable | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 1.28% | 2,834 |
| Primary | Colorado | USA | — | 1.03% | 2,287 |
| Notable | Quebec | Canada | — | 0.88% | 1,958 |
| Notable | Prairie Federation | Canada | — | 0.84% | 1,862 |
| Primary | Sonora | USA | — | 0.53% | 1,183 |
| | *1 smaller USA successor* | USA | — | 0.09% | 196 |
| | *1 smaller USA + Canada successor* | USA + Canada | — | 0.06% | 138 |

#### Janbogo

*Sinian draw 0.5550; fill to: CSA, South Korea, Australia, Italy, Indonesia, Germany*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | South Korea |  | 10.23% | 12.38% | 81,553 |
| Significant | Australia |  | 9.99% | 12.09% | 79,664 |
| Significant | Italy |  | 9.14% | 11.06% | 72,842 |
| Significant | Indonesia |  | 8.88% | 10.75% | 70,790 |
| Primary | Sinian Federation | China | 20.63% | 10.48% | 69,064 |
| Primary | CSA | USA | — | 6.44% | 42,402 |
| Significant | Germany |  | 4.64% | 5.62% | 37,020 |
| Significant | Japan |  | 4.41% | 4.41% | 29,022 |
| Primary | Cascadia | USA + Canada | — | 3.85% | 25,347 |
| Primary | Appalachia | USA | — | 3.61% | 23,798 |
| Primary | New England | USA | — | 3.59% | 23,635 |
| Notable | Chile |  | 3.22% | 3.22% | 21,178 |
| Notable | Malaysia |  | 3.13% | 3.13% | 20,638 |
| Notable | Philippines |  | 1.74% | 1.74% | 11,493 |
| Notable | New Zealand |  | 1.66% | 1.66% | 10,953 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 1.44% | 9,477 |
| Primary | Midwest Republic | USA | — | 1.13% | 7,441 |
| Significant | Quebec | Canada | — | 0.99% | 6,545 |
| Significant | Prairie Federation | Canada | — | 0.95% | 6,226 |
| Primary | Colorado | USA | — | 0.87% | 5,751 |
| Primary | Sonora | USA | — | 0.45% | 2,974 |
| | *1 smaller USA successor* | USA | — | 0.07% | 494 |
| | *1 smaller USA + Canada successor* | USA + Canada | — | 0.06% | 373 |

#### Scott

*Sinian draw 0.6337; fill to: CSA, Cascadia, Japan, UK, Australia, South Korea, Indonesia*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Japan |  | 10.81% | 12.46% | 23,646 |
| Significant | UK |  | 10.79% | 12.43% | 23,611 |
| Primary | Sinian Federation | China | 19.48% | 11.30% | 21,461 |
| Significant | Australia |  | 9.43% | 10.87% | 20,631 |
| Primary | CSA | USA | — | 7.54% | 14,306 |
| Significant | South Korea |  | 6.36% | 7.33% | 13,907 |
| Significant | Indonesia |  | 4.98% | 5.74% | 10,893 |
| Primary | Cascadia | USA + Canada | — | 5.48% | 10,398 |
| Primary | Appalachia | USA | — | 4.44% | 8,435 |
| Primary | New England | USA | — | 4.41% | 8,377 |
| Notable | Chile |  | 3.69% | 3.69% | 6,996 |
| Notable | New Zealand |  | 3.52% | 3.52% | 6,687 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 1.83% | 3,465 |
| Notable | Malaysia |  | 1.74% | 1.74% | 3,303 |
| Notable | Philippines |  | 1.58% | 1.58% | 2,994 |
| Primary | Midwest Republic | USA | — | 1.39% | 2,637 |
| Significant | Quebec | Canada | — | 1.26% | 2,393 |
| Significant | Prairie Federation | Canada | — | 1.20% | 2,276 |
| Primary | Colorado | USA | — | 1.07% | 2,038 |
| Primary | Sonora | USA | — | 0.56% | 1,054 |
| | *1 smaller USA successor* | USA | — | 0.09% | 175 |
| | *1 smaller USA + Canada successor* | USA + Canada | — | 0.07% | 133 |

#### Zukelli

*Sinian draw 0.5894; fill to: CSA, Cascadia, South Korea, Australia, Italy, Indonesia, Japan*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | South Korea |  | 11.10% | 13.51% | 86,449 |
| Primary | Sinian Federation | China | 22.63% | 12.21% | 78,140 |
| Significant | Australia |  | 9.55% | 11.62% | 74,392 |
| Significant | Italy |  | 6.24% | 7.60% | 48,556 |
| Significant | Indonesia |  | 5.89% | 7.17% | 45,864 |
| Primary | CSA | USA | — | 6.85% | 43,839 |
| Primary | Cascadia | USA + Canada | — | 5.92% | 37,890 |
| Significant | Japan |  | 4.69% | 5.71% | 36,500 |
| Primary | Appalachia | USA | — | 3.82% | 24,470 |
| Primary | New England | USA | — | 3.80% | 24,302 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 3.62% | 23,140 |
| Notable | Malaysia |  | 3.44% | 3.44% | 22,014 |
| Notable | New Zealand |  | 3.37% | 3.37% | 21,574 |
| Significant | Quebec | Canada | — | 2.50% | 15,981 |
| Significant | Prairie Federation | Canada | — | 2.38% | 15,203 |
| Notable | Philippines |  | 1.89% | 1.89% | 12,095 |
| Notable | Chile |  | 1.82% | 1.82% | 11,655 |
| Primary | Midwest Republic | USA | — | 1.20% | 7,651 |
| Primary | Colorado | USA | — | 0.92% | 5,913 |
| Primary | Sonora | USA | — | 0.48% | 3,058 |
| | *1 smaller USA + Canada successor* | USA + Canada | — | 0.08% | 530 |
| | *1 smaller USA successor* | USA | — | 0.08% | 507 |

#### Dome Fuji

*Sinian draw 0.5526; fill to: Indonesia, Australia, France, Germany, South Korea*

| Tier today | Row | From | Before | After |
|---|---|---|--:|--:|
| Significant | Indonesia |  | 5.51% | 6.60% |
| Significant | Australia |  | 5.16% | 6.18% |
| Significant | France |  | 5.00% | 5.99% |
| Significant | Germany |  | 4.83% | 5.79% |
| Significant | South Korea |  | 4.78% | 5.73% |
| Primary | Sinian Federation | China | 10.13% | 5.13% |
| Primary | CSA | USA | — | 3.24% |
| Significant | Brazil |  | 3.17% | 3.17% |
| Significant | Japan |  | 2.84% | 2.84% |
| Significant | UK |  | 2.49% | 2.49% |
| Primary | Cascadia | USA + Mexico + Canada | — | 2.34% |
| Primary | Appalachia | USA | — | 2.20% |
| Primary | New England | USA | — | 2.18% |
| Notable | Malaysia |  | 1.91% | 1.91% |
| Notable | Netherlands |  | 1.90% | 1.90% |
| Notable | Spain |  | 1.89% | 1.89% |
| Notable | Slovenia |  | 1.87% | 1.87% |
| Notable | Belarus |  | 1.83% | 1.83% |
| Notable | Croatia |  | 1.82% | 1.82% |
| Notable | Romania |  | 1.82% | 1.82% |
| Notable | Hungary |  | 1.81% | 1.81% |
| Notable | Czech Republic |  | 1.74% | 1.74% |
| Notable | Latvia |  | 1.73% | 1.73% |
| Notable | Serbia |  | 1.72% | 1.72% |
| Notable | Philippines |  | 1.71% | 1.71% |
| Notable | Estonia |  | 1.69% | 1.69% |
| Notable | Norway |  | 1.67% | 1.67% |
| Notable | México | Mexico | — | 1.51% |
| Notable | Chile |  | 0.99% | 0.99% |
| Notable | Finland |  | 0.98% | 0.98% |
| Notable | Slovakia |  | 0.96% | 0.96% |
| Notable | Bulgaria |  | 0.95% | 0.95% |
| Notable | Sweden |  | 0.94% | 0.94% |
| Notable | Vietnam |  | 0.94% | 0.94% |
| Significant | Russia (core state) | Russia | — | 0.93% |
| Notable | Ukraine |  | 0.92% | 0.92% |
| Notable | New Zealand |  | 0.85% | 0.85% |
| Notable | Thailand |  | 0.84% | 0.84% |
| Notable | Belgium |  | 0.84% | 0.84% |
| Notable | South Africa |  | 0.80% | 0.80% |
| Notable | Italy |  | 0.78% | 0.78% |
| Notable | Uruguay |  | 0.77% | 0.77% |
| Notable | Poland |  | 0.77% | 0.77% |
| Notable | Lithuania |  | 0.76% | 0.76% |
| Notable | Argentina (without Patagonia) | Argentina | — | 0.76% |
| Primary | Midwest Republic | USA | — | 0.69% |
| Notable | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 0.63% |
| Primary | Colorado | USA | — | 0.53% |
| Significant | Idelsk-Uralia | Russia | — | 0.52% |
| Notable | Quebec | Canada | — | 0.44% |
| Notable | Prairie Federation | Canada | — | 0.42% |
| Primary | Sonora | USA + Mexico | — | 0.41% |
| Significant | Siberia | Russia | — | 0.38% |
| Significant | Künnarantaiga | Russia | — | 0.18% |
| Notable | Yucatán | Mexico | — | 0.17% |
| Significant | Donska-Kubania | Russia | — | 0.16% |
| | *1 smaller Argentina successor* | Argentina | — | 0.08% |
| | *1 smaller USA successor* | USA | — | 0.05% |
| | *1 smaller USA + Canada successor* | USA + Canada | — | 0.03% |
| | *8 smaller Russia successors* | Russia | — | 0.06% |

#### Mawson

*Sinian draw 0.5642; fill to: UK, Australia, Indonesia, Japan, France, South Korea*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | UK |  | 8.99% | 10.72% | 77,396 |
| Significant | Australia |  | 8.29% | 9.88% | 71,379 |
| Significant | Indonesia |  | 7.89% | 9.41% | 67,935 |
| Significant | Japan |  | 7.48% | 8.92% | 64,346 |
| Primary | Sinian Federation | China | 17.02% | 8.79% | 63,477 |
| Significant | France |  | 5.29% | 6.31% | 45,515 |
| Significant | South Korea |  | 4.87% | 5.81% | 41,925 |
| Notable | Estonia |  | 3.17% | 3.17% | 22,899 |
| Notable | South Africa |  | 3.09% | 3.09% | 22,341 |
| Notable | Norway |  | 3.05% | 3.05% | 21,985 |
| Notable | Vietnam |  | 2.99% | 2.99% | 21,548 |
| Notable | Thailand |  | 2.97% | 2.97% | 21,442 |
| Notable | Belarus |  | 2.93% | 2.93% | 21,172 |
| Notable | Netherlands |  | 2.92% | 2.92% | 21,054 |
| Notable | Slovenia |  | 2.71% | 2.71% | 19,549 |
| Notable | Bulgaria |  | 2.68% | 2.68% | 19,356 |
| Significant | Germany |  | 1.86% | 1.86% | 13,436 |
| Notable | Czech Republic |  | 1.57% | 1.57% | 11,361 |
| Notable | Slovakia |  | 1.55% | 1.55% | 11,169 |
| Notable | Lithuania |  | 1.34% | 1.34% | 9,663 |
| Notable | Hungary |  | 1.32% | 1.32% | 9,546 |
| Notable | Romania |  | 1.28% | 1.28% | 9,276 |
| Notable | Poland |  | 1.27% | 1.27% | 9,170 |
| Notable | Croatia |  | 1.21% | 1.21% | 8,733 |
| Notable | Latvia |  | 1.16% | 1.16% | 8,377 |
| Notable | Ukraine |  | 1.08% | 1.08% | 7,819 |

#### Temirötkel

*Sinian draw 0.5829; fill to: Indonesia, Australia, Germany, UK, South Korea, France*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Indonesia |  | 8.59% | 10.21% | 9,532 |
| Significant | Australia |  | 8.27% | 9.83% | 9,179 |
| Significant | Germany |  | 8.22% | 9.77% | 9,122 |
| Significant | UK |  | 7.97% | 9.47% | 8,849 |
| Primary | Sinian Federation | China | 17.39% | 9.28% | 8,666 |
| Significant | South Korea |  | 5.07% | 6.03% | 5,627 |
| Significant | France |  | 4.82% | 5.73% | 5,354 |
| Notable | Serbia |  | 3.22% | 3.22% | 3,010 |
| Notable | Netherlands |  | 3.14% | 3.14% | 2,929 |
| Notable | Slovenia |  | 3.12% | 3.12% | 2,915 |
| Notable | Croatia |  | 3.11% | 3.11% | 2,900 |
| Notable | Romania |  | 2.81% | 2.81% | 2,621 |
| Notable | Lithuania |  | 2.81% | 2.81% | 2,625 |
| Notable | Norway |  | 2.80% | 2.80% | 2,615 |
| Notable | Belarus |  | 2.79% | 2.79% | 2,607 |
| Notable | Latvia |  | 2.76% | 2.76% | 2,576 |
| Significant | Japan |  | 2.71% | 2.71% | 2,527 |
| Notable | Czech Republic |  | 1.56% | 1.56% | 1,452 |
| Notable | Ukraine |  | 1.55% | 1.55% | 1,444 |
| Notable | Hungary |  | 1.54% | 1.54% | 1,438 |
| Notable | South Africa |  | 1.54% | 1.54% | 1,434 |
| Notable | Bulgaria |  | 1.24% | 1.24% | 1,159 |
| Notable | Poland |  | 1.23% | 1.23% | 1,144 |
| Notable | Estonia |  | 1.12% | 1.12% | 1,049 |
| Notable | Slovakia |  | 0.63% | 0.63% | 584 |

#### Ariun Nuur

*from Japan: Mongolia 4.19, Künnarantaiga 3.73*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Primary | Japan |  | 24.97% | 17.05% | 24,170 |
| Significant | Indonesia |  | 13.55% | 13.55% | 19,205 |
| Primary | CSA | USA | — | 8.20% | 11,622 |
| Primary | Cascadia | USA + Canada | — | 7.02% | 9,944 |
| Significant | Australia |  | 6.45% | 6.45% | 9,146 |
| Significant | South Korea |  | 6.10% | 6.10% | 8,645 |
| Primary | Appalachia | USA | — | 5.57% | 7,897 |
| Primary | New England | USA | — | 5.53% | 7,842 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 5.08% | 7,200 |
| Notable | Chile |  | 4.96% | 4.96% | 7,028 |
| Founder (new row) | Mongolia |  | — | 4.19% | 5,944 |
| Founder (new row) | Künnarantaiga |  | — | 3.73% | 5,290 |
| Significant | Quebec | Canada | — | 3.51% | 4,973 |
| Significant | Prairie Federation | Canada | — | 3.34% | 4,731 |
| Primary | Midwest Republic | USA | — | 1.74% | 2,469 |
| Notable | New Zealand |  | 1.71% | 1.71% | 2,422 |
| Primary | Colorado | USA | — | 1.35% | 1,908 |
| Primary | Sonora | USA | — | 0.70% | 987 |
| Primary | Alaska | USA + Canada | — | 0.12% | 168 |
| Primary | Hawaii | USA | — | 0.12% | 164 |

#### Casey

*Sinian draw 0.5501; fill to: CSA, South Korea, France, Australia, Japan, Indonesia*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | South Korea |  | 10.46% | 12.59% | 93,968 |
| Significant | France |  | 10.05% | 12.10% | 90,294 |
| Significant | Australia |  | 9.26% | 11.15% | 83,132 |
| Primary | Sinian Federation | China | 19.06% | 9.60% | 71,626 |
| Primary | CSA | USA | — | 7.64% | 57,029 |
| Significant | Japan |  | 5.33% | 6.42% | 47,874 |
| Significant | Indonesia |  | 4.92% | 5.92% | 44,201 |
| Primary | Appalachia | USA | — | 4.31% | 32,182 |
| Primary | New England | USA | — | 4.28% | 31,961 |
| Primary | Cascadia | USA | — | 3.94% | 29,430 |
| Notable | New Zealand |  | 3.36% | 3.36% | 25,040 |
| Notable | Philippines |  | 3.35% | 3.35% | 25,007 |
| Notable | Vietnam |  | 3.21% | 3.21% | 23,937 |
| Significant | Russia (core state) | Russia | — | 2.56% | 19,122 |
| Notable | Malaysia |  | 1.78% | 1.78% | 13,246 |
| Significant | Idelsk-Uralia | Russia | — | 1.44% | 10,701 |
| Primary | Midwest Republic | USA | — | 1.35% | 10,062 |
| Notable | Thailand |  | 1.13% | 1.13% | 8,403 |
| Primary | Colorado | USA | — | 1.04% | 7,777 |
| Significant | Siberia | Russia | — | 1.04% | 7,725 |
| Primary | Sonora | USA | — | 0.54% | 4,022 |
| Significant | Künnarantaiga | Russia | — | 0.51% | 3,767 |
| Significant | Donska-Kubania | Russia | — | 0.44% | 3,255 |
| | *2 smaller USA successors* | USA | — | 0.14% | 1,031 |
| | *8 smaller Russia successors* | Russia | — | 0.15% | 1,143 |

#### Davis

*Sinian draw 0.5719; fill to: Japan, Germany, UK, South Korea, Indonesia, Australia*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Japan |  | 9.36% | 11.27% | 64,904 |
| Significant | Germany |  | 9.15% | 11.02% | 63,448 |
| Significant | UK |  | 8.65% | 10.42% | 59,980 |
| Primary | Sinian Federation | China | 19.04% | 9.97% | 57,405 |
| Significant | South Korea |  | 7.14% | 8.60% | 49,510 |
| Significant | Indonesia |  | 5.14% | 6.19% | 35,642 |
| Significant | Australia |  | 4.93% | 5.94% | 34,186 |
| Notable | Thailand |  | 3.52% | 3.52% | 20,266 |
| Notable | Ukraine |  | 3.51% | 3.51% | 20,208 |
| Notable | Vietnam |  | 3.29% | 3.29% | 18,941 |
| Notable | Philippines |  | 3.25% | 3.25% | 18,712 |
| Notable | Malaysia |  | 3.13% | 3.13% | 18,021 |
| Notable | Romania |  | 2.97% | 2.97% | 17,100 |
| Notable | South Africa |  | 2.92% | 2.92% | 16,811 |
| Significant | Russia (core state) | Russia | — | 2.36% | 13,583 |
| Notable | New Zealand |  | 1.79% | 1.79% | 10,305 |
| Notable | Belarus |  | 1.63% | 1.63% | 9,385 |
| Notable | Bulgaria |  | 1.51% | 1.51% | 8,693 |
| Significant | Idelsk-Uralia | Russia | — | 1.32% | 7,602 |
| Notable | Lithuania |  | 1.25% | 1.25% | 7,197 |
| Notable | Estonia |  | 1.24% | 1.24% | 7,140 |
| Significant | Siberia | Russia | — | 0.95% | 5,488 |
| Notable | Latvia |  | 0.94% | 0.94% | 5,412 |
| Significant | Künnarantaiga | Russia | — | 0.46% | 2,676 |
| Significant | Donska-Kubania | Russia | — | 0.40% | 2,312 |
| | *8 smaller Russia successors* | Russia | — | 0.14% | 811 |

#### Mirny

*Sinian draw 0.5616; fill to: UK, South Korea, Indonesia, Japan, Australia, Philippines*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | UK |  | 12.35% | 15.16% | 102,768 |
| Significant | South Korea |  | 11.64% | 14.29% | 96,879 |
| Significant | Indonesia |  | 10.96% | 13.45% | 91,176 |
| Primary | Sinian Federation | China | 24.24% | 12.46% | 84,522 |
| Significant | Japan |  | 6.54% | 8.03% | 54,416 |
| Significant | Australia |  | 5.83% | 7.15% | 48,527 |
| Notable | Philippines |  | 4.50% | 5.52% | 37,475 |
| Notable | New Zealand |  | 4.48% | 4.48% | 30,374 |
| Notable | Thailand |  | 3.70% | 3.70% | 25,055 |
| Notable | Malaysia |  | 3.65% | 3.65% | 24,723 |
| Significant | Russia (core state) | Russia | — | 3.02% | 20,491 |
| Notable | Vietnam |  | 1.75% | 1.75% | 11,863 |
| Significant | Idelsk-Uralia | Russia | — | 1.69% | 11,468 |
| Notable | Belarus |  | 1.58% | 1.58% | 10,719 |
| Notable | South Africa |  | 1.56% | 1.56% | 10,557 |
| Significant | Siberia | Russia | — | 1.22% | 8,279 |
| Significant | Künnarantaiga | Russia | — | 0.59% | 4,037 |
| Significant | Donska-Kubania | Russia | — | 0.51% | 3,488 |
| | *8 smaller Russia successors* | Russia | — | 0.18% | 1,224 |

#### Relung Panen

*Sinian draw 0.6195; fill to: Russia (core state), Indonesia, Japan, South Korea, Australia, Thailand, Vietnam*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Indonesia |  | 12.23% | 14.08% | 67,214 |
| Significant | Japan |  | 11.98% | 13.79% | 65,841 |
| Significant | South Korea |  | 11.22% | 12.92% | 61,664 |
| Significant | Australia |  | 11.03% | 12.70% | 60,621 |
| Primary | Sinian Federation | China | 21.58% | 12.24% | 58,426 |
| Significant | Russia (core state) | Russia | — | 6.07% | 28,967 |
| Notable | Thailand |  | 5.15% | 5.93% | 28,304 |
| Notable | Vietnam |  | 4.76% | 5.48% | 26,161 |
| Notable | Malaysia |  | 3.30% | 3.30% | 15,751 |
| Notable | Philippines |  | 3.18% | 3.18% | 15,178 |
| Notable | New Zealand |  | 2.97% | 2.97% | 14,176 |
| Significant | Idelsk-Uralia | Russia | — | 2.95% | 14,078 |
| Significant | Siberia | Russia | — | 2.13% | 10,163 |
| Significant | Künnarantaiga | Russia | — | 1.04% | 4,956 |
| Significant | Donska-Kubania | Russia | — | 0.90% | 4,282 |
| Significant | Karelia | Russia | — | 0.12% | 583 |
| | *7 smaller Russia successors* | Russia | — | 0.19% | 920 |

#### Shirayuki

*Sinian draw 0.6427; fill to: Australia, South Korea, Germany*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Primary | Japan |  | 36.27% | 36.27% | 192,580 |
| Significant | Australia |  | 8.76% | 9.96% | 52,881 |
| Significant | South Korea |  | 7.89% | 8.97% | 47,629 |
| Significant | Germany |  | 4.93% | 5.61% | 29,760 |
| Significant | Sinian Federation | China | 7.18% | 4.23% | 22,434 |
| Significant | Russia (core state) | Russia | — | 3.60% | 19,123 |
| Notable | Romania |  | 3.54% | 3.54% | 18,796 |
| Notable | Vietnam |  | 3.16% | 3.16% | 16,779 |
| Notable | Ukraine |  | 3.11% | 3.11% | 16,512 |
| Notable | Belarus |  | 3.00% | 3.00% | 15,929 |
| Notable | Thailand |  | 2.99% | 2.99% | 15,875 |
| Notable | New Zealand |  | 2.97% | 2.97% | 15,770 |
| Significant | Idelsk-Uralia | Russia | — | 2.02% | 10,702 |
| Notable | Lithuania |  | 1.76% | 1.76% | 9,345 |
| Notable | South Africa |  | 1.66% | 1.66% | 8,813 |
| Notable | Bulgaria |  | 1.60% | 1.60% | 8,496 |
| Significant | Siberia | Russia | — | 1.46% | 7,726 |
| Notable | Latvia |  | 1.35% | 1.35% | 7,168 |
| Notable | Estonia |  | 1.22% | 1.22% | 6,478 |
| Significant | Künnarantaiga | Russia | — | 0.71% | 3,767 |
| Significant | Donska-Kubania | Russia | — | 0.61% | 3,255 |
| | *8 smaller Russia successors* | Russia | — | 0.22% | 1,143 |

#### Sinheung

*Sinian draw 0.5888; fill to: Japan, Germany*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Primary | South Korea |  | 34.62% | 34.62% | 165,973 |
| Significant | Germany |  | 8.64% | 11.00% | 52,745 |
| Significant | Japan |  | 7.78% | 9.91% | 47,494 |
| Significant | Sinian Federation | China | 9.74% | 5.25% | 25,174 |
| Significant | Indonesia |  | 4.41% | 4.41% | 21,142 |
| Notable | Thailand |  | 3.65% | 3.65% | 17,498 |
| Significant | Australia |  | 3.57% | 3.57% | 17,115 |
| Notable | Estonia |  | 3.52% | 3.52% | 16,875 |
| Notable | Hungary |  | 3.43% | 3.43% | 16,443 |
| Notable | Lithuania |  | 3.11% | 3.11% | 14,910 |
| Notable | Malaysia |  | 2.93% | 2.93% | 14,047 |
| Significant | Russia (core state) | Russia | — | 2.87% | 13,737 |
| Notable | Vietnam |  | 1.95% | 1.95% | 9,349 |
| Notable | Philippines |  | 1.77% | 1.77% | 8,486 |
| Significant | Idelsk-Uralia | Russia | — | 1.60% | 7,688 |
| Notable | Bulgaria |  | 1.45% | 1.45% | 6,951 |
| Notable | Latvia |  | 1.35% | 1.35% | 6,472 |
| Notable | South Africa |  | 1.23% | 1.23% | 5,896 |
| Significant | Siberia | Russia | — | 1.16% | 5,550 |
| Significant | Künnarantaiga | Russia | — | 0.56% | 2,706 |
| Significant | Donska-Kubania | Russia | — | 0.49% | 2,338 |
| | *8 smaller Russia successors* | Russia | — | 0.17% | 822 |

#### Zhongshan

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Primary | China |  | 35.83% | 35.83% | 208,145 |
| Significant | South Korea |  | 9.70% | 9.70% | 56,351 |
| Significant | Germany |  | 8.47% | 8.47% | 49,204 |
| Significant | Japan |  | 7.30% | 7.30% | 42,408 |
| Significant | Australia |  | 3.66% | 3.66% | 21,262 |
| Notable | Vietnam |  | 3.56% | 3.56% | 20,681 |
| Notable | Estonia |  | 3.55% | 3.55% | 20,622 |
| Notable | Thailand |  | 3.18% | 3.18% | 18,473 |
| Notable | Lithuania |  | 3.14% | 3.14% | 18,241 |
| Notable | Malaysia |  | 3.04% | 3.04% | 17,660 |
| Notable | Indonesia |  | 2.98% | 2.98% | 17,312 |
| Notable | Romania |  | 2.88% | 2.88% | 16,731 |
| Significant | Russia (core state) | Russia | — | 2.39% | 13,900 |
| Notable | Philippines |  | 1.72% | 1.72% | 9,992 |
| Notable | Latvia |  | 1.58% | 1.58% | 9,178 |
| Significant | Idelsk-Uralia | Russia | — | 1.34% | 7,779 |
| Notable | New Zealand |  | 1.28% | 1.28% | 7,435 |
| Notable | Bulgaria |  | 1.21% | 1.21% | 7,029 |
| Notable | South Africa |  | 1.20% | 1.20% | 6,972 |
| Significant | Siberia | Russia | — | 0.97% | 5,616 |
| Significant | Künnarantaiga | Russia | — | 0.47% | 2,738 |
| Significant | Donska-Kubania | Russia | — | 0.41% | 2,366 |
| | *8 smaller Russia successors* | Russia | — | 0.14% | 830 |

#### Contrapunto

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | France |  | 11.62% | 11.62% | 36,799 |
| Significant | UK |  | 11.30% | 11.30% | 35,789 |
| Significant | Germany |  | 10.72% | 10.72% | 33,955 |
| Significant | México | Mexico | — | 8.99% | 28,483 |
| Significant | Brazil |  | 6.69% | 6.69% | 21,187 |
| Primary | CSA | USA | — | 6.26% | 19,825 |
| Significant | Italy |  | 6.13% | 6.13% | 19,412 |
| Significant | South Korea |  | 5.79% | 5.79% | 18,336 |
| Primary | Cascadia | USA + Mexico | — | 4.39% | 13,918 |
| Primary | Appalachia | USA | — | 4.25% | 13,469 |
| Primary | New England | USA | — | 4.22% | 13,377 |
| Notable | Argentina (without Patagonia) | Argentina | — | 3.83% | 12,134 |
| Notable | Chile |  | 3.53% | 3.53% | 11,180 |
| Significant | Russia (core state) | Russia | — | 2.56% | 8,105 |
| Significant | Idelsk-Uralia | Russia | — | 1.43% | 4,536 |
| Primary | Midwest Republic | USA | — | 1.33% | 4,211 |
| Primary | Sonora | USA + Mexico | — | 1.31% | 4,152 |
| Significant | Siberia | Russia | — | 1.03% | 3,274 |
| Primary | Colorado | USA | — | 1.03% | 3,255 |
| Significant | Yucatán | Mexico | — | 1.00% | 3,180 |
| Notable | Uruguay |  | 0.91% | 0.91% | 2,882 |
| Significant | Künnarantaiga | Russia | — | 0.50% | 1,597 |
| Significant | Donska-Kubania | Russia | — | 0.44% | 1,380 |
| Notable | Araucanía-Patagonia | Argentina | — | 0.43% | 1,357 |
| | *2 smaller USA successors* | USA | — | 0.14% | 431 |
| | *8 smaller Russia successors* | Russia | — | 0.15% | 484 |

#### Esperanza

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Brazil |  | 18.92% | 18.92% | 183,087 |
| Significant | México | Mexico | — | 13.91% | 134,540 |
| Primary | CSA | USA | — | 10.51% | 101,716 |
| Significant | UK |  | 9.83% | 9.83% | 95,071 |
| Significant | Argentina (without Patagonia) | Argentina | — | 7.51% | 72,645 |
| Primary | Cascadia | USA + Mexico | — | 7.31% | 70,759 |
| Primary | Appalachia | USA | — | 7.14% | 69,107 |
| Primary | New England | USA | — | 7.09% | 68,633 |
| Notable | Uruguay |  | 6.60% | 6.60% | 63,843 |
| Notable | Chile |  | 2.49% | 2.49% | 24,110 |
| Primary | Midwest Republic | USA | — | 2.23% | 21,607 |
| Primary | Sonora | USA + Mexico | — | 2.10% | 20,299 |
| Primary | Colorado | USA | — | 1.73% | 16,700 |
| Significant | Yucatán | Mexico | — | 1.55% | 15,022 |
| Significant | Araucanía-Patagonia | Argentina | — | 0.84% | 8,124 |
| Primary | Hawaii | USA | — | 0.15% | 1,433 |
| | *1 smaller USA successor* | USA | — | 0.08% | 781 |

#### Marambio

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Spain |  | 14.19% | 14.19% | 40,209 |
| Significant | UK |  | 13.48% | 13.48% | 38,198 |
| Significant | México | Mexico | — | 11.24% | 31,861 |
| Primary | CSA | USA | — | 7.98% | 22,607 |
| Significant | Germany |  | 6.59% | 6.59% | 18,673 |
| Primary | Cascadia | USA + Mexico + Canada | — | 6.58% | 18,663 |
| Significant | Brazil |  | 6.50% | 6.50% | 18,435 |
| Primary | Appalachia | USA | — | 5.42% | 15,359 |
| Primary | New England | USA | — | 5.38% | 15,254 |
| Notable | Chile |  | 4.87% | 4.87% | 13,793 |
| Notable | Uruguay |  | 4.74% | 4.74% | 13,427 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 2.63% | 7,470 |
| Significant | Quebec | Canada | — | 1.82% | 5,159 |
| Significant | Prairie Federation | Canada | — | 1.73% | 4,908 |
| Primary | Midwest Republic | USA | — | 1.69% | 4,802 |
| Primary | Sonora | USA + Mexico | — | 1.65% | 4,681 |
| Primary | Colorado | USA | — | 1.31% | 3,712 |
| Significant | Yucatán | Mexico | — | 1.25% | 3,557 |
| Notable | Argentina (without Patagonia) | Argentina | — | 0.67% | 1,891 |
| Primary | Hawaii | USA | — | 0.11% | 318 |
| | *1 smaller USA + Canada successor* | USA + Canada | — | 0.09% | 256 |
| | *1 smaller Argentina successor* | Argentina | — | 0.07% | 211 |

#### Palmer City

*Sinian draw 0.6378; fill to: CSA, Cascadia, Brazil, France, Germany, México, UK*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Brazil |  | 9.68% | 9.75% | 16,179 |
| Significant | France |  | 9.54% | 9.61% | 15,946 |
| Significant | Germany |  | 9.51% | 9.58% | 15,895 |
| Primary | CSA | USA | — | 5.91% | 9,808 |
| Significant | UK |  | 5.54% | 5.58% | 9,264 |
| Primary | Cascadia | USA + Mexico + Canada | — | 4.72% | 7,834 |
| Significant | México | Mexico | — | 4.59% | 7,611 |
| Primary | Appalachia | USA | — | 3.99% | 6,613 |
| Primary | New England | USA | — | 3.96% | 6,568 |
| Notable | Uruguay |  | 3.70% | 3.70% | 6,141 |
| Notable | Argentina (without Patagonia) | Argentina | — | 2.74% | 4,552 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 2.08% | 3,444 |
| Significant | Quebec | Canada | — | 1.43% | 2,378 |
| Notable | Estonia |  | 1.39% | 1.39% | 2,312 |
| Significant | Prairie Federation | Canada | — | 1.36% | 2,262 |
| Notable | Czech Republic |  | 1.35% | 1.35% | 2,247 |
| Notable | Australia |  | 1.33% | 1.33% | 2,207 |
| Notable | Slovakia |  | 1.29% | 1.29% | 2,142 |
| Notable | Thailand |  | 1.26% | 1.26% | 2,089 |
| Primary | Midwest Republic | USA | — | 1.25% | 2,068 |
| Notable | Serbia |  | 1.16% | 1.16% | 1,931 |
| Notable | Belgium |  | 1.14% | 1.14% | 1,892 |
| Notable | South Korea |  | 1.09% | 1.09% | 1,813 |
| Notable | Italy |  | 1.06% | 1.06% | 1,761 |
| Notable | Norway |  | 1.01% | 1.01% | 1,669 |
| Notable | Croatia |  | 0.97% | 0.97% | 1,603 |
| Primary | Colorado | USA | — | 0.96% | 1,598 |
| Notable | South Africa |  | 0.96% | 0.96% | 1,590 |
| Primary | Sonora | USA + Mexico | — | 0.89% | 1,481 |
| Notable | Slovenia |  | 0.86% | 0.86% | 1,432 |
| Notable | Chile |  | 0.86% | 0.86% | 1,422 |
| Notable | Romania |  | 0.86% | 0.86% | 1,419 |
| Notable | Philippines |  | 0.82% | 0.82% | 1,353 |
| Notable | Netherlands |  | 0.76% | 0.76% | 1,261 |
| Notable | Japan |  | 0.73% | 0.73% | 1,209 |
| Notable | Poland |  | 0.70% | 0.70% | 1,169 |
| Notable | New Zealand |  | 0.67% | 0.67% | 1,117 |
| Notable | Bulgaria |  | 0.62% | 0.62% | 1,025 |
| Notable | Vietnam |  | 0.58% | 0.58% | 959 |
| Notable | Sinian Federation | China | 0.91% | 0.53% | 882 |
| Notable | Spain |  | 0.53% | 0.53% | 880 |
| Significant | Yucatán | Mexico | — | 0.51% | 843 |
| Notable | Russia (core state) | Russia | — | 0.50% | 835 |
| Notable | Latvia |  | 0.48% | 0.48% | 802 |
| Notable | Sweden |  | 0.46% | 0.46% | 762 |
| Notable | Belarus |  | 0.44% | 0.44% | 723 |
| Notable | Indonesia |  | 0.38% | 0.38% | 631 |
| Notable | Ukraine |  | 0.35% | 0.35% | 578 |
| Notable | Finland |  | 0.32% | 0.32% | 539 |
| Notable | Araucanía-Patagonia | Argentina | — | 0.31% | 509 |
| Notable | Idelsk-Uralia | Russia | — | 0.28% | 468 |
| Notable | Lithuania |  | 0.28% | 0.28% | 460 |
| Notable | Malaysia |  | 0.25% | 0.25% | 407 |
| Notable | Hungary |  | 0.23% | 0.23% | 381 |
| Notable | Siberia | Russia | — | 0.20% | 337 |
| | *10 smaller Russia successors* | Russia | — | 0.21% | 357 |
| | *1 smaller USA successor* | USA | — | 0.08% | 137 |
| | *1 smaller USA + Canada successor* | USA + Canada | — | 0.07% | 113 |

#### Pergamino

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Italy |  | 14.24% | 14.24% | 27,024 |
| Significant | Spain |  | 14.06% | 14.06% | 26,680 |
| Significant | UK |  | 13.72% | 13.72% | 26,024 |
| Primary | CSA | USA | — | 8.57% | 16,254 |
| Significant | France |  | 8.51% | 8.51% | 16,141 |
| Primary | Appalachia | USA | — | 5.82% | 11,043 |
| Primary | New England | USA | — | 5.78% | 10,968 |
| Primary | Cascadia | USA + Mexico | — | 5.44% | 10,324 |
| Significant | Germany |  | 5.03% | 5.03% | 9,544 |
| Notable | Chile |  | 4.76% | 4.76% | 9,027 |
| Notable | Argentina (without Patagonia) | Argentina | — | 4.53% | 8,594 |
| Notable | Brazil |  | 2.37% | 2.37% | 4,499 |
| Notable | México | Mexico | — | 2.11% | 4,008 |
| Primary | Midwest Republic | USA | — | 1.82% | 3,453 |
| Primary | Colorado | USA | — | 1.41% | 2,669 |
| Primary | Sonora | USA + Mexico | — | 0.91% | 1,727 |
| Notable | Araucanía-Patagonia | Argentina | — | 0.51% | 961 |
| Notable | Yucatán | Mexico | — | 0.24% | 448 |
| Primary | Hawaii | USA | — | 0.12% | 229 |
| | *1 smaller USA successor* | USA | — | 0.07% | 125 |

#### Puerto Abrigo

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | France |  | 16.71% | 16.71% | 77 |
| Significant | Germany |  | 14.83% | 14.83% | 68 |
| Significant | UK |  | 14.35% | 14.35% | 66 |
| Significant | Brazil |  | 9.65% | 9.65% | 44 |
| Primary | CSA | USA | — | 9.25% | 42 |
| Primary | Appalachia | USA | — | 6.29% | 29 |
| Primary | New England | USA | — | 6.24% | 28 |
| Primary | Cascadia | USA + Mexico | — | 5.95% | 27 |
| Notable | Chile |  | 5.74% | 5.74% | 26 |
| Significant | México | Mexico | — | 3.56% | 16 |
| Notable | Argentina (without Patagonia) | Argentina | — | 2.03% | 9 |
| Primary | Midwest Republic | USA | — | 1.97% | 9 |
| Primary | Colorado | USA | — | 1.52% | 7 |
| Primary | Sonora | USA + Mexico | — | 1.09% | 5 |
| Significant | Yucatán | Mexico | — | 0.40% | 2 |
| Notable | Araucanía-Patagonia | Argentina | — | 0.23% | 1 |
| Primary | Hawaii | USA | — | 0.13% | 1 |
| | *1 smaller USA successor* | USA | — | 0.07% | 0 |

#### Rothera

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Germany |  | 14.31% | 14.31% | 22,000 |
| Significant | Brazil |  | 14.00% | 14.00% | 21,526 |
| Primary | CSA | USA | — | 8.26% | 12,701 |
| Significant | France |  | 7.43% | 7.43% | 11,423 |
| Primary | Cascadia | USA + Canada + Mexico | — | 7.43% | 11,421 |
| Significant | UK |  | 7.12% | 7.12% | 10,948 |
| Significant | México | Mexico | — | 5.68% | 8,739 |
| Primary | Appalachia | USA | — | 5.61% | 8,630 |
| Primary | New England | USA | — | 5.57% | 8,570 |
| Notable | Chile |  | 5.23% | 5.23% | 8,044 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 5.23% | 8,033 |
| Significant | Quebec | Canada | — | 3.61% | 5,548 |
| Significant | Prairie Federation | Canada | — | 3.43% | 5,278 |
| Primary | Midwest Republic | USA | — | 1.75% | 2,698 |
| Notable | Argentina (without Patagonia) | Argentina | — | 1.72% | 2,643 |
| Primary | Colorado | USA | — | 1.36% | 2,085 |
| Primary | Sonora | USA + Mexico | — | 1.19% | 1,836 |
| Significant | Yucatán | Mexico | — | 0.63% | 976 |
| Notable | Araucanía-Patagonia | Argentina | — | 0.19% | 296 |
| Primary | Alaska | USA + Canada | — | 0.12% | 186 |
| Primary | Hawaii | USA | — | 0.12% | 179 |

#### Signy

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | France |  | 17.19% | 17.19% | 16,013 |
| Significant | UK |  | 16.96% | 16.96% | 15,795 |
| Primary | CSA | USA | — | 9.64% | 8,976 |
| Significant | Brazil |  | 8.04% | 8.04% | 7,488 |
| Significant | Germany |  | 7.81% | 7.81% | 7,270 |
| Primary | Appalachia | USA | — | 6.55% | 6,098 |
| Primary | New England | USA | — | 6.50% | 6,056 |
| Primary | Cascadia | USA | — | 5.99% | 5,577 |
| Notable | South Africa |  | 5.47% | 5.47% | 5,090 |
| Notable | Argentina (without Patagonia) | Argentina | — | 5.47% | 5,089 |
| Notable | Chile |  | 2.87% | 2.87% | 2,671 |
| Notable | Uruguay |  | 2.26% | 2.26% | 2,103 |
| Primary | Midwest Republic | USA | — | 2.05% | 1,907 |
| Primary | Colorado | USA | — | 1.58% | 1,474 |
| Primary | Sonora | USA | — | 0.82% | 762 |
| Notable | Araucanía-Patagonia | Argentina | — | 0.61% | 569 |
| Primary | Hawaii | USA | — | 0.14% | 126 |
| | *1 smaller USA successor* | USA | — | 0.07% | 69 |

*Every row, every census column: `10_city_tables.csv`.*
