# Population scenario: Santa Luce's 60% redistributed (2026-10-28)

> ## ✅ ADOPTED (`DR-68`) AND **APPLIED TO THE CENSUS 2026-10-28 (`DR-69`, Option A).** **Option A changes this file's Census I treatment of the two new groups:** Census I (before Amundsen Tower) has **no space workforce**; Amundsen Station's whole Census I share (22,982) is the **maritime fleet**. The space/sea split and the whole leave/hostel/overflow model (sections 3a, 7, 8) apply to **Census II only** (990 on break at once, about 198 hostel beds); the Census I columns of those sections are superseded. No census row, spec, Division of Industry row or megasheet was changed.
> Recorded at the developer's request ("definitely save this as a scenario file"). It waits for the census rework that accounts for Relung Panen (`DR-23`: no census edits until all ULM runs finish). Every figure is arithmetic on the current census rows. **It is not a migration and claims no one moved.**

## 1. How the scenario was built (the developer's steps, in order)

1. **Remove 60% of Santa Luce's population** (Census I: 302,542 humans + 318,002 robots = 620,544; Census II: 186,475 + 177,990 = 364,465). Santa Luce keeps 40%: Census I 201,695 H / 212,002 R; Census II 124,316 H / 118,660 R.
2. **Divide the removed people evenly across the 27 non-island cities** (the 38 minus the 11 island-labeled: Port Lockroy, Dumont d'Urville, Sayowa, Signy, Marambio, Sejong, Juan Carlos, Fort McMurdo, Scott, Palmer City, Rothera). Santa Luce is one of the 27 and gets its share back. Census I: about +11,205 humans and +11,778 robots each. Census II: four of the 27 have no Census II row by design (Ariun Nuur, Byrd, Kunlun, Dome Fuji), so it is split across the 23 with rows, about +15,846 each. Rounding leftovers go to the first cities in census order.
3. **Kunlun and Dome Fuji are robot-only.** Their human shares (11,205 + 11,205 = 22,410 in Census I) are taken out and divided across the other 24 continental cities (not counting Amundsen Station): +933 or +934 humans each. Their robot shares stay.
4. **Amundsen Station's share is not added to the city.** It becomes two non-city groups (section 3): a space workforce on rotating tours and a maritime fleet on rotating tours. Amundsen Station keeps its current 6,857 (Census I) and 4,891 (Census II).

**National totals are unchanged.** Census I: 15,623,523 H / 16,403,077 R / 32,026,600 combined (cities 32,003,618 + the two new groups 22,982). Census II: 10,486,701 H / 11,434,935 R / 21,921,636 (cities 21,905,791 + groups 15,845).

## 2. Resulting city numbers (the 27 continental cities; the 11 island cities do not change)

| City | Census I now | Census I scenario | Census II now | Census II scenario |
|---|--:|--:|--:|--:|
| Lazar | 2,358,287 | 2,382,205 | 1,623,579 | 1,639,426 |
| Esperanza | 1,878,287 | 1,902,205 | 1,178,039 | 1,193,886 |
| Cape Adare | 1,499,654 | 1,523,572 | 1,050,051 | 1,065,898 |
| Casey | 1,495,731 | 1,519,649 | 1,042,031 | 1,057,878 |
| Halley | 1,452,345 | 1,476,263 | 1,088,069 | 1,103,916 |
| Mawson | 1,446,733 | 1,470,651 | 952,446 | 968,293 |
| Mirny | 1,351,430 | 1,375,348 | 1,016,495 | 1,032,342 |
| Janbogo | 1,310,511 | 1,334,428 | 957,570 | 973,417 |
| Zhongshan | 1,151,489 | 1,175,406 | 897,016 | 912,863 |
| Zukelli | 1,258,651 | 1,282,568 | 937,659 | 953,506 |
| Neumayer | 1,252,080 | 1,275,997 | 830,747 | 846,594 |
| Shirayuki | 1,060,482 | 1,084,399 | 655,492 | 671,339 |
| Davis | 1,158,314 | 1,182,231 | 781,596 | 797,443 |
| Utstein | 1,137,917 | 1,161,834 | 766,762 | 782,609 |
| Belgrano | 1,071,890 | 1,095,807 | 837,768 | 853,614 |
| Sinheung | 962,415 | 986,332 | 799,463 | 815,309 |
| Denison | 906,222 | 930,139 | 623,477 | 639,322 |
| Santa Luce | 1,034,241 | 437,614 | 607,441 | 258,821 |
| Concordia | 1,015,947 | 1,039,863 | 635,302 | 651,147 |
| Troll | 954,450 | 978,366 | 671,832 | 687,677 |
| Relung Panen | 947,954 | 971,870 | 678,168 | 694,013 |
| Sanay | 463,669 | 487,585 | 275,117 | 290,962 |
| Ariun Nuur (Vostok) | 389,261 | 413,177 | 0 | 0 |
| Byrd | 376,890 | 400,805 | 0 | 0 |
| Kunlun | 123,449 | 135,226 | 0 | 0 |
| Dome Fuji | 55,072 | 66,849 | 0 | 0 |
| Amundsen Station | 6,857 | 6,857 | 4,891 | 4,891 |

Kunlun and Dome Fuji stay robot-only (0 humans): Kunlun 135,226, Dome Fuji 66,849 (Census I).

## 3. Amundsen Station's share, placed in two non-city groups

**Pool:** Census I 11,205 humans + 11,777 robots = 22,982; Census II 8,107 + 7,738 = 15,845. **Split: 50-50 on average over time (developer, `DR-68`); at any moment it can be any division.** At 60/40 space to sea, Census I would be 13,789 and 9,193.

| | Space workforce | Maritime fleet |
|---|--:|--:|
| **Census I** | 11,492 (5,603 H / 5,889 R) | 11,490 (5,602 H / 5,888 R) |
| **Census II** | 7,923 (4,054 H / 3,869 R) | 7,922 (4,053 H / 3,869 R) |

### 3a. Space workforce: rotating tours, 10-15% resting on Earth (developer's range)

| Resting share | On Earth (Census I) | In space (Census I) | On Earth (Census II) | In space (Census II) |
|---|--:|--:|--:|--:|
| 10.0% | 1,149 | 10,343 | 792 | 7,131 |
| 12.5% | 1,436 | 10,056 | 990 | 6,933 |
| 15.0% | 1,724 | 9,768 | 1,188 | 6,735 |

Rotation lengths that fit the range: about 8 months up and 1 down (11.1% resting) or 6 up and 1 down (14.3%). "Three weeks on, one week off" would leave 25% resting, outside the range.

### 3b. Maritime fleet: fishing vessels and radio relay points, all around Antarctica **excluding the Drake Passage**, rotating tours (lengths not set; alternatives)

| Rotation | At sea share | Aboard (Census I) | Ashore (Census I) | Aboard (Census II) | Ashore (Census II) |
|---|--:|--:|--:|--:|--:|
| 4 weeks on, 4 off | 50% | 5,745 | 5,745 | 3,961 | 3,961 |
| 2 on, 1 off | 67% | 7,660 | 3,830 | 5,281 | 2,641 |
| 3 on, 1 off | 75% | 8,618 | 2,872 | 5,942 | 1,980 |
| 4 on, 1 off | 80% | 9,192 | 2,298 | 6,338 | 1,584 |

*Illustration only (crew size invented):* at about 100 aboard per vessel, the 3-on-1-off case is roughly 86 vessels.

### 3c. Housing the resting space workers at Amundsen Station (developer, 2026-10-28)

> **Refined the same day; see section 7.** The developer later decided most resting space workers travel to Byrd, Janbogo, Zukelli or Concordia, so Amundsen Station's hostel only needs to house the share with no friends or family to visit. The full-size figures below are the ceiling if everyone stayed.

The space workers resting on Earth would be housed at Amundsen Station in **hostel- or barracks-style infrastructure, not residential homes.** The people resting at any moment equal the beds needed in steady state:

| Resting share | Humans (Census I) | Robots (Census I) | Total (Census I) | Total (Census II) |
|---|--:|--:|--:|--:|
| 10.0% | 560 | 589 | 1,149 | 792 |
| 12.5% | 700 | 736 | 1,436 | 990 |
| 15.0% | 840 | 883 | 1,724 | 1,188 |

- **Handover surge (illustrative assumption, not a ruling):** arrivals overlap departures and some rooms are down, so plan for capacity about 15% above the steady figure. At 12.5% resting that is about **1,651** places (Census I) and **1,138** (Census II).
- **Humans need beds; robots need charging and repair bays** (energy replenishment is primary, repair second). The human and robot columns above are the two kinds of space needed.
- **Against Amundsen Station's own residents:** 1,436 transient at 12.5% resting is 21% of its 6,857 (Census I) residents; 990 is 20% of its 4,891 (Census II). They are not residents and would not be counted in its population.
- **Maritime crews ashore (developer, 2026-10-28):** they are NOT housed in dedicated infrastructure. They generally know people closely in whatever city they are from, so on shore leave they stay with friends and family (to the extent a robot can have "family"). They are guests, not residents: they stay counted in the maritime group, not in the city they visit. No hostel capacity is needed for them.

## 4. Open questions

1. **Split ratio** between space and sea (50/50 assumed).
2. **Rotation lengths** for the maritime fleet; robot rest may deserve its own rotation (never write robots as tireless).
3. **Where resting people count (partly settled).** If resting workers lived in cities they would be counted there and partly cancel the removal. Here the hostel at Amundsen Station houses the space workers, so they stay in the space group. The sailors ashore stay with friends and family in their home cities (developer, 2026-10-28), as guests; they stay counted in the maritime group.
4. **Canon fit.** About 10,000 people in orbit at once and a fleet of about 10,000 aboard are large additions to the orbital and maritime canon. Check against the three-stage orbital infrastructure before adopting.
5. **Concordia** is among the 27 and received a share; its population is built from district counts, so it needs separate handling.
6. **Knock-on edits if adopted:** subnet totals, per-nation composition, Division of Industry workforce rows, extents, megasheets (rewritten later; never edit now).
7. **Amundsen Station** research and its Division of Industry are still to be done; this scenario leaves its own population unchanged.

## 4b. Consequences of the shore-leave ruling

- Ashore numbers (Census I, 3-on-1-off): 2,872 sailors at any moment. Spread across all 38 cities that is about 76 per city, a negligible load, so no city needs added housing or services for them.
- Each sailor needs a **home city** (where their friends and family are). That is a per-person attribute the census does not track today; it matters only if the group is later written into city-level material.
- Robots' "family" means chosen bonds (friends, shared households, mentors), consistent with the robot-relations canon; the file does not define it further.

## 6. Overland travel from Amundsen Station at the official later-era Rastra speed (`DR-63`, 2026-10-28)

**Speed: 45 km/h** ("advanced tracked or hybrid"), the developer's base of reference for later-era Rastras. **Road lengths are my estimates** (real station coordinates as proxies for the cities, great-circle distance times 1.15); the highway file gives no lengths. Driving only: 20 hours a day assumes relief drivers and sleeping aboard; add 10 to 15% for stops (an assumption, not ruled).

| Destination | Highways | Road (est.) | Driving hours | Days at 20 h/day | With +12.5% for stops |
|---|---|--:|--:|--:|--:|
| Byrd | Hwy 22 | ~1,277 km | ~28 h | ~1.4 | ~1.6 |
| Janbogo / Zukelli | Hwy 22 ramp, Hwy 175, connecting road | ~1,960 km | ~44 h | ~2.2 | ~2.5 |
| Concordia | Hwy 22 ramp, Hwy 175, Hwy 183 | ~3,306 km | ~73 h | ~3.7 | ~4.1 |

- **Concordia's road is about twice its direct distance** (1,657 km straight-line from the Pole) because canon's Hwy 175 runs to Janbogo's Hwy 183 ramp first.
- **Why it matters here:** space workers resting at Amundsen Station could return to a home city on a break. At the shortest rotation (1 week down), a Concordia round trip is about 8 days on the road, longer than the break. Byrd (about 3 days round trip) and Janbogo (about 5) fit better. This favors long rotations (7 to 8 months up, 1 down) or home visits only for nearby cities.
- **Not set:** fuel and range, the early-era (Arrastradora) speed, and cargo versus passenger capacity.

## 7. Where resting space workers spend their break (developer, 2026-10-28)

**Developer's premise (verbatim in substance).** Workers on leave from outer space mostly travel to **Byrd, Concordia, or Janbogo/Zukelli** and rest there, because those are the fastest cities to reach. There is a **national culture of welcoming space workers**; they only go to those four because they are closest. They often stay with friends and family. Amundsen Station keeps infrastructure only for the **percentage with no friends or family to go to**. So the hostel is much smaller, and the station's scientists, engineers, cooks, chefs and other staff remain a **solid majority** of its population at any time.

**Model used (illustrative; every parameter below is my assumption, not a ruling):**
- Break of about 30 days (the 7-months-up, 1-down rotation, 12.5% resting). Steady-state people on break: **1,436 (Census I), 990 (Census II)**.
- Round trips use `DR-63` (45 km/h), 20 h/day driving, +12.5% for stops: Byrd 3.2 days, Janbogo 4.9, Zukelli 4.9, Concordia 8.3. Days actually at the destination in a 30-day break: Byrd about 27, Janbogo and Zukelli about 25, Concordia about 22.
- Share of leavers per destination set **inversely proportional to one-way travel time** (the developer: "the fastest cities to get to"): Byrd 49%, Janbogo and Zukelli 16% each, Concordia 19%.
- Share staying at Amundsen Station (no friends or family): 10%, 20% or 30%, not ruled.

**Census I (1,436 on break at any moment)**

| Staying at Amundsen | Hostel beds needed (+15% surge) | In transit on the road | Byrd | Janbogo | Zukelli | Concordia |
|---|--:|--:|--:|--:|--:|--:|
| 10% | 144 (166) | 200 | 568 | 173 | 173 | 178 |
| **20%** | **287 (330)** | **178** | **505** | **154** | **154** | **159** |
| 30% | 431 (496) | 155 | 442 | 135 | 135 | 139 |

**Census II (990 on break at any moment)**

| Staying at Amundsen | Hostel beds needed (+15% surge) | In transit | Byrd | Janbogo | Zukelli | Concordia |
|---|--:|--:|--:|--:|--:|--:|
| 10% | 99 (114) | 138 | 391 | 119 | 119 | 123 |
| **20%** | **198 (228)** | **122** | **348** | **106** | **106** | **109** |
| 30% | 297 (342) | 107 | 304 | 93 | 93 | 96 |

**What it means:**
- **Amundsen Station's hostel shrinks from about 1,436 to about 287 beds (20% staying), about 330 with the surge allowance.** Against its 6,857 residents (Census I) the transient share is about 4%; against 4,891 (Census II), about 4%. Even with 30% staying it is about 6%. If everyone stayed (the old figure) it would be about 17%. The residents stay a solid majority under every case modeled.
- **Visitor load on the four cities is negligible:** about 500 at Byrd (a city of 376,890 in Census I), and 150 to 160 each at Janbogo, Zukelli and Concordia. They are guests with friends and family, not residents.
- **A 30-day break works for every destination; a 1-week break does not.** A Concordia round trip alone is 8.3 days. Only the long rotations (7 to 8 months up, 1 down) fit this culture.
- **Not modeled:** people who go to other cities (the premise says "usually" these four); stays shorter than the full break; and the stagger of departures through the month.
- **Recorded 2026-10-28:** the national welcoming custom is `DR-64`; the 20% staying share is the working number (`DR-65`), so the planning figures are about 287 hostel beds (Census I) and 198 (Census II). Neither is written into any city's culture file yet.

## 8. Byrd held near the others; the overflow spreads across the country (`DR-66`, developer, 2026-10-28)

**Rule.** Byrd's resting space workers stay in the same range as at Janbogo, Zukelli and Concordia. The overflow rests in other cities throughout the country. Working numbers use `DR-65`'s 20% staying share, the section 7 destination split for the other three cities, and an assumed **7-day average round trip** (range 5 to 9) to the overflow cities, whose distances are not computed.

| | Census I | Census II |
|---|--:|--:|
| People on break at once | 1,436 | 990 |
| Staying at Amundsen Station (hostel, 20%) | 287 | 198 |
| Leaving | 1,149 | 792 |
| **Byrd before / after** (at the destination at once) | ~505 / **~156** | ~348 / **~107** |
| Byrd leavers before / after | ~564 / ~174 | ~389 / ~120 |
| Janbogo, Zukelli, Concordia (at once, unchanged) | ~154, ~154, ~159 | ~106, ~106, ~109 |
| **Overflow leavers sent elsewhere** | **~390** | **~269** |
| Overflow at destinations at once (7-day round trip) | ~300 | ~207 |
| Overflow on the road at once | ~90 | ~62 |
| **Per city if spread evenly over the other 33 cities** | **~9** | **~6** |

Sensitivity of the overflow at destinations: a 5-day round trip gives about 326 (Census I) and 225 (Census II); a 9-day round trip gives about 275 and 189.

**Check, Census I:** hostel 287 + on the road 227 (137 on the named routes plus 90 overflow) + at destinations 923 (Byrd 156, Janbogo 154, Zukelli 154, Concordia 159, others 300) = 1,437.

- **The "other 33" is every city except Amundsen Station, Byrd, Janbogo, Zukelli and Concordia.** The even split is an illustration only.
- **Robot-only Kunlun and Dome Fuji** forbid humans, so only robot space workers can rest there.
- **Island-labeled cities** may need a non-road route (a boat or flight); their travel times are not modeled.
- **The load per city is tiny** (about 9 guests at once), so no city needs added housing or services for them.

## 5. Sources
Current census rows: `Locations/Cities/Official_Population_Census.md` (Sections for Census I and II); extent and island-label history: `Extent_and_Density_Per_City.md`; Kunlun and Dome Fuji robot-only canon: Human-Robot Relations baseline.
