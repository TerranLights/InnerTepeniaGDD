#!/usr/bin/env python3
"""
REMAP LINE CITATIONS  —  finds datasheet and Pre-Trip citations that name a line number in a file that has changed
since the datasheet was written, and moves each number to where that line is NOW (November To-Do N-7, 2026-10-21;
the general form of the by-hand fix made to the Vostok set, N-2a).

  usage:  python3 remap_line_citations.py <file_or_folder> --base <git_ref> [--apply]

  <file_or_folder>  a datasheet, a Pre-Trip sheet, or a folder of them (searched recursively for *.md)
  --base <ref>      the commit in which the cited files were in the state the citations describe (for the nine
                    datasheet sets built by 2026-10-01, `4a59fab8`)
  --apply           write the remapped numbers. Without it the tool only REPORTS what it would change.

HOW IT WORKS (mechanical; it never interprets)
  A citation is a file name ending in .md or .txt followed by line references: `Official_Population_Census.md L382`,
  `Spec.md L128, L130`, `X.md L2113–2114`, or the newer Pre-Trip form `X.md` lines 2427–2452. The name is resolved to ONE file in the repo (by file name; when several files
  share a name the preceding folder text must pick one, else the citation is skipped and listed). The file is read at
  <ref> and as it is today; the lines are matched by their text (difflib), and every cited number is moved to the line
  that has the same text now. A number is left alone, and listed, when its line's text no longer exists (the line
  itself was edited: read it). A citation whose file did not exist at <ref> under that path is skipped and listed.

⚠ NOT IDEMPOTENT: it moves numbers from the state at <ref> to the state today. Run it ONCE per file per <ref>; running it again on an already-remapped file moves the numbers a second time. (Check `git diff` first, or restore the file from the commit, before rerunning.)

KNOWN LIMIT (found 2026-10-21): it does NOT read numbers wrapped in bold (`lines **382–391**`, `**487**`), so Pre-Trip census/extent bullets were never moved by it. For Pre-Trip sheets use `Tools/build_pretrip.py` (it recomputes those rows). Also choose `--base` carefully: a commit is only right if the files were in that state when the citations were written (the runbook moved on 2026-10-01 after the first sheets were verified).

WHAT IT DOES NOT DO: it does not check that a citation was right in the first place, only that it still points where
it did. Citations written AFTER <ref> (for example the founders rows refreshed 2026-10-21) are already current; pass a
<ref> that predates the datasheet, and expect no change for lines in files that did not shift.
"""
import difflib
import os
import re
import subprocess
import sys
import collections

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
SKIP_DIRS = ("graphify-out", os.sep + ".git" + os.sep, "node_modules")

CITE = re.compile(
    r"((?:[A-Za-z0-9_.()'\- ]+/)*[A-Za-z0-9_.()'\-]+\.(?:md|txt))(`?)(\s+)"
    r"(L\d+(?:[–-]\d+)?(?:,\s*L?\d+(?:[–-]\d+)?)*)")
CITE_LINES = re.compile(
    r"((?:[A-Za-z0-9_.()'\- ]+/)*[A-Za-z0-9_.()'\-]+\.(?:md|txt))(`?)(\s+lines?\s+)"
    r"(\d+(?:[–-]\d+)?(?:,\s*\d+(?:[–-]\d+)?)*)")
NUM = re.compile(r"(L?)(\d+)(?:([–-])(\d+))?")


def build_index():
    idx = collections.defaultdict(list)
    for d, ds, fs in os.walk(REPO):
        if any(s in d + os.sep for s in SKIP_DIRS):
            continue
        for f in fs:
            if f.endswith((".md", ".txt")):
                idx[f].append(os.path.join(d, f))
    return idx


def git_show(ref, rel):
    r = subprocess.run(["git", "-C", REPO, "show", "%s:%s" % (ref, rel)], capture_output=True)
    return r.stdout.decode("utf-8", "replace").split("\n") if r.returncode == 0 else None


_map_cache = {}


def line_map(ref, path):
    """old line number -> new line number, by matching line text. None if the file is not usable."""
    if path in _map_cache:
        return _map_cache[path]
    rel = os.path.relpath(path, REPO)
    old = git_show(ref, rel)
    if old is None:
        _map_cache[path] = None
        return None
    new = open(path, encoding="utf-8", errors="replace").read().split("\n")
    sm = difflib.SequenceMatcher(None, [l.strip() for l in old], [l.strip() for l in new], autojunk=False)
    mp, edited = {}, set()
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                mp[i1 + k + 1] = j1 + k + 1
        elif tag == "replace" and (i2 - i1) == (j2 - j1):
            # a block of lines edited IN PLACE keeps its position: the citation follows the line, and the line
            # is listed so a human re-reads what it says now
            for k in range(i2 - i1):
                mp[i1 + k + 1] = j1 + k + 1
                edited.add(i1 + k + 1)
    _map_cache[path] = (mp, len(old), len(new), edited)
    return _map_cache[path]


