# Decisions after run 3, what the atlas settles, and the research for run 4 (2026-11-02, ~00:00–00:30)

**Scratch, not canon.** Nothing official was changed. This file records the developer's answers to the checklist
given after run 3, what the author's world atlas settles without a ruling, and the research run 4 needs.

## 1. The developer's answers (~00:00, verbatim, in the order of the checklist)

**"Settled only by a default I used, so each needs your yes":**

| Item | Developer | What it means |
|---|---|---|
| Economic size or headcount | *"Back when we synthesized the national population, we had already counted by GINI metrics and economic reference. So that part should already be taken care of. It means that we can just go right ahead and go by headcount."* | **Headcount (Option A) for every split.** The pools already carry the income and inequality adjustment, so the split within a pool goes by people. Replaces the Option B used in runs 1–3. |
| The pieces that left China; Hong Kong, Macau, Taiwan | *"They would definitely qualify economically so far as the GINI metric. So see if you're able to identify their numbers and how they would be represented and *where* they would be represented by the time zone metric."* | **They get rows.** Work out their numbers and place them by the time-zone window (section 4). |
| Canada's small pieces | *"Nobody's actually from the Neutral Scientific Territory, as it's purely scientific in nature, so its representation in Tepenia is irrelevant."* | **Left out, confirmed.** |
| Russia's finer details | *"I'm not really quite sure what you're asking me here."* | **Settled by the atlas instead** (section 2). No decision needed. |
| Which borders | *"At the time of the latest period along the timeline."* | **The atlas's final state** (what runs 1–3 used). |
| Kunlun's co-founders | *"Works for me."* | **Mongolia and Künnarantaiga join Kunlun's middle tier** (Kunlun's Option A, morning pass). |
| The four cities held back | *"I would say go ahead and commit their new numbers, yes. I can't think of any reason not to."* | **Concordia, Dome Fuji, Relung Panen and Amundsen Station are committed with the others.** |

**"Still needs a decision":**

| Item | Developer | Status |
|---|---|---|
| Canada's Demilitarized Zone | *"I'll need to think about a solution to that, and I probably will need to wait until tomorrow."* | **Waits for the developer.** |
| Italy and Germany not yet split (Sardinia, Austria) | *"That will require research and recalculation in that case."* | **Research and recalculation** (section 5). |
| Chile's part of the Patagonia zone; Guatemala's Petén | *"Is there a major city there? I can't remember."* | **Answered** (section 3). |
| Kazakhstan at Temirötkel and Mawson | *"We'll need to look into that in greater detail."* | **Later, in detail.** |
| Russia's core state at Mawson; Lazar's drop to 2% | *"That's not a problem, as current-day Russia has split into multiple countries. The lower numbers are to be expected."* | **Accepted.** |
| Uruguay at Pergamino | *"That may require some research and recalculation."* | **Later: research and recalculation.** |
| New Zealand at Scott | *"That's not a problem."* | **Accepted.** |
| Malaysia at Relung Panen | *"That may require some research and recalculation."* | **Later: research and recalculation.** |
| Zukelli's Italy (7.6% after run 3) | *"In that case, we'll need to figure out a way to redistribute some of the Italian background's percentage values to some other population."* | **Open: how, and to whom.** |
| Other outdated country names | *"That is definitely a problem that needs to be addressed."* | **Found to be wide** (section 2); research and recalculation. |

## 2. What the atlas settles, and the outdated names it reveals

Read from the world atlas's `data/world/numbering.csv` (one row per nation in the latest period, with the author's
notes) and the Latin America source's `nations-assignment.csv`. Every one of the composition file's 43 nations was
checked against it.

**Russia's details, settled:**
- **Kaliningrad:** *"former Russian oblast, a nation of its own; Confederacy wave 1 (not in the Russian package)."*
  Leaving it out of Russia's successors was right; it is its own nation in the Confederacy of Intermarium Nations.
- **Karelia:** Finland's note: *"does NOT include the Republic of Karelia, which at C-15 joins Finland and is supplied
  by the Russia extraction."* So in the latest period the Republic of Karelia is part of **Finland**, not a separate
  piece. This is the October 29 research's "C-15" version (the Republic of Karelia to Finland, Murmansk to
  Idelsk-Uralia); runs 1–3 used its other version. Run 4 should use C-15.
- **Russia (the core state) includes the eastern-Ukraine slice:** *"core Russia plus the eastern-Ukraine slice
  (Luhansk, Donetsk, Kharkiv, Dnipropetrovsk, Zaporizhzhia in full; Kherson Oblast east of the Dnieper only)."* The
  people there come from today's **Ukraine**, so Ukraine's rows divide between Ukraine and Russia's core state.
- **Russia at Byrd, Palmer City and Contrapunto:** moot under the pool split (each successor gets its share wherever
  the old row is).

**The composition file's nations against the latest period:**

