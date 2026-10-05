"""Shared code for the towns-candidate maps (06 and up). Layers on top of tepenia_common.

Data: data/town_candidates.csv (written 2026-10-04 from Towns/Data/Real_Station_Inventory_Crossmatched.csv):
  kind=station : the 32 Priority Batch 1 stations (numbers 1-32 match Towns_Priority_Batch_1_Reference_2026-10-04.md)
  kind=aws     : the 36 automatic weather stations outside the 38 cities (W1-W36, alphabetical), possible comms posts
Nothing here names or characterizes a town; these are real inventory rows only.
"""
import csv, math
from tepenia_common import *

TIER = {
    'A1': dict(label='Active, year-round', marker='o', face='#1B7F3B', edge='white', s=150),
    'A2': dict(label='Active, summer-only', marker='o', face='#8FD19A', edge='#1B7F3B', s=150),
    'B1': dict(label='Temporarily closed (COMNAP 2024)', marker='D', face='#E8A33A', edge='white', s=130),
    'B2': dict(label='Closed since 2000, revivable', marker='s', face='#8B5A2B', edge='white', s=130),
}
AWS_COL = '#6B4FA0'

SHORT = {'Arturo Prat Antarctic Naval Base': 'Arturo Prat', 'German Antarctic Receiving Station (GARS)': 'GARS',
         'Johann Gregor Mendel Czech Antarctic Station': 'Mendel', 'Gabriel de Castilla Station': 'Gabriel de Castilla',
         'Jinnah Antarctic Station': 'Jinnah', 'Arturo Parodi Station': 'Arturo Parodi', "O'Higgins Base": "O'Higgins",
         'Gabriel Gonzalez Videla': 'González Videla', 'San Martin': 'San Martín', 'Risopatron': 'Risopatrón',
         'Decepcion': 'Decepción', 'Matienzo': 'Matienzo'}


def load_candidates():
    rows = list(csv.DictReader(open(DATA / 'town_candidates.csv', encoding='utf8')))
    for r in rows:
        r['lat'], r['lon'] = float(r['lat']), float(r['lon'])
        r['x'], r['y'] = P(r['lat'], r['lon'])
        r['short'] = SHORT.get(r['name'], r['name'])
    return rows


def extent_for(rows, pad_frac=0.18, min_half=250_000):
    xs = [r['x'] for r in rows]; ys = [r['y'] for r in rows]
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    half = max((max(xs) - min(xs)) / 2, (max(ys) - min(ys)) / 2, min_half) * (1 + pad_frac)
    return (cx - half, cx + half, cy - half, cy + half)


def clusters(rows, thr_m):
    """Greedy grouping of rows closer than thr_m (single link)."""
    groups = []
    for r in rows:
        for g in groups:
            if any(math.hypot(r['x'] - q['x'], r['y'] - q['y']) < thr_m for q in g):
                g.append(r); break
        else:
            groups.append([r])
    return groups


def draw_markers(ax, rows, size=1.0, z=12):
    for r in rows:
        if r['kind'] == 'station':
            t = TIER[r['tier']]
            ax.scatter([r['x']], [r['y']], s=t['s'] * size, marker=t['marker'], facecolor=t['face'], edgecolor=t['edge'],
                       linewidth=1.6, zorder=z)
        else:
            unknown = r['status'] == 'unknown'
            ax.scatter([r['x']], [r['y']], s=95 * size, marker='^', facecolor=AWS_COL if unknown else 'white', edgecolor=AWS_COL,
                       linewidth=1.8, zorder=z - 0.5)


def _bbox(artist, renderer):
    return artist.get_window_extent(renderer)


def _overlap(a, b, pad=2):
    w = min(a.x1, b.x1) - max(a.x0, b.x0) + pad
    h = min(a.y1, b.y1) - max(a.y0, b.y0) + pad
    return max(w, 0) * max(h, 0)


def place_labels(fig, ax, items, fontsize=11, color=INK, z=20, radii=(14, 26, 42, 62, 88, 118), halo_lw=3.4, markers_xy=None):
    """Greedy label placement. items: list of (x, y, text). Tries 12 directions at growing radii, picks the spot with the
    least overlap against labels already on the axes, the other items' anchor points and earlier choices; adds a leader
    line when the label is far from its anchor."""
    fig.canvas.draw()
    rend = fig.canvas.get_renderer()
    obstacles = [t.get_window_extent(rend) for t in ax.texts if t.get_text().strip()]
    anchors = [ax.transData.transform((x, y)) for x, y, _ in items] + [ax.transData.transform(p) for p in (markers_xy or [])]
    dpi_scale = fig.dpi / 72.0
    placed = []
    # densest anchors first so they get the closest slots
    order = sorted(range(len(items)), key=lambda i: -sum(1 for j, a in enumerate(anchors[:len(items)]) if j != i and
                                                         math.hypot(a[0] - anchors[i][0], a[1] - anchors[i][1]) < 90))
    for i in order:
        x, y, text = items[i]
        best = None
        for ri, rad in enumerate(radii):
            for k in range(12):
                ang = math.radians(15 + k * 30)
                dx, dy = rad * math.cos(ang), rad * math.sin(ang)
                ha = 'left' if dx > 4 else ('right' if dx < -4 else 'center')
                t = ax.annotate(text, (x, y), xytext=(dx, dy), textcoords='offset points', ha=ha, va='center', fontsize=fontsize,
                                fontweight='bold', color=color, zorder=z)
                bb = _bbox(t, rend); t.remove()
                cost = sum(_overlap(bb, o) for o in obstacles) + sum(_overlap(bb, p) * 3 for p in placed)
                for j, a in enumerate(anchors):
                    if bb.x0 - 6 < a[0] < bb.x1 + 6 and bb.y0 - 6 < a[1] < bb.y1 + 6:
                        cost += 400
                # prefer short offsets slightly and an up-right bias
                cost += rad * 1.2 + (0 if dy >= 0 else 8)
                if best is None or cost < best[0]: best = (cost, dx, dy, ha, bb)
            if best and best[0] < 60 + radii[ri] * 1.2: break      # good enough at this radius
        _, dx, dy, ha, bb = best
        leader = math.hypot(dx, dy) > 24
        ax.annotate(text, (x, y), xytext=(dx, dy), textcoords='offset points', ha=ha, va='center', fontsize=fontsize,
                    fontweight='bold', color=color, zorder=z, path_effects=halo(halo_lw),
                    arrowprops=dict(arrowstyle='-', color='#55616B', lw=0.9, shrinkA=0, shrinkB=5,
                                    relpos=(0 if ha == 'left' else (1 if ha == 'right' else 0.5), 0.5)) if leader else None)
        placed.append(bb)


