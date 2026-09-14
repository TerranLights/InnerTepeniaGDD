#!/usr/bin/env python3
"""
QUOTATION AUDIT  —  ULM instrument, ON TRIAL (see 04_QA_Gates_and_Differentiation.md Part V)

Checks every quoted string in a location pass against the canon corpus it claims to quote.

  usage:  python3 quotation_audit.py <pass_folder> [--canon-only]

  <pass_folder>   the location pass to audit, e.g.  .../Mirny_Subnet/Zhongshan_Opus
  --canon-only    exclude ALL city passes from the corpus, not just this one, so a
                  quotation must validate against canon rather than against a sibling
                  pass. Stricter. NOT the mode the Zhongshan_Opus baseline was run in —
                  use the default if you want a number comparable to that baseline.

WHY IT IS SHAPED THIS WAY — three properties, each from a recorded failure:

  1. NORMALIZE HARD (dashes, curly quotes, markdown structure, case, whitespace).
     Prose files are hard-wrapped, so a multi-word pattern is broken somewhere. A naive
     grep returns FALSE NEGATIVES SILENTLY. 04 Part IV: "a zero from a scan is not a
     result until you have proved the scan could have found a hit."

  2. EXCLUDE THE PASS'S OWN FOLDER. Otherwise a quotation validates against itself and
     every quote "passes."

  3. HARD POSITIVE CONTROLS + A NEGATIVE CONTROL. On the first Zhongshan run the controls
     passed only because none of them spanned a line wrap — the instrument reported
     234/430 "missing" and was junk. An instrument whose positive controls are all easy
     reports zeroes you cannot trust.

The ellipsis split is the point of the whole tool: a quote written with "..." is testing
two independent fragments, and each side must be found on its own.
"""

import os
import re
import sys
import glob

BASE = "/home/kuroskalacs/Documents/Doll-Fi/media/"
GDD = BASE + "games/Inner Tepenia/InnerTepeniaGDD/"
ROOTS = [GDD + "Worldspace", GDD + "Reference", BASE + "Reference/TepenianUniverseTimeline"]
EXTRA = [GDD + "CLAUDE.md"]          # a repo-root file outside Worldspace. Omitting it
                                     # was a real defect in the first Zhongshan run.
PASSES_DIR = "City_Development_Passes"

DASHES = dict.fromkeys(map(ord, "—–−"), "-")
QUOTES = {0x2019: "'", 0x2018: "'", 0x201C: '"', 0x201D: '"'}


def norm(s):
    s = s.translate(DASHES).translate(QUOTES)
    s = re.sub(r"[*`_\[\]>|#]", " ", s)
    s = re.sub(r"[^\w\s'\"/.,;:()%\-]", " ", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def build_corpus(pass_dir, canon_only):
    pass_real = os.path.realpath(pass_dir)
    chunks, seen = [], set()
    for root in ROOTS:
        for dirpath, _, filenames in os.walk(root):
            real = os.path.realpath(dirpath)
            if "graphify-out" in dirpath:
                continue
            if real == pass_real or real.startswith(pass_real + os.sep):
                continue                                  # property 2
            if canon_only and PASSES_DIR in dirpath:
                continue
            for fn in filenames:
                if not fn.endswith(".md"):
                    continue
                p = os.path.join(dirpath, fn)
                if p in seen:
                    continue
                seen.add(p)
                try:
                    with open(p, encoding="utf-8", errors="ignore") as fh:
                        chunks.append(norm(fh.read()))
                except OSError:
                    pass
    for p in EXTRA:
        if os.path.exists(p) and p not in seen:
            seen.add(p)
            with open(p, encoding="utf-8", errors="ignore") as fh:
                chunks.append(norm(fh.read()))
    return len(chunks), "   ".join(chunks)


CONTROLS = [
    ("easy", "a terminus is nobody's midpoint"),
    ("HARD - blockquote wrap",
     "A pass may not proceed to Step 5 with a NEVER CITED row that nobody has looked at and explained"),
    ("HARD - outside Worldspace",
     "Paste raw QA scan output into the QA block. Never summarize it"),
    ("HARD - case mismatch",
     "YOU GO TO ESPERANZA AND YOU DO NOT COME HOME FOR FOUR YEARS"),
    ("HARD - long wrapped",
     "Different content is not differentiation; a different question is"),
]
NEGATIVE = "the quiet city runs entirely on geothermal steam from mount erebus"


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    canon_only = "--canon-only" in sys.argv
    if not args:
        print(__doc__)
        return 2
    pass_dir = os.path.realpath(args[0])
    if not os.path.isdir(pass_dir):
        print("not a directory: %s" % pass_dir)
        return 2

    nfiles, corpus = build_corpus(pass_dir, canon_only)
    print("pass audited : %s" % os.path.basename(pass_dir))
    print("corpus mode  : %s" % ("CANON ONLY (no city passes)" if canon_only
                                 else "default (own pass excluded)"))
    print("corpus files : %d   chars: %s" % (nfiles, format(len(corpus), ",")))
    print("")

    print("=== POSITIVE CONTROLS ===")
    ok_all = True
    for kind, c in CONTROLS:
        ok = norm(c) in corpus
        ok_all &= ok
        print("  [%-26s] %-9s %s" % (kind, "FOUND" if ok else "NOT FOUND", c[:55]))
    print("")
    print("  INSTRUMENT VALID: %s" % ("YES" if ok_all else "NO - DO NOT TRUST ZEROES"))
    neg_ok = norm(NEGATIVE) not in corpus
    print("  NEGATIVE CONTROL (must be absent): %s"
          % ("PASS - absent" if neg_ok else "FAIL - found!"))
    if not (ok_all and neg_ok):
        print("")
        print("  >> STOP. The instrument did not validate. Any zero below is meaningless.")

    miss, tot = [], 0
    for f in sorted(glob.glob(os.path.join(pass_dir, "*.md"))):
        with open(f, encoding="utf-8") as fh:
            raw = fh.read()
        for lineno, line in enumerate(raw.split("\n"), 1):
            in_cell = line.lstrip().startswith("|")
            for q in re.findall(r'"([^"\n]{45,240})"', line):
                for frag in re.split(r"\.\.\.|…", q):     # property: split on elision
                    frag = norm(frag).strip(" .,;:-")
                    if len(frag.split()) < 7:
                        continue
                    tot += 1
                    if frag not in corpus:
                        miss.append((os.path.basename(f), lineno, in_cell, frag))

    cells = sum(1 for m in miss if m[2])
    print("")
    print("=== QUOTATION AUDIT ===")
    print("fragments tested (single-line, ellipsis-split, >=7 words): %d" % tot)
    print("NOT FOUND in corpus: %d" % len(miss))
    print("  of those, in TABLE CELLS : %d" % cells)
    print("  of those, in PROSE       : %d" % (len(miss) - cells))
    print("")
    for fn, lineno, cell, q in miss:
        print("  [%s:%d]%s  %s" % (fn, lineno, "  [CELL]" if cell else "         ", q[:130]))
    print("")
    print("⚠ TRIAGE BY HAND. A miss is not yet a defect: the pass quoting ITSELF, and")
    print("  connective prose captured between two adjacent quotations, both show here.")
    print("  Confirm each at source before calling it a defect.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