| Today's name in the city tables | In the latest period | What it means for the tables |
|---|---|---|
| China | Sinian Federation (with Hong Kong, Macau, Hainan) · Manchuria · Mongolia (with Inner Mongolia) · East Turkestan · Tibet; Taiwan separate | Section 4 |
| USA, Canada, Mexico, Argentina, Russia, Italy, Germany | already worked out (runs 2–3; Italy and Germany still to do) | Italy: **Sicilia is a separate autonomous-zone row** inside Meridia; Sardinia is in Meridia. Germany: **Austro-Bavaria is Austria plus Bavaria** |
| **Belgium** | **gone:** Flanders is in the **Netherlands**; Wallonia, Brussels and Luxembourg are in **France** | Belgium's rows divide between France and the Netherlands |
| **South Korea** | **Korea**, unified with the North (2111–2130), **without Jeju-do** (the International Court of Diplomacy's neutral ground, shared by Korea, Japan and the Sinian Federation) | Renamed Korea; the North adds people; Jeju-do comes out |
| **UK** | **United Kingdom without Northern Ireland**, which is a separate nation | A small Northern Ireland slice |
| **Czech Republic** | **Czechia** (Confederacy wave 2) | A rename only |
| **Spain** | Spain **without Catalonia and the Basque Country** (Biscay, Gipuzkoa, Álava and Navarre), both separate nations | Spain's rows divide three ways |
| **Brazil** | Brazil **without seven states** (Acre, Amapá, Amazonas, Mato Grosso, Pará, Rondônia, Roraima), which belong to **Amazonia** | Brazil's rows divide |
| **Indonesia** | Indonesia **without Aceh** (autonomous zone drawn as its own nation) **and West Papua** (independent; the six Papua provinces) | Indonesia's rows divide three ways |
| **Thailand** | Thailand **without the Deep South**: **Patani** (Pattani, Yala, Narathiwat), independent after the 2083 war | A small Patani slice |
| **Philippines** | Philippines **without Sulu** | A small slice; where Sulu goes is not named in the world table (to check in the Southeast Asia region notes) |
| **Romania** | Romania **without five counties** (Satu Mare, Bihor, Sălaj, Maramureș, Arad), which go to **Hungary** | Romania's rows divide between Romania and Hungary |
| **Ukraine** | Ukraine **without the eastern slice** (to Russia's core state) | As above |
| **Chile** | Chile **without five regions** (La Araucanía, Los Ríos, Los Lagos, Aysén, Magallanes), in the **Araucanía-Patagonia zone** | Chile's rows divide |
| Serbia, Bulgaria | Serbia includes Kosovo; Bulgaria includes Kırklareli (East Thrace) | Places with no pool of their own today join; small |
| Japan, Germany (without Bavaria), France, Netherlands, Sweden, Norway, Finland, Denmark, Australia, New Zealand, South Africa, Uruguay, Vietnam, Malaysia, Poland and the other Confederacy members | as today, apart from the changes above | No change to their rows |

## 3. Chile's part of the Patagonia zone, and Petén ("Is there a major city there?")

**Chile's five regions: yes, several real cities.** 2024 census (INE, first results, people counted): La Araucanía
1,010,423 · Los Lagos 890,284 · Los Ríos 398,230 · Magallanes 166,537 · Aysén 100,745, **together 2,566,219, about
13.9% of Chile's 18,480,432.** Cities (2017 census, the latest with city figures on the source found): **Temuco
with Padre Las Casas 278,513** · Puerto Montt 171,136 · Valdivia 150,727 · Osorno 147,826 · Punta Arenas 125,932 ·
Angol 48,911 · Coyhaique 49,968 (commune 57,823 in 2024). No metropolis (Santiago is millions), but Temuco is a
regional city of about 280,000 and four others are 125,000–170,000. *So Chile's row in each city would give about
14% of itself to the zone.*

**Petén: no major city.** About 596,000 people (official estimate, mid-2018), 640,000 projected for 2023. The main
urban center is the Flores–Santa Elena–San Benito area around Lake Petén Itzá; the municipalities of Flores (41,166)
and San Benito (50,701) together hold about 92,000. The largest municipalities are mostly rural (Sayaxché 94,212,
La Libertad 80,597, San Luis 74,813). *Guatemala has no pool in the composition file; at Guatemala's income level
Petén's effective pool would be very small, so it changes almost nothing in any city.*

Sources: INE Chile press release on the 2024 census first results; Emol's regional table; BCN (Coyhaique); City
Population (Chile cities; Petén municipalities). Searches logged in section 6.

## 4. China's pieces and Taiwan by the time-zone window

**Their numbers (headcount, as now ruled; from `03_Results.md`, Option A):** of China's ~210M pool, the Sinian
Federation 187.8M, **Manchuria 14.2M, East Turkestan 3.9M, Mongolia's Inner Mongolia part 3.6M, Tibet 0.6M.** Hong
Kong and Macau (8.2 million people together) join the Sinian Federation's pool, and Taiwan (23.4 million) and
today's Mongolia (3.5 million) need pools of their own: none of the four was ever in China's 210M, so each needs
its income and inequality figures (research, section 5).

**Solar time zones** (where the people live; round(longitude ÷ 15)): Manchuria +8 (east Heilongjiang +9) ·
Mongolia +7 (Ulaanbaatar, Hohhot, Baotou) and +8 (eastern Inner Mongolia) · East Turkestan +5 (Kashgar, Yining,
Hotan) and +6 (Urumqi, Korla) · Tibet +6 (Lhasa, Shigatse) · Taiwan +8.

**Cities inside each one's window (within three solar zones):**

| Piece | Cities in its window | Cities with a China row today that are OUTSIDE it |
|---|---|---|
| Manchuria | Davis, Zhongshan, Shirayuki, Sinheung, Kunlun, Mirny, Casey, Ariun Nuur, Relung Panen, Concordia, Dumont d'Urville, Denison, Janbogo, Zukelli, Cape Adare, Fort McMurdo, Scott (17) | Byrd, Dome Fuji, Mawson, Palmer City, Temirötkel |
| Mongolia | the same 17 plus Mawson (18) | Byrd, Dome Fuji, Palmer City, Temirötkel |
| East Turkestan | Utstein, Temirötkel, Dome Fuji, Mawson, Davis, Zhongshan, Shirayuki, Sinheung, Kunlun, Mirny, Casey, Ariun Nuur, Relung Panen, Concordia, Dumont d'Urville (15) | Byrd, Palmer City and the five Ross Sea cities (Janbogo, Zukelli, Cape Adare, Fort McMurdo, Scott), plus Denison |
| Tibet | Temirötkel, Dome Fuji, Mawson, Davis, Zhongshan, Shirayuki, Sinheung, Kunlun, Mirny, Casey, Ariun Nuur, Relung Panen, Concordia, Dumont d'Urville (14) | as East Turkestan |
| Taiwan | the same 17 as Manchuria | (never in China's row) |

*Amundsen Station sits at the Pole, where every zone meets; it is treated as reachable from everywhere, as its
present table already is.* Zhongshan and Kunlun are in every window but stay exempt.

**How they would be represented (proposal for run 4):**
- **The four mainland pieces** take their headcount slice of China's row (Manchuria 6.76%, East Turkestan 1.87%,
  Inner Mongolia 1.70%, Tibet 0.26%) **in the cities inside their window.** Where a city is outside a piece's
  window, that slice stays with the Sinian Federation's part of the row (the window rule's usual result). The
  Sinian Federation's decline (55–65%) applies to its own part only, as instructed; whether the pieces decline too
  is a question (Manchuria has China's lowest birth rates today).
- **Hong Kong and Macau** add to the Sinian Federation's pool before its decline.
- **Taiwan and today's Mongolia** are new nations: their pools set their national number, placed in the cities in
  their window in proportion to each city's population, with every city keeping its total (the others scale down
  to make room). Ariun Nuur is the one city in the windows with no China row; Mongolia already has a founder row
  there (4.19%).

## 5. Research for run 4 (proposed; not started)

**Unit A, pools for people never in the composition file's pools** (population, GDP per person and inequality
from official sources, each pool estimated by comparison with the composition file's existing nations of similar
income and inequality): Taiwan · Hong Kong · Macau · Mongolia · Austria · Guatemala (for Petén) · North Korea (for
Korea) · Luxembourg (into France) · Kosovo (into Serbia).

