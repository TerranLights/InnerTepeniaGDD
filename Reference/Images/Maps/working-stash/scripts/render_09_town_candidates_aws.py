"""Map 09 - Towns: the 36 automatic weather stations outside the cities (possible comms posts), full continent."""
from tepenia_towns_common import *

cities = load_cities(); labels = load_labels('labels_full.csv'); rows = [r for r in load_candidates() if r['kind'] == 'aws']
fig, ax = new_figure('Towns — Possible Comms Posts', 'The 36 automatic weather stations outside the 38 cities  ·  skeleton-crew beacons at most (under 100 people), not settlements', panel_in=5.8)
draw_base(ax)
context_cities(ax, cities, labels)
draw_markers(ax, rows)
items = [(np.mean([r['x'] for r in g]), np.mean([r['y'] for r in g]), ' '.join(r['num'] for r in g)) for g in clusters(rows, 120_000)]
place_labels(fig, ax, items, fontsize=11, color='#3F2F70', markers_xy=[(r['x'], r['y']) for r in rows])
scale_bar(ax)
nu = sum(1 for r in rows if r['status'] == 'unknown'); nc = sum(1 for r in rows if r['status'] == 'closed')
put_legend(fig, ax, aws_legend_items(nu, nc) + city_context_item(), title='Possible comms posts', fs=11.5)
panel_list(fig, 'Index (alphabetical)', [('', [(r['num'], r['short'], f"{r['status']} · {r['nearest_city']}") for r in rows])], top=0.80, fs=8.6, lh=0.0113)
footer(fig, 'All 36 sit in East Antarctica; the data has none on the Peninsula  ·  Duplicate coordinates exist (GC 46 / Schwerdtfeger; GC41 / Radok)  ·  Data: data/town_candidates.csv')
save(fig, '09_Towns_Comms_Post_Candidates')
