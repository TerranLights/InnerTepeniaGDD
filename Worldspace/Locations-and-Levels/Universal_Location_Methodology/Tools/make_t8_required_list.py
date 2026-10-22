#!/usr/bin/env python3
"""
MAKE T8 REQUIRED LIST  —  builds a DRAFT reading list for one step or phase of a city pass from that city's own
Pre-Trip sheet, so Round 0 of every three-reader dispatch stops being hand-built (November To-Do N-3, 2026-10-21).

  usage:  python3 make_t8_required_list.py <pass_folder> <target> [--include-pass-files] [--write] [--force]

  <pass_folder>  the city's pass folder, e.g. .../City_Development_Passes/Mirny_Subnet/Mirny
  <target>       step:-1 | step:0 | step:1 | step:2 | step:3 | step:5 ... step:10 | phase:2 ... phase:10
                 (Step 4 is not dispatched as a unit; it runs per phase.)
  --include-pass-files
                 also write, as entries, the pass's own output files that come BEFORE the target (Frame, Steps 1-3,
                 earlier phases, earlier steps), as bare paths. Use for Steps 5-10, which read the finished pass;
                 the Step -1 contract's admitted line ranges still have to be added by hand where it restricts a file.
  --write        write the list to <pass_folder>/.t8_required_<NN>_<name>.txt (the existing convention)
                 instead of printing it. Refuses to overwrite an existing list unless --force.

WHAT IT DOES (all of it mechanical; none of it interpretation)
  1. Finds the target's `T8` block in the Pre-Trip sheet (00.0_Pre-Trip_Inspection.md) and extracts every absolute
     path written in backticks inside it. A path followed by a section anchor (§"Step 5") becomes `path :: AUTO`
     with the anchor kept as a comment: the reader locates the named section itself (triple_read_verify.py's AUTO).
  2. For a phase, also extracts the absolute addresses in the Pre-Trip's per-phase table rows for that phase, and
     those in the Phase Spine's MUST OPEN block for that phase (03_The_Phase_Spine.md).
  3. Adds the STANDARD entries (the same for every city) from ../T8_Standard_Entries.json, re-locating each stored
     line range in today's file by the text of its first and last line and flagging any span it cannot verify; then
     adds the city's own datasheet for the target (Datasheets/Step_N.md or Phase_N.md) when it exists.
  4. Checks that every path exists. A missing path is written as a comment and makes the exit status 1.
  5. Lists, as comments, the pass's own earlier output files that exist, in order, so the orchestrator can add the
     ones the step's rules admit.
  6. Prints a summary and an ENTRY-RANGE SENTENCE computed from the list itself (never typed by hand; Mirny's Step 9
     brief miscounted its own list by one, `T8_Standing_Brief_Lines.md` line 7).

WHAT IT DOES NOT DO (so nobody mistakes the draft for a finished list)
  * It does NOT decide which earlier pass files a step admits, nor at which line ranges (the Step -1 input contract
    and the step's own rules decide that). Those are listed as comments for the orchestrator to move up.
  * It does NOT resolve a directory address into files; a directory is written as a comment to resolve by hand.
  * It does NOT line-check section anchors; `:: AUTO` hands the range to the readers, and the orchestrator should
    replace it with checked ranges where the step needs them.
  * It never reads the content of any listed file (it only tests that the path exists). It reads only the Pre-Trip.
"""
import json
import os
import re
import sys

PRE = "00.0_Pre-Trip_Inspection.md"

NAMES = {  # target -> (file number, name), matching the existing .t8_required_* convention
    "step:-1": ("00.1", "StepMINUS1"), "step:0": ("00", "Step0"), "step:1": ("01", "Step1"),
    "step:2": ("02", "Step2"), "step:3": ("03", "Step3"),
    "step:5": ("05", "Step5"), "step:6": ("06", "Step6"), "step:7": ("07", "Step7"), "step:8": ("08", "Step8"),
    "step:9": ("09", "Step9"), "step:10": ("10", "Step10"),
}
for _n in range(2, 11):
    NAMES["phase:%d" % _n] = ("04", "Phase%d" % _n)

PASS_ORDER = ["00_Frame.md", "01_Inherited.md", "02_Spine.md", "03_Research.md"]


def datasheet_name(target):
    kind, n = target.split(":")
    return ("Step_%s.md" % n) if kind == "step" else ("Phase_%s.md" % n)


def block_re(target):
    kind, n = target.split(":")
    label = "Step" if kind == "step" else "Phase"
    num = ("[−-]1|MINUS1|MINUS-1") if n == "-1" else re.escape(n)
    return re.compile(r"🧪\s*`T8`\s*—\s*\*\*%s\s+(?:%s)(?![0-9])" % (label, num))


