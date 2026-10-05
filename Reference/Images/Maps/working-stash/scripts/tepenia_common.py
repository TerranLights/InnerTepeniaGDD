"""Shared code for every Tepenia map: projection, base layers, data loaders, and the drawing layers
(cities, highways, airports, subnets). Each render_NN_*.py script only composes these layers.

Projection: south polar stereographic, true scale at 71 S, 0 deg longitude at the top, 90 E to the right
(the orientation of the developer's earlier Antarctica/Tepenia sketches).
Base data: Natural Earth 10m (public domain), clipped to Antarctica by prepare_base_data.py -> data/base/*.geojson
Env vars (same convention as the other Map Files packages): OUT_DIR (default ../out).
"""
import csv, math, os
from pathlib import Path
import numpy as np
import geopandas as gpd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib import font_manager as fm
from matplotlib.patches import Rectangle, Circle
from matplotlib.lines import Line2D
from shapely.geometry import Point, LineString, MultiPoint
from shapely.ops import unary_union
from pyproj import Transformer

HERE = Path(__file__).resolve().parent.parent
DATA = HERE / 'data'
OUT = Path(os.environ.get('OUT_DIR', HERE / 'out')); OUT.mkdir(parents=True, exist_ok=True)

for f in (HERE / 'fonts').glob('*.ttf'):
    fm.fontManager.addfont(str(f))
SERIF, SANS = 'Crimson Text', 'Lato'
mpl.rcParams['font.family'] = SANS
mpl.rcParams['svg.fonttype'] = 'none'

CRS = '+proj=stere +lat_0=-90 +lat_ts=-71 +lon_0=0 +datum=WGS84 +units=m'
_T = Transformer.from_crs('EPSG:4326', CRS, always_xy=True)
def P(lat, lon): return _T.transform(lon, lat)

# ---- palette (subnet colors follow the developer's Arcanet subnet sketch) ----
SUBNET_COLOR = {'Palmer': '#6A5ACD', 'Halley': '#3FA3D8', 'Mawson': '#E8238A', 'Mirny': '#1DAA2A',
                'Janbogo': '#CC7A22', 'Byrd': '#8E9A10', 'Amundsen-Scott': '#3A3A3A'}
SUBNET_LABEL = {'Palmer': 'Palmer ("American") Subnet', 'Halley': 'Halley ("Atlantic") Subnet', 'Mawson': 'Mawson Subnet',
                'Mirny': 'Mirny ("Australian") Subnet', 'Janbogo': 'Janbogo Subnet', 'Byrd': 'Byrd ("Pacific") Subnet',
                'Amundsen-Scott': 'Amundsen-Scott (the Pole)'}
SEA, LAND, SHELF, ICE_EDGE, GRAT, INK, MUTED = '#DCE8F0', '#F3F0E8', '#EAF3F8', '#8FA6B5', '#B9CBD8', '#232B33', '#5F6F7B'


# ------------------------------------------------------------------ data loaders
def load_cities():
    rows = list(csv.DictReader(open(DATA / 'cities.csv', encoding='utf8')))
    for r in rows:
        r['lat'], r['lon'] = float(r['lat']), float(r['lon'])
        r['x'], r['y'] = P(r['lat'], r['lon'])
        r['hub'] = r['subnet_hub'] == '1'
    return {r['id']: r for r in rows}


def load_labels(name='labels_full.csv'):
    """id -> (dx, dy, ha) label offsets in points, from data/<name>."""
    out = {}
    p = DATA / name
    if p.exists():
        for r in csv.DictReader(open(p, encoding='utf8')):
            out[r['id']] = (float(r['dx']), float(r['dy']), r['ha'], r.get('text', '') or '')
    return out


def load_highways():
    specs = {r['id']: r for r in csv.DictReader(open(DATA / 'highways.csv', encoding='utf8'))}
    geom = {}
    for r in csv.DictReader(open(DATA / 'highway_geometry.csv')):
        geom.setdefault(r['line_id'], {'kind': r['kind'], 'hwy': r['highway_id'], 'pts': []})['pts'].append(
            P(float(r['lat']), float(r['lon'])))
    return specs, geom


