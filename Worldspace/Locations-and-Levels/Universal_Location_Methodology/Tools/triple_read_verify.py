#!/usr/bin/env python3
"""
TRIPLE-READ VERIFY  —  ULM instrument, ON TRIAL
(see PRE-TRIP_INSPECTION_RECIPE_TRIAL.md T8, S9.1)

Mechanically checks THREE subagents' self-reported "proof of reading" blocks against
the REAL files on disk. This is the Round-2 ground-truth half of T8 — the Round-3
agent-to-agent comprehension cross-check is NOT this script's job (a script cannot
judge whether a finding is a genuine reading of the material; it can only judge
whether a quoted line is the real line).

  usage:  python3 triple_read_verify.py <required_files.txt> <agent1_proof.md> <agent2_proof.md> <agent3_proof.md>

  required_files.txt   one entry per line - the resolved reading list for the
                        step/phase under check (from the pass's own §C/§D table):

                            /abs/path/to/file.md
                            /abs/path/to/partial.md :: 1-134,143
                            /abs/path/to/section.md :: AUTO

                        A bare path means the whole file is admissible. After ' :: '
                        comes the ADMISSIBLE RANGE - comma-separated line numbers and
                        N-M spans, 1-indexed and inclusive. AUTO means the reader
                        locates the range itself (a named section) and declares it in
                        LRANGE; the script then verifies against the reader's own
                        claim and reports any disagreement between readers.
  agentN_proof.md       each subagent's proof block, in the fixed format below

PROOF FORMAT each subagent must emit, once per required file, inside its own output:

  ### PROOF: <absolute path>
  LRANGE: <the admissible range the reader was bound to, or FULL>
  LINES: <integer, the subagent's own count OF THE ADMISSIBLE RANGE>
  L1: <exact text of the first admissible line, verbatim>
  LMID: <exact text of the middle admissible line ((N+1)//2, 1-indexed within range)>
  LLAST: <exact text of the LAST ADMISSIBLE line, verbatim>
  QUOTE: <one load-bearing sentence, exact, from INSIDE the admissible range>

WHY THIS SHAPE: a subagent that skimmed the first screen and stopped cannot produce
the correct LMID or LLAST text, because it does not know the file's real length or
what sits at its far end. A subagent that fabricates cannot produce line text that
happens to match the real file byte-for-byte. Reusing the exact-match method already
validated for R-25 (quotation_audit.py) rather than inventing a new one.

⛔ WHAT THIS DOES NOT PROVE: that the reading was UNDERSTOOD, only that it HAPPENED.
Comprehension is Round 3's job (agent-to-agent), not this script's.

⭐ RANGE SUPPORT ADDED 2026-09-11 (M-218, found on Davis Step −1). The original
version read every file whole. Two consequences, both measured, not theorized:

  1. LLAST pointed at the file's last line even when the contract stopped earlier —
     so an HONEST reader who correctly stopped at the contract boundary FAILED, and
     the only way to pass was to read forbidden material. The verification instrument
     required violating the input contract in order to prove compliance with it.
  2. The QUOTE check searched the WHOLE file, so a reader quoting a line from the
     FORBIDDEN range passed silently. That is the worse half: defect 1 punishes
     honesty, defect 2 rewards contamination.

Both are fixed by making the admissible range - not the file - the unit of proof.
"""

import hashlib
import os
import re
import sys

DASHES = dict.fromkeys(map(ord, "—–−"), "-")
QUOTES = {0x2019: "'", 0x2018: "'", 0x201C: '"', 0x201D: '"'}


