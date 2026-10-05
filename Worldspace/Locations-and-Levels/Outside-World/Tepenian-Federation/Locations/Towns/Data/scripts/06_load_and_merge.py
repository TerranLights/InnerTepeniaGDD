#!/usr/bin/env python3
"""Load all sources as observations, de-duplicate them into entities, write RAW/entities.json + RAW/merge_review.txt.
Source priority (earlier sources create the entity; later ones match or create):
 comnap24 > comnap17 > wikidata > wp_list > wp_camps > wp_airports > wp_hsm > scar
Matching rule: observation matches an existing entity when (a) same Wikidata QID, or (b) name_score >= 0.5 AND distance <= MAXD km,
or (c) manual override in OVERRIDES. See Method_and_Log.md for the full rules."""
import os, re, json, csv, sys
from urllib.parse import unquote
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inv_lib import *

OUTSIDE_NAMES = ()
MAXD = 4.0   # km, name-match radius
obs = []

def add(**k):
    k.setdefault('alts', []); k.setdefault('elev', None); k.setdefault('lat', None); k.setdefault('lon', None)
    k.setdefault('extra', {}); obs.append(k); return k

# ---------------- COMNAP 2024 CSV
def clean_cn(n):
    n = n.strip()
    n = re.sub(r'\s+Antartic Base$', '', n)
    n = re.sub(r'\s+Antarctic Base$', '', n)
    return n.strip()
rows = list(csv.DictReader(open(os.path.join(RAW, 'comnap_facilities.csv'), encoding='latin-1', newline='')))
for r in rows:
    en = r['English Name'].strip(); off = r['Official Name'].strip()
    kindmap = {'Station': 'station', 'Camp': 'camp', 'Refuge': 'refuge', 'Airfield Camp': 'airfield', 'Laboratory': 'lab', 'Depot': 'depot'}
    def f(x):
        try: return float(x)
        except: return None
    def ff(x):
        try: return float(str(x).replace(',', ''))
        except: return None
    add(src='comnap24', sid=r['Record ID#'], name=clean_cn(en), alts=[x for x in {en, off} if x and x != clean_cn(en)], lat=f(r['Latitude (DD)']), lon=f(r['Longitude (DD)']),
        elev=ff(r['Elevation (meters)']), kind=kindmap.get(r['Type'], 'other'), type_label=r['Type'], seasonality=r['Seasonality'], status_label=r['Status'],
        year_open=r['Year Established'].strip(), operator=r['Operator (primary)'] + (' ; ' + r['Operator (additional)'] if r['Operator (additional)'].strip() else ''),
        peak_pop=r['Peak Population'].strip(), region=r['Antarctic Region'].strip(), ddm=(r['Latitude (DDM)'] + ' ' + r['Longitude (DDM)']).strip(), elev_datum=r['Elevation Datum'],
        power=r['Power Supply Types'])

# ---------------- COMNAP 2017 catalog
N17 = ['Belgrano II', 'Brown', 'Camara', 'Carlini', 'Decepcion', 'Esperanza', 'Marambio', 'Matienzo', 'Melchior', 'Orcadas', 'Petrel', 'Primavera', 'San Martin', 'Casey', 'Davis', 'Mawson',
       'Princess Elisabeth', 'Ferraz', 'St. Kliment Ohridski', 'Carvajal', 'Dr. Guillermo Mann', 'Frei', 'Gabriel Gonzalez Videla', "O'Higgins", 'Prat', 'Professor Julio Escudero', 'Risopatron', 'Yelcho',
       'Great Wall', 'Kunlun', 'Taishan', 'Zhongshan', 'Johann Gregor Mendel', 'Pedro Vicente Maldonado', 'Aboa', 'Concordia', "Dumont d'Urville", 'Dallmann Laboratory', 'Kohnen', 'Neumayer III', 'Bharati', 'Maitri',
       'Mario Zucchelli', 'Syowa', 'Dirck Gerritsz Laboratory', 'Scott Base', 'Troll', 'Machu Picchu', 'Henryk Arctowski', 'Mountain Evening (Vechernyaya)', 'Jang Bogo', 'King Sejong', 'Bellingshausen',
       'Druzhnaya IV', 'Leningradskaya', 'Mirny', 'Molodezhnaya', 'Novolazarevskaya', 'Oazis', 'Progress', 'Russkaya', 'Vostok', 'SANAE IV', 'Gabriel de Castilla', 'International Field Camp Peninsula Byers',
       'Juan Carlos I', 'Wasa', 'Vernadsky', 'Halley VI', 'Rothera', 'Signy', 'Amundsen-Scott South Pole', 'McMurdo', 'Palmer', 'Artigas', 'Ruperto Elichiribehety']
