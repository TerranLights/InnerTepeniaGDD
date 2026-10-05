"""Map 12 - Towns focus: the three sites of developer interest (2026-10-04): #24 Russkaya, #16 Leningradskaya, #18/#19 Molodezhnaya + Mountain Evening (Mt Vechernyaya).
Shows each with its nearest city (dashed line, great-circle km) and the highway network, on the full continent."""
from tepenia_towns_common import *
from shapely.geometry import LineString, Point

cities = load_cities(); labels = load_labels('labels_full.csv'); allr = load_candidates(); specs, geom = load_highways()
want = {'24': 'Russkaya', '16': 'Leningradskaya', '18': 'Molodezhnaya', '19': 'Mountain Evening (Mt Vechernyaya)'}
rows = [r for r in allr if r['kind'] == 'station' and r['num'] in want]
fig, ax = new_figure('Towns — Sites of Interest', '#24 Russkaya  ·  #16 Leningradskaya  ·  #18 Molodezhnaya + #19 Mountain Evening  ·  with the nearest city and the highway network', panel_in=5.8)
draw_base(ax)
draw_highways(ax, specs, geom, size=0.8)
draw_junctions(ax)
context_cities(ax, cities, labels)
groups = [[r for r in rows if r['num'] in ('24',)], [r for r in rows if r['num'] in ('16',)], [r for r in rows if r['num'] in ('18', '19')]]
lines = [LineString(g['pts']) for g in geom.values()]
# open water = not land and not ice shelf (labels go over the sea, clear of every city)
solid = unary_union(list(base_layer('land').geometry) + list(base_layer('ice_shelves').geometry)).buffer(25_000)
city_pts = [Point(c['x'], c['y']) for c in cities.values()]
placed = []


def sea_spot(cx, cy, anchor, prefer_side, w_km=520, h_km=130):
    """Nearest open-water spot to `anchor`, searched outward from the site (away from the pole)."""
    ux, uy = cx / math.hypot(cx, cy), cy / math.hypot(cx, cy)
    px, py = -uy, ux
    best = None
    for d in range(120, 1500, 60):
        for off in (0, 1, -1, 2, -2, 3, -3):
            off = off * prefer_side
            x = cx + ux * d * 1000 + px * off * 330_000 / 2.0
            y = cy + uy * d * 1000 + py * off * 330_000 / 2.0
            pt = Point(x, y)
            box = pt.buffer(1).envelope
            from shapely.geometry import box as sbox
            bx = sbox(x - w_km * 500, y - h_km * 500, x + w_km * 500, y + h_km * 500)
            if bx.intersects(solid): continue
            if any(bx.distance(cp) < 90_000 for cp in city_pts): continue
            if any(bx.intersects(o) for o in placed): continue
            if abs(x) > R_VIEW * 0.97 or abs(y) > R_VIEW * 0.97: continue
            cost = math.hypot(x - anchor[0], y - anchor[1])
            if best is None or cost < best[0]: best = (cost, x, y, bx)
        if best and d > 360: break
    placed.append(best[3])
    return best[1], best[2]


for gi, g in enumerate(groups):
    cx, cy = np.mean([r['x'] for r in g]), np.mean([r['y'] for r in g])
    ax.scatter([cx], [cy], s=520, marker='o', facecolor='#8FD19A', edgecolor='#16202A', linewidth=2.6, zorder=14)
    c = min(cities.values(), key=lambda c: math.hypot(c['x'] - cx, c['y'] - cy))
    km = math.hypot(c['x'] - cx, c['y'] - cy) / 1000
    ax.plot([cx, c['x']], [cy, c['y']], color='#16202A', lw=1.7, ls=(0, (4, 3)), zorder=13, alpha=0.85)
    mid = ((cx + c['x']) / 2, (cy + c['y']) / 2)
    tx, ty = sea_spot(cx, cy, mid, +1)
    ax.annotate(f"{km:.0f} km to {c['name']}", xy=mid, xytext=(tx, ty), textcoords='data', fontsize=11.5, color='#16202A', ha='center', va='center', zorder=16,
                bbox=dict(boxstyle='round,pad=0.25', facecolor='white', edgecolor='#8FA6B5', alpha=0.97),
                arrowprops=dict(arrowstyle='-', color='#16202A', lw=0.9, alpha=0.7, shrinkA=0, shrinkB=0))
    best = min(lines, key=lambda L: L.distance(Point(cx, cy)))
    q = best.interpolate(best.project(Point(cx, cy)))
    hk = math.hypot(q.x - cx, q.y - cy) / 1000
    ax.plot([cx, q.x], [cy, q.y], color='#C8202F', lw=1.7, ls=(0, (1.5, 2.5)), zorder=13, alpha=0.9)
    mid2 = ((cx + q.x) / 2, (cy + q.y) / 2)
    tx, ty = sea_spot(cx, cy, mid2, -1, w_km=560)
    ax.annotate(f"{hk:.0f} km to nearest highway", xy=mid2, xytext=(tx, ty), textcoords='data', fontsize=10.5, color='#7A1520', ha='center', va='center', zorder=16,
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#E3B3B8', alpha=0.97),
                arrowprops=dict(arrowstyle='-', color='#C8202F', lw=0.9, alpha=0.7, shrinkA=0, shrinkB=0))
items = []
for g in groups:
    nums = ' + '.join(r['num'] for r in g); names = ' + '.join(want[r['num']].split(' (')[0] for r in g)
    items.append((np.mean([r['x'] for r in g]), np.mean([r['y'] for r in g]), f"{nums} {names}"))
place_labels(fig, ax, items, fontsize=14, markers_xy=[(np.mean([r['x'] for r in g]), np.mean([r['y'] for r in g])) for g in groups])
scale_bar(ax)
leg = [Line2D([], [], marker='o', ls='', markersize=14, markerfacecolor='#8FD19A', markeredgecolor='#16202A', markeredgewidth=2, label='Site of interest (real station)'), Line2D([], [], color='#16202A', lw=1.7, ls=(0, (4, 3)), label='Straight line to the nearest city'), Line2D([], [], color='#C8202F', lw=1.7, ls=(0, (1.5, 2.5)), label='Straight line to the nearest highway')]
put_legend(fig, ax, leg + city_context_item(), title='Sites of interest', fs=11)
facts = [('24', 'Russkaya', 'Rock nunatak (gneiss), Cape Burks; mothballed since 1990; active revival effort (unbuilt); ship window about 3 weeks; 713 km from Byrd'),
         ('16', 'Leningradskaya', 'Rock nunatak, about 1 km by 100 to 150 m; mothballed since 1991; last visit Jan 2020; 450 km from Cape Adare'),
         ('18', 'Molodezhnaya', 'Rock oasis 8.3 by 2.7 km, 40+ lakes; legacy station, flood hazard; seasonal; 296 km from Temirötkel'),
         ('19', 'Mountain Evening', 'Belarus station on bedrock; wintering planned, unconfirmed; 13 km from Molodezhnaya')]
import textwrap
x0, _ = fig._panel; y = 0.55
for n, nm, tx in facts:
    fig.text(x0 + 0.008, y, f'{n}  {nm}', fontsize=11, fontweight='bold', color=INK, va='top'); y -= 0.016
    body = '\n'.join(textwrap.wrap(tx, 52)); fig.text(x0 + 0.008, y, body, fontsize=9.8, color=MUTED, va='top'); y -= 0.016 * (body.count('\n') + 1) + 0.014
footer(fig, 'Real station coordinates (Towns inventory)  ·  Not a decision about any town or city  ·  Data: data/town_candidates.csv')
save(fig, '12_Towns_Sites_of_Interest')
