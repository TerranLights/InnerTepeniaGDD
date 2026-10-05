#!/usr/bin/env python3
"""Build Real_Station_Inventory_Raw.csv from the merged entities (06_load_and_merge.py -> RAW/merge_state.json).
Also writes RAW/build_diag.json (disagreements, exclusions, counts) used for the Method_and_Log.md."""
import os, re, sys, json, csv, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inv_lib import *
OUT = os.environ.get('OUT_CSV', '/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Towns/Data/Real_Station_Inventory_Raw.csv')
st = json.load(open(os.path.join(RAW, 'merge_state.json')))
OBS = {o['src'] + ':' + o['sid']: o for o in st['obs']}
EXTR = json.load(open(os.path.join(RAW, 'wp_extracts.json')))
WDL = json.load(open(os.path.join(RAW, 'wd_labels.json')))
SRC_PRI = ['comnap24', 'comnap17', 'wikidata', 'wp_list', 'wp_camps', 'wp_airports', 'wp_hsm', 'scar']
SRC_LABEL = {'comnap24': 'COMNAP Facilities CSV (Nov 2024)', 'comnap17': 'COMNAP Station Catalog (Aug 2017)', 'wikidata': 'Wikidata', 'wp_list': 'Wikipedia: Research stations in Antarctica (list)',
             'wp_camps': 'Wikipedia: Antarctic field camps', 'wp_airports': 'Wikipedia: List of airports in Antarctica', 'wp_hsm': 'Wikipedia: Historic Sites and Monuments in Antarctica', 'scar': 'SCAR Composite Gazetteer (placenames.aq)'}
COORD_PRI = ['comnap24', 'comnap17', 'wikidata', 'wp_list', 'wp_camps', 'wp_airports', 'wp_hsm', 'scar']

def lat_ok(o): return o['lat'] is not None and o['lon'] is not None
def latin(s): return bool(re.search(r'[A-Za-z]', s or ''))
def first_num(s):
    m = re.search(r'-?\d[\d,]*\.?\d*', s or '')
    return m.group(0).replace(',', '') if m else None

FAC_WORDS = re.compile(r"\b(station|base|camp|hut|huts|refuge|shelter|laborator\w*|runway|skiway|airfield|airstrip|aerodrome|airport|heliport|helipad|facility|observatory|depot|settlement|village|museum|research|outpost)\b", re.I)
GEO_SUBJ = re.compile(r"\b(is|was) (a|an|the) [^.]{0,70}?\b(peak|mountain|glacier|island|islands|bay|cape|lake|point|nunatak|peninsula|beach|hill|hills|ridge|cove|range|valley|pass|bluff|rock|plateau|cliff|headland|inlet|snowfield|coast)\b", re.I)
def facility_extract(t):
    s = re.split(r'(?<=[a-z\)])\.\s', t.strip().replace('\n', ' '))[0]
    if not FAC_WORDS.search(' '.join(s.split()[:30])): return False
    m = GEO_SUBJ.search(s)
    if m and not re.search(r"\b(station|base|camp|hut|refuge|runway|skiway|airfield|airstrip|laborator\w*)\b", s[:m.end()], re.I): return False
    if m and re.match(r".{0,60}\b(peak|mountain|glacier|nunatak|ridge|cape|point|island)\b", s, re.I) and not re.search(r"\b(station|base|camp|hut|refuge|runway|skiway|airfield|airstrip)\b[^.]{0,40}\b(is|was)\b", s[:m.start()+5], re.I) and not re.match(r"[^.]{0,60}\b(station|base|camp|hut|refuge|runway|skiway|airfield|airstrip)\b", s[:m.start()], re.I): return False
    return True