c17 = json.load(open(os.path.join(RAW, 'comnap_catalogue_parsed.json')))
assert len(c17) == len(N17) == 76
for n, r in zip(N17, c17):
    lat, lon, fl = parse_dms_pair(r.get('coord_dms', ''))
    def ff(x):
        try: return float(str(x).replace(',', ''))
        except: return None
    add(src='comnap17', sid=str(r['pdf_index'] - 8), name=n, lat=lat, lon=lon, elev=ff(r['altitude_m']), kind='station' if r['type'].lower().startswith('station') else ('lab' if r['type'].lower().startswith('lab') else ('camp' if 'camp' in r['type'].lower() else 'other')),
        type_label=r['type'], operational_period=r['operational_period'], dms=r.get('coord_dms', ''), dms_flags=fl, surface_type=r['surface_type'], location_text=r['location_text'], history_text=r['history_text'],
        features=r['features'], disciplines=r['disciplines'], beds=r['beds'], staff_summer=r['staff_summer'], staff_winter=r['staff_winter'], max_personnel=r['max_personnel'],
        permafrost=r['permafrost'], operator=r.get('name_operator_line', ''))

# ---------------- Wikidata
wd = json.load(open(os.path.join(RAW, 'wikidata_stations.json')))
wl = json.load(open(os.path.join(RAW, 'wd_labels.json')))
WD_STATION = {'Antarctic research station', 'research station', 'polar station', 'year-round Antarctic facility'}
def wd_kind(types):
    T = set(types)
    if T & WD_STATION: return 'station'
    if 'Antarctic field camp' in T: return 'camp'
    if 'whaling station' in T: return 'station'
    if T & {'shelter'}: return 'refuge'
    if T & {'aerodrome', 'blue ice runway', 'airstrip', 'airbase', 'airport', 'runway', 'commercial traffic aerodrome'}: return 'airfield'
    if T & {'weather station', 'automatic weather station'}: return 'aws'
    if T & {'ground station'}: return 'other'
    return 'excluded'
WD_EXCL_REASON = {'magnetic observatory': 'magnetic observatory (sub-facility of a station; merged as a note if it matches a station)', 'research expedition': 'expedition, not a location', 'church building': 'chapel/church (building at a station)',
                  'iceport': 'ship landing (iceport), no buildings', 'radio telescope': 'instrument at South Pole', 'neutrino detector': 'instrument at South Pole', 'astronomical observatory': 'instrument/observatory at a station'}
for q, r in wd.items():
    types = [t for t in r.get('types', '').split(' ; ') if t]
    m = re.match(r'Point\((-?[\d.]+) (-?[\d.]+)\)', r.get('coord', ''))
    lat = float(m.group(2)) if m else None; lon = float(m.group(1)) if m else None
    lab = wl.get(q, {})
    name = r.get('itemLabel', q)
    if name == q:
        name = lab.get('label_en') or next(iter(lab.get('labels_other', {}).values()), q)
    alts = [x for x in r.get('alts', '').split(' ; ') if x]
    for v in lab.get('labels_other', {}).values():
        if v != name and v not in alts: alts.append(v)
    elev = None
    for e in r.get('elevation', '').split(' ; '):
        try: elev = float(e); break
        except: pass
    def y(s): return yr(s.split(' ; ')[0]) if s else ''
    k = wd_kind(types)
    if k == 'aws':
        if re.search(r'Airstrip|Runway|Skiway|Airfield|Aerodrome', name, re.I): k = 'airfield'
        elif re.search(r'Refuge|Depot and|Hut\b', name, re.I): k = 'refuge'
    title = unquote(r['enwiki'].rsplit('/wiki/', 1)[-1]).replace('_', ' ') if r.get('enwiki') else ''
    add(src='wikidata', sid=q, name=name, alts=alts, lat=lat, lon=lon, elev=elev, kind=k, types=types, year_open=y(r.get('inception', '')), year_close=y(r.get('dissolved', '')), operator=' ; '.join(x for x in (r.get('operators', ''), ' ; '.join(c for c in r.get('countries', '').split(' ; ') if c and c != 'Antarctica')) if x),
        qid=q, wp_title=title, desc=lab.get('desc_en', ''), passes=r.get('passes'))

