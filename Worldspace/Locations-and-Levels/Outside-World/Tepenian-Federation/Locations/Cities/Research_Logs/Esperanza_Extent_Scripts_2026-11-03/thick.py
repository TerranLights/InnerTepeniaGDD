import sys, numpy as np, rasterio, pyproj
from rasterio.windows import from_bounds
path=sys.argv[1]; npz=sys.argv[2]
d=np.load(npz+"/hopebay_window.npz"); g=np.load(npz+"/hopebay_geo.npz"); r=np.load(npz+"/rema_win.npz"); q=np.load(npz+"/dem_derived.npz")
x0,y0=float(r["x0"]),float(r["y0"])
with rasterio.open(path) as ds:
    print(ds.crs,ds.res,ds.shape,ds.nodata,ds.dtypes)
    win=(x0-30000,y0-30000,x0+30000,y0+30000)
    w=from_bounds(*win,transform=ds.transform)
    T=ds.read(1,window=w,boundless=True,fill_value=-9999).astype("float32"); tf=ds.window_transform(w)
print(T.shape, "valid",(T>-9000).sum(), "range",T[T>-9000].min(),T[T>-9000].max())
n=1000
xs=x0-30000+60*(np.arange(n)+0.5); ys=y0+30000-60*(np.arange(n)+0.5); X,Y=np.meshgrid(xs,ys)
c=((X-tf.c)/500).astype(int); rr=((tf.f-Y)/500).astype(int)
c=np.clip(c,0,T.shape[1]-1); rr=np.clip(rr,0,T.shape[0]-1)
TH=T[rr,c]; TH=np.where(TH>-9000,TH,np.nan)
# classes consistent with area.py
v=d["v"]; li=d["landice"]; cnt=d["count"]; slope=q["slope"]; dem=q["dem"]; DLAT=q["DLAT"]; DLON=q["DLON"]
cv=((X-(x0-60000))/120).astype(int); rv=(((y0+60000)-Y)/120).astype(int)
V=v[rv,cv]; LI=li[rv,cv]; CN=cnt[rv,cv]
ice=(LI==1)&(CN>0)&(V>=0)&(V<5000)&~np.isnan(dem)&~np.isnan(TH)
fwd=pyproj.Transformer.from_crs(4326,3031,always_xy=True); ex,ey=fwd.transform(-(56+59.8/60),-(63+23.9/60)); R=np.hypot(X-ex,Y-ey)/1000
zones={"within 10 km of Esperanza Base":R<10,"within 20 km of Esperanza Base":R<20,
 "Tabarin region (63.41-63.66S, 57.17-56.55W)":(DLAT<=-63.41)&(DLAT>=-63.66)&(DLON>=-57.17)&(DLON<=-56.55)}
px=0.0036
for zn,zm in zones.items():
    m=ice&zm
    t=TH[m]
    print("\n%s (grounded ice %.0f km2, with thickness values)"%(zn,m.sum()*px))
    print("   ice thickness m: median %.0f  p10 %.0f  p25 %.0f  p75 %.0f  p90 %.0f  max %.0f"%(np.median(t),*np.percentile(t,[10,25,75,90]),t.max()))
    for lo,hi in [(0,50),(50,100),(100,200),(200,400),(400,1e9)]:
        print("   thickness %4d-%s m: %6.1f km2 (%2.0f%%)"%(lo,"inf" if hi>1e8 else int(hi),((t>=lo)&(t<hi)).sum()*px,100*((t>=lo)&(t<hi)).mean()))
    # combined with speed<20/50 and slope<6
    for sv,ss in [(20,6),(50,6)]:
        mm=m&(V<sv)&(slope<ss); tt=TH[mm]
        print("   speed<%d & slope<%d deg: %.1f km2; thickness median %.0f m, p10 %.0f, p90 %.0f; of that <50 m thick: %.1f km2"%(sv,ss,mm.sum()*px,np.median(tt),*np.percentile(tt,[10,90]),(tt<50).sum()*px))
# the 500 m source resolution: how many source cells in the 10 km zone
print("\nsource cells (500 m) within 10 km of Esperanza with thickness: ~%d"%int(((R<10)&ice).sum()*0.0036/0.25))
