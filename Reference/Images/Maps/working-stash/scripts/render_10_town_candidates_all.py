"""Map 10 - Towns: all 68 candidate sites together (32 stations + 36 automatic weather stations), full continent."""
from tepenia_towns_common import *

cities = load_cities(); labels = load_labels('labels_full.csv'); rows = load_candidates()
fig, ax = new_figure('Towns — All Candidate Sites', '32 candidate stations (circles, diamonds, squares) and 36 possible comms posts (triangles)  ·  no label numbers; see maps 06 to 09 for the indexes', panel_in=0)
draw_base(ax)
context_cities(ax, cities, labels)
draw_markers(ax, rows)
scale_bar(ax)
cnt = {k: sum(1 for r in rows if r['kind'] == 'station' and r['tier'] == k) for k in TIER}
nu = sum(1 for r in rows if r['kind'] == 'aws' and r['status'] == 'unknown'); nc = sum(1 for r in rows if r['kind'] == 'aws' and r['status'] == 'closed')
put_legend(fig, ax, station_legend_items(cnt) + aws_legend_items(nu, nc) + city_context_item(), title='Candidate sites', fs=11.5)
footer(fig, 'Data: data/town_candidates.csv (from the Towns real-station inventory)  ·  Not a decision about any town; scope per the developer\'s 2026-10-04 ruling')
save(fig, '10_Towns_All_Candidate_Sites')
