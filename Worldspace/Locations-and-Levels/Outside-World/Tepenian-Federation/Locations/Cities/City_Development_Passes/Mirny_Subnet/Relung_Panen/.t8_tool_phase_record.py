#!/usr/bin/env python3
"""Write a phase's round record from a JSON config, pasting every raw tool output whole.
usage: .t8_tool_phase_record.py <config.json>
config keys: tag (e.g. 04_Phase_03), title, output (the phase file), record (the record file to write), time,
round0, round1, round3_note, merge, triage (dict: tool-key -> triage text), dqs, cannot_show.
Raw files used, by name, in the pass folder: .t8_<tag>_round2_raw.txt, _quote_precheck_raw*.txt, _quotation_audit_raw*.txt,
_ame_sweep_raw*.txt, _handoff_audit_raw.txt, _phase_discipline_raw.txt (every one present is pasted, in order)."""
import sys, json, glob, os, subprocess
cfg = json.load(open(sys.argv[1], encoding="utf-8"))
tag = cfg["tag"]
TOOLS = "/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools"
def ver(t):
    return subprocess.run(["git", "log", "-1", "--format=%cs", "--", t], capture_output=True, text=True, cwd=TOOLS).stdout.strip()
r = lambda f: open(f, encoding="utf-8").read().rstrip("\n")
lst = r(".t8_required_%s.txt" % tag)
verd = []
for X in "ABC":
    L = open(".t8_%s_round3_reader%s.md" % (tag, X), encoding="utf-8").read().splitlines()
    for i, l in enumerate(L):
        if "VERDICT" in l.upper():
            for j in range(i, min(i + 4, len(L))):
                if j > i and "VERDICT" in L[j].upper() and "CONSISTENT" not in L[j]: break
                if "CONSISTENT" in L[j]:
                    v = ".t8_%s_round3_reader%s.md:%d: %s" % (tag, X, j + 1, L[j].strip()[:170])
                    if v not in verd: verd.append(v)
r3lines = ", ".join("`…reader%s.md` (%d)" % (X, len(open(".t8_%s_round3_reader%s.md" % (tag, X)).read().splitlines())) for X in "ABC")
outlines = len(open(cfg["output"], encoding="utf-8").read().splitlines())
tr = cfg.get("triage", {})
def block(title, path, key):
    s = "### %s, raw output, whole (`%s`)\n\n```\n%s\n```\n" % (title, path, r(path))
    if key in tr: s += "\n**Triage:** %s\n" % tr[key]
    return s
checks = []
n = 1
for pat, name, tool in [("quote_precheck_raw", "Quotation pre-check", None), ("quotation_audit_raw", "Quotation audit", "quotation_audit.py"),
                        ("ame_sweep_raw", "American English sweep", None), ("handoff_audit_raw", "Handoff audit", "handoff_audit.py"),
                        ("phase_discipline_raw", "Phase discipline check", "phase_discipline_check.py")]:
    files = sorted(glob.glob(".t8_%s_%s*.txt" % (tag, pat)))
    for f in files:
        label = "%d · %s%s%s" % (n, name, (", `Tools/%s` (last change %s)" % (tool, ver(tool))) if tool else "",
                                  (", " + f.split(pat)[1].strip("_").replace(".txt", "").replace("run", "run ")) if f.split(pat)[1] != ".txt" else "")
        checks.append(block(label, f, os.path.basename(f)))
    n += 1
doc = """# Round record — Relung Panen · ULM %s

**Output:** `%s` (%d lines). Three Opus readers, Round 2, Round 3, one fresh merge writer (`M-246`). Every tool output below is pasted whole. PROPOSED; nothing declared complete. Record written %s. Isolation: the fresh session (run log RL-07, RL-08); fresh readers and clean briefs.

## Round 0 — the list and the frozen briefs

%s

```
%s
```

## Round 1 — three readers

%s

## Round 2 — `Tools/triple_read_verify.py` (last change %s), raw output, whole (`.t8_%s_round2_raw.txt`)

```
%s
```

## Round 3 — cross-checks, saved as sent back

`.t8_%s_round3_readerA.md` and the others: %s; the other two outputs given by path. %s Verdict lines:

```
%s
```

**All six cross-verdicts CONSISTENT.**

## The merge

%s

## Close checks (run before this record existed)

%s
## Developer questions filed

%s

## What this record cannot show

%s 'judgement' is the one kept British form and is reported but not counted.
""" % (cfg["title"], cfg["output"], outlines, cfg["time"], cfg["round0"], lst, cfg["round1"], ver("triple_read_verify.py"), tag,
       r(".t8_%s_round2_raw.txt" % tag), tag, r3lines, cfg["round3_note"], "\n".join(verd), cfg["merge"], "\n".join(checks), cfg["dqs"],
       cfg["cannot_show"])
assert len(verd) == 6, "verdict lines found: %d" % len(verd)
open(cfg["record"], "w", encoding="utf-8").write(doc)
print(cfg["record"], len(doc.splitlines()), "lines;", len(checks), "check blocks")
