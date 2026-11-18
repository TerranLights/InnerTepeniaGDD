#!/usr/bin/env python3
"""File a pass file's DQ-n bullets into the decisions file, verbatim, above '## Answered'.
usage: .t8_tool_file_dqs.py <pass_file> <step label> <first DEC number> <expected DQ count>"""
import re, sys, os
src, label, first, expect = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
D = "/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md"
c = open(src, encoding="utf-8").read().split("\n")
d = open(D, encoding="utf-8").read()
last = max(int(x) for x in re.findall(r"DEC-(\d+)", d))
assert last == first - 1, "decisions file ends at DEC-%d, expected DEC-%d" % (last, first - 1)
blocks, num = [], first
starts = [i for i, l in enumerate(c) if re.match(r"^- \*\*DQ-(\d+) ·", l)]
for s in starts:
    e = s + 1
    while e < len(c) and not c[e].startswith("- **") and not c[e].startswith("#"):
        e += 1
    while c[e - 1].strip() == "":
        e -= 1
    dq = re.match(r"^- \*\*DQ-(\d+)", c[s]).group(1)
    rng = ("L%d" % (s + 1)) if e == s + 1 else ("L%d–L%d" % (s + 1, e))
    blocks.append(("### DEC-%d · OPEN · " + __import__("datetime").date.today().isoformat() + " · %s (DQ-%s)\n*From `%s` %s, copied verbatim:*\n%s\n") % (num, label, dq, os.path.basename(src), rng, "\n".join(c[s:e])))
    num += 1
assert len(blocks) == expect, "found %d DQ bullets, expected %d" % (len(blocks), expect)
anchor = "\n---\n\n## Answered"
assert d.count(anchor) == 1
open(D, "w", encoding="utf-8").write(d.replace(anchor, "\n" + "\n".join(blocks) + anchor))
print("filed DEC-%d to DEC-%d" % (first, num - 1))
