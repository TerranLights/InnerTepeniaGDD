import rasterio, numpy as np, pyproj
from rasterio.windows import from_bounds
from scipy import ndimage as ndi
B="https://its-live-data.s3.amazonaws.com/velocity_mosaic/v2/static/cog/ITS_LIVE_velocity_120m_RGI19A_0000_v02_%s.tif"
fwd=pyproj.Transformer.from_crs(4326,3031,always_xy=True); inv=pyproj.Transformer.from_crs(3031,4326,always_xy=True)
pts=[fwd.transform(lo,la) for la in (-63.35,-64.35) for lo in (-59.2,-56.3)]
xs=[p[0] for p in pts]; ys=[p[1] for p in pts]; win=(min(xs),min(ys),max(xs),max(ys))
with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR",CPL_VSIL_CURL_ALLOWED_EXTENSIONS=".tif",GDAL_HTTP_MAX_RETRY="3"):
    with rasterio.open("/vsicurl/"+B%"landice") as ds:
        w=from_bounds(*win,transform=ds.transform); li=ds.read(1,window=w,boundless=True,fill_value=0); tf=ds.window_transform(w)
    with rasterio.open("/vsicurl/"+B%"floatingice") as ds:
        fl=ds.read(1,window=w,boundless=True,fill_value=0)
ny,nx=li.shape; res=120.0
print("window",li.shape,"grounded ice km2: %.0f  floating ice km2: %.0f"%((li==1).sum()*0.0144,(fl==1).sum()*0.0144))
X=tf.c+res*(np.arange(nx)+0.5); Y=tf.f-res*(np.arange(ny)+0.5); XX,YY=np.meshgrid(X,Y); LO,LA=inv.transform(XX,YY)
g=(li==1)
lab,nl=ndi.label(g); sizes=ndi.sum(g,lab,range(1,nl+1))*0.0144
for i in np.argsort(-sizes)[:6]:
    m=lab==i+1; print("grounded-ice component %d: %.0f km2, lat %.2f..%.2f, lon %.2f..%.2f"%(i+1,sizes[i],LA[m].min(),LA[m].max(),LO[m].min(),LO[m].max()))
def comp_at(la,lo):
    x,yv=fwd.transform(lo,la); c=int((x-tf.c)/res); r=int((tf.f-yv)/res); return lab[r,c]
cT=comp_at(-63.50,-56.95); 
# find James Ross ice cap: the component with most area south of -63.9 and east of -58.5
cands=[(sizes[i],i+1) for i in range(nl)]
cJ=None
for s,i in sorted(cands,reverse=True):
    m=lab==i; 
    if LA[m].mean()<-63.95 and LO[m].mean()>-58.6 and s>200: cJ=i; break
print("Tabarin/Trinity component:",cT,"| James Ross component:",cJ)
if cJ and cT and cJ!=cT:
    dT=ndi.distance_transform_edt(lab!=cT)*res/1000
    mJ=(lab==cJ); idx=np.unravel_index(np.argmin(np.where(mJ,dT,np.inf)),dT.shape)
    print("narrowest gap between the two GROUNDED-ICE masks: %.1f km at lat %.3f lon %.3f (rock outcrops between would make the water gap smaller)"%(dT[idx],LA[idx],LO[idx]))
    ex,ey=fwd.transform(-(56+59.8/60),-(63+23.9/60)); R=np.hypot(XX-ex,YY-ey)/1000
    print("Esperanza Base to nearest James Ross grounded ice: %.1f km"%R[mJ].min())
    # gap statistics along the channel: for each James Ross ice pixel within 40 km of Trinity ice, distance
    sel=mJ&(dT<40); print("James Ross ice pixels within 40 km of the Trinity-side ice: %d; their distance p5 %.1f median %.1f km"%(sel.sum(),np.percentile(dT[sel],5),np.median(dT[sel])))