def context_cities(ax, cities, labels, label_size=9.5):
    """Cities as quiet context: small dots, small gray labels."""
    for cid, c in cities.items():
        col = SUBNET_COLOR[c['subnet']]
        ax.scatter([c['x']], [c['y']], s=55, marker='o', facecolor=col, edgecolor='white', linewidth=1.0, zorder=9, alpha=0.9)
        dx, dy, ha, txt = labels.get(cid, (10, 8, 'left', ''))
        ax.annotate(txt or city_label_text(c), (c['x'], c['y']), xytext=(dx * 0.7, dy * 0.7), textcoords='offset points', ha=ha,
                    va='center', fontsize=label_size, color='#4A5560', zorder=9.5, path_effects=halo(2.6, 'white', 0.85),
                    arrowprops=dict(arrowstyle='-', color='#8A96A0', lw=0.6, shrinkA=0, shrinkB=3) if math.hypot(dx, dy) > 30 else None)


def station_legend_items(counts=None):
    items = []
    for k, t in TIER.items():
        if counts is not None and k not in counts: continue
        n = f' ({counts[k]})' if counts and k in counts else ''
        items.append(Line2D([], [], marker=t['marker'], ls='', markersize=11, markerfacecolor=t['face'], markeredgecolor=t['edge'],
                            markeredgewidth=1.4, label=t['label'] + n))
    return items


def aws_legend_items(n_unknown=None, n_closed=None):
    return [Line2D([], [], marker='^', ls='', markersize=11, markerfacecolor=AWS_COL, markeredgecolor=AWS_COL,
                   label='Automatic weather station, status unknown' + (f' ({n_unknown})' if n_unknown else '')),
            Line2D([], [], marker='^', ls='', markersize=11, markerfacecolor='white', markeredgecolor=AWS_COL, markeredgewidth=1.8,
                   label='Automatic weather station, closed' + (f' ({n_closed})' if n_closed else ''))]


def city_context_item():
    return [Line2D([], [], marker='o', ls='', markersize=8, markerfacecolor='#999', markeredgecolor='white', label='The 38 cities (context; color = subnet)')]


def panel_list(fig, title, sections, top=0.60, fs=10.2, lh=0.0132):
    """Numbered index in the side panel. sections: [(heading, [(num, name, note)])]."""
    if not getattr(fig, '_panel', None): return
    x0, _ = fig._panel
    y = top
    fig.text(x0 + 0.008, y, title, fontsize=fs + 2, fontweight='bold', color=INK, va='top'); y -= lh * 1.7
    for head, lines in sections:
        fig.text(x0 + 0.008, y, head, fontsize=fs, fontweight='bold', color=MUTED, va='top'); y -= lh * 1.25
        for num, name, note in lines:
            fig.text(x0 + 0.008, y, f'{num:>3}', fontsize=fs, fontweight='bold', color=INK, va='top', family='DejaVu Sans Mono')
            fig.text(x0 + 0.034, y, f'{name}' + (f'  ·  {note}' if note else ''), fontsize=fs, color=INK, va='top')
            y -= lh
        y -= lh * 0.5


def scale_bar_small(ax, km, loc=(0.06, 0.05), size=1.0):
    """Scale bar for close-ups: tick height and text offsets scale with the bar length (tepenia_common.scale_bar has fixed 25 km ticks)."""
    x0 = ax._extent[0] + loc[0] * (ax._extent[1] - ax._extent[0]); y0 = ax._extent[2] + loc[1] * (ax._extent[3] - ax._extent[2])
    L = km * 1000; tick = L * 0.04
    ax.plot([x0, x0 + L], [y0, y0], color=INK, lw=2.2, zorder=9, solid_capstyle='butt')
    for k in range(3):
        ax.plot([x0 + k * L / 2] * 2, [y0 - tick, y0 + tick], color=INK, lw=1.6, zorder=9)
    for k, t in enumerate(['0', f'{km // 2}', f'{km} km']):
        ax.text(x0 + k * L / 2, y0 + tick * 2, t, fontsize=11 * size, ha='center', va='bottom', color=INK, zorder=9)
    ax.text(x0, y0 - tick * 2, 'Polar stereographic, scale true at 71°S', fontsize=9 * size, color=MUTED, va='top', ha='left', zorder=9)
