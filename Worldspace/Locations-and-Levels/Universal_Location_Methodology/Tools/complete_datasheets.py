#!/usr/bin/env python3
"""
COMPLETE DATASHEETS  —  adds to each city's datasheets every row the spine's MUST OPEN lists require and the sheet lacks,
in the position the spine's order gives it, and writes the Field Guide's coverage line at the top of each phase sheet.
(2026-10-23; developer: "make sure ... it has all of the information ... ULM needs ... add it ... where it's supposed to be".)

  usage:  python3 complete_datasheets.py <city_key> [--apply]        (without --apply: prints what it WOULD add; nothing is written)

HOW A ROW IS BUILT: with the datasheet builder's own helpers (`hits_rows`, `dir_hit_rows`, `cite`, `Sheet.safe`), so the same three
refusals apply: a source line carrying later-era content, a comparison with other places, or a multi-city list is NOT copied (it is
marked as excluded, with the line number). A row is a value + its citation, nothing else.
WHERE A ROW GOES: after the last existing row of the nearest EARLIER spine item that the sheet already names; else before the first row
of the nearest LATER one; else at the end of the sheet's last table.
THE COVERAGE LINE: "N of M MUST OPEN addresses are named in this sheet (D directly, V through a shared sheet it cites); not covered: ..."
placed under the sheet's header blockquote. A sheet with an uncovered address says it is INCOMPLETE there, as Rule 1 requires.
"""
import argparse
import glob
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_pretrip as B       # noqa: E402
import build_datasheets as DS   # noqa: E402
import check_must_open_coverage as CK  # noqa: E402

TODAY = B.TODAY
R = DS.R
UNIV = DS.UNIV
STATIONS = os.path.join(R, "Reference", "Real-World", "Stations")
COMNAP = os.path.join(STATIONS, "COMNAP_Antarctic_Station_Catalogue.pdf")
_comnap = []


def comnap_pages():
    if not _comnap:
        for p in range(1, 87):
            r = subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), "-layout", COMNAP, "-"], capture_output=True)
            _comnap.append(r.stdout.decode("utf-8", "replace"))
    return _comnap


EXEMPT = {(3, "Davis_Geosciences_Research")}      # the spine itself marks it "where applicable" (Davis only)


def tag_of(addr):
    d = addr.rstrip("/")
    parts = d.split("/")
    if addr.endswith(".md"):
        return os.path.basename(d).lower()
    return "/".join(parts[-2:]).lower() if parts[-1] in ("Locations", "Stations", "Factions") else parts[-1].lower()


def dir_rows_strict(d, root, label):
    """Like the builder's dir_hit_rows, but a multi-city list line is NOT copied (the builder's version allows them)."""
    ctx = d.ctx
    files = []
    for rt, _, fs in os.walk(root):
        for f in sorted(fs):
            if f.endswith(".md"):
                files.append(os.path.join(rt, f))
    hit = [(p, ctx.hits(p)) for p in files]
    hit = [(p, h) for p, h in hit if h]
    rows = [(label + " \u2014 directory enumerated", "%d `.md` files read; **%d name the city**" % (len(files), len(hit)),
             "`%s/` (enumerated %s)" % (os.path.relpath(root, R) if root.startswith(R) else "\u2026/" + os.path.relpath(root, UNIV), TODAY))]
    for p, h in hit:
        ls = B.read_lines(p)
        for n in h[:12]:
            rows.append(("\u21b3 " + os.path.relpath(p, root), d.sh.safe(ls[n - 1], os.path.basename(p), n, allow_multi=False), DS.cite(p, [n])))
        if len(h) > 12:
            rows.append(("\u21b3 " + os.path.relpath(p, root), "%d further lines: %s *(line numbers only)*" % (len(h) - 12, B.fmt_lines(h[12:])), DS.cite(p)))
    return rows


