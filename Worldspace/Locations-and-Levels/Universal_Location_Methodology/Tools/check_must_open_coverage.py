#!/usr/bin/env python3
"""
CHECK MUST-OPEN COVERAGE  —  the Field Guide's RULE 1, done city by city, phase by phase
(2026-10-23; developer: "when you do it by script, you just say yes").

  usage:  python3 check_must_open_coverage.py [--city KEY ...] [--out FILE]

THE RULE (Mechanical_Extraction_Field_Guide.md, RULE 1): "The spine's MUST OPEN list is the contract. ... open the phase's
MUST OPEN block, tick each address off against the datasheet, and record the coverage count in the datasheet itself (e.g.
'13 of 13'). A datasheet that does not cover the spine's list is INCOMPLETE and must say so at the top."

WHAT IT DOES
  1. Reads the eleven `MUST OPEN` blocks of 03_The_Phase_Spine.md (Phases 0-10) and turns each bullet into REQUIRED ITEMS:
     a file address -> its file name; a folder address with names in the bullet label -> those names; a bare folder -> the folder name.
  2. For each city, looks in the datasheet that carries that phase (Phase 0 -> Step_0.md, Phase 1 -> Step_1_and_2.md, Phase N -> Phase_N.md)
     and in the city's Pre-Trip section D, and records for each required item: NAMED (the item's name appears) or NOT NAMED.
  3. Reports, per phase, how many required items there are and how many cities name each; and per city, the gaps.
  4. Also reports whether each datasheet RECORDS a coverage count, as the Field Guide requires.

WHAT "NOT NAMED" MEANS: the datasheet does not mention the item by name. It is a lead, not a verdict: the content may be carried by a
shared (Tier U) sheet the datasheet cites. Each distinct NOT NAMED item is therefore listed once, for a human to judge.
"""
import argparse
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_pretrip as bp  # noqa: E402

SPINE = os.path.join(bp.ULM, "03_The_Phase_Spine.md")
# a few addresses are tested under more than one name a datasheet may use for them
ALIAS = {"City_Megasheets": ["megasheet"], "Zodiac_Signs_Full_Attributes.md": ["Zodiac_Signs_Quick_Reference"], "Davis_Geosciences_Research": ["geosciences_research", "geosciences research"]}
OUT_OF_SCOPE = {"Concordia", "Relung_Panen", "Amundsen_Station", "Shirayuki", "Sinheung", "Zhongshan_Opus", "Zhongshan_Sonnet", "Davis"}


def spine_items():
    """Phase -> list of (label, address, [acceptable names]). Every bullet of a MUST OPEN block that has an absolute address."""
    ls = open(SPINE, encoding="utf-8").read().split("\n")
    starts = [i for i, l in enumerate(ls) if "MUST OPEN" in l and l.startswith("> ###")]
    phases = {}
    for k, s in enumerate(starts):
        j, items = s + 1, []
        # the block runs until the first line that is not a quoted continuation, after at least one bullet
        while j < len(ls) and not (ls[j].startswith("> \u26d4") and "Not optional" in ls[j]) and not ls[j].startswith("> ### "):
            if ls[j].startswith("> - "):
                label = ls[j][4:]
                addrs = []
                m = j + 1
                while m < len(ls) and ls[m].startswith(">") and not ls[m].startswith("> - ") and not ls[m].startswith("> \u26d4") and not ls[m].startswith("> ###"):
                    addrs += re.findall(r"`(/home/[^`]+)`", ls[m])
                    m += 1
                names = [n for n in re.findall(r"`([^`/]+\.md)`", label)]
                for ad in addrs:
                    if ad.endswith(".md"):
                        acc = [os.path.basename(ad)]
                    else:
                        d = ad.rstrip("/")
                        acc = names[:] if names else [os.path.basename(d)] + (os.listdir(d) if os.path.isdir(d) else [])
                    items.append((re.sub(r"[*\u2b50\u26d4\u26a0\u2705`]", "", label).strip()[:60], ad, acc))
                j = m
                continue
            j += 1
        phases[k] = items
    return phases


def datasheet_for(ctx, phase):
    d = os.path.join(ctx.pass_dir, "Datasheets")
    f = {0: "Step_0.md", 1: "Step_1_and_2.md"}.get(phase, "Phase_%d.md" % phase)
    p = os.path.join(d, f)
    return p, (open(p, encoding="utf-8").read() if os.path.exists(p) else None)


CRS = os.path.join(bp.ULM, "Corpus_Reference_Sheets")
_crs_cache = {}


def tier_u_text(ds_text):
    """Text of every shared (Tier U) sheet that this datasheet cites."""
    out = []
    for nm in set(re.findall(r"([A-Za-z0-9_\-]+_Quick_Reference\.md)", ds_text or "")):
        if nm not in _crs_cache:
            f = os.path.join(CRS, nm)
            _crs_cache[nm] = open(f, encoding="utf-8").read() if os.path.exists(f) else ""
        out.append(_crs_cache[nm])
    return "\n".join(out)


