"""Map 03 - Tepenia: cities + airports."""
from tepenia_common import *

cities = load_cities(); labels = load_labels('labels_full.csv'); airports = load_airports(cities)
fig, ax = new_figure('Tepenia — Cities & Airports', 'Ten airport sites: eleven host cities, three more cities served by an airport they do not own', panel_in=5.6)
draw_base(ax)
draw_airports(ax, airports, cities)
draw_cities(ax, cities, labels)
draw_airport_names(ax, airports)
scale_bar(ax)
put_legend(fig, ax, airport_legend_items(), title='Airports')
put_notes(fig, ax, "Airport roster\n\nHosts (11 cities, 9 sites): Zukelli + Janbogo (one shared airport), Mirny, Zhongshan + Sinheung + Shirayuki (the Tri-Cities Airport), Troll, Rothera, Marambio (domestic), Belgrano, Byrd. Plus Machu Picchu (international) and Mountain Pass (an outpost, not a city).\n\nServed, not host: Pergamino and Contrapunto (via Machu Picchu); Santa Luce (via Troll first, Belgrano second).\n\nNo air access: 23 cities, including every Mawson-subnet city. Signy has neither road nor air access. Palmer City is deliberately air-disconnected.\n\nStatus: Byrd's fleet is grounded; Mountain Pass has been dark since the Tower fell.", top=0.30)
footer(fig, 'Per Locations/Infrastructure/Airports.md  ·  Mountain Pass is an outpost, not a city  ·  Machu Picchu: real station site on King George Island')
save(fig, '03_Tepenia_Cities_and_Airports')
