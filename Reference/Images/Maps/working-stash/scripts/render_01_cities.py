"""Map 01 - Tepenia: cities only. All 38 cities on real Antarctica, colored by Arcanet subnet."""
from tepenia_common import *

cities = load_cities(); labels = load_labels('labels_full.csv')
fig, ax = new_figure('Tepenia — Cities', 'All 38 cities, placed at the real GPS coordinates of their station sites  ·  colored by Arcanet subnet')
draw_base(ax)
draw_cities(ax, cities, labels)
scale_bar(ax)
put_legend(fig, ax, subnet_legend_items() + city_legend_items(), title='Cities by subnet')
footer(fig, 'Base: Natural Earth 10m (public domain)   ·   Data: data/cities.csv')
save(fig, '01_Tepenia_Cities')
