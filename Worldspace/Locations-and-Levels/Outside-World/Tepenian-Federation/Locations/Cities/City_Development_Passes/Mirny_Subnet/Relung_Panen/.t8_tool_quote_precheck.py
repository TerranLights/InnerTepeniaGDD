#!/usr/bin/env python3
"""Standing line 13: normalized check of every quoted string in a target file against
(a) the files on a T8 list at their admitted ranges and (b) the pass's own other .md files
(dot-files excluded, the target itself excluded). Prints counts and the strings not found.
Usage: quote_precheck.py <target.md> <list.txt> <pass_dir> [extra_file[::ranges] ...]"""
import re, sys, os, glob
DASH = dict.fromkeys(map(ord, "—–−"), "-")
QT = {0x2019: "'", 0x2018: "'", 0x201C: '"', 0x201D: '"'}
def norm(s):
    s = s.translate(DASH).translate(QT)
    s = re.sub(r"[*`_\[\]>|#]", " ", s)
    s = re.sub(r"[^\w\s'\"/.,;:()%\-+°]", " ", s)
    return re.sub(r"\s+", " ", s).strip().lower()
def spans(spec):
    out = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-"); out.append((int(a), int(b)))
        elif part:
            out.append((int(part), int(part)))
    return out
def load(entry):
    if " :: " in entry:
        path, rng = entry.split(" :: ", 1)
    elif "::" in entry:
        path, rng = entry.split("::", 1)
    else:
        path, rng = entry, None
    path = path.strip()
    with open(path, encoding="utf-8", errors="ignore") as fh:
        lines = fh.read().split("\n")
    if rng is None:
        return path, "\n".join(lines)
    keep = []
    for a, b in spans(rng):
        keep.extend(lines[a-1:b])
    return path, "\n".join(keep)
target, listf, pass_dir = sys.argv[1], sys.argv[2], sys.argv[3]
entries = [l.strip() for l in open(listf, encoding="utf-8") if l.strip()]
entries += sys.argv[4:]
src = [norm(load(e)[1]) for e in entries]
own = []
for f in glob.glob(os.path.join(pass_dir, "*.md")):
    if os.path.realpath(f) == os.path.realpath(target) or "superseded" in os.path.basename(f):
        continue
    own.append(norm(open(f, encoding="utf-8", errors="ignore").read()))
src_all, own_all = "   ".join(src), "   ".join(own)
raw = open(target, encoding="utf-8").read().split("\n")
tot = found_src = found_own = 0
miss = []
def quoted(line):
    line = re.sub(r"`[^`]*`", lambda m: re.sub(r'["“”]', "'", m.group(0)), line)   # a quote mark inside a code span does not open a quotation
    marks = [i for i, ch in enumerate(line) if ch in '"“”']
    out = []
    for k in range(0, len(marks) - 1, 2):
        out.append(line[marks[k] + 1:marks[k + 1]])
    return out
for n, line in enumerate(raw, 1):
    for q in quoted(line):
        for frag in re.split(r"\.\.\.|…", q):
            f = norm(frag).strip(" .,;:-")
            if len(f.split()) < 3:
                continue
            tot += 1
            if f in src_all: found_src += 1
            elif f in own_all: found_own += 1
            else: miss.append((n, f))
print("target: %s" % os.path.basename(target))
print("sources: %d list entries%s; own-pass files: %d (dot-files and superseded files excluded)" % (len(entries), "", len(own)))
print("quoted fragments (>=3 words, ellipsis-split): %d" % tot)
print("found in sources at admitted ranges: %d | found only in the pass's own files: %d | NOT FOUND: %d" % (found_src, found_own, len(miss)))
for n, f in miss:
    print("  L%d  %s" % (n, f[:160]))
