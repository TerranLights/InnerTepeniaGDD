"""Clip the Natural Earth layers to the Antarctic region and write small GeoJSON files into data/base/.
Input : data/ne_raw/*.shp  (run fetch_base_data.sh first, or set NE_DIR)
Output: data/base/{land,ice_shelves,ice_shelf_lines,coastline,regions,seas}.geojson
"""
import os
from pathlib import Path
import geopandas as gpd
from shapely.geometry import box

HERE = Path(__file__).resolve().parent.parent
NE = Path(os.environ.get('NE_DIR', HERE / 'data' / 'ne_raw'))
OUT = HERE / 'data' / 'base'; OUT.mkdir(parents=True, exist_ok=True)
CLIP = box(-180, -90, 180, -50)

def clip(name, out, cols=None):
    g = gpd.read_file(NE / f'{name}.shp')
    g = g.clip(CLIP)
    g = g[~g.geometry.is_empty]
    if cols: g = g[[c for c in cols if c in g.columns] + ['geometry']]
    g.to_file(OUT / f'{out}.geojson', driver='GeoJSON')
    print(out, len(g))

clip('ne_10m_land', 'land')
clip('ne_10m_antarctic_ice_shelves_polys', 'ice_shelves', ['name'])
clip('ne_10m_antarctic_ice_shelves_lines', 'ice_shelf_lines')
clip('ne_10m_coastline', 'coastline')
clip('ne_10m_geography_regions_polys', 'regions', ['NAME', 'FEATURECLA', 'SCALERANK'])
clip('ne_10m_geography_marine_polys', 'seas', ['name', 'featurecla', 'scalerank'])
