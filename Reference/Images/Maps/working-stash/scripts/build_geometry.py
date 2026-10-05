"""Build data/highway_geometry.csv (every highway line, spur and junction as lat/lon vertices).

Inputs : data/highways_traced.csv  (raw trace of the developer's sketch, see extract_highways_from_sketch.py)
         data/highways.csv         (which cities each highway serves, spurs, ramps)
         data/cities.csv           (real GPS)
Output : data/highway_geometry.csv  columns: line_id, kind(main|spur|boat), highway_id, seq, lat, lon
         data/junctions.csv        id, name, lat, lon

Rules: a main-line stop whose city lies within STOP_TOL of the traced line is spliced in at its exact GPS; the trace is
oriented so stops run in the listed order; ramps (snap_start/snap_end) end exactly on the neighboring highway; spurs run
straight from the nearest point of the parent line to the city. Hand-refine data/highway_geometry.csv if a shape is wrong,
then do NOT re-run this script without --rebuild (it refuses to overwrite).
"""
import csv, sys
from pathlib import Path
import numpy as np
from pyproj import Transformer

HERE = Path(__file__).resolve().parent.parent
D = HERE / 'data'
T = Transformer.from_crs('EPSG:4326', '+proj=stere +lat_0=-90 +lat_ts=-71 +lon_0=0 +datum=WGS84 +units=m', always_xy=True)
Ti = Transformer.from_crs('+proj=stere +lat_0=-90 +lat_ts=-71 +lon_0=0 +datum=WGS84 +units=m', 'EPSG:4326', always_xy=True)
STOP_TOL = 300_000.0    # m: farther than this and a stop is NOT spliced into the line (it would need a spur)
SKIP_TOL = 15_000.0     # m: closer than this and the line already passes through


def xy(lat, lon): return np.array(T.transform(lon, lat))
def ll(p): lon, lat = Ti.transform(p[0], p[1]); return (lat, lon)


def nearest_on_poly(poly, p):
    """-> (distance, segment index i, point q on segment i..i+1)"""
    best = (1e18, 0, poly[0])
    for i in range(len(poly) - 1):
        a, b = poly[i], poly[i + 1]; ab = b - a; L2 = float(ab @ ab)
        t = 0.0 if L2 == 0 else max(0.0, min(1.0, float((p - a) @ ab) / L2))
        q = a + t * ab; d = float(np.hypot(*(p - q)))
        if d < best[0]: best = (d, i, q)
    return best


def arclen_to(poly, i, q):
    s = sum(float(np.hypot(*(poly[k + 1] - poly[k]))) for k in range(i)); return s + float(np.hypot(*(q - poly[i])))


