"""Map 07 - Towns: Peninsula close-up of the Priority Batch 1 stations."""
from tepenia_towns_common import *

cities = load_cities(); labels = load_labels('labels_full.csv'); allr = load_candidates()
rows = [r for r in allr if r['kind'] == 'station' and -72 < r['lon'] < -50 and r['lat'] > -69]
fig, ax = new_figure('Towns — Candidate Stations: the Peninsula', f'{len(rows)} of the 32 lie on the Antarctic Peninsula and the South Shetlands (Orcadas, in the South Orkneys, is on map 06)', extent=extent_for(rows, 0.12, 250_000), width_in=17.0)
draw_base(ax, size=1.0, continent_names=False)
context_cities(ax, cities, labels, label_size=11)
draw_markers(ax, rows, size=1.3)
place_labels(fig, ax, [(r['x'], r['y'], f"{r['num']} {r['short']}") for r in rows], fontsize=11.5, markers_xy=[(r['x'], r['y']) for r in rows])
scale_bar_small(ax, 250)
cnt = {k: sum(1 for r in rows if r['tier'] == k) for k in TIER}
put_legend(fig, ax, station_legend_items({k:v for k,v in cnt.items() if v}) + city_context_item(), title='Candidate towns', loc='lower right', anchor=(0.995, 0.01), fs=11)
footer(fig, 'Numbers match Towns_Priority_Batch_1_Reference_2026-10-04.md  ·  Data: data/town_candidates.csv')
save(fig, '07_Towns_Candidate_Stations_Peninsula')
