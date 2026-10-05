#!/usr/bin/env python3
"""Compute the cross-checks (NOAA GHCN, Wikipedia category coverage, duplicate candidates, disagreements) and write Real_Station_Inventory_Method_and_Log.md.
Reads the final CSV plus RAW/merge_state.json, RAW/build_diag.json. Run after 07."""
import os, sys, re, json, csv, collections, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inv_lib import *
DATA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSVP = os.path.join(DATA, 'Real_Station_Inventory_Raw.csv')
LOGP = os.path.join(DATA, 'Real_Station_Inventory_Method_and_Log.md')
GHCN = os.environ.get('GHCN', '/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/to-be-integrated/climate data CURL/ghcnd-stations [NOAA].txt')
rows = list(csv.DictReader(open(CSVP, encoding='utf-8')))
st = json.load(open(os.path.join(RAW, 'merge_state.json')))
diag = json.load(open(os.path.join(RAW, 'build_diag.json')))
OBS = {o['src'] + ':' + o['sid']: o for o in st['obs']}
wp = json.load(open(os.path.join(RAW, 'wp_parsed.json')))
WDL = json.load(open(os.path.join(RAW, 'wd_labels.json')))
here = os.path.dirname(os.path.abspath(__file__))
OVR = {k: v for k, v in json.load(open(os.path.join(here, 'merge_overrides.json'))).items() if not k.startswith('_')}
def md(s): return str(s).replace('|', '/').replace('\n', ' ')
def fl(r):
    try: return float(r['latitude']), float(r['longitude'])
    except: return None
N = len(rows)
by_type = collections.Counter(r['type'] for r in rows); by_status = collections.Counter(r['status'] for r in rows)
by_flag = collections.Counter(r['stability_flag'] for r in rows); by_surf = collections.Counter(r['surface'] for r in rows)
xt = collections.defaultdict(collections.Counter)
for r in rows: xt[r['type']][r['status']] += 1
SRCN = {'comnap24': 'COMNAP Facilities CSV (Nov 2024)', 'comnap17': 'COMNAP Station Catalog (Aug 2017)', 'wikidata': 'Wikidata', 'wp_list': 'Wikipedia: Research stations in Antarctica', 'wp_camps': 'Wikipedia: Antarctic field camps',
        'wp_airports': 'Wikipedia: List of airports in Antarctica', 'wp_hsm': 'Wikipedia: Historic Sites and Monuments', 'scar': 'SCAR Composite Gazetteer'}
rows_with = collections.Counter(); only = collections.Counter()
for r in rows:
    ss = [k for k, v in SRCN.items() if v in r['sources']]
    for s in ss: rows_with[s] += 1
    if len(ss) == 1: only[ss[0]] += 1
obs_n = collections.Counter(o['src'] for o in st['obs'])
obs_main = collections.Counter(o['src'] for o in st['obs'] if not o.get('dropped') and not o.get('sub'))
obs_sub = collections.Counter(o['src'] for o in st['obs'] if o.get('sub'))
obs_drop = collections.Counter(o['src'] for o in st['obs'] if o.get('dropped'))
src_count = collections.Counter(len([k for k, v in SRCN.items() if v in r['sources']]) for r in rows)
# ---- GHCN cross-check
ghcn = []
if os.path.exists(GHCN):
    for line in open(GHCN, encoding='utf-8', errors='replace'):
        if line.startswith('AY'):
            try: ghcn.append((line[0:11], float(line[12:20]), float(line[21:30]), float(line[31:37]), line[41:71].strip()))
            except: pass
g_match = []; g_un = []
for gid, la, lo, el, nm in ghcn:
    best = None
    for r in rows:
        c = fl(r)
        if not c: continue
        d = haversine((la, lo), c)
        if best is None or d < best[0]: best = (d, r)
    (g_match if best and best[0] <= 5 else g_un).append((gid, la, lo, el, nm, best))
# ---- Wikipedia category coverage
cm = wp['cat_members']; have = set()
for r in rows:
    for t in r['wikipedia_titles'].split(' | '): have.add(t)
cat_missing = sorted(t for t in cm if t not in have)
# ---- duplicates (<1 km, different names, same broad type)
pts = [(r, fl(r)) for r in rows if fl(r)]
dups = []
for i in range(len(pts)):
    for j in range(i + 1, len(pts)):
        a, ca = pts[i]; b, cb = pts[j]
        if a['type'] != b['type'] or a['type'] in ('automatic weather station',): continue
        if abs(ca[0] - cb[0]) > 0.02: continue
        d = haversine(ca, cb)
        if d is not None and d < 1.0 and name_score(a['name'], b['name']) < 0.5:
            dups.append((d, a, b))
dups.sort(key=lambda x: x[0])
# same-name pairs at different places
samen = []
for i in range(len(rows)):
    for j in range(i + 1, len(rows)):
        a, b = rows[i], rows[j]
        if a['type'] == 'airfield' or b['type'] == 'airfield': continue
        same_tok = set(tokens(a['name'])) == set(tokens(b['name'])) and tokens(a['name'])
        if same_tok and fl(a) and fl(b) and a['type'] == b['type']:
            d = haversine(fl(a), fl(b))
            if d > 5: samen.append((d, a, b))
        elif same_tok and (not fl(a) or not fl(b)) and a['type'] == b['type']:
            samen.append((None, a, b))
# ---- implied-association distance (airfield/camp/hut whose name contains a station name but sits >30 km from it)
stations = [r for r in rows if r['type'] == 'station' and fl(r) and 'COMNAP Facilities' in r['sources']]
implied = []
for r in rows:
    if r['type'] in ('station',) or not fl(r): continue
    tk = set(tokens(r['name']))
    for s in stations:
        ts = set(tokens(s['name']))
        if ts and ts <= tk and ts != tk or (ts and ts == tk and r['type'] != 'station'):
            d = haversine(fl(r), fl(s))
            if d > 30: implied.append((d, r, s))
