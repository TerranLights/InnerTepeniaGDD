import numpy as np, pyproj
d=np.load("hopebay_window.npz"); r=np.load("rema_win.npz"); q=np.load("dem_derived.npz")
v=d["v"]; li=d["landice"]; cnt=d["count"]; slope=q["slope"]; dem=q["dem"]; DLAT=q["DLAT"]; DLON=q["DLON"]
x0,y0=float(r["x0"]),float(r["y0"]); n=1000
xs=x0-30000+60*(np.arange(n)+0.5); ys=y0+30000-60*(np.arange(n)+0.5); X,Y=np.meshgrid(xs,ys)
c=((X-(x0-60000))/120).astype(int); rr=(((y0+60000)-Y)/120).astype(int)
V=v[rr,c]; LI=li[rr,c]; CN=cnt[rr,c]
ice=(LI==1)&(CN>0)&(V>=0)&(V<5000)&~np.isnan(dem)
fwd=pyproj.Transformer.from_crs(4326,3031,always_xy=True); ex,ey=fwd.transform(-(56+59.8/60),-(63+23.9/60)); R=np.hypot(X-ex,Y-ey)/1000
pxkm2=0.06*0.06
zones={"within 10 km of Esperanza Base":R<10,"within 20 km of Esperanza Base":R<20,
 "Tabarin region (63.41-63.66S, 57.17-56.55W)":(DLAT<=-63.41)&(DLAT>=-63.66)&(DLON>=-57.17)&(DLON<=-56.55)}
sp=[(0,10,"<10"),(10,20,"10-20"),(20,50,"20-50"),(50,1e9,">=50")]
sl=[(0,3,"<3"),(3,6,"3-6"),(6,10,"6-10"),(10,90,">=10")]
print("Area of grounded ice (km2) by speed (m/yr, rows) and slope (deg, columns)  -- 60 m cells")
for zn,zm in zones.items():
    m=ice&zm
    print("\n%s: grounded ice %.0f km2 | elevation median %.0f m (p10 %.0f, p90 %.0f) | slope median %.1f deg"%(zn,m.sum()*pxkm2,np.nanmedian(dem[m]),*np.nanpercentile(dem[m],[10,90]),np.nanmedian(slope[m])))
    print("   speed \\ slope  "+"  ".join("%7s"%s[2] for s in sl)+"    total")
    for a,b,lab in sp:
        row=[(m&(V>=a)&(V<b)&(slope>=s0)&(slope<s1)).sum()*pxkm2 for s0,s1,_ in sl]
        print("   %-12s "%lab+"  ".join("%7.1f"%x for x in row)+"  %7.1f"%sum(row))
    tot=m.sum()*pxkm2
    for sv,ss in [(20,6),(20,10),(50,6),(50,10),(1e9,6),(1e9,10)]:
        a=(m&(V<sv)&(slope<ss)).sum()*pxkm2
        print("   speed<%s & slope<%d deg: %6.1f km2 (%2.0f%% of the zone's ice)"%("any" if sv>1e8 else int(sv),ss,a,100*a/tot))
print("\nArea needed for 1,200,000 people at 7,000-10,000 per km2: %.0f - %.0f km2"%(1.2e6/10000,1.2e6/7000))
print("Needed for Census II 753,159: %.0f - %.0f km2"%(753159/10000,753159/7000))
