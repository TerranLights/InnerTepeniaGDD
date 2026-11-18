#!/usr/bin/env python3
"""Copy a phase's ledger marks (its '## Ledger marks for PN' table: position | mark | key) into 00.2's PN column, keys only.
usage: .t8_tool_ledger.py <N> <phase file>"""
import sys, datetime
N=int(sys.argv[1]); ph=open(sys.argv[2]).read()
sec=ph.split('## Ledger marks for P%d'%N,1)[1].split('\n## ',1)[0]
names={'the child':'The Child','the lover, as a position':'The Lover *(position)*','the lover as a position':'The Lover *(position)*','the parent':'The Parent','the ruler':'The Ruler','the elder':'The Elder','the mentor':'The Mentor','the passer-through':'The Passer-Through','the neighbor':'The Neighbor','the lover faculty':'⭐ The Lover FACULTY'}
marks={}
for l in sec.split('\n'):
    if l.startswith('| The') or l.startswith('| **The'):
        c=[x.strip().strip('*').strip() for x in l.strip().strip('|').split('|')]
        k=c[0].lower().replace('*','').strip()
        assert k in names, k
        mark=c[1].strip(); key=c[2].strip() if len(c)>2 else ''
        marks[names[k]] = key if mark and mark.lower() not in ('','—','-','blank','no') and not mark.lower().startswith('no') else ''
assert len(marks)==9, marks
L=open('00.2_Position_Coverage_Ledger.md').read().split('\n')
hdr=[l for l in L if l.startswith('| Position |')][0].split('|')
col=[i for i,c in enumerate(hdr) if c.strip()=='P%d'%N][0]
for row,v in marks.items():
    for i,l in enumerate(L):
        if l.startswith('| '+row+' |'):
            cells=l.split('|'); cells[col]=(' '+v.replace('|','/')+' ') if v else ' '; L[i]='|'.join(cells)
open('00.2_Position_Coverage_Ledger.md','w').write('\n'.join(L))
for k,v in marks.items(): print('%-26s %s'%(k, v or '(blank)'))
