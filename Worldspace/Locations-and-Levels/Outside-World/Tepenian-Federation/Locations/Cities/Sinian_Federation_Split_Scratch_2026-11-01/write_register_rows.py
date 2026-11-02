#!/usr/bin/env python3
"""Add the city's Founding Register row to its Phase_2 datasheet and to its Pre-Trip's Phase 2 table; close the Pre-Trip's
open row. 2026-11-02 (DR-86, developer: 'all as recommended'). usage: python3 write_register_rows.py [--apply]"""
import glob, os, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from write_datasheet_tiers import DIRKEY, PASSES
CIT = HERE.parent
REG = CIT / "Founding_Register.md"
ABS = str(REG)
apply = "--apply" in sys.argv
RL = REG.read_text(encoding="utf-8").split("\n")
reg = {}
for i, l in enumerate(RL):
    if l.startswith("| ") and not l.startswith("| City") and not l.startswith("|---"):
        c = [x.strip() for x in l.strip().strip("|").split(" | ")]
        if len(c) >= 8:
            reg[c[0]] = (i + 1, c)
log = []
for d in sorted(glob.glob(str(PASSES / "*" / "*"))):
    folder = os.path.basename(d)
    key = DIRKEY.get(folder)
    if key is None:
        continue
    if key not in reg:
        log.append(("NO REGISTER ROW", key)); continue
    n, c = reg[key]
    founders, basis, src, notf = c[4], c[5], c[6], c[7]
    # ---- datasheet
    f = os.path.join(d, "Datasheets", "Phase_2.md")
    if os.path.exists(f):
        L = open(f, encoding="utf-8").read().split("\n")
        if not any(l.startswith("| Founding Register row") for l in L):
            i = next((k for k, l in enumerate(L) if l.startswith("| Composition tier")), None)
            if i is None:
                log.append(("no composition row in datasheet", key))
            else:
                while i + 1 < len(L) and L[i + 1].startswith("|"):
                    i += 1
                row = (f"| Founding Register row — the only source of founders (`DR-19`) | **Founders:** {founders} · **Basis:** {basis} · "
                       f"**Ruling:** {src} · **Not founders:** {notf} | `{ABS}` L{n} |")
                L.insert(i + 1, row)
                if apply:
                    open(f, "w", encoding="utf-8").write("\n".join(L))
                log.append(("datasheet row", key))
    # ---- pre-trip
    f = os.path.join(d, "00.0_Pre-Trip_Inspection.md")
    if os.path.exists(f):
        L = open(f, encoding="utf-8").read().split("\n")
        t = "\n".join(L)
        if "Founding Register — the city's own row" in t:
            continue
        i = next((k for k, l in enumerate(L) if l.startswith("| **2** | **P** Census")), None)
        j = next((k for k, l in enumerate(L) if l.startswith("| **Founding Register not in the Phase 2 table**")), None)
        m = re.search(r"(🧪 `T8` — \*\*Phase 2:\*\* the )(\d+)( admissible rows)", t)
        if i is None or m is None:
            log.append(("pre-trip pattern missing", key, i, j, bool(m))); continue
        newrow = f"| **2** | **P** Founding Register — the city's own row | `{ABS}` | ✅ | `MAPPED` | Row L{n} (founders, basis, ruling, ruled-out nations). Added 2026-11-02 (developer, `DR-86`) |"
        cells = L[j].split(" | ") if j is not None else []
        if j is not None: L[j] = " | ".join([cells[0], "✅ Closed 2026-11-02 (developer, `DR-86`)", "The Register's row is now in the Phase 2 table above and in the Phase 2 datasheet; the `T8` count below is one higher |"])
        L.insert(i + 1, newrow)
        t = "\n".join(L)
        t = re.sub(r"(🧪 `T8` — \*\*Phase 2:\*\* the )(\d+)( admissible rows)", lambda mm: f"{mm.group(1)}{int(mm.group(2)) + 1}{mm.group(3)}", t, count=1)
        if apply:
            open(f, "w", encoding="utf-8").write(t)
        log.append(("pre-trip", key))
import collections
print(collections.Counter(x[0] for x in log), [x for x in log if x[0] not in ("datasheet row", "pre-trip")], "APPLIED" if apply else "dry run")
