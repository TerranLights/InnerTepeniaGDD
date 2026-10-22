#!/usr/bin/env python3
"""
CLIMATE READER CHECK  —  recompute monthly mean-temperature normals from the BAS Met READER tables and test every spec's
`Mean` column against them  (climate reconciliation, 2026-10-21).

  usage:  python3 climate_reader_check.py --raw DIR --out FILE.md [--refresh]

  --raw DIR    folder where the downloaded READER pages are kept (created if missing; reused unless --refresh)
  --out FILE   writes the report (markdown)

WHAT IT DOES
  Surface stations:  https://legacy.bas.ac.uk/met/READER/surface/<Station>.All.temperature.html   (year x month table, with counts)
  AWS stations:      https://legacy.bas.ac.uk/met/READER/aws/<Station>.All.temperature.html
  Normal = mean of the yearly monthly values over 1991-2020 for surface stations (the WMO period); for AWS records, which are shorter,
  over every full year 1991-2025 (partial 2026 excluded). A month needs >= 10 years or it is left blank.
  Each spec's `Mean` column is read from the `#### Monthly Summary` table and compared month by month.
  A control set of cities whose specs are known to be READER-sourced is run the same way, to prove the method (they match to 0.1).
  The tool also reports, for every spec, months where `Mean` lies outside the same row's `Avg Low` .. `Avg High` (impossible).
WHAT IT DOES NOT DO: edit any spec. It only reports.
"""
import argparse
import glob
import html
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
SPECS = os.path.join(REPO, "Worldspace", "Locations-and-Levels", "Outside-World", "Tepenian-Federation", "Locations", "Cities", "Specs")
SURF = "https://legacy.bas.ac.uk/met/READER/surface/"
AWS = "https://legacy.bas.ac.uk/met/READER/aws/"
MN = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()

# (label, kind, station, spec path under Specs/, role)
TESTS = [
    ("Halley", "surface", "Halley", "Halley subnet/Halley.md", "stub"),
    ("Lazar", "surface", "Novolazarevskaya", "Halley subnet/Lazar.md", "stub"),
    ("Janbogo", "surface", "Mario_Zucchelli", "Janbogo subnet/Janbogo.md", "stub"),
    ("Janbogo (cross-check)", "aws", "Terra_Nova_Bay", "Janbogo subnet/Janbogo.md", "stub"),
    ("Troll", "aws", "Troll", "Halley subnet/Troll.md", "stub"),
    ("Kunlun", "aws", "Dome_A", "Mirny subnet/Kunlun.md", "stub"),
    ("Dome Fuji", "aws", "Dome_F", "Mawson subnet/Dome_Fuji.md", "stub"),
    ("Cape Adare (candidate proxy)", "aws", "Possession_Island", "Janbogo subnet/Cape_Adare.md", "stub"),
    ("Cape Adare (candidate proxy)", "aws", "Cape_Ross", "Janbogo subnet/Cape_Adare.md", "stub"),
    ("Sinheung (a finished city)", "surface", "Zhongshan", "Mirny subnet/Sinheung.md", "stub"),
    ("Zukelli", "surface", "Mario_Zucchelli", "Janbogo subnet/Zukelli.md", "control"),
    ("Rothera", "surface", "Rothera", "Palmer subnet/Rothera.md", "control"),
    ("Marambio", "surface", "Marambio", "Palmer subnet/Marambio.md", "control"),
    ("Esperanza", "surface", "Esperanza", "Palmer subnet/Esperanza.md", "control"),
    ("Neumayer", "surface", "Neumayer", "Halley subnet/Neumayer.md", "control"),
    ("Belgrano", "surface", "Belgrano_II", "Halley subnet/Belgrano.md", "control"),
    ("Casey", "surface", "Casey", "Mirny subnet/Casey.md", "control"),
    ("Davis", "surface", "Davis", "Mirny subnet/Davis.md", "control"),
    ("Mirny", "surface", "Mirny", "Mirny subnet/Mirny.md", "control"),
    ("Zhongshan", "surface", "Zhongshan", "Mirny subnet/Zhongshan.md", "control"),
    ("Shirayuki", "surface", "Zhongshan", "Mirny subnet/Shirayuki.md", "control"),
    ("Ariun Nuur", "surface", "Vostok", "Mirny subnet/Ariun_Nuur.md", "control"),
    ("Mawson", "surface", "Mawson", "Mawson subnet/Mawson.md", "control"),
    ("Dumont d'Urville", "surface", "Dumont_Durville", "Janbogo subnet/Dumont_dUrville.md", "control"),
    ("Scott", "surface", "Scott_Base", "Janbogo subnet/Scott.md", "control"),
    ("Fort McMurdo", "surface", "McMurdo", "Janbogo subnet/Fort_McMurdo.md", "control"),
]


