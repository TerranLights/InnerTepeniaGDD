# Tepenia map series (working stash)

Maps of Tepenia drawn on **real Antarctica** (Natural Earth 10m, south polar stereographic, true scale at 71°S, 0° at the top, 90°E to the right — the orientation of the developer's earlier sketches). Every city sits at the real GPS coordinates of its station site. Everything is generated from the CSV files in `data/`, so the maps can be re-rendered whenever the nation or city data changes.

**Read `PROGRESS TRACKER - Read This First.md` before touching anything.**

## The five maps (`out/`, PNG + SVG)

| File | Shows |
|---|---|
| `01_Tepenia_Cities` | the 38 cities, colored by Arcanet subnet; hubs are stars |
| `02_Tepenia_Cities_and_Highways` | cities + the highway network |
| `03_Tepenia_Cities_and_Airports` | cities + airports (hosted and served-not-host) |
| `04_Tepenia_Cities_Highways_and_Airports` | cities + highways + airports |
| `05_Tepenia_Arcanet_Subnets` | the six regional subnets (schematic zones) and the Pole relay |

## The towns-candidate maps (`out/`, PNG + SVG; added 2026-10-04)

Real stations only, from the Towns inventory (`Locations/Towns/Data/`). Numbers match `Locations/Towns/Towns_Priority_Batch_1_Reference_2026-10-04.md`. Data: `data/town_candidates.csv` (kind `station` = the 32 Priority Batch 1 stations; kind `aws` = the 36 automatic weather stations outside the cities, W1 to W36, alphabetical). Code: `scripts/tepenia_towns_common.py` + `render_06` to `render_11` (run one script at a time; they do not archive).

| File | Shows |
|---|---|
| `06_Towns_Candidate_Stations` | the 32 candidate stations, full continent, with a numbered index |
| `07_Towns_Candidate_Stations_Peninsula` | Peninsula and South Shetlands close-up (19 of the 32) |
| `08_Towns_Candidate_Stations_South_Shetlands` | South Shetlands and Hope Bay close-up (12 stations, densest cluster) |
| `09_Towns_Comms_Post_Candidates` | the 36 automatic weather stations (possible comms posts), full continent, numbered index |
| `10_Towns_All_Candidate_Sites` | all 68 sites together, no numbers |
| `11_Towns_Comms_Post_Candidates_Casey` | Casey / Law Dome close-up of the weather-station cluster |
| `13_Comms_Meta_Nodes` | the 38 cities plus the HF comms meta-nodes: proposed (the developer's four: Peninsula region, Utstein, Mawson, Casey) and possible (Halley, Belgrano, Neumayer, Santa Luce, Mirny, Davis/Larsemann, Signy, Rothera, Byrd, Macquarie Island), with great-circle hop lengths and Hobart plus three cities as link endpoints (view widened north to reach them); data `data/meta_nodes.csv`, `data/meta_links.csv`; code `scripts/render_13_meta_nodes.py` |
| `12_Towns_Sites_of_Interest` | the developer's three sites of interest (#24 Russkaya, #16 Leningradskaya, #18/#19 Molodezhnaya + Mountain Evening) with straight-line distances to the nearest city and highway |

## How to update the maps

1. Edit the relevant CSV in `data/` (see table).
2. `cd scripts && /tmp/mapvenv/bin/python3 render_all.py` (any Python with geopandas, shapely, pyproj and matplotlib works; `/tmp/mapvenv` is the one the Russia maps used and is rebuilt if `/tmp` is cleared).
3. `render_all.py` **moves the previous `out/` into `archive/<timestamp>/` first** — nothing is overwritten in place.
4. Look at the result (label collisions are the usual casualty), then log the change in `CHANGES.md`.

| Data file | What it holds | Edit when |
|---|---|---|
| `cities.csv` | id, name, subnet, lat, lon, hub flag, name flag (`placeholder` / `rename-pending`), spec file, post-war status | a city is renamed, moved between subnets, gets a new hub, or a placeholder is resolved |
| `labels_full.csv` | per-city label offset (points), alignment, optional text override | a label collides or a name changes |
| `highways.csv` | which cities each highway serves, spurs, ramps, colors | a highway's stops or endpoints change |
| `highway_geometry.csv` | every highway/spur as lat/lon vertices (the line shapes) | a route shape needs hand-refining |
| `highways_traced.csv` | raw trace of the developer's hand-drawn sketch (provenance only) | never (regenerate with `extract_highways_from_sketch.py`) |
| `junctions.csv` | The Temirötkel Junction | its position changes |
| `airports.csv` | airports, kind, status, which cities each serves | an airport is added, moved, or its status changes |
| `labels_airports.csv`, `highway_badges.csv`, `subnet_titles.csv` | label placement for those layers | collisions |
| `base/*.geojson` | Natural Earth Antarctica layers (clipped) | never; `fetch_base_data.sh` + `prepare_base_data.py` rebuild them |
| `ne_raw/` | the raw Natural Earth download (28 MB), only needed to rebuild `base/` | safe to delete; the fetch script re-downloads it |

⚠ `build_geometry.py` regenerates `highway_geometry.csv` from `highways.csv` + the trace and **refuses to overwrite** without `--rebuild`, because hand edits to the line shapes would be lost. Edit the CSV directly for small shape fixes; use `--rebuild` only when stops/spurs change, and re-apply any hand edits recorded in `CHANGES.md`.

## Conventions kept from the other Map Files packages

`OUT_DIR` env var for the output folder · Crimson Text (titles, sea names) + Lato (labels), copied into `fonts/` · SVGs keep live text (`svg.fonttype none`) · `README.md` / `CHANGES.md` / `PROGRESS TRACKER` triple · archive before overwriting.

## Data sources

Base geography: Natural Earth (public domain). City coordinates: each city's `Specs/*.md` (`**Based on:**` line). Highways: `Locations/Infrastructure/Highways.md` (stops) and the developer's hand-drawn `Reference/Images/Maps/Antarctica_highway_map_by_topology.jpeg` (route shapes). Airports: `Locations/Infrastructure/Airports.md`. Subnets: `Cities/Station_to_City_Map.md` and the developer's `Tepenian Arcanet subnet map by region.jpeg`.
