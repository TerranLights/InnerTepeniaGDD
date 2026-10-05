#!/usr/bin/env python3
"""Add distance to the nearest Tepenian highway to the cross-matched inventory.
Highway lines come from the maps project (highway_geometry.csv: traced from the developer's sketch, georeferenced). main + spur lines.
Distance = point-to-polyline in a local equirectangular approximation (fine for a reading aid; the traced lines are +/- ~20 km).
Writes Real_Station_Inventory_Crossmatched.csv in place with nearest_highway and highway_km. Decides nothing."""
import csv, math, os, collections
HERE=os.path.dirname(os.path.abspath(__file__)); D=os.path.dirname(HERE)
GEOM="/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Images/Maps/working-stash/data/highway_geometry.csv"
lines=collections.defaultdict(list)
for r in csv.DictReader(open(GEOM,encoding='utf8')): lines[(r['line_id'],r['kind'],r['highway_id'])].append((int(r['seq']),float(r['lat']),float(r['lon'])))
for k in lines: lines[k].sort()
R=6371.0088
def seg_km(p,a,b):
    # local polar-ish projection around p: x east km, y north km
    def xy(q):
        return (math.radians(q[1]-p[1])*R*math.cos(math.radians((q[0]+p[0])/2)), math.radians(q[0]-p[0])*R)
    ax,ay=xy(a); bx,by=xy(b); dx,dy=bx-ax,by-ay; L=dx*dx+dy*dy
    t=0 if L==0 else max(0,min(1,-(ax*dx+ay*dy)/L)); return math.hypot(ax+t*dx,ay+t*dy)
rows=list(csv.DictReader(open(os.path.join(D,'Real_Station_Inventory_Crossmatched.csv'),encoding='utf8')))
for r in rows:
    try: p=(float(r['latitude']),float(r['longitude']))
    except: r['nearest_highway']='unknown'; r['highway_km']=''; continue
    best=(1e9,'')
    for (lid,kind,hid),pts in lines.items():
        for i in range(len(pts)-1):
            d=seg_km(p,pts[i][1:],pts[i+1][1:])
            if d<best[0]: best=(d,hid if kind=='main' else lid)
    r['nearest_highway']=best[1]; r['highway_km']='%.0f'%best[0]
fn=list(rows[0].keys()); 
for c in ('nearest_highway','highway_km'):
    if c not in fn: fn.append(c)
w=csv.DictWriter(open(os.path.join(D,'Real_Station_Inventory_Crossmatched.csv'),'w',encoding='utf8',newline=''),fieldnames=fn); w.writeheader(); w.writerows(rows)
cand=[r for r in rows if r['city_match_class'] in ('CANDIDATE','NEAR_CITY')]
print('rows',len(rows),'candidate+near',len(cand))
for hid in ('hwy37','hwy22','hwy175','hwy59','hwy7','hwy4','hwy110','hwy2','hwy183','hwy1','hwy7ext'):
    s=[r for r in cand if r['nearest_highway']==hid and float(r['highway_km'] or 9999)<=150 and r['type'] in ('station','field camp','hut-refuge','airfield','other')]
    print('\n%s: %d non-AWS locations within 150 km'%(hid,len(s)))
    for r in sorted(s,key=lambda r:float(r['highway_km']))[:14]: print('   %-28s %4s km  %-11s %-10s %s'%(r['name'][:28],r['highway_km'],r['type'][:11],r['status'][:10],r['stability_flag'][:10]))