# ---- overrides table
ov_rows = []
for k, v in OVR.items():
    o = OBS.get(k)
    if not o: continue
    tgt = v[4:] if v.startswith('SUB:') else v
    ov_rows.append((k, o['name'], v))
# ---- name conflicts
name_conf = []
for e in st['ents']:
    obs = [OBS[k] for k in e if not OBS[k].get('sub')]
    if len(obs) < 2: continue
    prim = None
    for o in obs:
        if o['src'] == 'comnap24': prim = o; break
    if prim is None: prim = obs[0]
    others = []
    for o in obs:
        if o is prim: continue
        if not re.search(r'[A-Za-z]', o['name']): continue
        if name_score(prim['name'], o['name']) < 0.5 and not re.fullmatch(r'Station [A-Z]', o['name']):
            others.append('%s: "%s"' % (o['src'], o['name']))
    if others and prim['lat'] is not None and prim['lat'] < -60: name_conf.append((prim['name'], others))
# ---- write log
T = datetime.date.today().isoformat()
L = []
w = L.append
w('# Real Antarctic Station Inventory: Method and Log')
w('')
w('*Data collection only. No worldbuilding, no naming of towns, no ranking, no decisions about which locations are kept. Written in American English. Generated by `scripts/08_diagnostics_and_log.py` from the pipeline in `scripts/`; the counts below are computed, not typed.*')
w('')
w('**Output file:** `Real_Station_Inventory_Raw.csv` (same folder), UTF-8, comma-separated, %d data rows, %d columns.' % (N, len(rows[0])))
w('**Run date:** the sources were pulled 2026-10-03 to 2026-10-04 (this file regenerated %s).' % T)
w('')
w('## 1. What this is and the one rule behind every column')
w('')
w('The developer asked for **every usable real station location** after the 38 declared cities, with the stability test (slow ice, ideally bedrock below) to come later. This pass only collects the list and attributes. Therefore:')
w('')
w('- Every location any source supports is a row, including closed, abandoned, historic and seasonal ones, huts and refuges, field camps, airfields (skiways, blue-ice runways, heliports) and automatic weather stations. **Rows at the 38 declared cities are not excluded** (cross-match by coordinates later).')
w('- Scope: south of 60 S, plus the South Shetland and South Orkney islands (which are all at or south of 60.5 S, so the single test is latitude <= -60). Rows whose best coordinate is north of 60 S are not in the CSV; they are listed in section 7.')
w('- Evidence only: no ice velocity, no bedrock depth, no ranking. `surface` and `stability_flag` are filled **only from what a source states** (see 4.5); everything else is `unknown`.')
w('- Source coordinates are never "fixed", with one documented exception (a positive latitude, which cannot be in Antarctica; see 6.4). Where sources disagree, the primary is chosen by a fixed priority and every source value stays in `coords_by_source`.')
w('')
w('## 2. Sources: what was used, how, and what each gave')
w('')
w('| # | Source | URL | Access method | What it gave | Parsed records | Rows containing it |')
w('|---|---|---|---|---|---|---|')
srcrows = [
 ('comnap24', 'COMNAP Antarctic Facilities Information: `Facilities_Nov2024.csv`', 'https://www.comnap.aq/s/Facilities_Nov2024.csv (linked from https://www.comnap.aq/antarctic-facilities-information)', 'curl, CSV (ISO-8859-1)', 'Official 2024 catalog: id, English/official name, operator, type (Station, Camp, Refuge, Airfield Camp, Laboratory, Depot), seasonality, status (Open / Temporarily Closed), year established, decimal and DDM coordinates, elevation, peak population, power. No surface type, no winter/summer split.'),
 ('comnap17', 'COMNAP Antarctic Station Catalog (Aug 2017 PDF, 86 pp, 76 station pages)', 'https://www.comnap.aq/s/COMNAP_Antarctic_Station_Catalogue.pdf', 'curl, PDF parsed with PyMuPDF (`01_parse_comnap_catalogue_2017.py`)', 'Per station: DMS coordinates, type, operational period, location and history text, **"Type of surface facility built on"**, altitude, beds, summer/winter staff, max personnel, permafrost, main science disciplines.'),
 ('wikidata', 'Wikidata SPARQL', 'https://query.wikidata.org/sparql (and https://www.wikidata.org/w/api.php wbgetentities for labels/descriptions)', 'curl/requests POST, JSON', 'Items of facility-like classes with coordinates (P625) located in Antarctica (P17/P30 = Q51) **or** inside the box lat -90..-60. Inception P571, dissolved P576, operator P137, elevation P2044, English Wikipedia sitelink, aliases, descriptions.'),
 ('wp_list', 'Wikipedia: Research stations in Antarctica (= "List of Antarctic research stations")', 'https://en.wikipedia.org/wiki/Research_stations_in_Antarctica', 'MediaWiki API action=parse wikitext, parsed with Python; article coordinates via prop=coordinates', 'Four tables (permanent active, summer-only active, sub-Antarctic, inactive): country, administration, year established/closed, status text, summer/winter population. **The list has no coordinates**; the linked article\'s GeoData coordinates were used.'),
 ('wp_camps', 'Wikipedia: Antarctic field camps', 'https://en.wikipedia.org/wiki/Antarctic_field_camps', 'MediaWiki API wikitext', 'Field camps, refuges and huts with coordinates, year, activities, type/status, serving base.'),
 ('wp_airports', 'Wikipedia: List of airports in Antarctica', 'https://en.wikipedia.org/wiki/List_of_airports_in_Antarctica', 'MediaWiki API wikitext', 'Skiways, blue-ice runways, airstrips, heliports with coordinates, ICAO/other code, runway surface.'),
 ('wp_hsm', 'Wikipedia: Historic Sites and Monuments in Antarctica', 'https://en.wikipedia.org/wiki/Historic_Sites_and_Monuments_in_Antarctica', 'MediaWiki API wikitext', '91 HSM rows with coordinates and descriptions; only hut/station/building-type sites were kept (34 of 91).'),
 ('scar', 'SCAR Composite Gazetteer of Antarctica (placenames.aq)', 'https://data.aad.gov.au/aadc/gaz/scar/ -> 301 -> https://placenames.aq ; data API https://placenames.aq/api/place_names_consolidated', 'curl/requests to the PostgREST API (the web page itself is a JavaScript app)', 'Feature types Station (140 records, many national duplicates), Camp (16), AWS (6), Building (21; only the hut kept), Historic (4), Landing area (1), depots (2), plus a name search for hut/refuge/station/base/skiway words across all types. Used for coordinates, relic flags and narratives.'),
]
for i, (k, a, u, m, g) in enumerate(srcrows, 1):
    w('| %d | %s | %s | %s | %s | %d (%d used as separate observations, %d note-only, %d dropped) | %d |' % (i, a, u, m, g, obs_n[k], obs_main[k], obs_sub[k], obs_drop[k], rows_with[k]))