def load_airports(cities):
    specs, geom = load_highways()
    out = []
    for r in csv.DictReader(open(DATA / 'airports.csv', encoding='utf8')):
        pos = r['lat']
        if pos.startswith('@hwy37:'):          # midway along Hwy 37 between two stops
            a, b = pos.split(':')[1].split('-')
            line = LineString(geom['hwy37']['pts'])
            ta = line.project(Point(cities[a]['x'], cities[a]['y'])); tb = line.project(Point(cities[b]['x'], cities[b]['y']))
            q = line.interpolate((ta + tb) / 2); x, y = q.x, q.y
        elif pos.startswith('@'):
            ids = pos[1:].split('+'); x = np.mean([cities[i]['x'] for i in ids]); y = np.mean([cities[i]['y'] for i in ids])
        else:
            x, y = P(float(r['lat']), float(r['lon']))
        r['x'], r['y'] = x, y
        r['serves'] = [s for s in r['serves'].split(';') if s]
        r['label'] = '1' if r['id'] in ('zukelli_janbogo', 'tri_cities', 'machu_picchu', 'mountain_pass') else '0'
        out.append(r)
    return out


_base = {}
def base_layer(name):
    if name not in _base:
        g = gpd.read_file(DATA / 'base' / f'{name}.geojson')
        _base[name] = g.to_crs(CRS)
    return _base[name]


# ------------------------------------------------------------------ canvas
R_VIEW = 3.42e6      # half-width of the full-continent view, meters


def new_figure(title, subtitle, extent=None, width_in=18.0, panel_in=0.0):
    """Square map with a title band. extent = (xmin, xmax, ymin, ymax) in meters (default: whole continent)."""
    xmin, xmax, ymin, ymax = extent or (-R_VIEW, R_VIEW, -R_VIEW, R_VIEW)
    aspect = (ymax - ymin) / (xmax - xmin)
    band = 1.55
    W = width_in + panel_in
    fig = plt.figure(figsize=(W, width_in * aspect + band))
    H = fig.get_size_inches()[1]
    ax = fig.add_axes([0, 0, width_in / W, (H - band) / H])
    fig._panel = (width_in / W, (H - band) / H) if panel_in else None
    ax.set_xlim(xmin, xmax); ax.set_ylim(ymin, ymax); ax.set_aspect('equal'); ax.axis('off')
    fig.patch.set_facecolor('#FBFAF6')
    fig.text(0.035 * 18 / W, 1 - 0.55 / H, title, fontsize=44, fontfamily=SERIF, fontweight='bold', color=INK, va='center')
    fig.text(0.037 * 18 / W, 1 - 1.12 / H, subtitle, fontsize=15, color=MUTED, va='center')
    ax._extent = (xmin, xmax, ymin, ymax)
    return fig, ax


def halo(lw=3.0, color='white', alpha=0.92):
    return [pe.withStroke(linewidth=lw, foreground=color, alpha=alpha)]


