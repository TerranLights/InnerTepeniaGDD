#!/usr/bin/env python3
"""Fetch and parse Wikipedia pages via the MediaWiki API (https://en.wikipedia.org/w/api.php).
Pages: Research stations in Antarctica (a.k.a. List of Antarctic research stations), Antarctic field camps,
List of airports in Antarctica, Historic Sites and Monuments in Antarctica; plus category-tree members
(Outposts of Antarctica, Historic buildings and structures in Antarctica, Airports in Antarctica, Antarctic field camps).
For every linked article title, GeoData coordinates (prop=coordinates) and the Wikidata item (pageprops) are fetched.
Output: RAW/wp_parsed.json  {stations:[...], camps:[...], airports:[...], hsm:[...], titles:{title:{lat,lon,qid}}}
"""
import os, re, json, time, requests
RAW = os.environ.get('RAW', './raw')
UA = {'User-Agent': 'Mozilla/5.0 (research script; contact kuros.kalacs@terranlights.com)'}
API = 'https://en.wikipedia.org/w/api.php'

def get_wikitext(title):
    r = requests.get(API, headers=UA, params=dict(action='parse', prop='wikitext', redirects=1, page=title, format='json'), timeout=60).json()
    return r['parse']['wikitext']['*'], r['parse']['title']

CC = {'JAP': 'Japan', 'GDR': 'East Germany', 'SUN': 'Soviet Union', 'ARG': 'Argentina', 'AUS': 'Australia', 'BUL': 'Bulgaria', 'CHL': 'Chile', 'CHN': 'China', 'USA': 'United States', 'ITA': 'Italy',
      'UK': 'United Kingdom', 'GBR': 'United Kingdom', 'RUS': 'Russia', 'URU': 'Uruguay', 'FRA': 'France', 'GER': 'Germany', 'DEU': 'Germany',
      'NZL': 'New Zealand', 'JPN': 'Japan', 'IND': 'India', 'NOR': 'Norway', 'SWE': 'Sweden', 'FIN': 'Finland', 'BRA': 'Brazil', 'ESP': 'Spain',
      'POL': 'Poland', 'CZE': 'Czech Republic', 'ECU': 'Ecuador', 'PER': 'Peru', 'KOR': 'South Korea', 'ZAF': 'South Africa', 'RSA': 'South Africa',
      'BEL': 'Belgium', 'NLD': 'Netherlands', 'UKR': 'Ukraine', 'BLR': 'Belarus', 'ROU': 'Romania', 'PAK': 'Pakistan', 'URY': 'Uruguay', 'TUR': 'Turkey'}

def strip_refs(s):
    s = re.sub(r'<ref[^>/]*/>', '', s)
    s = re.sub(r'<ref[^>]*>.*?</ref>', '', s, flags=re.S)
    s = re.sub(r'<!--.*?-->', '', s, flags=re.S)
    return s

def _ill(m):
    args = m.group(1).split('|')
    for a in args:
        if a.startswith('lt='): return a[3:]
    return args[0]

