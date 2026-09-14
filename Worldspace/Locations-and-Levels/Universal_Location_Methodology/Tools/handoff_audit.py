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

        state = NONE
        if FORMAL_PAT.search(text):
            state = FORMAL
        elif INFORMAL_PAT.search(text):
            state = INFORMAL

        in_hf = in_sweep = False
        rows = 0
        for line in lines:
            s = line.strip()
            if "HANDED FORWARD" in line:
                in_hf, in_sweep = True, False
            elif s.startswith("#"):
                in_hf = False
                in_sweep = bool(FORMAL_PAT.search(line))
            if in_hf and s.startswith("|"):
                mm = TARGET_PAT.match(s)
                if mm:
                    outbound[int(re.sub(r"\D", "", mm.group(1)))].append((src, s[:100]))
            if in_sweep and s.startswith("|") and not re.match(r"^\|[\s:|-]+\|$", s):
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
    print("  POSITIVE (detector must find a formal block): phases %s"
          % (", ".join(map(str, sorted(pos))) or "NONE FOUND"))
    print("  NEGATIVE (detector must find nothing)       : phases %s"
          % (", ".join(map(str, sorted(neg))) or "none"))
    print("  INSTRUMENT VALID: %s"
          % ("YES - both classes present, detector discriminates" if pos and neg
             else "NO - detector never discriminated; DO NOT TRUST THESE VERDICTS"))
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
