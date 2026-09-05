# City Master Reference — Index

> **Built 2026-09-02.** Five parallel compiles, one per subnet, covering **all 37
> established cities/entities** in `Worldspace/.../Tepenian-Federation/Locations/Cities/`.
> **Purpose:** a single place to find everything already established about a city before
> making an assessment — most immediately, the per-city division-of-industry pass
> (`Division_of_Industry/16_Per_City_Three_Tier_Run.md`).

---

## ⭐ NATIONAL-SCOPE REFERENCE MATERIAL — not city-specific, useful for every assessment

**Added 2026-09-02, outside the `Cities/` tree, at the developer's direction — these are
not tied to any one city and should be checked whenever they're relevant, not just once.**

### `Reference/Images/Maps/` — visual ground truth

| File | Use |
|---|---|
| `Antarctica_highway_map_by_topology.jpeg` | The highway network by topology — cross-check against `Locations/Infrastructure/Highways.md` |
| `Antarctica_map_by_station_by_national_country_possession_A2917745...png` | Real-world station/nation map, pre-edit — the base layer every founding-nation assignment traces back to |
| `Tepenian airport and flight map.jpeg` · `...- highway overlay.jpeg` | The confirmed airport list's own source image, both plain and overlaid on the highway network — see `Locations/Infrastructure/Airports.md` |
| `Tepenian Arcanet subnet map by region.jpeg` | The subnet boundaries, visually |
| `North America with tentative labels.jpg` | ⚠ Scope unclear — not yet cross-referenced against any Tepenian content; flag if found irrelevant |

**City-specific, not general — do not treat as national reference:**
`Concordia-City_Color-Coded_map_by_District_-_Player_Paths.jpeg`,
`Concordia_City_-_Extended_map_-_with_labels...jpeg`,
`Concordia-City_Main_Quest_Trajectory_Map_2026-07-10.html`,
`Concordia_City_viewed_from_the_air_-_banner_image.jpeg` — all Concordia-only.

### `Reference/Real-World/` — ⭐ **FOUR** general-purpose folders *(was three — corrected 2026-09-03)*

> # ⛔⛔ CORRECTION 2026-09-03 — **`Climate Data` IS NOT EMPTY. It holds 37 files.**
>
> **This section read *"the empty `Climate Data`"* and listed it among six subfolders *"confirmed out of
> scope for this index."*** ***It contains `Climate Data/READER/` — 37 per-city climate files, BAS READER,
> WMO 1991–2020 standard normals, individually cited.***
>
> ### The timeline is the point
> **READER was committed `2026-07-04`. This index was written `2026-09-02` — two months later — and declared
> the folder empty.**
>
> ### The cause, and it is mechanical rather than careless
> **A listing of `Climate Data/` returns exactly one entry: `READER`, a DIRECTORY. No `.md` files at the top
> level.** ***A shallow check sees no files and concludes "empty."***
>
> > **⚠ THE SAME BUG WAS MADE INDEPENDENTLY A SECOND TIME, on 2026-09-03**, by an audit script testing for
> > per-city concept art: **it matched FILENAMES, and the art is stored in per-city DIRECTORIES**, so it
> > reported `0 of 37` — a total-gap claim that was false. ***Two different sessions, two months apart, same
> > error: a container mistaken for an absence.***
> >
> > **The rule that follows: when a check returns "empty" or "zero," confirm the instrument descends.**
> > *`04` Part IV already says a scan is worthless until proved it could find a hit; this is that rule for
> > directory trees.*
>
> **Consequence:** ***the strongest `G2` supply in the project sat unregistered and declared out-of-scope for
> two months.*** **Now registered in `00_RUNBOOK.md` §C.9 and at the point of use in §C.8c Phases 1 and 3.**

*(The other five subfolders — `Davis_Geosciences_Research`, `Ice-Cold_Buddhism_Research`,
`Pisces_Flood_Mechanism_Research`, `PTSD_Military_Trauma_Research` and
`Vostok_Genetics_Research` — are single-city or single-character research, confirmed out of
scope for this index by the developer.)*

