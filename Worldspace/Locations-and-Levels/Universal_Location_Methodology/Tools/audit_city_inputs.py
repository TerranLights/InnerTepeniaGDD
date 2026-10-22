#!/usr/bin/env python3
"""
AUDIT CITY INPUTS  —  does each city have every input the ULM requires, and do its Pre-Trip sheet and datasheets carry them?
(November To-Do, completeness review, 2026-10-21.)  READ-ONLY: it writes nothing but the report you ask for.

  usage:  python3 audit_city_inputs.py [--city KEY ...] [--scope november|all] [--out FILE]

  --scope november   the 30 cities in the November run (default).   all = every key in build_pretrip.py's table.

WHAT IT TESTS  (the presence tests of ULM_Input_Required_Reference.md, run mechanically; "mention" is never counted as "membership")
  T0-1..4   spec exists with a header · Geographic Basis + `Based on:` · census entry · `Arcanet Subnet:` field
  T1-G2     Annual Climate: a real monthly table AND the Precipitation-regime block · the climate READER file: absent / stub / dataset
  T1-G3     `Significance:` · a non-stub Economy & Industry section · the city's OWN row in Division_of_Industry/16 (not a mention)
  T1-G4     the city's row in Founding_Register.md (and its status) · spec `Founding population:` and `Settled:`
  T1-G5     `Access type:` in the closed set · named in Highways / Airports / Ports
  T1-G6     named in the universe repo's World_History_Reference or Timeline Eras (a known canon gap for some cities)
  T1-G7     `Based on:` · an entry with tiered picks in Inspirational-Influences.md
  T1-G8     census composition tier table · census Section A entry
  T2        cultures file / robot-culture file / enneagram file exist (read-last or withheld: existence only) · relationship files
            name the city · concept art holds real images · extent figure or coastline ruling
  PRE-TRIP  the sheet exists; its own verification block shows MISSING-INPUT=0 and 0 failed line claims; the ledger exists
  DATASHEETS  19 files, none a stub (< 8 lines), the DRAFT marking present, README row present

WHAT IT DOES NOT DO: judge quality, read withheld culture material (existence only), or compare one city with another.
"""
import argparse
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_pretrip as bp  # noqa: E402

CITIES, INFRA, PASSES, REPO = bp.CITIES, bp.INFRA, bp.PASSES, bp.REPO
OUT_OF_SCOPE = {"Concordia", "Relung_Panen", "Amundsen_Station", "Shirayuki", "Sinheung", "Zhongshan_Opus", "Zhongshan_Sonnet", "Davis"}
UNIVERSE = "/home/kuroskalacs/Documents/Doll-Fi/media/Reference/TepenianUniverseTimeline"


import unicodedata


def fold(s):
    s = unicodedata.normalize("NFKD", s)
    return "".join(ch for ch in s if not unicodedata.combining(ch))


def rd(p):
    return bp.read_lines(p) if os.path.isfile(p) else None


def section(ls, head_rx, level_rx=r"^#{1,2} "):
    """Lines of the section whose heading matches head_rx, up to the next heading of the same or higher level."""
    if ls is None:
        return None
    for i, ln in enumerate(ls):
        if re.match(head_rx, ln):
            lvl = len(re.match(r"^(#+)", ln).group(1))
            j = i + 1
            while j < len(ls) and not (re.match(r"^(#+) ", ls[j]) and len(re.match(r"^(#+)", ls[j]).group(1)) <= lvl):
                j += 1
            return ls[i:j]
    return None


def field(ls, name):
    if ls is None:
        return None
    for ln in ls[:60]:
        m = re.match(r"^\*\*%s:\*\*\s*(.*)" % re.escape(name), ln)
        if m:
            return m.group(1).strip()
    return None


