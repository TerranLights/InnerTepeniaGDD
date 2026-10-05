# CHANGES

## 2026-10-04 (later still) — map 13: Macquarie Island added (developer request)
- `data/meta_nodes.csv`: new possible node MAC (Macquarie Island) and status `external` link endpoints HOB (Hobart), DDU, CAD, ZUK; `data/meta_links.csv`: Hobart-MAC, MAC-DDU, MAC-Cape Adare, MAC-Zukelli, MAC-Casey. `render_13_meta_nodes.py` draws `external` nodes as small diamonds, labels only Hobart, and uses a wider extent (-3.5e6..3.9e6 x, -5.0e6..2.4e6 y) so Macquarie and Hobart fit. Backups: `*.bak-2026-10-04`. The island is not known to exist in canon; radio model pending.


## 2026-10-04 (later) — map 13 added: comms meta-nodes (developer request)
- `render_13_meta_nodes.py` -> `13_Comms_Meta_Nodes`: cities plus proposed (4) and possible (9) HF meta-nodes with great-circle hop lengths (WGS84 ellipsoid, so within about 0.4% of the spherical figures quoted in the research notes, e.g. Peninsula to Utstein 3,301 vs 3,288 km). Data in `data/meta_nodes.csv` and `data/meta_links.csv`: edit those to add, move or re-status a node, then re-run the script. Research behind the roles: `Locations/Towns/Open_Research_Topics.md`. Not canon.

## 2026-10-04 (later) — Hwy 4 rerouted around the head of Prydz Bay, LAND ONLY (developer request, second pass)
- **Problem:** Hwy 4 ran as a straight chord from Mawson to Sinheung (the Larsemann Hills / Tri-Cities junction): about 95 km over open water, and (after my first fix, which wrongly treated ice shelves as passable) about 200 km over the Amery Ice Shelf, which the developer reads as water. **Rule now: highways never cross open water or ice shelves; they stay on grounded land (rock and ice sheet).**
- **Fix (third pass, coast-hugging):** `data/highway_geometry.csv`, `hwy4` main line: after Mawson the route is a least-cost path over Natural Earth land minus ice shelves that is **rewarded for staying 9 to 35 km from the coast / shelf edge** (the second pass cut straight inland from Mawson): it follows the Mac. Robertson coast south from Mawson, then runs round the Amery Ice Shelf on its western and southern sides (down to about -73.4, 67.2) and back up its eastern side to the Larsemann Hills junction at Sinheung, approaching from the landward side. Hwy 4 is about 2,600 km (was about 1,780 km). Checked at 3 km spacing: no non-land samples except the Mawson and Sinheung city points themselves. Backups: `data/highway_geometry.csv.bak-2026-10-04` (original), `.bak-2026-10-04-v2` (ice-shelf-crossing fix), `.bak-2026-10-04-v3` (the straight-inland pass).
- **Not changed (flagged):** the first ~57 km of Hwy 4 from the Temirötkel Junction are still not on land (the junction point sits on the Syowa / Lützow-Holm coast in the base data); a land-only route there would be a 430 km detour (via -70.3, 39) and would split the shared junction with Hwy 7-ext and Hwy 37, so I left it.
- `render_all.py` now picks up every `render_NN_*.py` (it only matched `render_0*`, so maps 10 to 12 were skipped); all twelve maps were re-rendered (previous sets archived in `archive/`).