def find_block(lines, target):
    rx = block_re(target)
    for i, l in enumerate(lines):
        if rx.search(l):
            for j in range(i, min(i + 40, len(lines))):
                if "triple_read_verify" in lines[j]:
                    return lines[i:j + 1]
            return lines[i:i + 8]
    return None


def find_step_reads(lines, target):
    """Newer Pre-Trip format: a `### Step N — name` section holding a `**`T8` reads:**` bullet list whose nested
    bullets give a path and, usually, `lines a-b` or `in full`. Returns (path, range_spec, anchor) tuples, or None."""
    kind, n = target.split(":")
    if kind != "step":
        return None
    num = "[−-]1" if n == "-1" else re.escape(n)
    head = re.compile(r"^###\s+Step\s+%s(?![0-9])" % num)
    start = next((i for i, l in enumerate(lines) if head.match(l)), None)
    if start is None:
        return None
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("### ") or lines[i].startswith("## ")), len(lines))
    sec = lines[start:end]
    r0 = next((i for i, l in enumerate(sec) if "T8" in l and "reads" in l), None)
    if r0 is None:
        return None
    out = []
    for l in sec[r0 + 1:]:
        if re.match(r"^- ", l) or (l.strip() and not l.startswith("  ")):
            break
        pm = re.search(r"`(/[^`]+)`", l)
        if not pm:
            continue
        path = pm.group(1).strip()
        rest = l[pm.end():]
        lm = re.search(r"lines?\s+(.*)", rest)
        pieces = []
        if lm:
            # the first stated span is the step's own governing text (plain or bold); later plain spans in a note are not
            # entries, but later BOLD numbers are (the census and extent bullets list their rows that way: `**262–266**`)
            for k, tm in enumerate(re.finditer(r"(\*\*)?(\d+)(?:\s*[–-]\s*(\d+))?(\*\*)?", lm.group(1))):
                bold = bool(tm.group(1) and tm.group(4))
                if k == 0 or bold:
                    a, b = int(tm.group(2)), int(tm.group(3) or tm.group(2))
                    if k == 0 and not tm.group(3) and not bold:
                        continue                # a lone plain number first (e.g. a line in a note) is not a span
                    pieces.append((a, b))
        spans = pieces
        anchor = None
        spec = None
        if "§" in rest and not spans:
            anchor = "§" + rest.split("§", 1)[1].strip()
        elif spans:
            spec = ",".join(("%d-%d" % (a, b)) if a != b else ("%d" % a) for a, b in sorted(set(spans)))
        out.append((path, spec, anchor))
    return out


def extract_entries(block_lines):
    """Backticked absolute paths, each with the text that follows it up to the next backtick (an anchor, if any)."""
    entries = []
    text = "\n".join(block_lines)
    for m in re.finditer(r"`(/[^`]+)`([^`\n]*)", text):
        raw, tail = m.group(1).strip(), m.group(2)
        anchor = None
        mm = re.match(r"^(\S.*?)\s+§(.*)$", raw)
        if mm:
            raw, anchor = mm.group(1).strip(), "§" + mm.group(2).strip().rstrip(" +")
        elif re.match(r"^\s*(§|\+|in full|and)", tail) and "§" in tail:
            anchor = tail.strip(" +")
        if raw.startswith("/"):
            entries.append((raw, anchor))
    return entries


def phase_rows(lines, n):
    rows = []
    in_d = False
    for l in lines:
        if l.startswith("## D"):
            in_d = True
        elif l.startswith("## ") and in_d and not l.startswith("## D"):
            break
        if in_d and l.startswith("| **%s** |" % n):
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            if len(cells) >= 3:
                for m in re.finditer(r"`(/[^`]+)`", cells[2]):
                    entries_note = cells[5] if len(cells) > 5 else ""
                    rows.append((m.group(1).strip(), None, entries_note))
    return rows


STANDARD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "T8_Standard_Entries.json")
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".."))


def _nearest(idxs, want):
    return min(idxs, key=lambda i: abs(i - want)) if idxs else None