# ---------------- Wikipedia
wp = json.load(open(os.path.join(RAW, 'wp_parsed.json')))
T = wp['titles']
for s in wp['stations']:
    t = T.get(s['link'] or '', {})
    lat, lon = t.get('lat'), t.get('lon')
    add(src='wp_list', sid=s['list_section'] + ':' + s['name'], name=s['name'], lat=lat, lon=lon, qid=t.get('qid'), wp_title=s['link'] or '', list_section=s['list_section'], location_text=s['location'], country=s['country'], admin=s['admin'],
        year_open=s.get('year_est', ''), year_close=s.get('year_closed', ''), op_type=s.get('op_type', ''), status_text=s.get('status_text', ''), max_pers=s.get('max_pers', ''), summer_pop=s.get('summer_pop', ''), winter_pop=s.get('winter_pop', ''),
        kind='station')
for c in wp['camps']:
    t = T.get(c['link'] or '', {})
    ts = c['type_status'].lower()
    k = 'refuge' if ('refuge' in ts or 'hut' in ts or 'shelter' in ts) else ('camp' if 'camp' in ts else ('depot' if 'depot' in ts else 'camp'))
    if 'base' in ts: k = 'station'
    if re.search(r'Skiway|Runway|Airbase|Airfield|Airstrip', c['name'], re.I): k = 'airfield'
    lat, lon = c['lat'], c['lon']
    if lat is None and 'lat' in t: lat, lon = t['lat'], t['lon']
    add(src='wp_camps', sid=c['name'] + '|' + c['location'] + '|' + c['country'], name=c['name'], lat=lat, lon=lon, qid=t.get('qid'), wp_title=c['link'] or '', location_text=c['location'], country=c['country'], year_open=c['year_est'], type_status=c['type_status'],
        serving_base=c['serving_base'], activities=c['activities'], kind=k)
for a in wp['airports']:
    t = T.get(a['link'] or '', {})
    lat, lon = a['lat'], a['lon']
    nm = re.sub(r'\s*/\s*\(serving.*$', '', a['name']).strip()
    nm = re.sub(r'\{\{Interlanguage link\|([^|]*)\|.*?\}\}', r'\1', nm)
    add(src='wp_airports', sid=a['name'], name=nm, lat=lat, lon=lon, qid=t.get('qid'), wp_title=a['link'] or '', location_text=a['location'], country=a['country'], icao=a['icao'], runway=a['runway'], kind='airfield')
HSM_KEEP = {15, 22, 63, 14, 16, 18, 21, 26, 30, 33, 38, 39, 41, 42, 46, 47, 55, 56, 61, 62, 64, 67, 68, 71, 75, 76, 77, 79, 83, 84, 87, 10, 91, 4}
for h in wp['hsm']:
    try: n = int(h['number'])
    except: continue
    if n in HSM_KEEP:
        t = T.get(h['link'] or '', {})
        add(src='wp_hsm', sid='HSM %d' % n, name=h['name'], lat=h['lat'], lon=h['lon'], qid=t.get('qid'), wp_title=h['link'] or '', kind='hist', description=h['description'], proponent=h['proponent'], adopted=h['adopted'], hsm=n)

# ---------------- SCAR CGA
sc = json.load(open(os.path.join(RAW, 'scar_gaz_facilities.json')))
sn = json.load(open(os.path.join(RAW, 'scar_name_search.json')))
EXCL_SC = re.compile(r'Nunatak|Tarn|Glacier|L[oó]bulo|^Basen$|Castle|Castillo|Pico|Roca|Catedral|Bergan|Crags|Peak|Crest|Española|Skiway Col', re.I)
seen = set()
def scar_clean(n): return re.sub(r'\s*/[^/]*/\s*', ' ', n).replace(', Base', '').replace(', Station', '').replace(', Refugio', '').strip(' ,')
for code, lst in sc.items():
    for r in lst:
        nm = r['place_name_mapping']
        if EXCL_SC.search(nm): continue
        kind = {'312': 'station', '140': 'camp', '112': 'aws', '135': 'refuge', '205': 'hist', '229': 'airfield', '186': 'depot', '193': 'depot'}.get(code)
        if not kind: continue
        if code == '135' and 'tte' not in nm: continue  # only the hut among 'Building' type
        seen.add(r['name_id'])
        add(src='scar', sid=str(r['name_id']), name=scar_clean(nm), alts=[nm] if scar_clean(nm) != nm else [], lat=r['latitude'], lon=r['longitude'], elev=(float(r['altitude']) if r['altitude'] not in (None, '') else None), kind=kind,
            gaz=r['gazetteer_code'], feature_type=r['feature_type_name'], narrative=(r['narrative'] or ''), relic=r['is_relic'])