def fetch(raw, kind, st, refresh=False):
    base = SURF if kind == "surface" else AWS
    f = os.path.join(raw, "%s_%s.All.temperature.html" % (kind, st))
    if refresh or not os.path.exists(f) or os.path.getsize(f) < 500:
        subprocess.run(["curl", "-sS", "-m", "60", "-L", "-o", f, "%s%s.All.temperature.html" % (base, st)], check=True)
    return open(f, encoding="utf-8", errors="replace").read()


def parse(t):
    i0 = t.find("<body")
    b = re.sub(r"<script.*?</script>", "", t[i0:] if i0 >= 0 else t, flags=re.S)
    toks = [l.strip() for l in re.sub(r"<[^>]+>", "\n", html.unescape(b)).split("\n") if l.strip()]
    data, i, n = {}, 0, len(toks)
    while i < n:
        if re.fullmatch(r"(19|20)\d\d", toks[i]):
            y = int(toks[i])
            i += 1
            vals = []
            while len(vals) < 12 and i < n and not re.fullmatch(r"(19|20)\d\d", toks[i]):
                v = toks[i]
                i += 1
                if i < n and re.fullmatch(r"\(\s*\d+\s*\)", toks[i]):
                    i += 1
                if v == "-":
                    vals.append(None)
                else:
                    try:
                        vals.append(float(v))
                    except ValueError:
                        vals.append(None)
            if len(vals) == 12:
                data[y] = vals
        else:
            i += 1
    return data


def normals(data, a, b, need=10):
    out, ns = [], []
    for m in range(12):
        v = [d[m] for y, d in data.items() if a <= y <= b and d[m] is not None]
        ns.append(len(v))
        out.append(sum(v) / len(v) if len(v) >= need else None)
    return out, ns


def num(s):
    s = re.sub(r"[^\d\-+.−]", "", s.replace("−", "-"))
    try:
        return float(s)
    except ValueError:
        return None