## 2026-10-04 (later) — map 12 added
- `render_12_town_focus_sites.py` -> `12_Towns_Sites_of_Interest`: the three sites the developer singled out, with dashed lines to the nearest city and dotted lines to the nearest highway (highway lines are traced from the developer's sketch, good to about ±20 km).

## 2026-10-04 — towns-candidate maps 06 to 11 added
- New data `data/town_candidates.csv` (68 rows: 32 Priority Batch 1 stations + 36 automatic weather stations, from `Locations/Towns/Data/Real_Station_Inventory_Crossmatched.csv`); new code `scripts/tepenia_towns_common.py` and `render_06` to `render_11`. Maps 01 to 05 untouched (new scripts were run singly, so nothing was archived).
- Scope per the developer's 2026-10-04 ruling: huts and field camps out; automatic weather stations at most comms posts; the 32 are the active and recently-closed stations outside the cities. Not a decision about any town.
- Name fix: AWS codes keep their capitals (AM 01, GC 46, LGB 00 ...); "Automatic Weather Station" shortened to AWS in labels.

## 2026-10-03 (batch 2) — four more renames applied (`DR-40`–`DR-43`)
- City ids and names: `port_lockroy` → `puerto_abrigo` (Puerto Abrigo) · `juan_carlos` → `pergamino` (Pergamino) · `sejong` → `contrapunto` (Contrapunto) · `vostok` → `ariun_nuur` (Ariun Nuur). Spur `spur_port_lockroy` → `spur_puerto_abrigo`; Mountain Pass's anchor `@hwy37:kunlun-vostok` → `@hwy37:kunlun-ariun_nuur`; Machu Picchu's served-city list updated. Notes on maps 2, 3 and 4 and the Temirötkel Junction / Santa Luce wording in the notes of maps 2 and 3 (missed in batch 1) corrected. The central scientific district inside Ariun Nuur keeps the name "Vostok" (`DR-42`); the maps show cities, not districts, so nothing changes there.
- All five maps re-rendered (previous set archived).

## 2026-10-03 (night) — all four renames applied (`DR-36`–`DR-39`)
- City ids and names: `abowasa` → `santa_luce` · `sayowa` → `temirotkel` (Temirötkel) · `princess_elisabeth` → `utstein` · `bunger_hills_city` → `relung_panen`. The Sayowa Junction is now **the Temirötkel Junction** (`temirotkel_junction`); spur ids `spur_sayowa` → `spur_temirotkel`, `spur_bunger_hills_city` → `spur_relung_panen`. No placeholder names remain, so the † / ‡ footer notes were dropped. All five maps re-rendered (previous set archived). `build_geometry.py` now uses the new ids; `highway_geometry.csv` was edited by id only (no shape changes).

## 2026-10-03 (evening) — Abowasa renamed Santa Luce (`DR-36`)
- `{{ Abowasa }}` → **Santa Luce** in `cities.csv`, `highways.csv`, `airports.csv`, `labels_full.csv` (id `abowasa` → `santa_luce`); the † placeholder mark is gone for this city. Maps re-rendered. The spec file on disk is still `Specs/Halley subnet/Abowasa.md` until the rename sweep is approved.

## 2026-10-03 (later) — Halley is a spur of Hwy 7
- Developer ruling: Hwy 7 passes **near** Halley and reaches it by a **connecting road**; it cannot run through the city because the ice moves constantly. `data/highways.csv`: `halley` moved from Hwy 7's main stops to its spurs; geometry rebuilt (`build_geometry.py --rebuild`; no hand edits existed) and all five maps re-rendered (previous set archived). Hwy 59's ramp still sits on Hwy 7 between Halley's spur and Abowasa.
- Written into `Locations/Infrastructure/Highways.md` the same day (Hwy 7 route and bullet, Endpoints table, new "Halley Connecting Road" section, Major Junctions row). Also written (developer approved) into `Cities/City_Relationship_Database.md` (Hwy 7 row; Abowasa, Belgrano and Halley neighbor lists; Belgrano's Hwy 59 note; the open-items line) and `Specs/Halley subnet/Halley.md` (`Access type` ON → SPUR, and the Highway access line).

## 2026-10-03 — first build (v1)
- Built the full pipeline and the five maps requested by the developer: cities only · cities + highways · cities + airports · cities + highways + airports · subnets.
- **Base:** Natural Earth 10m land, ice shelves, coastline, ice-shelf fronts; south polar stereographic.
- **Cities:** 38 (Palmer 8, Halley 8, Mawson 3, Mirny 9 incl. the placeholder-named Bunger Hills City, Janbogo 8, Byrd 1, Amundsen-Scott 1). Coordinates from each spec's `**Based on:**` line. Zhongshan and Sinheung share one coordinate (the specs say they are a few hundred meters apart), so they draw as one dot with separate labels.
- **Highways:** shapes traced from the developer's hand-colored sketch. The sketch was georeferenced by least squares against 17 real station dots (~6 px RMS, about 20 km), each highway's color mask was reduced to a centerline, then every stop was snapped to the real GPS of its city. Where the sketch's endpoint sat far from the real city (the Prydz Bay tri-junction ~400 km west of the real Larsemann Hills; Byrd ~160 km), the trace near the city was dropped and the line runs straight into the city. Spurs (Rothera, Puerto Abrigo, Palmer City by boat, Neumayer, Janbogo, Zukelli, Cape Adare, Fort McMurdo/Scott, Bunger Hills City, the Sayowa Spur) are straight lines from the nearest point of the parent line.
- **Airports:** 10 markers per `Airports.md` (its ten-marker reconciliation). Machu Picchu uses the real Machu Picchu Station coordinates; Mountain Pass is placed midway along Hwy 37 between Kunlun and Ariun Nuur; Zukelli/Janbogo and the Tri-Cities Airport sit at the mean of the cities they serve.
- **Subnets:** zones are convex hulls of 300 km buffers around member cities — schematic, not borders. Signy gets its own dashed ring and a dashed link to Palmer City (weak Arcanet link, per Signy's spec). The Pole is a dotted ring (relay, not a subnet territory).
- Placeholder names are marked on every map: `†` placeholder (Abowasa, Bunger Hills City), `‡` name to be replaced (Sayowa, DR-32).
- Earlier test renders were moved to `archive/2026-10-03_1552/`.
