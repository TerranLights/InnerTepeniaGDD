#!/usr/bin/env python3
"""Roll each extraction file's '## Restrained-handling register' into Content_Filter_Denials_Log.md (Part B2).
Re-run any time: python3 extractions/_rollup_register.py   (from the Dark_Humor_Research folder)."""
import glob, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log = os.path.join(ROOT, 'Content_Filter_Denials_Log.md')
BEGIN, END = '<!-- AUTO-REGISTER-BEGIN -->', '<!-- AUTO-REGISTER-END -->'
parts = []
for f in sorted(glob.glob(os.path.join(ROOT, 'extractions', 'E*.md'))):
    t = open(f, encoding='utf-8').read()
    m = re.search(r'^## Restrained-handling register\s*$', t, re.M)
    if not m:
        continue
    body = t[m.end():]
    n = re.search(r'^(## |Read:)', body, re.M)
    body = body[:n.start()] if n else body
    body = body.strip()
    rows = len([l for l in body.split('\n') if l.startswith('|') and not re.match(r'^\|[\s\-|]+\|$', l) and 'Finding' not in l.split('|')[1:2][0:1].__str__()])
    parts.append('### %s\n\n%s\n' % (os.path.basename(f), body))
block = BEGIN + '\n\n## Part B2 — Registers from each extraction file (auto-rolled-up; regenerate with `extractions/_rollup_register.py`)\n\n*Files whose agents were told to keep a formal register. Line numbers are in the source text file named in each table. Retry ask for every row: quote the withheld wording (public-domain WWI sources at length where the example is the point; others briefly), as an addendum to the finding.*\n\n' + '\n'.join(parts) + '\n' + END
s = open(log, encoding='utf-8').read()
if BEGIN in s:
    s = re.sub(re.escape(BEGIN) + r'.*?' + re.escape(END), lambda _: block, s, flags=re.S)
else:
    s = s.replace('\n---\n\n## Part C', '\n---\n\n' + block + '\n\n---\n\n## Part C', 1)
open(log, 'w', encoding='utf-8').write(s)
print('files rolled up:', len(parts))
