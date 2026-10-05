"""Map 11 - Towns: close-up of the densest cluster of automatic weather stations (Casey, Law Dome and Wilkes Land coast)."""
from tepenia_towns_common import *

cities = load_cities(); labels = load_labels('labels_full.csv'); allr = load_candidates()
rows = [r for r in allr if r['kind'] == 'aws' and r['nearest_city'] in ('Casey', 'Relung Panen') and float(r['nearest_city_km']) < 300]
fig, ax = new_figure('Towns — Possible Comms Posts: Casey and Law Dome', f'{len(rows)} automatic weather stations on the Wilkes Land coast and Law Dome  ·  numbers match map 09', extent=extent_for(rows, 0.3, 200_000), width_in=17.0)
draw_base(ax, graticule=True, continent_names=False, region_names=False)
context_cities(ax, cities, labels, label_size=11)
draw_markers(ax, rows, size=1.5)
place_labels(fig, ax, [(r['x'], r['y'], f"{r['num']} {r['short']}") for r in rows], fontsize=11, color='#3F2F70', markers_xy=[(r['x'], r['y']) for r in rows])
scale_bar_small(ax, 100)
nu = sum(1 for r in rows if r['status'] == 'unknown'); nc = sum(1 for r in rows if r['status'] == 'closed')
put_legend(fig, ax, aws_legend_items(nu, nc) + city_context_item(), title='Possible comms posts', loc='lower right', anchor=(0.995, 0.01), fs=11)
footer(fig, 'AO 28 and Loewe Massif AWS sit within about 1 km of each other  ·  Data: data/town_candidates.csv')
save(fig, '11_Towns_Comms_Post_Candidates_Casey')