def resolve_piece(lines, piece):
    """Re-find a range piece by the text of its first and last line. Returns (a, b, status)."""
    a0, b0, first, last = piece["a"], piece["b"], piece["first"], piece["last"]
    span = b0 - a0
    f_idx = [i + 1 for i, l in enumerate(lines) if l.strip() == first] if len(first) >= 12 else []
    l_idx = [i + 1 for i, l in enumerate(lines) if l.strip() == last] if len(last) >= 12 else []
    if f_idx and l_idx:
        a = _nearest(f_idx, a0)
        cands = [i for i in l_idx if i >= a]
        b = _nearest(cands, a + span) if cands else None
        if b is not None and abs((b - a) - span) <= max(3, span // 20):
            return a, b, "moved" if (a, b) != (a0, b0) else "same"
    if f_idx and not l_idx:
        a = _nearest(f_idx, a0)
        if a + span <= len(lines):
            return a, a + span, "first-line-only"
    if l_idx and not f_idx:
        b = _nearest(l_idx, b0)
        if b - span >= 1:
            return b - span, b, "last-line-only"
    return a0, b0, "UNVERIFIED"


def standard_entries(target):
    """Entries that are the same for every city (T8_Standard_Entries.json), with ranges re-located in today's files."""
    if not os.path.exists(STANDARD):
        return [], []
    data = json.load(open(STANDARD, encoding="utf-8"))["entries"].get(target, [])
    out, warns = [], []
    for e in data:
        path = os.path.join(REPO, e["path"])
        if not os.path.exists(path):
            out.append("# MISSING STANDARD ENTRY: %s" % path)
            warns.append(path)
            continue
        if e.get("whole"):
            out.append(path)
        elif e.get("auto") or not e.get("pieces"):
            out.append("%s :: AUTO" % path)
            out.append("#   ^ standard entry with no stored range; line-check it")
        else:
            lines = open(path, encoding="utf-8", errors="replace").read().split("\n")
            parts, status = [], []
            for pc in e["pieces"]:
                a, b, s = resolve_piece(lines, pc)
                parts.append("%d-%d" % (a, b) if a != b else "%d" % a)
                status.append(s)
            out.append("%s :: %s" % (path, ",".join(parts)))
            moved = [s for s in status if s != "same"]
            if moved:
                out.append("#   ^ re-located in today's file (%s); %s" % (", ".join(sorted(set(moved))),
                           "LINE-CHECK: some spans could not be verified" if any(s in ("UNVERIFIED", "first-line-only", "last-line-only") for s in status) else "fingerprints matched"))
                if any(s == "UNVERIFIED" for s in status):
                    warns.append(path)
    return out, warns


SPINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "03_The_Phase_Spine.md")


