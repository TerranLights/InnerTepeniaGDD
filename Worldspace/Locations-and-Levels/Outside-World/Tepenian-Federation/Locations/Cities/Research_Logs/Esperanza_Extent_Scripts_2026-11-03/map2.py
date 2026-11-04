import numpy as np, pyproj
d=np.load("hopebay_window.npz"); g=np.load("hopebay_geo.npz"); r=np.load("rema_win.npz")
v=d["v"]; li=d["landice"]; cnt=d["count"]; LAT,LON=g["LAT"],g["LON"]
dem=r["dem"]; x0,y0=float(r["x0"]),float(r["y0"]); n=1000
# DEM grid (60 m, 60 km window centered at x0,y0)
xs=x0-30000+60*(np.arange(n)+0.5); ys=y0+30000-60*(np.arange(n)+0.5); X,Y=np.meshgrid(xs,ys)
inv=pyproj.Transformer.from_crs(3031,4326,always_xy=True); DLON,DLAT=inv.transform(X,Y)
demv=np.where(dem>-9000,dem,np.nan)
# slope in degrees on 60 m grid
gy,gx=np.gradient(np.nan_to_num(demv,nan=0.0),60.0)
slope=np.degrees(np.arctan(np.hypot(gx,gy))); slope[np.isnan(demv)]=np.nan
np.savez("dem_derived.npz",slope=slope,DLAT=DLAT.astype("float32"),DLON=DLON.astype("float32"),dem=demv)
# sample function at lat/lon on velocity grid
fwd=pyproj.Transformer.from_crs(4326,3031,always_xy=True)
def vel_at(lat,lon,half=450):  # median over ~0.9 km cell
    x,y=fwd.transform(lon,lat); c=int((x-(x0-60000))/120); rr=int(((y0+60000)-y)/120)
    sl=(slice(max(rr-4,0),rr+5),slice(max(c-4,0),c+5)); l=li[sl]; cc=cnt[sl]; vv=v[sl]
    m=(l==1)&(cc>0)&(vv>=0)&(vv<5000)
    if (l==1).mean()<0.4: return None
    return np.median(vv[m]) if m.any() else None
def dem_at(lat,lon):
    x,y=fwd.transform(lon,lat); c=int((x-(x0-30000))/60); rr=int(((y0+30000)-y)/60)
    if not(4<=c<n-4 and 4<=rr<n-4): return None
    a=demv[rr-4:rr+5,c-4:c+5]; return None if np.isnan(a).mean()>0.5 else np.nanmedian(a)
lats=np.arange(-63.34,-63.78,-0.016); lons=np.arange(-57.55,-56.45,0.0185)
print("MAP A: median surface speed (tens of m/yr; 0=<10 ... 9=90-99, A=100-199, B=200+) on grounded ice;  '.'=not grounded ice")
print("       columns W->E from %.2fW to %.2fW; rows N->S; cell ~1.3 km x 1.8 km;  H = Hope Bay head (Esperanza)"%(-lons[0],-lons[-1]))
ex,ey=-(56+59.8/60),-(63+23.9/60)
def sym(s): 
    if s is None: return "."
    return "0123456789"[int(s//10)] if s<100 else ("A" if s<200 else "B")
for la in lats:
    row=""
    for lo in lons:
        if abs(la-ey)<0.009 and abs(lo-ex)<0.01: row+="H"; continue
        row+=sym(vel_at(la,lo))
    print("%6.2fS %s"%(-la,row))
print("\nMAP B: surface elevation (hundreds of m; 0=<100 ... 9=900+; '.'=no DEM = water)")
for la in lats:
    row=""
    for lo in lons:
        e=dem_at(la,lo); row+="." if e is None else "0123456789"[min(9,int(e//100))]
    print("%6.2fS %s"%(-la,row))