def resolve(name_with_dirs, idx):
    base = os.path.basename(name_with_dirs.strip())
    cands = idx.get(base, [])
    if len(cands) == 1:
        return cands[0], None
    if not cands:
        return None, "no such file"
    hint = name_with_dirs.strip().strip("`").replace("/", os.sep)
    if os.sep in hint:
        good = [c for c in cands if c.endswith(hint)]
        if len(good) == 1:
            return good[0], None
        # the hint's folder words must all be folders of the candidate (`Specs/Casey.md` -> Specs/<subnet>/Casey.md)
        words = [w for w in hint.split(os.sep)[:-1] if w.strip()]
        good = [c for c in cands if all(w in c.split(os.sep) for w in words)]
        if len(good) == 1:
            return good[0], None
    return None, "name is ambiguous (%d files)" % len(cands)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--base" not in sys.argv or not args:
        print(__doc__)
        return 2
    base = sys.argv[sys.argv.index("--base") + 1]
    args = [a for a in args if a != base]
    target = os.path.abspath(args[0])
    files = [target] if os.path.isfile(target) else sorted(
        os.path.join(d, f) for d, _, fs in os.walk(target) for f in fs if f.endswith(".md"))
    apply = "--apply" in sys.argv
    idx = build_index()
    total_moved = total_cites = 0
    unmatched, reread, skipped = [], [], collections.Counter()
    per_file = collections.OrderedDict()
    for fpath in files:
        text = open(fpath, encoding="utf-8").read()
        moved_here = [0]

        def fix(m):
            nonlocal total_cites
            name, tick, ws, refs = m.group(1), m.group(2), m.group(3), m.group(4)
            path, why = resolve(name, idx)
            if path is None:
                skipped["%s: %s" % (os.path.basename(name), why)] += 1
                return m.group(0)
            lm = line_map(base, path)
            if lm is None:
                skipped["%s: not at %s under that path" % (os.path.basename(name), base)] += 1
                return m.group(0)
            mp, nold, nnew, edited = lm
            total_cites += 1

            def one(n):
                a = int(n.group(2))
                b = int(n.group(4)) if n.group(4) else None
                na = mp.get(a) if a <= nold else a
                nb = (mp.get(b) if b <= nold else b) if b else None
                if na is None or (b and nb is None):
                    unmatched.append((os.path.relpath(fpath, REPO), os.path.basename(name), n.group(0)))
                    return n.group(0)
                if a in edited or (b and b in edited):
                    reread.append((os.path.relpath(fpath, REPO), os.path.basename(name), n.group(0), na, nb))
                if na != a or (b and nb != b):
                    moved_here[0] += 1
                return "%s%d%s" % (n.group(1), na, ("%s%d" % (n.group(3), nb)) if b else "")
            return name + tick + ws + NUM.sub(one, refs)
        new_text = CITE_LINES.sub(fix, CITE.sub(fix, text))
        if moved_here[0]:
            per_file[os.path.relpath(fpath, REPO)] = moved_here[0]
            total_moved += moved_here[0]
            if apply:
                open(fpath, "w", encoding="utf-8").write(new_text)
    print("%s  base %s  (%d file(s) searched)" % ("APPLIED" if apply else "DRY RUN", base, len(files)))
    print("citations checked: %d   line numbers moved: %d   in %d file(s)" % (total_cites, total_moved, len(per_file)))
    for f, n in per_file.items():
        print("  %4d  %s" % (n, f))
    if reread:
        print("\nFOLLOWED THE LINE, WHICH WAS EDITED IN PLACE (the number is right; re-read what the line says now): %d" % len(reread))
        for f, n, c, na, nb in reread[:80]:
            print("  %s: %s %s -> %s" % (f, n, c, "%d%s" % (na, ("-%d" % nb) if nb else "")))
    if unmatched:
        print("\nLEFT AS WRITTEN: the cited line's text no longer exists (the line itself was edited); read each: %d" % len(unmatched))
        for f, n, c in unmatched[:60]:
            print("  %s: %s %s" % (f, n, c))
    if skipped:
        print("\nSKIPPED:")
        for k, v in skipped.most_common():
            print("  %3d  %s" % (v, k))
    return 0


if __name__ == "__main__":
    sys.exit(main())