def audit(key):
    ctx = bp.Ctx(key)
    R = []          # (id, status, note)   status: OK · GAP · NOTE

    def add(i, st, note=""):
        R.append((i, st, note))

    spec = rd(ctx.spec)
    # ---- T0
    if spec is None:
        add("T0-1 spec exists", "GAP", "no spec file at %s" % os.path.relpath(ctx.spec, CITIES))
    else:
        hdr = spec[0].startswith("# ")
        add("T0-1 spec exists", "OK" if hdr else "GAP", "%d lines%s" % (len(spec), "" if hdr else "; no `# ` header"))
    based = field(spec, "Based on")
    gb = section(spec, r"^## Geographic Basis")
    add("T0-2 Geographic Basis + `Based on:`", "OK" if (based and gb and len(gb) > 3 and "TBD" not in (based or "")[:10]) else "GAP",
        "Based on: %s" % ((based or "MISSING")[:70]))
    cd = bp.census_data(ctx)
    add("T0-3 census entry", "OK" if cd["heading"] else "GAP", "entry L%s" % (cd["entry"][0] if cd["entry"] else "-"))
    if cd["rows1"] and cd["rows2"]:
        add("T0-3 census rows (Census I / II)", "OK", "Census I rows %d · Census II rows %d" % (len(cd["rows1"]), len(cd["rows2"])))
    elif cd["rows1"]:
        add("T0-3 census rows (Census I / II)", "NOTE", "Census I row present; NO Census II row. The census states why (Official_Population_Census.md L634: Census II figures not computed for Byrd and Vostok; none for the all-robot cities). Census I governs (DR-4), so not blocking")
    else:
        add("T0-3 census rows (Census I / II)", "GAP", "no Census I row")
    sub = field(spec, "Arcanet Subnet")
    add("T0-4 `Arcanet Subnet:`", "OK" if sub else "GAP", (sub or "MISSING")[:60])

    # ---- T1-G2 climate
    clim = section(spec, r"^### Annual Climate", ) if spec else None
    if clim is None:
        clim = section(spec, r"^## .*Climate")
    txt = "\n".join(clim) if clim else ""
    has_table = bool(re.search(r"^\|\s*Jan\s*\|", "\n".join(spec or []), re.M))
    has_regime = "Precipitation regime" in "\n".join(spec or [])
    add("T1-G2 spec monthly table", "OK" if has_table else "GAP", "" if has_table else "no `| Jan |` row in the spec (a stub or placeholder climate file)")
    add("T1-G2 spec Precipitation-regime block", "OK" if has_regime else "GAP", "")
    rd_ = rd(ctx.reader)
    if rd_ is None:
        add("T1-G2 climate READER file", "NOTE", "no READER file (%s.md); check whether a real absence is documented" % ctx.c["reader"])
    else:
        real = any(re.match(r"^\|\s*Jan\b", l) for l in rd_) or len(rd_) > 25
        add("T1-G2 climate READER file", "OK" if real else "GAP", "%d lines%s" % (len(rd_), "" if real else " — a status stub, not a dataset"))

    # ---- T1-G3
    sig = field(spec, "Significance")
    add("T1-G3 `Significance:`", "OK" if sig else "GAP", "")
    eco = section(spec, r"^## Economy")
    eco_txt = " ".join(l for l in (eco or [])[1:] if l.strip() and l.strip() != "---")
    d16 = bp.di16_data(ctx)
    thin = (not eco) or re.search(r"\bTBD\b", eco_txt) or len(eco_txt) < 450
    if not eco:
        add("T1-G3 Economy & Industry section", "GAP" if not d16["row"] else "NOTE", "no section")
    elif thin:
        add("T1-G3 Economy & Industry section", "NOTE" if d16["row"] else "GAP",
            "partial (%d chars%s); the city's economic figures come from its own row in Division_of_Industry/16" % (len(eco_txt), ", says TBD" if re.search(r"\bTBD\b", eco_txt) else ""))
    else:
        add("T1-G3 Economy & Industry section", "OK", "%d chars" % len(eco_txt))
    add("T1-G3 own row in Division_of_Industry/16 (membership, not mention)", "OK" if d16["row"] else "GAP",
        "row L%s" % d16["row"] if d16["row"] else "no per-city row (a mention does not count)")

    # ---- T1-G4
    reg = rd(os.path.join(CITIES, "Founding_Register.md"))
    reg_row = None
    for i, ln in enumerate(reg or [], 1):
        if ln.startswith("|") and len(ln.split("|")) > 5:
            c0 = re.sub(r"[*`{}]", "", ln.split("|")[1]).strip()
            if fold(c0) in [fold(n) for n in [ctx.name] + ctx.former]:
                reg_row = (i, ln.split("|")[4].strip())
                break
    if reg_row and "✅" in reg_row[1]:
        st, note = "OK", "row L%d, status %s" % reg_row
    elif reg_row:
        st, note = "GAP", "row L%d, status %s (NOT ruled)" % reg_row
    else:
        st, note = "GAP", "no row in Founding_Register.md"
    add("T1-G4 Founding Register row ruled", st, note)
    add("T1-G4 spec `Founding population:`", "OK" if field_any(spec, "Founding population") else "GAP", "")
    add("T1-G4 spec `Settled:`", "OK" if field_any(spec, "Settled") else "GAP", "")

    # ---- T1-G5
    at = field(spec, "Access type")
    tok = re.match(r"(ON|SPUR|SEA-LINK|NONE)\b", at or "")
    add("T1-G5 `Access type:` token", "OK" if tok else "GAP", (at or "MISSING")[:50])
    for fn in ("Highways.md", "Airports.md", "Ports.md"):
        h = ctx.hits(os.path.join(INFRA, fn))
        add("T1-G5 named in %s" % fn, "OK" if h else "NOTE", ("%d lines" % len(h)) if h else "no mention (may be correct: not every city has an airport or port)")

    # ---- T1-G6
    g6 = 0
    for p in [os.path.join(UNIVERSE, "Reference", "World_History_Reference.md")] + glob.glob(os.path.join(UNIVERSE, "Timeline Eras", "2 *", "*.md")):
        h = ctx.hits(p)
        g6 += len(h or [])
    add("T1-G6 named in universe history / Second Interwar era files", "OK" if g6 else "NOTE", "%d hit lines" % g6 if g6 else "named in neither (a known canon gap for some cities, not an addressing error)")

    # ---- T1-G7
    ii = rd(os.path.join(CITIES, "Inspirational-Influences.md"))
    ent = None
    for i, ln in enumerate(ii or []):
        if re.match(r"^#{4,5} ", ln) and fold(re.sub(r"[#*`{}\s]+", " ", ln).strip()) in [fold(n) for n in [ctx.name] + ctx.former + [ctx.name.replace(" ", "")]]:
            ent = i
            break
    if ent is not None:
        j = ent + 1
        while j < len(ii) and not re.match(r"^#{1,5} ", ii[j]):
            j += 1
        body = "\n".join(ii[ent:j])
        tiers = sum(body.count(t) for t in ("[PRIMARY]", "[SECONDARY]", "[SUPPORTING]"))
        add("T1-G7 Inspirational-Influences entry with tiered picks", "OK" if tiers else "GAP", "%d tiered picks" % tiers)
    else:
        add("T1-G7 Inspirational-Influences entry with tiered picks", "GAP", "no entry found under the city's name")

    # ---- T1-G8
    add("T1-G8 composition tier table (census entry)", "OK" if cd["entry"] else "GAP", "")
    uei = ctx.hits(os.path.join(CITIES, "Upper_Earth_Immigration_Composition.md"))
    add("T1-G8 Upper_Earth_Immigration_Composition names the city", "OK" if uei else "NOTE", "%d lines" % len(uei) if uei else "no mention")

    # ---- T2
    add("T2-1 Local_Cultures file (read LAST, existence only)", "OK" if bp.ex(ctx.culture) else "NOTE", "")
    add("T2-1 Megasheet folder (WITHHELD, existence only)", "OK" if bp.ex(ctx.mega_dir) else "NOTE", "")
    add("T2-5 Local_Robot_Culture file", "OK" if bp.ex(ctx.robot) else "GAP", "" if bp.ex(ctx.robot) else "no robot-culture sheet (read at Step 5)")
    add("T2-5 Enneagram personality file", "OK" if bp.ex(ctx.enn) else "NOTE", "")
    for fn in ("City_Relationship_Database.md", "City_Cross_Subnet_Relationships.md", "City_National_Connections.md"):
        h = ctx.hits(os.path.join(CITIES, fn))
        add("T2-6 named in %s" % fn, "OK" if h else "NOTE", "%d lines" % len(h) if h else "no mention")
    imgs = []
    if os.path.isdir(ctx.concept):
        for root, _, fs in os.walk(ctx.concept):
            imgs += [f for f in fs if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".gif"))]
    add("T2-7 concept art holds real images", "OK" if imgs else "NOTE", "%d image files" % len(imgs) if imgs else "empty or missing folder (optional input)")
    ext = bp.extent_data(ctx)
    add("T2-8 extent / area (own row or coastline ruling)", "OK" if (ext["rows"] or ext["others"]) else "NOTE",
        "rows %s / other lines %s" % (len(ext["rows"]), len(ext["others"])))
    add("Neo-race catalog exists", "OK" if bp.ex(ctx.neo) else "NOTE", "")

    # ---- Pre-Trip and datasheets
    pt = os.path.join(ctx.pass_dir, "00.0_Pre-Trip_Inspection.md")
    ptl = rd(pt)
    if ptl is None:
        add("PRE-TRIP sheet exists", "GAP", "")
    else:
        t = "\n".join(ptl)
        m = re.search(r"MISSING-INPUT=(\d+)", t)
        mi = int(m.group(1)) if m else None
        m2 = re.search(r"(\d+) claims . (\d+) OK . (\d+) FAIL", t)
        add("PRE-TRIP sheet exists", "OK", "%d lines" % len(ptl))
        add("PRE-TRIP verification: no missing inputs", "OK" if mi == 0 else ("GAP" if mi else "NOTE"),
            "MISSING-INPUT=%s" % mi if mi is not None else "no verification count in the sheet")
        add("PRE-TRIP verification: line claims all OK", "OK" if (m2 and m2.group(3) == "0") else ("GAP" if m2 else "NOTE"),
            "%s claims, %s fail" % (m2.group(1), m2.group(3)) if m2 else "no count in the sheet")
    add("Position-Coverage ledger exists", "OK" if bp.ex(os.path.join(ctx.pass_dir, "00.2_Position_Coverage_Ledger.md")) else "GAP", "")
    dsd = os.path.join(ctx.pass_dir, "Datasheets")
    fs = sorted(glob.glob(os.path.join(dsd, "*.md")))
    add("DATASHEETS: 19 files", "OK" if len(fs) == 19 else "GAP", "%d files" % len(fs))
    def by_design(f):
        s = "\n".join(rd(f) or [])
        return ("DELIBERATELY EMPTY" in s or "STRUCTURALLY BLOCKED" in s or "Tier U" in s[:600])
    empty_by_design = {f for f in fs if by_design(f)}
    small = [os.path.basename(f) for f in fs if len(rd(f) or []) < 8 and f not in empty_by_design]
    add("DATASHEETS: none a stub", "OK" if not small else "GAP", "stubs: %s" % ", ".join(small) if small else "")
    nodraft = [os.path.basename(f) for f in fs if "DRAFT" not in "\n".join(rd(f) or []) and f not in empty_by_design]
    add("DATASHEETS: DRAFT marking on every file", "OK" if not nodraft else "GAP", "missing in: %s" % ", ".join(nodraft) if nodraft else "")
    rm = rd(os.path.join(ctx.pass_dir, "README.md"))
    add("README has the Datasheets row", "OK" if rm and any("Datasheets" in l for l in rm) else "NOTE", "")
    return ctx, R


