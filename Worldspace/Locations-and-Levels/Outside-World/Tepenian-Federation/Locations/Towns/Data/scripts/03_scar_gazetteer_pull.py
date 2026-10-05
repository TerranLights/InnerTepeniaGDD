#!/usr/bin/env python3
"""Pull facility-type records from the SCAR Composite Gazetteer of Antarctica (CGA) via its PostgREST API.
Entry URL data.aad.gov.au/aadc/gaz/scar/ 301-redirects to https://placenames.aq ; API root https://placenames.aq/api
Feature types pulled (codes from /api/feature_types): 312 Station, 140 Camp, 274 Refuge, 112 AWS, 135 Building,
205 Historic, 229 Landing area, 186 Food Depot, 191 Fuel depot, 193 Gear Depot, 101 Aerial.
Output: RAW/scar_gaz_facilities.json
"""
import os, json, requests
RAW = os.environ.get('RAW', './raw')
UA = {'User-Agent': 'Mozilla/5.0 (research script; contact kuros.kalacs@terranlights.com)'}
CODES = [312, 140, 274, 112, 135, 205, 229, 186, 191, 193, 101]
out = {}
for c in CODES:
    rows, off = [], 0
    while True:
        r = requests.get('https://placenames.aq/api/place_names_consolidated', headers=UA, timeout=120, params={
            'feature_type_code': f'eq.{c}', 'select': 'name_id,place_id,place_name_mapping,latitude,longitude,altitude,narrative,gazetteer_code,gazetteer_name,feature_type_code,feature_type_name,is_relic,date_named,comments',
            'limit': 1000, 'offset': off, 'order': 'name_id'})
        r.raise_for_status()
        b = r.json()
        rows += b
        if len(b) < 1000: break
        off += 1000
    out[c] = rows
    print(c, len(rows))
json.dump(out, open(os.path.join(RAW, 'scar_gaz_facilities.json'), 'w'), indent=1, ensure_ascii=False)