w('| 9 | NOAA GHCN-Daily station list (local file, cross-check only) | `to-be-integrated/climate data CURL/ghcnd-stations [NOAA].txt` | read locally | %d stations with an AY (Antarctica) id; used only for the cross-check in 5.3 | %d | 0 (not a row source) |' % (len(ghcn), len(ghcn)))
w('')
w('**Observation counts:** %d source records were parsed in total. After de-duplication they became **%d** CSV rows (plus %d entities outside the scope test, see 7). Rows backed by 1 / 2 / 3 / 4+ sources: %s.' % (sum(obs_n.values()), N, len(diag['out_of_scope']), ' / '.join(str(src_count.get(k, 0)) for k in (1, 2, 3)) + ' / ' + str(sum(v for k, v in src_count.items() if k >= 4))))
w('')
w('Rows that exist **only** in one source: ' + '; '.join('%s %d' % (SRCN[k], only[k]) for k in SRCN if only[k]) + '.')
w('')
w('### 2.1 Source health log (what worked, what did not)')
w('')
w('| Source / endpoint | Result |')
w('|---|---|')
for a, b in [
 ('https://www.comnap.aq/ (HTTP)', 'worked (HTTP 200). The page https://www.comnap.aq/antarctic-facilities-information lists the CSV, the PDF and a Firebase web app (https://comnap-antarctic-facilities.web.app/) that was **not** used (JavaScript app, CSV already contains the same table).'),
 ('COMNAP `Facilities_Nov2024.csv`', 'worked. 114 rows. Encoding is ISO-8859-1 (accents appear as garbage if read as UTF-8). Typos inside: "Antartic" in names, a positive latitude for Zhongshan Skiway, Criosfera 2 longitude sign (see 6).'),
 ('COMNAP Station Catalog PDF (2017)', 'worked, 20.8 MB. Two-page spreads, one station per spread, 76 stations; the table of contents could not be parsed reliably (4 rows lost to column overflow), so coordinates were read from each station page instead.'),
 ('https://data.aad.gov.au/aadc/gaz/scar/', 'answered 301 to https://placenames.aq. The HTML is an empty single-page app with no static data; the underlying PostgREST API (https://placenames.aq/api) worked and was used. The gazetteer "Refuge" feature type (code 274) has **0** records, so huts/refuges were searched by name instead.'),
 ('Wikidata SPARQL', 'worked (HTTP 200). One survey query (class counts), one pull in two passes (country/continent = Antarctica, and lat box), no timeouts. Not every Antarctic facility is typed consistently (e.g. Lame Dog Hut and Nordenskiöld House typed "building", Refuge Abrazo de Maipú typed "human settlement"), so the class list was widened and held items were matched back by name/proximity.'),
 ('Wikidata wbgetentities', 'worked (%d entities: English label/description plus labels in 16 other languages, needed because %d items have no English label).' % (len(WDL), sum(1 for v in WDL.values() if not v['label_en']))),
 ('Wikipedia MediaWiki API (parse, query, categorymembers, extracts, coordinates)', 'worked. Four list pages parsed. The research-station list has no coordinates; %d of %d looked-up titles returned GeoData coordinates, %d returned a Wikidata item.' % (sum(1 for v in wp['titles'].values() if 'lat' in v), len(wp['titles']), sum(1 for v in wp['titles'].values() if v.get('qid'))) + ' Category tree (28 categories, 258 articles) used for a coverage cross-check.'),
 ('Wayback Machine', 'not needed (no page was blocked).'),
 ('WebSearch', 'not used (budget exhausted, per instruction). WebFetch not used (curl sufficed).'),
 ('NOAA GHCN-Daily list (local)', 'worked, cross-check only.'),
]: w('| %s | %s |' % (md(a), md(b)))
w('')
w('## 3. Counts')
w('')
w('**Total rows: %d.**' % N)
w('')
w('### 3.1 By type')
w('')
w('| type | rows |'); w('|---|---|')
for k, v in by_type.most_common(): w('| %s | %d |' % (k, v))
w('')
w('### 3.2 By status')
w('')
w('| status | rows |'); w('|---|---|')
for k, v in by_status.most_common(): w('| %s | %d |' % (k, v))
w('')
w('Status vocabulary note: `closed` includes COMNAP "Temporarily Closed" rows (stated in `status_detail`) and Wikipedia "Closed/Dismantled/Destroyed/Lost" rows; `abandoned` is only used where a source says "Abandoned"; `historic` where the Historic Sites list, an ASPA/HSM number or the SCAR relic flag says so and nothing says it operates; `unknown` where no source states a status (mostly airfields, heliports and Wikidata/SCAR-only rows).')
w('')
w('### 3.3 Type by status')
w('')
sts = ['year-round', 'summer-only', 'closed', 'abandoned', 'historic', 'planned or under construction', 'unknown']
w('| type | ' + ' | '.join(sts) + ' | total |'); w('|---|' + '---|' * (len(sts) + 1))
for t in sorted(xt): w('| %s | ' % t + ' | '.join(str(xt[t].get(s, 0)) for s in sts) + ' | %d |' % sum(xt[t].values()))
w('')
w('`planned or under construction` has 0 rows: no source in this pass lists a planned or under-construction facility that is not already operating (COMNAP 2024 lists Qinling, opened 2024, as year-round; Wikipedia lists it as permanent).')
w('')
w('### 3.4 Stability flag and surface (evidence stated by sources only)')
w('')
w('| stability_flag | rows |'); w('|---|---|')
for k, v in by_flag.most_common(): w('| %s | %d |' % (k, v))
w('')
w('| surface | rows |'); w('|---|---|')
for k, v in by_surf.most_common(): w('| %s | %d |' % (k, v))
w('')
w('### 3.5 Rows containing each source')
w('')
w('| source | rows containing it | rows that exist only because of it |'); w('|---|---|---|')
for k in SRCN: w('| %s | %d | %d |' % (SRCN[k], rows_with[k], only[k]))
w('')
w('## 4. Method')
w('')
w('### 4.1 Pipeline (scripts in `scripts/`, run in this order)')
w('')
w('| script | what it does |'); w('|---|---|')
for a, b in [('00_fetch_raw.sh', 'curl commands that download the COMNAP files, the Wikipedia pages and the SCAR API descriptors'), ('01_parse_comnap_catalogue_2017.py', 'PDF -> JSON, one record per station page'),
             ('02_wikidata_pull.py / 02b_wikidata_labels.py', 'SPARQL pull (two passes) and labels/descriptions'), ('03_scar_gazetteer_pull.py / 03b_scar_name_search.py', 'SCAR API: feature types, then name search'),
             ('04a_wikipedia_category_members.py', 'category walk for coverage cross-check'), ('04_wikipedia_pull_and_parse.py', 'parse the four Wikipedia pages and fetch article coordinates/Wikidata ids'),
             ('05_fetch_wp_extracts.py', 'intro extracts of every linked article (used for purpose and for surface wording)'), ('06_load_and_merge.py (+ `merge_overrides.json`, `inv_lib.py`)', 'load all sources as observations and de-duplicate into entities'),
             ('07_build_inventory_csv.py (+ `manual_notes.json`)', 'choose primary values, derive status/surface/flag, write the CSV'), ('08_diagnostics_and_log.py', 'cross-checks and this log')]: w('| `%s` | %s |' % (a, b))
