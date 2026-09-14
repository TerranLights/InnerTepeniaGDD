#!/usr/bin/env python3
"""
PHASE DISCIPLINE CHECK  —  ULM instrument, ON TRIAL
(see PRE-TRIP_INSPECTION_RECIPE_TRIAL.md T3/T4/T5, and 04_QA_Gates_and_Differentiation.md Part V.2 C3-C5)

Checks the three phase-close disciplines that have no other checker:

  T3  the POSITION-COVERAGE LEDGER (00.2_Position_Coverage_Ledger.md) — reports which
      cells are blank, per phase. Does NOT judge whether a mark is correct — a blank
      is a fact about the ledger, not a verdict on the phase.
  T4  the per-phase SHED marker — every 04_Phase_*.md must carry one line answering
      "what did this phase's axis have no use for?" Reports presence/absence only.
  T5  the early Lover-faculty smoke test — Phase 6 carries an early marker with a
      verdict; Step 8's Review Panel carries the real one. Reports both verdicts
      side by side so a human can compare them; does not compare them itself,
      because "did the early run change the later phases" is a judgment call this
      tool cannot make from text alone.

  usage:  python3 phase_discipline_check.py <pass_folder>

⛔ TRIAGE BY HAND, same as the other two Tools/ scripts. This reports STRUCTURE
(is the marker there, what does it say) never CORRECTNESS (was the mark honest).
A pass can fail every check here and still be a good pass that simply didn't run
this trial edition — that is itself one of the trial's two informative outcomes
(PRE-TRIP_INSPECTION_RECIPE_TRIAL.md S9.3: "the obligation is to RECORD, not to
comply").

MARKERS THIS TOOL LOOKS FOR — defined once, here, so the recipe and the checker
cannot drift apart the way 00f's operational list and its output template did
(R-31):

  T3 ledger file  : 00.2_Position_Coverage_Ledger.md, a markdown table whose first
                     column is the nine positions and whose header row is phase
                     numbers (2..10).
  T4 marker       : a line in a 04_Phase_*.md file starting with (after markdown
                     stripping) "T4 - SHED:" or "T4 SHED:" (case-insensitive).
  T5 early marker : a line in the Phase 6 file starting with "T5 - EARLY LOVER
                     FACULTY:" (case-insensitive), verdict is the rest of the line.
  T5 late marker  : in 08_Review_Panel.md, the Lover faculty line inside the panel
                     output block (00f's own template names it "Lover faculty").
"""

import os
import re
import sys
import glob

POSITIONS = [
    "The Child", "The Lover", "The Parent", "The Ruler", "The Elder",
    "The Mentor", "The Passer-Through", "The Neighbor", "The Lover FACULTY",
]

T4_PAT = re.compile(r"T4\s*[-–]\s*SHED\s*:\s*(.*)", re.I)
T5_EARLY_PAT = re.compile(r"T5\s*[-–]\s*EARLY\s+LOVER\s+FACULTY\s*:\s*(.*)", re.I)
LOVER_FACULTY_PAT = re.compile(r"lover\s+faculty", re.I)

CELL_STRIP = re.compile(r"[*`_\[\]>#]")


def strip_md(s):
    return CELL_STRIP.sub("", s).strip()


