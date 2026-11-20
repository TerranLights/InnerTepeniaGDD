#!/usr/bin/env python3
"""File bullet-form questions (- **Q-n · (tag)** text *Recommended:* rec *(source.)*) into the decisions file.
usage: file_decs_bullets.py <unit file> <label> <first Q> <last Q> <first DEC> <previous DEC> [--dry]"""
import re, sys, shutil
fn, label, q1, q2, d1, prev = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]); dry='--dry' in sys.argv
C = '/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/'
L = open(C + 'City_Development_Passes/Mirny_Subnet/Ariun_Nuur/' + fn).read().split('\n')
rows = {}; cur = None
for l in L:
    m = re.match(r'^- \*\*Q-(\d+)(?: ◆)?(?: · (.*?))?(?:\*\*(?!\*)\s*(.*))?$', l)
    if m:
        cur = int(m.group(1)); rows.setdefault(cur, [m.group(2) or '', m.group(3) if m.group(3) is not None else '**OPEN**']); continue
    if cur is not None and l.startswith('  ') and l.strip():
        rows[cur][1] += ' ' + l.strip(); continue
    cur = None
want = set(range(q1, q2 + 1)); assert want <= set(rows), sorted(want - set(rows))
blocks = ''
for k, q in enumerate(sorted(want)):
    tag, text = rows[q]
    if text.startswith('**OPEN**'):
        rest = text[len('**OPEN**'):]
        i = rest.find('**'); tag = tag + ' ' + rest[:i].strip(); text = rest[i+2:] if i >= 0 else rest
    tag = tag.strip().strip('()')
    src = ''
    text = re.sub(r'\s+-\s+\*', ' *', text)
    mb = re.search(r'\s*\*\[([^\]]*)\]\*\s*$', text)
    if mb: src = mb.group(1); text = text[:mb.start()]
    ms = re.search(r'\s*\*\(([^()]*(?:\([^()]*\)[^()]*)*)\)\*\s*$', text)
    if ms and not src: src = ms.group(1).rstrip('.'); text = text[:ms.start()]
    if '*Recommended:*' in text: question, rec = text.split('*Recommended:*', 1)
    else: question, rec = text, '(see the source)'
    if len(tag) > 40 or not question.strip(' -'):
        question = (tag + ' ' + question.strip(' -')).strip(); tag = ''
    blocks += (f"### DEC-{d1+k} · PROVISIONAL · 2026-11-20 · Ariun Nuur, {label} (Q-{q}{', ' + tag.strip() if tag.strip() else ''})\n"
               f"- **Question.** {question.strip()}\n- **Recommended (PROVISIONAL).** {rec.strip()}\n"
               f"- **Where:** `City_Development_Passes/Mirny_Subnet/Ariun_Nuur/{fn}`, Questions for the developer, Q-{q}"
               f"{' (raised by ' + src + ')' if src else ''}.\n\n")
if dry: print(blocks); print('...', len(want)); sys.exit()
p = C + 'Research_Logs/DECISIONS_NEEDED_FROM_DEVELOPER.md'
shutil.copy(p, f'/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/f3e3ba60-3018-46e7-b33a-2aecaa179ab5/scratchpad/DECISIONS_backup_before_DEC{d1}.md')
s = open(p).read()
a = s.index(f'### DEC-{prev} · '); j = s.index('\n## Answered', a)
s = s[:j].rstrip('\n') + '\n\n' + blocks.rstrip('\n') + '\n' + s[j:]
open(p, 'w').write(s)
print(f'filed DEC-{d1} to DEC-{d1+len(want)-1} ({len(want)})')
