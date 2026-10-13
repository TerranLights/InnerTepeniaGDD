#!/usr/bin/env python3
"""Assemble 07_QA_Gates.md = .t8_Step7_merge_body.md + the readers' fenced raw-output blocks, per gate, verbatim."""
import re
from pathlib import Path
H = Path(__file__).resolve().parent
body = (H / ".t8_Step7_merge_body.md").read_text(encoding="utf-8").rstrip("\n") + "\n"
out = [body]
total = 0
gates = ["0","1","2","3","4","5","6","7","8","9","10","11","C","F","I","P","G"]
data = {}
for r in "ABC":
    L = (H / f".t8_Step7_reader{r}.md").read_text(encoding="utf-8").splitlines()
    start = next(i for i,l in enumerate(L) if l.startswith("### Gate 0"))
    end = next(i for i,l in enumerate(L) if l.startswith("## The closing test"))
    cur = None; blocks = {g: [] for g in gates}; inb = False; buf = []
    for l in L[start:end]:
        m = re.match(r"### Gate (\w+)", l)
        if m and not inb:
            cur = m.group(1); continue
        if l.startswith("```"):
            if not inb: inb = True; buf = []
            else:
                inb = False
                if cur in blocks: blocks[cur].append(buf)
            continue
        if inb: buf.append(l)
    data[r] = blocks
for g in gates:
    out.append(f"\n### Gate {g}\n")
    any_ = False
    for r in "ABC":
        for k, b in enumerate(data[r][g], 1):
            any_ = True; total += len(b)
            out.append(f"**[{r}] block {k}** ({len(b)} lines)\n```\n" + "\n".join(b) + "\n```\n")
    if not any_:
        out.append("*(no fenced raw-output block in any reader's gate section; the gate was a reading procedure)*\n")
out.append(f"\n*End of extracted raw output: {total} lines in total.*\n")
(H / "07_QA_Gates.md").write_text("".join(out), encoding="utf-8")
print("wrote 07_QA_Gates.md; raw lines", total, "; total lines", len("".join(out).splitlines()))