rows = []; diag = dict(out_of_scope=[], coord_disagree=[], status_disagree=[], name_disagree=[], sign_issues=[], no_coords=[], lat_fix=[], year_disagree=[])
for ei, keys in enumerate(st['ents']):
    obs = [OBS[k] for k in keys]
    main = [o for o in obs if not o.get('sub')]
    subs = [o for o in obs if o.get('sub')]
    by = collections.defaultdict(list)
    for o in main: by[o['src']].append(o)
    first = lambda src: by[src][0] if by.get(src) else None
    # ---------- kind (curated sources first)
    kind = None
    for src in ['comnap24', 'wp_list', 'wp_camps', 'wp_airports', 'wikidata', 'wp_hsm', 'scar', 'comnap17']:
        if by.get(src):
            kinds = [o['kind'] for o in by[src] if o['kind'] not in ('excluded', 'aws')]
            if src in ('wikidata', 'scar') and not kinds: continue
            if kinds: kind = kinds[0]; break
    if kind is None:
        kind = 'aws' if any(o['kind'] == 'aws' for o in main) else 'other'
    # ---------- names
    names = []
    def addn(n, src):
        n = (n or '').strip()
        if n and n not in [x[0] for x in names]: names.append((n, src))
    for src in ['comnap24', 'wikidata', 'wp_list', 'wp_camps', 'wp_airports', 'wp_hsm', 'comnap17', 'scar']:
        for o in by.get(src, []):
            addn(o['name'], src)
    pri = None
    for n, s in names:
        if latin(n) and not re.fullmatch(r'Q\d+', n) and not n.isupper(): pri = (n, s); break
    if pri is None:
        for n, s in names:
            if latin(n) and not re.fullmatch(r'Q\d+', n): pri = (n, s); break
    if pri is None:
        for o in by.get('wikidata', []):
            for v in WDL.get(o['qid'], {}).get('labels_other', {}).values():
                if latin(v): pri = (v, 'wikidata'); break
    if pri is None: pri = names[0]
    alts = []
    seen = {fold(pri[0]).lower()}
    for n, s in names:
        k = fold(n).lower()
        if k not in seen and latin(n): alts.append(n); seen.add(k)
    for o in main:
        for a in o['alts']:
            k = fold(a).lower()
            if latin(a) and k not in seen and not re.fullmatch(r'Q\d+', a): alts.append(a); seen.add(k)
        if o['src'] == 'wikidata':
            for lang, al in WDL.get(o['qid'], {}).get('aliases', {}).items():
                for a in al[:3]:
                    k = fold(a).lower()
                    if latin(a) and k not in seen: alts.append(a); seen.add(k)
    # ---------- coordinates
    coords = []   # (src, label, lat, lon)
    flags = []
    for src in COORD_PRI:
        for o in by.get(src, []):
            if not lat_ok(o): continue
            lat, lon = o['lat'], o['lon']
            lab = src
            if src == 'comnap17': lab = 'comnap17(DMS %s)' % o.get('dms', '')
            elif src == 'wikidata': lab = 'wikidata:' + o['qid']
            elif src == 'scar': lab = 'scar:%s:%s' % (o['gaz'], o['sid'])
            elif src == 'wp_list': lab = 'wp_list(article coords%s)' % (': ' + o['wp_title'] if o.get('wp_title') else '')
            elif src == 'wp_camps': lab = 'wp_camps'
            elif src == 'wp_airports': lab = 'wp_airports'
            elif src == 'wp_hsm': lab = 'wp_hsm:' + o['sid']
            if lat > 0:
                diag['lat_fix'].append((pri[0], lab, lat, lon))
                flags.append('source latitude positive (north) in %s: %.6f; sign flipped to south for use' % (src, lat))
                lat = -lat
            coords.append((src, lab, lat, lon, o))
    primary = coords[0] if coords else None
    plat = plon = None; csrc = 'unknown'
    if primary:
        plat, plon, csrc = primary[2], primary[3], primary[1]
        # consensus check: if primary (comnap/other) has lon sign opposite to every other source that agree with each other
        others = [c for c in coords[1:]]
        if others:
            ds = [haversine((plat, plon), (c[2], c[3])) for c in others]
            far = [c for c, d in zip(others, ds) if d > 2]
            if len(far) == len(others) and len(others) >= 2:
                # do others agree with each other?
                dd = [haversine((others[0][2], others[0][3]), (c[2], c[3])) for c in others[1:]]
                if all(d < 2 for d in dd):
                    plat, plon, csrc = others[0][2], others[0][3], others[0][1] + ' (consensus of %d later sources; first-priority source disagrees)' % len(others)
                    flags.append('primary coordinate taken from consensus of %d sources because first-priority source %s differs' % (len(others), primary[1]))
    maxd = 0.0; dis = []
    if plat is not None:
        for c in coords:
            d = haversine((plat, plon), (c[2], c[3]))
            if d is not None and d > maxd: maxd = d
            if d is not None and d > 2.0:
                dis.append('%s (%.1f km)' % (c[1], d))
                # sign tests
                if abs(c[2] - plat) < 0.05 and abs(abs(c[3]) - abs(plon)) < 0.1 and (c[3] > 0) != (plon > 0) and abs(plon) > 1:
                    flags.append('longitude sign differs in %s (|lon| agrees within 0.1 deg)' % c[1]); diag['sign_issues'].append((pri[0], c[1], 'lon sign'))
                elif abs(c[3] - plon) < 0.1 and abs(abs(c[2]) - abs(plat)) < 0.1 and (c[2] > 0) != (plat > 0):
                    flags.append('latitude sign differs in %s' % c[1]); diag['sign_issues'].append((pri[0], c[1], 'lat sign'))
                elif (c[3] > 0) != (plon > 0) and haversine((plat, plon), (c[2], -c[3])) is not None and haversine((plat, plon), (c[2], -c[3])) < 15 and abs(plon) > 1:
                    flags.append('possible longitude sign error: %s mirrored in longitude is %.1f km from primary' % (c[1], haversine((plat, plon), (c[2], -c[3])))); diag['sign_issues'].append((pri[0], c[1], 'lon sign (mirror within 15 km)'))
                elif abs(c[2] - plat) < 0.02 and abs(c[3] - plon) < 0.5 and False: pass
        if dis: diag['coord_disagree'].append((pri[0], '%.1f' % maxd, '; '.join(dis)))
    else:
        diag['no_coords'].append(pri[0])
    # scope
    if plat is not None and plat > -60.0:
        diag['out_of_scope'].append((pri[0], '%.3f,%.3f' % (plat, plon), '; '.join(sorted({o['src'] for o in main}))))
        continue
    # ---------- elevation
    ev = []
    for src in ['comnap24', 'comnap17', 'wikidata', 'scar']:
        for o in by.get(src, []):
            if o.get('elev') is not None: ev.append((src, o['elev']))
    elev = ev[0][1] if ev else None
    elev_src = ev[0][0] if ev else 'unknown'
    elev_by = ' | '.join('%s:%g' % e for e in ev) if ev else 'unknown'
    # ---------- type
    cn = first('comnap24')
    detail = []
    for o in main:
        t = o.get('type_label') or o.get('types') or o.get('type_status') or o.get('op_type') or o.get('feature_type') or ''
        if isinstance(t, list): t = '; '.join(t)
        if t: detail.append('%s:%s' % (o['src'], t))
    nm = pri[0]
    if kind == 'station': typ = 'station'
    elif kind == 'camp': typ = 'field camp'
    elif kind == 'refuge': typ = 'hut-refuge'
    elif kind == 'airfield': typ = 'airfield'
    elif kind == 'aws': typ = 'automatic weather station'
    elif kind == 'hist': typ = 'hut-refuge' if re.search(r'hut|shelter|house|refuge|igloo|huts', nm, re.I) else 'other'
    elif kind == 'lab': typ = 'other'
    elif kind == 'depot': typ = 'other'
    else: typ = 'other'
    if typ in ('field camp', 'other') and kind in ('camp', 'hist') and re.search(r'\bhut\b|huts|shelter|\bhouse\b|igloo|refuge', nm, re.I): typ = 'hut-refuge'
    if kind == 'lab': detail.append('laboratory')
    if kind == 'depot': detail.append('depot')
    # ---------- status
    def cat(s): return {'year-round': 'active', 'summer-only': 'active'}.get(s, 'inactive' if s in ('closed', 'abandoned', 'historic') else 'unknown')
    cands = []
    for o in by.get('comnap24', []):
        if o['status_label'] == 'Temporarily Closed': cands.append(('comnap24', 'closed', 'COMNAP 2024: Temporarily Closed (seasonality %s)' % o['seasonality']))
        elif o['seasonality'] == 'Year-Round': cands.append(('comnap24', 'year-round', 'COMNAP 2024: Year-Round, Open'))
        else: cands.append(('comnap24', 'summer-only', 'COMNAP 2024: Seasonal, Open'))
    for o in by.get('comnap17', []):
        op = o['operational_period']
        cands.append(('comnap17', 'year-round' if op.lower().startswith('year') else 'summer-only', 'COMNAP 2017: operational period "%s"' % op))
    for o in by.get('wp_list', []):
        sec = o['list_section']
        if sec == 'permanent_active': cands.append(('wp_list', 'year-round', 'Wikipedia list: permanent active'))
        elif sec == 'summer_only_active': cands.append(('wp_list', 'summer-only', 'Wikipedia list: summer-only active'))
        elif sec == 'inactive' and by.get('comnap24') and by['comnap24'][0]['status_label'] != 'Temporarily Closed':
            pass   # predecessor row at the same site: kept in notes only
        elif sec == 'inactive':
            t = o.get('status_text', '')
            s = 'abandoned' if re.search(r'abandon', t, re.I) else 'closed'
            cands.append(('wp_list', s, 'Wikipedia list (inactive): "%s"%s' % (t, ', closed %s' % o['year_close'] if o.get('year_close') else '')))
    for o in by.get('wp_camps', []):
        t = o['type_status']
        if re.search(r'Historic|ASPA', t): s = 'historic'
        elif re.search(r'Abandon', t): s = 'abandoned'
        elif re.search(r'Closed|Lost|Destroyed|Dismantled|Demolished|Removed|inactive|Covered by ice|Temporary closed', t, re.I): s = 'closed'
        elif re.search(r'Open|Occasionally used|Rebuilt', t, re.I): s = 'summer-only'
        else: s = 'unknown'
        cands.append(('wp_camps', s, 'Wikipedia field-camps list: "%s"' % t))
    for o in by.get('wp_hsm', []):
        cands.append(('wp_hsm', 'historic', 'Historic Site/Monument no. %s' % o['hsm']))
    for o in by.get('wikidata', []):
        if o.get('year_close'): cands.append(('wikidata', 'closed', 'Wikidata dissolved/closed %s' % o['year_close']))
    for o in by.get('scar', []):
        if o.get('relic'): cands.append(('scar', 'historic', 'SCAR gazetteer relic flag'))
    status = 'unknown'; sdetail = 'no source gives status'
    for c in cands:
        if c[1] != 'unknown': status, sdetail = c[1], c[2]; break
    first_src = next((c[0] for c in cands if c[1] != 'unknown'), None)
    if first_src and first_src not in ('comnap24',):
        same = [c for c in cands if c[0] == first_src and c[1] != 'unknown']
        if len({cat(c[1]) for c in same}) > 1:
            status = 'unknown'; sdetail = 'conflict inside %s: %s' % (first_src, ' vs '.join(c[2] for c in same))
    cmp_c = [c for c in cands if c[0] in ('comnap24', 'comnap17', 'wp_list', 'wp_camps', 'wikidata') and c[1] != 'unknown']   # Historic-Sites/SCAR 'historic' labels describe monuments inside active stations, not a conflict
    cats = {cat(c[1]) for c in cmp_c}
    kinds_seen = {c[1] for c in cmp_c if c[1] in ('year-round', 'summer-only')}
    if len(cats - {'unknown'}) > 1 or len(kinds_seen) > 1:
        diag['status_disagree'].append((pri[0], '; '.join('%s=%s' % (c[0], c[1]) for c in cands)))
    all_status = ' || '.join('%s: %s' % (c[0], c[2]) for c in cands) or 'unknown'
    # ---------- years
    yo = []; yc = []
    for src in ['comnap24', 'wp_list', 'wp_camps', 'wikidata']:
        for o in by.get(src, []):
            y = yr(o.get('year_open', ''))
            if y and not (src == 'wp_list' and o['list_section'] == 'inactive' and by.get('comnap24') and by['comnap24'][0]['status_label'] != 'Temporarily Closed'): yo.append((src, y))
    for o in by.get('wp_list', []):
        y = yr(o.get('year_close', ''))
        if y and not (o['list_section'] == 'inactive' and by.get('comnap24') and by['comnap24'][0]['status_label'] != 'Temporarily Closed'): yc.append(('wp_list', y))
    for o in by.get('wp_camps', []):
        m = re.search(r'(?:Closed|Abandoned|Demolished|Dismantled|Removed|inactive since|Destroyed in)\s*(?:in\s*)?(1[89]\d\d|20\d\d)', o['type_status'] + ' ' + o.get('activities', ''))
        if m: yc.append(('wp_camps', m.group(1)))
        else:
            m = re.search(r'Abandoned\s*/\s*(1[89]\d\d)', o['type_status'])
            if m: yc.append(('wp_camps', m.group(1)))
    for o in by.get('wikidata', []):
        if o.get('year_close'): yc.append(('wikidata', o['year_close']))
    year_open = yo[0][1] if yo else 'unknown'
    if cn and cn['status_label'] != 'Temporarily Closed':   # entity has a current (open) COMNAP 2024 record: closure years in other sources belong to predecessors/other eras; kept in years_by_source only
        yc_other = [('%s(other era/predecessor)' % s, y) for s, y in yc]; yc = []
    elif cn:   # temporarily closed per COMNAP: accept closure years only from rows with the same station name; other rows are predecessors at the site
        pred = [oo for oo in main if oo['src'] in ('wp_list', 'wikidata') and yr(oo.get('year_close', '')) and name_score(oo['name'], pri[0]) < 0.5]
        yc_other = [('%s(predecessor row "%s")' % (oo['src'], oo['name']), yr(oo.get('year_close', ''))) for oo in pred]
        yc = [(s, y) for s, y in yc if not any(s == oo['src'] and y == yr(oo.get('year_close', '')) for oo in pred)]
    else: yc_other = []
    year_close = yc[0][1] if yc else 'unknown'
    if status in ('year-round', 'summer-only') and not yc: year_close = 'n/a (active)'
    elif status == 'closed' and not yc and cn and cn['status_label'] == 'Temporarily Closed': year_close = 'n/a (temporarily closed per COMNAP 2024)'
    ybs = ' | '.join('open %s:%s' % x for x in yo) + (' | ' if yo and (yc or yc_other) else '') + ' | '.join('closed %s:%s' % x for x in (yc + yc_other))
    if not ybs: ybs = 'unknown'
    if len({y for _, y in yo}) > 1: diag['year_disagree'].append((pri[0], ybs))
    # ---------- capacity
    cw = cs = cp = cb = None; capsrc = []
    c17 = first('comnap17')
    if c17:
        def nz(x): return x if x and x != 'unknown' else None
        cw, cs, cb = nz(c17['staff_winter']), nz(c17['staff_summer']), nz(c17['beds'])
        cp = nz(c17['max_personnel'])
        if cw or cs or cb or cp: capsrc.append('COMNAP 2017 (staff on station winter/summer, beds, max personnel)')
    wl = first('wp_list')
    if wl:
        if not cw and wl.get('winter_pop'): cw = wl['winter_pop']; capsrc.append('Wikipedia list winter pop')
        if not cs and wl.get('summer_pop'): cs = wl['summer_pop']; capsrc.append('Wikipedia list summer pop')
        if not cp and wl.get('max_pers'): cp = wl['max_pers']; capsrc.append('Wikipedia list max persons')
    if cn and cn.get('peak_pop') and not cp:
        cp = cn['peak_pop']; capsrc.append('COMNAP 2024 peak population')
    elif cn and cn.get('peak_pop') and cp and cp.replace(',', '') != cn['peak_pop'].replace(',', ''):
        capsrc.append('COMNAP 2024 peak population %s (differs)' % cn['peak_pop'])
    # ---------- operator
    ops = []
    def addo(x):
        for x in (x or '').split(' ; '):
            x = ' '.join(x.split())
            if x and x not in ops: ops.append(x)
    for src in ['comnap24', 'wp_list', 'wp_camps', 'wp_airports', 'wikidata']:
        for o in by.get(src, []):
            if src == 'wp_list': addo((o['country'] + (' - ' + o['admin'] if o.get('admin') else '')))
            elif src in ('wp_camps', 'wp_airports'): addo(o['country'])
            else: addo(o.get('operator'))
    if not ops:
        for o in by.get('comnap17', []): addo(o.get('operator'))
    for o in by.get('wp_hsm', []): addo(o.get('proponent'))
    for o in by.get('scar', [])[:0]: pass
    ops = [o for o in ops if o and o != '-']
    # drop garbled COMNAP-2017 name/operator lines when something else exists; drop strings contained in longer ones
    ops_f = [o for o in ops if not re.search(r'^\S.*\b(Station|Base|Hut)\b.*(Antarctic|Programa|Institute|Survey)', o)] or ops
    keep = []
    for o in ops_f:
        if not any(o != x and o.lower() in x.lower() for x in ops_f) and o not in keep: keep.append(o)
    operator = ' ; '.join(keep[:4]) if keep else 'unknown'
    # ---------- text bundle
    texts = []   # (src, field, text)
    for o in by.get('comnap17', []):
        texts += [('comnap17', 'location', o.get('location_text', '')), ('comnap17', 'history', o.get('history_text', ''))]
    for o in by.get('wp_list', []): texts.append(('wp_list', 'location', o.get('location_text', '')))
    for o in by.get('wp_camps', []): texts += [('wp_camps', 'location', o.get('location_text', '')), ('wp_camps', 'activities', o.get('activities', ''))]
    for o in by.get('wp_airports', []): texts.append(('wp_airports', 'location', o.get('location_text', '')))
    for o in by.get('wp_hsm', []): texts.append(('wp_hsm', 'description', o.get('description', '')))
    for o in by.get('scar', []): texts.append(('scar', 'narrative', o.get('narrative', '')))
    for o in by.get('wikidata', []):
        texts.append(('wikidata', 'description', o.get('desc', '')))
    titles = {o.get('wp_title') for o in main if o.get('wp_title')}
    for t in sorted(titles):
        ex = EXTR.get(t, '')
        if ex and facility_extract(ex): texts.append(('wikipedia:' + t, 'intro', ex))
    # ---------- purpose
    purpose = None; psrc = None
    if c17 and c17['disciplines'] not in ('unknown', '') and 'www.' not in c17['disciplines']:
        purpose = 'science disciplines: ' + c17['disciplines'].rstrip('.'); psrc = 'COMNAP 2017 "Main science disciplines"'
    if not purpose:
        for o in by.get('wp_camps', []):
            if o.get('activities'): purpose = o['activities']; psrc = 'Wikipedia field-camps list "Activities"'; break
    if not purpose:
        for o in by.get('wp_camps', []):
            if o.get('serving_base') and o['serving_base'].strip() not in ('', 'n/a'):
                purpose = 'support site serving %s (listed as serving base)' % o['serving_base']; psrc = 'Wikipedia field-camps list "Serving base"'; break
    if not purpose:
        for src, f, t in texts:
            if src.startswith('wikipedia:') and t:
                s = re.split(r'(?<=[a-z\)])\.\s', t.strip().replace('\n', ' '))[0]
                purpose = s[:230]; psrc = '%s (first sentence)' % src; break
    if not purpose:
        for src, f, t in texts:
            if src == 'wp_hsm' and t: purpose = t[:200]; psrc = 'Historic Sites list description'; break
    if not purpose:
        for src, f, t in texts:
            if src == 'scar' and t and len(t) > 25 and not t.startswith('Unmanned') and re.search(r'station|base\b|camp|research|scientific|established|operated|hut|refuge|depot|runway|skiway|airstrip|expedition', re.split(r'(?<=[a-z\)])\.\s', t.strip())[0], re.I):
                s = re.split(r'(?<=[a-z\)])\.\s', t.strip())[0]; purpose = s[:230]; psrc = 'SCAR gazetteer narrative (first sentence)'; break
    if not purpose:
        for src, f, t in texts:
            if src == 'wikidata' and t: purpose = t; psrc = 'Wikidata description'; break
    if not purpose:
        wdt = [t for o in by.get('wikidata', []) for t in o.get('types', [])]
        if wdt: purpose = 'unknown (Wikidata class only: %s)' % '; '.join(sorted(set(wdt))[:3]); psrc = 'Wikidata instance-of'
        else: purpose = 'unknown'; psrc = 'unknown'
    if cn and not (purpose or '').strip(): purpose = 'unknown'
    if purpose and len(purpose) > 220: purpose = purpose[:217].rsplit(' ', 1)[0] + ' [...]'
    # ---------- surface
    ev_ice = []; ev_rock = []; ev_move = []; surface_stated = None
    PREP = r"\b(on|atop|upon|onto)\s+(the\s+)?"
    BAD_MID = re.compile(r"shore|edge|side|slope|flank|foot|snout|margin|valley|terminus|near|beside|adjacent|south|north|east|west|toe|front|mouth|head of", re.I)
    def prose_hits(tt):
        out = []
        for m in re.finditer(PREP + r"((?:[\w'’\-\.]+\s+){0,5}?)(ice[\s-]shelf|ice tongue)", tt, re.I):
            if not BAD_MID.search(m.group(3)): out.append(('shelf', m))
        for m in re.finditer(PREP + r"((?:[\w'’\-]+\s+){0,4}?)glacier\b", tt, re.I):
            if not BAD_MID.search(m.group(3)) and not re.match(r"\s*(of|bay|inlet)", tt[m.end():m.end() + 8], re.I): out.append(('glac', m))
        for m in re.finditer(PREP + r"((?:[\w'’\-]+\s+){0,3}?)(ice[\s-]sheet|ice cap|ice dome|ice divide|snow plain|plateau)\b|\bAntarctic Plateau\b|East Antarctic Ice Sheet|West Antarctic Ice Sheet", tt, re.I):
            out.append(('sheet', m))
        for m in re.finditer(r"\bon\s+(the\s+)?(fast\s+|sea\s+)?sea[\s-]ice|sea[\s-]ice (skiway|runway|station|camp)", tt, re.I):
            out.append(('sea', m))
        return out
    def loc_hits(tt):
        out = []
        for k, rg in (('shelf', r"ice[\s-]shelf|ice tongue"), ('glac', r"\bglacier\b"), ('sheet', r"ice[\s-]sheet|plateau|\bdome\b|ice divide|ice cap"), ('sea', r"sea[\s-]ice")):
            m = re.search(rg, tt, re.I)
            if m: out.append((k, m))
        return out
    def rock_hits(tt):
        out = []
        for rg in (PREP + r"((?:[\w'’\-\.]+\s+){0,4}?)(nunatak|rock outcrop|outcrop|rocky (?:point|peninsula|island|ridge|ground|shore|promontory|bluff))\b",
                   r"\bice[-\s]free\b", r"\b(in|at|on)\s+(the\s+)?([\w'’\-]+\s+){0,2}?oasis\b", r"\bstone hut\b|\bbare rock\b|\bsolid rock\b|\bbuilt on rock\b|\bscoria\b"):
            m = re.search(rg, tt, re.I)
            if m: out.append(m)
        return out
    rx = dict(move=re.compile(r"\bmoved\b|relocat|resited|crushed|\bsank\b|\bsunk\b|buried|snowed under|under snow|calved|deterioration of the ice|moving ice|ice[\s-]flow", re.I))
    st_texts = []
    for o in by.get('comnap17', []):
        if o['surface_type'] and o['surface_type'] != 'unknown':
            surface_stated = ('COMNAP 2017 "Type of surface facility built on": %s' % o['surface_type'], o['surface_type'])
    for o in by.get('wp_airports', []):
        rw = o.get('runway', '')
        if re.search(r'Sea Ice', rw, re.I): ev_ice.append(('sea', 'Wikipedia airports list runway surface "%s"' % re.sub(r'\{\{.*?\}\}', '', rw).strip()[:40]))
        elif re.search(r'Gravel', rw, re.I): ev_rock.append('Wikipedia airports list runway surface Gravel')
    for src, f, t in texts:
        if not t: continue
        tt = t.replace('\n', ' ')
        hits = loc_hits(tt) if f == 'location' and src in ('wp_list', 'wp_camps', 'wp_airports') else prose_hits(tt)
        for k, m in hits:
            ev_ice.append((k, '%s %s: "...%s..."' % (src, f, tt[max(0, m.start() - 20):m.end() + 20].strip()[:100])))
        for m in rock_hits(tt):
            ev_rock.append('%s %s: "...%s..."' % (src, f, tt[max(0, m.start() - 20):m.end() + 20].strip()[:100]))
        m = rx['move'].search(tt)
        if m and not (src == 'wikidata'): ev_move.append('%s %s: "...%s..."' % (src, f, tt[max(0, m.start() - 30):m.end() + 30].strip()[:110]))
    for o in by.get('wp_list', []):
        if o['list_section'] == 'inactive' and re.search(r'lost|under snow|sunk', o.get('status_text', ''), re.I):
            ev_move.append('wp_list status "%s"' % o['status_text'])
    surface = 'unknown'; ssrc = 'no source states the surface'; flag = 'unknown'
    kinds_ice = {k for k, _ in ev_ice}
    st_s = surface_stated[1].lower() if surface_stated else ''
    if surface_stated:
        if 'shelf' in st_s: surface = 'ice shelf'; flag = 'ice_shelf_or_glacier_or_sea_ice (needs velocity test)'
        elif 'sheet' in st_s and ('moraine' in st_s or 'rock' in st_s): surface = 'rock and ice'; flag = 'ice_shelf_or_glacier_or_sea_ice (needs velocity test)'
        elif 'sheet' in st_s or 'ice cap' in st_s: surface = 'ice sheet'; flag = 'ice_sheet_interior'
        elif 'glacier' in st_s: surface = 'glacier'; flag = 'ice_shelf_or_glacier_or_sea_ice (needs velocity test)'
        elif 'sea' in st_s: surface = 'sea ice'; flag = 'ice_shelf_or_glacier_or_sea_ice (needs velocity test)'
        elif re.search(r'ice-free|rock|scoria|ground|outcrop', st_s): surface = 'bare rock'; flag = 'rock'
        ssrc = surface_stated[0]
        # nunatak-on-shelf style mixed evidence
        if surface == 'ice shelf' and any(re.search(r'nunatak|rock outcrop', e, re.I) for e in ev_rock): surface = 'rock and ice'; ssrc += '; location text also says nunatak/rock'
        if surface == 'bare rock' and 'ice-free' in st_s: ssrc += ' (ice-free ground = rock/gravel/moraine; type of ground not stated)'
    else:
        strong_ice = [e for e in ev_ice if e[0] in ('shelf', 'sea', 'glac')]
        sheet_ev = [e for e in ev_ice if e[0] == 'sheet']
        # airfield with ice/snow runway: type of ice body not stated unless text says so
        if strong_ice:
            k0 = strong_ice[0][0]
            surface = {'shelf': 'ice shelf', 'sea': 'sea ice', 'glac': 'glacier'}[k0]
            flag = 'ice_shelf_or_glacier_or_sea_ice (needs velocity test)'
            if ev_rock and surface in ('ice shelf', 'glacier'): surface = 'rock and ice'
            ssrc = strong_ice[0][1]
        elif sheet_ev:
            surface = 'ice sheet'; flag = 'ice_sheet_interior'; ssrc = sheet_ev[0][1]
            if ev_rock: surface = 'rock and ice'; flag = 'unknown'; ssrc += ' ; also rock mentioned: ' + ev_rock[0]
        elif ev_rock:
            surface = 'bare rock'; flag = 'rock'; ssrc = ev_rock[0]
    # moved/relocated mention => flag for test unless stated rock
    move_note = ''
    if ev_move:
        move_note = 'moved/lost/relocated wording in sources: ' + ' || '.join(ev_move[:2])
        if flag == 'unknown' or (flag == 'ice_sheet_interior'):
            flag = 'ice_shelf_or_glacier_or_sea_ice (needs velocity test)' if flag == 'unknown' else flag
    # ---------- location text
    loc = ''
    for src, f, t in texts:
        if src == 'wp_list' and t: loc = t; break
    if not loc:
        for src, f, t in texts:
            if f == 'location' and t: loc = t[:200]; break
    if not loc and c17: loc = c17['location_text'][:200]
    if not loc and cn and cn.get('region'): loc = cn['region']
    if not loc: loc = 'unknown'
    # ---------- notes
    notes = []
    for o in subs:
        cl = '; '.join(o.get('types', [])) if o.get('types') else o['kind']
        notes.append('Also in %s (not a separate row): "%s" [%s] at %s,%s' % (o['src'], o['name'], cl, '%.4f' % o['lat'] if o['lat'] is not None else '?', '%.4f' % o['lon'] if o['lon'] is not None else '?'))
    if c17:
        notes.append('COMNAP 2017 DMS: ' + c17.get('dms', '') + ('' if not c17.get('dms_flags') else ' (flags: %s)' % '; '.join(c17['dms_flags'])))
    if cn and cn.get('ddm'): notes.append('COMNAP 2024 DDM: ' + cn['ddm'])
    for o in main:
        if o['src'] == 'wp_list' and o['list_section'] == 'inactive' and by.get('comnap24'):
            notes.append('Wikipedia inactive-list row at the same site: "%s" (%s, est %s, closed %s)' % (o['name'], o.get('status_text', ''), o.get('year_open', ''), o.get('year_close', '')))
        if o['src'] == 'wp_list' and o['list_section'] == 'subantarctic': notes.append('listed by Wikipedia among sub-Antarctic stations')
    wl_all = [o for o in by.get('wp_list', [])]
    if len(wl_all) > 1: notes.append('Wikipedia list has %d rows merged here: %s' % (len(wl_all), '; '.join('%s (%s %s-%s)' % (o['name'], o.get('status_text') or o['list_section'], o.get('year_open', ''), o.get('year_close', '')) for o in wl_all)))
    if move_note: notes.append(move_note)
    if cn and cn.get('region'): notes.append('COMNAP region: ' + cn['region'])
    if kind == 'airfield' and not by.get('wp_airports') and not by.get('comnap24'): notes.append('airfield/runway listed by Wikidata or SCAR only')
    for o in by.get('wp_airports', []):
        rw = re.sub(r'\{\{convert\|([\d,]+)\|ft\|m\}\}', r'\1 ft', o.get('runway', '')).replace('\n', ' ')
        if '{{' in rw: continue
        notes.append('Wikipedia airport list: runway "%s"%s' % (rw[:60], ', ICAO ' + o['icao'] if o.get('icao') else ''))
    for o in by.get('comnap17', [])[:1]:
        if o.get('permafrost') and o['permafrost'] != 'unknown': notes.append('COMNAP 2017 permafrost: ' + o['permafrost'])
    for o in by.get('wp_camps', []):
        if o.get('serving_base'): notes.append('Wikipedia camps list: serving base "%s"' % o['serving_base'])
    for o in by.get('wp_list', []):
        if o.get('wp_title') and '#' in str(o.get('sid', '')): pass
    MN = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'manual_notes.json')))
    if pri[0] in MN and not pri[0].startswith('_'): notes.append(MN[pri[0]])
    if flags: notes.append('COORD FLAGS: ' + ' ; '.join(dict.fromkeys(flags)))
    if plat is None: notes.append('no source gives coordinates')
    # known anomalies in individual sources (only where the sources themselves show the inconsistency)
    srcs = [s for s in SRC_PRI if by.get(s)]
    srcids = []
    for o in main:
        if o['src'] == 'wikidata': srcids.append('wikidata:' + o['qid'])
        elif o['src'] == 'scar': srcids.append('scar:%s:%s' % (o['gaz'], o['sid']))
        elif o['src'] in ('comnap24', 'comnap17'): srcids.append('%s:%s' % (o['src'], o['sid']))
        else: srcids.append('%s:%s' % (o['src'], o['sid'][:60]))
    wp_t = sorted(titles)
    rows.append(dict(
        name=pri[0], alternate_names=' | '.join(alts[:14]) if alts else 'none found',
        latitude='%.6f' % plat if plat is not None else 'unknown', longitude='%.6f' % plon if plon is not None else 'unknown',
        coord_source=csrc, coords_by_source=' | '.join('%s=%.6f,%.6f' % (c[1], c[2], c[3]) for c in coords) if coords else 'unknown',
        coord_disagreement_max_km=('%.1f' % maxd) if plat is not None else 'unknown', coord_disagreement_over_2km=('yes: ' + '; '.join(dis)) if dis else ('no' if plat is not None else 'unknown'),
        elevation_m=('%g' % elev) if elev is not None else 'unknown', elevation_source=elev_src, elevation_by_source=elev_by,
        type=typ, type_detail=' | '.join(detail[:6]) if detail else 'unknown',
        status=status, status_detail=sdetail, status_all_sources=all_status,
        year_opened=year_open, year_closed=year_close, years_by_source=ybs,
        capacity_winter=cw if cw else 'unknown', capacity_summer=cs if cs else 'unknown', capacity_peak_persons=cp if cp else 'unknown', beds=cb if cb else 'unknown',
        capacity_source='; '.join(capsrc) if capsrc else 'unknown',
        operator_context_only=operator, purpose_as_stated=(purpose or 'unknown').replace('\n', ' '), purpose_source=psrc or 'unknown',
        surface=surface, surface_source=ssrc, stability_flag=flag, location_text=loc.replace('\n', ' '),
        sources=' ; '.join(SRC_LABEL[s] for s in srcs), source_ids=' ; '.join(srcids[:14]) + (' ; ...' if len(srcids) > 14 else ''),
        wikipedia_titles=' | '.join(wp_t) if wp_t else 'none', notes=' || '.join(n.replace('\n', ' ') for n in notes) if notes else 'none', _sort=(plat if plat is not None else -99, plon if plon is not None else 0), _kind=kind, _src=set(srcs)))
