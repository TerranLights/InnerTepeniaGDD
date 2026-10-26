# Hand-over to the worldbuilding session: Santa Luce, the "two Italys," and what the GDD side needs

**Written 2026-10-23 by the Inner Tepenia GDD session, for the Claude session working on the novel repo's `worldbuilding/` folder.** The developer will work with you there. This file is self-contained: you do not need the GDD session's history. **Nothing here has been done in your repo, in the timeline repo, or in the map folders.** Everything below was done, or only read, on the GDD side.

---

## 0 · Read this first: the rules that bind this work

1. **Never write in the `TepenianUniverseTimeline` repo** (`/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/`). It is the authoritative, all-ruling canon and must be perfect; anything entering it must contain no mistake. Worldbuilding is done elsewhere and promoted only when finished, by the developer. (Developer, 2026-10-23.)
2. **Do not invent.** The developer's standing words about the CIN: *do not invent its member list, government or history. Ask, or read what has been written.* The same applies to Magna Lombardia and Meridia beyond what the map files record.
3. **No forced fit.** An empty slot is a result, not a gap. Do not fill a blank to look complete.
4. **One location on its own terms.** For city work, never compare a city to another city. (This governs the GDD side; it matters here only if profiles end up written per city.)
5. **Station-builder is not population origin.** A real station's builder is a coordinate, not a founder. Founders for Tepenian cities come only from the GDD's Founding Register.
6. **Culture is produced by time, place and local struggle applied to a stated composition.** Do not transplant a source culture intact, and do not refuse ethnic material. Act 1 (2564 to early 2600s): people are "X who live in Antarctica." Act 2 (late 2600s on): properly Tepenian; origin is ancestry, not identity. Differentiate locally, converge nationally.
7. **The developer prefers plain language.** They do not know internal code numbers (`DR-60` and the like); describe the thing, not its label. **American English** everywhere.
8. **Research thoroughly.** A recalled fact is a guess; a wrong fact is worse than a missing one. Query from several angles, log exact search strings and dead ends, and treat nothing as exhausted after one search.
9. **Operating hours (GDD side):** culture and city synthesis runs only 05:00 to 14:59 (wrap-up 13:59). Whether worldbuilding in your repo falls under that is for the developer; ask if it matters.
10. **Create freely, ask before changing or removing anything existing.**

## 1 · Why this hand-over exists (the situation)

The GDD is building a city called **Santa Luce** (Halley subnet, Queen Maud Land, Antarctica; formerly the placeholder "Abowasa"). Its founders were ruled (2026-10-01, and re-confirmed 2026-10-03) as **"Italy and the Confederacy of Intermarium Nations (CIN), jointly."** But Italy no longer exists in the developer's post-war map. It is two countries. The GDD needs to know **which** Italy, and then it needs the cultural stock of each founder, to rewrite Santa Luce's culture files and write its robot-culture sheet.

The developer asked where the actual post-war worldbuilding lives. It is **not** in the timeline repo (which has a First Interwar beat sheet and a world history, but nothing about Italy or Europe, and under `Worldspace/Locations/Earth/Upper_Earth/` only `Asia_East`). It is in your repo's `worldbuilding/` folder and in the developer's map project (section 4).

## 2 · The two Italys: what the developer's own files say

Source of record: `/home/kuroskalacs/Documents/Doll-Fi/media/y-files/Map Files/Europe/`, mainly `02 reorganization/03 follow-up - determining Western Europe/` (its `DECISION LOG - Confederacy of Intermarium Nations (membership order).md`, section 4f, and its `OPEN QUESTIONS - Western Europe (for the later European worldbuilding pass).md`) and the `Italy/` folder beside them (13 maps, `italy_maps.py`, `italy-provinces.geojson`, `Italy - Regional Data and Sources.md`, `Sardinia - North, South or Autonomous Zone (research).md`). The latest map and its README are in `04 follow-up - final map INIT 2083/`.

**Decided by the developer, 2026-09-30:** Italy splits into two countries at **Border B** (chosen over two other candidate lines, after a seven-principle comparison).