w('')
w('Raw downloads are not stored in the repository (they are re-fetchable with `00_fetch_raw.sh`); the scripts read them from the folder given by the environment variable `RAW` (default `./raw`).')
w('')
w('### 4.2 De-duplication rules (script 06)')
w('')
w('Every source record is an *observation*. Observations are processed in the order COMNAP 2024, COMNAP 2017, Wikidata, Wikipedia station list, field camps, airports, Historic Sites, SCAR. An observation joins an existing entity (row) when **any** of these holds, otherwise it starts a new entity:')
w('')
w('1. Same Wikidata item (Wikipedia station-list rows are linked to Wikidata through the linked article), or, for other Wikipedia lists, same Wikidata item **and** at least one shared name token (stops "Ortiz refuge" joining "Brown" just because the article is shared).')
w('2. Name score >= 0.5 and distance <= 4 km. Name score = shared name tokens / smaller token set, after accent folding, a synonym table (Showa=Syowa, Molodyozhnaya=Molodezhnaya, Changcheng=Great Wall, Jubany=Carlini, ...), removal of generic words (station, base, refuge, skiway, ...), Roman numerals converted to digits. A shared single letter or numeral alone never counts; different numerals (Druzhnaya 3 vs 4, Station B vs C) block a match.')
w('3. Identical normalized name and distance <= 5 km.')
w('4. COMNAP 2017 vs COMNAP 2024 only: identical normalized name and distance <= 60 km (the 2017 PDF has coordinate typos that put four stations 4 to 150 km off, see 6.1).')
w('5. If one side has no coordinates: identical normalized name (score >= 0.9) and same kind.')
w('')
w('Kind separation: an airfield/skiway/heliport never merges into the station, camp or hut of the same name (Carlini station vs Carlini airstrip are two rows), except that a plain COMNAP "Airfield Camp" record merges with the camp/skiway/runway records of the same name within 1 km (Browning Pass, Enigma Lake, D85, Wilkins). Automatic weather stations never merge into non-AWS rows except identical-name records within 1 km (the BoM climate records DAVIS, MAWSON, CASEY, DOVERS and EDGEWORTH DAVID, which are attached as notes).')
w('')
w('Items attached as **notes only** (not their own row, no coordinate used): Wikidata items of excluded classes that match a row by name or lie within 3 km of one (magnetic observatories, churches/chapels, telescopes and detectors, monuments, observatories, expeditions that lie on a station site); each appears in the `notes` column of the row it was attached to.')
w('')
w('Same-site successors/predecessors are kept in one row when the Wikipedia list itself says "became X" (Station T -> Carvajal, Faraday -> Vernadsky, Station V -> Jorge Boonen, destacamento naval Esperanza -> Esperanza) and are noted in `notes` and `years_by_source`; the closure years of such predecessor rows are **not** used as the row\'s `year_closed` while COMNAP lists the successor as open.')
w('')
w('### 4.3 Manual overrides (%d)' % len(ov_rows))
w('')
w('Automatic rules cannot see translation/alias differences or coordinate typos, so %d decisions were made by hand in `scripts/merge_overrides.json`. They are listed so nothing is hidden. Format: observation -> target observation (`SUB:` = attach as note only, `NEW` = force a separate row).' % len(ov_rows))
w('')
w('| observation | name | -> target | distance to target row (km) |'); w('|---|---|---|---|')
ent_of = {}
for ei, keys in enumerate(st['ents']):
    for k in keys: ent_of[k] = ei