def spine_must_open(n):
    """Absolute addresses in the spine's MUST OPEN block for Phase n (the blocks appear in phase order, Phase 0 first)."""
    if not os.path.exists(SPINE):
        return []
    text = open(SPINE, encoding="utf-8").read().split("\n")
    starts = [i for i, l in enumerate(text) if "MUST OPEN" in l and l.lstrip().startswith("> ###")]
    idx = int(n)
    if idx >= len(starts):
        return []
    end = starts[idx + 1] if idx + 1 < len(starts) else len(text)
    block = "\n".join(text[starts[idx]:end])
    found = []
    for m in re.finditer(r"`(/[^`]+)`", block):
        found.append((m.group(1).strip(), None, "spine MUST OPEN"))
    return found


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) < 2:
        print(__doc__)
        return 2
    pass_dir, target = os.path.realpath(args[0]), args[1]
    if target not in NAMES:
        print("unknown target %r. Use step:-1, step:0..3, step:5..10 or phase:2..10." % target)
        return 2
    pre = os.path.join(pass_dir, PRE)
    if not os.path.exists(pre):
        print("no Pre-Trip sheet at %s (build it first: PRE-TRIP_INSPECTION_RECIPE.md)" % pre)
        return 2
    lines = open(pre, encoding="utf-8").read().split("\n")
    block = find_block(lines, target)
    reads = find_step_reads(lines, target) if block is None else None
    if block is None and reads is None:
        print("no T8 block found for %s in the Pre-Trip sheet" % target)
        return 2

    if reads is not None:
        ents = [(p, (("RANGE:" + spec) if spec else a), "") for p, spec, a in reads]
    else:
        ents = [(p, a, "") for p, a in extract_entries(block)]
    if target.startswith("phase:"):
        ents += phase_rows(lines, target.split(":")[1])
        ents += spine_must_open(target.split(":")[1])

    out, seen = [], set()
    missing, unresolved, dirs, ranged = [], [], [], 0
    for p, anchor, note in ents:
        if p in seen:
            continue
        seen.add(p)
        if p.endswith("/") or os.path.isdir(p):
            dirs.append(p)
            out.append("# DIRECTORY, resolve to files by hand (read its own README first): %s%s"
                       % (p, ("   [%s]" % note) if note else ""))
        elif not os.path.exists(p):
            missing.append(p)
            out.append("# MISSING PATH (not written as an entry): %s" % p)
        elif anchor and anchor.startswith("RANGE:"):
            out.append("%s :: %s" % (p, anchor[6:]))
        elif anchor:
            unresolved.append((p, anchor))
            out.append("%s :: AUTO" % p)
            out.append("#   ^ anchor %s  (AUTO: the readers locate it; replace with a line-checked range where the step needs one)" % anchor)
        else:
            out.append(p)
    std_lines, std_warns = standard_entries(target)
    for l in std_lines:
        pth = l.split(" :: ")[0]
        if l.startswith("#"):
            out.append(l)
        elif pth in seen:
            # the Pre-Trip already named this path; keep the standard entry only if it carries ranges
            if " :: " in l and not l.endswith(":: AUTO"):
                out[:] = [x for x in out if x != pth and not x.startswith(pth + " :: AUTO")]
                out.append(l)
        else:
            seen.add(pth)
            out.append(l)
    # drop an anchor comment whose AUTO entry the standard entry replaced
    cleaned = []
    for l in out:
        if l.startswith("#   ^ anchor") and not (cleaned and cleaned[-1].endswith(":: AUTO")):
            continue
        cleaned.append(l)
    out[:] = cleaned
    ds = os.path.join(pass_dir, "Datasheets", datasheet_name(target))
    if os.path.exists(ds) and ds not in seen:
        out.append(ds)

    kind, n = target.split(":")
    def before(f):
        """True if pass file f comes before the target's own output."""
        m = re.match(r"^04_Phase_(\d\d)_", f)
        if kind == "phase":
            if m:
                return int(m.group(1)) < int(n)
            return f in PASS_ORDER
        if f in PASS_ORDER:
            return True
        if m:
            return True
        m2 = re.match(r"^(0[5-9]|10)_", f)
        return bool(m2) and int(m2.group(1)) < int(n)
    avail = []
    for f in PASS_ORDER:
        if os.path.exists(os.path.join(pass_dir, f)):
            avail.append(f)
    for f in sorted(os.listdir(pass_dir)):
        if re.match(r"^04_Phase_\d\d_", f) or re.match(r"^0[5-9]_|^10_", f):
            avail.append(f)
    # only files that come before this step's own output
    avail = [f for f in avail if before(f)]
    if "--include-pass-files" in sys.argv:
        for f in avail:
            full = os.path.join(pass_dir, f)
            if full not in seen:
                seen.add(full)
                out.append(full)
        avail = []
    if avail:
        out.append("# PASS FILES THAT EXIST (the step's rules and the Step -1 contract decide which are admitted, and at which ranges):")
        for f in avail:
            out.append("#   %s" % os.path.join(pass_dir, f))

    entries = [l for l in out if l and not l.startswith("#")]
    total = len(entries)
    n_pre = len(ents) - len(missing) - len(dirs)
    n_pre = max(0, min(n_pre, total))
    n_ds = 1 if os.path.exists(ds) else 0
    n_pass = total - n_pre - n_ds
    parts = ["entries 1-%d are the Pre-Trip addresses" % n_pre] if n_pre else []
    if n_ds:
        parts.append("entry %d is the city's own datasheet" % (n_pre + 1))
    if n_pass > 0:
        parts.append("entries %d-%d are the pass's own earlier files" % (n_pre + n_ds + 1, total))
    sentence = "The list has %d entries: %s." % (total, "; ".join(parts) if parts else "none classified")

    header = ["# Draft list built by Tools/make_t8_required_list.py for %s (%s). Replace each AUTO and add the admitted pass files by hand." %
              (os.path.basename(pass_dir), target)]
    text = "\n".join(header + out) + "\n"

    print("target       : %s   pass: %s" % (target, os.path.basename(pass_dir)))
    print("entries      : %d   AUTO anchors to check: %d   directories to resolve: %d   missing paths: %d"
          % (total, len(unresolved), len(dirs), len(missing)))
    print("entry sentence (computed): %s" % sentence)
    if "--write" in sys.argv:
        num, nm = NAMES[target]
        path = os.path.join(pass_dir, ".t8_required_%s_%s.txt" % (num, nm))
        if os.path.exists(path) and "--force" not in sys.argv:
            print("REFUSING to overwrite existing %s (use --force)" % path)
            return 2
        open(path, "w", encoding="utf-8").write(text)
        print("wrote %s" % path)
    else:
        print("-" * 78)
        print(text)
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