| Folder | Contents | Use |
|---|---|---|
| ⭐⭐ **`Climate Data/Precipitation_Falls_vs_Lands.md`** | **THE precipitation reference.** Four distinct quantities — *falls aloft · reaches the surface · accumulates · gauge-caught* — differing by **more than an order of magnitude**, with the mechanism, the published coefficients, and a falls-vs-lands figure for **all 37 cities** | **Phases 1 and 3; any weather, construction, agriculture or daily-life writing.** ⛔ **READ THIS BEFORE USING ANY PRECIPITATION NUMBER.** *Amundsen Station's gauge reads 2.1 mm against ~70–80 mm of actual accumulation — the gauge catches ~3%.* ⭐ **The controlling variable is WIND, not cold: Vostok and Denison are equally cold and are opposite weather experiences** |
| ⭐ **`Climate Data/Climate_Data_Corpus_Audit_2026-09-04.md`** | The 37-city audit: what was wrong, what was corrected, and per-column provenance policy | Read before trusting any pre-2026-09-04 climate figure |
| ⭐ **`…/Cities/Research_Logs/Climate_Data_Research_Log.md`** | Every verbatim search string, every source accepted and rejected, every snag, across eight sessions | ⛔ **Check the rejected list before researching climate** — it records which sources are dead ends and why |
| **`to-be-integrated/climate data CURL/ncei/`** | Raw NCEI GSOM + GHCN-Daily archive data as downloaded | For re-deriving any figure. ⚠ **tenths of a degree; apply the gap rule for outliers** |
| ⭐ **`Worldspace/Robot_Biology_and_Culture/Robot_Cold_Physiology.md`** | What cold costs a robot — recharge, capacity, embrittlement | Phases 3–4, and any Frostlands or high-latitude survival writing |
| ⭐ **`…/Concordia-City/Concordia_Altitude_and_Atmosphere.md`** | What altitude costs a human at Concordia — no acclimatization; heated, not pressurized | Phases 1, 4, 9; any Concordia human-population writing |
| ⭐ **`Climate Data/READER/`** *(38 files)* | Per-city monthly mean temperatures — **BAS READER, WMO 1991–2020 standard normals**, each with its climate authority, data period and citation | **`G2`, Phases 1 and 3.** ⛔⛔ **MOST FILES ARE NAMED FOR THE REAL-WORLD STATION, NOT THE TEPENIAN CITY** — `Aboa.md` *(Abowasa)*, `Princess_Elizabeth.md` *(note the `z`)*, `Sejong.md` *(King Sejong)*. ***A search by city name can return a confident false negative; use the ALIAS SET.*** *(`Bharati_TBD.md` was renamed to `Shirayuki.md` 2026-09-04 — that particular trap is closed.)* ⚠ **Temperature ONLY in most files — no precipitation, no daylight** *(checked 2026-09-03)*; **the four written or rewritten 2026-09-04** — `Denison` *(created)*, `Shirayuki`, `Port_Lockroy`, `Juan_Carlos` — **also carry precipitation, daylight and proxy provenance.** **Denison's gap is closed.** |
| **`Industry_Staffing_and_Productivity/`** | MCAA Labor Productivity Factors (Ibbs & Sun, ASCE 2016) — the sourced basis for the whole difficulty layer; its in-depth companion critique; a wastewater-plant staffing guide (image-only PDF, not yet OCR'd) | Already consumed by `Division_of_Industry/08` §4.1, §6.4b. **The README inside names unobtained sources worth a future session** — RSMeans location factors, AWWA staffing benchmarks, CRREL cold-regions studies, McMurdo's functional staff breakdown |
| **`jobs_professions_and_fields/`** | The full SOC 2018 manual (23 major → 98 minor groups) plus derived cross-category and district-matching notes | The source behind the SOC cross-check that found four missing industries in the 22-industry register (`00_Necessary_Industries_Register.md`) |
| **`Stations/`** | `Antarctic_Stations_With_Airstrips.md`, the COMNAP Antarctic Station Catalogue (PDF) | The founding/real-world-basis reference for any city — **note `Locations/Infrastructure/Airports.md`'s own caveat: this list is background reference only, not a predictor of Tepenia's own airport network**, which was confirmed separately from the developer's own map |

---

### ⭐⭐ `Universal_Location_Methodology/` — **the input roster, the audit, and the to-do.** Added 2026-09-03

**This index answers *"what already exists for this city."*** ***These three answer the inverse — "what is
REQUIRED, and which cities do not have it."*** **Read them together; neither half is complete alone.**

**Base:** `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/`

| File | What it is | Use |
|---|---|---|
| **`ULM_Input_Required_Reference.md`** | **THE BAR** — every input the ULM cannot produce for itself: Tier 0 blocking · Tier 0b · the eight Tier 1 generators · Tier 2 · 21 Tier 3 particulars · per-phase canon targets · RESERVED · the three admissibility axes. **Each row: a verified ABSOLUTE address and a MECHANICAL presence test** | **Before assessing any city**, to know what it is supposed to have |
| **`ULM_Input_Available_Audit.md`** | **THE MEASUREMENT** — all 37 cities checked against that bar, organized by subnet | To see, per city, what is absent. ⚠ **Read its SCOPE-CORRECTIONS box first** — four fields were struck after measurement and their rows are stale by design |
| **`Location_Data-Input_To-Do.md`** | **THE RANKED LIST** — what is still missing, ordered by how many cities lack it, with stated tie-breaks | ⚠ **Carries a blind-spot warning: *when the count and the tier disagree, the tier wins.*** Also a `Removed` section — **four fields are NOT requirements; do not re-add them** |

> ### The headline the audit produced, because it bears on every city in this index
> ***No city has a declared EXTENT — 0 of 37.*** **`01` §2 requires both a population band and an extent
> band; `00_RUNBOOK.md` Step 2 orders the division; `04` Gate 11's only recorded catch came from it.**
> **Six cities carry an area figure and NONE is a city extent** — each measures the real-world *site*.
> ⚠ **Sayowa's own spec has already run the division and recorded `~50,000/km² — the implausibility`.**
> **`density = Census I ÷ extent`, and Census I is complete for all 37 — so fixing either variable derives
> the other for the whole corpus. It is one ruling, not thirty-seven.**

---

## ⛔ THE CANON-TIER LEGEND — read this before citing anything below

**Applied uniformly across all five files. One correction was made mid-compile and is
recorded here rather than silently absorbed:**

| Tier | Sources | Meaning |
|---|---|---|
| **✅ CANON** | `Specs/*.md` · `Local_Cultures/**` · `Official_Population_Census.md` · `City_Relationship_Database.md` · `City_Cross_Subnet_Relationships.md` · `Station_to_City_Map.md` · `National_Medical_and_Care_Institutes.md` · any `Division_of_Industry` figure marked RELIABLE or a developer ruling | Settled fact |
| **⚠ VISION NOTES** | `City_Vision_Notes/*.md` | Developer-sourced and real, but pre-synthesis — most is already folded into Specs/Local_Cultures verbatim |
| **🔴 DRAFT / NOT CANON** | `City_Megasheets/**/*_Full_Extrapolation.md`, `*_Cross_Reference_Synthesis.md` — the folder's own README calls these *"the invention pass"* and *"the implication-hunting pass"* · **any vignette or Course_of_Events-style narrative content, wherever it appears, including when cited secondhand inside another file that presents it confidently as settled** | Unreviewed invention. **Per the developer's explicit instruction this session: vignettes are not canon, full stop — regardless of how the source frames them** |
| **🛠 DESIGN TOOL** | `City_Enneagram_Personalities/*.md` · `City_Symbolic_Substrate/*.md` | Analytical/thematic layers, not narrative fact |

### ⚠⚠ CORRECTION MADE DURING THE COMPILE — `Local_Robot_Culture/**` is NOT canon-tier

**The original brief given to all five forks classified `Local_Robot_Culture/**` as ✅
canon.** Two forks (Janbogo, Palmer) caught this independently by reading the files
themselves: **every `Local_Robot_Culture` file self-declares *"Provisional — findings
are proposals for developer review, not asserted canon"* in its own header.**

> **Correct tier: 🔴 DRAFT — provisional by the source's own declaration.** Downgraded
> throughout. **This is not a minor label fix** — it means every robot-elemental
> assignment, every robot-culture reading cited from this folder anywhere in the five
> reference files, is a *proposal*, not a settled fact, until reviewed.

---

## What exists — the full file inventory under `Cities/`

**488 markdown files, 11 categories, plus 16 top-level cross-city files.**

| Category | Files | Canon tier | Coverage in this compile |
|---|--:|---|---|
| `City_Megasheets/` | 252 | 🔴 mostly, per-component *(see below)* | Existence + category noted everywhere; deep-read selectively — see per-subnet notes |
| `Local_Cultures/` | 40 | ✅ | Read in full, all 37 |
| `Specs/` | 38 | ✅ | Read in full, all 37 |
| `City_Enneagram_Personalities/` | 38 | 🛠 | Read directly for the richer entries; cross-reference-table pulls elsewhere |
| `City_Vision_Notes/` | 37 | ⚠ | Read in full, all 37 |
| `Local_Robot_Culture/` | 35 | 🔴 *(corrected — see above)* | Read in full or selectively per subnet; {{Abowasa}} has none |
| `Division_of_Industry/` | 18 | ✅ *(ruled figures)* | Cross-referenced throughout — this is the compile's other input |
| `Research_Logs/` | 5 | 📋 process log | Not deep-read; exists for future research passes |
| `City_Symbolic_Substrate/` | 4 | 🛠 | Read once per subnet, entries extracted |
| `Local_Robot_Culture_Methodology/` | 4 | 📋 methodology | Not deep-read |
| `City_Concept-Art/` | 1 | — visual assets | Not relevant to this compile |
| **Top-level loose files** | 16 | mostly ✅ | `Official_Population_Census.md`, `City_Relationship_Database.md`, `City_Cross_Subnet_Relationships.md`, `City_National_Connections.md`, `City_Refugee_District_Affinities.md`, `Station_to_City_Map.md`, `National_Capital_Candidates.md`, `National_Medical_and_Care_Institutes.md`, `Upper_Earth_Immigration_Composition.md`, `Bunger_Hills_City/Development_Brief.md`, plus process/audit files *(`Full_City_Integrity_Check.md`, `Founding_Nation_Bug_Investigation_Methodology.md`, `Division_of_Industry_Sweep_2026-08-31.md`, `Investigation_Loop_Round2_Tracker.md`, `Inspirational-Influences.md`, `Overview.md`)* |

**Megasheet component breakdown** *(each city folder holds up to 6 files)*:

| Component | What it is | Tier |
|---|---|---|
| `[City]_Mega_Init.md` | Step 1 — restates already-established material | 🔴 pipeline synthesis, higher confidence than the two below |
| `[City]_Full_Extrapolation.md` | Step 2 — **"the invention pass"** | 🔴 draft, unreviewed |
| `[City]_Cross_Reference_Synthesis.md` | Step 3 — **"the implication-hunting pass"** | 🔴 draft, unreviewed |
| `[City]_Community_Infrastructure.md`, `[City]_Physical_Infrastructure_Attributes.md` | Supporting detail sheets | 🔴 draft |
| `README.md` | Concatenation of all of the above | 🔴 draft *(inherits the tier of its contents)* |

**Not searched, per explicit scope:** `Background-Lore/Cities/**` — the Course of Events
and historical-vignette tree. It exists but sits outside `Worldspace/.../Cities/`, and
its content is non-canon regardless.

---

## The five subnet references

| File | Subnet | Cities/entities | Lines |
|---|---|--:|--:|
| [`Halley_Subnet_Reference.md`](./Halley_Subnet_Reference.md) | Halley | Neumayer, Halley, {{Abowasa}}, Troll, Sanay, Belgrano, Princess Elisabeth, Lazar | 354 |
| [`Janbogo_Subnet_Reference.md`](./Janbogo_Subnet_Reference.md) | Janbogo | Denison, Concordia, Dumont d'Urville, Cape Adare, Zukelli, Fort McMurdo, Janbogo, Scott | 350 |
| [`Mirny_Subnet_Reference.md`](./Mirny_Subnet_Reference.md) | Mirny | Vostok, Mirny, Zhongshan, Shirayuki, Davis, Sinheung, Casey, Kunlun | 307 |
| [`Palmer_Subnet_Reference.md`](./Palmer_Subnet_Reference.md) | Palmer | Marambio, Signy, Esperanza, Sejong, Juan Carlos, Palmer City, Rothera, Port Lockroy | 373 |
| [`Mawson_Byrd_Amundsen_Reference.md`](./Mawson_Byrd_Amundsen_Reference.md) | Mawson · Byrd · Amundsen | Mawson, Sayowa, Dome Fuji, Byrd, Amundsen Station | 262 |

**37 cities/entities. {{Bunger Hills City}} deliberately excluded — deferred on purpose,
per `Division_of_Industry/15_Open_Items_and_Three_Resolutions.md` List A item 2.**

---

## ⭐ Cross-cutting findings — things that matter beyond any one city

1. **⭐⭐ Two of the "ten estimates" in `16`'s provenance table were never estimates.**
   The Janbogo compile independently re-verified: **Denison's and Cape Adare's 25%
   mandates are genuine canon §15 figures.** *(Already caught and corrected in `16`'s
   provenance section on 2026-09-02; the big Half B table's `src` column was still
   showing `H` for both rows and has now been fixed to `C` in this same pass.)*

2. **Structural gaps confirmed, not caused by this compile:**
   - **Concordia** has no `Local_Cultures`, `Enneagram`, `Local_Robot_Culture`, or
     `Megasheet` entry at all — special-cased as the present-tense, ongoing primary
     setting rather than a "died in the war" pipeline city.
   - **{{Abowasa}}** has no `Local_Robot_Culture` pass, pending a known founding-nation
     consistency fix.
   - **Byrd's and Amundsen Station's** megasheet folders both lack a `README.md` — every
     other city folder has one.

3. **⚠ Live, unresolved bug, flagged not fixed** *(out of this compile's scope)*:
   **Sejong's** 2026-08-02 Hangul-founding-population fix was applied to some files but
   not all — `Sejong_Community_Infrastructure.md` and two Background-Lore files still
   carry the invalidated premise.

4. **✅ A correction already in memory, confirmed independently.** Signy's Specs text
   claims humans *"can sustain themselves indefinitely"* on Scotia Sea marine resources.
   The food model (`Division_of_Industry/14`) caps marine capacity at ~16–17% of national
   calories/fat — the claim doesn't hold as stated. Already recorded in
   `project_city_post_cultures` memory; the Palmer compile found and cross-referenced
   the same issue independently, which is a good consistency check rather than a new
   finding.

5. **Economic identity, ranked by how open it still is:**
   - **🔴 Lazar** — the standout. The developer's own words in its Specs file: what
     drives its megacity-scale economy is *"explicitly unresolved and flagged as needing
     real development, not just a placeholder gap."* Confirmed independently by the
     Halley compile. Its distinctive-tier workforce alone exceeds the nine smallest
     Tepenian cities combined.
   - **🔴 Palmer City** — its own source file states outright: *"economic foundations
     beyond entertainment/hospitality remain TBD… a reasonable working estimate, not
     confirmed canon."*
   - **⚠ Dome Fuji** — the seed-archive mandate (14.5–20% in `16`) independently flagged
     by the Mawson/Byrd/Amundsen compile as *"likely too high."* Consistent with `15`'s
     own note that 10% is probably closer.
   - **⚠ Zhongshan** — the maritime-port 20% is confirmed as my own Half A estimate, not
     canon, but the compile notes it *"has a real candidate answer,"* unlike Lazar.
   - **⏸️ Sejong / Juan Carlos** — whether Juan Carlos shares Sejong's Machu Picchu
     Airport border-gateway role is still open, pending developer ruling
     (`16`, Sejong/Marambio ruling section).

6. **⭐ Byrd's geological reclassification, restated for visibility.** Ice-sheet, not
   rock-founded — 2,164 m of ice to bedrock, a real-world fact caught this session
   (`13` §15). It is now a forced food importer in the national model, a status change
   from what would otherwise have been assumed.

---

## How to use this

**For a per-city assessment** *(the division-of-industry pass, or anything else)*: open
the relevant subnet file, read that city's section top to bottom — it already separates
canon from draft from design-tooling, so nothing needs re-sorting. **Cross-reference
`Division_of_Industry/13`, `15` and `16`** for the economic figures; this reference
supplies everything else — geography, founding, culture, notable locations, open flags.

**Do not cite 🔴-tier content as fact in a Spec or Local_Cultures file.** It exists to
show what's *been proposed*, not what's settled — including, now, everything under
`Local_Robot_Culture/`.