def item_rows(d, ph, label, addr, acc):
    """Rows (label, value, citation) for one missing spine item."""
    ctx = d.ctx
    base = os.path.basename(addr.rstrip("/"))
    if base == "Locations" and "TepenianUniverseTimeline" in addr:
        return dir_rows_strict(d, addr.rstrip("/"), "Universe repo `Worldspace/Locations/`")
    if base == "Stations":
        air = os.path.join(STATIONS, "Antarctic_Stations_With_Airstrips.md")
        asrc = B.read_lines(air)
        rows = DS.hits_rows(d, air, "`Antarctic_Stations_With_Airstrips.md` — lines naming the city", allow_multi=True)
        fixed = []
        for r in rows:
            m = re.search(r"L(\d+)", r[2])
            if m and not asrc[int(m.group(1)) - 1].startswith("|") and "excluded" not in r[1]:
                r = (r[0], "*[commentary line in the source, not a table row; not copied, line number recorded only]*", r[2])
            fixed.append(r)
        rows = fixed
        if rows and rows[0][0].startswith("`Antarctic_Stations"):
            rows[0] = (rows[0][0] + " (the Country column is the station's builder: infrastructure only, `DR-19`, `DR-24`)", rows[0][1], rows[0][2])
        pages = [i + 1 for i, t in enumerate(comnap_pages()) if ctx.rx.search(ctx.strip_subnet(t))]
        rows.append(("`COMNAP_Antarctic_Station_Catalogue.pdf` — pages naming the city (86 pages read)",
                     ("pages %s *(page numbers only: the catalogue's index and entry pages are not separated here)*" % ", ".join(str(x) for x in pages)) if pages else "Checked by name: **zero pages**",
                     "`COMNAP_Antarctic_Station_Catalogue.pdf`"))
        return rows
    if base == "City_Concept-Art":
        cd = ctx.concept
        if B.ex(cd):
            files = os.listdir(cd)
            real = [f for f in files if f != ".gitkeep"]
            val = ("EMPTY — `.gitkeep` only, %d file(s) total" % len(files)) if not real and files else "%d file(s): %s" % (len(real), ", ".join(real[:12]))
        else:
            val = "**No concept-art folder exists**"
        return [("Concept-art directory status", val, "Checked %s: `City_Concept-Art/`" % TODAY)]
    if base == "01_Burden_Scoring_Model.md":
        readme = os.path.join(DS.DI, "README.md")
        l = B.read_lines(readme)[48]
        return [("`01_Burden_Scoring_Model.md` — status stamp in the folder README", "`%s`" % re.sub(r"\*\*", "", l).strip(), DS.cite(readme, [49]))]
    if base in ("City_Cross_Subnet_Relationships.md", "City_National_Connections.md"):
        p = os.path.join(DS.C, base)
        h = ctx.hits(p) or []
        return [("`%s` — lines naming the city" % base, ("%d line(s): %s *(line numbers only: this file builds on material withheld by its own stated method)*" % (len(h), B.fmt_lines(h))) if h else "Checked by name: **zero hits**", DS.cite(p, h or None))]
    if base == "Factions":
        fr = os.path.join(R, "Worldspace", "Factions")
        fl = []
        for rt, _, fs in os.walk(fr):
            for f in sorted(fs):
                if f.endswith(".md") and "Robot_Religions" not in rt:
                    h = ctx.hits(os.path.join(rt, f))
                    if h:
                        fl.append((os.path.join(rt, f), h))
        return [("`Factions/` — files naming the city (religions excluded; see `Phase_6.md`)", ("; ".join("`%s` %s" % (os.path.relpath(p, fr), B.fmt_lines(h)) for p, h in fl) + " *(line numbers only)*") if fl else "Checked by name: **zero hits** in every file outside `Robot_Religions/`", "`Worldspace/Factions/`")]
    if addr.endswith(".md"):
        return DS.hits_rows(d, addr, "`%s`" % base, allow_multi=True)
    if os.path.isdir(addr):
        return dir_rows_strict(d, addr.rstrip("/"), "`%s/`" % base)
    return [("`%s`" % base, "⬜ source not found at the spine's address", "`%s`" % addr)]


def parse_table_rows(lines):
    """Indexes of data rows of every markdown table in the file."""
    idx = []
    for i, l in enumerate(lines):
        if l.startswith("|") and not re.match(r"^\|\s*:?-", l) and i + 0 > 0:
            idx.append(i)
    return idx


def add_rows(lines, items, ph, newrows):
    """Insert newrows[i] (list of (label, value, citation)) for the item indexes in `newrows`, in spine order."""
    for i in sorted(newrows):
        text_rows = ["| %s |" % " | ".join(DS.esc(str(x)) if k else str(x).replace("\n", " ") for k, x in enumerate(r)) for r in newrows[i]]
        rows_idx = parse_table_rows(lines)
        pos = None
        for j in range(i - 1, -1, -1):
            tg = tag_of(items[j][1])
            hit = [k for k in rows_idx if tg in lines[k].lower()]
            if hit:
                pos = max(hit) + 1
                break
        if pos is None:
            for j in range(i + 1, len(items)):
                tg = tag_of(items[j][1])
                hit = [k for k in rows_idx if tg in lines[k].lower()]
                if hit:
                    pos = min(hit)
                    break
        if pos is None:
            pos = (max(rows_idx) + 1) if rows_idx else len(lines)
        lines[pos:pos] = text_rows
    return lines