def named(text, req):
    t = text.lower()
    r = req.lower().rstrip("/")
    r = r[:-3] if r.endswith(".md") else r
    return r in t.replace("_", " ").replace("\\", "") or r in t or r.replace("_", " ") in t.replace("_", " ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--city", nargs="*")
    ap.add_argument("--out")
    a = ap.parse_args()
    keys = a.city or [k for k in bp.CITY if k not in OUT_OF_SCOPE]
    spine = spine_items()
    ctxs = {k: bp.Ctx(k) for k in keys}
    lines = ["# MUST-OPEN coverage by name — raw output, %d cities" % len(keys), ""]
    cover = {}      # (phase, item) -> [cities that name it]
    percity = {k: [] for k in keys}
    countrec = {}
    for ph, items in spine.items():
        for label, addr, acc in items:
            rq = addr if addr.endswith(".md") else addr.rstrip("/")
            rq = os.path.basename(rq)
            for k in keys:
                p, txt = datasheet_for(ctxs[k], ph)
                direct = txt is not None and any(named(txt, x) for x in acc + ALIAS.get(rq, []))
                via = (not direct) and txt is not None and any(named(tier_u_text(txt), x) for x in acc + ALIAS.get(rq, []))
                ok = "direct" if direct else ("via Tier U" if via else False)
                cover.setdefault((ph, label, rq), []).append((k, ok))
                if not ok:
                    percity[k].append((ph, label, rq))
    for k in keys:
        for ph in spine:
            p, txt = datasheet_for(ctxs[k], ph)
            countrec[(k, ph)] = bool(txt and re.search(r"\b\d+\s+of\s+\d+\b", txt) and re.search(r"coverage|MUST[- ]OPEN", txt, re.I))
    for ph, items in spine.items():
        lines.append("## Phase %d — %d required addresses" % (ph, len(items)))
        lines.append("| Spine label | Address (file or folder) | named directly | covered via a cited shared sheet | NOT covered |")
        lines.append("|---|---|--:|--:|--:|")
        for label, addr, acc in items:
            rq = os.path.basename(addr.rstrip("/"))
            r = cover[(ph, label, rq)]
            d = sum(1 for _, o in r if o == "direct")
            v = sum(1 for _, o in r if o == "via Tier U")
            lines.append("| %s | `%s` | %d | %d | %d |" % (label.replace("|", "/"), rq, d, v, len(r) - d - v))
        lines.append("")
    lines.append("## Does any datasheet record a coverage count, as the Field Guide requires?")
    n = sum(1 for v in countrec.values() if v)
    lines.append("%d of %d (city, phase) datasheets carry one." % (n, len(countrec)))
    lines.append("")
    lines.append("## Per city: required items its datasheets do not name")
    for k in keys:
        lines.append("### %s — %d gaps" % (ctxs[k].name, len(percity[k])))
        for ph, label, rq in percity[k]:
            lines.append("- Phase %d: `%s` (%s)" % (ph, rq, label))
    txt = "\n".join(lines) + "\n"
    if a.out:
        open(a.out, "w", encoding="utf-8").write(txt)

    # ---------------- Pre-Trip: per-phase lists and block structure
    pt_rows = []
    for k in keys:
        f = os.path.join(ctxs[k].pass_dir, "00.0_Pre-Trip_Inspection.md")
        txt = open(f, encoding="utf-8").read() if os.path.exists(f) else ""
        d0 = txt.find("## D \u00b7 Per-phase canon")
        d1 = txt.find("## E \u00b7", d0)
        sec = txt[d0:d1] if d0 >= 0 and d1 > d0 else ""
        miss = []
        for ph, items in spine.items():
            for label, addr, acc in items:
                if not any(x.lower().rstrip("/") in sec.lower() for x in acc + ALIAS.get(os.path.basename(addr.rstrip("/")), [])):
                    miss.append((ph, os.path.basename(addr.rstrip("/"))))
        steps = len(re.findall(r"^### Step (?:\u22121|\d+)", txt, re.M))
        gov = len(re.findall(r"\*\*Phase (\d+) \u2014 governing", txt))
        t8 = len(re.findall(r"`T8` \u2014 \*\*Phase (\d+)", txt))
        secs = [c for c in "ABCDEFGHIJKLMN" if re.search(r"^## (?:\U0001f9ea )?%s \u00b7" % c, txt, re.M)]
        pt_rows.append((k, steps, gov, t8, "".join(secs), miss))
    lines2 = ["", "## Pre-Trip checks", "| City | step blocks (of 11) | phase 'governing' lines (of 11) | phase T8 lines (of 11) | sections present | spine addresses absent from section D |", "|---|--:|--:|--:|---|---|"]
    for k, s, g, t8_, secs, miss in pt_rows:
        lines2.append("| %s | %d | %d | %d | %s | %s |" % (ctxs[k].name, s, g, t8_, secs, ", ".join("P%d %s" % m for m in miss) or "none"))
    txt_out = "\n".join(lines) + "\n" + "\n".join(lines2) + "\n"
    if a.out:
        open(a.out, "w", encoding="utf-8").write(txt_out)
    print()
    print("PRE-TRIP: step blocks / governing / T8 lines / sections / spine addresses missing from section D")
    for k, s, g, t8_, secs, miss in pt_rows:
        print("  %-20s %2d %2d %2d  %-14s %s" % (ctxs[k].name, s, g, t8_, secs, ", ".join("P%d %s" % m for m in miss) or "-"))
    # console summary
    print("phases parsed (addresses per phase):", {k: len(v) for k, v in spine.items()})
    print("coverage counts recorded in datasheets: %d of %d" % (n, len(countrec)))
    for ph, items in spine.items():
        for label, addr, acc in items:
            rq = os.path.basename(addr.rstrip("/"))
            r = cover[(ph, label, rq)]
            d = sum(1 for _, o in r if o == "direct")
            v = sum(1 for _, o in r if o == "via Tier U")
            miss = len(r) - d - v
            flag = "" if miss == 0 else "   <-- NOT covered in %d" % miss
            print("P%-2d %-44s direct %2d  via-shared %2d  none %2d%s" % (ph, rq[:44], d, v, miss, flag))
    tot = sum(len(v) for v in percity.values())
    print("TOTAL gaps across %d cities: %d" % (len(keys), tot))


if __name__ == "__main__":
    sys.exit(main())
