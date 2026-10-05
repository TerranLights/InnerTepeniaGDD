"""Map 08 - Towns: South Shetlands and the Peninsula tip, the densest cluster of Priority Batch 1."""
from tepenia_towns_common import *

cities = load_cities(); labels = load_labels('labels_full.csv'); allr = load_candidates()
rows = [r for r in allr if r['kind'] == 'station' and r['lat'] > -64.3 and -62 < r['lon'] < -55 and r['lat'] < -62]
fig, ax = new_figure('Towns — Candidate Stations: South Shetlands', f'{len(rows)} stations around King George, Greenwich and Deception Islands and Hope Bay', extent=extent_for(rows, 0.35, 120_000), width_in=17.0)
draw_base(ax, graticule=True, continent_names=False, region_names=False)
context_cities(ax, cities, labels, label_size=11)
draw_markers(ax, rows, size=1.6)
place_labels(fig, ax, [(r['x'], r['y'], f"{r['num']} {r['short']}") for r in rows], fontsize=12, markers_xy=[(r['x'], r['y']) for r in rows])
scale_bar_small(ax, 100)
cnt = {k: sum(1 for r in rows if r['tier'] == k) for k in TIER}
put_legend(fig, ax, station_legend_items({k:v for k,v in cnt.items() if v}) + city_context_item(), title='Candidate towns', loc='lower right', anchor=(0.995, 0.01), fs=11)
footer(fig, 'Several rows share one site (GARS, O\'Higgins and Rada Covadonga are within 0.1 km)  ·  Numbers match the Priority Batch 1 reference file')
save(fig, '08_Towns_Candidate_Stations_South_Shetlands')
