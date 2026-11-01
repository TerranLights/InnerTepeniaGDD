# Esperanza: site size and education figures (research log, 2026-11-01)

Requested by the developer during the Esperanza walk-through (2026-10-31). Two parts: (a) how much ground Esperanza has, (b) what the medical-institutes file and its neighbors should say now that the census has changed. **No existing file was edited by this research.** Decisions are listed at the end.

## (a) Site size

### Required area (arithmetic)

| Census | Population | Area at 10,000/km² | Area at 7,000/km² |
|---|--:|--:|--:|
| Census I | 1,902,205 | 190.2 km² | 271.7 km² |
| Census II | 1,193,886 | 119.4 km² | 170.5 km² |

The 7,000–10,000/km² band comes from `Extent_and_Area_APPROACH.md` (L330), reached independently at Signy, Marambio and Dumont d'Urville.

### What the real ground gives

| Fact | Value | Source |
|---|---|---|
| Hope Bay (the water) | 3 nmi × 2 nmi = 5.6 km × 3.7 km | Wikipedia, Hope Bay, Antarctica (1976 Sailing Directions gives a narrower figure) |
| **Hope Bay ice-free ground** | **about 4 km²** | Poeiras et al. 2026, *Anais da Academia Brasileira de Ciências* 98(3), "Plants, algae and lichens communities of Hope Bay": *"The site holds approximately 4 km2 of ice-free area."* Vegetation covers about 12% of it. |
| Hope Bay IBA (bird area, eastern side) | 2.03 km² | BirdLife / Key Biodiversity Areas factsheet |
| Esperanza Base | about 55 winter inhabitants; Uruguayan summer station Elichiribehety also on the bay | Wikipedia |
| Tabarin Peninsula | 28 km long, 9.3–22.2 km wide, lies SOUTH of the Hope Bay–Duse Bay trough (Depot and Mondor Glaciers fill the trough) | Wikipedia, Tabarin Peninsula |
| Nearby relief | Mount Flora 520 m, Mount Taylor 1,000 m, Twin Peaks 750 m, Scar Hills ~200 m | Wikipedia, Hope Bay |
| Ulu Peninsula, James Ross Island | about 250 km² of ice-free ground mapped (northern sector); "the largest deglaciated area in the Antarctic Peninsula region" | Jennings et al. 2021, *Journal of Maps* 17(2), 125–139 |
| Ice-free share of the Peninsula | about 3% of the Antarctic Peninsula and offshore islands | Hughes et al. 2015, as summarized by a secondary source |

The bay's 5.6 × 3.7 km is water. The first-guess area of about 21 km² is not land.

### Distances (great circle, from Hope Bay about 63.40°S 57.0°W)

| To | km |
|---|--:|
| Vega Island (about 63.85°S 57.4°W) | 54 |
| Ulu Peninsula, Cape Lachman area (about 63.80°S 57.88°W) | 62 |
| Ulu Peninsula, southern lobe (about 64.1°S 58.0°W) | 92 |
| Seymour Island | 99 |
| Snow Hill Island | 123 |

(Coordinates are approximate. The Prince Gustav Channel crossing is shorter from the Duse Bay side than from Hope Bay.)

### Findings

1. **Hope Bay's own rock holds about 4 km², about 1.5–2% of what Esperanza needs.** Esperanza cannot sit on Hope Bay's bare ground.
2. **The "no rock" argument does not apply.** Developer rule (2026-10-04): cities may stand on ice; only ice speed matters, and no speed threshold has been set. Rock area is not a size test.
3. **The James Ross reservation is not as close as the Extent file's wording suggests.** The Ulu Peninsula is roughly 60–90 km from Hope Bay, across a channel and the Tabarin Peninsula's flank. It is a second site, not a bridgehead.
4. **Ice speed near Hope Bay: NOT FOUND.** Searched thickness and velocity for Mott Snowfield, Arena Glacier, Depot Glacier and the Tabarin ice cap, standard and extended, and found none. This is a dead end at the sources, not at the query. A velocity dataset (for example the MEaSUREs Antarctic ice-velocity maps) would have to be read directly.
5. Tabarin Peninsula alone (28 km × 9–22 km) is larger than the required area, but it lies south of Esperanza's own bay.

### Options for the developer

| Option | What it means | Cost |
|---|---|---|
| **A. Two-site city** | Hope Bay core (port, Institute, Hwy 1 terminus) plus the Ulu Peninsula for the bulk of the housing; joined by road over the Prince Gustav Ice Shelf or a causeway | The Extent file already reserved the ground; the road is a 60–90 km structure that the file calls fragile |
| **B. Spread over ice** | The city runs inland over the Trinity Peninsula ice at 7,000–10,000/km² | Needs ice speed and thickness data that was not found; fits the cities-on-ice rule |
| **C. Lower the population, relocate the difference** | Move part of the 1.9 M elsewhere | The developer already named this as a possibility; it is a population-work decision |
| **D. Combination** | Smaller Esperanza on Hope Bay plus Tabarin plus ice, with some relocation | Needs the population work first |

## (b) Education figures

| Item | Old | New | Arithmetic |
|---|---|---|---|
| Esperanza education sector, whole-workforce basis (NMCI L176, DoI README L189, `Phase_4` row) | 350,155 | 211,198 | 25% × 844,793 distinctive tier (`16` §11) |
| Students taught at the file's 1:12 ratio | "four million" | about 2.5 million | 211,198 × 12 = 2,534,376 |
| "Twelve times its own need" (DoI README L189) | 350,155 vs 29,615 = 11.8× | 211,198 vs 29,616 = **7.1×** | own schooling 24,839 + childcare 4,777 = 29,616 |
| Institute student body share (NMCI L173) | "about 2% of a 1.88 M city" | **1.99%** of 1,902,205; 3.17% of Census II (1,193,886) | 37,800 ÷ population |
| Mandated half of the education sector | 105,599 | unchanged | 12.5% × 844,793 |

Notes:
- The 844,793 figure and the 1.40 M workforce behind it still rest on the old Census I (1,878,287). The Division-of-Industry rows are rebuilt in the population work, so the new numbers above are the "§11 basis" values, not final ones.
- 2.5 million students is more than the city's population. At 1:12 this is teaching capacity for national tertiary and child-rearing work, not enrollment.
- NMCI is locked canon. L173 stays true at 1.99% on the new count; L176 is the only line that changes.

## Decisions needed from the developer
1. Option A, B, C or D for the site (and whether to run a velocity-dataset search for ice speed first).
2. Whether to edit NMCI L173 ("1.88 M" → "1.90 M"), L176 (211,198 workers, about 2.5 million students), DoI README L189 ("seven times"), and the `Phase_4` row, now or after the population work.
3. Marambio spec L58 (Esperanza's old population) waits on the same choice.

## Developer decision (2026-11-01)
**Option D, a combination:** a smaller Esperanza on Hope Bay plus Tabarin Peninsula plus ice, with some relocation of population. It depends on the population work, so the education-line edits (NMCI L173/L176, DoI README L189, `Phase_4` row), Marambio spec L58 and the Esperanza extent declaration are HELD. Open: ice speed and thickness near Hope Bay and Tabarin (velocity dataset); the Ulu Peninsula's role.
