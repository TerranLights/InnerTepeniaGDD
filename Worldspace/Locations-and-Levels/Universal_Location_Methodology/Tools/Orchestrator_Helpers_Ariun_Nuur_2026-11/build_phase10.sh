#!/bin/bash
# usage: build_phase10.sh  (after Phase 9 is recorded and the symbol entries are appended to the draft list)
set -e
S=/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/9d90e9d3-c049-471e-860e-caf23e07bb73/scratchpad/t8
cd $S
python3 -I make_phase_brief.py spec_phase10.py DRAFT_t8_brief_04_Phase10.md
python3 -I - <<'PY'
import runpy
S='/tmp/claude-1000/-home-kuroskalacs-Documents-Doll-Fi-media-games-Inner-Tepenia-InnerTepeniaGDD/9d90e9d3-c049-471e-860e-caf23e07bb73/scratchpad/t8/'
w=runpy.run_path(S+'spec_phase10.py')['WEB_RULES']
p=S+'DRAFT_t8_brief_04_Phase10.md'; b=open(p).read()
o='- **No web research at this phase** (Step 3 did it; its findings are in entry 16). A hole the research did not reach is a\n  request, never an inference (runbook M-158).'
assert b.count(o)==1, 'no-web rule not found'
b=b.replace(o,w+'\n- A hole the research did not reach is a request, never an inference (runbook M-158).')
open(p,'w').write(b); print('web rules in')
PY
