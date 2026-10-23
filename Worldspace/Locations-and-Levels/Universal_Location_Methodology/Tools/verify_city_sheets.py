#!/usr/bin/env python3
"""
VERIFY CITY SHEETS  —  one city, every check the Field Guide and the Pre-Trip recipe put on that city's sheets, with the evidence.
(2026-10-23.)  Read-only.

  usage:  python3 verify_city_sheets.py <city_key> [--quiet]

CHECKS (each prints PASS / FAIL / NOTE and the evidence)
  Datasheets
    D1  the 19 manifest files exist
    D2  every spine MUST OPEN address of Phases 0-10 is named in that phase's sheet, directly or through a shared sheet it cites
    D3  every phase sheet carries the coverage line (Rule 1)
    D4  Step_5 is the explicit deliberate stub
    D5  Step_6 carries the table's section inventory (ten sections)
    D6  the Division-of-Industry reliability sheet is cited in the Phase 1, 4 and 7 sheets (the carve-out gate)
    D7  no later-era words in any sheet (the Field Guide's sweep list), outside the builder's own marker text
    D8  inference markers (the Field Guide's scan): count and where, to be READ
    D9  every sheet is marked DRAFT (or is a deliberate stub / Tier U pointer)
    D10 every shared (Tier U) sheet a datasheet cites exists
    D11 the city's README carries the Datasheets row
    D12 Step_-1 carries the Specs file's section ranges; Step_0 carries the census rows
  Pre-Trip
    P1  all sections A-N present
    P2  12 step blocks, 11 phase "governing" lines, 11 T8 lines
    P3  every spine MUST OPEN address appears in section D
    P4  every datasheet file is pointed to
    P5  every alias in the city's name set appears in section A
    P6  the verification block reports 0 missing inputs and 0 failed line claims
    P7  no placeholder tokens and no other city's name carried over
    P8  the position-coverage ledger exists
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_pretrip as B       # noqa: E402
import build_datasheets as DS   # noqa: E402
import check_must_open_coverage as CK  # noqa: E402
import complete_datasheets as CD  # noqa: E402

MANIFEST = ["Step_-1.md", "Step_0.md", "Step_1_and_2.md", "Step_3.md", "Step_5.md", "Step_6.md", "Step_7.md", "Step_8.md", "Step_9.md", "Step_10.md"] + ["Phase_%d.md" % i for i in range(2, 11)]
INFER = re.compile(r"⇒|therefore|which means|the real|this is the")


def verify(key):
    ctx = B.Ctx(key)
    res = []

    def add(i, st, note):
        res.append((i, st, note))
    ddir = os.path.join(ctx.pass_dir, "Datasheets")
    miss = [f for f in MANIFEST if not os.path.exists(os.path.join(ddir, f))]
    add("D1 19 manifest files", "PASS" if not miss else "FAIL", "all present" if not miss else "missing: " + ", ".join(miss))
    txt = {f: open(os.path.join(ddir, f), encoding="utf-8").read() for f in MANIFEST if f not in miss}
    spine = CK.spine_items()
    gaps, nocov = [], []
    for ph, items in spine.items():
        f = {0: "Step_0.md", 1: "Step_1_and_2.md"}.get(ph, "Phase_%d.md" % ph)
        t = txt.get(f)
        if t is None:
            continue
        for label, addr, acc in items:
            base = os.path.basename(addr.rstrip("/"))
            if (ph, base) in CD.EXEMPT:
                continue
            if CD.classify(t, acc, CK.ALIAS.get(base, [])) is None:
                gaps.append("P%d %s" % (ph, base))
        if CD.COV_MARK not in t:
            nocov.append(f)
    add("D2 spine MUST OPEN covered", "PASS" if not gaps else "FAIL", "all %d addresses covered" % sum(len(v) for v in spine.values()) if not gaps else "not covered: " + "; ".join(gaps))
    add("D3 coverage line on phase sheets", "PASS" if not nocov else "FAIL", "all 11 carry it" if not nocov else "missing on: " + ", ".join(nocov))
    s5 = txt.get("Step_5.md", "")
    add("D4 Step_5 deliberate stub", "PASS" if re.search(r"DELIBERATELY EMPTY|STRUCTURALLY BLOCKED", s5) else "FAIL", "stub statement present" if re.search(r"DELIBERATELY EMPTY|STRUCTURALLY BLOCKED", s5) else "no stub statement")
    s6 = txt.get("Step_6.md", "")
    pats = ["Capability shape", "Composition & Arrival", "Surface & Texture", "Ordinary Life", "Phase 6 \u2014 Meaning", "Phase 7 \u2014 Order", "Phase 8 \u2014 Making", "Relation & Geometry", "Populations", "Catalog axis"]
    found = [x for x in pats if re.search(re.escape(x), s6, re.I)]
    add("D5 Step_6 section inventory", "PASS" if len(found) == 10 else "FAIL", "ten sections incl. Phase 10" if len(found) == 10 else "found %d of 10: missing %s" % (len(found), ", ".join(x for x in pats if x not in found)))
    gate = [f for f in ("Step_1_and_2.md", "Phase_4.md", "Phase_7.md") if f in txt and "Division_of_Industry_Reliability_Quick_Reference" not in txt[f]]
    add("D6 DoI reliability gate cited (Phases 1, 4, 7)", "PASS" if not gate else "FAIL", "cited in all three" if not gate else "not cited in: " + ", ".join(gate))
    war = []
    for f, t in txt.items():
        for n, l in enumerate(t.split("\n"), 1):
            if DS.WAR.search(l) and "excluded" not in l and "not copied" not in l.lower() and "FLAGGED" not in l and not l.startswith("> ⛔"):
                war.append("%s L%d" % (f, n))
    add("D7 later-era words", "PASS" if not war else "NOTE", "none outside marker text" if not war else "%d line(s) to READ: %s" % (len(war), "; ".join(war[:8])))
    inf = []
    for f, t in txt.items():
        for n, l in enumerate(t.split("\n"), 1):
            if INFER.search(l) and l.startswith("|"):
                inf.append("%s L%d" % (f, n))
    add("D8 inference markers (read, never strip)", "NOTE" if inf else "PASS", ("%d table row(s): %s" % (len(inf), "; ".join(inf[:8]))) if inf else "none")
    nod = [f for f, t in txt.items() if "DRAFT" not in t and not re.search(r"DELIBERATELY EMPTY|STRUCTURALLY BLOCKED|Tier U", t[:700])]
    add("D9 DRAFT marking", "PASS" if not nod else "FAIL", "all marked" if not nod else "unmarked: " + ", ".join(nod))
    missu = []
    for f, t in txt.items():
        for nm in set(re.findall(r"([A-Za-z0-9_\-]+_Quick_Reference\.md)", t)):
            if not os.path.exists(os.path.join(B.ULM, "Corpus_Reference_Sheets", nm)):
                missu.append(nm)
    add("D10 shared sheets cited exist", "PASS" if not missu else "FAIL", "all exist" if not missu else "missing: " + ", ".join(sorted(set(missu))))
    rm = os.path.join(ctx.pass_dir, "README.md")
    add("D11 README Datasheets row", "PASS" if os.path.exists(rm) and "Datasheets" in open(rm, encoding="utf-8").read() else "FAIL", "")
    m1 = txt.get("Step_-1.md", "")
    c0 = txt.get("Step_0.md", "")
    ok12 = bool(re.search(r"L\d+", m1)) and ("Census" in c0 or "census" in c0)
    add("D12 Step_-1 spec ranges and Step_0 census rows", "PASS" if ok12 else "FAIL", "line-range citations present; census named" if ok12 else "check by hand")
    # ---- Pre-Trip
    pf = os.path.join(ctx.pass_dir, "00.0_Pre-Trip_Inspection.md")
    if not os.path.exists(pf):
        add("P1 Pre-Trip exists", "FAIL", "no file")
        return ctx, res
    pt = open(pf, encoding="utf-8").read()
    secs = [c for c in "ABCDEFGHIJKLMN" if re.search(r"^## (?:\U0001f9ea )?%s ·" % c, pt, re.M)]
    add("P1 sections A-N", "PASS" if len(secs) == 14 else "FAIL", "".join(secs))
    steps = len(re.findall(r"^### Step (?:−1|\d+)", pt, re.M))
    gov = len(re.findall(r"\*\*Phase (\d+) — governing", pt))
    t8 = len(re.findall(r"`T8` — \*\*Phase (\d+)", pt))
    add("P2 step/phase blocks", "PASS" if (steps, gov, t8) == (12, 11, 11) else "FAIL", "steps %d, governing %d, T8 %d (want 12, 11, 11)" % (steps, gov, t8))
    d0 = pt.find("## D · Per-phase canon")
    d1 = pt.find("## E ·", d0)
    sec = pt[d0:d1] if d0 >= 0 and d1 > d0 else ""
    pmiss = []
    for ph, items in spine.items():
        for label, addr, acc in items:
            base = os.path.basename(addr.rstrip("/"))
            if (ph, base) in CD.EXEMPT:
                continue
            if not any(x.lower().rstrip("/") in sec.lower() for x in acc + CK.ALIAS.get(base, [])):
                pmiss.append("P%d %s" % (ph, base))
    add("P3 spine addresses in section D", "PASS" if not pmiss else "FAIL", "all present" if not pmiss else "absent: " + "; ".join(pmiss))
    npt = [f for f in MANIFEST if f not in pt]
    add("P4 datasheet files pointed to", "PASS" if not npt else "FAIL", "all 19" if not npt else "not pointed to: " + ", ".join(npt))
    a0 = pt.find("## A ·")
    a1 = pt.find("## B ·", a0)
    secA = pt[a0:a1]
    norm = lambda x: x.lower().replace("\u2019", "'").replace("\u2018", "'")
    noal = [n for n in ctx.names if norm(n) not in norm(secA)]
    add("P5 aliases in section A", "PASS" if not noal else "FAIL", "all %d names present" % len(ctx.names) if not noal else "absent from section A: " + ", ".join(noal))
    m = re.search(r"MISSING-INPUT=(\d+)", pt)
    m2 = re.search(r"(\d+) claims . (\d+) OK . (\d+) FAIL", pt)
    okv = bool(m and m.group(1) == "0" and m2 and m2.group(3) == "0")
    add("P6 verification block", "PASS" if okv else "FAIL", ("0 missing inputs; %s claims, 0 failed" % m2.group(1)) if okv else "block missing or non-zero")
    ph = re.findall(r"<[A-Za-z_ ]+>|<STATION>|<N>", "\n".join(l for l in pt.split("\n") if "placeholder check" not in l.lower() and "placeholder" not in l.lower()))
    add("P7 placeholders / carried names", "PASS" if not ph else "FAIL", "none" if not ph else "tokens: " + ", ".join(sorted(set(ph))[:5]))
    add("P8 ledger exists", "PASS" if os.path.exists(os.path.join(ctx.pass_dir, "00.2_Position_Coverage_Ledger.md")) else "FAIL", "")
    return ctx, res


def main():
    key = sys.argv[1]
    ctx, res = verify(key)
    f = sum(1 for r in res if r[1] == "FAIL")
    print("== %s: %d checks, %d FAIL, %d NOTE" % (ctx.name, len(res), f, sum(1 for r in res if r[1] == "NOTE")))
    for i, st, note in res:
        if st != "PASS" or "--quiet" not in sys.argv:
            print("  %-4s %-48s %s" % (st, i, note[:170]))
    return 1 if f else 0


if __name__ == "__main__":
    sys.exit(main())