def clean(s):
    s = strip_refs(s)
    s = re.sub(r'\{\{ill\|([^{}]*)\}\}', _ill, s)
    s = re.sub(r'\{\{(?:[Ff]lagu?|[Ff]lagcountry|[Nn]oflag)\|([^}|]*)[^}]*\}\}', r'\1', s)
    s = re.sub(r'\{\{([A-Z]{2,3})\}\}', lambda m: CC.get(m.group(1), m.group(1)), s)
    s = re.sub(r'\{\{(?:efn|Efn|hs|abbr|anchor|Anchor)[^}]*\}\}', '', s)
    s = re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]', r'\1', s)
    s = re.sub(r'<br\s*/?>', ' / ', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = re.sub(r"'''?", '', s)
    return ' '.join(s.split())

def first_link(s):
    m = re.search(r'\[\[([^\]|#]*)', strip_refs(s))
    return m.group(1).strip() if m else None

def parse_tables(text):
    """returns list of tables; each = list of rows; each row = list of raw cell strings"""
    tables = []
    for tm in re.finditer(r'\{\|(.*?)\n\|\}', text, re.S):
        body = tm.group(1)
        rows = re.split(r'\n\|-[^\n]*', body)
        tab = []
        for row in rows:
            cells = []
            hdr = False
            cur = None
            for line in row.split('\n'):
                if line.startswith('!'):
                    hdr = True
                    continue
                if line.startswith('|') and not line.startswith('|-'):
                    parts = re.split(r'\|\|', line[2:] if line.startswith('||') else line[1:])
                    # a leading '|' that is a double '||' at line start
                    for p in parts:
                        cells.append(p)
                    cur = len(cells) - 1
                elif cur is not None and line.strip():
                    cells[cur] += '\n' + line
            if cells and not hdr:
                tab.append(cells)
        tables.append(tab)
    return tables

def parse_coord(txt):
    """first {{coord|...}} template in txt -> (lat, lon). Handles decimal {{coord|63.4|S|56.2|W}}, DMS {{coord|71|31||S|08|48||E}},
    {{coord|77|33|S|166|10|E}}, {{coord|77|38|0|S|166|24|0|E}}, spaces and line breaks inside the template."""
    m = re.search(r'\{\{\s*coord\s*\|([^}]*)\}\}', txt, re.I)
    if not m: return (None, None)
    t = [x.strip() for x in m.group(1).split('|')]
    try:
        i = next(k for k, x in enumerate(t) if x in ('N', 'S'))
        j = next(k for k, x in enumerate(t) if k > i and x in ('E', 'W'))
        def val(parts):
            nums = [float(x) for x in parts if x not in ('',)]
            return sum(n / (60 ** k) for k, n in enumerate(nums[:3]))
        lat = val(t[:i]) * (-1 if t[i] == 'S' else 1)
        lon = val(t[i + 1:j]) * (-1 if t[j] == 'W' else 1)
        return (lat, lon)
    except Exception:
        return (None, None)

out = {}
# ---- 1. Research stations list
wt, ttl = get_wikitext('Research stations in Antarctica')
sections = [(m.start(), m.group(2)) for m in re.finditer(r'^(==+)\s*(.*?)\s*==+\s*$', wt, re.M)]
def section_text(name, nxt):
    a = [p for p, n in sections if n == name][0]
    b = [p for p, n in sections if n == nxt][0]
    return wt[a:b]
stations = []
for sec, nxt, kind in [('Permanent active stations', 'Subantarctic stations', 'permanent_active'), ('Subantarctic stations', 'Summer-only active stations', 'subantarctic'),
                       ('Summer-only active stations', 'Maps of active stations', 'summer_only_active'), ('Inactive stations', 'Impact and pollution', 'inactive')]:
    for tab in parse_tables(section_text(sec, nxt)):
        for cells in tab:
            if len(cells) < 6: continue
            name = clean(cells[0])
            rec = dict(list_section=kind, name=name, link=first_link(cells[0]), location=clean(cells[1]), country=clean(cells[2]), admin=clean(cells[3]), cells=[clean(c) for c in cells[4:]])
            if kind == 'permanent_active':   # est, max, summer, winter, utc, temp
                c = rec['cells']; rec.update(year_est=c[0], max_pers=c[1], summer_pop=c[2], winter_pop=c[3], mat=c[5] if len(c) > 5 else '')
            elif kind == 'summer_only_active':   # est, max, summer, utc, temp
                c = rec['cells']; rec.update(year_est=c[0], max_pers=c[1], summer_pop=c[2], winter_pop='', mat=c[4] if len(c) > 4 else '')
            elif kind == 'subantarctic':
                c = rec['cells']; rec.update(year_est=c[0], summer_pop=c[1], winter_pop=c[2], mat=c[4] if len(c) > 4 else '')
            else:   # inactive: est, type, utc, temp, year closed, status
                c = rec['cells']; rec.update(year_est=c[0], op_type=c[1], year_closed=c[4] if len(c) > 4 else '', status_text=c[5] if len(c) > 5 else '')
            stations.append(rec)
    # first table only holds the main list per section; keep going (sections can hold several tables)
out['stations'] = stations
# ---- 2. Field camps
wt2, _ = get_wikitext('Antarctic field camps')
camps = []
for tab in parse_tables(wt2):
    for cells in tab:
        if len(cells) < 8: continue
        name = clean(cells[0])
        if not name: continue
        lat, lon = parse_coord('||'.join(cells))
        camps.append(dict(name=name, link=first_link(cells[0]), location=clean(cells[1]), country=clean(cells[2]), year_est=clean(cells[3]), activities=clean(cells[4]),
                          type_status=clean(cells[5]), serving_base=clean(cells[6]), lat=lat, lon=lon, coord_raw=clean(cells[7])[:80]))
out['camps'] = camps
# ---- 3. Airports
wt3, _ = get_wikitext('List of airports in Antarctica')
airports = []
for tab in parse_tables(wt3):
    for cells in tab:
        if len(cells) < 7: continue
        name = clean(cells[0])
        lat, lon = parse_coord('||'.join(cells))
        airports.append(dict(name=name, link=first_link(cells[0]), country=clean(cells[1]), icao=(re.findall(r'\b[A-Z]{4}\b', clean(cells[2])) or [''])[0], iata=clean(cells[3]), other=clean(cells[4]), location=clean(cells[5]), lat=lat, lon=lon, runway=clean(cells[7]) if len(cells) > 7 else ''))
out['airports'] = airports
# ---- 4. HSM
wt4, _ = get_wikitext('Historic Sites and Monuments in Antarctica')
hsm = []
for chunk in wt4.split('{{Antarctic Protected Area row')[1:]:
    f = dict(re.findall(r'\n\s*\|\s*([a-zA-Z_0-9]+)\s*=\s*(.*)', chunk))
    def num(x):
        try: return float(x)
        except: return None
    hsm.append(dict(type=f.get('type', '').strip(), number=f.get('number', '').strip(), name=clean(f.get('name', '')), description=clean(f.get('description', '')),
                    proponent=clean(f.get('proponent', '')), management=clean(f.get('management', '')), adopted=clean(f.get('adopted', '')), lat=num(f.get('lat', '').strip()), lon=num(f.get('lon', '').strip()), link=first_link(f.get('name', ''))))
out['hsm'] = hsm
# ---- 5. title lookup (coords + wikidata id) for all linked titles + category members
cat_members = json.load(open(os.path.join(RAW, 'wp_category_members.json')))
titles = set(cat_members.keys())
for k in ('stations', 'camps', 'airports', 'hsm'):
    for r in out[k]:
        if r.get('link'): titles.add(r['link'])
titles = sorted(titles)
info = {}
for i in range(0, len(titles), 40):
    batch = titles[i:i + 40]
    cont = {}
    while True:
        r = requests.get(API, headers=UA, params=dict(action='query', prop='coordinates|pageprops', ppprop='wikibase_item', colimit=500, coprimary='primary', redirects=1, titles='|'.join(batch), format='json', **cont), timeout=60).json()
        q = r.get('query', {})
        redir = {x['from']: x['to'] for x in q.get('redirects', [])}
        norm = {x['from']: x['to'] for x in q.get('normalized', [])}
        for pid, p in q.get('pages', {}).items():
            t = p.get('title')
            d = info.setdefault(t, {})
            if 'coordinates' in p: d['lat'] = p['coordinates'][0]['lat']; d['lon'] = p['coordinates'][0]['lon']
            if 'pageprops' in p: d['qid'] = p['pageprops'].get('wikibase_item')
        for a in batch:
            t = norm.get(a, a); t = redir.get(t, t)
            if t in info: info[a] = info[t]
        if 'continue' in r: cont = {k: v for k, v in r['continue'].items()}
        else: break
    time.sleep(0.2)
out['titles'] = info
out['cat_members'] = cat_members
json.dump(out, open(os.path.join(RAW, 'wp_parsed.json'), 'w'), indent=1, ensure_ascii=False)
for k in ('stations', 'camps', 'airports', 'hsm'): print(k, len(out[k]))
print('titles', len(titles), 'with coords', sum(1 for t in titles if 'lat' in info.get(t, {})), 'with qid', sum(1 for t in titles if info.get(t, {}).get('qid')))
import collections
print(collections.Counter(s['list_section'] for s in stations))