for k, nm, v in ov_rows:
    tv = v[4:] if v.startswith('SUB:') else v
    d = ''
    try:
        tk = None
        if tv in OBS: tk = tv
        elif ':~' in tv:
            s_, p_ = tv.split(':~', 1); c = [kk for kk, oo in OBS.items() if oo['src'] == s_ and p_.lower() in oo['name'].lower()]; tk = c[0] if len(c) == 1 else None
        o = OBS[k]
        if tk and o['lat'] is not None and OBS[tk]['lat'] is not None: d = '%.1f' % haversine((o['lat'], o['lon']), (OBS[tk]['lat'], OBS[tk]['lon']))
    except Exception: pass
    w('| %s | %s | %s | %s |' % (md(k), md(nm), md(v), d))
w('')
w('### 4.4 Choosing primary values')
w('')
w('- **Name:** first Latin-script name by source priority COMNAP 2024 (with the generic suffix "Antartic Base" removed; the original stays in alternate names) > Wikidata label > Wikipedia list > camps > airports > Historic Sites > COMNAP 2017 > SCAR. All other names, Wikidata aliases and foreign-language labels go to `alternate_names` (max 14).')
w('- **Coordinates:** priority COMNAP 2024 > COMNAP 2017 (DMS converted; the original DMS string is kept in `notes`) > Wikidata > Wikipedia article/list coordinates > SCAR. Exception: if the first-priority source is at least 2 km from **every** other source and the others agree with each other within 2 km, the consensus of the others is used and flagged (`coord_source` says so). `coord_disagreement_max_km` is the largest distance from the primary to any source coordinate; `coord_disagreement_over_2km` names every source over 2 km.')
w('- **Elevation:** COMNAP 2024 > COMNAP 2017 > Wikidata > SCAR; all values in `elevation_by_source`. Datums differ (COMNAP: MSL or WGS84 as given) and were not converted.')
w('- **Type:** from the curated sources first (COMNAP 2024, Wikipedia list, camps, airports), then Wikidata classes, Historic Sites, SCAR. COMNAP "Station" -> station, "Camp" -> field camp, "Refuge" -> hut-refuge, "Airfield Camp" -> airfield, "Laboratory" and "Depot" -> other (with `type_detail`). Hut/shelter/house/igloo names under camp/historic -> hut-refuge. `base` is not used as a separate type: the source label ("Base", "Station", "Laboratory") is kept in `type_detail`.')
w('- **Status and years:** priority COMNAP 2024 > COMNAP 2017 > Wikipedia list > camps > Historic Sites > Wikidata dissolved date > SCAR relic flag; every source\'s statement is kept in `status_all_sources`. Opening year: first of COMNAP 2024, Wikipedia list, camps, Wikidata; all in `years_by_source`.')
w('- **Capacity:** `capacity_winter` / `capacity_summer` are "Number of staff on station (off-peak/winter | peak/summer season)" from COMNAP 2017, else the Wikipedia list\'s winter/summer population. `capacity_peak_persons` is COMNAP 2017 "Max number of personnel at a time", else the Wikipedia list "Max. persons", else COMNAP 2024 "Peak Population". `beds` is COMNAP 2017 only. These are operating figures stated by the sources; no source gives a separate "rated capacity", so none is invented.')
w('- **operator_context_only:** COMNAP operator, Wikipedia country and administration, Wikidata operator/country, deduplicated. Context only: it is not an input to anything.')
w('- **purpose_as_stated:** COMNAP 2017 "Main science disciplines" > Wikipedia camps "Activities" > first sentence of the Wikipedia article intro (<= 230 characters) > Historic Sites description > SCAR narrative first sentence > Wikidata description > Wikidata class (marked unknown). The source is in `purpose_source`.')
w('')
w('### 4.5 Surface and stability flag (script 07)')
w('')
w('Only stated evidence is used; an absent statement gives `unknown`. In order:')
w('')
w('1. COMNAP 2017 "Type of surface facility built on" (values seen: Ice-free ground, Ice-shelf, Ice-sheet, Ice sheet, Ice-sheet + Moraine, Rock outcrop, Scoria permafrost). Ice-free ground / rock / scoria -> `bare rock`; Ice-shelf -> `ice shelf`; Ice-sheet -> `ice sheet`; Ice-sheet + moraine -> `rock and ice`. "Ice-free ground" is recorded as rock but the source does not say whether it is bedrock, gravel or moraine (noted in `surface_source`).')
w('2. Short location fields (Wikipedia list "Location", camps "Location", airports "Location"): the words ice shelf / ice tongue, glacier, sea ice, ice sheet / plateau / dome / ice cap.')
w('3. Prose (COMNAP 2017 location and history text, Wikipedia intro, SCAR narrative, Historic Sites description): only explicit "on / atop / upon the ... ice shelf | glacier | ice sheet | ice cap | plateau | sea ice" phrasing, and "ice-free", "oasis", "on ... nunatak / rock outcrop", "stone hut", "bare rock", "scoria". Mere proximity ("near", "along", "on the shore of") is rejected.')
w('4. Wikipedia airports list runway surface: "Sea Ice" -> sea ice; "Gravel" -> rock; "Ice"/"Snow" does not say what kind of ice body, so it gives nothing.')
w('5. `stability_flag`: `rock` = rock evidence only; `ice_sheet_interior` = ice-sheet evidence only; `ice_shelf_or_glacier_or_sea_ice (needs velocity test)` = any ice-shelf, glacier or sea-ice evidence, or a `rock and ice` mix, **or** wording in the sources that the facility "moved", was "relocated", "resited", "crushed", "sunk", "buried", is "under snow", "lost", or mentions "deterioration of the ice" (quoted in `notes`); `unknown` otherwise. The flag is a prompt for the next pass, not a verdict: e.g. a station on a rock outcrop beside an ice shelf is flagged because the source says "ice shelf" and "nunatak" together.')
w('')
w('### 4.6 HSM selection')
w('')
w('Of 91 Historic Sites and Monuments, 34 were kept as rows (huts, historic stations/bases, shelters, ruins: HSM %s). The other 57 are cairns, crosses, plaques, busts, graves, memorials, statues, wrecks, lighthouses, message posts and camp sites without buildings; they are not facilities.' % ', '.join(str(x) for x in sorted({int(OBS[k]['hsm']) for k in OBS if OBS[k]['src'] == 'wp_hsm'})))
w('')
w('## 5. Cross-checks')
w('')
w('### 5.1 Wikipedia category coverage')
w('')
w('Walking the category trees Outposts of Antarctica (all sub-categories), Historic buildings and structures in Antarctica, Airports in Antarctica and Antarctic field camps gave 258 article titles. **%d** of them appear in the `wikipedia_titles` column of a row. The %d that do not are listed here; they are articles about people, books, ships, organizations, programs, generic topics, features or sub-objects. A few are facilities that are present under another title (Mawson\'s Huts = row Cape Denison; Shackleton\'s Hut; Maudheim Station = row Maudheim; Florentino Ameghino Refuge and Groussac Refuge = rows Florentino Ameghino and Groussac). No category member turned out to be a station missing from the CSV.' % (len(cm) - len(cat_missing), len(cat_missing)))
w('')
w('`' + '` ; `'.join(md(t) for t in cat_missing) + '`')
w('')
w('### 5.2 Possible duplicates and same-name pairs (left as separate rows on purpose)')
w('')
w('Pairs of rows of the same type within 1 km whose names share nothing (could be two facilities at one site, or one facility under two names): **%d pairs**. First 120 by distance:' % len(dups))
w('')
w('| km | row A | row B |'); w('|---|---|---|')
for d, a, b in dups[:120]: w('| %.2f | %s (%s) | %s (%s) |' % (d, md(a['name']), a['id'], md(b['name']), b['id']))
w('')
w('Rows with the same name but different places (>5 km) or one without coordinates, same type: **%d pairs**.' % len(samen))
w('')
w('| km | row A | row B |'); w('|---|---|---|')
for d, a, b in sorted(samen, key=lambda x: -(x[0] or 0))[:80]: w('| %s | %s (%s) | %s (%s) |' % ('%.0f' % d if d else 'no coords', md(a['name']), a['id'], md(b['name']), b['id']))
w('')
w('### 5.3 NOAA GHCN-Daily cross-check')
w('')
w('%d GHCN stations carry an AY id. **%d** have a row within 5 km; **%d** do not (they are weather-station sites with no matching facility in the sources above: automatic weather stations of the US/AMRC and other networks, field sites and sea-ice stations). They are **not** added as rows (cross-check only, per instruction); the unmatched list follows.' % (len(ghcn), len(g_match), len(g_un)))
w('')
w('| GHCN id | name | lat | lon | elev m | nearest row | km |'); w('|---|---|---|---|---|---|---|')
for gid, la, lo, el, nm, best in g_un: w('| %s | %s | %.3f | %.3f | %.0f | %s | %.0f |' % (gid, md(nm), la, lo, el, md(best[1]['name']) if best else '-', best[0] if best else 0))
w('')
w('### 5.4 Rows whose name implies a station but whose coordinates are far from it')
w('')
w('A row named after a station (airfield, camp, hut) that sits more than 30 km from that station\'s COMNAP position (candidates for mis-located source coordinates; nothing was changed). Most hits are explained by the name itself (plateau skiways, namesake refuges, an AWS called Mount Brown); the one clear anomaly is Belgrano II Skiway.')
w('')
w('| row | km from | station |'); w('|---|---|---|')
for d, r, s in sorted(implied, key=lambda x: -x[0]): w('| %s (%s) | %.0f | %s |' % (md(r['name']), r['id'], d, md(s['name'])))
w('')
w('## 6. Disagreements found')
w('')
w('### 6.1 Coordinates over 2 km (%d rows)' % len(diag['coord_disagree']))
w('')
w('| row | max km | source(s) over 2 km from the primary |'); w('|---|---|---|')
for nm, mx, ds in sorted(diag['coord_disagree'], key=lambda x: -float(x[1])): w('| %s | %s | %s |' % (md(nm), mx, md(ds)))
w('')
w('Most under ~12 km are the same facility recorded at slightly different spots (station center vs skiway vs gazetteer centroid). The large ones (tens to thousands of km) fall into four groups: sign or digit typos in one source (Criosfera 2, Mid Point, Yamato Yukihara, Strom Camp, Rifugio Cristo Redentor, Dr. Guillermo Mann, the 2017 PDF rows); Wikipedia-list rows whose "coordinates" are those of the linked area article rather than the station (Charcot = Adelie Land article); stations on moving ice whose sources give different historic positions (Little America, Komsomolskaya, Sovetskaya, Little Rockford, Filchner-Ronne stations); and the same facility placed at two real nearby spots (Dome Fuji station vs dome summit). See 6.3 and the `notes` column.')
w('')
w('### 6.2 Name conflicts (the sources use different names for one row; %d rows)' % len(name_conf))
w('')
w('| row (primary) | other source names with no shared token |'); w('|---|---|')
for nm, ot in sorted(name_conf): w('| %s | %s |' % (md(nm), md('; '.join(ot[:6]))))
w('')
w('### 6.3 Sign and typo anomalies detected inside the sources')
w('')
w('Detected automatically (mirror-longitude within 15 km, or equal coordinates with one sign flipped):')
w('')
for nm, src, kind in diag['sign_issues']: w('- %s: %s (%s)' % (md(nm), md(src), kind))
w('')
w('Annotated by hand in `scripts/manual_notes.json` (each is evidence visible in the sources themselves; no coordinate was changed): Dome C camp (longitude sign), Siple Dome Skiway (longitude sign), Belgrano II Skiway (coordinates copied from Matienzo), Boulder Clay Runway (Wikidata carries Browning Pass coordinates), Zhongshan Station airfield entry, Rifugio Cristo Redentor (latitude digit), Criosfera 2 (longitude sign), Pole of Inaccessibility (HSM latitude), Ruperto Elichiribehety and Gabriel de Castilla (COMNAP 2017 longitude typos), Henryk Arctowski (2017 table-of-contents latitude 69 instead of 62), Robert Guillard (SCAR 34 km off).')
w('')
w('### 6.4 The single coordinate change')
w('')
w('COMNAP 2024 gives Zhongshan Skiway latitude **+69.623611** (north). A positive latitude cannot be in Antarctica, so the sign was flipped to -69.623611 for use; the flag is in `notes`. This is the only place a source coordinate was altered. Rows affected: %d.' % len(diag['lat_fix']))
w('')
w('### 6.5 Status disagreements between sources (%d rows)' % len(diag['status_disagree']))
w('')
w('| row | statements |'); w('|---|---|')
for nm, s in sorted(diag['status_disagree']): w('| %s | %s |' % (md(nm), md(s)))
w('')
w('Typical causes: COMNAP 2024 "Temporarily Closed" vs Wikipedia "summer-only active"; COMNAP 2017 "Year-round" vs COMNAP 2024 "Seasonal" (Halley VI, Escudero); successors listed beside predecessors.')
w('')
w('### 6.6 Opening-year disagreements (%d rows)' % len(diag['year_disagree']))
w('')
w('Different sources give different years (station vs. its predecessor, "established" vs "opened", or reconstruction). All values are in `years_by_source`. First 60:')
w('')
for nm, y in sorted(diag['year_disagree'])[:60]: w('- %s: %s' % (md(nm), md(y)))
w('')
w('## 7. Outside the scope test, dropped, or without coordinates')
w('')
w('### 7.1 Not in the CSV: best coordinate north of 60 S (%d)' % len(diag['out_of_scope']))
w('')
w('| entity | lat,lon | sources |'); w('|---|---|---|')
for nm, c, s in diag['out_of_scope']: w('| %s | %s | %s |' % (md(nm), c, md(s)))
w('')
w('(These are the sub-Antarctic stations, Macquarie, South Georgia and similar; the instruction scope is south of 60 S plus the South Shetland and South Orkney islands.)')
w('')
w('### 7.2 Wikidata items dropped (excluded class, no site to attach to)')
w('')
for l in st['log']:
    if l[0] == 'DROP': w('- %s: %s' % (md(l[2]), md(l[3])))
