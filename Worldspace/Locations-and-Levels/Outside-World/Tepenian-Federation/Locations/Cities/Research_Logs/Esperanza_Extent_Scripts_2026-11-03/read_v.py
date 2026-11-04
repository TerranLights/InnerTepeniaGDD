import rasterio, numpy as np, pyproj, json, sys
from rasterio.windows import from_bounds
B="https://its-live-data.s3.amazonaws.com/velocity_mosaic/v2/static/cog/ITS_LIVE_velocity_120m_RGI19A_0000_v02_%s.tif"
tr=pyproj.Transformer.from_crs(4326,3031,always_xy=True)
lat0,lon0=-63.50,-57.0
x0,y0=tr.transform(lon0,lat0)
half=60000
win=(x0-half,y0-half,x0+half,y0+half)
out={}
with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR",CPL_VSIL_CURL_ALLOWED_EXTENSIONS=".tif",GDAL_HTTP_MAX_RETRY="3"):
    for k in ["v","v_error","count","landice","floatingice"]:
        with rasterio.open("/vsicurl/"+B%k) as ds:
            w=from_bounds(*win,transform=ds.transform)
            a=ds.read(1,window=w,boundless=True,fill_value=ds.nodata)
            out[k]=a; 
            if k=="v": tfm=ds.window_transform(w); nod=ds.nodata
np.savez("hopebay_window.npz",**out,x0=x0,y0=y0,half=half)
print({k:v.shape for k,v in out.items()})
v=out["v"]; ok=(v!=nod)&np.isfinite(v)
print("valid velocity pixels:",ok.sum(),"of",v.size, " v range:",np.nanmin(v[ok]),np.nanmax(v[ok]))
print("window transform:",tfm)
