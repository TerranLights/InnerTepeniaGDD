# Population work: preparation for 2026-11-02

**What this is.** Groundwork for the population session the developer set for 2026-11-02: every open population item with where it sits, and China's present share in every city. Built 2026-11-01 evening by reading and counting existing files. **Nothing here is a ruling and no figure was changed.**

## The developer's criteria (quoted from the Weekly To-Do, 2026-10-31 entry)

> *"In a lot of cities, China just clearly dominates, and this would cause the country to end up leaning towards one major culture. Ideally, I would like to get it so that perhaps it's not exactly, precisely, equally multicultural, but it's generally multicultural. … This doesn't mean that we need to add more people from the smaller percentage countries. … The two exceptions to this are Zhongshan and Kunlun, because those are cities that are actually set up by the Sinian Federation."*
>
> Final wording on the 5% line: *"consider raising the headcounts of populations at about 5% or MORE where that is what makes the mix generally multicultural. Populations at about 5% or less can generally stay roughly where they are."*

And the research that comes first: in the First and Second Interwar timelines "China" is the **Sinian Federation**, and some territories fragmented away, so its population differs (real, full research under LAW 0-R).

## China's share in every city today

Read from each spec's per-nation table (the first table whose shares sum to about 100%; shares as the spec writes them). "China ÷ largest other" is DERIVED. Which cities count as "clearly dominated" is the developer's call; the grouping below is by rank only.

### A. China is the largest nation

| City | China share (spec line) | China rank | Largest other nation | China ÷ largest other |
|---|--:|--:|---|--:|
| Zhongshan *(exempt)* | 35.83% (`Specs/Mirny subnet/Zhongshan.md` L32) | 1 of 18 | South Korea 9.70% | 3.69× |
| Dumont d'Urville | 24.31% (`Specs/Janbogo subnet/Dumont_dUrville.md` L60) | 1 of 12 | USA 20.13% | 1.21× |
| Mirny | 24.24% (`Specs/Mirny subnet/Mirny.md` L32) | 1 of 14 | UK 12.35% | 1.96× |
| Zukelli | 22.63% (`Specs/Janbogo subnet/Zukelli.md` L32) | 1 of 12 | USA 19.47% | 1.16× |
| Relung Panen | 21.58% (`Specs/Mirny subnet/Relung_Panen.md` L57) | 1 of 11 | Russia 12.60% | 1.71× |
| Janbogo | 20.63% (`Specs/Janbogo subnet/Janbogo.md` L32) | 1 of 13 | USA 18.39% | 1.12× |
| Davis | 19.04% (`Specs/Mirny subnet/Davis.md` L32) | 1 of 21 | Japan 9.36% | 2.03× |
| Temirötkel | 17.39% (`Specs/Mawson subnet/Temirotkel.md` L72) | 1 of 25 | Indonesia 8.59% | 2.02× |
| Mawson | 17.02% (`Specs/Mawson subnet/Mawson.md` L32) | 1 of 26 | UK 8.99% | 1.89× |

### B. China is second

| City | China share (spec line) | China rank | Largest other nation | China ÷ largest other |
|---|--:|--:|---|--:|
| Denison | 22.29% (`Specs/Janbogo subnet/Denison.md` L69) | 2 of 11 | USA 26.19% | 0.85× |
| Cape Adare | 19.85% (`Specs/Janbogo subnet/Cape_Adare.md` L33) | 2 of 12 | USA 22.26% | 0.89× |
| Scott | 19.48% (`Specs/Janbogo subnet/Scott.md` L55) | 2 of 12 | USA 22.62% | 0.86× |
| Fort McMurdo | 19.34% (`Specs/Janbogo subnet/Fort_McMurdo.md` L55) | 2 of 15 | USA 21.69% | 0.89× |
| Amundsen Station | 19.31% (`Specs/Amundsen-Scott subnet/Amundsen_Station.md` L32) | 2 of 12 | USA 22.80% | 0.85× |
| Casey | 19.06% (`Specs/Mirny subnet/Casey.md` L32) | 2 of 13 | USA 21.96% | 0.87× |
| Kunlun *(exempt)* | 15.22% (`Specs/Mirny subnet/Kunlun.md` L51) | 2 of 19 | USA 15.43% | 0.99× |
| Dome Fuji | 10.13% (`Specs/Mawson subnet/Dome_Fuji.md` L61) | 2 of 43 | USA 11.20% | 0.90× |
| Sinheung | 9.74% (`Specs/Mirny subnet/Sinheung.md` L89) | 2 of 17 | South Korea 34.62% | 0.28× |

### C. China is further down