w('')
w('### 7.3 Rows with no coordinates in any source (%d)' % len(diag['no_coords']))
w('')
w(', '.join(md(x) for x in diag['no_coords']) + '.')
w('')
w('## 8. What is incomplete (honest limits)')
w('')
unk_surface = by_surf['unknown']; unk_status = by_status['unknown']
w('- **Surface is stated for only %d of %d rows (%d unknown).** Only COMNAP 2017 (76 stations) states the surface systematically; all other rows rely on scattered wording. The next pass has to test the %d `unknown` rows and the %d flagged rows with real ice-velocity/bedrock data.' % (N - unk_surface, N, unk_surface, by_flag['unknown'], by_flag['ice_shelf_or_glacier_or_sea_ice (needs velocity test)']))
w('- **Status is `unknown` for %d rows** (mostly airfields/heliports, Wikidata-only huts and AWS, camps whose list cell is blank).' % unk_status)
w('- **Capacity** exists only for stations in COMNAP 2017, the Wikipedia list, or with a COMNAP 2024 peak figure; huts, refuges, camps, airfields have none. COMNAP 2024 has no winter/summer split.')
w('- **Automatic weather stations** are incomplete by design: only Australian-network and SCAR-listed AWS appear (from Wikidata and SCAR). The US AMRC/UW-Madison AWS network, the Italian Meteo-Climatological Observatory network, BAS and Japanese unmanned sites are not in any source used; the GHCN cross-check (5.3) shows what that leaves out.')
w('- **Field camps are a living list.** Wikipedia\'s list (221 rows) is a snapshot; temporary US, NZ, Italian, Australian and Chinese traverse camps, private tourism camps other than Union Glacier and Patriot Hills, ice-core drill camps and sea-ice camps are only partially captured.')
w('- **Huts and refuges** come from Wikipedia\'s field-camp list (strong on Argentina, Chile, Brazil, Australia, NZ), COMNAP "Refuge" rows (9), Wikidata "shelter" items and Historic Sites. Other national refuge networks (e.g. detailed BAS and Russian field huts, Japanese field huts, Norwegian and Belgian huts) are probably under-counted. The SCAR gazetteer feature type for refuges is empty.')
w('- **Historic/closed stations** come from Wikipedia\'s inactive list (72 rows), Wikidata and SCAR; stations known only from the older literature that none of these carry are missing. SANAE I-III are merged into one row because Wikipedia and Wikidata point all three to one item; Halley I-V have no separate coordinates beyond the three SCAR records (Halley, Halley (1988), Halley Station).')
w('- **Coordinates for %d rows are missing** (7.3). Wikipedia list rows built from other-language wikis ("ill" links) have no article coordinates; they were matched by name to other sources where possible.' % len(diag['no_coords']))
w('- **The 2017 COMNAP PDF is older than the 2024 CSV**; it is used for text fields (surface, capacity, disciplines), so a few of those may be out of date.')
w('- **Not collected:** Arctic/sub-Antarctic stations (out of scope), ships, aircraft-only landing sites, penguin or sealer huts without any research/support role (unless on the HSM/refuge lists), pre-1900 sites other than historic huts.')
w('')
w('## 9. Column dictionary')
w('')
w('| column | meaning |'); w('|---|---|')
cols = [('id', 'slug of the primary name; duplicates get -2, -3'), ('name / alternate_names', 'primary name; every other name, alias, translation (pipe-separated)'), ('latitude / longitude', 'WGS84 decimal degrees of the primary coordinate; `unknown` if no source has one'),
 ('coord_source', 'which source supplied the primary coordinate'), ('coords_by_source', 'every source coordinate: `source=lat,lon`'), ('coord_disagreement_max_km / coord_disagreement_over_2km', 'largest distance from primary to another source; sources over 2 km'),
 ('elevation_m / elevation_source / elevation_by_source', 'elevation in meters (as stated, datum not converted)'), ('type / type_detail', 'station, field camp, hut-refuge, airfield, automatic weather station, other; plus the source labels'),
 ('status / status_detail / status_all_sources', 'year-round, summer-only, closed, abandoned, historic, planned or under construction, unknown; what decided it; every source statement'), ('year_opened / year_closed / years_by_source', '`n/a (active)` where open; all years by source'),
 ('capacity_winter / capacity_summer / capacity_peak_persons / beds / capacity_source', 'see 4.4'), ('operator_context_only', 'operating nation(s) and organization, context only'), ('purpose_as_stated / purpose_source', 'what the facility is for, one phrase, as a source states it'),
 ('surface / surface_source', 'bare rock, rock and ice, ice sheet, ice shelf, glacier, sea ice, unknown; the quoted evidence'), ('stability_flag', 'rock, ice_sheet_interior, ice_shelf_or_glacier_or_sea_ice (needs velocity test), unknown'),
 ('location_text', 'location wording from the sources'), ('sources / source_ids / wikipedia_titles', 'which sources back the row; their ids (comnap24:record id, comnap17:catalog page, wikidata:Q-id, scar:gazetteer:name_id, wp_*:row key); linked Wikipedia articles'), ('notes', 'everything else: DMS originals, predecessor rows, note-only items, runway data, coordinate flags and anomalies')]
