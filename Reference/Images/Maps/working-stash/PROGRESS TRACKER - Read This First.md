# Tepenia maps — Progress Tracker (read this first in any new session touching these maps)

**Last updated 2026-10-03.** Requested by the developer: *real Antarctica with real GPS as the base layer; a series of Tepenia maps in `working-stash/` with every city labeled, plus highways and airports; then keep the maps updated as the nation and city data change.* The developer specified the set: **cities only · cities + highways · cities + airports · cities + highways + airports · subnets.**

## The standing rule
**Whenever city, nation, highway, airport or subnet data changes anywhere in the project, update the matching CSV here and re-render** (`scripts/render_all.py`). Triggers: a city renamed or a placeholder resolved · a founding-register or subnet change · a highway stop/route change · an airport added, moved or changed status · a city's coordinates corrected.

## State: v1 built (2026-10-03) — the five maps
See `README.md` for files and `CHANGES.md` for how they were built.

## State: towns-candidate maps 06 to 11 added (2026-10-04)
Six more maps (PNG + SVG in `out/`) show the 32 Priority Batch 1 candidate-town stations and the 36 automatic weather stations (possible comms posts). Data `data/town_candidates.csv`; code `scripts/tepenia_towns_common.py` + `render_06` to `render_11`. **Re-render a map whenever the batch changes** (a station added or dropped, a status verified): edit the CSV (regenerate it from `Locations/Towns/Data/Real_Station_Inventory_Crossmatched.csv` or hand-edit) and run the affected `render_NN` script. `render_all.py` also picks them up and archives `out/` first. Numbers 1 to 32 must stay in step with `Locations/Towns/Towns_Priority_Batch_1_Reference_2026-10-04.md`. Nothing on these maps names or characterizes a town.

## Names (all four renames applied 2026-10-03)
Santa Luce (was Abowasa) · Temirötkel (was Sayowa) · Utstein / Utsteinen (was Princess Elisabeth) · Relung Panen (was Bunger Hills City). Map data uses the new names and ids; see `Cities/City_Renames_Alias_Table_2026-10-03.md` for the full map of old → new.

## Developer rulings applied to the maps
- **2026-10-03: Hwy 7 passes near Halley with a connecting road; it does not go through the city (the ice is always moving).** Applied here and written into `Highways.md`, `City_Relationship_Database.md` and `Specs/Halley subnet/Halley.md` (Access type ON → SPUR). Also fixed (developer approved; none of these cities has been through the ULM): Local_Cultures/Halley_Subnet Abowasa, Troll, Neumayer and Halley's own file.

## Decisions I made that the developer has not confirmed (flag, don't treat as canon)
1. **Hwy 22 stop order.** `Highways.md` lists Hwy 22's route as *…Hwy 175 junction → dual-junction with Hwy 37 → junction with Hwy 59 → tri-junction*, but its own ramp text (59's ramp is *farther from the Pole than 175's*) and the developer's sketch put the **59 ramp BEFORE the Hwy 37 crossing**. The map follows the sketch. The text order is probably the slip.
2. **Amundsen Station's spec** says Hwy 175 and Hwy 59 *terminate at* the station; `Highways.md` says they end in **ramps on Hwy 22**. The map follows `Highways.md`.
3. **Relung Panen (was Bunger Hills City)** has no airport, port or highway stop of its own; only its spec's spur to Casey is drawn. Its coordinates (66°15′S 100°45′E) are the oasis center, which its spec notes as unreconciled.
4. **Fort McMurdo / Scott spur.** Both specs say *near Hwy 183, connected by a spur across McMurdo Sound, crossing type TBD*. Drawn dashed from the nearest point of Hwy 183, which is far from the Ross Island coast on the sketch; the attachment point is a placeholder.
5. **Highway shapes are schematic.** They follow the developer's hand-drawn sketch, which does not match real terrain or the real coast everywhere, and were not engineered against ice-sheet features. Treat them as network topology, not surveyed routes.
6. **Subnet zones** are drawn from city positions, not from any canon boundary. Canon only says which cities belong to which subnet and which are hubs.
7. **Machu Picchu Airport** uses the real station's coordinates (about 20 km from Contrapunto), not the developer's marker position (which sat on Pergamino's label).
8. **Mountain Pass** is placed at the midpoint of the Kunlun–Ariun Nuur stretch of Hwy 37; no distance is canon.

## Known cosmetic issues
- Hwy 1's last stretch before Byrd has a slight dogleg (a vertex kept from the sketch trace); (FIXED 2026-10-04: Hwy 4 now goes around the head of Prydz Bay on land; see CHANGES.md.)
- The Machu Picchu badge sits on top of Contrapunto's dot (about 20 km apart at this scale).
- Short spurs near Janbogo/Zukelli draw as tiny overlapping stubs at full-continent scale; close-ups would fix this.
- `data/ne_raw/` (28 MB of raw Natural Earth downloads) can be deleted; `render_all.py` re-fetches it only if `data/base/` is missing.

## Not built yet (optional, the developer has not asked)
- **Ports map** (`Ports.md` has a full per-city roster with tiers, the Tri-Cities port at Nella Fjord, Sanay's coastal port ~160 km from the city).
- **Post-war status map** (destroyed / damaged / survived; the column is already in `cities.csv` from `Station_to_City_Map.md`, but that table has known stale notes).
- **Regional close-ups** (Peninsula and South Shetlands, Larsemann Hills, Ross Island/Terra Nova Bay) so crowded clusters get real labels instead of leader lines.
- **Shaded relief / elevation base.** Natural Earth has no Antarctic elevation; a DEM would show the plateau and the Transantarctic Mountains behind the routes. The first attempt (NOAA ERDDAP/ETOPO) found no dataset; try Bedmap2 or REMA at low resolution.

## Provenance lessons from this build
- The developer's sketch placed several stations 150–420 km from their real GPS (Prydz Bay tri-junction, Byrd's end of Hwy 1/22, Casey, Jang Bogo/Zucchelli). Real GPS wins; the sketch supplies route *shape* only.
- Archive before overwriting: `render_all.py` does it automatically. Never re-run `build_geometry.py --rebuild` without checking `CHANGES.md` for hand edits.
