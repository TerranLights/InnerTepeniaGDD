import numpy as np, pyproj
d=np.load("hopebay_window.npz"); e=np.load("hopebay_extra.npz"); g=np.load("hopebay_geo.npz")
v=d["v"]; li=d["landice"]; cnt=d["count"]; verr=d["v_error"]; v21=e["v21"]; amp=e["v_amp"]; dvdt=e["dv_dt"]
LAT,LON=g["LAT"],g["LON"]; x0,y0,half=float(d["x0"]),float(d["y0"]),float(d["half"]); n=1000; px=120.0
xs=x0-half+px*(np.arange(n)+0.5); ys=y0+half-px*(np.arange(n)+0.5); X,Y=np.meshgrid(xs,ys)
fwd=pyproj.Transformer.from_crs(4326,3031,always_xy=True); ex,ey=fwd.transform(-(56+59.8/60),-(63+23.9/60)); R=np.hypot(X-ex,Y-ey)/1000
ice=(li==1)&(cnt>0)&(v>=0)&(v<5000)
def box(lat0,lat1,lon0,lon1): return (LAT<=lat0)&(LAT>=lat1)&(LON>=lon0)&(LON<=lon1)
zones={"within 10 km of Esperanza":R<10,"within 20 km of Esperanza":R<20,"Tabarin box 63.40-63.66S 57.30-56.70W":box(-63.40,-63.66,-57.30,-56.70),"central Tabarin ice 63.46-63.60S":box(-63.46,-63.60,-57.20,-56.80),"Hope Bay head zone":box(-63.40,-63.46,-57.15,-56.85)}
print("version check on grounded ice (v2 vs v2.1), valid in both:")
ok=ice&(v21>=0)&(v21<5000)
print("  pixels",int(ok.sum())," median v2 %.1f  median v2.1 %.1f  median |diff| %.2f m/yr  p95 |diff| %.2f"%(np.median(v[ok]),np.median(v21[ok]),np.median(np.abs(v[ok]-v21[ok])),np.percentile(np.abs(v[ok]-v21[ok]),95)))
print("\nper zone (v2): speed / reported error / seasonal amplitude / trend 2014-2022")
for nm,m in zones.items():
    mm=m&ice
    a=mm&(amp<1000)&(amp>=0); t=mm&(dvdt>-1000)&(dvdt<1000)&(dvdt!=-32767)
    er=mm&(verr>=0)&(verr<1000)
    print(" %-40s n=%6d  median v %5.1f | median stated error %4.1f | seasonal amp median %4.1f (p90 %4.1f) | dv/dt median %+5.2f m/yr^2 (p10 %+5.2f p90 %+5.2f)"%(nm,mm.sum(),np.median(v[mm]),np.median(verr[er]) if er.any() else float('nan'),np.median(amp[a]) if a.any() else float('nan'),np.percentile(amp[a],90) if a.any() else float('nan'),np.median(dvdt[t]) if t.any() else float('nan'),*(np.percentile(dvdt[t],[10,90]) if t.any() else (float('nan'),)*2)))
    print("     v2.1 median %.1f ; observation count median %d"%(np.median(v21[mm&(v21>=0)&(v21<5000)]),np.median(cnt[mm])))
# displacement per century for typical speeds
print("\nDisplacement per century at speed s:", {s:"%.1f km"%(s*100/1000) for s in (5,10,15,20,50,100)})
