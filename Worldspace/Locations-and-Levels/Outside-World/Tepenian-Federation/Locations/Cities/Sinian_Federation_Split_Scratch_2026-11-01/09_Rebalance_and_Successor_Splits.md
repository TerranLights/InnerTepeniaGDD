# Run 2: the rebalance with the developer's settings, plus the successor splits (2026-11-01, ~23:40 onward)

**Scratch, not canon, not a ruling. No official file was changed.** Figures come from `calc_rebalance_v2.py`
(read-only on the specs; it reuses run 1's functions and last night's `calc_part2.py`); every row of every city, in
every census column, is in `09_city_tables.csv`; the script's whole output is the appendix.

## What was asked

The developer, ~23:35, after reading run 1 (`08_Sinian_Decline_Rebalance.md`):

> *"in that case, go with the proportional fill and use a 4.5% cutoff, use a randomly-generated value between
> 55-65% (instead of 55-60), and also calculate for populations from North America (now many countries),
> what-was-current-day-Russia (also now many countries), and Argentina, and see what the resulting numbers look
> like"*

## What was done

**Step 1, the Sinian Federation (the 20 cities with Chinese presence except Zhongshan and Kunlun).** As in run 1,
with the developer's three changes: China's row becomes the Sinian Federation's share (91.56%, Option B) times a
random draw **between 0.55 and 0.65** per city (same seed and order as run 1; draws 0.5501–0.6464, so the Sinian
factor runs 0.504–0.592); the gap goes **in proportion to size** to the city's nations at **4.5% or more** outside
its top tier (Concordia: to its other top-tier nations, as in run 1).

**Step 2, the successor splits (every city except Kunlun).** Read as dividing each city's existing USA, Canada,
Mexico, Russia and Argentina rows among their successor states; nobody else's numbers change. Each successor gets
its share of the old country's effective pool (Option B, economic size; for Russia, the October 29 research's
city-independent split, primary variant):

- **USA:** CSA 28.91% · Appalachia 19.64% · New England 19.51% · Cascadia 17.96% · Midwest Republic 6.14% ·
  Colorado 4.75% · Sonora 2.45% · Hawaii 0.41% · Alaska 0.22%
- **Canada:** Demilitarized Zone 36.54% · Quebec 25.23% · Prairie Federation 24.01% · Cascadia 13.82% · Alaska 0.40%
- **Mexico:** México 79.71% · Yucatán 8.90% · Sonora 6.91% · Cascadia 4.48%
- **Argentina:** Argentina (without Patagonia) 89.94% · Araucanía-Patagonia 10.06%
- **Russia:** Russia (core state) 41.83% · Idelsk-Uralia 23.41% · Siberia 16.90% · Künnarantaiga 8.24% ·
  Donska-Kubania 7.12% · Karelia 0.97% · Dagestan 0.61% · Chechnya 0.29% · Kabardino-Balkaria 0.20% · North
  Ossetia-Alania 0.19% · Karachay-Cherkessia 0.10% · Tuva 0.08% · Ingushetia 0.06%

Successors drawn from more than one country (Cascadia, Sonora, Alaska) are added together within a city.

**Choices made to get a number, each still the developer's to change:**
- **Kunlun is left exactly as it is.** Its rows are chosen by space-program heritage, not population, and its table
  is rebuilt on 2026-11-02 under Option A.
- **Zhongshan's China row is untouched** (exempt); its Russia row is split like everyone else's, since the
  exemption is about China.
- **Canada's Demilitarized Zone keeps its own row,** labeled "not a nation", because where its exiles count is
  still decision 2.
- **Canada's Neutral Scientific Territory and Greenland pieces** (0.08% of Canada's pool together) are left out,
  as recommended; Canada's other successors are scaled up to cover them.
- **Every successor reaches every city in proportion to its pool** (no time-zone window). This is the "pool split"
  side of the open Russia ruling; see the decisions below.
- **Order:** the decline first, then the splits. A check with the order reversed is in the appendix.

**Totals:** every one of the 37 cities keeps its exact total in every census column (the script checks this).

## What the numbers look like

### City by city (after both steps)

| City | China → Sinian Fed. | Leader before | Leader after | Lead after (1st ÷ 2nd) | Top five after (%) |
|---|---|---|---|--:|---|
| Amundsen Station | 19.31 → 11.33 | USA 22.80 | UK 12.35 | 1.05 | UK 12.3, Germany 11.8, Sinian Federation 11.3, Japan 11.2, South Korea 6.7 |
| Byrd | 2.95 → 1.67 | USA 13.57 | Australia 7.07 | 1.04 | Australia 7.1, Japan 6.8, Demilitarized Zone 4.2, Cascadia 4.1, CSA 3.9 |
| Belgrano | — | USA 28.57 | Brazil 13.73 | 1.02 | Brazil 13.7, Germany 13.4, CSA 8.3, Appalachia 5.6, New England 5.6 |
| Halley | — | USA 23.53 | Brazil 11.69 | 1.11 | Brazil 11.7, UK 10.6, France 7.3, CSA 6.8, Cascadia 5.7 |
| Lazar | — | USA 19.05 | UK 10.08 | 1.06 | UK 10.1, Germany 9.5, Brazil 9.1, CSA 5.5, Appalachia 3.7 |
| Neumayer | — | USA 19.51 | France 10.03 | 1.07 | France 10.0, Germany 9.4, CSA 5.6, UK 5.2, Brazil 4.6 |
| Sanay | — | Germany 25.00 | Germany 25.00 | 2.16 | Germany 25.0, Brazil 11.6, UK 7.2, Estonia 4.6, Serbia 4.5 |
| Santa Luce | — | USA 17.02 | Brazil 8.93 | 1.14 | Brazil 8.9, UK 7.8, Magna Lombardia 6.4, CSA 4.9, Russia (core state) 3.8 |
| Troll | — | USA 18.60 | UK 8.44 | 1.01 | UK 8.4, Brazil 8.4, France 5.5, CSA 5.4, Russia (core state) 4.1 |
| Utstein | — | Japan 16.94 | Japan 16.94 | 2.07 | Japan 16.9, Brazil 8.2, France 7.7, Australia 7.2, Germany 4.6 |
| Cape Adare | 19.85 → 11.51 | USA 22.26 | Australia 12.65 | 1.03 | Australia 12.7, Japan 12.3, Sinian Federation 11.5, Indonesia 10.9, CSA 6.4 |
| Concordia | 7.70 → 4.23 | Japan 9.32 | Japan 10.07 | 1.00 | Japan 10.1, South Korea 10.1, Australia 8.4, Indonesia 8.3, Vietnam 4.2 |
| Denison | 22.29 → 13.19 | USA 26.19 | South Korea 15.39 | 1.14 | South Korea 15.4, Indonesia 13.5, Sinian Federation 13.2, Japan 9.3, CSA 7.6 |
| Dumont d'Urville | 24.31 → 13.88 | China 24.31 | France 14.86 | 1.01 | France 14.9, Japan 14.8, Australia 14.0, Sinian Federation 13.9, Indonesia 7.0 |
| Fort McMurdo | 19.34 → 9.90 | USA 21.69 | Germany 13.39 | 1.08 | Germany 13.4, France 12.4, Japan 11.6, Sinian Federation 9.9, CSA 6.3 |
| Janbogo | 20.63 → 10.48 | China 20.63 | South Korea 12.65 | 1.02 | South Korea 12.7, Australia 12.4, Italy 11.3, Indonesia 11.0, Sinian Federation 10.5 |
| Scott | 19.48 → 11.30 | USA 22.62 | Japan 12.68 | 1.00 | Japan 12.7, UK 12.7, Sinian Federation 11.3, Australia 11.1, South Korea 7.5 |
| Zukelli | 22.63 → 12.21 | China 22.63 | South Korea 13.54 | 1.11 | South Korea 13.5, Sinian Federation 12.2, Australia 11.7, Italy 7.6, Indonesia 7.2 |
| Dome Fuji | 10.13 → 5.13 | USA 11.20 | Indonesia 6.60 | 1.07 | Indonesia 6.6, Australia 6.2, France 6.0, Germany 5.8, South Korea 5.7 |
| Mawson | 17.02 → 8.79 | China 17.02 | UK 10.72 | 1.08 | UK 10.7, Australia 9.9, Indonesia 9.4, Japan 8.9, Sinian Federation 8.8 |
| Temirötkel | 17.39 → 9.28 | China 17.39 | Indonesia 10.21 | 1.04 | Indonesia 10.2, Australia 9.8, Germany 9.8, UK 9.5, Sinian Federation 9.3 |
| Ariun Nuur | — | USA 28.36 | Japan 24.97 | 1.84 | Japan 25.0, Indonesia 13.6, CSA 8.2, Cascadia 7.0, Australia 6.5 |
| Casey | 19.06 → 9.60 | USA 21.96 | South Korea 12.60 | 1.04 | South Korea 12.6, France 12.1, Australia 11.2, Sinian Federation 9.6, Japan 6.4 |
| Davis | 19.04 → 9.97 | China 19.04 | Japan 11.06 | 1.02 | Japan 11.1, Germany 10.8, UK 10.2, Sinian Federation 10.0, South Korea 8.4 |
| Mirny | 24.24 → 12.46 | China 24.24 | UK 14.81 | 1.06 | UK 14.8, South Korea 14.0, Indonesia 13.1, Sinian Federation 12.5, Japan 7.8 |
| Relung Panen | 21.58 → 12.24 | China 21.58 | Indonesia 13.89 | 1.02 | Indonesia 13.9, Japan 13.6, South Korea 12.7, Australia 12.5, Sinian Federation 12.2 |
| Shirayuki | 7.18 → 4.23 | Japan 36.27 | Japan 36.27 | 3.77 | Japan 36.3, Australia 9.6, South Korea 8.7, Germany 5.4, Sinian Federation 4.2 |
| Sinheung | 9.74 → 5.25 | South Korea 34.62 | South Korea 34.62 | 3.36 | South Korea 34.6, Germany 10.3, Japan 9.3, Sinian Federation 5.3, Indonesia 4.4 |
| Zhongshan | 35.83 → 35.83 | China 35.83 | China 35.83 | 3.69 | China 35.8, South Korea 9.7, Germany 8.5, Japan 7.3, Australia 3.7 |
| Contrapunto | — | USA 21.65 | France 11.62 | 1.03 | France 11.6, UK 11.3, Germany 10.7, México 9.0, Brazil 6.7 |
| Esperanza | — | USA 36.36 | Brazil 18.92 | 1.36 | Brazil 18.9, México 13.9, CSA 10.5, UK 9.8, Argentina (without Patagonia) 7.5 |
| Marambio | — | USA 27.59 | Spain 14.19 | 1.05 | Spain 14.2, UK 13.5, México 11.2, CSA 8.0, Germany 6.6 |
| Palmer City | 0.91 → 0.53 | USA 20.29 | Brazil 9.76 | 1.01 | Brazil 9.8, France 9.6, Germany 9.6, CSA 5.9, UK 5.6 |
| Pergamino | — | USA 29.63 | Italy 14.24 | 1.01 | Italy 14.2, Spain 14.1, UK 13.7, CSA 8.6, France 8.5 |
| Puerto Abrigo | — | USA 32.00 | France 16.71 | 1.13 | France 16.7, Germany 14.8, UK 14.3, Brazil 9.7, CSA 9.3 |
| Rothera | — | USA 28.57 | Germany 14.31 | 1.02 | Germany 14.3, Brazil 14.0, CSA 8.3, France 7.4, Cascadia 7.4 |
| Signy | — | USA 33.33 | France 17.19 | 1.01 | France 17.2, UK 17.0, CSA 9.6, Brazil 8.0, Germany 7.8 |