| City | China share (spec line) | China rank | Largest other nation | China ÷ largest other |
|---|--:|--:|---|--:|
| Concordia | 7.70% (`Specs/Janbogo subnet/Concordia.md` L36) | 6 of 38 | Japan 9.32% | 0.83× |
| Shirayuki | 7.18% (`Specs/Mirny subnet/Shirayuki.md` L62) | 5 of 17 | Japan 36.27% | 0.20× |
| Byrd | 2.95% (`Specs/Byrd subnet/Byrd.md` L83) | 6 of 42 | USA 13.57% | 0.22× |
| Palmer City | 0.91% (`Specs/Palmer subnet/Palmer_City.md` L100) | 21 of 40 | USA 20.29% | 0.04× |

### D. China is not in the table

Ariun Nuur, Belgrano, Contrapunto, Esperanza, Halley, Lazar, Marambio, Neumayer, Pergamino, Puerto Abrigo, Rothera, Sanay, Santa Luce, Signy, Troll, Utstein (16 cities).

*Note:* Palmer City's per-nation table lists 43 nations; the reader parsed 40 of its rows (the other three are written in a different row format). China's row (L100, 0.91%) was checked by eye.

## Every open population item, and where it sits

Paths are under `Worldspace/Locations-and-Levels/` unless they start with `Specs/`, `Research_Logs/` or a file name in the `Cities/` folder. Ledger IDs refer to `Universal_Location_Methodology/Manual_Input_Audit_2026-10-29/FIX_LEDGER.md`.

| # | Item | Where it sits | State |
|--:|---|---|---|
| 1 | **Sinian Federation research** (which territories split from today's China, successor populations) and the **rebalance** of the cities China dominates | Weekly To-Do, 2026-10-31 entry; the table above | Not started |
| 2 | **Russia-split rulings**: the in-window threshold, solar versus official time zones, pool split versus window split, and whether a split Russia keeps its share at Byrd, Palmer City and Contrapunto | `Research_Logs/Russia_Split_Proportions_RS1…RS4_*_2026-10-29.md`, `RS1b` input table and the CSV | Research done 2026-10-29; rulings open |
| 3 | **Esperanza, Option D**: the city's extent, and the people who move out | `Research_Logs/Esperanza_Site_Size_and_Education_Figures_2026-11-01.md`; ledger ES-003, ES-025, ES-S08 | Option chosen 2026-11-01; figure waits for the population work |
| 4 | **Esperanza's old figures in other files**: medical-institutes file L173 and L176, Division of Industry README L189 ("twelve times"), the `Phase_4` medical-institutes row, Marambio's spec L58 | ledger ES-S07, MB-S06 | Held for item 3 |
| 5 | **Puerto Abrigo**: 127,958 (Census I) and 95,215 (Census II) awaiting redistribution; its industry rows still on the old 128,887 (`09` L77; `16` L281, L184 and §14; later composition-file tables) | `Official_Population_Census.md` §D-OVERFLOW (L693); ledger PA-002, PA-S01 | Held for the redistribution |
| 6 | **Palmer City**: Census II humans (180,688) exceed Census I humans (165,912), 108.91% retention, unexplained | ledger PC-S03 | Carried to the population work |
| 7 | **Palmer City**: spec composition table disagrees with the census | `City_Input_Gaps_2026-10-27.md` B row | Deferred to the census rework |
| 8 | **Contrapunto**: the same disagreement | same | Same |
| 9 | **Byrd**: the same disagreement, plus its Russia share and the missing city-level composition section | same; Byrd walk-through item 9 | Same; the RS4 log is recorded as not an input |
| 10 | **Pergamino**: Uruguay, the Register's first founder, is absent from the spec's tier lists and per-nation table (spec L36–L59) and the census Section A entry | ledger PG-S03 | Resolve in the composition re-derivation |
| 11 | **Santa Luce**: the saved scenario that moves about 60% of its people elsewhere | `Universal_Location_Methodology/Population_Scenario_Santa_Luce_Redistribution_2026-10-28.md` | Saved, not applied |
| 12 | **Relung Panen**: its census entry and per-nation tier table | input check gaps T0-3 and T1-G8; `Relung_Panen/ULM_Input_Status.md` | Held for the population work |
| 13 | **Mawson**: its founders (Kazakhstan, Russia, Australia) are absent from its tier table, where China is sole Primary | ledger MW-S06 (spec L129, L183) | Russia split pending |
| 14 | **Zukelli**: Italy at Significant (6.24%) in an Australian-founded city | ledger ZK-S05 (`DR-23`) | Census deferred |
| 15 | **Casey**: the `16` §21 worker counts (1,128,834) were never recomputed for the newer workforce (1,146,682) | ledger CASEY-S05 | Developer: "leave … for now and address them later" |

**Follow-on work once figures change:** every city whose census or nation mix changes needs its spec table, census entry, composition-file section and datasheet rows (`Step_0`, `Step_-1`, `Phase_2`, `Phase_4`) brought into line, then the sheet verifier re-run (`Universal_Location_Methodology/Tools/verify_city_sheets.py`). Never rebuild an existing sheet with `--force`.
