#!/usr/bin/env python3
"""Fetch Wikipedia intro extracts (plain text, first 3 sentences) for every article title seen so far
(titles from wp_parsed.json plus enwiki sitelinks from wikidata_stations.json). MediaWiki API, prop=extracts.
Output: RAW/wp_extracts.json {title: extract}"""
import os, json, time, requests
from urllib.parse import unquote
RAW = os.environ.get('RAW', './raw')
UA = {'User-Agent': 'Mozilla/5.0 (research script; contact kuros.kalacs@terranlights.com)'}
API = 'https://en.wikipedia.org/w/api.php'
wp = json.load(open(os.path.join(RAW, 'wp_parsed.json')))
wd = json.load(open(os.path.join(RAW, 'wikidata_stations.json')))
titles = set(wp['titles'].keys())
for q, r in wd.items():
    u = r.get('enwiki')
    if u: titles.add(unquote(u.rsplit('/wiki/', 1)[-1]).replace('_', ' '))
titles = sorted(t for t in titles if t)
ex = {}
for i in range(0, len(titles), 20):
    b = titles[i:i + 20]
    r = requests.get(API, headers=UA, params=dict(action='query', prop='extracts', exintro=1, explaintext=1, exsentences=3, exlimit=20, redirects=1, titles='|'.join(b), format='json'), timeout=60).json()
    q = r.get('query', {})
    redir = {x['from']: x['to'] for x in q.get('redirects', [])}
    norm = {x['from']: x['to'] for x in q.get('normalized', [])}
    got = {p['title']: p.get('extract', '') for p in q.get('pages', {}).values()}
    for a in b:
        t = norm.get(a, a); t = redir.get(t, t)
        if t in got: ex[a] = got[t]
    time.sleep(0.2)
json.dump(ex, open(os.path.join(RAW, 'wp_extracts.json'), 'w'), indent=1, ensure_ascii=False)
print('titles', len(titles), 'extracts', len(ex), 'non-empty', sum(1 for v in ex.values() if v))
