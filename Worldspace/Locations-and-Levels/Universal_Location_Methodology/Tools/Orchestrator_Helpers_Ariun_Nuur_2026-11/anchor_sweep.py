#!/usr/bin/env python3
"""Step 9 item 5: stale-anchor and span sweep. For every tracked file whose lines shifted mid-file since the run began (base
fb387f71^), list every citation by line number to that file inside the pass's own files, with the shift points, so each can be
re-checked against the file as it now stands. Prints only file names, line numbers and the citing line's first 160 chars."""
import subprocess,re,glob,os
G="/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/"
P=G+"Worldspace/Locations-and-Levels/Outside-World/Tepenian-Federation/Locations/Cities/City_Development_Passes/Mirny_Subnet/Ariun_Nuur/"
base="fb387f71^"
os.chdir(G)
files=[x for x in subprocess.run(["git","diff","--name-only",base],capture_output=True,text=True).stdout.split("\n") if x]
shifted={}
for f in files:
    if "/Mirny_Subnet/" in f and "/Ariun_Nuur/" not in f: continue   # never another city's files
    if "/Mawson_Subnet/" in f: continue
    d=subprocess.run(["git","diff","-U0",base,"--",f],capture_output=True,text=True).stdout
    oldlen=subprocess.run(["git","show",f"{base}:{f}"],capture_output=True,text=True).stdout.count("\n")
    pts=[]
    for m in re.finditer(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@",d,re.M):
        os_,oc,ns,nc=int(m.group(1)),int(m.group(2) or 1),int(m.group(3)),int(m.group(4) or 1)
        if oc!=nc and os_<oldlen: pts.append((os_,nc-oc))
    if pts: shifted[f]=pts
citers=[p for p in glob.glob(P+"*.md")+glob.glob(P+"Datasheets/*.md") if not os.path.basename(p).startswith(".")]
for f,pts in shifted.items():
    b=os.path.basename(f); stem=b[:-3] if b.endswith(".md") else b
    keys={b,stem}
    print(f"=== {f}  shifts (old line, net lines): {pts}")
    n=0
    for c in sorted(citers):
        for i,l in enumerate(open(c,encoding="utf-8"),1):
            if not any(k in l for k in keys): continue
            for k in keys:
                for m in re.finditer(re.escape(k)+r"[^\n]{0,60}?\bL(\d+)",l):
                    ln=int(m.group(1))
                    if ln>=pts[0][0]:
                        n+=1; print(f"  {os.path.basename(c)}:{i}  cites L{ln}  | {l.strip()[:160]}")
    print(f"  ({n} citations at or past the first shift)")