**Reading it (DERIVED from the table):**
- **In 30 of the 37 cities the leading nation is at most 1.14 times the next.** The seven exceptions are the three
  founding allocations (Zhongshan, Shirayuki, Sinheung, all intended), Sanay (Germany at 25%, untouched by this
  run), and three cities where the USA's split leaves one nation clearly ahead: **Ariun Nuur** (Japan 25.0%,
  1.84×), **Utstein** (Japan 16.9%, 2.07×) and **Esperanza** (Brazil 18.9%, 1.36×).
- **No city outside those seven has any nation above 17.2%** (Signy's France).
- **The Sinian Federation** ranges from 0.53% (Palmer City) to 13.88% (Dumont d'Urville) and is in the top five in
  16 of its 20 cities: a major community nearly everywhere it was, dominant nowhere.
- **The largest successor rows:** México 13.9% and the CSA 10.5% (both Esperanza); Cascadia 7.4% (Rothera); the
  Demilitarized Zone 5.2% (Rothera); Russia's core state 6.0% (Relung Panen). The smallest successors (Hawaii,
  Alaska, Tuva, Karelia and the five Caucasus republics) never add up to more than 0.37% of a city (Troll).

### Nationally (Census I humans, 15,612,333 in the specs; the census's 11,205 maritime-fleet humans have no nation)

| Rank | Nation or successor | Humans after | Share | Before |
|--:|---|--:|--:|---|
| 1 | Japan | 1,055,208 | 6.76% | 953,710 |
| 2 | South Korea | 1,009,340 | 6.47% | 892,502 |
| 3 | Sinian Federation | 992,151 | 6.35% | China 1,660,450 (incl. Zhongshan's 208,145, unchanged) |
| 4 | UK | 905,182 | 5.80% | 855,222 |
| 5 | Australia | 842,401 | 5.40% | 727,081 |
| 6 | Germany | 770,778 | 4.94% | 735,406 |
| 7 | CSA | 711,987 | 4.56% | part of the USA (2,462,596) |
| 8 | Indonesia | 709,614 | 4.55% | 606,976 |
| 9 | Brazil | 705,096 | 4.52% | 704,963 |
| 10 | France | 526,283 | 3.37% | 490,468 |
| 11 | Cascadia | 503,535 | 3.23% | parts of the USA, Canada, Mexico |
| 12 | Appalachia | 483,737 | 3.10% | part of the USA |
| 13 | New England | 480,417 | 3.08% | part of the USA |

*The full national table (69 rows) is in the appendix.* **Before this work, the USA was 15.8% of Tepenia's humans
and China 10.6%; after it, no single origin is above 6.8%,** and the top ten are all between 3.4% and 6.8%.

## Can these be reasonably and justifiably made?

### The successor splits: owed by canon, not just justifiable
The countries split long before the exile era (the First Interwar reorganizations; the borders are the developer's
atlas). A city table that says "USA" or "Russia" in the Second Interwar names a country that no longer exists, so
dividing those rows is a correction, not a design choice. What is still open is only **how**:

1. **By pool, or by time-zone window.** This run gives every successor its pool share everywhere. The composition
   method's own rule is that small pools reach only cities within three solar time zones; under it, the smallest
   successors would drop out of distant cities and their people go to the successors in the window. That changes
   little (those rows are at most 0.37% of any city), but the **mid-size** successors (Midwest Republic, Colorado,
   Sonora, Quebec, the Prairie Federation, Yucatán, Künnarantaiga, Donska-Kubania, Araucanía-Patagonia) depend on
   what counts as a "large pool", and that is the open Russia ruling, now widened to every split country. The
   October 29 research already has the window answer for Russia in 14 cities (`RS2`–`RS4`).
2. **Canada's Demilitarized Zone** (128,728 humans nationally; up to 5.2% of a city, at Rothera): not a nation
   (decision 2).
3. **Option A or B** for every country (decision 1): this run used B throughout.

### The rebalance with the new settings
- **The wider band (55–65%)** puts the Sinian Federation at 50–59% of China's old figure city by city, still in
  line with the UN projection cited in `07` and `08`.
- **The proportional fill and the 4.5% line** remove run 1's two mechanical problems: the borderline nations
  (Davis's founder Australia among them) now receive their share, and the fill follows community size, as the
  migration-network research found (`08`, sources).
- **Run 1's main condition is met:** with the USA split applied, every China-and-USA city ends flat (lead at most
  1.14). Cape Adare ends with Australia 12.7%, Japan 12.3%, the Sinian Federation 11.5%, Indonesia 10.9%, which fits
  its ruling of no single dominant national community.

### What still needs the developer
1. **Three new single leaders made visible by the USA split:**
   - **Ariun Nuur:** Japan 25.0% (1.84×) in a city founded by Künnarantaiga and Mongolia, neither of which has a row.
   - **Utstein:** Japan 16.9% (2.07×) in a city founded by the Scandinavian Trade Union nations. The only ones in its
     table are Norway (2.76%) and Finland (2.57%).
   - **Esperanza:** Brazil 18.9% (1.36×) in an Argentine-founded city; Argentina is 7.5% plus 0.8% for Patagonia.
     Its Option D (a smaller city) is also pending.

   In each case the old USA row was hiding a mismatch between the founders and the long-run mix. It was not caused
   by this run, but this is where it shows.
2. **Japan and South Korea become Tepenia's two largest origin communities** (6.8% and 6.5%), with Australia fifth.
   Run 1's caveat stands: both face real-world population decline as steep as China's, and Australia is the nation
   already noted as heavily represented (`FQ-20`).
3. **Sanay** (Germany 25%, 2.16×, in a South African-founded city) was not touched by this run; it is the largest
   single share left outside the founding allocations. Noted only.
4. **Run 1's founder gaps still stand:** Kazakhstan (Temirötkel, Mawson), Russia (Mawson), Idelsk-Uralia (Mirny),
   New Zealand at Scott (3.52%) and Malaysia at Relung Panen (3.30%).
5. **The four cities recommended to wait** (Concordia, Dome Fuji, Relung Panen, Amundsen Station) are computed here
   for completeness; the recommendation stands.
6. **Order.** Doing the splits first and the decline second lets the CSA and Cascadia take part of the fill in the
   American cities, and stops "Russia" taking fill as a whole. The leaders come out the same in every city, and the
   leads within 0.06 except in Shirayuki (3.77 → 3.64) and Sinheung (3.36 → 3.15), where Russia's successors fall
   under 4.5% and their part of the fill goes to the second-place nations instead (check table in the appendix). **Claude recommends splits first when this is applied for
   real:** the communities in the Second Interwar are successor communities, so the fill should follow them.

### In one paragraph
**With the developer's settings and the splits together, the result is what the developer described: generally
multicultural, not equal.** No origin is above 6.8% nationally; 30 of 37 cities have no clear single leader; the
Sinian Federation stays a large community almost everywhere it was without dominating any city outside Zhongshan.
The splits themselves are owed by canon; what remains are the rulings on how to split (pool or window, Option A or
B, the Demilitarized Zone), the three founder mismatches the USA split exposes (Ariun Nuur, Utstein, Esperanza),
and who the setting wants its largest communities to be (Japan, South Korea, Australia).

## Files

`calc_rebalance_v2.py` (rerun to reproduce) · `09_city_tables.csv` (every row, every census column, 37 cities) ·
this file. Run 1's files (`08_*`) are kept as they were.

*Self-correction logged in `07` (~23:50): its national China figure had dropped Byrd's 5,853 humans; fixed. Run 1
and run 2 were not affected (both read Byrd correctly).*

---

## Appendix: the script's full output

*Pasted from `python3 calc_rebalance_v2.py`, unedited apart from heading levels.*

### Successor shares used (Option B: each successor's share of the old country's pool)

- **USA:** CSA 28.91% · Appalachia 19.64% · New England 19.51% · Cascadia 17.96% · Midwest Republic 6.14% · Colorado 4.75% · Sonora 2.45% · Hawaii 0.41% · Alaska 0.22%
- **Canada:** Demilitarized Zone (s. Ontario; not a nation) 36.54% · Quebec 25.23% · Prairie Federation 24.01% · Cascadia 13.82% · Alaska 0.40%
- **Mexico:** México 79.71% · Yucatán 8.90% · Sonora 6.91% · Cascadia 4.48%
- **Argentina:** Argentina (without Patagonia) 89.94% · Araucanía-Patagonia 10.06%
- **Russia:** Russia (core state) 41.83% · Idelsk-Uralia 23.41% · Siberia 16.90% · Künnarantaiga 8.24% · Donska-Kubania 7.12% · Karelia 0.97% · Dagestan 0.61% · Chechnya 0.29% · Kabardino-Balkaria 0.20% · North Ossetia-Alania 0.19% · Karachay-Cherkessia 0.10% · Tuva 0.08% · Ingushetia 0.06%

### Draws (seed 20261101, uniform 0.55-0.65, same order as run 1)

| City | Draw | Sinian factor (0.9156 × draw) |
|---|--:|--:|
| Dumont d'Urville | 0.6236 | 0.5710 |
| Mirny | 0.5616 | 0.5142 |
| Zukelli | 0.5894 | 0.5397 |
| Relung Panen | 0.6195 | 0.5673 |
| Janbogo | 0.5550 | 0.5082 |
| Davis | 0.5719 | 0.5237 |
| Temirötkel | 0.5829 | 0.5338 |
| Mawson | 0.5642 | 0.5166 |
| Denison | 0.6464 | 0.5919 |
| Cape Adare | 0.6333 | 0.5799 |
| Scott | 0.6337 | 0.5803 |
| Fort McMurdo | 0.5591 | 0.5119 |
| Amundsen Station | 0.6410 | 0.5869 |
| Casey | 0.5501 | 0.5037 |
| Dome Fuji | 0.5526 | 0.5060 |
| Sinheung | 0.5888 | 0.5391 |
| Concordia | 0.5996 | 0.5490 |
| Shirayuki | 0.6427 | 0.5885 |
| Byrd | 0.6184 | 0.5662 |
| Palmer City | 0.6378 | 0.5840 |

*Every city keeps its exact total in every census column: yes.*

### Every city, after both steps

| City | China → Sinian Fed. | Leader before | Leader after | Lead after (1st ÷ 2nd) | Top five after (%) |
|---|---|---|---|--:|---|
| Amundsen Station | 19.31 → 11.33 | USA 22.80 | UK 12.35 | 1.05 | UK 12.3, Germany 11.8, Sinian Federation 11.3, Japan 11.2, South Korea 6.7 |
| Byrd | 2.95 → 1.67 | USA 13.57 | Australia 7.07 | 1.04 | Australia 7.1, Japan 6.8, Demilitarized Zone 4.2, Cascadia 4.1, CSA 3.9 |
| Belgrano | — | USA 28.57 | Brazil 13.73 | 1.02 | Brazil 13.7, Germany 13.4, CSA 8.3, Appalachia 5.6, New England 5.6 |
| Halley | — | USA 23.53 | Brazil 11.69 | 1.11 | Brazil 11.7, UK 10.6, France 7.3, CSA 6.8, Cascadia 5.7 |
| Lazar | — | USA 19.05 | UK 10.08 | 1.06 | UK 10.1, Germany 9.5, Brazil 9.1, CSA 5.5, Appalachia 3.7 |
| Neumayer | — | USA 19.51 | France 10.03 | 1.07 | France 10.0, Germany 9.4, CSA 5.6, UK 5.2, Brazil 4.6 |
| Sanay | — | Germany 25.00 | Germany 25.00 | 2.16 | Germany 25.0, Brazil 11.6, UK 7.2, Estonia 4.6, Serbia 4.5 |
| Santa Luce | — | USA 17.02 | Brazil 8.93 | 1.14 | Brazil 8.9, UK 7.8, Magna Lombardia 6.4, CSA 4.9, Russia (core state) 3.8 |
| Troll | — | USA 18.60 | UK 8.44 | 1.01 | UK 8.4, Brazil 8.4, France 5.5, CSA 5.4, Russia (core state) 4.1 |
| Utstein | — | Japan 16.94 | Japan 16.94 | 2.07 | Japan 16.9, Brazil 8.2, France 7.7, Australia 7.2, Germany 4.6 |
| Cape Adare | 19.85 → 11.51 | USA 22.26 | Australia 12.65 | 1.03 | Australia 12.7, Japan 12.3, Sinian Federation 11.5, Indonesia 10.9, CSA 6.4 |
| Concordia | 7.70 → 4.23 | Japan 9.32 | Japan 10.07 | 1.00 | Japan 10.1, South Korea 10.1, Australia 8.4, Indonesia 8.3, Vietnam 4.2 |
| Denison | 22.29 → 13.19 | USA 26.19 | South Korea 15.39 | 1.14 | South Korea 15.4, Indonesia 13.5, Sinian Federation 13.2, Japan 9.3, CSA 7.6 |
| Dumont d'Urville | 24.31 → 13.88 | China 24.31 | France 14.86 | 1.01 | France 14.9, Japan 14.8, Australia 14.0, Sinian Federation 13.9, Indonesia 7.0 |
| Fort McMurdo | 19.34 → 9.90 | USA 21.69 | Germany 13.39 | 1.08 | Germany 13.4, France 12.4, Japan 11.6, Sinian Federation 9.9, CSA 6.3 |
| Janbogo | 20.63 → 10.48 | China 20.63 | South Korea 12.65 | 1.02 | South Korea 12.7, Australia 12.4, Italy 11.3, Indonesia 11.0, Sinian Federation 10.5 |
| Scott | 19.48 → 11.30 | USA 22.62 | Japan 12.68 | 1.00 | Japan 12.7, UK 12.7, Sinian Federation 11.3, Australia 11.1, South Korea 7.5 |
| Zukelli | 22.63 → 12.21 | China 22.63 | South Korea 13.54 | 1.11 | South Korea 13.5, Sinian Federation 12.2, Australia 11.7, Italy 7.6, Indonesia 7.2 |
| Dome Fuji | 10.13 → 5.13 | USA 11.20 | Indonesia 6.60 | 1.07 | Indonesia 6.6, Australia 6.2, France 6.0, Germany 5.8, South Korea 5.7 |
| Mawson | 17.02 → 8.79 | China 17.02 | UK 10.72 | 1.08 | UK 10.7, Australia 9.9, Indonesia 9.4, Japan 8.9, Sinian Federation 8.8 |
| Temirötkel | 17.39 → 9.28 | China 17.39 | Indonesia 10.21 | 1.04 | Indonesia 10.2, Australia 9.8, Germany 9.8, UK 9.5, Sinian Federation 9.3 |
| Ariun Nuur | — | USA 28.36 | Japan 24.97 | 1.84 | Japan 25.0, Indonesia 13.6, CSA 8.2, Cascadia 7.0, Australia 6.5 |
| Casey | 19.06 → 9.60 | USA 21.96 | South Korea 12.60 | 1.04 | South Korea 12.6, France 12.1, Australia 11.2, Sinian Federation 9.6, Japan 6.4 |
| Davis | 19.04 → 9.97 | China 19.04 | Japan 11.06 | 1.02 | Japan 11.1, Germany 10.8, UK 10.2, Sinian Federation 10.0, South Korea 8.4 |
| Mirny | 24.24 → 12.46 | China 24.24 | UK 14.81 | 1.06 | UK 14.8, South Korea 14.0, Indonesia 13.1, Sinian Federation 12.5, Japan 7.8 |
| Relung Panen | 21.58 → 12.24 | China 21.58 | Indonesia 13.89 | 1.02 | Indonesia 13.9, Japan 13.6, South Korea 12.7, Australia 12.5, Sinian Federation 12.2 |
| Shirayuki | 7.18 → 4.23 | Japan 36.27 | Japan 36.27 | 3.77 | Japan 36.3, Australia 9.6, South Korea 8.7, Germany 5.4, Sinian Federation 4.2 |
| Sinheung | 9.74 → 5.25 | South Korea 34.62 | South Korea 34.62 | 3.36 | South Korea 34.6, Germany 10.3, Japan 9.3, Sinian Federation 5.3, Indonesia 4.4 |
| Zhongshan | 35.83 → 35.83 | China 35.83 | China 35.83 | 3.69 | China 35.8, South Korea 9.7, Germany 8.5, Japan 7.3, Australia 3.7 |
| Contrapunto | — | USA 21.65 | France 11.62 | 1.03 | France 11.6, UK 11.3, Germany 10.7, México 9.0, Brazil 6.7 |
| Esperanza | — | USA 36.36 | Brazil 18.92 | 1.36 | Brazil 18.9, México 13.9, CSA 10.5, UK 9.8, Argentina (without Patagonia) 7.5 |
| Marambio | — | USA 27.59 | Spain 14.19 | 1.05 | Spain 14.2, UK 13.5, México 11.2, CSA 8.0, Germany 6.6 |
| Palmer City | 0.91 → 0.53 | USA 20.29 | Brazil 9.76 | 1.01 | Brazil 9.8, France 9.6, Germany 9.6, CSA 5.9, UK 5.6 |
| Pergamino | — | USA 29.63 | Italy 14.24 | 1.01 | Italy 14.2, Spain 14.1, UK 13.7, CSA 8.6, France 8.5 |
| Puerto Abrigo | — | USA 32.00 | France 16.71 | 1.13 | France 16.7, Germany 14.8, UK 14.3, Brazil 9.7, CSA 9.3 |
| Rothera | — | USA 28.57 | Germany 14.31 | 1.02 | Germany 14.3, Brazil 14.0, CSA 8.3, France 7.4, Cascadia 7.4 |
| Signy | — | USA 33.33 | France 17.19 | 1.01 | France 17.2, UK 17.0, CSA 9.6, Brazil 8.0, Germany 7.8 |

### Nationally (Census I humans, summed from the specs: 15,612,333 before, 15,612,333 after)

| Rank | Nation or successor | Humans after | Share of Tepenia | Before (as listed today) |
|--:|---|--:|--:|---|
| 1 | Japan | 1,055,208 | 6.76% | 953,710 |
| 2 | South Korea | 1,009,340 | 6.47% | 892,502 |
| 3 | Sinian Federation | 992,151 | 6.35% | China 1,660,450 (includes Zhongshan's 208,145, unchanged) |
| 4 | UK | 905,182 | 5.80% | 855,222 |
| 5 | Australia | 842,401 | 5.40% | 727,081 |
| 6 | Germany | 770,778 | 4.94% | 735,406 |
| 7 | CSA | 711,987 | 4.56% | part of USA |
| 8 | Indonesia | 709,614 | 4.55% | 606,976 |
| 9 | Brazil | 705,096 | 4.52% | 704,963 |
| 10 | France | 526,283 | 3.37% | 490,468 |
| 11 | Cascadia | 503,535 | 3.23% | part of USA, Canada, Mexico |
| 12 | Appalachia | 483,737 | 3.10% | part of USA |
| 13 | New England | 480,417 | 3.08% | part of USA |
| 14 | Chile | 229,408 | 1.47% | 229,408 |
| 15 | Russia (core state) | 226,719 | 1.45% | part of Russia |
| 16 | New Zealand | 226,668 | 1.45% | 226,668 |
| 17 | México | 222,084 | 1.42% | part of Mexico |
| 18 | Argentina (without Patagonia) | 215,331 | 1.38% | part of Argentina |
| 19 | Philippines | 202,631 | 1.30% | 196,541 |
| 20 | Vietnam | 200,650 | 1.29% | 197,574 |
| 21 | Malaysia | 198,508 | 1.27% | 198,508 |
| 22 | Italy | 190,845 | 1.22% | 164,828 |
| 23 | Thailand | 176,509 | 1.13% | 173,181 |
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
| 36 | Ukraine | 130,844 | 0.84% | 130,844 |
| 37 | Croatia | 129,454 | 0.83% | 129,454 |
| 38 | Demilitarized Zone (s. Ontario; not a nation) | 128,728 | 0.82% | part of Canada |
| 39 | Idelsk-Uralia | 126,883 | 0.81% | part of Russia |
| 40 | Belarus | 122,235 | 0.78% | 122,235 |
| 41 | Norway | 121,223 | 0.78% | 121,223 |
| 42 | Uruguay | 119,026 | 0.76% | 119,026 |
| 43 | Latvia | 117,792 | 0.75% | 117,792 |
| 44 | Netherlands | 117,470 | 0.75% | 117,470 |
| 45 | Colorado | 116,898 | 0.75% | part of USA |
| 46 | Finland | 103,357 | 0.66% | 103,357 |
| 47 | Siberia | 91,596 | 0.59% | part of Russia |
| 48 | Quebec | 88,903 | 0.57% | part of Canada |
| 49 | Prairie Federation | 84,576 | 0.54% | part of Canada |
| 50 | Sonora | 79,700 | 0.51% | part of USA, Mexico |
| 51 | Spain | 77,165 | 0.49% | 77,165 |
| 52 | Künnarantaiga | 44,663 | 0.29% | part of Russia |
| 53 | Belgium | 42,545 | 0.27% | 42,545 |
| 54 | Sweden | 39,657 | 0.25% | 39,657 |
| 55 | Donska-Kubania | 38,590 | 0.25% | part of Russia |
| 56 | Yucatán | 24,797 | 0.16% | part of Mexico |
| 57 | Araucanía-Patagonia | 24,081 | 0.15% | part of Argentina |
| 58 | Magna Lombardia | 13,649 | 0.09% | 13,649 |
| 59 | Hawaii | 10,029 | 0.06% | part of USA |
| 60 | Alaska | 6,879 | 0.04% | part of USA, Canada |
| 61 | Karelia | 5,256 | 0.03% | part of Russia |
| 62 | Meridia | 4,550 | 0.03% | 4,550 |
| 63 | Dagestan | 3,305 | 0.02% | part of Russia |
| 64 | Chechnya | 1,572 | 0.01% | part of Russia |
| 65 | Kabardino-Balkaria | 1,084 | 0.01% | part of Russia |
| 66 | North Ossetia-Alania | 1,032 | 0.01% | part of Russia |
| 67 | Karachay-Cherkessia | 539 | 0.00% | part of Russia |
| 68 | Tuva | 434 | 0.00% | part of Russia |
| 69 | Ingushetia | 326 | 0.00% | part of Russia |

### Check: the splits first, then the decline (order reversed)

*Same draws and rules; successor rows count as outside the top tier, so they can receive the fill.*

| City | Receivers, decline first | Receivers, splits first | Leader then | Lead (1st ÷ 2nd) |
|---|---|---|---|--:|
| Amundsen Station | UK, Germany, Japan, Canada, South Korea, Australia | CSA, Cascadia, UK, Germany, Japan, South Korea, Australia | UK 12.17 | 1.05 |
| Byrd | Australia, Japan | Australia, Japan | Australia 7.07 | 1.04 |
| Cape Adare | Australia, Japan, Indonesia, Canada, South Korea, UK | CSA, Cascadia, Australia, Japan, Indonesia, South Korea, UK | Australia 12.48 | 1.03 |
| Concordia | Japan, South Korea, Russia, Australia, Indonesia | Japan, South Korea, Australia, Indonesia | Japan 10.27 | 1.00 |
| Denison | South Korea, Indonesia, Japan, Australia | CSA, Appalachia, New England, Cascadia, South Korea, Indonesia, Japan, Australia | South Korea 14.21 | 1.08 |
| Dumont d'Urville | France, Japan, Australia, Indonesia | CSA, France, Japan, Australia, Indonesia | France 14.47 | 1.01 |
| Fort McMurdo | Germany, France, Japan, Italy | CSA, Germany, France, Japan, Italy | Germany 12.94 | 1.08 |
| Janbogo | South Korea, Australia, Italy, Indonesia, Germany | CSA, South Korea, Australia, Italy, Indonesia, Germany | South Korea 12.38 | 1.02 |
| Scott | Japan, UK, Australia, South Korea, Canada, Indonesia | CSA, Cascadia, Japan, UK, Australia, South Korea, Indonesia | Japan 12.46 | 1.00 |
| Zukelli | South Korea, Canada, Australia, Italy, Indonesia, Japan | CSA, Cascadia, South Korea, Australia, Italy, Indonesia, Japan | South Korea 13.51 | 1.11 |
| Dome Fuji | Indonesia, Australia, France, Germany, South Korea | Indonesia, Australia, France, Germany, South Korea | Indonesia 6.60 | 1.07 |
| Mawson | UK, Australia, Indonesia, Japan, France, South Korea | UK, Australia, Indonesia, Japan, France, South Korea | UK 10.72 | 1.08 |
| Temirötkel | Indonesia, Australia, Germany, UK, South Korea, France | Indonesia, Australia, Germany, UK, South Korea, France | Indonesia 10.21 | 1.04 |
| Casey | South Korea, France, Australia, Russia, Japan, Indonesia | CSA, South Korea, France, Australia, Japan, Indonesia | South Korea 12.59 | 1.04 |
| Davis | Japan, Germany, UK, South Korea, Russia, Indonesia, Australia | Japan, Germany, UK, South Korea, Indonesia, Australia | Japan 11.27 | 1.02 |
| Mirny | UK, South Korea, Indonesia, Russia, Japan, Australia, Philippines | UK, South Korea, Indonesia, Japan, Australia, Philippines | UK 15.16 | 1.06 |
| Relung Panen | Russia, Indonesia, Japan, South Korea, Australia, Thailand, Vietnam | Russia (core state), Indonesia, Japan, South Korea, Australia, Thailand, Vietnam | Indonesia 14.08 | 1.02 |
| Shirayuki | Australia, Russia, South Korea, Germany | Australia, South Korea, Germany | Japan 36.27 | 3.64 |
| Sinheung | Japan, Germany, Russia | Japan, Germany | South Korea 34.62 | 3.15 |
| Palmer City | Brazil, France, Germany, Mexico, Canada, UK | CSA, Cascadia, Brazil, France, Germany, México, UK | Brazil 9.75 | 1.01 |

### City by city (rows under 0.10% are added together by source country; every row is in the CSV)

#### Amundsen Station

*draw 0.6410; fill to: UK, Germany, Japan, Canada, South Korea, Australia*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | UK |  | 10.57% | 12.35% | 138 |
| Significant | Germany |  | 10.09% | 11.79% | 132 |
| Primary | Sinian Federation | China | 19.31% | 11.33% | 127 |
| Significant | Japan |  | 9.59% | 11.20% | 125 |
| Significant | South Korea |  | 5.70% | 6.66% | 74 |
| Primary | CSA | USA | — | 6.59% | 74 |
| Significant | Australia |  | 5.22% | 6.10% | 69 |
| Primary | Cascadia | USA + Canada | — | 5.10% | 57 |
| Primary | Appalachia | USA | — | 4.48% | 50 |
| Primary | New England | USA | — | 4.45% | 50 |
| Notable | New Zealand |  | 3.59% | 3.59% | 40 |
| Notable | Argentina (without Patagonia) | Argentina | — | 3.23% | 36 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 2.65% | 30 |
| Significant | Quebec | Canada | — | 1.83% | 21 |
| Significant | Prairie Federation | Canada | — | 1.74% | 20 |
| Notable | Norway |  | 1.67% | 1.67% | 19 |
| Notable | Chile |  | 1.67% | 1.67% | 19 |
| Primary | Midwest Republic | USA | — | 1.40% | 16 |
| Primary | Colorado | USA | — | 1.08% | 12 |
| Primary | Sonora | USA | — | 0.56% | 6 |
| Notable | Araucanía-Patagonia | Argentina | — | 0.36% | 4 |
| | *1 smaller USA successor* | USA | — | 0.09% | 1 |
| | *1 smaller USA + Canada successor* | USA + Canada | — | 0.08% | 1 |

*Split today's: USA 22.80%, Canada 6.20%, Argentina 3.59% (after step 1 where it received fill).*

#### Byrd

*draw 0.6184; fill to: Australia, Japan*

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

*Split today's: USA 13.57%, Canada 11.43%, Russia 1.19%, Argentina 0.98%, Mexico 0.96% (after step 1 where it received fill).*

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

*Split today's: USA 28.57%, Argentina 4.40% (after step 1 where it received fill).*

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

*Split today's: USA 23.53%, Canada 10.34%, Argentina 2.32% (after step 1 where it received fill).*

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

*Split today's: USA 19.05%, Russia 4.81%, Argentina 1.46% (after step 1 where it received fill).*

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

*Split today's: USA 19.51%, Argentina 3.16% (after step 1 where it received fill).*

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

*Split today's: Argentina 4.22% (after step 1 where it received fill).*

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

*Split today's: USA 17.02%, Russia 9.04%, Argentina 3.06% (after step 1 where it received fill).*

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

*Split today's: USA 18.60%, Russia 9.88%, Argentina 3.43% (after step 1 where it received fill).*

#### Utstein

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Primary | Japan |  | 16.94% | 16.94% | 95,863 |
| Significant | Brazil |  | 8.18% | 8.18% | 46,290 |
| Significant | France |  | 7.73% | 7.73% | 43,730 |
| Significant | Australia |  | 7.19% | 7.19% | 40,664 |
| Significant | Germany |  | 4.58% | 4.58% | 25,913 |
| Primary | CSA | USA | — | 4.17% | 23,614 |
| Primary | Appalachia | USA | — | 2.83% | 16,044 |
| Primary | New England | USA | — | 2.82% | 15,934 |
| Notable | Belgium |  | 2.78% | 2.78% | 15,758 |
| Notable | Norway |  | 2.76% | 2.76% | 15,638 |
| Notable | Poland |  | 2.73% | 2.73% | 15,443 |
| Notable | Ukraine |  | 2.71% | 2.71% | 15,325 |
| Notable | Serbia |  | 2.67% | 2.67% | 15,091 |
| Primary | Cascadia | USA | — | 2.59% | 14,672 |
| Notable | Finland |  | 2.57% | 2.57% | 14,564 |
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
| Primary | Sonora | USA | — | 0.35% | 2,005 |
| Notable | Araucanía-Patagonia | Argentina | — | 0.12% | 679 |
| | *2 smaller USA successors* | USA | — | 0.09% | 514 |

*Split today's: USA 14.43%, Argentina 1.19% (after step 1 where it received fill).*

#### Cape Adare

*draw 0.6333; fill to: Australia, Japan, Indonesia, Canada, South Korea, UK*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Australia |  | 10.76% | 12.65% | 95,915 |
| Significant | Japan |  | 10.49% | 12.34% | 93,568 |
| Primary | Sinian Federation | China | 19.85% | 11.51% | 87,249 |
| Significant | Indonesia |  | 9.28% | 10.91% | 82,726 |
| Primary | CSA | USA | — | 6.44% | 48,786 |
| Significant | South Korea |  | 5.29% | 6.22% | 47,205 |
| Significant | UK |  | 5.03% | 5.92% | 44,859 |
| Primary | Cascadia | USA + Canada | — | 5.06% | 38,333 |
| Primary | Appalachia | USA | — | 4.37% | 33,146 |
| Primary | New England | USA | — | 4.34% | 32,918 |
| Notable | Chile |  | 3.74% | 3.74% | 28,375 |
| Notable | New Zealand |  | 3.19% | 3.19% | 24,155 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 2.80% | 21,209 |
| Notable | Philippines |  | 2.08% | 2.08% | 15,745 |
| Significant | Quebec | Canada | — | 1.93% | 14,647 |
| Significant | Prairie Federation | Canada | — | 1.84% | 13,935 |
| Notable | Malaysia |  | 1.52% | 1.52% | 11,526 |
| Primary | Midwest Republic | USA | — | 1.37% | 10,364 |
| Primary | Colorado | USA | — | 1.06% | 8,010 |
| Primary | Sonora | USA | — | 0.55% | 4,142 |
| | *1 smaller USA successor* | USA | — | 0.09% | 687 |
| | *1 smaller USA + Canada successor* | USA + Canada | — | 0.08% | 607 |

*Split today's: USA 22.26%, Canada 6.51% (after step 1 where it received fill).*

#### Concordia

*draw 0.5996; fill to: Japan, South Korea, Russia, Australia, Indonesia (FALLBACK: nobody outside the top tier reaches 4.5%)*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Primary | Japan |  | 9.32% | 10.07% | 52,060 |
| Primary | South Korea |  | 9.31% | 10.06% | 51,957 |
| Primary | Australia |  | 7.82% | 8.45% | 43,652 |
| Primary | Indonesia |  | 7.72% | 8.34% | 43,074 |
| Significant | Vietnam |  | 4.23% | 4.23% | 21,846 |
| Primary | Sinian Federation | China | 7.70% | 4.23% | 21,844 |
| Primary | Russia (core state) | Russia | — | 4.16% | 21,492 |
| Significant | Belarus |  | 3.77% | 3.77% | 19,477 |
| Significant | New Zealand |  | 3.76% | 3.76% | 19,461 |
| Significant | Philippines |  | 2.62% | 2.62% | 13,518 |
| Primary | Idelsk-Uralia | Russia | — | 2.33% | 12,028 |
| Significant | Malaysia |  | 1.95% | 1.95% | 10,079 |
| Primary | Siberia | Russia | — | 1.68% | 8,683 |
| Notable | Serbia |  | 1.59% | 1.59% | 8,227 |
| Significant | Thailand |  | 1.58% | 1.58% | 8,187 |
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
| Primary | Künnarantaiga | Russia | — | 0.82% | 4,234 |
| Notable | Latvia |  | 0.81% | 0.81% | 4,176 |
| Notable | Italy |  | 0.75% | 0.75% | 3,856 |
| Notable | Sweden |  | 0.75% | 0.75% | 3,879 |
| Notable | Bulgaria |  | 0.72% | 0.72% | 3,719 |
| Primary | Donska-Kubania | Russia | — | 0.71% | 3,658 |
| Notable | Ukraine |  | 0.69% | 0.69% | 3,581 |
| Notable | Romania |  | 0.69% | 0.69% | 3,559 |
| Notable | Slovakia |  | 0.66% | 0.66% | 3,408 |
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
| | *8 smaller Russia successors* | Russia | — | 0.25% | 1,285 |
| | *1 smaller USA successor* | USA | — | 0.02% | 93 |
| | *1 smaller USA + Canada successor* | USA + Canada | — | 0.01% | 64 |

*Split today's: Russia 9.20%, USA 4.43%, Mexico 1.29%, Canada 0.61% (after step 1 where it received fill).*

#### Denison

*draw 0.6464; fill to: South Korea, Indonesia, Japan, Australia*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | South Korea |  | 12.31% | 15.39% | 70,295 |
| Significant | Indonesia |  | 10.77% | 13.46% | 61,517 |
| Primary | Sinian Federation | China | 22.29% | 13.19% | 60,263 |
| Significant | Japan |  | 7.41% | 9.26% | 42,288 |
| Primary | CSA | USA | — | 7.57% | 34,580 |
| Significant | Australia |  | 5.87% | 7.34% | 33,509 |
| Primary | Appalachia | USA | — | 5.14% | 23,494 |
| Primary | New England | USA | — | 5.11% | 23,333 |
| Primary | Cascadia | USA | — | 4.70% | 21,485 |
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

*Split today's: USA 26.19% (after step 1 where it received fill).*

#### Dumont d'Urville

*draw 0.6236; fill to: France, Japan, Australia, Indonesia*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | France |  | 11.80% | 14.86% | 29,894 |
| Significant | Japan |  | 11.72% | 14.76% | 29,706 |
| Significant | Australia |  | 11.08% | 13.95% | 28,069 |
| Primary | Sinian Federation | China | 24.31% | 13.88% | 27,934 |
| Significant | Indonesia |  | 5.59% | 7.04% | 14,166 |
| Primary | CSA | USA | — | 5.82% | 11,709 |
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

*Split today's: USA 20.13% (after step 1 where it received fill).*

#### Fort McMurdo

*draw 0.5591; fill to: Germany, France, Japan, Italy*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Germany |  | 10.49% | 13.39% | 29,730 |
| Significant | France |  | 9.73% | 12.42% | 27,573 |
| Significant | Japan |  | 9.08% | 11.59% | 25,758 |
| Primary | Sinian Federation | China | 19.34% | 9.90% | 21,998 |
| Primary | CSA | USA | — | 6.27% | 13,931 |
| Significant | Italy |  | 4.90% | 6.25% | 13,888 |
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

*Split today's: USA 21.69%, Canada 3.49% (after step 1 where it received fill).*

#### Janbogo

*draw 0.5550; fill to: South Korea, Australia, Italy, Indonesia, Germany*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | South Korea |  | 10.23% | 12.65% | 83,312 |
| Significant | Australia |  | 9.99% | 12.35% | 81,382 |
| Significant | Italy |  | 9.14% | 11.30% | 74,413 |
| Significant | Indonesia |  | 8.88% | 10.98% | 72,317 |
| Primary | Sinian Federation | China | 20.63% | 10.48% | 69,064 |
| Significant | Germany |  | 4.64% | 5.74% | 37,819 |
| Primary | CSA | USA | — | 5.32% | 35,028 |
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

*Split today's: USA 18.39%, Canada 3.94% (after step 1 where it received fill).*

#### Scott

*draw 0.6337; fill to: Japan, UK, Australia, South Korea, Canada, Indonesia*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Japan |  | 10.81% | 12.68% | 24,062 |
| Significant | UK |  | 10.79% | 12.65% | 24,026 |
| Primary | Sinian Federation | China | 19.48% | 11.30% | 21,461 |
| Significant | Australia |  | 9.43% | 11.06% | 20,994 |
| Significant | South Korea |  | 6.36% | 7.46% | 14,152 |
| Primary | CSA | USA | — | 6.54% | 12,414 |
| Significant | Indonesia |  | 4.98% | 5.84% | 11,084 |
| Primary | Cascadia | USA + Canada | — | 4.87% | 9,249 |
| Primary | Appalachia | USA | — | 4.44% | 8,435 |
| Primary | New England | USA | — | 4.41% | 8,377 |
| Notable | Chile |  | 3.69% | 3.69% | 6,996 |
| Notable | New Zealand |  | 3.52% | 3.52% | 6,687 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 2.14% | 4,063 |
| Notable | Malaysia |  | 1.74% | 1.74% | 3,303 |
| Notable | Philippines |  | 1.58% | 1.58% | 2,994 |
| Significant | Quebec | Canada | — | 1.48% | 2,806 |
| Significant | Prairie Federation | Canada | — | 1.41% | 2,669 |
| Primary | Midwest Republic | USA | — | 1.39% | 2,637 |
| Primary | Colorado | USA | — | 1.07% | 2,038 |
| Primary | Sonora | USA | — | 0.56% | 1,054 |
| | *1 smaller USA successor* | USA | — | 0.09% | 175 |
| | *1 smaller USA + Canada successor* | USA + Canada | — | 0.07% | 140 |

*Split today's: USA 22.62%, Canada 5.00% (after step 1 where it received fill).*

#### Zukelli

*draw 0.5894; fill to: South Korea, Canada, Australia, Italy, Indonesia, Japan*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | South Korea |  | 11.10% | 13.54% | 86,643 |
| Primary | Sinian Federation | China | 22.63% | 12.21% | 78,140 |
| Significant | Australia |  | 9.55% | 11.65% | 74,559 |
| Significant | Italy |  | 6.24% | 7.61% | 48,665 |
| Significant | Indonesia |  | 5.89% | 7.19% | 45,967 |
| Significant | Japan |  | 4.69% | 5.72% | 36,582 |
| Primary | CSA | USA | — | 5.63% | 36,016 |
| Primary | Cascadia | USA + Canada | — | 5.17% | 33,054 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 4.41% | 28,229 |
| Primary | Appalachia | USA | — | 3.82% | 24,470 |
| Primary | New England | USA | — | 3.80% | 24,302 |
| Notable | Malaysia |  | 3.44% | 3.44% | 22,014 |
| Notable | New Zealand |  | 3.37% | 3.37% | 21,574 |
| Significant | Quebec | Canada | — | 3.05% | 19,496 |
| Significant | Prairie Federation | Canada | — | 2.90% | 18,547 |
| Notable | Philippines |  | 1.89% | 1.89% | 12,095 |
| Notable | Chile |  | 1.82% | 1.82% | 11,655 |
| Primary | Midwest Republic | USA | — | 1.20% | 7,651 |
| Primary | Colorado | USA | — | 0.92% | 5,913 |
| Primary | Sonora | USA | — | 0.48% | 3,058 |
| | *1 smaller USA + Canada successor* | USA + Canada | — | 0.09% | 586 |
| | *1 smaller USA successor* | USA | — | 0.08% | 507 |

*Split today's: USA 19.47%, Canada 9.90% (after step 1 where it received fill).*

#### Dome Fuji

*draw 0.5526; fill to: Indonesia, Australia, France, Germany, South Korea*

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

*Split today's: USA 11.20%, Russia 2.22%, Mexico 1.89%, Canada 1.73%, Argentina 0.84% (after step 1 where it received fill).*

#### Mawson

*draw 0.5642; fill to: UK, Australia, Indonesia, Japan, France, South Korea*

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

*draw 0.5829; fill to: Indonesia, Australia, Germany, UK, South Korea, France*

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

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Primary | Japan |  | 24.97% | 24.97% | 35,404 |
| Significant | Indonesia |  | 13.55% | 13.55% | 19,205 |
| Primary | CSA | USA | — | 8.20% | 11,622 |
| Primary | Cascadia | USA + Canada | — | 7.02% | 9,944 |
| Significant | Australia |  | 6.45% | 6.45% | 9,146 |
| Significant | South Korea |  | 6.10% | 6.10% | 8,645 |
| Primary | Appalachia | USA | — | 5.57% | 7,897 |
| Primary | New England | USA | — | 5.53% | 7,842 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 5.08% | 7,200 |
| Notable | Chile |  | 4.96% | 4.96% | 7,028 |
| Significant | Quebec | Canada | — | 3.51% | 4,973 |
| Significant | Prairie Federation | Canada | — | 3.34% | 4,731 |
| Primary | Midwest Republic | USA | — | 1.74% | 2,469 |
| Notable | New Zealand |  | 1.71% | 1.71% | 2,422 |
| Primary | Colorado | USA | — | 1.35% | 1,908 |
| Primary | Sonora | USA | — | 0.70% | 987 |
| Primary | Alaska | USA + Canada | — | 0.12% | 168 |
| Primary | Hawaii | USA | — | 0.12% | 164 |

*Split today's: USA 28.36%, Canada 13.90% (after step 1 where it received fill).*

#### Casey

*draw 0.5501; fill to: South Korea, France, Australia, Russia, Japan, Indonesia*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | South Korea |  | 10.46% | 12.60% | 94,044 |
| Significant | France |  | 10.05% | 12.11% | 90,368 |
| Significant | Australia |  | 9.26% | 11.16% | 83,199 |
| Primary | Sinian Federation | China | 19.06% | 9.60% | 71,626 |
| Significant | Japan |  | 5.33% | 6.42% | 47,913 |
| Primary | CSA | USA | — | 6.35% | 47,367 |
| Significant | Indonesia |  | 4.92% | 5.93% | 44,237 |
| Primary | Appalachia | USA | — | 4.31% | 32,182 |
| Primary | New England | USA | — | 4.28% | 31,961 |
| Primary | Cascadia | USA | — | 3.94% | 29,430 |
| Notable | New Zealand |  | 3.36% | 3.36% | 25,040 |
| Notable | Philippines |  | 3.35% | 3.35% | 25,007 |
| Notable | Vietnam |  | 3.21% | 3.21% | 23,937 |
| Significant | Russia (core state) | Russia | — | 3.09% | 23,041 |
| Notable | Malaysia |  | 1.78% | 1.78% | 13,246 |
| Significant | Idelsk-Uralia | Russia | — | 1.73% | 12,895 |
| Primary | Midwest Republic | USA | — | 1.35% | 10,062 |
| Significant | Siberia | Russia | — | 1.25% | 9,309 |
| Notable | Thailand |  | 1.13% | 1.13% | 8,403 |
| Primary | Colorado | USA | — | 1.04% | 7,777 |
| Significant | Künnarantaiga | Russia | — | 0.61% | 4,539 |
| Primary | Sonora | USA | — | 0.54% | 4,022 |
| Significant | Donska-Kubania | Russia | — | 0.53% | 3,922 |
| | *2 smaller USA successors* | USA | — | 0.14% | 1,031 |
| | *8 smaller Russia successors* | Russia | — | 0.18% | 1,377 |

*Split today's: USA 21.96%, Russia 6.13% (after step 1 where it received fill).*

#### Davis

*draw 0.5719; fill to: Japan, Germany, UK, South Korea, Russia, Indonesia, Australia*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Japan |  | 9.36% | 11.06% | 63,662 |
| Significant | Germany |  | 9.15% | 10.81% | 62,233 |
| Significant | UK |  | 8.65% | 10.22% | 58,832 |
| Primary | Sinian Federation | China | 19.04% | 9.97% | 57,405 |
| Significant | South Korea |  | 7.14% | 8.43% | 48,563 |
| Significant | Indonesia |  | 5.14% | 6.07% | 34,960 |
| Significant | Australia |  | 4.93% | 5.82% | 33,531 |
| Notable | Thailand |  | 3.52% | 3.52% | 20,266 |
| Notable | Ukraine |  | 3.51% | 3.51% | 20,208 |
| Notable | Vietnam |  | 3.29% | 3.29% | 18,941 |
| Notable | Philippines |  | 3.25% | 3.25% | 18,712 |
| Notable | Malaysia |  | 3.13% | 3.13% | 18,021 |
| Notable | Romania |  | 2.97% | 2.97% | 17,100 |
| Notable | South Africa |  | 2.92% | 2.92% | 16,811 |
| Significant | Russia (core state) | Russia | — | 2.79% | 16,047 |
| Notable | New Zealand |  | 1.79% | 1.79% | 10,305 |
| Notable | Belarus |  | 1.63% | 1.63% | 9,385 |
| Significant | Idelsk-Uralia | Russia | — | 1.56% | 8,980 |
| Notable | Bulgaria |  | 1.51% | 1.51% | 8,693 |
| Notable | Lithuania |  | 1.25% | 1.25% | 7,197 |
| Notable | Estonia |  | 1.24% | 1.24% | 7,140 |
| Significant | Siberia | Russia | — | 1.13% | 6,483 |
| Notable | Latvia |  | 0.94% | 0.94% | 5,412 |
| Significant | Künnarantaiga | Russia | — | 0.55% | 3,161 |
| Significant | Donska-Kubania | Russia | — | 0.47% | 2,731 |
| | *8 smaller Russia successors* | Russia | — | 0.17% | 959 |

*Split today's: Russia 5.64% (after step 1 where it received fill).*

#### Mirny

*draw 0.5616; fill to: UK, South Korea, Indonesia, Russia, Japan, Australia, Philippines*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | UK |  | 12.35% | 14.81% | 100,440 |
| Significant | South Korea |  | 11.64% | 13.96% | 94,684 |
| Significant | Indonesia |  | 10.96% | 13.15% | 89,110 |
| Primary | Sinian Federation | China | 24.24% | 12.46% | 84,522 |
| Significant | Japan |  | 6.54% | 7.84% | 53,184 |
| Significant | Australia |  | 5.83% | 6.99% | 47,427 |
| Notable | Philippines |  | 4.50% | 5.40% | 36,626 |
| Notable | New Zealand |  | 4.48% | 4.48% | 30,374 |
| Notable | Thailand |  | 3.70% | 3.70% | 25,055 |
| Notable | Malaysia |  | 3.65% | 3.65% | 24,723 |
| Significant | Russia (core state) | Russia | — | 3.62% | 24,578 |
| Significant | Idelsk-Uralia | Russia | — | 2.03% | 13,755 |
| Notable | Vietnam |  | 1.75% | 1.75% | 11,863 |
| Notable | Belarus |  | 1.58% | 1.58% | 10,719 |
| Notable | South Africa |  | 1.56% | 1.56% | 10,557 |
| Significant | Siberia | Russia | — | 1.46% | 9,930 |
| Significant | Künnarantaiga | Russia | — | 0.71% | 4,842 |
| Significant | Donska-Kubania | Russia | — | 0.62% | 4,183 |
| | *8 smaller Russia successors* | Russia | — | 0.22% | 1,469 |

*Split today's: Russia 7.22% (after step 1 where it received fill).*

#### Relung Panen

*draw 0.6195; fill to: Russia, Indonesia, Japan, South Korea, Australia, Thailand, Vietnam*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Indonesia |  | 12.23% | 13.89% | 66,274 |
| Significant | Japan |  | 11.98% | 13.60% | 64,921 |
| Significant | South Korea |  | 11.22% | 12.74% | 60,802 |
| Significant | Australia |  | 11.03% | 12.52% | 59,773 |
| Primary | Sinian Federation | China | 21.58% | 12.24% | 58,426 |
| Significant | Russia (core state) | Russia | — | 5.98% | 28,562 |
| Notable | Thailand |  | 5.15% | 5.85% | 27,908 |
| Notable | Vietnam |  | 4.76% | 5.40% | 25,795 |
| Significant | Idelsk-Uralia | Russia | — | 3.35% | 15,985 |
| Notable | Malaysia |  | 3.30% | 3.30% | 15,751 |
| Notable | Philippines |  | 3.18% | 3.18% | 15,178 |
| Notable | New Zealand |  | 2.97% | 2.97% | 14,176 |
| Significant | Siberia | Russia | — | 2.42% | 11,539 |
| Significant | Künnarantaiga | Russia | — | 1.18% | 5,626 |
| Significant | Donska-Kubania | Russia | — | 1.02% | 4,862 |
| Significant | Karelia | Russia | — | 0.14% | 662 |
| | *7 smaller Russia successors* | Russia | — | 0.22% | 1,045 |

*Split today's: Russia 12.60% (after step 1 where it received fill).*

#### Shirayuki

*draw 0.6427; fill to: Australia, Russia, South Korea, Germany*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Primary | Japan |  | 36.27% | 36.27% | 192,580 |
| Significant | Australia |  | 8.76% | 9.62% | 51,064 |
| Significant | South Korea |  | 7.89% | 8.66% | 45,993 |
| Significant | Germany |  | 4.93% | 5.41% | 28,738 |
| Significant | Sinian Federation | China | 7.18% | 4.23% | 22,434 |
| Significant | Russia (core state) | Russia | — | 3.95% | 20,995 |
| Notable | Romania |  | 3.54% | 3.54% | 18,796 |
| Notable | Vietnam |  | 3.16% | 3.16% | 16,779 |
| Notable | Ukraine |  | 3.11% | 3.11% | 16,512 |
| Notable | Belarus |  | 3.00% | 3.00% | 15,929 |
| Notable | Thailand |  | 2.99% | 2.99% | 15,875 |
| Notable | New Zealand |  | 2.97% | 2.97% | 15,770 |
| Significant | Idelsk-Uralia | Russia | — | 2.21% | 11,750 |
| Notable | Lithuania |  | 1.76% | 1.76% | 9,345 |
| Notable | South Africa |  | 1.66% | 1.66% | 8,813 |
| Notable | Bulgaria |  | 1.60% | 1.60% | 8,496 |
| Significant | Siberia | Russia | — | 1.60% | 8,482 |
| Notable | Latvia |  | 1.35% | 1.35% | 7,168 |
| Notable | Estonia |  | 1.22% | 1.22% | 6,478 |
| Significant | Künnarantaiga | Russia | — | 0.78% | 4,136 |
| Significant | Donska-Kubania | Russia | — | 0.67% | 3,574 |
| | *8 smaller Russia successors* | Russia | — | 0.24% | 1,254 |

*Split today's: Russia 8.61% (after step 1 where it received fill).*

#### Sinheung

*draw 0.5888; fill to: Japan, Germany, Russia*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Primary | South Korea |  | 34.62% | 34.62% | 165,973 |
| Significant | Germany |  | 8.64% | 10.31% | 49,411 |
| Significant | Japan |  | 7.78% | 9.28% | 44,493 |
| Significant | Sinian Federation | China | 9.74% | 5.25% | 25,174 |
| Significant | Indonesia |  | 4.41% | 4.41% | 21,142 |
| Notable | Thailand |  | 3.65% | 3.65% | 17,498 |
| Significant | Australia |  | 3.57% | 3.57% | 17,115 |
| Notable | Estonia |  | 3.52% | 3.52% | 16,875 |
| Notable | Hungary |  | 3.43% | 3.43% | 16,443 |
| Significant | Russia (core state) | Russia | — | 3.42% | 16,387 |
| Notable | Lithuania |  | 3.11% | 3.11% | 14,910 |
| Notable | Malaysia |  | 2.93% | 2.93% | 14,047 |
| Notable | Vietnam |  | 1.95% | 1.95% | 9,349 |
| Significant | Idelsk-Uralia | Russia | — | 1.91% | 9,171 |
| Notable | Philippines |  | 1.77% | 1.77% | 8,486 |
| Notable | Bulgaria |  | 1.45% | 1.45% | 6,951 |
| Significant | Siberia | Russia | — | 1.38% | 6,621 |
| Notable | Latvia |  | 1.35% | 1.35% | 6,472 |
| Notable | South Africa |  | 1.23% | 1.23% | 5,896 |
| Significant | Künnarantaiga | Russia | — | 0.67% | 3,228 |
| Significant | Donska-Kubania | Russia | — | 0.58% | 2,789 |
| | *8 smaller Russia successors* | Russia | — | 0.20% | 980 |

*Split today's: Russia 6.85% (after step 1 where it received fill).*

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

*Split today's: Russia 5.72% (after step 1 where it received fill).*

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

*Split today's: USA 21.65%, Mexico 11.28%, Russia 6.12%, Argentina 4.26% (after step 1 where it received fill).*

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

*Split today's: USA 36.36%, Mexico 17.45%, Argentina 8.35% (after step 1 where it received fill).*

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

*Split today's: USA 27.59%, Mexico 14.10%, Canada 7.21%, Argentina 0.74% (after step 1 where it received fill).*

#### Palmer City

*draw 0.6378; fill to: Brazil, France, Germany, Mexico, Canada, UK*

| Tier today | Row | From | Before | After | Census I humans after |
|---|---|---|--:|--:|--:|
| Significant | Brazil |  | 9.68% | 9.76% | 16,189 |
| Significant | France |  | 9.54% | 9.62% | 15,957 |
| Significant | Germany |  | 9.51% | 9.59% | 15,905 |
| Primary | CSA | USA | — | 5.87% | 9,733 |
| Significant | UK |  | 5.54% | 5.59% | 9,269 |
| Primary | Cascadia | USA + Mexico + Canada | — | 4.69% | 7,789 |
| Significant | México | Mexico | — | 4.59% | 7,616 |
| Primary | Appalachia | USA | — | 3.99% | 6,613 |
| Primary | New England | USA | — | 3.96% | 6,568 |
| Notable | Uruguay |  | 3.70% | 3.70% | 6,141 |
| Notable | Argentina (without Patagonia) | Argentina | — | 2.74% | 4,552 |
| Significant | Demilitarized Zone (s. Ontario; not a nation) | Canada | — | 2.09% | 3,472 |
| Significant | Quebec | Canada | — | 1.45% | 2,398 |
| Notable | Estonia |  | 1.39% | 1.39% | 2,312 |
| Significant | Prairie Federation | Canada | — | 1.37% | 2,281 |
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
| Primary | Sonora | USA + Mexico | — | 0.90% | 1,486 |
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
| Significant | Yucatán | Mexico | — | 0.51% | 850 |
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

*Split today's: USA 20.29%, Mexico 5.71%, Canada 5.68%, Argentina 3.05%, Russia 1.20% (after step 1 where it received fill).*

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

*Split today's: USA 29.63%, Argentina 5.04%, Mexico 2.65% (after step 1 where it received fill).*

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

*Split today's: USA 32.00%, Mexico 4.46%, Argentina 2.26% (after step 1 where it received fill).*

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

*Split today's: USA 28.57%, Canada 14.30%, Mexico 7.13%, Argentina 1.91% (after step 1 where it received fill).*

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

*Split today's: USA 33.33%, Argentina 6.08% (after step 1 where it received fill).*

*Every row, every census column: `09_city_tables.csv`.*
