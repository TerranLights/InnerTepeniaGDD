#!/usr/bin/env python3
"""Pull Antarctic station-type items from Wikidata SPARQL (https://query.wikidata.org/sparql).
Two passes: (A) items with P17 or P30 = Antarctica (Q51); (B) items inside the box lat -90..-60 (any longitude).
Both restricted to a set of facility-like classes (and subclasses of 'Antarctic research station').
Output: RAW/wikidata_stations.json (one record per item, multi-valued fields joined by ' ; ').
"""
import os, json, time, requests
RAW = os.environ.get('RAW', './raw')
UA = {'User-Agent': 'Mozilla/5.0 (research script; contact kuros.kalacs@terranlights.com)', 'Accept': 'application/sparql-results+json'}
TYPES = 'wd:Q749622 wd:Q4771007 wd:Q4930096 wd:Q62447 wd:Q989946 wd:Q486972 wd:Q1503257 wd:Q59217270 wd:Q195339 wd:Q41176 wd:Q96088884 wd:Q190107 wd:Q846837 wd:Q695850 wd:Q1248784 wd:Q94993988 wd:Q184590 wd:Q29826390 wd:Q3497366 wd:Q1349167 wd:Q1254933 wd:Q62832 wd:Q184356 wd:Q1081138 wd:Q38048707 wd:Q16970 wd:Q2031836 wd:Q366301 wd:Q4989906 wd:Q44782 wd:Q1313726'
def query(geo):
    return f'''
SELECT ?item ?itemLabel
 (GROUP_CONCAT(DISTINCT ?alt; separator=" ; ") AS ?alts)
 (SAMPLE(?coord) AS ?coord) (GROUP_CONCAT(DISTINCT ?typeL; separator=" ; ") AS ?types)
 (GROUP_CONCAT(DISTINCT STR(?inc); separator=" ; ") AS ?inception)
 (GROUP_CONCAT(DISTINCT STR(?dis); separator=" ; ") AS ?dissolved)
 (GROUP_CONCAT(DISTINCT ?opL; separator=" ; ") AS ?operators)
 (GROUP_CONCAT(DISTINCT ?ctL; separator=" ; ") AS ?countries)
 (GROUP_CONCAT(DISTINCT STR(?elev); separator=" ; ") AS ?elevation)
 (SAMPLE(?art) AS ?enwiki)
WHERE {{
  VALUES ?cls {{ {TYPES} }}
  {{ ?item wdt:P31 ?cls }} UNION {{ ?item wdt:P31/wdt:P279+ wd:Q749622 }}
  {geo}
  ?item wdt:P625 ?coord .
  ?item wdt:P31 ?ty . ?ty rdfs:label ?typeL FILTER(LANG(?typeL)="en")
  OPTIONAL {{ ?item skos:altLabel ?alt FILTER(LANG(?alt)="en") }}
  OPTIONAL {{ ?item wdt:P571 ?inc }}
  OPTIONAL {{ ?item wdt:P576 ?dis }}
  OPTIONAL {{ ?item wdt:P137 ?op . ?op rdfs:label ?opL FILTER(LANG(?opL)="en") }}
  OPTIONAL {{ ?item wdt:P17 ?ct . ?ct rdfs:label ?ctL FILTER(LANG(?ctL)="en") }}
  OPTIONAL {{ ?item wdt:P2044 ?elev }}
  OPTIONAL {{ ?art schema:about ?item ; schema:isPartOf <https://en.wikipedia.org/> }}
  SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}
}} GROUP BY ?item ?itemLabel'''
GEO_A = '{ ?item wdt:P17 wd:Q51 } UNION { ?item wdt:P30 wd:Q51 }'
GEO_B = '''SERVICE wikibase:box { ?item wdt:P625 ?loc . bd:serviceParam wikibase:cornerSouthWest "Point(-180 -90)"^^geo:wktLiteral . bd:serviceParam wikibase:cornerNorthEast "Point(180 -60)"^^geo:wktLiteral . }'''
res = {}
for name, geo in (('A_country_or_continent_Antarctica', GEO_A), ('B_box_south_of_60S', GEO_B)):
    for attempt in range(3):
        r = requests.post('https://query.wikidata.org/sparql', data={'query': query(geo)}, headers=UA, timeout=170)
        print(name, r.status_code, len(r.content))
        if r.status_code == 200: break
        time.sleep(10)
    if r.status_code != 200:
        print(r.text[:500]); continue
    rows = r.json()['results']['bindings']
    print(name, 'rows', len(rows))
    for b in rows:
        q = b['item']['value'].rsplit('/', 1)[-1]
        rec = {k: v['value'] for k, v in b.items()}
        rec['passes'] = res.get(q, {}).get('passes', []) + [name]
        res[q] = rec
json.dump(res, open(os.path.join(RAW, 'wikidata_stations.json'), 'w'), indent=1, ensure_ascii=False)
print('unique items', len(res))