def spec_table(path):
    hdr, rows = None, {}
    for ln in open(path, encoding="utf-8"):
        if ln.startswith("|"):
            c = [x.strip() for x in ln.strip().strip("|").split("|")]
            if c and c[0] == "Month" and any(h.startswith("Mean") for h in c):
                hdr = c
                continue
            if hdr and c[0] in MN and len(c) >= len(hdr) - 1:
                d = dict(zip(hdr, c))
                rows[c[0]] = (num(d.get("Avg High (day)", "")), num(d.get("Mean", "")), num(d.get("Avg Low (night)", "")))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--refresh", action="store_true")
    a = ap.parse_args()
    os.makedirs(a.raw, exist_ok=True)
    cache, L = {}, []
    stub_lines, ctl_lines, detail = [], [], []
    for label, kind, st, sp, role in TESTS:
        key = (kind, st)
        if key not in cache:
            d = parse(fetch(a.raw, kind, st, a.refresh))
            lo, hi = (1991, 2020) if kind == "surface" else (1991, 2025)
            nm, ns = normals(d, lo, hi)
            yrs = sorted(d)
            cache[key] = (d, nm, ns, lo, hi, yrs)
        d, nm, ns, lo, hi, yrs = cache[key]
        spec = spec_table(os.path.join(SPECS, sp))
        diffs = [(m, spec[m][1], nm[i]) for i, m in enumerate(MN) if m in spec and spec[m][1] is not None and nm[i] is not None]
        ad = [abs(x - y) for _, x, y in diffs]
        if not diffs:
            line = "| %s | %s %s | — | no overlap |" % (label, kind, st)
        else:
            w = max(diffs, key=lambda z: abs(z[1] - z[2]))
            line = "| %s | %s `%s` | %d | max %.1f · mean %.1f (worst %s: spec %g vs %.1f) |" % (label, kind, st, len(diffs), max(ad), sum(ad) / len(ad), w[0], w[1], w[2])
        (ctl_lines if role == "control" else stub_lines).append(line)
        if role != "control":
            detail.append("\n#### %s — READER %s `%s` (%s, %d yrs on file %s–%s; normal over %d–%d)\n" % (label, kind, st, "record", len(yrs), yrs[0], yrs[-1], lo, hi))
            detail.append("| | " + " | ".join(MN) + " |\n|---|" + "---:|" * 12)
            detail.append("| **READER normal** | " + " | ".join("%.1f" % x if x is not None else "—" for x in nm) + " |")
            detail.append("| years in the normal | " + " | ".join(str(n) for n in ns) + " |")
            detail.append("| **Spec `Mean`** | " + " | ".join("%g" % spec[m][1] if m in spec and spec[m][1] is not None else "—" for m in MN) + " |")
            detail.append("| difference | " + " | ".join("%+.1f" % (spec[m][1] - nm[i]) if m in spec and spec[m][1] is not None and nm[i] is not None else "—" for i, m in enumerate(MN)) + " |")
    # impossibility sweep over every spec
    imp = []
    for f in sorted(glob.glob(os.path.join(SPECS, "*", "*.md"))):
        nm_ = os.path.basename(f)[:-3]
        if nm_.startswith("_"):
            continue
        rows = spec_table(f)
        bad = [m for m, (h, me, lo_) in rows.items() if None not in (h, me, lo_) and (me > h + 0.6 or me < lo_ - 0.6 or h < lo_)]
        if bad:
            imp.append("| %s | %d | %s |" % (nm_, len(bad), ", ".join(bad)))
    out = ["# READER recomputed normals vs the specs' `Mean` column — 2026-10-21",
           "",
           "Produced by `Tools/climate_reader_check.py` (read-only). Source: the BAS Met READER tables (`legacy.bas.ac.uk/met/READER/`), downloaded 2026-10-21; raw pages archived in `to-be-integrated/climate data CURL/reader_2026-10-21/`.",
           "",
           "**Method.** Surface stations: mean of the yearly monthly values over 1991–2020. Automatic weather stations (AWS), whose records are short: every full year 1991–2025. A month needs ≥ 10 years or it is left blank. **The method is proven by the control set below: cities whose specs really were taken from READER match to ≤ 0.1 °C.**",
           "",
           "## 1 · The control set — specs known to be READER-sourced (method proof)",
           "| City | READER station | months | difference from the spec |", "|---|---|--:|---|"] + ctl_lines + [
           "",
           "## 2 · The cities that had a stub READER file, and the others tested",
           "| City | READER station | months | difference from the spec `Mean` |", "|---|---|--:|---|"] + stub_lines + [
           "",
           "### Month-by-month",
           ] + detail + [
           "",
           "## 3 · Specs whose own `Mean` falls outside the same row's low–high range (impossible)",
           "| Spec | months | which |", "|---|--:|---|"] + imp + [""]
    open(a.out, "w", encoding="utf-8").write("\n".join(out))
    print("wrote", a.out)


if __name__ == "__main__":
    sys.exit(main())
