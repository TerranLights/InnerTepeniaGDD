#!/usr/bin/env python3
"""Assemble the ten Step 5 merge parts into 05_Reconciliation.md.

Reads .t8_Step5_merge_part_01.md .. _10.md in order, resolves the step-local
numbering keys, checks nothing is missing, and writes 05_Reconciliation.md.

Key syntax:
  definition   **{{X:key}}   (the first occurrence preceded by two asterisks) assigns the next
               number in series X, in order of appearance in the assembled text.
  reference    {{X:key}} or [[X:key]] anywhere else resolves to the same label.
Series: C -> C-n, BT -> BT-n, D -> D-n, R -> R-(130+n), Q -> Q-(99+n),
        PA -> PA-(68+n), S5RF -> S5-RF-n, S5 -> S5-n.

Usage: assemble_merge5.py [--check]    (--check resolves and reports, writes nothing)
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARTS = [HERE / f".t8_Step5_merge_part_{i:02d}.md" for i in range(1, 11)]
OUT = HERE / "05_Reconciliation.md"

SERIES = {
    "C": lambda n: f"C-{n}",
    "BT": lambda n: f"BT-{n}",
    "D": lambda n: f"D-{n}",
    "R": lambda n: f"R-{130 + n}",
    "Q": lambda n: f"Q-{99 + n}",
    "PA": lambda n: f"PA-{68 + n}",
    "S5RF": lambda n: f"S5-RF-{n}",
    "S5": lambda n: f"S5-{n}",
}
DEF = re.compile(r"\*\*\{\{(C|BT|D|R|Q|PA|S5RF|S5):([a-z0-9-]+)\}\}")
REF = re.compile(r"(?:\{\{|\[\[)(C|BT|D|R|Q|PA|S5RF|S5):([a-z0-9-]+)(?:\}\}|\]\])")


def main():
    check_only = "--check" in sys.argv
    problems = []
    texts = []
    for p in PARTS:
        if not p.exists():
            problems.append(f"missing part file: {p.name}")
            continue
        texts.append(p.read_text(encoding="utf-8"))
    if problems:
        print("\n".join(problems))
        sys.exit(1)
    full = "\n".join(t.rstrip("\n") + "\n" for t in texts)

    labels = {}
    counts = {k: 0 for k in SERIES}
    for m in DEF.finditer(full):
        s, key = m.group(1), m.group(2)
        if (s, key) in labels:
            problems.append(f"duplicate definition {s}:{key}")
            continue
        counts[s] += 1
        labels[(s, key)] = SERIES[s](counts[s])

    def sub_def(m):
        return "**" + labels[(m.group(1), m.group(2))]

    out = DEF.sub(sub_def, full)

    unresolved = set()

    def sub_ref(m):
        k = (m.group(1), m.group(2))
        if k not in labels:
            unresolved.add(f"{k[0]}:{k[1]}")
            return m.group(0)
        return labels[k]

    out = REF.sub(sub_ref, out)
    for u in sorted(unresolved):
        problems.append(f"unresolved key {u}")

    leftovers = re.findall(r"\{\{[^}]*\}\}|\[\[[^\]]*\]\]", out)
    for lo in leftovers:
        problems.append(f"leftover marker {lo!r}")

    # every defined key must be referenced at least once outside its definition (soft check)
    unref = []
    for (s, key) in labels:
        pat = re.compile(r"(?:\{\{|\[\[)%s:%s(?:\}\}|\]\])" % (re.escape(s), re.escape(key)))
        if not pat.search(full):
            unref.append(f"{s}:{key}")

    print("series counts:", {k: v for k, v in counts.items()})
    print("labels:", len(labels))
    print("defined but never referenced (informational):", unref if unref else "none")
    if problems:
        print("PROBLEMS:")
        for p in problems:
            print("  -", p)
        sys.exit(1)
    if not check_only:
        OUT.write_text(out, encoding="utf-8")
        print(f"wrote {OUT.name}: {len(out.splitlines())} lines")
    else:
        print("check passed; nothing written")


if __name__ == "__main__":
    main()
