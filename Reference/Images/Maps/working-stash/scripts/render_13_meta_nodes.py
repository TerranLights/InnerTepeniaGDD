"""Map 13 - Comms network: proposed and possible HF 'meta-nodes' on the 38 cities (developer request, 2026-10-04).
Data: data/meta_nodes.csv (status proposed = developer's four; possible = candidates from the radio research),
data/meta_links.csv. Distances are great-circle km computed here. Research: Locations/Towns/Open_Research_Topics.md."""
from tepenia_towns_common import *
from pyproj import Geod
import textwrap

GEOD = Geod(ellps='WGS84')
nodes = {r['id']: r for r in csv.DictReader(open(DATA / 'meta_nodes.csv', encoding='utf8'))}
for r in nodes.values():
    r['lat'], r['lon'] = float(r['lat']), float(r['lon']); r['x'], r['y'] = P(r['lat'], r['lon'])
links = list(csv.DictReader(open(DATA / 'meta_links.csv', encoding='utf8')))
cities = load_cities(); labels = load_labels('labels_full.csv')

fig, ax = new_figure('Comms Network — Meta-Nodes', 'Proposed (the developer\'s four) and possible HF meta-nodes, with great-circle hop lengths  ·  research: Locations/Towns/Open_Research_Topics.md', panel_in=6.4, extent=(-3.5e6, 3.9e6, -5.0e6, 2.4e6))
draw_base(ax)
context_cities(ax, cities, labels, label_size=9.2)

PROP, POSS = '#B3122A', '#0E7C86'
def path(a, b):
    pts = GEOD.npts(a['lon'], a['lat'], b['lon'], b['lat'], 60)
    xy = [(a['x'], a['y'])] + [P(la, lo) for lo, la in pts] + [(b['x'], b['y'])]
    return np.array(xy)
dist = {}
for L in links:
    a, b = nodes[L['a']], nodes[L['b']]
    km = GEOD.inv(a['lon'], a['lat'], b['lon'], b['lat'])[2] / 1000; dist[(L['a'], L['b'])] = km
    xy = path(a, b)
    if L['status'] == 'proposed':
        ax.plot(xy[:, 0], xy[:, 1], color='white', lw=7.5, zorder=8, alpha=0.9, solid_capstyle='round')
        ax.plot(xy[:, 0], xy[:, 1], color=PROP, lw=4.2, zorder=8.5, solid_capstyle='round')
    else:
        ax.plot(xy[:, 0], xy[:, 1], color='white', lw=5.0, zorder=8, alpha=0.8)
        ax.plot(xy[:, 0], xy[:, 1], color=POSS, lw=2.6, ls=(0, (4, 3)), zorder=8.5)
    # hop-length label at the middle of the line
    m = xy[len(xy) // 2]
    ax.text(m[0], m[1], f'{km:,.0f}', fontsize=9.6, fontweight='bold', color=PROP if L['status'] == 'proposed' else POSS, ha='center', va='center',
            zorder=9, bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='none', alpha=0.9))

# Peninsula meta-node region: a ring of radius 200 km around the centroid (the five cities lie within about 200 km)
pen = nodes['PEN']; th = np.linspace(0, 2 * np.pi, 200)
ax.plot(pen['x'] + 200_000 * np.cos(th), pen['y'] + 200_000 * np.sin(th), color=PROP, lw=2.2, ls=(0, (2, 2)), zorder=9)

for nid, r in nodes.items():
    if r['status'] == 'external':
        ax.scatter([r['x']], [r['y']], s=70, marker='D', facecolor='white', edgecolor=POSS, linewidth=1.8, zorder=13)
    elif r['status'] == 'proposed':
        ax.scatter([r['x']], [r['y']], s=520, marker='H', facecolor=PROP, edgecolor='white', linewidth=2.2, zorder=14)
    else:
        ax.scatter([r['x']], [r['y']], s=330, marker='H', facecolor='white', edgecolor=POSS, linewidth=3.0, zorder=14)