def field_any(spec, name):
    if spec is None:
        return None
    for ln in spec:
        if re.match(r"^\*\*%s:\*\*" % re.escape(name), ln):
            return ln
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--city", nargs="*")
    ap.add_argument("--scope", default="november")
    ap.add_argument("--out")
    a = ap.parse_args()
    keys = a.city or [k for k in bp.CITY if a.scope == "all" or k not in OUT_OF_SCOPE]
    out = []
    summary = []
    for k in keys:
        ctx, R = audit(k)
        gaps = [r for r in R if r[1] == "GAP"]
        notes = [r for r in R if r[1] == "NOTE"]
        summary.append((ctx.name, len(R), len(gaps), len(notes), gaps))
        out.append("\n## %s  (%s)\n" % (ctx.name, k))
        out.append("| Test | Result | Detail |\n|---|---|---|")
        for i, st, note in R:
            out.append("| %s | %s | %s |" % (i, {"OK": "ok", "GAP": "**GAP**", "NOTE": "note"}[st], note.replace("|", "/")))
    head = ["# City input audit — raw output", "", "Generated by `Tools/audit_city_inputs.py`. **ok** = present; **GAP** = a required input or built file is missing or is a stub; **note** = absent but optional, or may be correct.", "",
            "| City | Tests | GAPS | Notes |", "|---|--:|--:|--:|"]
    for n, t, g, no, _ in summary:
        head.append("| %s | %d | %d | %d |" % (n, t, g, no))
    head.append("")
    text = "\n".join(head + out) + "\n"
    if a.out:
        open(a.out, "w", encoding="utf-8").write(text)
        print("wrote", a.out)
    for n, t, g, no, gaps in summary:
        print("%-22s tests %-3d GAP %-2d note %-2d" % (n, t, g, no))
        for i, st, note in gaps:
            print("      GAP  %s — %s" % (i, note))
    return 0


if __name__ == "__main__":
    sys.exit(main())
