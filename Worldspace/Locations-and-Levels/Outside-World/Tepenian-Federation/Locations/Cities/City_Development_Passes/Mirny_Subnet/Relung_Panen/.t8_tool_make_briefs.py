#!/usr/bin/env python3
"""Generate the three frozen briefs for one T8 unit.
usage: make_briefs.py <template.md> <list.txt> <list.desc> <results.txt> <out_prefix> <stage_root> <unit_tag>
- list.txt: one entry per line (path or 'path :: ranges'); list.desc: one description per entry, same order.
- results.txt: orchestrator-verified results, one per line, each already carrying its (source: ...) pointer.
- writes <out_prefix>_A.md, _B.md, _C.md; staging <stage_root>/reader<X>/, output <unit_tag>_reader<X>.md there."""
import sys, os, re
tpl, lst, desc, res, outp, stage, tag = sys.argv[1:8]
entries = [l.rstrip("\n") for l in open(lst, encoding="utf-8") if l.strip()]
descs = [l.rstrip("\n") for l in open(desc, encoding="utf-8") if l.strip()]
assert len(entries) == len(descs), "list has %d entries, desc has %d" % (len(entries), len(descs))
for e in entries:
    p = e.split(" :: ")[0]
    assert os.path.exists(p), "missing: " + p
results = [l.rstrip("\n") for l in open(res, encoding="utf-8") if l.strip()]
# standing lines, part A, verbatim from the file
sl = open("/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/T8_Standing_Brief_Lines.md", encoding="utf-8").read()
partA = sl.split("## A ·")[1].split("## B ·")[0]
standing = [l for l in partA.split("\n") if re.match(r"^(1|2|3|4|5|6|10|11)\. ", l)]
assert len(standing) == 8, "standing lines found: %d" % len(standing)
# entry sentence, computed from the list
groups, prev, start = [], None, 1
for i, d in enumerate(descs, 1):
    if d != prev:
        if prev is not None: groups.append((start, i - 1, prev))
        prev, start = d, i
groups.append((start, len(descs), prev))
parts = [("entry %d is %s" % (a, d)) if a == b else ("entries %d-%d are %s" % (a, b, d)) for a, b, d in groups]
sentence = "The list has %d entries: %s." % (len(entries), "; ".join(parts))
listing = "\n".join("  %d. %s" % (i, e) for i, e in enumerate(entries, 1))
resblock = "\n".join("- " + r for r in results) if results else "- none"
T = open(tpl, encoding="utf-8").read()
for X in "ABC":
    st = os.path.join(stage, "reader" + X)
    out = os.path.join(st, "%s_reader%s.md" % (tag, X))
    b = (T.replace("{X}", X).replace("{OUT}", out).replace("{STAGE}", st).replace("{N}", str(len(entries)))
          .replace("{ENTRY_SENTENCE}", sentence).replace("{LIST}", listing).replace("{RESULTS}", resblock)
          .replace("{STANDING}", "\n".join(standing)))
    assert "{" not in re.sub(r"`[^`]*`", "", b) or True
    leftover = re.findall(r"\{[A-Z_]+\}", b)
    assert not leftover, "unfilled placeholders: %s" % leftover
    open("%s_%s.md" % (outp, X), "w", encoding="utf-8").write(b)
    os.makedirs(st, exist_ok=True)
print(sentence)
print("briefs written:", ", ".join("%s_%s.md" % (os.path.basename(outp), X) for X in "ABC"), "| entries:", len(entries), "| results:", len(results))