def check_t3(pass_dir):
    print("=== T3 - POSITION-COVERAGE LEDGER ===")
    ledger = os.path.join(pass_dir, "00.2_Position_Coverage_Ledger.md")
    if not os.path.exists(ledger):
        print("  NOT FOUND: %s" % ledger)
        print("  T3 not applied this pass (or not yet reached its first phase close).")
        print("")
        return
    lines = [l for l in open(ledger, encoding="utf-8").read().split("\n") if l.strip().startswith("|")]
    if len(lines) < 2:
        print("  ledger file exists but contains no table")
        print("")
        return
    header = [c.strip() for c in lines[0].strip("|").split("|")]
    phases = header[1:]
    rows = []
    for line in lines[2:]:
        cells = [c.strip() for c in line.strip("|").split("|")]
        if not cells or not cells[0]:
            continue
        rows.append(cells)
    print("  phases in header: %s" % ", ".join(phases))
    for cells in rows:
        pos = strip_md(cells[0])
        marks = cells[1:]
        blanks = [phases[i] for i, m in enumerate(marks) if i < len(phases) and not m.strip()]
        filled = len(marks) - len(blanks)
        print("  %-22s filled=%-2d blank=%-2d  blank at: %s"
              % (pos, filled, len(blanks), ", ".join(blanks) if blanks else "-"))
    print("")
    print("  NOTE: a blank cell is a WARNING BEFORE Step 8, not a defect. Do not")
    print("  fill a blank by writing new phase content toward it - that is the")
    print("  contamination 00f Rule 3 forbids (see the recipe's hard bound on T3).")
    print("")


def check_t4(pass_dir):
    print("=== T4 - PER-PHASE SHED MARKER ===")
    files = sorted(glob.glob(os.path.join(pass_dir, "04_Phase_*.md")))
    if not files:
        print("  no 04_Phase_*.md files found")
        print("")
        return
    found, missing = 0, []
    for f in files:
        text = open(f, encoding="utf-8").read()
        hit = None
        for line in text.split("\n"):
            m = T4_PAT.search(strip_md(line))
            if m:
                hit = m.group(1).strip()
                break
        name = os.path.basename(f)
        if hit is not None:
            found += 1
            print("  [%s]  T4 present: %s" % (name, hit[:90]))
        else:
            missing.append(name)
    for name in missing:
        print("  [%s]  T4 MARKER ABSENT" % name)
    print("")
    print("  %d/%d phase files carry a T4 marker." % (found, len(files)))
    if found == len(files) and found > 0:
        print("  >> If EVERY phase's answer was literally 'nothing', T4 is falsified")
        print("     per its own stated condition (the question would be decorative).")
        print("     This tool cannot see the marker's CONTENT well enough to judge")
        print("     that - read the %d lines above by hand." % found)
    print("")


def check_t5(pass_dir):
    print("=== T5 - EARLY LOVER-FACULTY SMOKE TEST ===")
    phase6 = sorted(glob.glob(os.path.join(pass_dir, "04_Phase_06*.md")))
    early = None
    if phase6:
        text = open(phase6[0], encoding="utf-8").read()
        for line in text.split("\n"):
            m = T5_EARLY_PAT.search(strip_md(line))
            if m:
                early = m.group(1).strip()
                break
    if early is not None:
        print("  EARLY (Phase 6) verdict: %s" % early)
    else:
        print("  EARLY marker absent in %s" % (phase6[0] if phase6 else "(no Phase 6 file found)"))

    panel = os.path.join(pass_dir, "08_Review_Panel.md")
    late = None
    if os.path.exists(panel):
        text = open(panel, encoding="utf-8").read()
        for line in text.split("\n"):
            if LOVER_FACULTY_PAT.search(line):
                late = strip_md(line)[:140]
                break
    if late is not None:
        print("  LATE (Step 8) mention   : %s" % late)
    else:
        print("  LATE marker absent (08_Review_Panel.md missing or has no Lover-faculty line yet)")

    print("")
    if early is not None and late is not None:
        print("  Both present. COMPARE BY HAND: if the early verdict changed what any")
        print("  phase between 6 and 8 wrote, T5 is FALSIFIED per its own stated")
        print("  condition and must be withdrawn, not quietly kept.")
    else:
        print("  T5 not fully applied this pass (one or both markers absent).")
    print("")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    pass_dir = os.path.realpath(sys.argv[1])
    if not os.path.isdir(pass_dir):
        print("not a directory: %s" % pass_dir)
        return 2
    print("pass audited : %s" % os.path.basename(pass_dir))
    print("")
    check_t3(pass_dir)
    check_t4(pass_dir)
    check_t5(pass_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