SC_EXTRA = re.compile(r'\(Base [A-Z]\)|Dobrowolski Station|^Byrd Station|^S-2|Skiway|Belgrano Station|Wilkins Aerodrome|Elichiribehety|Refuge /|Refugio|Skelton Depot|Southern Depot', re.I)
for k, r in sn.items():
    if r['name_id'] in seen: continue
    nm = r['place_name_mapping']
    if not SC_EXTRA.search(nm) or EXCL_SC.search(nm): continue
    if r['feature_type_name'] not in (None, 'Anchorage', 'Landing area', 'Station'): continue
    kind = 'refuge' if re.search(r'Refug', nm) else ('airfield' if re.search(r'Skiway|Aerodrome', nm) else ('depot' if 'Depot' in nm else 'station'))
    add(src='scar', sid=str(r['name_id']), name=scar_clean(nm), alts=[nm], lat=r['latitude'], lon=r['longitude'], elev=(float(r['altitude']) if r['altitude'] not in (None, '') else None), kind=kind,
        gaz=r['gazetteer_code'], feature_type=r['feature_type_name'] or 'unspecified', narrative=(r['narrative'] or ''), relic=r['is_relic'])

# ---------------- matching
ORDER = ['comnap24', 'comnap17', 'wikidata', 'wp_list', 'wp_camps', 'wp_airports', 'wp_hsm', 'scar']
here = os.path.dirname(os.path.abspath(__file__))
OVR = json.load(open(os.path.join(here, 'merge_overrides.json')))
OVR = {k: v for k, v in OVR.items() if not k.startswith('_')}
OBS = {o['src'] + ':' + o['sid']: o for o in obs}
def resolve(spec):
    if spec in OBS: return spec
    if ':~' in spec:
        src, pat = spec.split(':~', 1)
        c = [k for k, o in OBS.items() if o['src'] == src and pat.lower() in o['name'].lower()]
        if len(c) == 1: return c[0]
        raise SystemExit('override spec %r matches %d: %s' % (spec, len(c), c[:6]))
    raise SystemExit('unknown override spec %r' % spec)
OVR = {resolve(k): v for k, v in OVR.items()}
ents = []; byobs = {}; log = []; pending = []
def obs_names(p):
    ns = [p['name']]
    if p['src'] == 'comnap24': ns += p['alts'][:2]
    if p['src'] == 'scar': ns += p['alts'][:1]
    return ns
def best_entity(o, kind=None):
    kind = kind or o['kind']
    best = None
    for e in ents:
        main = [p for p in e['obs'] if not p.get('sub')]
        if not main: continue
        ds = [haversine((o['lat'], o['lon']), (p['lat'], p['lon'])) for p in main if p['lat'] is not None and o['lat'] is not None]
        d = min(ds) if ds else None
        sc_ = max(name_score(o['name'], n) for p in main for n in obs_names(p))
        same_name_close = sc_ >= 0.99 and d is not None and d < 1.0
        ek = e['kind']
        cn_airfield = any(p.get('src') == 'comnap24' and p.get('kind') == 'airfield' for p in main)
        if kind == 'aws' or ek == 'aws':
            if not (kind == ek or same_name_close): continue
        elif (kind == 'airfield') != (ek == 'airfield'):
            other = kind if ek == 'airfield' else ek
            if not (same_name_close and cn_airfield and other in ('camp', 'depot', 'refuge')): continue
        ok = False
        srcs = {p['src'] for p in main}
        qid_hit = o.get('qid') and any(p.get('qid') == o['qid'] for p in main)
        if qid_hit and (o['src'] == 'wp_list' or sc_ > 0): ok = True
        elif d is not None and sc_ >= 0.5 and d <= MAXD: ok = True
        elif d is not None and sc_ >= 0.99 and d <= 5: ok = True
        elif d is not None and sc_ >= 0.99 and d <= 60 and ((o['src'] == 'comnap17' and 'comnap24' in srcs) or (o['src'] == 'comnap24' and 'comnap17' in srcs)) and kind == ek: ok = True
        elif d is None and sc_ >= 0.9 and kind == ek: ok = True
        if ok:
            key = (sc_, -(d if d is not None else 99))
            if best is None or key > best[0]: best = (key, e, d, sc_)
    return best
