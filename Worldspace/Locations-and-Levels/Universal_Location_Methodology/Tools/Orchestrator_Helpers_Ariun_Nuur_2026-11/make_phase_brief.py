#!/usr/bin/env python3
"""Build a frozen T8 brief for one ULM phase unit of Ariun Nuur (orchestrator helper).
usage: make_phase_brief.py <spec.py> <out.md>
spec.py defines: N, TITLE, LISTNAME, ENTRIES (str), NENTRIES, RESEARCH_ENTRY, TASK (str), EXTRA4 (str), FIRST_RF, FIRST_REQ,
FIRST_Q, FIRST_ROW, FIRST_SH, SWEEP_FILES (str), WRITES (str)"""
import sys, runpy
here = '/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/9d90e9d3-c049-471e-860e-caf23e07bb73/scratchpad/t8/'
parts = runpy.run_path(here + 'phase_parts.py')
s = runpy.run_path(sys.argv[1])
PASS = ('/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/'
        'Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/')
rules = parts['RULES'].replace('RESEARCH_ENTRY', s['RESEARCH_ENTRY'])
brief = f'''# T8 Round 1 brief — Ariun Nuur, ULM Phase {s['N']} ({s['TITLE']}) — FROZEN at dispatch, 2026-11-19

You are one of three independent readers (A, B, C). You will not see the others' work until Round 3. This brief is final; no part of it
will be amended while you work (`00_RUNBOOK.md` L933–951). If anything in it cannot be satisfied, say so in your output; do not guess past it.

## 0 · Before anything else
1. **Create your output file first**, at the path given to you in your dispatch message (your own private staging folder; nobody else
   writes there), **with the Write tool**, and write to it only with Write and Edit. Create and delete no other file anywhere, temporary
   copies included; write intermediate notes inside your output file.
2. Start it with a `## 0 · Reading log`. Log each list entry as you finish reading it. If you are cut off, resume from your log.
3. The reading list is `{s['LISTNAME']}` in the pass folder
   `{PASS}`.
   **The list has {s['NENTRIES']} entries:** {s['ENTRIES']}
   Read the list file itself with Read before you begin. You may use `wc -l` and `sed -n 'Np'` on a listed file, inside its admitted
   range, only to check a count or a positional line. **No `grep`, `awk` or other command on any file, your own output file included.**

{parts['STD']}{rules}
## 3 · The task — write Ariun Nuur's Phase {s['N']} ({s['TITLE']}) — the real content, not a description of it
Follow the runbook's Step 4 (entry 1: open the phase's `MUST OPEN` block before writing; formalize before inventing; name the axis in
bold before the content; a null is a result; general-population and shadow-proportion discipline; push every finding to a physical or
behavioral expression; when you park a figure, list its downstream uses) and the phase spine's Phase {s['N']} (entry 2). Your output, after
the reading log, has these sections:

1. **`## Canon opened`** (`M-171`), at the head: ✅ what was OPENED · ⛔ what was REFUSED and why · ⚠ what was *n/a* for this city and why,
   one line per `MUST OPEN` address of the phase.
2. **The handoff sweep** (Pre-Trip §H), under a heading that contains the words *Handoff sweep*, **as a table** (one row per place:
   the place, what it hands, the discharge), so the handoff audit can count it; Block 1 for places that name the phase, Block 2 for places
   that reach it by generator, **each block under its own heading that also contains the words *Handoff sweep*** (the audit resets at
   every heading), and in the sweep rows write *handed-forward table*, never the capitalized table title: search {s['SWEEP_FILES']} for every row addressed to `Phase {s['N']}`
   (normalized: ignore emphasis marks and line wrapping), one row per distinct line or block, and discharge each: answered here,
   closed as not applicable with the reason, or carried to a named later phase or step with the reason (`DEC-715`, PROVISIONAL).
3. **The asymmetry check on inherited material first opened here** (`DEC-710`, PROVISIONAL): for each finding in a source first opened at
   this phase that describes a threshold, gate, conversion, verdict, admission or status change: both directions written? the side
   decided against; as durable? the route back; disposition. Rows numbered from {s['FIRST_ROW']}.
{s['TASK']}
- **Generators used:** a line beginning `Generators used:` naming which of G1–G8 this phase drew on, each citing its source rows.
- **HANDED FORWARD:** a table of rows this phase hands to later phases or steps, with the target in the form `| **Phase N** |` or
  `| **Step N** |`, what is handed, and why.
- **Positions covered** (the Pre-Trip's position-coverage ledger, bookkeeping only): which of The Child, The Lover (position), The
  Parent, The Ruler, The Elder, The Mentor, The Passer-Through, The Neighbor and the Lover faculty this phase's own content actually
  covers, each with the finding that covers it. **Never write toward a blank:** a position the phase does not reach stays blank.
- **`T4 - SHED:`** one line: what did this phase's axis have no use for?
- **Reserved findings** (from RF-{s['FIRST_RF']}), **shadow candidates** (from SH-{s['FIRST_SH']}), **requests** (from REQ-{s['FIRST_REQ']}) and
  **questions for the developer** (from Q-{s['FIRST_Q']}), each question with a recommended answer; use your own reader-range numbers (for
  example "RF-A1"); the merge assigns the final numbers.
- **Your PROOF blocks, one per list entry, LAST in your output, after every other section, with nothing written after your final QUOTE
  line**, in exactly this format:
{parts['PROOF']}{parts['S4']}{s['EXTRA4']}
## 5 · Hand back
Your final message to the orchestrator is a **receipt only**: your output file's path, its line count, the differentiation axis named,
the counts of findings, asymmetry rows, handed-forward rows, positions covered, reserved findings, shadows, requests and questions, the
handoff-sweep count, and `MANIFEST: read <k> of {s['NENTRIES']} entries; not reached — <entries or "none">`. Nothing else: no summary of
findings. The file this phase writes, after the merge, is `{s['WRITES']}`.
'''
open(sys.argv[2], 'w').write(brief)
print(len(brief.splitlines()), 'lines')
