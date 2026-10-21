#!/usr/bin/env python3
"""
HANDOFF AUDIT  —  ULM instrument, ON TRIAL (see 04_QA_Gates_and_Differentiation.md Part V.2)

Reconciles the two sides of the handoff ledger, which nothing currently does.

  usage:  python3 handoff_audit.py <pass_folder>

A pass writes handoffs OUT in "HANDED FORWARD" blocks and sweeps them IN by hand (00.0 §H).
Nothing checks that the two sides agree, so a row addressed to Phase 8 can evaporate and no
instrument notices. On the pass this was written for, five did, and the loss was found by
accident two phases later.

  OUTBOUND  = rows in "HANDED FORWARD" tables addressed to "| **Phase N** |"
  INBOUND   = FORMAL  - a titled sweep block, enumerated, greppable
              INFORMAL- the sweep is mentioned in prose but never enumerated
              NONE    - no trace at all
  MISMATCH  = a number, not an opinion

⛔ TRIAGE BY HAND. A mismatch is not automatically a defect: one outbound row can legitimately
discharge as several inbound rows, or be refused with a reason.

⚠ THE HARD FAILURE is not a mismatch. It is NONE - a phase with rows addressed to it and no
trace of having read them. That is what actually happened.

REPAIRED 2026-10-21 (Mirny handoff decision 13, group A; M-284). Two defects: (1) the validity control demanded a phase
with NO sweep block in the pass itself, which a healthy pass never has, so it printed "INSTRUMENT VALID: NO" on every run
from Phase 5 to Step 8; the control is now a built-in self-test on two fixed strings (one that must read FORMAL, one that
must read NONE), independent of the pass. (2) the sweep row count included the table's header row, so it ran one higher than
the table; only data rows (after the separator line) are counted now.

⚠ AND THE INSTRUMENT'S OWN LIMIT, STATED BECAUSE PART V's FIRST TRIAL LEARNED IT THE HARD WAY:
this detects a FORM, not an act. A phase that ran the sweep perfectly and wrote no block reads
as NONE. That is a false positive, and it is also the finding - a step with no required form
cannot be audited at all. Read the controls below before trusting any verdict.
"""

import os
import re
import sys
import glob
import collections

FORMAL_PAT = re.compile(r"INBOUND\s+HANDOFF|HANDOFF\s+SWEEP", re.I)
INFORMAL_PAT = re.compile(r"§H\b|handed\s+to\s+this\s+phase|inbound\s+docket", re.I)
TARGET_PAT = re.compile(r"^\|\s*\*{0,2}(?:⭐|⛔|⚠|\s)*\*{0,2}\s*(Phase\s*\d+)\s*\*{0,2}\s*\|", re.I)
PHASE_NUM = re.compile(r"04_Phase_(\d+)")

FORMAL, INFORMAL, NONE = "FORMAL", "informal", "NONE"


def classify(text):
    """The same three-way classification scan() uses, so the self-test exercises the real detector."""
    if FORMAL_PAT.search(text):
        return FORMAL
    if INFORMAL_PAT.search(text):
        return INFORMAL
    return NONE


def self_test():
    """Built-in positive and negative controls, independent of the pass being audited."""
    pos = classify("## INBOUND HANDOFF SWEEP\n| row |\n|---|\n| a |\n")
    neg = classify("## Findings\nNothing is said here about earlier phases.\n")
    return pos == FORMAL and neg == NONE


def scan(pass_dir):
    files = sorted(glob.glob(os.path.join(pass_dir, "04_Phase_*.md")))
    outbound = collections.defaultdict(list)
    sweeps = {}

    for f in files:
        src = os.path.basename(f)
        m = PHASE_NUM.search(src)
        pn = int(m.group(1)) if m else None
        text = open(f, encoding="utf-8").read()
        lines = text.split("\n")

        state = classify(text)

        in_hf = in_sweep = False
        rows = 0
        seen_sep = False
        for line in lines:
            s = line.strip()
            if not s.startswith("|"):
                seen_sep = False
            if "HANDED FORWARD" in line:
                in_hf, in_sweep = True, False
            elif s.startswith("#"):
                in_hf = False
                in_sweep = bool(FORMAL_PAT.search(line))
            if in_hf and s.startswith("|"):
                mm = TARGET_PAT.match(s)
                if mm:
                    outbound[int(re.sub(r"\D", "", mm.group(1)))].append((src, s[:100]))
            if in_sweep and s.startswith("|"):
                if re.match(r"^\|[\s:|-]+\|$", s):
                    seen_sep = True          # the header row above it is not a data row
                elif seen_sep:
                    rows += 1
        if pn is not None:
            sweeps[pn] = (state, rows)
    return outbound, sweeps, files


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    pass_dir = os.path.realpath(sys.argv[1])
    if not os.path.isdir(pass_dir):
        print("not a directory: %s" % pass_dir)
        return 2

    outbound, sweeps, files = scan(pass_dir)
    print("pass audited : %s" % os.path.basename(pass_dir))
    print("phase files  : %d" % len(files))
    print("")

    # ---- CONTROLS. Part V's first trial: an instrument with no controls reports
    # ---- numbers you cannot trust. Name the known-good and known-bad cases.
    print("=== CONTROLS (edit these per pass; they are what makes a zero trustworthy) ===")
    pos = [p for p, (st, _) in sweeps.items() if st == FORMAL]
    neg = [p for p, (st, _) in sweeps.items() if st == NONE]
    print("  PHASES WITH A FORMAL SWEEP BLOCK (found in this pass): %s"
          % (", ".join(map(str, sorted(pos))) or "none"))
    print("  PHASES WITH NO TRACE OF A SWEEP (found in this pass)  : %s"
          % (", ".join(map(str, sorted(neg))) or "none"))
    ok = self_test()
    print("  SELF-TEST (fixed positive and negative strings)       : %s" % ("passed" if ok else "FAILED"))
    print("  INSTRUMENT VALID: %s"
          % ("YES - the detector separates a formal block from no block on the built-in controls" if ok
             else "NO - the built-in controls failed; DO NOT TRUST THESE VERDICTS"))
    print("")

    print("  phase | outbound | sweep    | rows | verdict")
    print("  ------+----------+----------+------+---------")
    hard = 0
    for pn in sorted(sweeps):
        n_out = len(outbound.get(pn, []))
        state, n_in = sweeps[pn]
        if n_out == 0:
            v = "n/a - nothing addressed to it"
        elif state == NONE:
            v = "*** NONE - %d ROWS UNACCOUNTED ***" % n_out
            hard += 1
        elif state == INFORMAL:
            v = "informal only - %d rows never enumerated" % n_out
            hard += 1
        elif n_in == 0:
            v = "*** BLOCK EMPTY ***"
            hard += 1
        else:
            v = "reconcile %d enumerated against %d outbound" % (n_in, n_out)
        print("  %5d | %8d | %-8s | %4d | %s" % (pn, n_out, state, n_in, v))

    print("")
    print("TOTAL outbound handoff rows: %d" % sum(len(v) for v in outbound.values()))
    print("PHASES WITH ROWS ADDRESSED TO THEM AND NO ENUMERATION: %d" % hard)
    print("")
    print("=== outbound rows, per target, for hand reconciliation ===")
    for pn in sorted(outbound):
        print("  -> Phase %d:" % pn)
        for src, t in outbound[pn]:
            print("       [%s]  %s" % (src, t[:88]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