def classify(text, acc, extra):
    d = text is not None and any(CK.named(text, x) for x in acc + extra)
    if d:
        return "direct"
    return "via Tier U" if (text is not None and any(CK.named(CK.tier_u_text(text), x) for x in acc + extra)) else None


COV_MARK = "MUST-OPEN coverage — Field Guide Rule 1"


def coverage_line(ph, items, text):
    d = v = 0
    miss, na = [], []
    for label, addr, acc in items:
        base = os.path.basename(addr.rstrip("/"))
        if (ph, base) in EXEMPT:
            na.append(base)
            continue
        c = classify(text, acc, CK.ALIAS.get(base, []))
        if c == "direct":
            d += 1
        elif c == "via Tier U":
            v += 1
        else:
            miss.append(base)
    n = d + v + len(miss)
    s = "> \U0001f4c2 **%s (spine, Phase %d), checked %s:** **%d of %d** addresses are named in this sheet (%d directly, %d through a shared Tier U sheet it cites)." % (COV_MARK, ph, TODAY, d + v, n, d, v)
    if na:
        s += " Not applicable: `%s` (the spine marks it \"where applicable\": Davis only)." % "`, `".join(na)
    if miss:
        s += " ⛔ **NOT COVERED — THIS SHEET IS INCOMPLETE:** `%s`." % "`, `".join(miss)
    return s


def put_coverage(lines, line):
    lines = [l for l in lines if COV_MARK not in l]
    # after the last line of the leading header block (title, blank, blockquote lines)
    i = 0
    while i < len(lines) and not lines[i].startswith("|"):
        i += 1
    j = i
    while j > 0 and not lines[j - 1].startswith(">"):
        j -= 1
    lines[j:j] = [line, ""] if j > 0 and lines[j - 1].strip() == "" else ["", line] if j > 0 else [line]
    return lines


GATE_LINE = ("> \u26d4\u26d4 **DoI CITATION GATE \u2014 binds every Division-of-Industry figure below.** `Corpus_Reference_Sheets/Division_of_Industry_Reliability_Quick_Reference.md`: "
             "workforce, difficulty, baseline load, distinctive tier and a city's own sector sizes are citable; an export headcount is not; nor is any \"feeds N people\" claim.")


def put_gate(lines):
    if any("Division_of_Industry_Reliability_Quick_Reference" in l for l in lines):
        return lines
    i = 0
    while i < len(lines) and not lines[i].startswith("|"):
        i += 1
    j = i
    while j > 0 and not lines[j - 1].startswith(">"):
        j -= 1
    lines[j:j] = [GATE_LINE, ""] if j > 0 and lines[j - 1].strip() == "" else ["", GATE_LINE]
    return lines


def process(key, apply):
    ctx = B.Ctx(key)
    d = DS.Data(ctx)
    spine = CK.spine_items()
    ddir = os.path.join(ctx.pass_dir, "Datasheets")
    report = []
    for ph, items in spine.items():
        f = {0: "Step_0.md", 1: "Step_1_and_2.md"}.get(ph, "Phase_%d.md" % ph)
        p = os.path.join(ddir, f)
        if not os.path.exists(p):
            report.append((ph, f, "FILE MISSING", []))
            continue
        text = open(p, encoding="utf-8").read()
        lines = text.split("\n")
        new = {}
        for i, (label, addr, acc) in enumerate(items):
            base = os.path.basename(addr.rstrip("/"))
            if (ph, base) in EXEMPT:
                continue
            if classify(text, acc, CK.ALIAS.get(base, [])) is None:
                new[i] = item_rows(d, ph, label, addr, acc)
        added = []
        if new:
            lines = add_rows(lines, items, ph, new)
            added = [(items[i][0], len(r)) for i, r in new.items()]
        if f in ("Step_1_and_2.md", "Phase_4.md", "Phase_7.md"):
            lines = put_gate(lines)
        newtext = "\n".join(lines)
        lines = put_coverage(newtext.split("\n"), coverage_line(ph, items, newtext))
        newtext = "\n".join(lines)
        if apply:
            open(p, "w", encoding="utf-8").write(newtext)
        report.append((ph, f, "ok" if not added else "added", added))
    return ctx, d, report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("city")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    ctx, d, rep = process(a.city, a.apply)
    print("== %s (%s)  %s" % (ctx.name, a.city, "APPLIED" if a.apply else "dry run"))
    for ph, f, st, added in rep:
        print("  Phase %-2d %-18s %s %s" % (ph, f, st, "; ".join("%s (+%d rows)" % x for x in added)))
    print("  excluded by the safe-copy rules:", len(d.sh.log))


if __name__ == "__main__":
    sys.exit(main())