| | **Magna Lombardia** (north) | **Meridia** (south) |
|---|---|---|
| Territory | Toscana, Umbria, Marche and everything north of them (includes South Tyrol, now inside it) | Lazio, Abruzzo, Molise, Campania, Puglia, Basilicata, Calabria and Sicilia |
| Population (2026 estimate) | ~33.6 million | ~23.8 million without Sardinia (~25.4 million with it) |
| GDP per head (2023, nominal) | ~€42,300 | ~€28,000 |
| Capital | **Bologna** (political), **Milano** (economic, not formally decided) | **Roma**, with the Vatican inside, 52 km from the border |
| Special areas | none noted | **Sicilia is an Autonomous Zone** |
| Name origin | | "Meridia" is a coinage from Latin *meridies* ("noon, south"), echoing *meridionale*, *Mezzogiorno* and the *meridionalismo* ("Southern Question") |

**Still open in the developer's own files:** Sardinia's host (the developer doubts it should be an Autonomous Zone; the research note scores it South on 5 of 6 principles) · Meridia's internal arrangements and the Sicilia details · the Bologna-Milano relationship · South Tyrol's treatment · the names are decided but Magna Lombardia's formal capital arrangement is "not formally decided."

Other facts in the same folders: the **Confederacy of Intermarium Nations (CIN)** is "basically Eastern Europe, pretty much" (developer, 2026-10-01), with a membership-order decision log, 16 accession maps (Poland as the core, then 15 waves: Lithuania/Kaliningrad, Czechia/Slovakia, Latvia, Estonia, Belarus, Ukraine, Hungary, Romania, Moldova, Bulgaria, Croatia/Slovenia, Serbia, Montenegro/Bosnia, Greece, then "Skoprodija"). **Austro-Bavaria** (one country, two states, twin capitals München and Wien) is independent and not in the CIN. **Belgium** was split and absorbed into France and the Netherlands in the early 2100s (developer, 2026-10-01; the map already draws it at the 2083 start).

⚠ **Dating:** only East Asia's maps are dated near 2564. The Europe map is the *start-of-2083 initial* state. The developer's wording is that the maps are "solid, though still malleable, in-progress."

## 3 · The ruling made on the GDD side (2026-10-23)