def draw_base(ax, graticule=True, region_names=True, size=1.0, continent_names=True):
    ax.add_patch(Rectangle((ax._extent[0], ax._extent[2]), ax._extent[1] - ax._extent[0], ax._extent[3] - ax._extent[2],
                           facecolor=SEA, zorder=0))
    # polygons are drawn WITHOUT outlines (the land polygon's closing edge along 180 deg would show as a seam);
    # the coastline and ice-shelf front layers draw the real edges
    base_layer('land').plot(ax=ax, facecolor=LAND, edgecolor='none', linewidth=0, zorder=2)
    base_layer('ice_shelves').plot(ax=ax, facecolor=SHELF, edgecolor='none', linewidth=0, zorder=3)
    base_layer('coastline').plot(ax=ax, color=ICE_EDGE, linewidth=0.8, zorder=3.5)
    base_layer('ice_shelf_lines').plot(ax=ax, color=ICE_EDGE, linewidth=0.6, zorder=3.5)
    if graticule:
        th = np.radians(np.linspace(0, 360, 721))
        for lat in (-60, -70, -80):
            r = math.hypot(*P(lat, 0))
            ax.plot(r * np.sin(th), r * np.cos(th), color=GRAT, lw=0.7, zorder=1, ls=(0, (1, 2.5)))
        for lon in range(0, 360, 30):
            a = math.radians(lon); r0, r1 = math.hypot(*P(-89.5, 0)), math.hypot(*P(-58, 0))
            ax.plot([r0 * math.sin(a), r1 * math.sin(a)], [r0 * math.cos(a), r1 * math.cos(a)], color=GRAT, lw=0.7, zorder=1, ls=(0, (1, 2.5)))
        # Antarctic Circle
        r = math.hypot(*P(-66.5622, 0))
        ax.plot(r * np.sin(th), r * np.cos(th), color='#5B8DB0', lw=1.4, ls=(0, (4, 4)), zorder=1.5)
        ax.text(*P(-66.5622, 205), 'ANTARCTIC CIRCLE', fontsize=11 * size, color='#5B8DB0', fontfamily=SERIF, style='italic',
                rotation=0, ha='center', va='center', zorder=1.6, path_effects=halo(2.5, SEA, 1))
        # meridian + latitude labels at the rim
        rr = math.hypot(*P(-58.6, 0))
        for lon in range(0, 360, 30):
            a = math.radians(lon); l = lon if lon <= 180 else lon - 360
            lab = '0°' if l == 0 else ('180°' if abs(l) == 180 else f'{abs(l)}°{"E" if l > 0 else "W"}')
            if abs(rr * math.sin(a)) < ax._extent[1] and abs(rr * math.cos(a)) < ax._extent[3]:
                ax.text(rr * math.sin(a), rr * math.cos(a), lab, fontsize=11 * size, color=MUTED, ha='center', va='center', zorder=1.6)
        for lat in (-60, -70, -80):
            x, y = P(lat, -22.5)
            ax.text(x, y, f'{abs(lat)}°S', fontsize=10 * size, color=MUTED, ha='center', va='center', zorder=1.6,
                    path_effects=halo(2.5, SEA, 1), rotation=0)
    if region_names:
        names = [('EAST ANTARCTICA', -82.5, 148, 0), ('WEST ANTARCTICA', -79, -100, 0), ('ANTARCTIC PENINSULA', -73.6, -74.5, -52)]
        for t, la, lo, rot in (names if continent_names else []):
            x, y = P(la, lo)
            ax.text(x, y, t, fontsize=12.5 * size, color='#9AA9B4', fontfamily=SERIF, style='italic', ha='center', va='center', rotation=rot,
                    zorder=2.5, alpha=0.9)
        for t, la, lo in [('Weddell Sea', -69.5, -40), ('Bellingshausen Sea', -71, -88), ('Amundsen Sea', -72, -112),
                          ('Ross Sea', -71, 178), ('Ross Ice Shelf', -81.2, -176), ('Ronne Ice Shelf', -78.3, -62), ('Pacific Ocean', -64, -140),
                          ('Southern Ocean', -62.4, 150), ('Indian Ocean', -62.8, 60), ('Atlantic Ocean', -61.3, -12),
                          ('King Haakon VII Sea', -68.3, 6), ('Prydz Bay', -68.3, 75), ('Dumont d\'Urville Sea', -64.2, 128)]:
            x, y = P(la, lo)
            ax.text(x, y, t, fontsize=11 * size, color='#5F8FB2', fontfamily=SERIF, style='italic', ha='center', va='center', zorder=2.5)


def scale_bar(ax, km=1000, loc=(0.06, 0.04), size=1.0):
    x0 = ax._extent[0] + loc[0] * (ax._extent[1] - ax._extent[0]); y0 = ax._extent[2] + loc[1] * (ax._extent[3] - ax._extent[2])
    L = km * 1000
    ax.plot([x0, x0 + L], [y0, y0], color=INK, lw=2.2, zorder=9, solid_capstyle='butt')
    for k in range(0, 3):
        ax.plot([x0 + k * L / 2] * 2, [y0 - 25000, y0 + 25000], color=INK, lw=1.6, zorder=9)
    for k, t in enumerate(['0', f'{km // 2}', f'{km} km']):
        ax.text(x0 + k * L / 2, y0 + 55000, t, fontsize=11 * size, ha='center', va='bottom', color=INK, zorder=9)
    ax.text(x0, y0 - 70000, 'Polar stereographic, scale true at 71°S', fontsize=9 * size, color=MUTED, va='top', ha='left', zorder=9)


def footer(fig, text):
    fig.text(0.037 * 18 / fig.get_size_inches()[0], 0.012, text, fontsize=9.5, color=MUTED, va='bottom', ha='left')


# ------------------------------------------------------------------ layers
def city_label_text(c):
    t = c['name']
    if c['name_flag'] == 'placeholder': t += ' †'
    elif c['name_flag'] == 'rename-pending': t += ' ‡'
    return t


