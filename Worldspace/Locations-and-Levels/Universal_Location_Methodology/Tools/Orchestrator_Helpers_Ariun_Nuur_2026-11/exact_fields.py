#!/usr/bin/env python3
"""Exact (un-normalized) check of PROOF L1 and LLAST against the source's first and last admitted lines. usage: exact_fields.py <reader.md>..."""
import sys, re
for f in sys.argv[1:]:
    t = open(f).read().split('\n'); bad = 0; n = 0
    for i, l in enumerate(t):
        if not l.startswith('### PROOF: '): continue
        path = l[11:].strip(); blk = {}
        for x in t[i+1:i+9]:
            m = re.match(r'^(LRANGE|L1|LLAST): ?(.*)$', x)
            if m: blk[m.group(1)] = m.group(2)
        try: src = open(path).read().split('\n')
        except Exception as e: print(f, 'cannot open', path); continue
        if src and src[-1] == '': src = src[:-1]
        r = blk.get('LRANGE', 'FULL').strip()
        if r == 'FULL': first, last = 1, len(src)
        else:
            nums = [int(x) for x in re.findall(r'\d+', r)]; first, last = nums[0], nums[-1]
        for k, ln in (('L1', first), ('LLAST', last)):
            if k not in blk: continue
            n += 1; want = src[ln-1].rstrip(); got = blk[k].rstrip()
            if got == '' and want.strip() == '': continue
            if got != want and got.strip() != want.strip():
                bad += 1; print(f'{f.split("/")[-1]}  {path.split("/")[-1]}  {k} L{ln}\n   claimed: {got[:110]!r}\n   source : {want[:110]!r}')
    print(f'{f.split("/")[-1]}: {n} fields compared exactly, {bad} differ')
