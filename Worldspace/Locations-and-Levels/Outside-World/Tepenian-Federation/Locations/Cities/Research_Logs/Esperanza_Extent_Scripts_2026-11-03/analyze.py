import numpy as np, pyproj
d=np.load("hopebay_window.npz"); v=d["v"]; li=d["landice"]; cnt=d["count"]; err=d["v_error"]
x0,y0,half=float(d["x0"]),float(d["y0"]),float(d["half"]); n=1000; px=120.0
xs=x0-half+px*(np.arange(n)+0.5); ys=y0+half-px*(np.arange(n)+0.5)
X,Y=np.meshgrid(xs,ys)
inv=pyproj.Transformer.from_crs(3031,4326,always_xy=True)
LON,LAT=inv.transform(X,Y); np.savez("hopebay_geo.npz",LAT=LAT.astype("float32"),LON=LON.astype("float32"))
fwd=pyproj.Transformer.from_crs(4326,3031,always_xy=True)
ice=(li==1)&(cnt>0)&(v>=0)&(v<5000)
def stats(mask,label):
    m=mask&ice
    if m.sum()==0: print("%-52s no land-ice pixels"%label); return
    vv=v[m]; a=m.sum()*px*px/1e6
    print("%-52s area %7.1f km2 | median %6.1f | p25 %6.1f p75 %6.1f p90 %6.1f | <10: %3.0f%%  <20: %3.0f%%  <50: %3.0f%%  >=100: %3.0f%%"%(label,a,np.median(vv),*np.percentile(vv,[25,75,90]),100*(vv<10).mean(),100*(vv<20).mean(),100*(vv<50).mean(),100*(vv>=100).mean()))
# Esperanza Base ~ 63°23.9'S 56°59.8'W (Hope Bay, NE end)
ex,ey=fwd.transform(-(56+59.8/60),-(63+23.9/60))
R=np.hypot(X-ex,Y-ey)/1000
print("Esperanza Base at x,y =",round(ex),round(ey)," grid check lat/lon:", )
print("--- grounded ice by distance from Esperanza Base (km)")
for a,b in [(0,3),(3,6),(6,10),(10,15),(15,20),(20,30),(30,45)]:
    stats((R>=a)&(R<b),"  ring %2d-%2d km"%(a,b))
stats(R<10,"  within 10 km"); stats(R<20,"  within 20 km")
print("--- boxes (lat/lon, approximate named areas)")
def box(lat0,lat1,lon0,lon1): return (LAT<=lat0)&(LAT>=lat1)&(LON>=lon0)&(LON<=lon1)
stats(box(-63.40,-63.46,-57.15,-56.85),"  Hope Bay head / Depot Glacier terminus zone")
stats(box(-63.46,-63.60,-57.20,-56.80),"  isthmus / central Tabarin ice (63.46-63.60S)")
stats(box(-63.48,-63.62,-57.05,-56.75),"  Tabarin east half (Cape Green side)")
stats(box(-63.40,-63.66,-57.30,-56.70),"  whole Tabarin box 63.40-63.66S, 57.30-56.70W")
stats(box(-63.66,-63.80,-57.4,-56.7),"  south of Duse Bay (Mott Snowfield side)")
print("--- speed profile along the meridian 57.0W, land ice only, lat bands of 0.05 deg")
for la in np.arange(-63.35,-63.80,-0.05):
    stats(box(la,la-0.05,-57.05,-56.95),"  lat %.2f..%.2f, 57.05-56.95W"%(la,la-0.05))
