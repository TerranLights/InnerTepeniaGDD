#!/usr/bin/env python3
"""Blind insertion of Casey's ten rows into the city differentiation table (runbook L2934, M-272).
Reads the rows from 06_Differentiation.md (the fenced block under each '### Section N' heading).
For each section of the table: finds the section by its '# N.' heading, finds the table header by its first-column label 'City',
asserts the column count, inserts Casey's row after the table's last row. Prints only headings, counts and line numbers,
never another row's content. Writes a backup first; refuses if Casey already has a row. Usage: insert_casey_rows.py <table> <06 file> <backup> [--apply]"""
import sys, re
table, src, backup = sys.argv[1:4]; apply = "--apply" in sys.argv
T = open(table, encoding="utf-8").read().split("\n")
if any(re.match(r"^\|\s*Casey\s*\|", l) for l in T): sys.exit("Casey already has a row; refusing")
S = open(src, encoding="utf-8").read().split("\n")
rows = {}
for i, l in enumerate(S):
    m = re.match(r"^### Section (\d+)\b", l)
    if m:
        n = int(m.group(1))
        j = i + 1
        while j < len(S) and not S[j].startswith("```"): j += 1
        block = []
        k = j + 1
        while k < len(S) and not S[k].startswith("```"):
            if S[k].strip(): block.append(S[k])
            k += 1
        assert len(block) == 1, (n, len(block))
        rows[n] = block[0]
assert sorted(rows) == list(range(1, 11)), sorted(rows)
def cols(l): return len([c for c in l.strip().strip("|").split("|")])
heads = [(i, int(re.match(r"^# (\d+)\.", l).group(1))) for i, l in enumerate(T) if re.match(r"^# (\d+)\.", l)]
plan = []
for idx, (hi, n) in enumerate(heads):
    end = heads[idx + 1][0] if idx + 1 < len(heads) else len(T)
    h = next(i for i in range(hi, end) if re.match(r"^\|\s*City\s*\|", T[i]))
    last = h + 1
    while last + 1 < end and T[last + 1].startswith("|"): last += 1
    hc, rc = cols(T[h]), cols(rows[n])
    print(f"section {n}: heading L{hi+1}, header L{h+1} ({hc} cols), last table line L{last+1}, Casey row {rc} cols")
    assert hc == rc, (n, hc, rc)
    plan.append((last, rows[n]))
if not apply: sys.exit("dry run only")
open(backup, "w", encoding="utf-8").write("\n".join(T))
for last, row in sorted(plan, reverse=True): T.insert(last + 1, row)
open(table, "w", encoding="utf-8").write("\n".join(T))
B = open(backup, encoding="utf-8").read().split("\n"); N = open(table, encoding="utf-8").read().split("\n")
import difflib
added = [l for l in difflib.ndiff(B, N) if l.startswith("+ ")]; removed = [l for l in difflib.ndiff(B, N) if l.startswith("- ")]
print(f"inserted {len(added)} lines, removed {len(removed)}; every inserted line is Casey's: {all(re.match(r'^\+ \|\s*Casey\s*\|', l) for l in added)}")