**Question:** which Italy founded Santa Luce? Time-zone proximity (the Register's usual test) could not separate them, since both lie in the same longitude band. So the GDD compared **economic capacity**, using the repo's exile-eligibility rule (exiles were people who could afford robots or loved someone who did, so effective exile pool = population scaled by GDP per head, reduced for inequality):

- Population × GDP per head: Magna Lombardia ≈ €1.42 trillion, Meridia ≈ €0.67 trillion. Magna Lombardia carries about **2.1 times** Meridia's weight.
- The GDD's composition file carries pre-war Italy at ~27 million effective exiles. Split pro rata, that illustrates roughly **18 million (Magna Lombardia) to 9 million (Meridia)**. This is an illustration, **not a ruled ratio**.
- Meridia is not incapable of sending exiles; 9 million is comparable to nations that rank Notable or Significant elsewhere in the same file. Its poorer regions (Campania, Calabria, Sicilia at ~€21,000 to €23,000 per head, 14 to 17 percent unemployment) are much weaker than its one strong region, Lazio (~€41,700).
- Caveats: the figures are 2023, pre-war, and regional averages (no within-region inequality data). Economics only; it does not settle cultural fit.

**The developer's ruling (their words):** *"the population comes from both (proportionally, not necessarily equally), but the oversight, coordination, management, and logistics is determined by Magna Lombardia."*

Recorded on the GDD side as: **Italy's two successor states and the CIN, jointly; Italian population from both Magna Lombardia and Meridia in proportion to economic weight (exact ratio open); oversight, coordination, management and logistics are Magna Lombardia's.**

**One reading to confirm with the developer:** the GDD session took this to concern only the Italian side, leaving the **CIN's role unchanged**. It was not stated either way.

Recorded in: GDD `Worldspace/Locations-and-Levels/Universal_Location_Methodology/DEVELOPER_RULINGS_LOG.md` (the entry numbered `DR-60`), and the Santa Luce row of `Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Founding_Register.md`.

## 4 · Where things live (all absolute paths)

| What | Path |
|---|---|
| Timeline repo (canon; **do not write**) | `/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline/` |
| The First Interwar beat sheet (2083 to 2564) | `…/Timeline Eras/1 The First Interwar Period/Timeline.md` (no Italy or Europe content) |
| Timeline repo world history | `…/Reference/World_History_Reference.md` |
| Falkland Treaty draft | `…/Reference/Falkland_Treaty/` |
| Timeline repo Earth locations | `…/Worldspace/Locations/Earth/Upper_Earth/Asia_East/` (the only region there) |
| The standing "no stereotypes" law (full text) | `…/Reference/No_National_Stereotypes.md` |
| Your repo's worldbuilding | `/home/kuroskalacs/Documents/Doll-Fi/media/Literature/books/CurrentNovelDocs/worldbuilding/` (`nations/`, `history/`, `extractions/`, `METHOD - How Nations Get Drawn.md`, `STATUS - Cross-Session Progress Tracker.md`, `README.md`) |
| Developer's map project | `/home/kuroskalacs/Documents/Doll-Fi/media/y-files/Map Files/` (Europe is under `Europe/`) |
| The GDD's one-page summary of the maps by time zone | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Post-War_Nations_Founder_Reference.md` (a working summary, not canon; the map files are the authority) |
| GDD Santa Luce work list | `…/Cities/City_Development_Passes/Halley_Subnet/Santa_Luce/ROBOT_CULTURE_REVISIT_TRACKER_2026-10-23.md` |

**Not found anywhere (as of today):** a Europe nation profile, a character profile for Magna Lombardia, Meridia or the CIN, or a CIN member list written as a document (only the decision log and maps). Your `STATUS` tracker lists Europe as "Stage 1 done" (research notes, 14 of them, now in `Europe/01 initial generations/research/`) and the remaining stages untouched.

## 5 · What the GDD side needs from the worldbuilding side

The GDD will not wait on these and will not invent them. It uses whatever is settled and marks the rest open.

1. **Magna Lombardia and Meridia, as peoples and as post-war states:** the cultural stock of each (regional cultures, working and economic culture, language, religion), at the 2083-to-2564 time scale. Magna Lombardia's logistics and management tradition matters most, since `DR-60` gave it that role. Anything beyond the map files should be marked research or proposal until the developer decides.
2. **The CIN:** its member list and any cultural character the developer has settled. Also settle whether the older "Intermarium / Intermaria" bloc in the GDD's `Upper_Earth_Immigration_Composition.md` (members include Poland and Romania) is the same entity as the CIN. That is unconfirmed.
3. **The open Italian items in section 2** (Sardinia's host, Sicilia, Meridia's internal arrangements), only where the answer could change who sent people to Antarctica.
4. **Confirmation of the CIN reading in section 3.**

Nothing from this list is needed until the GDD's research resumes (see below).

## 6 · What the GDD side will do with it (so you can see what depends on what)

Santa Luce's **Local Cultures, Enneagram, Vision Notes and Neo-Races catalog** all still rest on the superseded Finnish-Swedish founding and must be revisited; its **Planet and Element symbols** are unassigned (it is the only city left out); then its **robot-culture sheet** can be written. Steps, with line numbers, are in the Santa Luce tracker named in section 4. The same "which Italy" question will be checked next at **Zukelli**, whose Founding Register heritage column says "Italian." The GDD's census and composition files keep pre-war "Italy" until all 38 city passes finish (the developer's rule).

**Timing:** the developer's weekly model allotment was at 98%. The GDD's web research is paused until it resets (about 23:00 on 2026-10-24); the tracker defaults to resuming at 05:00 on 2026-10-25.

## 7 · Facts this session verified versus did not

**Read directly from the developer's files and the GDD (reliable):** the Border B composition, populations, GDP per head, capitals, Sicilia's status, the CIN accession order, the `DR-60` wording, the Register row, and every path in section 4 (each was listed or opened during this session).

**Computed by the GDD session (check if you rely on it):** the €1.42T and €0.67T products and the 2.1× ratio (population × GDP per head from the developer's table; Meridia taken without Sardinia), and the illustrative 18M to 9M split of the 27M pool.

**Not checked:** anything about Magna Lombardia's or Meridia's culture, economy or institutions after 2083; any CIN member beyond the accession-order list; whether the Europe maps have changed since their last recorded stage.
