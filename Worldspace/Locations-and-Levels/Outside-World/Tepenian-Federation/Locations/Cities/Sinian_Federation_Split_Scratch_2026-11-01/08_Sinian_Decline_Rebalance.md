# The Sinian Federation's decline and the city rebalance: overnight scratch run (2026-11-01, ~23:00 onward)

**Scratch, not canon, not a ruling.** At the developer's instruction, **no official file was changed**: no spec,
census entry, composition file, datasheet or Register row. Figures come from `calc_rebalance.py` (read-only on
the specs, the census and the composition file); the full count tables for every census column are in
`08_rebalance_city_tables.csv`; the script's whole output is the appendix at the end of this file. Rerun the
script after any change; the random draws are seeded, so a rerun gives the same numbers.

## What was asked

The developer, ~22:50, leaving the session in auto mode for the night:

> *"For the rest of the night, on the various scratch files, (don't write this to the official files, just use the
> scratch files), see if you can calculate for the cities that have Chinese presence. First of all, start from the
> figure that you had initially calculated of what the Sinian population would be after having lost the lands
> that were part of current-day China. Then, for the Sinian Federation's resulting population and its effects upon
> the relevantly-affected Tepenian cities, (with the exceptions of Zhongshan and Kunlun), use a randomly generated
> value of the resulting numerical population being anywhere between 55 to 60% of what it currently is. Then, in
> order to make up for the difference, whatever populations are currently lesser-represented, but also above 5% of
> a particular city's population, balance out those populations to fill the numbers back to what the city's total
> population had previously been. Once that's done, let's see what the numbers actually look like, and see if they
> are adjustments that can be reasonably, justifiably made."*

## How the instruction was carried out (each choice can be reversed by changing one line of the script)

1. **The territorial step.** China's row becomes the Sinian Federation's share of it: **91.56%**, the Sinian
   Federation's share of China's economy (`03_Results.md`, Option B, the one Claude recommended; the developer has
   not chosen yet). With Option A (headcount, 89.42%) every Sinian figure below would be 2.3% smaller in relative
   terms (for example Mirny 12.34% → 12.05%); nothing changes in kind.
2. **The 55–60%.** One random draw per city, uniform between 0.55 and 0.60, seeded (20261101). The draws ran from
   0.5501 (Casey) to 0.5982 (Denison). With the territorial step, each city's China figure is multiplied by
   0.504–0.548, so the Sinian Federation lands at about **half of China's old figure** in every city.
3. **"Lesser-represented, but also above 5%."** Read as: **at least 5.00% of the city, and not in the city's top
   tier.** The literal alternative, "below China's share and at least 5%", fails in two ways: in Byrd, Palmer City,
   Shirayuki and Concordia, where China is small, nobody qualifies; and in Dumont d'Urville, Zukelli and Janbogo it
   would hand part of the gap to the USA, the city's other top-tier nation, making the USA the new dominant one.
   Each city's section in the appendix says where the literal reading would differ.
4. **"Balance out."** The gap is split **evenly** among the qualifying nations (the headline; the project's own
   precedent, as in the Santa Luce redistribution and Zhongshan's rounds). A **proportional** split (each in
   proportion to its present size) is shown beside it in every table.
5. **The pieces that left China** (Manchuria, East Turkestan, Tibet, Inner Mongolia) get no rows here; their part of
   China's old figure is inside the gap that gets filled. *(Decision 3 in `03` is still open; if they become rows,
   Manchuria would be about 1–2% in these cities and the fill correspondingly smaller.)*
6. **Totals.** Every city keeps its exact total in every census column (Census I and II, robots and humans); the
   script checks this and it holds in all 20 cities. Tepenia's total does not change.
7. **Concordia** has no nation outside its top tier that reaches 5%, so its gap goes back to its other five
   top-tier nations (marked FALLBACK). See the verdicts.

## Results at a glance (even fill)

| City | China before | Sinian after | Leader before | Leader after | Lead after (1st ÷ 2nd) | Founders: before → after |
|---|--:|--:|---|---|--:|---|
| Dumont d'Urville | 24.31% | 13.06% | Sinian Fed. 24.31% | USA 20.13% | 1.38 | Japan 11.72 → 14.53 |
| Mirny | 24.24% | 12.34% | Sinian Fed. 24.24% | UK 14.33% | 1.05 | (Idelsk-Uralia, no row) |
| Zukelli | 22.63% | 11.80% | Sinian Fed. 22.63% | USA 19.47% | 1.47 | Australia 9.55 → 11.72 |
| Relung Panen | 21.58% | 11.55% | Sinian Fed. 21.58% | Russia 14.27% | 1.03 | Indonesia 12.23 → 13.90; Malaysia 3.30 → 3.30 |
| Janbogo | 20.63% | 10.44% | Sinian Fed. 20.63% | USA 18.39% | 1.44 | South Korea 10.23 → 12.78 |
| Davis | 19.04% | 9.78% | Sinian Fed. 19.04% | Japan 10.90% | 1.02 | Australia 4.93 → 4.93 |
| Temirötkel | 17.39% | 9.02% | Sinian Fed. 17.39% | Indonesia 10.26% | 1.03 | (Kazakhstan, no row); (the CIN members, all Notable) |
| Mawson | 17.02% | 8.68% | Sinian Fed. 17.02% | UK 10.66% | 1.07 | Australia 8.29 → 9.96; (Kazakhstan, no row); (Russia, no row) |
| Denison | 22.29% | 12.21% | USA 26.19% | USA 26.19% | 1.77 | Australia 5.87 → 8.39 |
| Cape Adare | 19.85% | 10.75% | USA 22.26% | USA 22.26% | 1.81 | — |
| Scott | 19.48% | 10.56% | USA 22.62% | USA 22.62% | 1.80 | New Zealand 3.52 → 3.52 |
| Fort McMurdo | 19.34% | 9.82% | USA 21.69% | USA 21.69% | 1.59 | — |
| Amundsen Station | 19.31% | 10.53% | USA 22.80% | USA 22.80% | 1.89 | — |
| Casey | 19.06% | 9.60% | USA 21.96% | USA 21.96% | 1.78 | Australia 9.26 → 11.15 |
| Dome Fuji | 10.13% | 5.11% | USA 11.20% | USA 11.20% | 1.56 | — |
| Sinheung | 9.74% | 5.08% | South Korea 34.62% | South Korea 34.62% | 3.40 | South Korea 34.62 → 34.62 |
| Concordia | 7.70% | 4.05% | Japan 9.32% | Japan 10.05% | 1.00 | — |
| Shirayuki | 7.18% | 3.92% | Japan 36.27% | Japan 36.27% | 3.68 | Japan 36.27 → 36.27 |
| Byrd | 2.95% | 1.58% | USA 13.57% | USA 13.57% | 1.19 | — |
| Palmer City | 0.91% | 0.49% | USA 20.29% | USA 20.29% | 2.08 | — |

*Founders are the Founding Register's. "No row" means the founder has no line in the city's population table today.*

**Nationally (Census I humans):** the Sinian Federation falls from **1,660,450 (10.6%)** to **965,841 (6.2%)**,
of whom 208,145 are Zhongshan's (unchanged). The largest gains: **Australia +122,747, South Korea +112,577,
Japan +108,168, Indonesia +106,983**, then Russia +61,417, the UK +50,953, France +38,977, Italy +30,638, Canada
+28,863, Germany +25,082. After the run, Japan (1,061,878) and South Korea (1,005,079) both pass the Sinian
Federation nationally; the USA (2,462,596, unchanged) is about 2.5 times it. Full table in the appendix.

## Can these adjustments be reasonably and justifiably made?

### What supports them

- **The premise is realistic, even conservative.** The UN's 2024 medium projection has China at about 633–639
  million by 2100, roughly 45% of today, only 75 years out (`07` file, sources there). Here the Sinian Federation
  ends at 55–60% of its own population, about 50–55% of old China's.
- **Fewer people means fewer emigrants, if anything more than in proportion.** Migration peaks in early adulthood
  (the Rogers–Castro age schedule puts the peak in the early-to-mid twenties), and a shrinking population is an
  aging one. Hatton and Williamson (2009), as summarized by Peri (2011): emigration rates from Asia and Latin
  America fell in the 2000s mainly for demographic reasons; *"As smaller cohorts reached their working age and
  larger cohorts got older, net emigration rates declined."*
- **Newcomers follow established communities, which is what the 5% line encodes.** Beine, Docquier and Özden
  (2011): *"the overall network externality is strong: the elasticity of migration flows to network size is around
  one."* Peri (2011): *"previous migrants attract new migrants via network and family effects."* So when fewer
  Sinian emigrants come, the places they would have taken going to the communities already established in the
  city is the expected real-world pattern.
- **It fits how the census sets city sizes.** City totals in this project are set by the city (island caps, extent
  and density work, held overflow), not by any one nation's supply. Keeping each city's total and changing who
  fills it is consistent with that.
- **It does what the developer asked for in the cities China led.** In the eight China-led cities the top four or
  five nations end within a few points of each other. Mirny: UK 14.3%, South Korea 13.6%, Indonesia 12.9%, the
  Sinian Federation 12.3%. Davis: Japan 10.9%, Germany 10.7%, the UK 10.2%, the Sinian Federation 9.8%. That is
  "generally multicultural" without being equal.

### What does not hold up as it stands, or needs a decision