**Unit B, headcounts for the new splits** (latest official population by unit): Belgium (Flanders against
Wallonia with Brussels) · Northern Ireland · Catalonia and the Basque Country with Navarre · the seven Amazonian
states · Aceh and the six Papua provinces · Pattani, Yala, Narathiwat · Sulu (and where it goes) · the five
Romanian counties · Ukraine's eastern slice · Jeju-do · Sicilia · Bavaria (have) · the Republic of Karelia and
Murmansk (the October 29 research has them) · Chile's five regions (have, section 3).

**Then run 4:** headcount for every split; Karelia per the latest map; China's pieces and Taiwan placed by the
window; Hong Kong and Macau in the Sinian pool; Italy and Germany split; every outdated name mapped; Kunlun's Option A
with its co-founders; the four held-back cities committed with the rest; the national table rebuilt.

**Still waiting for the developer:** Canada's Demilitarized Zone; Zukelli's Italy (to whom); Kazakhstan,
Uruguay and Malaysia (research later); whether China's pieces decline too.

## 6. Search log (this session, continued)

| # | Search or page | Result |
|--:|---|---|
| 6 | `Censo 2024 Chile resultados población por región La Araucanía Los Ríos Los Lagos Aysén Magallanes INE` | Regional 2024 figures (INE release; Emol's table) |
| 7 | `Censo 2024 Chile población comunas Temuco Puerto Montt Valdivia Osorno Punta Arenas Coyhaique` | Only Coyhaique's 2024 commune figure (BCN); city figures not yet published for 2024 |
| 8 | `Petén Guatemala población censo 2018 INE municipios San Benito Flores Santa Elena área urbana` | Led to City Population's Petén page |
| — | Fetched: https://www.citypopulation.de/en/chile/cities/ | 1992/2002/2017 city figures (no 2024 column) |
| — | Fetched: https://citypopulation.de/en/guatemala/admin/17__petén/ | Department and municipality estimates for mid-2018 and the 2023 projection (no census count on the page) |

Eight searches this session in all, none refused.
