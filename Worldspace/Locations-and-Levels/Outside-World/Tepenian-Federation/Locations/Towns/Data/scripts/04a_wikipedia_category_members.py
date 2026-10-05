#!/usr/bin/env python3
"""Recursive category walk on English Wikipedia (MediaWiki API list=categorymembers) for coverage cross-checking.
Roots: Outposts of Antarctica, Historic buildings and structures in Antarctica, Airports in Antarctica, Antarctic field camps.
Output: RAW/wp_category_members.json {article title: [category, ...]}"""
import os, json, requests
RAW = os.environ.get('RAW', './raw')
UA = {'User-Agent': 'Mozilla/5.0 (research script; contact kuros.kalacs@terranlights.com)'}
API = 'https://en.wikipedia.org/w/api.php'
def cat(title, seen, out):
    if title in seen: return
    seen.add(title); cont = {}
    while True:
        r = requests.get(API, headers=UA, params=dict(action='query', list='categorymembers', cmtitle=title, cmlimit=500, format='json', **cont)).json()
        for m in r['query']['categorymembers']:
            if m['ns'] == 14: cat(m['title'], seen, out)
            elif m['ns'] == 0: out.setdefault(m['title'], []).append(title)
        if 'continue' in r: cont = r['continue']
        else: break
out, seen = {}, set()
for c in ['Category:Outposts of Antarctica', 'Category:Historic buildings and structures in Antarctica', 'Category:Airports in Antarctica', 'Category:Antarctic field camps']:
    cat(c, seen, out)
json.dump(out, open(os.path.join(RAW, 'wp_category_members.json'), 'w'), ensure_ascii=False)
print(len(seen), 'categories;', len(out), 'articles')
