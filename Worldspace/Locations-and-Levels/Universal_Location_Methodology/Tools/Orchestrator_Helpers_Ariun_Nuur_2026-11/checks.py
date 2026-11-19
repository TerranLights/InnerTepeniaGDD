#!/usr/bin/env python3
"""Orchestrator checks for one T8 unit's merged output (read-only).
usage: checks.py <output.md> <list.txt> <brief.md>
Prints: the per-quotation pre-check, the American English sweep, and the other-location name scan."""
import re, sys

out, lst, brief = sys.argv[1:4]

def norm(s):
    s = re.sub(r'[*_`]', '', s)
    s = s.replace('’', "'").replace('‘', "'").replace('–', '-').replace('—', '-')
    s = re.sub(r'\s+', ' ', s)
    return s.strip().lower()

def load_span(path, ranges):
    L = open(path, encoding='utf-8', errors='ignore').read().split('\n')
    if not ranges:
        return '\n'.join(L)
    keep = []
    for part in ranges.split(','):
        part = part.strip()
        if '-' in part:
            a, b = part.split('-'); keep.extend(L[int(a) - 1:int(b)])
        else:
            keep.append(L[int(part) - 1])
    return '\n'.join(keep)

corpus = []
for line in open(lst, encoding='utf-8'):
    line = line.strip()
    if not line:
        continue
    if ' :: ' in line:
        p, r = line.split(' :: ', 1)
    else:
        p, r = line, None
    corpus.append(load_span(p, r))
corpus.append(open(brief, encoding='utf-8').read())
C = norm('\n'.join(corpus))

text = open(out, encoding='utf-8').read()
quotes = []
for l in text.split('\n'):
    pos = [i for i, ch in enumerate(l) if ch == '"']
    for k in range(0, len(pos) - 1, 2):
        s = l[pos[k] + 1:pos[k + 1]]
        if len(s) >= 6:
            quotes.append(s)
quotes += re.findall(r'“([^”]{6,}?)”', text)
checked = 0; miss = []
for q in quotes:
    parts = [p for p in re.split(r'…|\.\.\.', q) if len(p.strip()) >= 4]
    if not parts:
        continue
    checked += 1
    if not all(norm(p) in C for p in parts):
        miss.append(q)
print(f'quoted strings checked: {checked} not found: {len(miss)}')
for m in miss:
    print('  MISS:', m[:160])

brit = re.compile(r"\b(\w*(?:colour|honour|behaviour|favour|labour|neighbour|harbour|rumour|vapour|armour|flavour)\w*|centre[sd]?|metres?|litres?|theatres?|fibres?|licence[sd]?|defence|offence|catalogue[sd]?|analys(?:e|ed|es|ing)|travell(?:ed|ing|er|ers)|modell(?:ed|ing)|cancell(?:ed|ing)|(?:organ|real|recogn|emphas|summar|categor|priorit|minim|maxim|optim|util|character|standard|normal|special|stabil|central|author|apolog|critic|final|memorial|civil|colon|industrial|urban|visual|symbol|harmon|synchron|famil|internal|legal|local|global|capital|formal|general|mobil|neutral|polar|revital|steril|subsid|theor|weapon|modern)is(?:e|ed|es|ing|ation|ations)|grey|whilst|amongst|programmes?|tyres?|aluminium|sceptic\w*|manoeuvr\w*)\b", re.I)
hits = [(i, m.group(0)) for i, l in enumerate(text.split('\n'), 1) for m in brit.finditer(l)]
print(f'{out.split("/")[-1]} British-form hits: {hits}')

names = ['Concordia', 'Zhongshan', 'Davis', 'Casey', 'Mawson', 'Kunlun', 'Byrd', 'Janbogo', 'Zukelli', 'Shirayuki',
         'Sinheung', 'Relung Panen', 'Esperanza', 'Belgrano', 'Halley', 'Lazar', 'Neumayer', 'Scott', 'Fort McMurdo',
         'Pergamino', 'Contrapunto', 'Dome Fuji', 'Amundsen', 'Mirny', 'Mawson', 'Cape Adare', 'Dumont', 'Progress',
         'Syowa', 'Troll', 'Palmer', 'Rothera', 'Vernadsky', 'Marambio', 'Bellingshausen', 'Great Wall', 'Jang Bogo']
nh = {}
for i, l in enumerate(text.split('\n'), 1):
    for n in names:
        if re.search(r'\b' + re.escape(n) + r'\b', l):
            nh.setdefault(n, []).append(i)
print(f'other-location name scan (names: line numbers): {nh}')
print('tower-name count:', len(re.findall(r'(?i)amundsen tower', text)))
