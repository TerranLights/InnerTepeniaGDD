#!/usr/bin/env python3
"""Cross-match the raw station inventory against the 38 declared Tepenian cities by coordinates.
Reads Real_Station_Inventory_Raw.csv and the maps project's cities.csv (city coordinates = the specs' `Based on:` coordinates).
Writes Real_Station_Inventory_Crossmatched.csv (adds nearest_city, nearest_city_km, city_match_class) and prints a summary.
city_match_class: AT_CITY (<=25 km) | NEAR_CITY (25-100 km) | CANDIDATE (>100 km) | NO_COORDS
Pure arithmetic; decides nothing. Thresholds are reading aids only."""
import csv, math, collections, os
HERE=os.path.dirname(os.path.abspath(__file__)); D=os.path.dirname(HERE)
CITIES="/home/kuroskalacs/Documents/Doll-Fi/media/games/Inner Tepenia/InnerTepeniaGDD/Reference/Images/Maps/working-stash/data/cities.csv"
def gc(a,b,c,d):
    R=6371.0088; p1,p2=math.radians(a),math.radians(c); dl=math.radians(d-b)
    h=math.sin((p2-p1)/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*R*math.asin(math.sqrt(h))
cities=[(r['name'],float(r['lat']),float(r['lon'])) for r in csv.DictReader(open(CITIES,encoding='utf8'))]
rows=list(csv.DictReader(open(os.path.join(D,'Real_Station_Inventory_Raw.csv'),encoding='utf8')))
out=[]; cnt=collections.Counter()
for r in rows:
    try: la,lo=float(r['latitude']),float(r['longitude'])
    except: r.update(nearest_city='unknown',nearest_city_km='',city_match_class='NO_COORDS'); out.append(r); cnt['NO_COORDS']+=1; continue
    best=min(((gc(la,lo,cl,co),n) for n,cl,co in cities))
    k=best[0]; cls='AT_CITY' if k<=25 else ('NEAR_CITY' if k<=100 else 'CANDIDATE')
    r.update(nearest_city=best[1],nearest_city_km='%.1f'%k,city_match_class=cls); out.append(r); cnt[cls]+=1
fn=list(rows[0].keys())+['nearest_city','nearest_city_km','city_match_class']
w=csv.DictWriter(open(os.path.join(D,'Real_Station_Inventory_Crossmatched.csv'),'w',encoding='utf8',newline=''),fieldnames=fn); w.writeheader(); w.writerows(out)
print('rows',len(out),dict(cnt))
# candidate breakdown
for cls in ('AT_CITY','NEAR_CITY','CANDIDATE'):
    sub=[r for r in out if r['city_match_class']==cls]
    print('\n==',cls,len(sub)); print(' type  ',dict(collections.Counter(r['type'] for r in sub)))
    print(' status',dict(collections.Counter(r['status'] for r in sub)))
    print(' stab  ',dict(collections.Counter(r['stability_flag'] for r in sub)))
# per city: stations AT_CITY
at=collections.defaultdict(list)
for r in out:
    if r['city_match_class']=='AT_CITY': at[r['nearest_city']].append(r['name'])
print('\nCities with a station within 25 km:',len(at),'of',len(cities)); 
print('Cities with NO station within 25 km:',[n for n,_,_ in cities if n not in at])