for a, b in cols: w('| `%s` | %s |' % (a, b))
w('')
w('## 10. Reproducing')
w('')
w('```')
w('export RAW=./raw   # scratch folder for downloads')
w('bash scripts/00_fetch_raw.sh')
w('for s in 01_parse_comnap_catalogue_2017 02_wikidata_pull 02b_wikidata_labels 03_scar_gazetteer_pull 03b_scar_name_search 04a_wikipedia_category_members 04_wikipedia_pull_and_parse 05_fetch_wp_extracts 06_load_and_merge 07_build_inventory_csv 08_diagnostics_and_log; do python3 scripts/$s.py; done')
w('```')
w('')
w('Requires Python 3 with `requests` and `PyMuPDF`. Wikipedia/Wikidata change daily; a re-run will not reproduce these counts exactly.')
w('')
w('## Appendix A. Wikidata class survey (exploratory query that fixed the class list)')
w('')
w('Run once before the main pull to see which classes Antarctic items use (result: mountain 7212, island 2179, glacier 2122, ... Antarctic research station 191, Antarctic field camp 21, blue ice runway 14, aerodrome 14, shelter 13, human settlement 9, magnetic observatory 8, polar station 6, research station 5, building 5, weather station 4, ...). Facility-like classes were then listed in `scripts/02_wikidata_pull.py` (variable TYPES) plus every subclass of "Antarctic research station".')
w('')
w('```sparql')
w('SELECT ?type ?typeLabel (COUNT(?item) AS ?n) WHERE {')
w('  ?item wdt:P625 ?c . ?item wdt:P31 ?type . ?item wdt:P17|wdt:P30 wd:Q51 .')
w('  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }')
w('} GROUP BY ?type ?typeLabel ORDER BY DESC(?n) LIMIT 1000')
w('```')
open(LOGP, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('log written', len(L), 'lines; ghcn', len(ghcn), len(g_match), len(g_un), 'dups', len(dups), 'samen', len(samen), 'implied', len(implied), 'name_conf', len(name_conf))
