# Datasheet & Pre-Trip Tracker — by subnet

**DRAFT. Created 2026-09-30; recounted 2026-10-21.** Bookkeeping only: it records **which cities have which instruction artifacts**. It
holds no findings and no content from any source. Counts below were taken from the live folders on the date above;
re-count before relying on a row.

**Pass folders live at:**
`/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/<Subnet>/<City>/`

## The three artifacts

| Artifact | What it is | Where | Built by |
|---|---|---|---|
| **Datasheets** | Instant-reference input: value + citation only, no synthesis. **19 files per city** (`Step_-1` · `Step_0` · `Step_1_and_2` · `Step_3` · `Step_5`–`Step_10` · `Phase_2`–`Phase_10`) | `<city>/Datasheets/` | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Mechanical_Extraction_Field_Guide.md` |
| **Pre-Trip sheet** | The city's own address book: every step and phase resolved to absolute paths, tested for existence | `<city>/00.0_Pre-Trip_Inspection.md` | `/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/PRE-TRIP_INSPECTION_RECIPE.md` |
| **Ledger** | Position-coverage bookkeeping, filled phase by phase | `<city>/00.2_Position_Coverage_Ledger.md` | created with the Pre-Trip sheet |

**Legend:** ✅ present · ⬜ absent · 🔸 partial · **n/19** = datasheet files present · **README row** = the city's own `README.md` carries the Field Guide's required "Datasheets — READ FIRST" row.
**Pass files** = how many of the city's real ULM output files exist (`00_Frame` … `10_Readiness_Check`, and the phase/gate/round files).

## Totals *(38 cities; Zhongshan has two trial folders, Opus and Sonnet)*

| | Count |
|---|---:|
| Cities with a full 19-file datasheet set | **33** — the 9 hand-built ones (Cape Adare, Casey, Davis, Denison, Dumont d'Urville, Kunlun, Mirny, Vostok, Zukelli) plus **24 generated 2026-10-21** (N-5, DRAFT) |
| Cities with a Pre-Trip sheet | **34 cities (35 folders)** — the 8 hand-built ones (Casey, Davis, Denison, Dumont d'Urville, Kunlun, Mirny, Vostok, Zhongshan with both trial folders) plus **26 generated 2026-10-21** (N-4) |
| Cities with neither artifact | **4** — Concordia (district method), Relung Panen (name confirmed; its specs and culture sheets are still to be synthesized), Shirayuki and Sinheung (ULM already done) |
| Cities with a Pre-Trip sheet but no datasheets yet | **0** (Zhongshan's two trial folders and the finished Tri-Cities hold none, by design) |

## Amundsen Station

| City | Datasheets | Pre-Trip | Ledger | Pass files | Notes |
|---|:-:|:-:|:-:|:-:|---|
| Amundsen Station | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | *(2026-10-21: its pass folder is empty, no `README.md` yet)* A research and relay outpost, not a residential city, per the census; counted among the 38 and has its own pass folder · Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |

## Byrd subnet

| City | Datasheets | Pre-Trip | Ledger | Pass files | Notes |
|---|:-:|:-:|:-:|:-:|---|
| Byrd | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |

## Halley subnet

| City | Datasheets | Pre-Trip | Ledger | Pass files | Notes |
|---|:-:|:-:|:-:|:-:|---|
| Abowasa | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | **now **Santa Luce****; pass folder keeps the old name; Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |
| Belgrano | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |
| Halley | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |
| Lazar | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |
| Neumayer | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |
| Princess Elisabeth | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | **now **Utstein****; pass folder keeps the old name; Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |
| Sanay | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |
| Troll | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |

## Janbogo subnet

| City | Datasheets | Pre-Trip | Ledger | Pass files | Notes |
|---|:-:|:-:|:-:|:-:|---|
| Cape Adare | ✅ 19/19 *(DRAFT)* | ✅ | ✅ | 0 | Built 2026-09-30 from primary sources, not T8-verified · absolute paths · README row ⏸️ pending approval · Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) |
| Concordia | ⬜ 0/19 | ⬜ | ⬜ | 0 | Hub city; its 13 districts use the **district** methodology, not this one |
| Denison | ✅ 19/19 | ✅ | ✅ | 0 | README row ✅ |
| Dumont d'Urville | ✅ 19/19 | ✅ | ✅ | 0 | README row ✅ · ⚠ **City flagged for revisit** (developer, 2026-09-30): not founded by France; datasheets will need rebuilding after the revisit. *(2026-10-21: the developer ruled it will get a new name in line with its Japanese founders; name not chosen; the spec's founders passages were corrected 2026-10-13.)* |
| Fort McMurdo | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |
| Janbogo | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |
| Scott | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |
| Zukelli | ✅ 19/19 *(DRAFT)* | ✅ | ✅ | 0 | Built 2026-09-30 from primary sources, not T8-verified · absolute paths · ⚠ Italy flagged for eventual census review · README row ⏸️ pending approval. *(2026-10-21: the developer ruled it will get a new name in line with its Australian founders; name not chosen; the spec's founders passages were corrected 2026-10-13, so these datasheets need a re-check.)* · Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) |

## Mawson subnet

| City | Datasheets | Pre-Trip | Ledger | Pass files | Notes |
|---|:-:|:-:|:-:|:-:|---|
| Dome Fuji | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |
| Mawson | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |
| Sayowa | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | **now **Temirotkel****; pass folder keeps the old name; Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |

## Mirny subnet

| City | Datasheets | Pre-Trip | Ledger | Pass files | Notes |
|---|:-:|:-:|:-:|:-:|---|
| Relung Panen | ⬜ 0/19 | ⬜ | ⬜ | 0 | **38th city; official name confirmed by the developer 2026-10-21** (formerly the placeholder `{{Bunger Hills City}}`). Its pass folder was renamed from `Bunger_Hills_City/` to `Relung_Panen/` on 2026-10-21. Its own specs, details and culture sheets are still to be synthesized; Pre-Trip, ledger and datasheets wait for that. |
| Casey | ✅ 19/19 | ✅ | ✅ | 0 | README row ✅ |
| Davis | ✅ 19/19 | ✅ | ⬜ | 19 | ULM complete; its ledger lives elsewhere or was never split out |
| Kunlun | ✅ 19/19 | ✅ | ✅ | 0 | README row ✅ |
| Mirny | ✅ 19/19 | ✅ | ✅ | 21 | *(recounted 2026-10-21: was 4)* ULM Steps −1 through 10 have been run; Step 10 recorded as "run, awaiting developer review"; Mirny is **not** declared complete. The folder holds 45 files in all, including the T8 round records and the Social Contract amendment register. |
| Shirayuki | ⬜ 0/19 | ⬜ | ⬜ | 19 | Tri-Cities; ULM already done without these artifacts |
| Sinheung | ⬜ 0/19 | ⬜ | ⬜ | 18 | Tri-Cities; ULM already done without these artifacts |
| Vostok | ✅ 19/19 | ✅ | ✅ | 0 | README row ✅ |
| Zhongshan (Opus) | ⬜ 0/19 | ✅ | ⬜ | 19 | Trial folder; ULM done |
| Zhongshan (Sonnet) | ⬜ 0/19 | ✅ | ⬜ | 6 | Trial folder; ULM partial |

## Palmer subnet

| City | Datasheets | Pre-Trip | Ledger | Pass files | Notes |
|---|:-:|:-:|:-:|:-:|---|
| Esperanza | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |
| Juan Carlos | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | **now **Pergamino****; pass folder keeps the old name; Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |
| Marambio | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |
| Palmer City | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |
| Port Lockroy | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | **now **Puerto Abrigo****; pass folder keeps the old name; Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |
| Rothera | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |
| Sejong | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | **now **Contrapunto****; pass folder keeps the old name; Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |
| Signy | ✅ 19/19 *(DRAFT, generated 2026-10-21)* | ✅ | ✅ | 0 | Pre-Trip + ledger generated 2026-10-21 (`Tools/build_pretrip.py`; alias set is a mechanical draft) · datasheets generated 2026-10-21 by `Tools/build_datasheets.py`; README row ✅ |

## Rules this tracker follows

- **Update a row in the same turn the artifact is written.** A row that says ✅ must be re-countable from the folder.
- **A partial set is 🔸 with the count**, never ✅. A missing file is a hole, not an exemption.
- **Datasheet rows also need the README wiring row** (Field Guide, second wiring step). Record it in Notes when the set is created.
- **This file is bookkeeping, not a canon source.** No pass reads it as an input.

## Build log

| Date | Event |
|---|---|
| 2026-10-21 | **N-5:** 19-file datasheet sets generated for the 24 cities that lacked them (`Tools/build_datasheets.py`; 456 files, DRAFT) and wired into each city's README (Amundsen Station's README was created; Cape Adare's and Zukelli's rows were added too). 33 cities now have a full set. |
| 2026-10-21 | Developer confirmed **Relung Panen** as the official name of the 38th city (the placeholder `{{Bunger Hills City}}` is retired); the row above now carries it. |
| 2026-10-21 | **N-4:** Pre-Trip sheet + ledger generated for 26 cities by the new `Tools/build_pretrip.py` (Casey's sheet as the template; every city row recomputed; runbook/spine line numbers re-located). Totals now **34 cities (35 folders) with a Pre-Trip sheet; 32 cities with a ledger; 9 with datasheets**. Skipped on purpose: Concordia (district method), Relung Panen (its specs and culture sheets are still to be synthesized), Shirayuki and Sinheung (ULM done). The 8 hand-built sheets are unchanged and carry stale line numbers (see the November To-Do, item N-4a). |
| 2026-10-21 | Founders lines refreshed in the datasheets of Zukelli, Dumont d'Urville, Denison, Kunlun, Vostok and Mirny (16 files plus one line), against the corrected specs and the Founding Register; Casey, Davis and Cape Adare were already correct. **Vostok's set still cites the renamed spec `Specs/Vostok.md` about 53 times (now `Ariun_Nuur.md`, lines shifted by two)**; fix with the rename sweep. Dumont d'Urville's and Zukelli's sets will need rebuilding when their new names are chosen. |
| 2026-10-21 | Recounted from the live folders (the first item of `Dev-Road-Map/November_To-Do.md`). Totals unchanged: **9 cities with a full 19-file datasheet set; 8 cities (9 folders) with a Pre-Trip sheet; 6 cities with a ledger** (Casey, Denison, Dumont d'Urville, Kunlun, Mirny, Vostok). Mirny's row updated; Amundsen Station, Dumont d'Urville and Zukelli notes added. The 38th-city placeholder folder is `Bunger_Hills_City`; Relung Panen has a dossier but no folder in `City_Development_Passes`. |
| 2026-09-30 | Tracker drafted from live folder counts. |
| 2026-09-30 | Cape Adare: 19 datasheets built (DRAFT), per `Mechanical_Extraction_Field_Guide.md`. |
| 2026-09-30 | Zukelli: 19 datasheets built (DRAFT). ±3 window ruled Notable-only, as written (developer; `DR-19`). |