items = [(r['x'], r['y'], r['name']) for r in nodes.values() if r['status'] != 'external' or r['id'] == 'HOB']
place_labels(fig, ax, items, fontsize=12.5, markers_xy=[(r['x'], r['y']) for r in nodes.values()])
scale_bar(ax)

leg = [Line2D([], [], marker='H', ls='', markersize=17, markerfacecolor=PROP, markeredgecolor='white', markeredgewidth=1.8, label='Proposed meta-node (developer)'),
       Line2D([], [], marker='H', ls='', markersize=15, markerfacecolor='white', markeredgecolor=POSS, markeredgewidth=2.6, label='Possible meta-node (research)'),
       Line2D([], [], color=PROP, lw=4, label='Proposed trunk hop (km)'),
       Line2D([], [], color=POSS, lw=2.6, ls=(0, (4, 3)), label='Possible hop (km)'),
       Line2D([], [], marker='D', ls='', markersize=8, markerfacecolor='white', markeredgecolor=POSS, markeredgewidth=1.6, label='Link endpoint (city or Hobart), not a node'),
       Line2D([], [], marker='o', ls='', markersize=8, markerfacecolor='#999', markeredgecolor='white', label='The 38 cities (color = subnet)')]
put_legend(fig, ax, leg, title='Meta-nodes', fs=11)
notes = [
 ('How to read', 'A meta-node is a tight subregion with a strong antenna or a set of directional antennas (about 1 kW, +6 to +10 dBi). Hop lengths are great-circle km.'),
 ('Peninsula', 'Ring = 200 km around the centroid of Palmer City, Pergamino, Marambio, Esperanza and Puerto Abrigo. A Weddell-facing array on the southeast side (Rothera or Marambio) is 80 to 220 km nearer the Weddell nodes.'),
 ('Weddell sector', 'The 3,288 km Peninsula to Utstein hop works 23 to 24 h at 1 kW with +6 dBi but only 3 to 21 h/day with simple antennas, so a Weddell node (Halley or Belgrano) is required for simple stations and helpful for strong ones. Neumayer adds a failure point once one of them is in.'),
 ('Indian Ocean', 'Mawson, Mirny and Davis/Larsemann are optional: Mawson to Casey (2,029 km) already works 24 h with strong antennas. All of Mawson to Casey lies in the polar cap, so extra nodes cannot cure a polar-cap blackout.'),
 ('Byrd', 'Byrd to Rothera (1,990 km) is the better link (one quiet end); Byrd to Belgrano is weaker in polar night. The Pole, McMurdo and Jang Bogo share the polar-cap blackout and do not help.'),
 ('Macquarie Island', 'Possible relay between Tasmania and the Antarctic coast: Hobart to Macquarie 1,545 km, Macquarie to Dumont d\'Urville 1,692, to Cape Adare 1,949, to Zukelli 2,262, to Casey 2,877. Hobart to Dumont d\'Urville direct is 2,681 km. Radio model pending; the island is not known to exist in canon.'),
 ('Not shown', 'Signy is a regional hub, not a trunk link. Elephant/Clarence relay: not needed for HF (Esperanza serves). Research is model output: spot-check before relying on it.'),
]
x0, _ = fig._panel; y = 0.64
for h, t in notes:
    fig.text(x0 + 0.008, y, h, fontsize=11, fontweight='bold', color=INK, va='top'); y -= 0.0145
    body = '\n'.join(textwrap.wrap(t, 56)); fig.text(x0 + 0.008, y, body, fontsize=9.3, color=MUTED, va='top'); y -= 0.0132 * (body.count('\n') + 1) + 0.013
footer(fig, 'Proposed = the developer\'s four; possible = candidates from the radio research  ·  Not canon  ·  Data: data/meta_nodes.csv, data/meta_links.csv')
save(fig, '13_Comms_Meta_Nodes')
