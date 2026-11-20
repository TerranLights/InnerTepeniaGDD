#!/usr/bin/env python3
"""Save an agent's latest SubagentHandback message to a file. usage: save_reply.py <agent_id> <dest> <header line>"""
import json, sys
T='/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/f3e3ba60-3018-46e7-b33a-2aecaa179ab5/tasks/'
aid, dest, head = sys.argv[1], sys.argv[2], sys.argv[3]
last=None
for l in open(T+aid+'.output'):
    try: d=json.loads(l)
    except Exception: continue
    m=d.get('message'); c=m.get('content') if isinstance(m,dict) else None
    if isinstance(c,list):
        for b in c:
            if b.get('type')=='tool_use' and b.get('name')=='SubagentHandback': last=b['input'].get('message')
open(dest,'w').write(head+'\n\n'+last.rstrip()+'\n')
v=[x for x in last.split('\n') if x.strip().startswith('VERDICT')][:2]
print(dest.split('/')[-1], len(last.split('\n')), 'lines;', ' | '.join(x.strip()[:40] for x in v))
