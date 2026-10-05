"""Map 02 - Tepenia: cities + highways."""
from tepenia_common import *

cities = load_cities(); labels = load_labels('labels_full.csv'); specs, geom = load_highways()
fig, ax = new_figure('Tepenia — Cities & Highways', 'The overland highway network (pre-war routes; coastal sections partly out of service since the Long Night War)', panel_in=5.6)
draw_base(ax)
draw_highways(ax, specs, geom)
draw_junctions(ax)
draw_highway_badges(ax, specs, geom, offsets=load_badge_offsets())
draw_cities(ax, cities, labels)
scale_bar(ax)
put_legend(fig, ax, highway_legend_items(specs), title='Highways')
put_notes(fig, ax, "How to read this map\n\nRoute shapes are traced from the developer's hand-drawn highway sketch and georeferenced onto real Antarctica; where a city sits off the sketched line, a spur connects it. Stops and endpoints follow Locations/Infrastructure/Highways.md.\n\nSquare = The Temirötkel Junction (Hwy 4, Hwy 7-ext and Hwy 37 converge near, not in, Sayowa). The Zhongshan/Sinheung/Shirayuki tri-junction joins Hwy 4, 22 and 110. Concordia joins Hwy 37, 110 and 183; Dumont d'Urville joins Hwy 2 and 183; Byrd joins Hwy 1 and 22.\n\nNo highway: Pergamino, Contrapunto and Signy are islands. Palmer City is reached by boat from a Hwy 1 ramp. Fort McMurdo and Scott share a spur whose crossing type is still undecided (dashed).", top=0.60)
footer(fig, 'Route shapes traced from the developer\'s hand-drawn highway sketch, georeferenced onto real Antarctica; stops per Locations/Infrastructure/Highways.md')
save(fig, '02_Tepenia_Cities_and_Highways')