def main():
    out = D / 'highway_geometry.csv'
    if out.exists() and '--rebuild' not in sys.argv:
        sys.exit(f'{out.name} exists; hand edits would be lost. Re-run with --rebuild to overwrite.')
    cities = {r['id']: xy(float(r['lat']), float(r['lon'])) for r in csv.DictReader(open(D / 'cities.csv', encoding='utf8'))}
    traced = {}
    for r in csv.DictReader(open(D / 'highways_traced.csv')):
        traced.setdefault(r['route_id'], []).append(xy(float(r['lat']), float(r['lon'])))
    specs = list(csv.DictReader(open(D / 'highways.csv', encoding='utf8')))

    # --- Temirötkel Junction: the point where the traced ends of Hwy 4, Hwy 7-ext and Hwy 37 converge
    ends = [traced['hwy7ext'][0], traced['hwy7ext'][-1], traced['hwy4'][0], traced['hwy4'][-1], traced['hwy37'][0], traced['hwy37'][-1]]
    sayowa = cities['temirotkel']
    cand = sorted(ends, key=lambda p: np.hypot(*(p - sayowa)))[:3]
    cities['temirotkel_junction'] = np.mean(cand, axis=0)

    lines = {}   # id -> polyline (list of xy)
    for s in specs:
        poly = [p.copy() for p in traced[s['trace_id']]]
        stops = [x for x in s['main_stops'].split(';') if x]
        # orient so the stops run in the listed order
        if len(stops) >= 2:
            ts = []
            for c in stops:
                d, i, q = nearest_on_poly(poly, cities[c]); ts.append(arclen_to(poly, i, q))
            if ts[0] > ts[-1]: poly = poly[::-1]
        # splice stops
        for c in stops:
            d, i, q = nearest_on_poly(poly, cities[c])
            if d <= SKIP_TOL:
                continue
            if d <= STOP_TOL:
                poly.insert(i + 1, cities[c].copy())
            else:
                print(f'  ! {s["id"]}: stop {c} is {d/1000:.0f} km from the traced line; NOT spliced', file=sys.stderr)
        # end the line exactly at the first/last stop. Where the sketch's end sits well away from the real site (the sketch's
        # Prydz Bay junction and Byrd are 150-420 km off), drop the trace vertices near the real site so the line approaches it
        # directly instead of overshooting and doubling back.
        if stops:
            for end, c in ((0, stops[0]), (-1, stops[-1])):
                tgt = cities[c]
                if np.hypot(*(poly[end] - tgt)) < 90_000:
                    poly[end] = tgt.copy()
                else:
                    rad = 600_000 if c in ('zhongshan', 'sinheung') else 450_000
                    stop_pts = [tuple(cities[x]) for x in stops]
                    while len(poly) > 2 and np.hypot(*(poly[end] - tgt)) < rad and tuple(poly[end]) not in stop_pts:
                        poly.pop(0 if end == 0 else -1)
                    if end == 0: poly.insert(0, tgt.copy())
                    else: poly.append(tgt.copy())
        lines[s['id']] = poly

    # --- ramps: connectors end exactly on the neighboring highway
    for s in specs:
        poly = lines[s['id']]
        if s['snap_start'] and s['snap_end']:       # connectors: orient so the start touches snap_start's highway
            ds = nearest_on_poly(lines[s['snap_start']], poly[0])[0] + nearest_on_poly(lines[s['snap_end']], poly[-1])[0]
            dr = nearest_on_poly(lines[s['snap_start']], poly[-1])[0] + nearest_on_poly(lines[s['snap_end']], poly[0])[0]
            if dr < ds: poly.reverse()
        if s['snap_start']:
            d, i, q = nearest_on_poly(lines[s['snap_start']], poly[0]); poly[0] = q
        if s['snap_end']:
            d, i, q = nearest_on_poly(lines[s['snap_end']], poly[-1]); poly[-1] = q
    # Hwy 2 starts on Hwy 110 (west of Casey); Hwy 22/110/4 meet at the Tri-Cities
    # --- spurs
    spurs = []   # (line_id, kind, parent, [pts])
    for s in specs:
        for sp in [x for x in s['spurs'].split(';') if x]:
            city, parent, style = sp.split(':')
            if parent.startswith('@'):
                a = cities[parent[1:]]; spurs.append((f'spur_{city}', 'spur', s['id'], [a, cities[city]]))
            else:
                d, i, q = nearest_on_poly(lines[parent], cities[city])
                spurs.append((f'spur_{city}', 'boat' if style == 'boat' else ('spur_dashed' if style == 'dashed' else 'spur'), parent, [q, cities[city]]))
    # Temirötkel Spur
    spurs.append(('spur_temirotkel', 'spur', 'hwy4', [cities['temirotkel_junction'], cities['temirotkel']]))

    with open(out, 'w', newline='', encoding='utf8') as f:
        w = csv.writer(f); w.writerow(['line_id', 'kind', 'highway_id', 'seq', 'lat', 'lon'])
        for s in specs:
            for k, p in enumerate(lines[s['id']]):
                la, lo = ll(p); w.writerow([s['id'], 'main', s['id'], k, f'{la:.4f}', f'{lo:.4f}'])
        for lid, kind, parent, pts in spurs:
            for k, p in enumerate(pts):
                la, lo = ll(p); w.writerow([lid, kind, parent, k, f'{la:.4f}', f'{lo:.4f}'])
    la, lo = ll(cities['temirotkel_junction'])
    with open(D / 'junctions.csv', 'w', newline='', encoding='utf8') as f:
        w = csv.writer(f); w.writerow(['id', 'name', 'lat', 'lon', 'note'])
        w.writerow(['temirotkel_junction', 'The Temirötkel Junction', f'{la:.4f}', f'{lo:.4f}', 'Hwy 4 / Hwy 7-ext / Hwy 37; near, not in, Temirötkel (Highways.md L68)'])
    print('wrote', out.name, 'and junctions.csv')


if __name__ == '__main__':
    main()
