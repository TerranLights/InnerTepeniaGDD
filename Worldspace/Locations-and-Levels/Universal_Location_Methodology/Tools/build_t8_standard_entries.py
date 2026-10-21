#!/usr/bin/env python3
"""
BUILD T8 STANDARD ENTRIES  —  one-time (re)build of `T8_Standard_Entries.json` from a finished pass's hand-built
reading lists (November To-Do N-3a, 2026-10-21; developer approved).

  usage:  python3 build_t8_standard_entries.py <pass_folder> <git_ref> [--out FILE]

  <pass_folder>  a finished pass whose `.t8_required_*.txt` lists were hand-resolved (Mirny)
  <git_ref>      the commit in which those lists and the files they point at were in the state the lists describe
                 (line ranges are re-read from that commit, so later edits to the files cannot shift them)

WHAT IS A "STANDARD" ENTRY: an entry that is the same for EVERY city. The rule is mechanical:
    * any entry under Universal_Location_Methodology/ (the runbook, spine, disciplines, reference sheets, rulings), or
    * any whole-file entry (no line range) that is not one city's own file.
  Everything else is CITY-SPECIFIC and stays with the orchestrator and the Step -1 contract: the city's own pass files,
  its spec and culture files, its datasheet and Pre-Trip sheet, its research log, and any shared file opened only at the
  lines that concern this city (for example a census row).

WHY A FINGERPRINT: a range such as `00_RUNBOOK.md :: 309-372` is a line number, and line numbers drift when the file is
edited. For every range piece this tool stores the text of the piece's FIRST and LAST line as they were; the list
generator re-finds those two lines in today's file and moves the range to match, and refuses (writes `:: AUTO` and a
warning) if it cannot find them, which is the signal to line-check that span by hand.
"""
import json
import os
import re
import subprocess
import sys
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
OUT_DEFAULT = os.path.join(HERE, "..", "T8_Standard_Entries.json")
CITY_MARKERS = ("/City_Development_Passes/", "/Specs/", "/Local_Cultures/", "/Local_Robot_Culture/",
                "/Research_Logs/", "/Pre-Trip", "/Datasheets/")


def git_show(ref, relpath):
    r = subprocess.run(["git", "-C", REPO, "show", "%s:%s" % (ref, relpath)], capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout.decode("utf-8", "replace").split("\n")


def parse_pieces(spec):
    out = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        m = re.match(r"^(\d+)\s*-\s*(\d+)$", part)
        if m:
            out.append((int(m.group(1)), int(m.group(2))))
        elif part.isdigit():
            out.append((int(part), int(part)))
    return out


def target_of(fname):
    m = re.match(r"\.t8_required_(\d\d(?:\.\d)?)_(Step|Phase)(\w+)\.txt", fname)
    if not m:
        return None
    kind = "phase" if m.group(2) == "Phase" else "step"
    n = m.group(3)
    n = "-1" if n == "MINUS1" else n
    return "%s:%s" % (kind, n)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) < 2:
        print(__doc__)
        return 2
    pass_dir, ref = os.path.realpath(args[0]), args[1]
    out_path = os.path.abspath(OUT_DEFAULT)
    if "--out" in sys.argv:
        out_path = os.path.abspath(sys.argv[sys.argv.index("--out") + 1])
    result, stats = {}, {}
    for f in sorted(glob.glob(os.path.join(pass_dir, ".t8_required_*.txt"))):
        tgt = target_of(os.path.basename(f))
        if not tgt or tgt == "step:-1":
            continue
        entries, total, city = [], 0, 0
        for raw in open(f, encoding="utf-8"):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            total += 1
            path, _, spec = line.partition(" :: ")
            path, spec = path.strip(), spec.strip()
            if not path.startswith(REPO):
                city += 1
                continue
            rel = os.path.relpath(path, REPO)
            is_city = any(mk in path for mk in CITY_MARKERS) or os.path.isdir(path)
            standard = ("Universal_Location_Methodology" in path) or (not spec and not is_city)
            if not standard or is_city:
                city += 1
                continue
            e = {"path": rel, "whole": not spec, "auto": spec.upper() == "AUTO", "pieces": []}
            if spec and not e["auto"]:
                lines = git_show(ref, rel)
                if lines is None:
                    e["note"] = "file not found at %s" % ref
                else:
                    for a, b in parse_pieces(spec):
                        if a <= len(lines) and b <= len(lines):
                            e["pieces"].append({"a": a, "b": b, "first": lines[a - 1].strip(), "last": lines[b - 1].strip()})
                        else:
                            e["note"] = "range %d-%d outside the file at %s" % (a, b, ref)
            entries.append(e)
        result[tgt] = entries
        stats[tgt] = (len(entries), total)
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump({"built_from": os.path.basename(pass_dir), "git_ref": ref, "entries": result}, fh, indent=1, ensure_ascii=False)
    print("wrote %s" % out_path)
    print("%-10s %9s %9s" % ("target", "standard", "of total"))
    for t, (s, tot) in sorted(stats.items()):
        print("%-10s %9d %9d" % (t, s, tot))
    return 0


if __name__ == "__main__":
    sys.exit(main())