def draw_cities(ax, cities, labels, color_by_subnet=True, size=1.0, z=10, markers=True, label_cities=True, subnet_filter=None,
                label_size=13.5):
    for cid, c in cities.items():
        if subnet_filter and c['subnet'] not in subnet_filter: continue
        col = SUBNET_COLOR[c['subnet']] if color_by_subnet else INK
        if markers:
            if c['hub']:
                ax.scatter([c['x']], [c['y']], s=330 * size, marker='*', facecolor=col, edgecolor='white', linewidth=1.3, zorder=z + 1)
            elif c['subnet'] == 'Amundsen-Scott':
                ax.scatter([c['x']], [c['y']], s=170 * size, marker='D', facecolor=col, edgecolor='white', linewidth=1.3, zorder=z + 1)
            else:
                ax.scatter([c['x']], [c['y']], s=105 * size, marker='o', facecolor=col, edgecolor='white', linewidth=1.5, zorder=z + 1)
        if label_cities:
            dx, dy, ha, txt = labels.get(cid, (14, 10, 'left', ''))
            t = txt or city_label_text(c)
            va = 'center'
            leader = math.hypot(dx, dy) > 22
            ax.annotate(t, (c['x'], c['y']), xytext=(dx, dy), textcoords='offset points', ha=ha, va=va, fontsize=label_size * size,
                        fontweight='bold', color=INK, zorder=z + 3, path_effects=halo(3.4),
                        arrowprops=dict(arrowstyle='-', color='#55616B', lw=0.9, shrinkA=0, shrinkB=4, relpos=(0 if ha == 'left' else (1 if ha == 'right' else 0.5), 0.5)) if leader else None)


def draw_highways(ax, specs, geom, size=1.0, z=6, number_tags=True):
    for lid, g in geom.items():
        pts = np.array(g['pts']); s = specs[g['hwy']]
        col = s['color']
        if g['kind'] == 'main':
            ls = (0, (3.2, 2.4)) if s['style'] == 'dashed' else '-'
            hls = (0, (3.2 * 4.6 / 7.5, 2.4 * 4.6 / 7.5)) if s['style'] == 'dashed' else '-'    # same dash length as the line itself
            ax.plot(pts[:, 0], pts[:, 1], color='white', lw=7.5 * size, zorder=z, ls=hls, solid_capstyle='butt' if s['style'] == 'dashed' else 'round', solid_joinstyle='round', alpha=0.9)
            ax.plot(pts[:, 0], pts[:, 1], color=col, lw=4.6 * size, zorder=z + 0.1, ls=ls, solid_capstyle='round', solid_joinstyle='round')
        else:
            ls = (0, (1.5, 2.2)) if g['kind'] == 'boat' else ((0, (3, 2)) if g['kind'] == 'spur_dashed' else '-')
            ax.plot(pts[:, 0], pts[:, 1], color='white', lw=5.2 * size, zorder=z, solid_capstyle='round', alpha=0.9)
            ax.plot(pts[:, 0], pts[:, 1], color=col, lw=2.9 * size, zorder=z + 0.1, ls=ls, solid_capstyle='round')


def draw_junctions(ax, size=1.0, z=7):
    for r in csv.DictReader(open(DATA / 'junctions.csv', encoding='utf8')):
        x, y = P(float(r['lat']), float(r['lon']))
        ax.scatter([x], [y], s=70 * size, marker='s', facecolor='white', edgecolor=INK, linewidth=1.4, zorder=z + 3)


def draw_airports(ax, airports, cities, size=1.0, z=8, label=True, label_offsets=None):
    label_offsets = label_offsets or {}
    for a in airports:
        status = a['status']
        face = {'operational': '#C8202F', 'grounded': '#E8A33A', 'dark': '#8B8F94'}[status]
        big = a['kind'] == 'international'
        ax.scatter([a['x']], [a['y']], s=(640 if big else 400) * size, marker='o', facecolor='#16202A', edgecolor='white', linewidth=1.8, zorder=z + 1)
        ax.scatter([a['x']], [a['y']], s=(300 if big else 175) * size, marker='o', facecolor=face, edgecolor='none', zorder=z + 2)
        ax.text(a['x'], a['y'], '✈', fontsize=(15 if big else 10.5) * size, ha='center', va='center', color='white',
                fontfamily='DejaVu Sans', zorder=z + 3)
        for sid in a['serves']:
            c = cities.get(sid)
            if c and math.hypot(c['x'] - a['x'], c['y'] - a['y']) > 25000:
                ax.plot([a['x'], c['x']], [a['y'], c['y']], color='#16202A', lw=1.5 * size, ls=(0, (1.2, 2.4)), zorder=z, alpha=0.85)


