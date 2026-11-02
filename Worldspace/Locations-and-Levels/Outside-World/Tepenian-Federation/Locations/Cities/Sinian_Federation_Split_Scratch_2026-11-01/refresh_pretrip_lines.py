#!/usr/bin/env python3
"""Refresh ONLY the line-citation numbers in each existing Pre-Trip sheet, using build_pretrip.py's live scan as the
reference (the remapper skips bold-wrapped numbers, which is how the Pre-Trip writes census/extent/16 lines).
usage: python3 refresh_pretrip_lines.py [--apply] [CityKey ...]
For each city: generate a fresh Pre-Trip into the scratchpad; pair lines whose text is equal once digits are removed;
in a pair, replace a number in the old line by the new line's number only when it sits in a line-citation context
(preceded by 'L', '**', 'lines ', a range dash or a list comma) and is not part of a date. Everything else is left."""
import difflib, os, re, subprocess, sys, glob
from pathlib import Path
HERE = Path(__file__).resolve().parent
REPO = Path(subprocess.run(["git", "-C", str(HERE), "rev-parse", "--show-toplevel"], capture_output=True).stdout.decode().strip())
TOOLS = REPO / "Worldspace/Locations-and-Levels/Universal_Location_Methodology/Tools"
PASSES = REPO / "Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes"
SCR = Path(os.environ.get("SCRATCH", "/tmp"))
TOK = re.compile(r"(\d+|\D+)")
strip = lambda s: re.sub(r"\d+", "#", s)


def merge(old, new, changes):
    to, tn = TOK.findall(old), TOK.findall(new)
    if len(to) != len(tn):
        return old
    out = []
    for i, (a, b) in enumerate(zip(to, tn)):
        if a.isdigit() and b.isdigit() and a != b:
            before = "".join(tn[:i])
            after = "".join(tn[i + 1:])
            ctx = re.search(r"(?:\bL|\*\*|\blines? |\blines? \*\*|[–-]|, |\(L|L)$", before) is not None
            date = re.search(r"\d{4}-$|\d{4}-\d{2}-$", before) or re.match(r"-\d", after) and re.search(r"\d{4}$", "".join(tn[max(0, i - 1):i + 1]))
            if re.search(r"\d{4}-\d{2}-$", before) or re.search(r"\d{4}-$", before) or (len(a) == 4 and 2020 <= int(a) <= 2030):
                date = True
            if ctx and not date and int(a) < 20000 and int(b) < 20000:
                changes.append((a, b))
                out.append(b)
                continue
        out.append(a)
    return "".join(out)


def main():
    apply = "--apply" in sys.argv
    keys = [a for a in sys.argv[1:] if not a.startswith("--")]
    sys.path.insert(0, str(TOOLS))
    import build_pretrip as B
    keys = keys or list(B.CITY.keys())
    total = 0
    for k in keys:
        ctx = B.Ctx(k)
        old_path = Path(ctx.pass_dir) / "00.0_Pre-Trip_Inspection.md"
        if not old_path.exists():
            print(k, "no Pre-Trip"); continue
        tmp = SCR / "pt_gen" / k
        tmp.mkdir(parents=True, exist_ok=True)
        subprocess.run([sys.executable, "-B", str(TOOLS / "build_pretrip.py"), k, "--out", str(SCR / "pt_gen")], capture_output=True, cwd=str(TOOLS))
        newp = SCR / "pt_gen" / k / "00.0_Pre-Trip_Inspection.md"
        O = old_path.read_text(encoding="utf-8").split("\n")
        N = newp.read_text(encoding="utf-8").split("\n")
        sm = difflib.SequenceMatcher(None, [strip(l) for l in O], [strip(l) for l in N], autojunk=False)
        changes, nlines = [], 0
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == "equal":
                for d in range(i2 - i1):
                    if O[i1 + d] != N[j1 + d]:
                        m = merge(O[i1 + d], N[j1 + d], changes)
                        if m != O[i1 + d]:
                            O[i1 + d] = m
                            nlines += 1
        total += len(changes)
        print(f"{k:18s} numbers changed: {len(changes):3d} in {nlines:2d} lines", (changes if "--show" in sys.argv else ""))
        if apply:
            old_path.write_text("\n".join(O), encoding="utf-8")
    print("total numbers", total, "APPLIED" if apply else "dry run")


if __name__ == "__main__":
    main()
