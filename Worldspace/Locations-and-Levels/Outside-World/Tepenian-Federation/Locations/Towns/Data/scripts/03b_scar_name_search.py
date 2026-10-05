#!/usr/bin/env python3
"""Second SCAR gazetteer pass: name search (ilike) for facility words across ALL feature types, because the 'Refuge' (274) feature type is empty
and many huts/historic bases are filed under no feature type. Output: RAW/scar_name_search.json {name_id: record}"""
import os, json, requests
RAW = os.environ.get('RAW', './raw')
UA = {'User-Agent': 'Mozilla/5.0 (research script; contact kuros.kalacs@terranlights.com)'}
pats = ['Hut', 'Refug', 'Camp', 'Station', 'Skiway', 'Airfield', 'Runway', 'Laborator', 'Observator', 'Estaci', 'Base', 'Hütte', 'Cabin', 'Lodge', 'Depot', 'Aerodrome', 'Airstrip']
res = {}
for p in pats:
    off = 0
    while True:
        r = requests.get('https://placenames.aq/api/place_names_consolidated', headers=UA, timeout=120, params={'place_name_mapping': f'ilike.*{p}*',
            'select': 'name_id,place_id,place_name_mapping,latitude,longitude,altitude,narrative,gazetteer_code,feature_type_code,feature_type_name,is_relic,date_named', 'limit': 1000, 'offset': off, 'order': 'name_id'})
        b = r.json()
        for x in b: res[x['name_id']] = x
        if len(b) < 1000: break
        off += 1000
    print(p, len(res))
json.dump(res, open(os.path.join(RAW, 'scar_name_search.json'), 'w'), ensure_ascii=False)