def city_legend_items():
    return [Line2D([], [], marker='*', ls='', markersize=17, markerfacecolor='#777', markeredgecolor='white', label='Subnet hub'),
            Line2D([], [], marker='o', ls='', markersize=10, markerfacecolor='#777', markeredgecolor='white', label='City'),
            Line2D([], [], marker='D', ls='', markersize=9, markerfacecolor=SUBNET_COLOR['Amundsen-Scott'], markeredgecolor='white', label='Amundsen Station (the South Pole)')]


def subnet_legend_items(include_pole=False):
    subs = ['Palmer', 'Halley', 'Mawson', 'Mirny', 'Janbogo', 'Byrd'] + (['Amundsen-Scott'] if include_pole else [])
    return [Line2D([], [], marker='o', ls='', markersize=11, markerfacecolor=SUBNET_COLOR[s], markeredgecolor='white', label=SUBNET_LABEL[s])
            for s in subs]


def put_legend(fig, ax, handles, title=None, loc='upper right', anchor=(0.995, 0.995), ncol=1, fs=12.5):
    kw = dict(handles=handles, ncol=ncol, fontsize=fs, title=title, title_fontsize=fs + 1.5, frameon=True, framealpha=1.0,
              edgecolor='#B9CBD8', facecolor='#FBFAF6', borderpad=0.9, labelspacing=0.65, handlelength=2.6)
    if getattr(fig, '_panel', None):          # legend lives in the side panel, clear of the map
        x0, ytop = fig._panel
        leg = fig.legend(loc='upper left', bbox_to_anchor=(x0 + 0.004, ytop - 0.004), **kw)
    else:
        leg = ax.legend(loc=loc, bbox_to_anchor=anchor, **kw)
    leg.set_zorder(20)
    for t in leg.get_texts(): t.set_color(INK)
    return leg


def save(fig, stem):
    png, svg = OUT / f'{stem}.png', OUT / f'{stem}.svg'
    fig.savefig(png, dpi=200, facecolor=fig.get_facecolor())
    fig.savefig(svg, facecolor=fig.get_facecolor())
    plt.close(fig)
    print('wrote', png)


# ------------------------------------------------------------------ legends/badges for the network layers
def highway_legend_items(specs):
    items = []
    for hid, s in specs.items():
        nm = s['name']
        lab = f"Hwy {s['number']}-ext — {nm}" if hid == 'hwy7ext' else f"Hwy {s['number']} — {nm}"
        ls = (0, (3.2, 2.4)) if s['style'] == 'dashed' else '-'
        items.append(Line2D([], [], color=s['color'], lw=5, ls=ls, label=lab))
    items.append(Line2D([], [], color='#444', lw=3, label='Connecting road / ramp (spur)'))
    items.append(Line2D([], [], color='#444', lw=3, ls=(0, (1.5, 2.2)), label='Boat crossing (Palmer City)'))
    items.append(Line2D([], [], marker='s', ls='', markersize=9, markerfacecolor='white', markeredgecolor=INK, label='The Temirötkel Junction'))
    return items


def airport_legend_items():
    out = []
    for lab, col, ms in [('Airport — operational', '#C8202F', 15), ('Airport — International (Machu Picchu)', '#C8202F', 19),
                         ('Airport — grounded (Byrd)', '#E8A33A', 15), ('Airport — dark / historical (Mountain Pass)', '#8B8F94', 15)]:
        out.append(Line2D([], [], marker='o', ls='', markersize=ms, markerfacecolor=col, markeredgecolor='#16202A', markeredgewidth=3, label=lab))
    out.append(Line2D([], [], color='#16202A', lw=1.6, ls=(0, (1.2, 2.4)), label='Served by that airport'))
    return out


def draw_highway_badges(ax, specs, geom, size=1.0, offsets=None):
    """Highway-number tags at the middle of each main line (offsets: hwy_id -> fraction along the line, 0..1)."""
    offsets = offsets or {}
    for hid, s in specs.items():
        g = geom[hid]; line = LineString(g['pts'])
        q = line.interpolate(offsets.get(hid, 0.5), normalized=True)
        ax.text(q.x, q.y, s['number'], fontsize=10.5 * size, fontweight='bold', color='white', ha='center', va='center', zorder=9,
                bbox=dict(boxstyle='round,pad=0.22', facecolor=s['color'], edgecolor='white', linewidth=1.4))