def norm(s):
    s = s.translate(DASHES).translate(QUOTES)
    s = re.sub(r"[*`_\[\]>|#]", " ", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def parse_range(spec, total):
    """'1-134,143' -> [1..134, 143], 1-indexed and clamped to the real file length.

    Returns None for FULL/empty (meaning: the whole file), so callers can tell
    'no restriction' apart from 'a restriction that happens to cover everything'.
    """
    spec = (spec or "").strip()
    if not spec or re.fullmatch(r"(?i)\s*(full|all|whole)\s*", spec):
        return None
    # Drop parenthetical asides BEFORE scanning. Readers annotate this field in prose
    # and the asides carry line numbers that are not part of the range - measured, on
    # the first real run: one reader wrote "L1-134 u {L143}   (file length 181)" and
    # another "L2390-2414 (... next heading at L2416)". A scan that keeps the asides
    # silently widens the admissible range to include the very lines under quarantine,
    # which is the opposite of what this parser is for.
    spec = re.sub(r"\([^)]*\)", " ", spec)
    # Then scan for spans and bare numbers rather than splitting on separators: a
    # split-based parser either chokes on the remaining prose or mangles it (an early
    # version replaced every letter "u" with a comma).
    keep = set()
    for lo, hi, solo in re.findall(r"[Ll]?(\d+)\s*[-–—]\s*[Ll]?(\d+)|[Ll]?(\d+)", spec):
        if solo:
            keep.add(int(solo))
        else:
            keep.update(range(int(lo), int(hi) + 1))
    if not keep:
        return "BAD"
    return sorted(n for n in keep if 1 <= n <= total)


def first_int(s):
    """The first integer outside any parenthetical aside, or None."""
    m = re.search(r"\d+", re.sub(r"\([^)]*\)", " ", str(s)))
    return int(m.group()) if m else None


def real_facts(path, spec=None):
    """Ground truth for the ADMISSIBLE RANGE, not for the file."""
    with open(path, encoding="utf-8", errors="ignore") as fh:
        lines = fh.read().split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    picked = parse_range(spec, len(lines))
    if picked == "BAD":
        return None
    sel = lines if picked is None else [lines[n - 1] for n in picked]
    n = len(sel)
    if n == 0:
        return {"LINES": 0, "L1": "", "LMID": "", "LLAST": "", "TEXT": ""}
    mid = (n + 1) // 2
    return {"LINES": n, "L1": sel[0], "LMID": sel[mid - 1], "LLAST": sel[-1],
            "TEXT": norm("\n".join(sel))}


def locate(path, quote):
    """Where a rejected quote really came from - as a LINE NUMBER, never as text.

    ⛔ The failure message must not reproduce the quarantined line. A reader that
    quoted forbidden material has contaminated itself; printing that material into
    the audit log contaminates every later reader of the log, which is the exact
    failure the range check exists to catch. The line number and a hash prove the
    same point and carry no payload.
    """
    with open(path, encoding="utf-8", errors="ignore") as fh:
        lines = fh.read().split("\n")
    q = norm(quote)
    for i, line in enumerate(lines, 1):
        if q and q in norm(line):
            return "found at L%d, outside the admissible range" % i
    return "not found anywhere in this file - fabricated"


def render_claim(path, claimed, admissible_text):
    """Print a wrong claim WITHOUT reproducing forbidden material.

    A plain typo or an invention is safe to echo and is much easier to diagnose with
    the text in hand. Real text from outside the admissible range is not: echoing it
    turns the audit log into the leak. So: redact only what is genuinely in the file
    and genuinely out of contract, and show everything else.
    """
    if not claimed:
        return "''"
    if norm(claimed) in admissible_text:
        return repr(claimed[:60])
    where = locate(path, claimed)
    if where.startswith("found"):
        return "[REDACTED - %s, sha1:%s]" % (
            where, hashlib.sha1(norm(claimed).encode()).hexdigest()[:12])
    return repr(claimed[:60])


def parse_proof(path):
    text = open(path, encoding="utf-8", errors="ignore").read()
    blocks = {}
    current = None
    field = None
    for line in text.split("\n"):
        m = re.match(r"^#{0,3}\s*PROOF:\s*(.+)$", line.strip())
        if m:
            current = m.group(1).strip()
            blocks[current] = {}
            field = None
            continue
        if current is None:
            continue
        blocks[current].setdefault("_RAW", "")
        blocks[current]["_RAW"] += line + "\n"
        m = re.match(r"^(LRANGE|LINES|L1|LMID|LLAST|QUOTE)\s*:\s*(.*)$", line.strip())
        if m:
            field = m.group(1)
            blocks[current][field] = m.group(2)
        elif field and line.strip():
            # allow a proof value to wrap onto a following line
            blocks[current][field] += " " + line.strip()
    return blocks


NEWLINE_CLAIM = re.compile(
    r"no\s+trailing\s+newline|not\s+newline[- ]terminated|lacks?\s+a\s+trailing\s+newline"
    r"|missing\s+(?:a\s+)?trailing\s+newline", re.I)


def check_newline_claim(path, raw):
    """Catch the FABRICATED PREMISE, independently of whether the count is right.

    Measured across two T8 rounds: four readers reported LINES wrong, every error was
    exactly +1, and every one carried the same sentence - "this file has no trailing
    newline." None of them ran `tail -c 1`. It is the locally correct answer to "when
    does wc -l undercount," it costs nothing to assert, and it dissolves the
    discrepancy between a tool display's line numbering and the real file.

    The count alone is a weak trap: LMID uses (N+1)//2, which absorbs an off-by-one
    whenever N is odd, and LLAST comes from the file rather than from N - so nothing
    inside the block contradicts a wrong N. And no midpoint formula fixes that: any
    function that halves N collides on some N/N+1 pair. So check the CLAIM instead of
    relying on the count to expose it. A reader that asserts this about a
    newline-terminated file has stated a checkable byte-level fact without checking
    it, in a report whose entire purpose is verified reading - which is worth flagging
    even on the occasions when the arithmetic happens to survive.
    """
    if not raw or not NEWLINE_CLAIM.search(raw):
        return None
    with open(path, "rb") as fh:
        if fh.seek(0, 2) == 0:
            return None
        fh.seek(-1, 2)
        if fh.read(1) == b"\n":
            return "claims 'no trailing newline'; file ENDS WITH 0x0a"
    return None


def parse_required(req_file):
    """Each line is '<path>' or '<path> :: <rangespec>'."""
    out = []
    for line in open(req_file, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "::" in line:
            path, spec = line.split("::", 1)
            out.append((path.strip(), spec.strip()))
        else:
            out.append((line, None))
    return out


def main():
    if len(sys.argv) < 5:
        print(__doc__)
        return 2
    req_file, a1, a2, a3 = sys.argv[1:5]
    required = parse_required(req_file)
    agents = {"agent1": parse_proof(a1), "agent2": parse_proof(a2), "agent3": parse_proof(a3)}

    print("required files: %d" % len(required))
    print("agents: %s" % ", ".join(agents))
    print("")

    all_pass = True
    for path, spec in required:
        exists = os.path.exists(path)
        label = path if spec is None else "%s  [range %s]" % (path, spec)
        print("=== %s ===" % label)
        if not exists:
            print("  ⛔ FILE DOES NOT EXIST ON DISK - cannot verify, treat as a hole")
            all_pass = False
            continue

        # AUTO: the reader locates its own range, so ground truth is per-agent and the
        # readers disagreeing about WHICH range is itself a finding worth printing.
        auto = (spec or "").strip().upper() == "AUTO"
        if auto:
            # Compare PARSED ranges. Readers annotate LRANGE differently while meaning
            # the identical span, and flagging that as disagreement trains the operator
            # to ignore the warning - which is how a real disagreement gets missed.
            nlines = sum(1 for _ in open(path, encoding="utf-8", errors="ignore"))
            spans = {}
            for n, b in agents.items():
                raw = (b.get(path) or {}).get("LRANGE", "").strip()
                if not raw:
                    continue
                got = parse_range(raw, nlines)
                spans[n] = "FULL" if got is None else ("BAD" if got == "BAD" else
                                                       (min(got), max(got), len(got)))
            if len(set(map(str, spans.values()))) > 1:
                print("  ⚠ READERS DISAGREE ON THE RANGE: %s" % spans)
                all_pass = False
        truth = None if auto else real_facts(path, spec)
        if truth is None and not auto:
            print("  ⛔ UNPARSEABLE RANGE SPEC %r - fix required_files.txt" % spec)
            all_pass = False
            continue

        for name, blocks in agents.items():
            proof = blocks.get(path)
            if proof is None:
                print("  %-8s ⛔ NO PROOF BLOCK FOR THIS FILE" % name)
                all_pass = False
                continue
            ok = True

            if auto:
                truth = real_facts(path, proof.get("LRANGE", ""))
                if truth is None:
                    print("  %-8s ⛔ UNPARSEABLE LRANGE %r" % (name, proof.get("LRANGE", "")))
                    all_pass = False
                    continue
            elif spec is not None:
                # A reader that says FULL on a ranged file either ignored the contract
                # or read past it. Either way the proof is not evidence of compliance.
                declared = parse_range(proof.get("LRANGE", ""), 10 ** 9)
                if declared is None:
                    ok = False
                    print("  %-8s ⛔ LRANGE claims FULL, but this file is ranged %r"
                          % (name, spec))
                elif declared == "BAD":
                    ok = False
                    print("  %-8s ⛔ LRANGE UNPARSEABLE: %r" % (name, proof.get("LRANGE", "")))

            for field in ("LINES", "L1", "LMID", "LLAST"):
                claimed = str(proof.get(field, "")).strip()
                actual = str(truth[field]).strip()
                if field == "LINES":
                    # Compare the NUMBER, not the annotation. Readers append their
                    # working ("135   (file length is 181)"), and a raw string compare
                    # fails a reader whose count is exactly right - measured on the
                    # first real run, where it produced a false failure while the
                    # genuine off-by-one on another file looked identical.
                    match = first_int(claimed) == first_int(actual)
                else:
                    match = norm(claimed) == norm(actual)
                if not match:
                    ok = False
                    print("  %-8s ⛔ %-5s MISMATCH  claimed=%s  actual=%r"
                          % (name, field, render_claim(path, claimed, truth["TEXT"]),
                             actual[:60]))

            quote = proof.get("QUOTE", "").strip()
            if not quote:
                ok = False
                print("  %-8s ⛔ NO QUOTE" % name)
            elif norm(quote) not in truth["TEXT"]:
                # Scoped to the admissible range on purpose: a quote pulled from
                # outside it is contamination, and the old whole-file search passed it.
                ok = False
                where = locate(path, quote)
                print("  %-8s ⛔ QUOTE NOT IN ADMISSIBLE RANGE  (%s, sha1:%s)"
                      % (name, where, hashlib.sha1(norm(quote).encode()).hexdigest()[:12]))

            bad_claim = check_newline_claim(path, proof.get("_RAW", ""))
            if bad_claim:
                ok = False
                print("  %-8s ⛔ UNVERIFIED BYTE-LEVEL CLAIM: %s" % (name, bad_claim))

            if ok:
                print("  %-8s ✅ all fields match ground truth" % name)
            all_pass = all_pass and ok
        print("")

    print("=== VERDICT ===")
    print("UNANIMOUS - CLEARED TO WRITE" if all_pass else
          "⛔ NOT UNANIMOUS - DO NOT WRITE. Log which agent/file failed and why.")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
