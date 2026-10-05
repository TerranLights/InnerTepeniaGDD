"""Map 06 - Towns: the 32 Priority Batch 1 stations (full continent), numbered as in Towns_Priority_Batch_1_Reference_2026-10-04.md."""
from tepenia_towns_common import *

cities = load_cities(); labels = load_labels('labels_full.csv'); rows = [r for r in load_candidates() if r['kind'] == 'station']
fig, ax = new_figure('Towns — Candidate Stations', 'The 32 Priority Batch 1 stations: 25 active, 7 recently closed and revivable  ·  numbers match the reference file', panel_in=5.8)
draw_base(ax)
context_cities(ax, cities, labels)
draw_markers(ax, rows)
items = []
for g in clusters(rows, 110_000):
    items.append((np.mean([r['x'] for r in g]), np.mean([r['y'] for r in g]), ' · '.join(r['num'] for r in g)))
place_labels(fig, ax, items, fontsize=12.5, markers_xy=[(r['x'], r['y']) for r in rows])
scale_bar(ax)
cnt = {k: sum(1 for r in rows if r['tier'] == k) for k in TIER}
put_legend(fig, ax, station_legend_items(cnt) + city_context_item(), title='Candidate towns (real stations)', fs=11.5)
secs = []
for k, t in TIER.items():
    secs.append((f"{k}  {t['label']}", [(r['num'], r['short'], r['nearest_city']) for r in rows if r['tier'] == k]))
panel_list(fig, 'Index', secs, top=0.775, fs=9.6, lh=0.0128)
footer(fig, 'Real station coordinates (Towns/Data inventory)  ·  Peninsula and South Shetlands are crowded: see maps 07 and 08  ·  Data: data/town_candidates.csv')
save(fig, '06_Towns_Candidate_Stations')