def load_badge_offsets():
    out = {}
    p = DATA / 'highway_badges.csv'
    if p.exists():
        for r in csv.DictReader(open(p)): out[r['id']] = float(r['t'])
    return out


def draw_airport_names(ax, airports, size=1.0, offsets=None):
    offs = offsets or load_airport_label_offsets()
    for a in airports:
        # an airport at a city that already carries the same name is identified by its ring alone (no duplicate label)
        if a.get('label', '1') == '0':
            continue
        dx, dy, ha = offs.get(a['id'], (0, -22, 'center'))
        ax.annotate(a['name'].replace(' Airport', '').replace(' Airfield', '') + ('\n(international)' if a['kind'] == 'international' else ''),
                    (a['x'], a['y']), xytext=(dx, dy), textcoords='offset points', ha=ha, va='center', fontsize=11.5 * size, style='italic',
                    color='#7A1520', fontweight='bold', zorder=16, path_effects=halo(3.2),
                    arrowprops=dict(arrowstyle='-', color='#7A1520', lw=0.8, shrinkA=0, shrinkB=9) if math.hypot(dx, dy) > 28 else None)


def put_notes(fig, ax, text, top=0.52, fs=11.5, width=44):
    """Free text under the legend in the side panel (only on maps that have a panel)."""
    import textwrap
    if not getattr(fig, '_panel', None): return
    x0, ytop = fig._panel
    body = '\n\n'.join('\n'.join(textwrap.wrap(par, width)) for par in text.split('\n\n'))
    fig.text(x0 + 0.008, top, body, fontsize=fs, color=MUTED, va='top', ha='left', linespacing=1.35)


def load_airport_label_offsets():
    out = {}
    p = DATA / 'labels_airports.csv'
    if p.exists():
        for r in csv.DictReader(open(p)): out[r['id']] = (float(r['dx']), float(r['dy']), r['ha'])
    return out


def draw_subnet_zones(ax, cities, buffer_m=300_000, hull_exclude=('signy',)):
    from shapely.geometry import Point as SP
    for sn, col in SUBNET_COLOR.items():
        if sn == 'Amundsen-Scott': continue
        pts = [SP(c['x'], c['y']) for c in cities.values() if c['subnet'] == sn and c['id'] not in hull_exclude]
        zone = unary_union([p.buffer(buffer_m) for p in pts]).convex_hull
        if sn == 'Byrd': zone = pts[0].buffer(520_000)
        if zone.geom_type == 'Polygon':
            xs, ys = zone.exterior.xy
            ax.fill(xs, ys, facecolor=col, alpha=0.17, edgecolor='none', zorder=4)
            ax.plot(xs, ys, color=col, lw=3.0, alpha=0.95, zorder=4.2, solid_joinstyle='round')
    # Signy: its own dashed ring and a dashed weak link to the Palmer subnet hub
    sg, pc = cities['signy'], cities['palmer_city']
    ax.add_patch(Circle((sg['x'], sg['y']), 120_000, facecolor=SUBNET_COLOR['Palmer'], alpha=0.17, edgecolor='none', zorder=4))
    ax.add_patch(Circle((sg['x'], sg['y']), 120_000, facecolor='none', edgecolor=SUBNET_COLOR['Palmer'], lw=2.4, ls=(0, (3, 2.5)), zorder=4.2))
    ax.plot([sg['x'], pc['x']], [sg['y'], pc['y']], color=SUBNET_COLOR['Palmer'], lw=2.4, ls=(0, (3, 2.5)), zorder=4.2)
    # the Pole: a ring (relay, not a subnet territory)
    am = cities['amundsen_station']
    ax.add_patch(Circle((am['x'], am['y']), 180_000, facecolor='none', edgecolor=SUBNET_COLOR['Amundsen-Scott'], lw=2.4, ls=(0, (1.5, 2)), zorder=4.2))


def draw_subnet_titles(ax, size=1.0):
    p = DATA / 'subnet_titles.csv'
    for r in csv.DictReader(open(p, encoding='utf8')):
        x, y = P(float(r['lat']), float(r['lon']))
        ax.text(x, y, r['text'].replace('\\n', '\n'), fontsize=float(r.get('size') or 25) * size, fontfamily=SERIF, fontweight='bold',
                color=SUBNET_COLOR[r['subnet']], ha='center', va='center', zorder=15, linespacing=0.95, path_effects=halo(4.2, '#FBFAF6', 0.92))
