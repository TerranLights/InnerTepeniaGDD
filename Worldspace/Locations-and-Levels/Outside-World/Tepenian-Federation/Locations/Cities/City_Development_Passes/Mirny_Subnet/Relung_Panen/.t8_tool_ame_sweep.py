#!/usr/bin/env python3
"""American English sweep: British spellings by word-boundary regex. Prints each hit with its line.
'judgement' is the one kept British form and is reported but not counted. Usage: ame_sweep.py <file> [...]"""
import re, sys
PAT = r"\b(\w*(?:colour|favour|honour|labour|harbour|neighbour|behaviour|rumour|vapour|savour|flavour|endeavour|armour|humour|odour|valour|vigour|parlour|splendour|tumour)\w*|\w*(?:organis|realis|recognis|characteris(?!tic)|emphasis(?!ed\b)|summaris|categoris|prioritis|minimis|maximis|utilis|standardis|normalis|finalis|apologis|criticis|analys(?:e|ed|es|ing)\b|paralys(?:e|ed|es|ing)\b|catalys(?:e|ed|es|ing)\b)\w*|centre\w*|metre\w*|litre\w*|theatre\w*|fibre\w*|calibre|sombre|meagre|defence|offence|licence|pretence|practis\w*|travell\w*|cancell\w*|modell\w*|labell\w*|levell\w*|signall\w*|fuell\w*|counsell\w*|jewell\w*|grey\w*|plough\w*|programme\w*|catalogue\w*|dialogue\w*|analogue\w*|tonne\w*|aluminium|sulphur\w*|manoeuvr\w*|aeroplane\w*|towards|amongst|whilst|learnt|spelt|dreamt|burnt|judgement\w*|acknowledgement\w*|enrol\b|enrolment|fulfil\b|fulfilment|instalment|ageing|storey\w*|kerb\w*|tyre\w*|cheque\w*|gaol\w*|mould\w*|moult\w*|smoulder\w*|pyjama\w*|draught\w*|sceptic\w*|anaesthe\w*|haemo\w*|oestr\w*|foetus|paediatric\w*|orthopaedic\w*|encyclopaedi\w*|mediaeval)\b"
total = kept = 0
for fn in sys.argv[1:]:
    for n, line in enumerate(open(fn, encoding="utf-8"), 1):
        for m in re.finditer(PAT, line, re.I):
            w = m.group(0)
            if w.lower().startswith("judgement") and w.lower() in ("judgement", "judgements"):
                kept += 1; print("  KEPT  %s:%d  %s" % (fn.split('/')[-1], n, w)); continue
            total += 1
            print("  HIT   %s:%d  %s  | %s" % (fn.split('/')[-1], n, w, line.strip()[:140]))
print("British-form hits (excluding kept 'judgement'): %d ; kept 'judgement': %d" % (total, kept))