1. **In the nine China-and-USA cities the USA becomes the single leader** (1.4–1.9 times the next nation:
   Dumont d'Urville, Zukelli, Janbogo, Denison, Cape Adare, Scott, Fort McMurdo, Amundsen Station, Casey). That
   trades one dominant nation for another. **Cape Adare** is the sharpest case: the Register rules it *"Mixed; no
   single dominant national community."* **What resolves it is the USA split:** if the USA's row is also split
   among its successors (illustration in the appendix: every successor in proportion to its pool, no time-zone
   window), all nine cities go flat, with the leader at most 1.12 times the next and the largest American
   successor (the CSA) at about 5.3–7.6%. **So these nine cities are only reasonable if the decline and the USA
   split are applied together.**
2. **The 5% line splits tier-mates on de-stacking noise.** Thirteen nations in twelve cities sit between 4.5% and
   5%, mostly middle-tier nations that are below 5% only because the de-stacking randomizer put them there (for
   example Casey's Indonesia at 4.92% next to tier-mate Japan at 5.33%). The worst case: **Davis's founder,
   Australia, at 4.93%, gets nothing** while Indonesia at 5.14% gets a share. The developer's own wording on
   2026-10-31 was *"about 5% or MORE."* **Recommendation: put the line at 4.5%.** The variant table in the
   appendix shows it: each borderline nation lands at about 5.7–7.3%, and the other recipients give up 0.2–0.8
   points each.
3. **The national gains go mostly to nations with their own reasons not to grow.**
   - **Australia gains the most (+122,747).** It is already about 2.8 times what its pool alone would supply
     (its ratio to 2% of its pool), rising to 3.3. The Register's Denison and Zukelli rows record the developer's
     thought that *"Australia is heavily represented"* (`FQ-20`). The fill works against that.
   - **Japan (+108,168) and South Korea (+112,577)** face the same demographic decline as China, faster in South
     Korea's case: the UN's 2024 medium projection has South Korea at about 22 million by 2100 (−57%) and Japan at
     about 77 million (−38%). Growing both by over 100,000 because China's population fell is inconsistent unless
     the setting gives them a different history. *(This is the same question raised in `07`, point 4.)*
   - Indonesia (+106,983) rises from about 1.9 to 2.2 times its pool figure.
   - None of this breaks the arithmetic; it is a question of who the setting wants the newcomers to be.
4. **Founders below the line, or with no row, get nothing.** Scott's founder New Zealand stays at 3.52% and
   Relung Panen's co-founder Malaysia at 3.30% while other nations grow. Temirötkel's founder Kazakhstan, and
   Mawson's Kazakhstan and Russia, have no row at all (Mawson's is already open as population item 13). Mirny's
   founder Idelsk-Uralia has no row either, though Russia, which it comes from, gains. **Zukelli's Italy grows
   from 6.24% to 8.41%**, while ledger item ZK-S05 already questions Italy at that level in an Australian-founded
   city.
5. **The tier method no longer produces these tables.** In the China-led cities no nation keeps an eight-share
   lead; the Sinian Federation sits among the middle-tier nations. The tables become hand-set, like Zhongshan's,
   Sinheung's, Shirayuki's and Kunlun's, and the tier labels (Primary, Significant, Notable) would need
   reassigning city by city. The composition file's description of the 8/3/1 method would need a note saying
   which cities depart from it and why.
6. **Five cities are better left for later, or follow something else:**
   - **Concordia:** China is sixth of 38 (7.70%), one of six nearly equal top-tier nations, so the city is already
     multicultural. Nobody outside its top tier reaches 5%, so the gap goes back to the other five top-tier
     nations, which changes nothing about the mix. And **its 13 finished district passes were built on this
     composition.** Recommendation: leave it until the district work is revisited.
   - **Dome Fuji:** all robots, whose national origin is *"preserved from source cities."* Its figures should
     follow whatever its source cities become, not take a draw of their own.
   - **Relung Panen:** its composition is held for the population work (population item 12); do it then.
   - **Amundsen Station:** it is being redesigned as a proper town (developer decision, 2026-10-31); its
     composition will be redone there.
   - **Palmer City:** China's 0.91% came from the random-percentage expansion, not from the pool. The change is
     about 700 people; harmless either way.

### Verdict by city

| City | Verdict | Why |
|---|---|---|
| Mirny | **Reasonable** | Four nations within 2 points at the top; founder's predecessor Russia gains |
| Davis | **Reasonable with the 4.5% line** | Otherwise its founder, Australia, is passed over at 4.93% |
| Temirötkel | **Reasonable, together with the founders fix** | Its founder Kazakhstan has no row |
| Mawson | **Reasonable, together with the founders fix** | Kazakhstan and Russia have no row (population item 13) |
| Dumont d'Urville | **Reasonable only with the USA split** | Alone, the USA leads 1.38×; its founder Japan gains |
| Zukelli | **Reasonable only with the USA split**; check Italy | Alone, the USA leads 1.47×; Italy grows against ZK-S05 |
| Janbogo | **Reasonable only with the USA split** | Alone, the USA leads 1.44×; its founder South Korea gains |
| Denison | **Reasonable only with the USA split** | Alone, the USA leads 1.77× |
| Cape Adare | **Only with the USA split** | Alone, it contradicts its "no single dominant community" ruling |
| Scott | **Reasonable only with the USA split** | Alone, the USA leads 1.80×; founder New Zealand stays at 3.52% |
| Fort McMurdo | **Reasonable only with the USA split** | Alone, the USA leads 1.59× |
| Casey | **Reasonable only with the USA split**, with the 4.5% line | Alone, the USA leads 1.78×; Indonesia at 4.92% |
| Sinheung | **Reasonable, small** | Follows from the premise alone (−4.66 points); goes to its middle tier |
| Shirayuki | **Reasonable, small** | Follows from the premise alone (−3.26 points); goes to its middle tier |
| Byrd | **Reasonable, small** | −1.37 points to Australia and Japan; its composition is also open (population item 9) |
| Palmer City | **Harmless either way** | About 700 people; China's row was randomly assigned |
| Relung Panen | **Later** | Composition held (population item 12) |
| Amundsen Station | **Later** | Town redesign |
| Dome Fuji | **Follow its source cities** | Robots with origins carried from other cities |
| Concordia | **Leave for now** | Already multicultural; 13 finished district passes rest on it |

### The one-paragraph answer

**Yes, with conditions.** The decline itself is realistic and the real-world evidence supports both halves of the
mechanism (fewer emigrants from an aging, shrinking country; newcomers following established communities). As run
tonight it does what was wanted in the eight China-led cities. But in the nine cities China shared with the USA it
only works together with the USA split; the 5% line should be "about 5%" (4.5%) so that tier-mates and Davis's
founder are not split by de-stacking noise; and who receives the newcomers needs a look, because the largest
national gains go to Australia (already flagged as over-represented) and to Japan and South Korea (which face the
same demographic decline). Concordia, Dome Fuji, Relung Panen and Amundsen Station should wait. On the evidence,
a **proportional** fill fits the network research better than an even one; an even fill fits the multicultural
aim better. The difference is under about 1.3 points per nation in every city (both are in every table).

## Decisions this hands to the developer

1. Even or proportional fill.
2. The line at 5% or at 4.5%.
3. Apply the decline and the USA split together in the nine China-and-USA cities, or not at all there.
4. Whether Japan and South Korea (and any other low-birth-rate nation) take a decline of their own, and whether
   Australia should be among the receivers.
5. Founders with no row (Kazakhstan at Temirötkel and Mawson, Russia at Mawson, Idelsk-Uralia at Mirny) and
   founders below the line (New Zealand at Scott, Malaysia at Relung Panen).
6. Whether Concordia, Dome Fuji, Relung Panen and Amundsen Station wait, as recommended.
7. Still open from before: Option A or B for the territorial step, and whether the pieces that left China get rows.

## Sources and search log (this session)

| # | Search or page | Result |
|--:|---|---|
| 1 | `UN World Population Prospects 2024 China population projection 2100 medium variant` | China about 633–639 million in 2100 (secondary sources; used in `07`) |
| 2 | `World Population Prospects 2024 South Korea Japan population 2100 projection` | South Korea about 22 million, Japan about 77 million in 2100 (secondary) |
| 3 | `Beine Docquier Özden diasporas network effects migration Journal of Development Economics 2011 findings` | "Diasporas", *J. Dev. Econ.* 95 (2011) 30–41: diasporas increase flows and explain most of their variability (abstract via search results) |
| 4 | `migration age schedule Rogers Castro peak migration young adults ages 20-30 model` | Peak in early adulthood, about ages 20–22 in the standard schedule (IIASA RR-84-03 and later) |
| 5 | `population aging reduces emigration rates demographic decline fewer young adults emigrants evidence` | Led to Peri (2011) below; no direct panel test found (dead end at the sources for a direct test) |
| — | Fetched: Beine, Docquier and Özden, "Dissecting Network Externalities in International Migration", CESifo Working Paper 3333 (January 2011), https://www.ifo.de/DocDL/cesifo1_wp3333.pdf | Abstract read in full (quoted above). The first fetch hit a redirect from cesifo.org; followed |
| — | Fetched: Giovanni Peri, "Immigration and Europe's Demographic Problems: Analysis and Policy Considerations", CESifo DICE Report 4/2011, https://www.ifo.de/DocDL/dicereport411-forum1.pdf | Hatton and Williamson passage read in full (quoted above) |

Five searches, none refused. The UN's own data portal was not opened; the population projections are from
secondary sites (listed in `07`).

---

## Appendix: the script's full output

*Pasted from `python3 calc_rebalance.py`, unedited. Tables: the random draws; every city, nation by nation (shares
before, after with an even fill, the change, after with a proportional fill, and Census I humans); the summary; the
national table; the 4.5% variant; the USA-split illustration. ★ marks the nations that receive the fill.*

### Random draws (seed 20261101, uniform 0.55-0.60, one per city, in table order)

| City | Draw | Sinian factor (0.9156 x draw) | Option A check (0.8942 x draw) |
|---|--:|--:|--:|
| Dumont d'Urville | 0.5868 | 0.5373 | 0.5247 |
| Mirny | 0.5558 | 0.5089 | 0.4970 |
| Zukelli | 0.5697 | 0.5216 | 0.5094 |
| Relung Panen | 0.5848 | 0.5354 | 0.5229 |
| Janbogo | 0.5525 | 0.5059 | 0.4941 |
| Davis | 0.5610 | 0.5136 | 0.5016 |
| Temirötkel | 0.5665 | 0.5187 | 0.5065 |
| Mawson | 0.5571 | 0.5101 | 0.4981 |
| Denison | 0.5982 | 0.5478 | 0.5349 |
| Cape Adare | 0.5916 | 0.5417 | 0.5290 |
| Scott | 0.5919 | 0.5419 | 0.5292 |
| Fort McMurdo | 0.5545 | 0.5078 | 0.4959 |
| Amundsen Station | 0.5955 | 0.5453 | 0.5325 |
| Casey | 0.5501 | 0.5037 | 0.4919 |
| Dome Fuji | 0.5513 | 0.5048 | 0.4930 |
| Sinheung | 0.5694 | 0.5214 | 0.5091 |
| Concordia | 0.5748 | 0.5263 | 0.5140 |
| Shirayuki | 0.5963 | 0.5460 | 0.5332 |
| Byrd | 0.5842 | 0.5349 | 0.5224 |
| Palmer City | 0.5939 | 0.5438 | 0.5310 |

### City by city (shares; headline = even fill)

#### Dumont d'Urville

*draw 0.5868 · Sinian factor 0.5373 · fill goes to: France, Japan, Australia, Indonesia · literal reading (below China and at least 5%) would give: USA, France, Japan, Australia, Indonesia*

| Tier today | Nation | Before | After (even) | Change | After (proportional) | Census I humans before | after (even) |
|---|---|--:|--:|--:|--:|--:|--:|
| Primary | USA | 20.13% | 20.13% | +0.00 | 20.13% | 40,500 | 40,500 |
| Significant | France ★ | 11.80% | 14.61% | +2.81 | 15.10% | 23,734 | 29,393 |
| Significant | Japan ★ | 11.72% | 14.53% | +2.81 | 15.00% | 23,584 | 29,243 |
| Significant | Australia ★ | 11.08% | 13.89% | +2.81 | 14.18% | 22,285 | 27,943 |
| Primary | Sinian Federation (was China) | 24.31% | 13.06% | -11.25 | 13.06% | 48,919 | 26,285 |
| Significant | Indonesia ★ | 5.59% | 8.40% | +2.81 | 7.15% | 11,247 | 16,905 |
| Notable | New Zealand | 4.16% | 4.16% | +0.00 | 4.16% | 8,361 | 8,361 |
| Notable | Vietnam | 4.04% | 4.04% | +0.00 | 4.04% | 8,128 | 8,128 |
| Notable | Philippines | 3.40% | 3.40% | +0.00 | 3.40% | 6,839 | 6,839 |
| Notable | Malaysia | 2.16% | 2.16% | +0.00 | 2.16% | 4,339 | 4,339 |
| Significant | South Korea | 1.48% | 1.48% | +0.00 | 1.48% | 2,980 | 2,980 |
| Notable | Thailand | 0.14% | 0.14% | +0.00 | 0.14% | 278 | 278 |

*Column totals unchanged: yes.  ★ = receives the fill.*

#### Mirny

*draw 0.5558 · Sinian factor 0.5089 · fill goes to: UK, South Korea, Indonesia, Russia, Japan, Australia · just under the line, so left as is: Philippines 4.50%*

| Tier today | Nation | Before | After (even) | Change | After (proportional) | Census I humans before | after (even) |
|---|---|--:|--:|--:|--:|--:|--:|
| Significant | UK ★ | 12.35% | 14.33% | +1.98 | 15.05% | 83,739 | 97,193 |
| Significant | South Korea ★ | 11.64% | 13.62% | +1.98 | 14.18% | 78,940 | 92,394 |
| Significant | Indonesia ★ | 10.96% | 12.94% | +1.98 | 13.35% | 74,293 | 87,747 |
| Primary | Sinian Federation (was China) | 24.24% | 12.34% | -11.90 | 12.34% | 164,374 | 83,651 |
| Significant | Russia ★ | 7.22% | 9.20% | +1.98 | 8.80% | 48,987 | 62,441 |
| Significant | Japan ★ | 6.54% | 8.52% | +1.98 | 7.97% | 44,340 | 57,794 |
| Significant | Australia ★ | 5.83% | 7.81% | +1.98 | 7.10% | 39,541 | 52,994 |
| Notable | Philippines | 4.50% | 4.50% | +0.00 | 4.50% | 30,536 | 30,536 |
| Notable | New Zealand | 4.48% | 4.48% | +0.00 | 4.48% | 30,374 | 30,374 |
| Notable | Thailand | 3.70% | 3.70% | +0.00 | 3.70% | 25,055 | 25,055 |
| Notable | Malaysia | 3.65% | 3.65% | +0.00 | 3.65% | 24,723 | 24,723 |
| Notable | Vietnam | 1.75% | 1.75% | +0.00 | 1.75% | 11,863 | 11,863 |
| Notable | Belarus | 1.58% | 1.58% | +0.00 | 1.58% | 10,719 | 10,719 |
| Notable | South Africa | 1.56% | 1.56% | +0.00 | 1.56% | 10,557 | 10,557 |

*Column totals unchanged: yes.  ★ = receives the fill.*

#### Zukelli

*draw 0.5697 · Sinian factor 0.5216 · fill goes to: South Korea, Canada, Australia, Italy, Indonesia · literal reading (below China and at least 5%) would give: USA, South Korea, Canada, Australia, Italy, Indonesia · just under the line, so left as is: Japan 4.69%*

| Tier today | Nation | Before | After (even) | Change | After (proportional) | Census I humans before | after (even) |
|---|---|--:|--:|--:|--:|--:|--:|
| Primary | USA | 19.47% | 19.47% | +0.00 | 19.47% | 124,570 | 124,570 |
| Significant | South Korea ★ | 11.10% | 13.27% | +2.17 | 13.92% | 71,022 | 84,874 |
| Significant | Canada ★ | 9.90% | 12.07% | +2.17 | 12.41% | 63,330 | 77,182 |
| Primary | Sinian Federation (was China) | 22.63% | 11.80% | -10.83 | 11.80% | 144,788 | 75,528 |
| Significant | Australia ★ | 9.55% | 11.72% | +2.17 | 11.97% | 61,117 | 74,969 |
| Significant | Italy ★ | 6.24% | 8.41% | +2.17 | 7.82% | 39,891 | 53,743 |
| Significant | Indonesia ★ | 5.89% | 8.06% | +2.17 | 7.38% | 37,680 | 51,532 |
| Significant | Japan | 4.69% | 4.69% | +0.00 | 4.69% | 29,987 | 29,987 |
| Notable | Malaysia | 3.44% | 3.44% | +0.00 | 3.44% | 22,014 | 22,014 |
| Notable | New Zealand | 3.37% | 3.37% | +0.00 | 3.37% | 21,574 | 21,574 |
| Notable | Philippines | 1.89% | 1.89% | +0.00 | 1.89% | 12,095 | 12,095 |
| Notable | Chile | 1.82% | 1.82% | +0.00 | 1.82% | 11,655 | 11,655 |

*Column totals unchanged: yes.  ★ = receives the fill.*

#### Relung Panen

*draw 0.5848 · Sinian factor 0.5354 · fill goes to: Russia, Indonesia, Japan, South Korea, Australia, Thailand · just under the line, so left as is: Vietnam 4.76%*

| Tier today | Nation | Before | After (even) | Change | After (proportional) | Census I humans before | after (even) |
|---|---|--:|--:|--:|--:|--:|--:|
| Significant | Russia ★ | 12.60% | 14.27% | +1.67 | 14.57% | 60,138 | 68,113 |
| Significant | Indonesia ★ | 12.23% | 13.90% | +1.67 | 14.14% | 58,371 | 66,346 |
| Significant | Japan ★ | 11.98% | 13.65% | +1.67 | 13.85% | 57,179 | 65,154 |
| Significant | South Korea ★ | 11.22% | 12.89% | +1.67 | 12.97% | 53,551 | 61,526 |
| Significant | Australia ★ | 11.03% | 12.70% | +1.67 | 12.75% | 52,645 | 60,620 |
| Primary | Sinian Federation (was China) | 21.58% | 11.55% | -10.03 | 11.55% | 102,997 | 55,148 |
| Notable | Thailand ★ | 5.15% | 6.82% | +1.67 | 5.95% | 24,580 | 32,554 |
| Notable | Vietnam | 4.76% | 4.76% | +0.00 | 4.76% | 22,719 | 22,719 |
| Notable | Malaysia | 3.30% | 3.30% | +0.00 | 3.30% | 15,751 | 15,751 |
| Notable | Philippines | 3.18% | 3.18% | +0.00 | 3.18% | 15,178 | 15,178 |
| Notable | New Zealand | 2.97% | 2.97% | +0.00 | 2.97% | 14,176 | 14,176 |

*Column totals unchanged: yes.  ★ = receives the fill.*

#### Janbogo

*draw 0.5525 · Sinian factor 0.5059 · fill goes to: South Korea, Australia, Italy, Indonesia · literal reading (below China and at least 5%) would give: USA, South Korea, Australia, Italy, Indonesia · just under the line, so left as is: Germany 4.64%*

| Tier today | Nation | Before | After (even) | Change | After (proportional) | Census I humans before | after (even) |
|---|---|--:|--:|--:|--:|--:|--:|
| Primary | USA | 18.39% | 18.39% | +0.00 | 18.39% | 121,153 | 121,153 |
| Significant | South Korea ★ | 10.23% | 12.78% | +2.55 | 12.96% | 67,370 | 84,156 |
| Significant | Australia ★ | 9.99% | 12.54% | +2.55 | 12.65% | 65,809 | 82,595 |
| Significant | Italy ★ | 9.14% | 11.69% | +2.55 | 11.58% | 60,174 | 76,960 |
| Significant | Indonesia ★ | 8.88% | 11.43% | +2.55 | 11.25% | 58,479 | 75,264 |
| Primary | Sinian Federation (was China) | 20.63% | 10.44% | -10.19 | 10.44% | 135,893 | 68,750 |
| Significant | Germany | 4.64% | 4.64% | +0.00 | 4.64% | 30,582 | 30,582 |
| Significant | Japan | 4.41% | 4.41% | +0.00 | 4.41% | 29,022 | 29,022 |
| Significant | Canada | 3.94% | 3.94% | +0.00 | 3.94% | 25,936 | 25,936 |
| Notable | Chile | 3.22% | 3.22% | +0.00 | 3.22% | 21,178 | 21,178 |
| Notable | Malaysia | 3.13% | 3.13% | +0.00 | 3.13% | 20,638 | 20,638 |
| Notable | Philippines | 1.74% | 1.74% | +0.00 | 1.74% | 11,493 | 11,493 |
| Notable | New Zealand | 1.66% | 1.66% | +0.00 | 1.66% | 10,953 | 10,953 |

*Column totals unchanged: yes.  ★ = receives the fill.*

#### Davis

*draw 0.5610 · Sinian factor 0.5136 · fill goes to: Japan, Germany, UK, South Korea, Russia, Indonesia · just under the line, so left as is: Australia 4.93%*

| Tier today | Nation | Before | After (even) | Change | After (proportional) | Census I humans before | after (even) |
|---|---|--:|--:|--:|--:|--:|--:|
| Significant | Japan ★ | 9.36% | 10.90% | +1.54 | 11.28% | 53,889 | 62,775 |
| Significant | Germany ★ | 9.15% | 10.69% | +1.54 | 11.03% | 52,680 | 61,566 |
| Significant | UK ★ | 8.65% | 10.19% | +1.54 | 10.43% | 49,801 | 58,687 |
| Primary | Sinian Federation (was China) | 19.04% | 9.78% | -9.26 | 9.78% | 109,620 | 56,305 |
| Significant | South Korea ★ | 7.14% | 8.68% | +1.54 | 8.61% | 41,108 | 49,994 |
| Significant | Russia ★ | 5.64% | 7.18% | +1.54 | 6.80% | 32,472 | 41,358 |
| Significant | Indonesia ★ | 5.14% | 6.68% | +1.54 | 6.20% | 29,593 | 38,478 |
| Significant | Australia | 4.93% | 4.93% | +0.00 | 4.93% | 28,384 | 28,384 |
| Notable | Thailand | 3.52% | 3.52% | +0.00 | 3.52% | 20,266 | 20,266 |
| Notable | Ukraine | 3.51% | 3.51% | +0.00 | 3.51% | 20,208 | 20,208 |
| Notable | Vietnam | 3.29% | 3.29% | +0.00 | 3.29% | 18,941 | 18,941 |
| Notable | Philippines | 3.25% | 3.25% | +0.00 | 3.25% | 18,712 | 18,712 |
| Notable | Malaysia | 3.13% | 3.13% | +0.00 | 3.13% | 18,021 | 18,021 |
| Notable | Romania | 2.97% | 2.97% | +0.00 | 2.97% | 17,100 | 17,100 |
| Notable | South Africa | 2.92% | 2.92% | +0.00 | 2.92% | 16,811 | 16,811 |
| Notable | New Zealand | 1.79% | 1.79% | +0.00 | 1.79% | 10,305 | 10,305 |
| Notable | Belarus | 1.63% | 1.63% | +0.00 | 1.63% | 9,385 | 9,385 |
| Notable | Bulgaria | 1.51% | 1.51% | +0.00 | 1.51% | 8,693 | 8,693 |
| Notable | Lithuania | 1.25% | 1.25% | +0.00 | 1.25% | 7,197 | 7,197 |
| Notable | Estonia | 1.24% | 1.24% | +0.00 | 1.24% | 7,140 | 7,140 |
| Notable | Latvia | 0.94% | 0.94% | +0.00 | 0.94% | 5,412 | 5,412 |

*Column totals unchanged: yes.  ★ = receives the fill.*

#### Temirötkel

*draw 0.5665 · Sinian factor 0.5187 · fill goes to: Indonesia, Australia, Germany, UK, South Korea · just under the line, so left as is: France 4.82%*

| Tier today | Nation | Before | After (even) | Change | After (proportional) | Census I humans before | after (even) |
|---|---|--:|--:|--:|--:|--:|--:|
| Significant | Indonesia ★ | 8.59% | 10.26% | +1.67 | 10.48% | 8,018 | 9,581 |
| Significant | Australia ★ | 8.27% | 9.94% | +1.67 | 10.09% | 7,721 | 9,284 |
| Significant | Germany ★ | 8.22% | 9.89% | +1.67 | 10.02% | 7,673 | 9,236 |
| Significant | UK ★ | 7.97% | 9.64% | +1.67 | 9.72% | 7,444 | 9,007 |
| Primary | Sinian Federation (was China) | 17.39% | 9.02% | -8.37 | 9.02% | 16,236 | 8,421 |
| Significant | South Korea ★ | 5.07% | 6.74% | +1.67 | 6.18% | 4,733 | 6,296 |
| Significant | France | 4.82% | 4.82% | +0.00 | 4.82% | 4,504 | 4,504 |
| Notable | Serbia | 3.22% | 3.22% | +0.00 | 3.22% | 3,010 | 3,010 |
| Notable | Netherlands | 3.14% | 3.14% | +0.00 | 3.14% | 2,929 | 2,929 |
| Notable | Slovenia | 3.12% | 3.12% | +0.00 | 3.12% | 2,915 | 2,915 |
| Notable | Croatia | 3.11% | 3.11% | +0.00 | 3.11% | 2,900 | 2,900 |
| Notable | Romania | 2.81% | 2.81% | +0.00 | 2.81% | 2,621 | 2,621 |
| Notable | Lithuania | 2.81% | 2.81% | +0.00 | 2.81% | 2,625 | 2,625 |
| Notable | Norway | 2.80% | 2.80% | +0.00 | 2.80% | 2,615 | 2,615 |
| Notable | Belarus | 2.79% | 2.79% | +0.00 | 2.79% | 2,607 | 2,607 |
| Notable | Latvia | 2.76% | 2.76% | +0.00 | 2.76% | 2,576 | 2,576 |
| Significant | Japan | 2.71% | 2.71% | +0.00 | 2.71% | 2,527 | 2,527 |
| Notable | Czech Republic | 1.56% | 1.56% | +0.00 | 1.56% | 1,452 | 1,452 |
| Notable | Ukraine | 1.55% | 1.55% | +0.00 | 1.55% | 1,444 | 1,444 |
| Notable | Hungary | 1.54% | 1.54% | +0.00 | 1.54% | 1,438 | 1,438 |
| Notable | South Africa | 1.54% | 1.54% | +0.00 | 1.54% | 1,434 | 1,434 |
| Notable | Bulgaria | 1.24% | 1.24% | +0.00 | 1.24% | 1,159 | 1,159 |
| Notable | Poland | 1.23% | 1.23% | +0.00 | 1.23% | 1,144 | 1,144 |
| Notable | Estonia | 1.12% | 1.12% | +0.00 | 1.12% | 1,049 | 1,049 |
| Notable | Slovakia | 0.63% | 0.63% | +0.00 | 0.63% | 584 | 584 |

*Column totals unchanged: yes.  ★ = receives the fill.*

#### Mawson

*draw 0.5571 · Sinian factor 0.5101 · fill goes to: UK, Australia, Indonesia, Japan, France · just under the line, so left as is: South Korea 4.87%*

| Tier today | Nation | Before | After (even) | Change | After (proportional) | Census I humans before | after (even) |
|---|---|--:|--:|--:|--:|--:|--:|
| Significant | UK ★ | 8.99% | 10.66% | +1.67 | 10.97% | 64,921 | 76,960 |
| Significant | Australia ★ | 8.29% | 9.96% | +1.67 | 10.11% | 59,874 | 71,913 |
| Significant | Indonesia ★ | 7.89% | 9.56% | +1.67 | 9.62% | 56,985 | 69,024 |
| Significant | Japan ★ | 7.48% | 9.15% | +1.67 | 9.12% | 53,975 | 66,014 |
| Primary | Sinian Federation (was China) | 17.02% | 8.68% | -8.34 | 8.68% | 122,871 | 62,677 |
| Significant | France ★ | 5.29% | 6.96% | +1.67 | 6.45% | 38,179 | 50,217 |
| Significant | South Korea | 4.87% | 4.87% | +0.00 | 4.87% | 35,168 | 35,168 |
| Notable | Estonia | 3.17% | 3.17% | +0.00 | 3.17% | 22,899 | 22,899 |
| Notable | South Africa | 3.09% | 3.09% | +0.00 | 3.09% | 22,341 | 22,341 |
| Notable | Norway | 3.05% | 3.05% | +0.00 | 3.05% | 21,985 | 21,985 |
| Notable | Vietnam | 2.99% | 2.99% | +0.00 | 2.99% | 21,548 | 21,548 |
| Notable | Thailand | 2.97% | 2.97% | +0.00 | 2.97% | 21,442 | 21,442 |
| Notable | Belarus | 2.93% | 2.93% | +0.00 | 2.93% | 21,172 | 21,172 |
| Notable | Netherlands | 2.92% | 2.92% | +0.00 | 2.92% | 21,054 | 21,054 |
| Notable | Slovenia | 2.71% | 2.71% | +0.00 | 2.71% | 19,549 | 19,549 |
| Notable | Bulgaria | 2.68% | 2.68% | +0.00 | 2.68% | 19,356 | 19,356 |
| Significant | Germany | 1.86% | 1.86% | +0.00 | 1.86% | 13,436 | 13,436 |
| Notable | Czech Republic | 1.57% | 1.57% | +0.00 | 1.57% | 11,361 | 11,361 |
| Notable | Slovakia | 1.55% | 1.55% | +0.00 | 1.55% | 11,169 | 11,169 |
| Notable | Lithuania | 1.34% | 1.34% | +0.00 | 1.34% | 9,663 | 9,663 |
| Notable | Hungary | 1.32% | 1.32% | +0.00 | 1.32% | 9,546 | 9,546 |
| Notable | Romania | 1.28% | 1.28% | +0.00 | 1.28% | 9,276 | 9,276 |
| Notable | Poland | 1.27% | 1.27% | +0.00 | 1.27% | 9,170 | 9,170 |
| Notable | Croatia | 1.21% | 1.21% | +0.00 | 1.21% | 8,733 | 8,733 |
| Notable | Latvia | 1.16% | 1.16% | +0.00 | 1.16% | 8,377 | 8,377 |
| Notable | Ukraine | 1.08% | 1.08% | +0.00 | 1.08% | 7,819 | 7,819 |

*Column totals unchanged: yes.  ★ = receives the fill.*

#### Denison

*draw 0.5982 · Sinian factor 0.5478 · fill goes to: South Korea, Indonesia, Japan, Australia*

| Tier today | Nation | Before | After (even) | Change | After (proportional) | Census I humans before | after (even) |
|---|---|--:|--:|--:|--:|--:|--:|
| Primary | USA | 26.19% | 26.19% | +0.00 | 26.19% | 119,604 | 119,604 |
| Significant | South Korea ★ | 12.31% | 14.83% | +2.52 | 15.72% | 56,228 | 67,739 |
| Significant | Indonesia ★ | 10.77% | 13.29% | +2.52 | 13.76% | 49,206 | 60,717 |
| Primary | Sinian Federation (was China) | 22.29% | 12.21% | -10.08 | 12.21% | 101,810 | 55,767 |
| Significant | Japan ★ | 7.41% | 9.93% | +2.52 | 9.46% | 33,825 | 45,336 |
| Significant | Australia ★ | 5.87% | 8.39% | +2.52 | 7.50% | 26,803 | 38,313 |
| Notable | New Zealand | 3.92% | 3.92% | +0.00 | 3.92% | 17,910 | 17,910 |
| Notable | Vietnam | 3.72% | 3.72% | +0.00 | 3.72% | 16,974 | 16,974 |
| Notable | Philippines | 3.64% | 3.64% | +0.00 | 3.64% | 16,643 | 16,643 |
| Notable | Malaysia | 2.42% | 2.42% | +0.00 | 2.42% | 11,034 | 11,034 |
| Notable | Thailand | 1.45% | 1.45% | +0.00 | 1.45% | 6,631 | 6,631 |

*Column totals unchanged: yes.  ★ = receives the fill.*

#### Cape Adare

*draw 0.5916 · Sinian factor 0.5417 · fill goes to: Australia, Japan, Indonesia, Canada, South Korea, UK*

| Tier today | Nation | Before | After (even) | Change | After (proportional) | Census I humans before | after (even) |
|---|---|--:|--:|--:|--:|--:|--:|
| Primary | USA | 22.26% | 22.26% | +0.00 | 22.26% | 168,738 | 168,738 |
| Significant | Australia ★ | 10.76% | 12.28% | +1.52 | 12.83% | 81,557 | 93,050 |
| Significant | Japan ★ | 10.49% | 12.01% | +1.52 | 12.50% | 79,562 | 91,055 |
| Significant | Indonesia ★ | 9.28% | 10.80% | +1.52 | 11.06% | 70,343 | 81,835 |
| Primary | Sinian Federation (was China) | 19.85% | 10.75% | -9.10 | 10.75% | 150,466 | 81,512 |
| Significant | Canada ★ | 6.51% | 8.03% | +1.52 | 7.76% | 49,357 | 60,849 |
| Significant | South Korea ★ | 5.29% | 6.81% | +1.52 | 6.31% | 40,139 | 51,631 |
| Significant | UK ★ | 5.03% | 6.55% | +1.52 | 6.00% | 38,144 | 49,636 |
| Notable | Chile | 3.74% | 3.74% | +0.00 | 3.74% | 28,375 | 28,375 |
| Notable | New Zealand | 3.19% | 3.19% | +0.00 | 3.19% | 24,155 | 24,155 |
| Notable | Philippines | 2.08% | 2.08% | +0.00 | 2.08% | 15,745 | 15,745 |
| Notable | Malaysia | 1.52% | 1.52% | +0.00 | 1.52% | 11,526 | 11,526 |

*Column totals unchanged: yes.  ★ = receives the fill.*

#### Scott

*draw 0.5919 · Sinian factor 0.5419 · fill goes to: Japan, UK, Australia, South Korea, Canada · just under the line, so left as is: Indonesia 4.98%*

| Tier today | Nation | Before | After (even) | Change | After (proportional) | Census I humans before | after (even) |
|---|---|--:|--:|--:|--:|--:|--:|
| Primary | USA | 22.62% | 22.62% | +0.00 | 22.62% | 42,938 | 42,938 |
| Significant | Japan ★ | 10.81% | 12.59% | +1.78 | 13.09% | 20,519 | 23,908 |
| Significant | UK ★ | 10.79% | 12.57% | +1.78 | 13.06% | 20,489 | 23,877 |
| Significant | Australia ★ | 9.43% | 11.21% | +1.78 | 11.42% | 17,903 | 21,291 |
| Primary | Sinian Federation (was China) | 19.48% | 10.56% | -8.92 | 10.56% | 36,985 | 20,044 |
| Significant | South Korea ★ | 6.36% | 8.14% | +1.78 | 7.70% | 12,068 | 15,456 |
| Significant | Canada ★ | 5.00% | 6.78% | +1.78 | 6.05% | 9,482 | 12,870 |
| Significant | Indonesia | 4.98% | 4.98% | +0.00 | 4.98% | 9,452 | 9,452 |
| Notable | Chile | 3.69% | 3.69% | +0.00 | 3.69% | 6,996 | 6,996 |
| Notable | New Zealand | 3.52% | 3.52% | +0.00 | 3.52% | 6,687 | 6,687 |
| Notable | Malaysia | 1.74% | 1.74% | +0.00 | 1.74% | 3,303 | 3,303 |
| Notable | Philippines | 1.58% | 1.58% | +0.00 | 1.58% | 2,994 | 2,994 |

*Column totals unchanged: yes.  ★ = receives the fill.*

#### Fort McMurdo

*draw 0.5545 · Sinian factor 0.5078 · fill goes to: Germany, France, Japan · just under the line, so left as is: Italy 4.90%*

| Tier today | Nation | Before | After (even) | Change | After (proportional) | Census I humans before | after (even) |
|---|---|--:|--:|--:|--:|--:|--:|
| Primary | USA | 21.69% | 21.69% | +0.00 | 21.69% | 48,185 | 48,185 |
| Significant | Germany ★ | 10.49% | 13.66% | +3.17 | 13.90% | 23,299 | 30,350 |
| Significant | France ★ | 9.73% | 12.90% | +3.17 | 12.89% | 21,608 | 28,658 |
| Significant | Japan ★ | 9.08% | 12.25% | +3.17 | 12.03% | 20,186 | 27,236 |
| Primary | Sinian Federation (was China) | 19.34% | 9.82% | -9.52 | 9.82% | 42,970 | 21,819 |
| Significant | Italy | 4.90% | 4.90% | +0.00 | 4.90% | 10,884 | 10,884 |
| Significant | UK | 4.27% | 4.27% | +0.00 | 4.27% | 9,481 | 9,481 |
| Notable | Chile | 3.54% | 3.54% | +0.00 | 3.54% | 7,869 | 7,869 |
| Notable | Canada | 3.49% | 3.49% | +0.00 | 3.49% | 7,757 | 7,757 |
| Notable | Malaysia | 3.31% | 3.31% | +0.00 | 3.31% | 7,355 | 7,355 |
| Notable | New Zealand | 3.20% | 3.20% | +0.00 | 3.20% | 7,118 | 7,118 |
| Notable | Australia | 1.92% | 1.92% | +0.00 | 1.92% | 4,276 | 4,276 |
| Notable | Indonesia | 1.82% | 1.82% | +0.00 | 1.82% | 4,040 | 4,040 |
| Notable | South Korea | 1.64% | 1.64% | +0.00 | 1.64% | 3,637 | 3,637 |
| Notable | Philippines | 1.59% | 1.59% | +0.00 | 1.59% | 3,525 | 3,525 |

*Column totals unchanged: yes.  ★ = receives the fill.*

#### Amundsen Station

*draw 0.5955 · Sinian factor 0.5453 · fill goes to: UK, Germany, Japan, Canada, South Korea, Australia*

| Tier today | Nation | Before | After (even) | Change | After (proportional) | Census I humans before | after (even) |
|---|---|--:|--:|--:|--:|--:|--:|
| Primary | USA | 22.80% | 22.80% | +0.00 | 22.80% | 256 | 256 |
| Significant | UK ★ | 10.57% | 12.03% | +1.46 | 12.53% | 118 | 135 |
| Significant | Germany ★ | 10.09% | 11.55% | +1.46 | 11.96% | 113 | 130 |
| Significant | Japan ★ | 9.59% | 11.05% | +1.46 | 11.37% | 107 | 123 |
| Primary | Sinian Federation (was China) | 19.31% | 10.53% | -8.78 | 10.53% | 216 | 118 |
| Significant | Canada ★ | 6.20% | 7.66% | +1.46 | 7.35% | 70 | 86 |
| Significant | South Korea ★ | 5.70% | 7.16% | +1.46 | 6.76% | 64 | 80 |
| Significant | Australia ★ | 5.22% | 6.68% | +1.46 | 6.19% | 59 | 75 |
| Notable | Argentina | 3.59% | 3.59% | +0.00 | 3.59% | 40 | 40 |
| Notable | New Zealand | 3.59% | 3.59% | +0.00 | 3.59% | 40 | 40 |
| Notable | Norway | 1.67% | 1.67% | +0.00 | 1.67% | 19 | 19 |
| Notable | Chile | 1.67% | 1.67% | +0.00 | 1.67% | 19 | 19 |

*Column totals unchanged: yes.  ★ = receives the fill.*

#### Casey

*draw 0.5501 · Sinian factor 0.5037 · fill goes to: South Korea, France, Australia, Russia, Japan · just under the line, so left as is: Indonesia 4.92%*

| Tier today | Nation | Before | After (even) | Change | After (proportional) | Census I humans before | after (even) |
|---|---|--:|--:|--:|--:|--:|--:|
| Primary | USA | 21.96% | 21.96% | +0.00 | 21.96% | 163,832 | 163,832 |
| Significant | South Korea ★ | 10.46% | 12.35% | +1.89 | 12.86% | 78,047 | 92,162 |
| Significant | France ★ | 10.05% | 11.94% | +1.89 | 12.36% | 74,996 | 89,111 |
| Significant | Australia ★ | 9.26% | 11.15% | +1.89 | 11.38% | 69,047 | 83,162 |
| Primary | Sinian Federation (was China) | 19.06% | 9.60% | -9.46 | 9.60% | 142,192 | 71,617 |
| Significant | Russia ★ | 6.13% | 8.02% | +1.89 | 7.54% | 45,713 | 59,828 |
| Significant | Japan ★ | 5.33% | 7.22% | +1.89 | 6.55% | 39,763 | 53,878 |
| Significant | Indonesia | 4.92% | 4.92% | +0.00 | 4.92% | 36,712 | 36,712 |
| Notable | New Zealand | 3.36% | 3.36% | +0.00 | 3.36% | 25,040 | 25,040 |
| Notable | Philippines | 3.35% | 3.35% | +0.00 | 3.35% | 25,007 | 25,007 |
| Notable | Vietnam | 3.21% | 3.21% | +0.00 | 3.21% | 23,937 | 23,937 |
| Notable | Malaysia | 1.78% | 1.78% | +0.00 | 1.78% | 13,246 | 13,246 |
| Notable | Thailand | 1.13% | 1.13% | +0.00 | 1.13% | 8,403 | 8,403 |

*Column totals unchanged: yes.  ★ = receives the fill.*

#### Dome Fuji

*draw 0.5513 · Sinian factor 0.5048 · fill goes to: Indonesia, Australia, France · just under the line, so left as is: Germany 4.83%, South Korea 4.78%*

| Tier today | Nation | Before | After (even) | Change | After (proportional) |
|---|---|--:|--:|--:|--:|
| Primary | USA | 11.20% | 11.20% | +0.00 | 11.20% |
| Significant | Indonesia ★ | 5.51% | 7.18% | +1.67 | 7.27% |
| Significant | Australia ★ | 5.16% | 6.83% | +1.67 | 6.81% |
| Significant | France ★ | 5.00% | 6.67% | +1.67 | 6.60% |
| Primary | Sinian Federation (was China) | 10.13% | 5.11% | -5.02 | 5.11% |
| Significant | Germany | 4.83% | 4.83% | +0.00 | 4.83% |
| Significant | South Korea | 4.78% | 4.78% | +0.00 | 4.78% |
| Significant | Brazil | 3.17% | 3.17% | +0.00 | 3.17% |
| Significant | Japan | 2.84% | 2.84% | +0.00 | 2.84% |
| Significant | UK | 2.49% | 2.49% | +0.00 | 2.49% |
| Significant | Russia | 2.22% | 2.22% | +0.00 | 2.22% |
| Notable | Malaysia | 1.91% | 1.91% | +0.00 | 1.91% |
| Notable | Netherlands | 1.90% | 1.90% | +0.00 | 1.90% |
| Notable | Spain | 1.89% | 1.89% | +0.00 | 1.89% |
| Notable | Mexico | 1.89% | 1.89% | +0.00 | 1.89% |
| Notable | Slovenia | 1.87% | 1.87% | +0.00 | 1.87% |
| Notable | Belarus | 1.83% | 1.83% | +0.00 | 1.83% |
| Notable | Croatia | 1.82% | 1.82% | +0.00 | 1.82% |
| Notable | Romania | 1.82% | 1.82% | +0.00 | 1.82% |
| Notable | Hungary | 1.81% | 1.81% | +0.00 | 1.81% |
| Notable | Czech Republic | 1.74% | 1.74% | +0.00 | 1.74% |
| Notable | Latvia | 1.73% | 1.73% | +0.00 | 1.73% |
| Notable | Canada | 1.73% | 1.73% | +0.00 | 1.73% |
| Notable | Serbia | 1.72% | 1.72% | +0.00 | 1.72% |
| Notable | Philippines | 1.71% | 1.71% | +0.00 | 1.71% |
| Notable | Estonia | 1.69% | 1.69% | +0.00 | 1.69% |
| Notable | Norway | 1.67% | 1.67% | +0.00 | 1.67% |
| Notable | Chile | 0.99% | 0.99% | +0.00 | 0.99% |
| Notable | Finland | 0.98% | 0.98% | +0.00 | 0.98% |
| Notable | Slovakia | 0.96% | 0.96% | +0.00 | 0.96% |
| Notable | Bulgaria | 0.95% | 0.95% | +0.00 | 0.95% |
| Notable | Sweden | 0.94% | 0.94% | +0.00 | 0.94% |
| Notable | Vietnam | 0.94% | 0.94% | +0.00 | 0.94% |
| Notable | Ukraine | 0.92% | 0.92% | +0.00 | 0.92% |
| Notable | New Zealand | 0.85% | 0.85% | +0.00 | 0.85% |
| Notable | Thailand | 0.84% | 0.84% | +0.00 | 0.84% |
| Notable | Belgium | 0.84% | 0.84% | +0.00 | 0.84% |
| Notable | Argentina | 0.84% | 0.84% | +0.00 | 0.84% |
| Notable | South Africa | 0.80% | 0.80% | +0.00 | 0.80% |
| Notable | Italy | 0.78% | 0.78% | +0.00 | 0.78% |
| Notable | Uruguay | 0.77% | 0.77% | +0.00 | 0.77% |
| Notable | Poland | 0.77% | 0.77% | +0.00 | 0.77% |
| Notable | Lithuania | 0.76% | 0.76% | +0.00 | 0.76% |

*Column totals unchanged: yes.  ★ = receives the fill.*

#### Sinheung

*draw 0.5694 · Sinian factor 0.5214 · fill goes to: Japan, Germany, Russia*

| Tier today | Nation | Before | After (even) | Change | After (proportional) | Census I humans before | after (even) |
|---|---|--:|--:|--:|--:|--:|--:|
| Primary | South Korea | 34.62% | 34.62% | +0.00 | 34.62% | 165,973 | 165,973 |
| Significant | Germany ★ | 8.64% | 10.19% | +1.55 | 10.37% | 41,421 | 48,871 |
| Significant | Japan ★ | 7.78% | 9.33% | +1.55 | 9.34% | 37,298 | 44,748 |
| Significant | Russia ★ | 6.85% | 8.40% | +1.55 | 8.22% | 32,841 | 40,290 |
| Significant | Sinian Federation (was China) | 9.74% | 5.08% | -4.66 | 5.08% | 46,694 | 24,345 |
| Significant | Indonesia | 4.41% | 4.41% | +0.00 | 4.41% | 21,142 | 21,142 |
| Notable | Thailand | 3.65% | 3.65% | +0.00 | 3.65% | 17,498 | 17,498 |
| Significant | Australia | 3.57% | 3.57% | +0.00 | 3.57% | 17,115 | 17,115 |
| Notable | Estonia | 3.52% | 3.52% | +0.00 | 3.52% | 16,875 | 16,875 |
| Notable | Hungary | 3.43% | 3.43% | +0.00 | 3.43% | 16,443 | 16,443 |
| Notable | Lithuania | 3.11% | 3.11% | +0.00 | 3.11% | 14,910 | 14,910 |
| Notable | Malaysia | 2.93% | 2.93% | +0.00 | 2.93% | 14,047 | 14,047 |
| Notable | Vietnam | 1.95% | 1.95% | +0.00 | 1.95% | 9,349 | 9,349 |
| Notable | Philippines | 1.77% | 1.77% | +0.00 | 1.77% | 8,486 | 8,486 |
| Notable | Bulgaria | 1.45% | 1.45% | +0.00 | 1.45% | 6,951 | 6,951 |
| Notable | Latvia | 1.35% | 1.35% | +0.00 | 1.35% | 6,472 | 6,472 |
| Notable | South Africa | 1.23% | 1.23% | +0.00 | 1.23% | 5,896 | 5,896 |

*Column totals unchanged: yes.  ★ = receives the fill.*

#### Concordia

*draw 0.5748 · Sinian factor 0.5263 · fill goes to: Japan, South Korea, Russia, Australia, Indonesia (FALLBACK: no nation outside the top tier reaches 5%) · literal reading (below China and at least 5%) would give: nobody*

| Tier today | Nation | Before | After (even) | Change | After (proportional) | Census I humans before | after (even) |
|---|---|--:|--:|--:|--:|--:|--:|
| Primary | Japan ★ | 9.32% | 10.05% | +0.73 | 10.10% | 48,202 | 51,972 |
| Primary | South Korea ★ | 9.31% | 10.04% | +0.73 | 10.09% | 48,107 | 51,877 |
| Primary | Russia ★ | 9.20% | 9.93% | +0.73 | 9.97% | 47,572 | 51,341 |
| Primary | Australia ★ | 7.82% | 8.55% | +0.73 | 8.48% | 40,417 | 44,186 |
| Primary | Indonesia ★ | 7.72% | 8.45% | +0.73 | 8.37% | 39,882 | 43,651 |
| Significant | USA | 4.43% | 4.43% | +0.00 | 4.43% | 22,918 | 22,918 |
| Significant | Vietnam | 4.23% | 4.23% | +0.00 | 4.23% | 21,846 | 21,846 |
| Primary | Sinian Federation (was China) | 7.70% | 4.05% | -3.65 | 4.05% | 39,787 | 20,940 |
| Significant | Belarus | 3.77% | 3.77% | +0.00 | 3.77% | 19,477 | 19,477 |
| Significant | New Zealand | 3.76% | 3.76% | +0.00 | 3.76% | 19,461 | 19,461 |
| Significant | Philippines | 2.62% | 2.62% | +0.00 | 2.62% | 13,518 | 13,518 |
| Significant | Malaysia | 1.95% | 1.95% | +0.00 | 1.95% | 10,079 | 10,079 |
| Notable | Serbia | 1.59% | 1.59% | +0.00 | 1.59% | 8,227 | 8,227 |
| Significant | Thailand | 1.58% | 1.58% | +0.00 | 1.58% | 8,187 | 8,187 |
| Notable | Estonia | 1.55% | 1.55% | +0.00 | 1.55% | 8,022 | 8,022 |
| Notable | Belgium | 1.54% | 1.54% | +0.00 | 1.54% | 7,956 | 7,956 |
| Notable | France | 1.51% | 1.51% | +0.00 | 1.51% | 7,820 | 7,820 |
| Notable | Spain | 1.47% | 1.47% | +0.00 | 1.47% | 7,591 | 7,591 |
| Notable | Croatia | 1.44% | 1.44% | +0.00 | 1.44% | 7,440 | 7,440 |
| Notable | Hungary | 1.43% | 1.43% | +0.00 | 1.43% | 7,418 | 7,418 |
| Notable | Finland | 1.41% | 1.41% | +0.00 | 1.41% | 7,280 | 7,280 |
| Notable | Czech Republic | 1.38% | 1.38% | +0.00 | 1.38% | 7,143 | 7,143 |
| Notable | Norway | 1.38% | 1.38% | +0.00 | 1.38% | 7,120 | 7,120 |
| Notable | UK | 1.32% | 1.32% | +0.00 | 1.32% | 6,822 | 6,822 |
| Notable | Poland | 1.32% | 1.32% | +0.00 | 1.32% | 6,812 | 6,812 |
| Notable | Mexico | 1.29% | 1.29% | +0.00 | 1.29% | 6,653 | 6,653 |
| Notable | Lithuania | 0.84% | 0.84% | +0.00 | 0.84% | 4,345 | 4,345 |
| Notable | Latvia | 0.81% | 0.81% | +0.00 | 0.81% | 4,176 | 4,176 |
| Notable | Italy | 0.75% | 0.75% | +0.00 | 0.75% | 3,856 | 3,856 |
| Notable | Sweden | 0.75% | 0.75% | +0.00 | 0.75% | 3,879 | 3,879 |
| Notable | Bulgaria | 0.72% | 0.72% | +0.00 | 0.72% | 3,719 | 3,719 |
| Notable | Ukraine | 0.69% | 0.69% | +0.00 | 0.69% | 3,581 | 3,581 |
| Notable | Romania | 0.69% | 0.69% | +0.00 | 0.69% | 3,559 | 3,559 |
| Notable | Slovakia | 0.66% | 0.66% | +0.00 | 0.66% | 3,408 | 3,408 |
| Notable | Canada | 0.61% | 0.61% | +0.00 | 0.61% | 3,179 | 3,179 |
| Notable | Netherlands | 0.59% | 0.59% | +0.00 | 0.59% | 3,042 | 3,042 |
| Notable | Germany | 0.58% | 0.58% | +0.00 | 0.58% | 2,977 | 2,977 |
| Notable | Slovenia | 0.28% | 0.28% | +0.00 | 0.28% | 1,459 | 1,459 |

*Column totals unchanged: yes.  ★ = receives the fill.*

#### Shirayuki

*draw 0.5963 · Sinian factor 0.5460 · fill goes to: Australia, Russia, South Korea · literal reading (below China and at least 5%) would give: nobody · just under the line, so left as is: Germany 4.93%*

| Tier today | Nation | Before | After (even) | Change | After (proportional) | Census I humans before | after (even) |
|---|---|--:|--:|--:|--:|--:|--:|
| Primary | Japan | 36.27% | 36.27% | +0.00 | 36.27% | 192,580 | 192,580 |
| Significant | Australia ★ | 8.76% | 9.85% | +1.09 | 9.89% | 46,512 | 52,281 |
| Significant | Russia ★ | 8.61% | 9.70% | +1.09 | 9.72% | 45,716 | 51,485 |
| Significant | South Korea ★ | 7.89% | 8.98% | +1.09 | 8.91% | 41,893 | 47,662 |
| Significant | Germany | 4.93% | 4.93% | +0.00 | 4.93% | 26,176 | 26,176 |
| Significant | Sinian Federation (was China) | 7.18% | 3.92% | -3.26 | 3.92% | 38,123 | 20,816 |
| Notable | Romania | 3.54% | 3.54% | +0.00 | 3.54% | 18,796 | 18,796 |
| Notable | Vietnam | 3.16% | 3.16% | +0.00 | 3.16% | 16,779 | 16,779 |
| Notable | Ukraine | 3.11% | 3.11% | +0.00 | 3.11% | 16,512 | 16,512 |
| Notable | Belarus | 3.00% | 3.00% | +0.00 | 3.00% | 15,929 | 15,929 |
| Notable | Thailand | 2.99% | 2.99% | +0.00 | 2.99% | 15,875 | 15,875 |
| Notable | New Zealand | 2.97% | 2.97% | +0.00 | 2.97% | 15,770 | 15,770 |
| Notable | Lithuania | 1.76% | 1.76% | +0.00 | 1.76% | 9,345 | 9,345 |
| Notable | South Africa | 1.66% | 1.66% | +0.00 | 1.66% | 8,813 | 8,813 |
| Notable | Bulgaria | 1.60% | 1.60% | +0.00 | 1.60% | 8,496 | 8,496 |
| Notable | Latvia | 1.35% | 1.35% | +0.00 | 1.35% | 7,168 | 7,168 |
| Notable | Estonia | 1.22% | 1.22% | +0.00 | 1.22% | 6,478 | 6,478 |

*Column totals unchanged: yes.  ★ = receives the fill.*

#### Byrd

*draw 0.5842 · Sinian factor 0.5349 · fill goes to: Australia, Japan · literal reading (below China and at least 5%) would give: nobody*

| Tier today | Nation | Before | After (even) | Change | After (proportional) | Census I humans before | after (even) |
|---|---|--:|--:|--:|--:|--:|--:|
| Primary | USA | 13.57% | 13.57% | +0.00 | 13.57% | 26,924 | 26,924 |
| Primary | Canada | 11.43% | 11.43% | +0.00 | 11.43% | 22,677 | 22,677 |
| Significant | Australia ★ | 6.42% | 7.11% | +0.69 | 7.12% | 12,737 | 14,098 |
| Significant | Japan ★ | 6.19% | 6.88% | +0.69 | 6.86% | 12,281 | 13,642 |
| Significant | South Korea | 3.19% | 3.19% | +0.00 | 3.19% | 6,329 | 6,329 |
| Notable | Lithuania | 2.27% | 2.27% | +0.00 | 2.27% | 4,504 | 4,504 |
| Notable | Philippines | 2.23% | 2.23% | +0.00 | 2.23% | 4,425 | 4,425 |
| Notable | Thailand | 2.22% | 2.22% | +0.00 | 2.22% | 4,404 | 4,404 |
| Notable | Indonesia | 2.21% | 2.21% | +0.00 | 2.21% | 4,385 | 4,385 |
| Notable | Malaysia | 2.20% | 2.20% | +0.00 | 2.20% | 4,365 | 4,365 |
| Notable | Brazil | 2.20% | 2.20% | +0.00 | 2.20% | 4,365 | 4,365 |
| Notable | Croatia | 2.16% | 2.16% | +0.00 | 2.16% | 4,285 | 4,285 |
| Notable | Latvia | 2.15% | 2.15% | +0.00 | 2.15% | 4,266 | 4,266 |
| Notable | Netherlands | 2.10% | 2.10% | +0.00 | 2.10% | 4,167 | 4,167 |
| Notable | Slovakia | 2.06% | 2.06% | +0.00 | 2.06% | 4,087 | 4,087 |
| Notable | South Africa | 2.02% | 2.02% | +0.00 | 2.02% | 4,008 | 4,008 |
| Notable | Czech Republic | 1.96% | 1.96% | +0.00 | 1.96% | 3,889 | 3,889 |
| Notable | Uruguay | 1.96% | 1.96% | +0.00 | 1.96% | 3,889 | 3,889 |
| Notable | Vietnam | 1.94% | 1.94% | +0.00 | 1.94% | 3,850 | 3,850 |
| Notable | UK | 1.93% | 1.93% | +0.00 | 1.93% | 3,829 | 3,829 |
| Notable | Finland | 1.90% | 1.90% | +0.00 | 1.90% | 3,770 | 3,770 |
| Notable | New Zealand | 1.90% | 1.90% | +0.00 | 1.90% | 3,770 | 3,770 |
| Notable | Romania | 1.90% | 1.90% | +0.00 | 1.90% | 3,770 | 3,770 |
| Significant | Sinian Federation (was China) | 2.95% | 1.58% | -1.37 | 1.58% | 5,853 | 3,131 |
| Notable | Norway | 1.23% | 1.23% | +0.00 | 1.23% | 2,440 | 2,440 |
| Notable | Hungary | 1.23% | 1.23% | +0.00 | 1.23% | 2,440 | 2,440 |
| Notable | Ukraine | 1.22% | 1.22% | +0.00 | 1.22% | 2,420 | 2,420 |
| Notable | Russia | 1.19% | 1.19% | +0.00 | 1.19% | 2,361 | 2,361 |
| Notable | Germany | 1.19% | 1.19% | +0.00 | 1.19% | 2,361 | 2,361 |
| Notable | Belarus | 1.17% | 1.17% | +0.00 | 1.17% | 2,321 | 2,321 |
| Notable | Poland | 1.16% | 1.16% | +0.00 | 1.16% | 2,302 | 2,302 |
| Notable | France | 1.11% | 1.11% | +0.00 | 1.11% | 2,203 | 2,203 |
| Notable | Bulgaria | 1.06% | 1.06% | +0.00 | 1.06% | 2,103 | 2,103 |
| Notable | Chile | 1.02% | 1.02% | +0.00 | 1.02% | 2,024 | 2,024 |
| Notable | Argentina | 0.98% | 0.98% | +0.00 | 0.98% | 1,944 | 1,944 |
| Notable | Mexico | 0.96% | 0.96% | +0.00 | 0.96% | 1,905 | 1,905 |
| Notable | Italy | 0.92% | 0.92% | +0.00 | 0.92% | 1,826 | 1,826 |
| Notable | Slovenia | 0.92% | 0.92% | +0.00 | 0.92% | 1,826 | 1,826 |
| Notable | Spain | 0.91% | 0.91% | +0.00 | 0.91% | 1,805 | 1,805 |
| Notable | Belgium | 0.91% | 0.91% | +0.00 | 0.91% | 1,805 | 1,805 |
| Notable | Sweden | 0.90% | 0.90% | +0.00 | 0.90% | 1,785 | 1,785 |
| Notable | Serbia | 0.86% | 0.86% | +0.00 | 0.86% | 1,706 | 1,706 |

*Column totals unchanged: yes.  ★ = receives the fill.*

#### Palmer City

*draw 0.5939 · Sinian factor 0.5438 · fill goes to: Brazil, France, Germany, Mexico, Canada, UK · literal reading (below China and at least 5%) would give: nobody*

| Tier today | Nation | Before | After (even) | Change | After (proportional) | Census I humans before | after (even) |
|---|---|--:|--:|--:|--:|--:|--:|
| Primary | USA | 20.29% | 20.29% | +0.00 | 20.29% | 33,666 | 33,666 |
| Significant | Brazil ★ | 9.68% | 9.75% | +0.07 | 9.77% | 16,056 | 16,171 |
| Significant | France ★ | 9.54% | 9.61% | +0.07 | 9.63% | 15,825 | 15,940 |
| Significant | Germany ★ | 9.51% | 9.58% | +0.07 | 9.60% | 15,774 | 15,889 |
| Significant | Mexico ★ | 5.71% | 5.78% | +0.07 | 5.76% | 9,475 | 9,590 |
| Significant | Canada ★ | 5.68% | 5.75% | +0.07 | 5.73% | 9,424 | 9,539 |
| Significant | UK ★ | 5.54% | 5.61% | +0.07 | 5.59% | 9,193 | 9,307 |
| Notable | Uruguay | 3.70% | 3.70% | +0.00 | 3.70% | 6,141 | 6,141 |
| Notable | Argentina | 3.05% | 3.05% | +0.00 | 3.05% | 5,061 | 5,061 |
| Notable | Estonia | 1.39% | 1.39% | +0.00 | 1.39% | 2,312 | 2,312 |
| Notable | Czech Republic | 1.35% | 1.35% | +0.00 | 1.35% | 2,247 | 2,247 |
| Notable | Australia | 1.33% | 1.33% | +0.00 | 1.33% | 2,207 | 2,207 |
| Notable | Slovakia | 1.29% | 1.29% | +0.00 | 1.29% | 2,142 | 2,142 |
| Notable | Thailand | 1.26% | 1.26% | +0.00 | 1.26% | 2,089 | 2,089 |
| Notable | Russia | 1.20% | 1.20% | +0.00 | 1.20% | 1,997 | 1,997 |
| Notable | Serbia | 1.16% | 1.16% | +0.00 | 1.16% | 1,931 | 1,931 |
| Notable | Belgium | 1.14% | 1.14% | +0.00 | 1.14% | 1,892 | 1,892 |
| Notable | South Korea | 1.09% | 1.09% | +0.00 | 1.09% | 1,813 | 1,813 |
| Notable | Italy | 1.06% | 1.06% | +0.00 | 1.06% | 1,761 | 1,761 |
| Notable | Norway | 1.01% | 1.01% | +0.00 | 1.01% | 1,669 | 1,669 |
| Notable | Croatia | 0.97% | 0.97% | +0.00 | 0.97% | 1,603 | 1,603 |
| Notable | South Africa | 0.96% | 0.96% | +0.00 | 0.96% | 1,590 | 1,590 |
| Notable | Slovenia | 0.86% | 0.86% | +0.00 | 0.86% | 1,432 | 1,432 |
| Notable | Chile | 0.86% | 0.86% | +0.00 | 0.86% | 1,422 | 1,422 |
| Notable | Romania | 0.86% | 0.86% | +0.00 | 0.86% | 1,419 | 1,419 |
| Notable | Philippines | 0.82% | 0.82% | +0.00 | 0.82% | 1,353 | 1,353 |
| Notable | Netherlands | 0.76% | 0.76% | +0.00 | 0.76% | 1,261 | 1,261 |
| Notable | Japan | 0.73% | 0.73% | +0.00 | 0.73% | 1,209 | 1,209 |
| Notable | Poland | 0.70% | 0.70% | +0.00 | 0.70% | 1,169 | 1,169 |
| Notable | New Zealand | 0.67% | 0.67% | +0.00 | 0.67% | 1,117 | 1,117 |
| Notable | Bulgaria | 0.62% | 0.62% | +0.00 | 0.62% | 1,025 | 1,025 |
| Notable | Vietnam | 0.58% | 0.58% | +0.00 | 0.58% | 959 | 959 |
| Notable | Spain | 0.53% | 0.53% | +0.00 | 0.53% | 880 | 880 |
| Notable | Sinian Federation (was China) | 0.91% | 0.49% | -0.42 | 0.49% | 1,511 | 822 |
| Notable | Latvia | 0.48% | 0.48% | +0.00 | 0.48% | 802 | 802 |
| Notable | Sweden | 0.46% | 0.46% | +0.00 | 0.46% | 762 | 762 |
| Notable | Belarus | 0.44% | 0.44% | +0.00 | 0.44% | 723 | 723 |
| Notable | Indonesia | 0.38% | 0.38% | +0.00 | 0.38% | 631 | 631 |
| Notable | Ukraine | 0.35% | 0.35% | +0.00 | 0.35% | 578 | 578 |
| Notable | Finland | 0.32% | 0.32% | +0.00 | 0.32% | 539 | 539 |
| Notable | Lithuania | 0.28% | 0.28% | +0.00 | 0.28% | 460 | 460 |
| Notable | Malaysia | 0.25% | 0.25% | +0.00 | 0.25% | 407 | 407 |
| Notable | Hungary | 0.23% | 0.23% | +0.00 | 0.23% | 381 | 381 |

*Column totals unchanged: yes.  ★ = receives the fill.*

### Summary (even fill)

| City | China before | Sinian after | Leader before | Leader after | Lead after (1st ÷ 2nd) | Founders: before → after |
|---|--:|--:|---|---|--:|---|
| Dumont d'Urville | 24.31% | 13.06% | Sinian Fed. 24.31% | USA 20.13% | 1.38 | Japan 11.72 → 14.53 |
| Mirny | 24.24% | 12.34% | Sinian Fed. 24.24% | UK 14.33% | 1.05 | (Idelsk-Uralia, no row) |
| Zukelli | 22.63% | 11.80% | Sinian Fed. 22.63% | USA 19.47% | 1.47 | Australia 9.55 → 11.72 |
| Relung Panen | 21.58% | 11.55% | Sinian Fed. 21.58% | Russia 14.27% | 1.03 | Indonesia 12.23 → 13.90; Malaysia 3.30 → 3.30 |
| Janbogo | 20.63% | 10.44% | Sinian Fed. 20.63% | USA 18.39% | 1.44 | South Korea 10.23 → 12.78 |
| Davis | 19.04% | 9.78% | Sinian Fed. 19.04% | Japan 10.90% | 1.02 | Australia 4.93 → 4.93 |
| Temirötkel | 17.39% | 9.02% | Sinian Fed. 17.39% | Indonesia 10.26% | 1.03 | (Kazakhstan, no row); (the CIN members, all Notable) |
| Mawson | 17.02% | 8.68% | Sinian Fed. 17.02% | UK 10.66% | 1.07 | Australia 8.29 → 9.96; (Kazakhstan, no row); (Russia, no row) |
| Denison | 22.29% | 12.21% | USA 26.19% | USA 26.19% | 1.77 | Australia 5.87 → 8.39 |
| Cape Adare | 19.85% | 10.75% | USA 22.26% | USA 22.26% | 1.81 | — |
| Scott | 19.48% | 10.56% | USA 22.62% | USA 22.62% | 1.80 | New Zealand 3.52 → 3.52 |
| Fort McMurdo | 19.34% | 9.82% | USA 21.69% | USA 21.69% | 1.59 | — |
| Amundsen Station | 19.31% | 10.53% | USA 22.80% | USA 22.80% | 1.89 | — |
| Casey | 19.06% | 9.60% | USA 21.96% | USA 21.96% | 1.78 | Australia 9.26 → 11.15 |
| Dome Fuji | 10.13% | 5.11% | USA 11.20% | USA 11.20% | 1.56 | — |
| Sinheung | 9.74% | 5.08% | South Korea 34.62% | South Korea 34.62% | 3.40 | South Korea 34.62 → 34.62 |
| Concordia | 7.70% | 4.05% | Japan 9.32% | Japan 10.05% | 1.00 | — |
| Shirayuki | 7.18% | 3.92% | Japan 36.27% | Japan 36.27% | 3.68 | Japan 36.27 → 36.27 |
| Byrd | 2.95% | 1.58% | USA 13.57% | USA 13.57% | 1.19 | — |
| Palmer City | 0.91% | 0.49% | USA 20.29% | USA 20.29% | 2.08 | — |

### Nationally (Census I humans; the census table plus this run's changes)

| Nation | Before | After (even) | Change | After (proportional) | Before ÷ (2% of pool) | After (even) ÷ (2% of pool) |
|---|--:|--:|--:|--:|--:|--:|
| Australia | 727,081 | 849,828 | +122,747 | 851,574 | 2.80 | 3.27 |
| South Korea | 892,502 | 1,005,079 | +112,577 | 1,016,764 | 1.72 | 1.93 |
| Japan | 953,710 | 1,061,878 | +108,168 | 1,059,384 | 0.73 | 0.82 |
| Indonesia | 606,976 | 713,959 | +106,983 | 711,470 | 1.90 | 2.23 |
| Russia | 494,209 | 555,626 | +61,417 | 547,927 | 0.99 | 1.11 |
| UK | 855,222 | 906,175 | +50,953 | 911,374 | 1.34 | 1.42 |
| France | 490,468 | 529,445 | +38,977 | 529,875 | 0.70 | 0.76 |
| Italy | 164,828 | 195,466 | +30,638 | 190,990 | 0.31 | 0.36 |
| Canada | 327,961 | 356,824 | +28,863 | 355,598 | 0.82 | 0.89 |
| Germany | 735,406 | 760,488 | +25,082 | 763,946 | 0.80 | 0.83 |
| Thailand | 173,181 | 181,155 | +7,974 | 177,019 | 1.08 | 1.13 |
| Mexico | 278,536 | 278,651 | +115 | 278,622 | 0.77 | 0.77 |
| Brazil | 704,963 | 705,078 | +115 | 705,109 | 2.07 | 2.07 |
| China → Sinian Federation (Zhongshan unchanged) | 1,660,450 | 965,841 | -694,609 | 965,841 | 0.40 | 0.23 |

*Tepenia's human total is unchanged (15,623,523): every city keeps its size.*

### Variant: the line at 4.5% ("about 5%"), even fill

*Only the cities where the 4.5% line adds a nation are listed; the Sinian figure is the same as above.*

| City | Added at 4.5% | Its share: before → after (5% line) → after (4.5% line) | Other recipients' gain: 5% line → 4.5% line |
|---|---|---|--:|
| Mirny | Philippines | Philippines 4.50 → 4.50 → 6.20 | +1.98 → +1.70 |
| Zukelli | Japan | Japan 4.69 → 4.69 → 6.49 | +2.17 → +1.80 |
| Relung Panen | Vietnam | Vietnam 4.76 → 4.76 → 6.19 | +1.67 → +1.43 |
| Janbogo | Germany | Germany 4.64 → 4.64 → 6.68 | +2.55 → +2.04 |
| Davis | Australia | Australia 4.93 → 4.93 → 6.25 | +1.54 → +1.32 |
| Temirötkel | France | France 4.82 → 4.82 → 6.22 | +1.67 → +1.40 |
| Mawson | South Korea | South Korea 4.87 → 4.87 → 6.26 | +1.67 → +1.39 |
| Scott | Indonesia | Indonesia 4.98 → 4.98 → 6.47 | +1.78 → +1.49 |
| Fort McMurdo | Italy | Italy 4.90 → 4.90 → 7.28 | +3.17 → +2.38 |
| Casey | Indonesia | Indonesia 4.92 → 4.92 → 6.50 | +1.89 → +1.58 |
| Dome Fuji | Germany, South Korea | Germany 4.83 → 4.83 → 5.83; South Korea 4.78 → 4.78 → 5.78 | +1.67 → +1.00 |
| Shirayuki | Germany | Germany 4.93 → 4.93 → 5.74 | +1.09 → +0.81 |

### Illustration: the China-and-USA cities once the USA's row is also split (even fill)

*Assumes every American successor reaches the city in proportion to its share of the USA's pool (Option B); the time-zone window and the split rulings are not applied.*

| City | USA after this run | Largest American successor (CSA) | Leader then | Lead then (1st ÷ 2nd) |
|---|--:|--:|---|--:|
| Dumont d'Urville | 20.13% | 5.82% | France 14.61% | 1.01 |
| Zukelli | 19.47% | 5.63% | South Korea 13.27% | 1.10 |
| Janbogo | 18.39% | 5.32% | South Korea 12.78% | 1.02 |
| Denison | 26.19% | 7.57% | South Korea 14.83% | 1.12 |
| Cape Adare | 22.26% | 6.44% | Australia 12.28% | 1.02 |
| Scott | 22.62% | 6.54% | Japan 12.59% | 1.00 |
| Fort McMurdo | 21.69% | 6.27% | Germany 13.66% | 1.06 |
| Amundsen Station | 22.80% | 6.59% | UK 12.03% | 1.04 |
| Casey | 21.96% | 6.35% | South Korea 12.35% | 1.03 |

*Full count tables (every column, both fills): `08_rebalance_city_tables.csv`.*
