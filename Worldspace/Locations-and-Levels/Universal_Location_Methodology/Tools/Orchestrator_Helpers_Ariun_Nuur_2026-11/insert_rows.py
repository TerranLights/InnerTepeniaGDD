#!/usr/bin/env python3
"""Insert this city's ten rows into the cross-city differentiation table, WRITE-ONLY (runbook L2934, M-272).
usage: insert_rows.py <table.md> <rows.json> [--dry]
rows.json: {"1": "| Ariun Nuur | ... |", ..., "10": "..."}
For each section N it finds the heading '# N. ...', the first table header row after it, asserts the header starts with '| City |'
and that the new row has the same number of cells, then inserts the row after the section's last table row.
It prints only section numbers, heading TEXT, column counts and insertion line numbers; never another row's content."""
import sys, json, re
tab, rows_path = sys.argv[1], sys.argv[2]; dry = "--dry" in sys.argv
L = open(tab).read().split("\n")
rows = json.load(open(rows_path))
def cells(l): return l.strip().strip("|").count("|") + 1
inserts = []
for n in range(1, 11):
    h = next(i for i, l in enumerate(L) if re.match(rf"^# {n}\. ", l))
    hdr = next(i for i in range(h + 1, len(L)) if L[i].startswith("| City |"))
    assert L[hdr + 1].startswith("|---") or L[hdr + 1].startswith("|:-") or set(L[hdr + 1].replace("|", "").strip()) <= set("-: "), f"no separator after header, section {n}"
    j = hdr + 1
    while j + 1 < len(L) and L[j + 1].startswith("|"): j += 1
    new = rows[str(n)]
    assert new.startswith("| Ariun Nuur |"), f"row {n} must start with the city"
    assert cells(new) == cells(L[hdr]), f"section {n}: row has {cells(new)} cells, header has {cells(L[hdr])}"
    assert not any(l.startswith("| Ariun Nuur |") for l in L[hdr:j + 1]), f"section {n}: a row for this city already exists"
    inserts.append((j + 1, new))
    print(f"section {n}: heading '{L[h][:60]}' · header cells {cells(L[hdr])} · insert after line {j + 1}")
if not dry:
    for pos, new in sorted(inserts, reverse=True): L.insert(pos, new)
    open(tab, "w").write("\n".join(L)); print("written:", len(inserts), "rows")