def attach(o, target, note):
    key = o['src'] + ':' + o['sid']
    target['obs'].append(o); byobs[key] = target
    log.append(('MATCH', key, o['name'], note))
def place(o, defer_ok=True):
    key = o['src'] + ':' + o['sid']
    ov = OVR.get(key)
    sub = False
    if ov and ov.startswith('SUB:'): ov = ov[4:]; sub = True
    if ov == 'DROP':
        o['dropped'] = 'manual drop'; log.append(('DROP', key, o['name'], 'manual')); return True
    if ov and ov != 'NEW':
        tkey = resolve(ov) if ov not in OBS else ov
        if tkey not in byobs:
            if defer_ok: return False
            raise SystemExit('override target never placed: %s -> %s' % (key, ov))
        if sub: o['sub'] = True
        attach(o, byobs[tkey], '-> %s (manual override)' % byobs[tkey]['obs'][0]['name']); return True
    if o['kind'] == 'excluded':
        o['held'] = True; return True
    best = None if ov == 'NEW' else best_entity(o)
    if best:
        if o['src'] == 'wikidata' and o['kind'] == 'aws' and best[1]['kind'] != 'aws': o['sub'] = True
        attach(o, best[1], '-> %s (score %.2f, dist %s km)' % (best[1]['obs'][0]['name'], best[3], ('%.2f' % best[2]) if best[2] is not None else 'n/a'))
    else:
        e = dict(kind=o['kind'], obs=[o]); ents.append(e); byobs[key] = e
        log.append(('NEW', key, o['name'], o['kind']))
    return True
for src in ORDER:
    for o in [x for x in obs if x['src'] == src]:
        if not place(o): pending.append(o)
    # retry pending after every source (targets may now exist)
    again = True
    while again and pending:
        again = False
        for o in list(pending):
            if place(o): pending.remove(o); again = True
for o in pending: place(o, defer_ok=False)
# held (excluded-class Wikidata items): match by name, else attach to nearest facility within 3 km as a note-only item, else drop
for o in obs:
    if not o.get('held'): continue
    key = o['src'] + ':' + o['sid']
    best = best_entity(o, kind='station')
    o['sub'] = True
    if best:
        attach(o, best[1], '-> %s (excluded-class item, name/qid match; note only)' % best[1]['obs'][0]['name']); continue
    near = None
    for e in ents:
        if e['kind'] in ('airfield', 'aws'): continue
        main = [p for p in e['obs'] if not p.get('sub') and p['lat'] is not None]
        if not main or o['lat'] is None: continue
        d = min(haversine((o['lat'], o['lon']), (p['lat'], p['lon'])) for p in main)
        if d <= 3 and (near is None or d < near[0]): near = (d, e)
    if near and not re.search(r'Expedition|iceport|Iceport|Anchorage|Rock$|Beaches|Inlet', o['name']):
        attach(o, near[1], '-> %s (excluded-class item attached by proximity %.2f km; note only)' % (near[1]['obs'][0]['name'], near[0]))
    else:
        o['dropped'] = 'wikidata item of excluded class (' + '; '.join(o['types']) + ')'; log.append(('DROP', key, o['name'], o['dropped']))
for i, e in enumerate(ents): e['idx'] = i
json.dump(dict(obs=obs, ents=[[ (p['src'] + ':' + p['sid']) for p in e['obs']] for e in ents], log=log), open(os.path.join(RAW, 'merge_state.json'), 'w'), ensure_ascii=False, indent=0, default=str)
import collections
print('observations', len(obs), collections.Counter(o['src'] for o in obs))
print('entities', len(ents), collections.Counter(e['kind'] for e in ents))
print(collections.Counter(l[0] for l in log))
