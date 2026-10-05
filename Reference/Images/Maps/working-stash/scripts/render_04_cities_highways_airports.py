"""Map 04 - Tepenia: cities + highways + airports."""
from tepenia_common import *

cities = load_cities(); labels = load_labels('labels_full.csv'); specs, geom = load_highways(); airports = load_airports(cities)
fig, ax = new_figure('Tepenia — Cities, Highways & Airports', 'The whole transport network on one sheet', panel_in=5.6)
draw_base(ax)
draw_highways(ax, specs, geom)
draw_junctions(ax)
draw_highway_badges(ax, specs, geom, size=0.9, offsets=load_badge_offsets())
draw_airports(ax, airports, cities)
draw_cities(ax, cities, labels)
draw_airport_names(ax, airports)
scale_bar(ax)
put_legend(fig, ax, highway_legend_items(specs) + airport_legend_items(), title='Highways & airports', fs=11.5)
put_notes(fig, ax, "Notes\n\nHighway shapes are traced from the developer's hand-drawn sketch; airports follow Airports.md. Dotted lines join an airport to cities it serves but does not host.\n\nMachu Picchu sits about 20 km from Contrapunto on King George Island; Mountain Pass lies on Hwy 37 midway between Kunlun and Ariun Nuur.", top=0.43)
footer(fig, 'Highways: shapes traced from the developer\'s sketch, stops per Highways.md  ·  Airports per Airports.md')
save(fig, '04_Tepenia_Cities_Highways_and_Airports')
