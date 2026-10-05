"""Map 05 - Tepenia: Arcanet regional subnets."""
from tepenia_common import *

cities = load_cities(); labels = load_labels('labels_full.csv')
fig, ax = new_figure('Tepenia — Arcanet Subnets', 'Six regional subnets and the Pole relay  ·  zones are schematic groupings of member cities, not borders')
draw_base(ax, continent_names=False)
draw_subnet_zones(ax, cities)
draw_cities(ax, cities, labels, label_size=11.5)
draw_subnet_titles(ax)
scale_bar(ax)
put_legend(fig, ax, subnet_legend_items(include_pole=True) + city_legend_items()[:2], title='Subnets', loc='upper right')
footer(fig, 'Hubs (star): Palmer City, Halley, Mawson, Mirny, Janbogo, Byrd  ·  Signy\'s Arcanet link to the Palmer subnet is weak (dashed)')
save(fig, '05_Tepenia_Arcanet_Subnets')