# ids
cnt = collections.Counter()
rows.sort(key=lambda r: (r['name'].lower(), r['_sort']))
for r in rows:
    base = slug(r['name']) or 'unnamed'
    cnt[base] += 1
    r['id'] = base if cnt[base] == 1 else '%s-%d' % (base, cnt[base])
# first occurrence also needs no suffix; fine. Make order: by id
COLS = ['id', 'name', 'alternate_names', 'latitude', 'longitude', 'coord_source', 'coords_by_source', 'coord_disagreement_max_km', 'coord_disagreement_over_2km', 'elevation_m', 'elevation_source', 'elevation_by_source',
        'type', 'type_detail', 'status', 'status_detail', 'status_all_sources', 'year_opened', 'year_closed', 'years_by_source', 'capacity_winter', 'capacity_summer', 'capacity_peak_persons', 'beds', 'capacity_source',
        'operator_context_only', 'purpose_as_stated', 'purpose_source', 'surface', 'surface_source', 'stability_flag', 'location_text', 'sources', 'source_ids', 'wikipedia_titles', 'notes']
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=COLS, quoting=csv.QUOTE_MINIMAL, extrasaction='ignore')
    w.writeheader()
    for r in rows: w.writerow({c: (r.get(c) if r.get(c) not in (None, '') else 'unknown') for c in COLS})
diag['n_rows'] = len(rows)
diag['by_type'] = collections.Counter(r['type'] for r in rows)
diag['by_status'] = collections.Counter(r['status'] for r in rows)
diag['by_flag'] = collections.Counter(r['stability_flag'] for r in rows)
diag['by_surface'] = collections.Counter(r['surface'] for r in rows)
diag['by_source_combo'] = collections.Counter(' + '.join(sorted(r['_src'])) for r in rows)
srcc = collections.Counter()
for r in rows:
    for s in r['_src']: srcc[s] += 1
diag['rows_per_source'] = srcc
json.dump(diag, open(os.path.join(RAW, 'build_diag.json'), 'w'), ensure_ascii=False, indent=1, default=str)
print('rows', len(rows)); print(diag['by_type']); print(diag['by_status']); print(diag['by_flag']); print(diag['by_surface']); print(srcc)
print('out of scope', len(diag['out_of_scope']), 'no coords', len(diag['no_coords']))
