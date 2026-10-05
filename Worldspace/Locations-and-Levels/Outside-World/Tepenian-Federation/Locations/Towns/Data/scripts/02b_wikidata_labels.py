#!/usr/bin/env python3
"""For every Wikidata item pulled by 02, fetch English description plus labels/descriptions in other languages
(wbgetentities, https://www.wikidata.org/w/api.php) so unlabeled items can be named and every item has a description.
Output: RAW/wd_labels.json {qid: {label_en, desc_en, labels_other:{lang:label}, desc_other:{lang:desc}}}"""
import os, json, time, requests
RAW = os.environ.get('RAW', './raw')
UA = {'User-Agent': 'Mozilla/5.0 (research script; contact kuros.kalacs@terranlights.com)'}
wd = json.load(open(os.path.join(RAW, 'wikidata_stations.json')))
qids = sorted(wd.keys())
LANGS = 'en|es|fr|de|ru|no|it|pl|pt|sv|nl|ja|zh|uk|bg|cs|ko'
out = {}
for i in range(0, len(qids), 40):
    b = qids[i:i + 40]
    r = requests.get('https://www.wikidata.org/w/api.php', headers=UA, params=dict(action='wbgetentities', ids='|'.join(b), props='labels|descriptions|aliases', languages=LANGS, format='json'), timeout=60).json()
    for q, e in r.get('entities', {}).items():
        lab = {l: v['value'] for l, v in e.get('labels', {}).items()}
        des = {l: v['value'] for l, v in e.get('descriptions', {}).items()}
        al = {l: [x['value'] for x in v] for l, v in e.get('aliases', {}).items()}
        out[q] = dict(label_en=lab.get('en', ''), desc_en=des.get('en', ''), labels_other={k: v for k, v in lab.items() if k != 'en'}, desc_other={k: v for k, v in des.items() if k != 'en'}, aliases=al)
    time.sleep(0.2)
json.dump(out, open(os.path.join(RAW, 'wd_labels.json'), 'w'), indent=1, ensure_ascii=False)
print(len(out), 'entities; with en desc', sum(1 for v in out.values() if v['desc_en']))
