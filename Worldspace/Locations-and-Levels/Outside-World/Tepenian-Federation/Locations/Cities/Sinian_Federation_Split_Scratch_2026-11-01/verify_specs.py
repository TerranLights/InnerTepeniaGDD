#!/usr/bin/env python3
"""Check the written specs against final_tables.json and against each spec's own header census numbers."""
import json, re, sys
from pathlib import Path
from apply_final import SPEC_PATH
HERE = Path(__file__).resolve().parent
d = json.load(open(HERE / 'final_tables.json', encoding='utf-8'))['cities']
bad = 0
for city, x in d.items():
    p = HERE.parent / 'Specs' / SPEC_PATH[city]
    L = p.read_text(encoding='utf-8').split('\n')
    h = next(i for i, l in enumerate(L) if re.match(r'^\| *Tier *\| *Nation *\|', l))
    ncols = len(L[h].strip().strip('|').split('|')) - 3
    rows = []
    i = h + 2
    while L[i].startswith('|'):
        cells = [c.strip() for c in L[i].strip().strip('|').split('|')]
        nm = re.sub(r'\s*\*\(.*\)\*$', '', cells[1])
        cnt = [int(c.replace(',', '')) if re.fullmatch(r'[\d,]+', c) else None for c in cells[3:]]
        rows.append((cells[0], nm, float(cells[2].rstrip('%')), cnt))
        i += 1
    jr = {r['nation']: r for r in x['rows']}
    if len(rows) != len(jr):
        print('ROWCOUNT', city, len(rows), len(jr)); bad += 1
    for t, nm, sh, cnt in rows:
        j = jr[nm]
        if cnt != j['counts'][:ncols] or t != j['tier']:
            print('MISMATCH', city, nm, cnt, j['counts'][:ncols], t, j['tier']); bad += 1
    sums = [sum((r[3][k] or 0) for r in rows) for k in range(ncols)]
    txt = '\n'.join(L)
    m = re.search(r'\*\*Census I[^:]*:\*\* ([\d,]+) humans / ([\d,]+) robots', txt)
    m2 = re.search(r'\*\*Census II[^:]*:\*\* ([\d,]+) humans / ([\d,]+) robots', txt)
    hdr = []
    if m: hdr += [int(m.group(2).replace(',', '')), int(m.group(1).replace(',', ''))]
    if m2: hdr += [int(m2.group(2).replace(',', '')), int(m2.group(1).replace(',', ''))]
    ok = (sums[:len(hdr)] == hdr) if hdr else None
    shsum = sum(r[2] for r in rows)
    print(f"{city:18s} cols {sums} header(robots,humans,...) {hdr}  {'OK' if ok else ('NO HEADER' if ok is None else 'DIFF')}  share sum {shsum:.2f}")
    if ok is False: bad += 1
print('problems:', bad)
