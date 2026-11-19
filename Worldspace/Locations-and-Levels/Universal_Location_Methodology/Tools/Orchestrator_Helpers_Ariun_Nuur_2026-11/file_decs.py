#!/usr/bin/env python3
"""File a unit's developer questions into the decisions file (orchestrator helper).
usage: file_decs.py <unit file name> <unit label> <first Q> <last Q> <first DEC> <previous DEC>"""
import re, sys, shutil
fn, label, q1, q2, d1, prev = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
C = '/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/'
src = open(C + 'City_Development_Passes/Mirny_Subnet/Ariun_Nuur/' + fn).read().split('\n')
want = set(range(q1, q2 + 1)); rows = {}
for l in src:
    m = re.match(r'^\| Q-(\d+) \|', l)
    if m and int(m.group(1)) in want and int(m.group(1)) not in rows:
        rows[int(m.group(1))] = l
assert sorted(rows) == sorted(want), (sorted(want - set(rows)))
blocks = ''
for k, q in enumerate(sorted(rows)):
    c = [x.strip() for x in rows[q].strip().strip('|').split('|')]
    question, rec = c[1], c[2]; srcr = c[3] if len(c) > 3 else ''
    blocks += (f"### DEC-{d1+k} · PROVISIONAL · 2026-11-19 · Ariun Nuur, {label} (Q-{q})\n- **Question.** {question}\n"
               f"- **Recommended (PROVISIONAL).** {rec}\n- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/{fn}`, "
               f"Questions for the developer, Q-{q} (raised by {srcr}).\n\n")
p = C + 'Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md'
shutil.copy(p, f'/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/9d90e9d3-c049-471e-860e-caf23e07bb73/scratchpad/DECISIONS_backup_before_DEC{d1}.md')
s = open(p).read()
a = s.index(f'### DEC-{prev} · '); j = s.index('\n## Answered', a)
s = s[:j].rstrip('\n') + '\n\n' + blocks.rstrip('\n') + '\n' + s[j:]
open(p, 'w').write(s)
print(f'filed DEC-{d1} to DEC-{d1+len(rows)-1} ({len(rows)})')
