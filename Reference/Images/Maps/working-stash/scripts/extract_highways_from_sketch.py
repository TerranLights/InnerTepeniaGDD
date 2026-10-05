"""One-time extraction: trace the developer's hand-drawn highway overlay into geo-referenced polylines.

Input : ../Antarctica_highway_map_by_topology.jpeg  (developer's hand-colored sketch on a real-station base map)
Method: 1) polar-stereographic calibration of the sketch against 17 real station dots (least squares, ~6 px RMS ~ 20 km)
        2) per-highway color mask (legend swatch colors) -> centerline via distance-weighted shortest path between the
           mask's two most distant points (dilated to bridge dashes / crossings)
        3) pixel -> lat/lon, simplified to ~40 km vertices
Output: data/highways_traced.csv  (route_id, seq, lat, lon)   -- a RAW trace, refined by hand into data/highway_routes.csv
This is the provenance of the route SHAPES only; which cities each highway serves comes from Locations/Infrastructure/Highways.md.
"""
import heapq, sys
from pathlib import Path
import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent.parent
SRC = HERE.parent / 'Antarctica_highway_map_by_topology.jpeg'
CX, CY, A, B = 945.861, 1268.971, 3663.167, 37.832     # fitted: x = CX + r*(A sin l + B cos l); y = CY - r*(A cos l - B sin l)
rho = lambda lat: np.tan(np.radians((90 + lat) / 2))

def to_px(lat, lon):
    r = rho(lat); l = np.radians(lon)
    return CX + r * (A * np.sin(l) + B * np.cos(l)), CY - r * (A * np.cos(l) - B * np.sin(l))

def to_geo(x, y):
    # invert: solve for (r sin l, r cos l)
    dx, dy = x - CX, CY - y
    M = np.array([[A, B], [-A, B]]) if False else None
    # dx = r(A sin + B cos), dy = r(A cos - B sin)  -> with u=r sin l, v=r cos l: dx = A u + B v ; dy = A v - B u
    det = A * A + B * B
    u = (A * dx - B * dy) / det
    v = (B * dx + A * dy) / det
    r = np.hypot(u, v); lon = np.degrees(np.arctan2(u, v))
    lat = 2 * np.degrees(np.arctan(r)) - 90
    return lat, lon

COLORS = {'hwy1': (100, 88, 226), 'hwy7': (197, 120, 42), 'hwy7ext': (251, 93, 34), 'hwy59': (36, 198, 247),
          'hwy175': (107, 245, 209), 'hwy22': (172, 67, 230), 'hwy4': (239, 30, 132), 'hwy110': (12, 181, 18),
          'hwy183': (164, 85, 26), 'hwy2': (210, 185, 30), 'hwy37': (114, 102, 30)}
DILATE = {'hwy7ext': 3, 'hwy37': 5, 'hwy22': 3, 'hwy175': 3}   # extra bridging where another highway is drawn over this one
Y_SPLIT = {'hwy7': (0, 1250), 'hwy183': (1250, 99999)}   # hwy7 and hwy183 share one color: split by image row

def trace(name, im, step=3):
    col = np.array(COLORS[name])
    d = np.sqrt(((im - col) ** 2).sum(-1))
    m = d < 38
    m[:565] = False                                       # legend area
    lo, hi = Y_SPLIT.get(name, (0, 99999)); m[:lo] = False; m[hi:] = False
    H, W = m.shape; h, w = H // step, W // step
    g = m[:h * step, :w * step].reshape(h, step, w, step).any(axis=(1, 3))
    # dilate to bridge dashes
    for _ in range(DILATE.get(name, 2)):
        p = np.pad(g, 1); g = g | p[:-2, 1:-1] | p[2:, 1:-1] | p[1:-1, :-2] | p[1:-1, 2:]
    # keep largest component
    seen = np.zeros_like(g); best = []
    for y, x in zip(*np.nonzero(g)):
        if seen[y, x]: continue
        st = [(y, x)]; seen[y, x] = True; comp = []
        while st:
            cy, cx = st.pop(); comp.append((cy, cx))
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    yy, xx = cy + dy, cx + dx
                    if 0 <= yy < h and 0 <= xx < w and g[yy, xx] and not seen[yy, xx]:
                        seen[yy, xx] = True; st.append((yy, xx))
        if len(comp) > len(best): best = comp
    G = np.zeros_like(g); 
    for y, x in best: G[y, x] = True
    # centerline weight: erosion depth
    depth = G.astype(int); cur = G.copy()
    for _ in range(12):
        p = np.pad(cur, 1, constant_values=False)
        cur = cur & p[:-2, 1:-1] & p[2:, 1:-1] & p[1:-1, :-2] & p[1:-1, 2:]
        if not cur.any(): break
        depth += cur
    mx = depth.max()
    cost = np.where(G, (mx - depth + 1.0) ** 2, np.inf)
    nodes = best
    def bfs(src):
        dist = {src: 0}; q = [src]; i = 0
        while i < len(q):
            c = q[i]; i += 1
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    n = (c[0] + dy, c[1] + dx)
                    if n in dist or not (0 <= n[0] < h and 0 <= n[1] < w) or not G[n]: continue
                    dist[n] = dist[c] + 1; q.append(n)
        return q[-1]
    a = bfs(nodes[0]); b = bfs(a)
    def dijkstra(s, t):
        D = {s: 0.0}; prev = {}; pq = [(0.0, s)]
        while pq:
            dd, c = heapq.heappop(pq)
            if c == t: break
            if dd > D.get(c, 1e18): continue
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dy == 0 and dx == 0: continue
                    n = (c[0] + dy, c[1] + dx)
                    if not (0 <= n[0] < h and 0 <= n[1] < w) or not G[n]: continue
                    nd = dd + cost[n] * (1.414 if dy and dx else 1.0)
                    if nd < D.get(n, 1e18): D[n] = nd; prev[n] = c; heapq.heappush(pq, (nd, n))
        path = [t]
        while path[-1] != s: path.append(prev[path[-1]])
        return path[::-1]
    path = dijkstra(a, b)
    pts = [((x + 0.5) * step, (y + 0.5) * step) for y, x in path]
    return pts

def simplify(pts, tol):
    pts = np.array(pts)
    def rec(i, j):
        if j <= i + 1: return [i]
        p, q = pts[i], pts[j]; seg = q - p; L = np.hypot(*seg) or 1
        dd = np.abs(seg[0] * (pts[i + 1:j, 1] - p[1]) - seg[1] * (pts[i + 1:j, 0] - p[0])) / L
        k = dd.argmax()
        return rec(i, i + 1 + k) + rec(i + 1 + k, j) if dd[k] > tol else [i]
    idx = rec(0, len(pts) - 1) + [len(pts) - 1]
    return pts[idx]

if __name__ == '__main__':
    im = np.array(Image.open(SRC).convert('RGB')).astype(int)
    out = HERE / 'data' / 'highways_traced.csv'
    with open(out, 'w') as f:
        f.write('route_id,seq,lat,lon\n')
        for name in COLORS:
            pts = simplify(trace(name, im), tol=7)
            for i, (x, y) in enumerate(pts):
                la, lo = to_geo(x, y)
                f.write(f'{name},{i},{la:.3f},{lo:.3f}\n')
            print(name, len(pts), 'vertices', file=sys.stderr)
